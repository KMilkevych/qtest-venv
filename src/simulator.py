from typing import Any, Literal
from qiskit import ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, QuantumError
from qiskit.circuit.library import IGate, XGate, YGate, ZGate
from qiskit.quantum_info.operators.channel import Kraus
from qiskit.circuit.library.generalized_gates import PauliGate, UnitaryGate
from qiskit.quantum_info import hellinger_distance

from custom_noise_models.tenerife import (
    AVG_TENERIFE,
    BEST_TENERIFE,
    WORST_TENERIFE,
    MEDIAN_TENERIFE,
)
from custom_noise_models.guadalupe import (
    AVG_GUADALUPE,
    BEST_GUADALUPE,
    WORST_GUADALUPE,
    MEDIAN_GUADALUPE,
)
from custom_noise_models.cambridge import (
    AVG_CAMBRIDGE,
    BEST_CAMBRIDGE,
    WORST_CAMBRIDGE,
    MEDIAN_CAMBRIDGE,
)

from qiskit.circuit import Reset
from numpy import array_equal

from circuits import (
    LogicalQubit,
    PhysicalQubit,
    make_final_mapping,
    with_swaps_as_cnots,
    fill_holes_with_id_gates,
)

ACCEPTED_PLATFORMS = ["tokyo", "tenerife", "cambridge", "guadalupe"]


def get_instr_groups(noise_model: NoiseModel):
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_gate_errors = [
        error for error in original_errors if error["type"] == "qerror"
    ]

    # GATE ERRORS
    instr_op_prob = []
    for error in original_gate_errors:
        instructions = error["instructions"]
        probabilities = error["probabilities"]
        instr_with_prob = list(zip(instructions, probabilities, strict=True))
        for instr, prob in instr_with_prob:
            instr_op_prob.append((instr, error["operations"], prob))

    groups = []

    while instr_op_prob:
        candidate = instr_op_prob.pop()
        group = [candidate]
        equal_indexes = []
        for i in range(len(instr_op_prob)):
            if i >= len(instr_op_prob):
                break

            candidate_instr = candidate[0]
            compare_instr = instr_op_prob[i][0]
            candidate_op = candidate[1]
            compare_op = instr_op_prob[i][1]

            if candidate_op != compare_op:
                continue

            candidate_contains_kraus = any(
                [part["name"] == "kraus" for part in candidate_instr]
            )
            compare_contains_kraus = any(
                [part["name"] == "kraus" for part in compare_instr]
            )

            if candidate_contains_kraus and not compare_contains_kraus:
                continue

            if not candidate_contains_kraus and compare_contains_kraus:
                continue

            if (
                not candidate_contains_kraus
                and not compare_contains_kraus
                and candidate_instr != compare_instr
            ):
                continue

            if (
                not candidate_contains_kraus
                and not compare_contains_kraus
                and candidate_instr == compare_instr
            ):
                equal_indexes.append(i)
                continue

            kraus_instr_appears_at_same_index = [
                part["name"] == "kraus" for part in candidate_instr
            ] == [part["name"] == "kraus" for part in compare_instr]

            if not kraus_instr_appears_at_same_index:
                continue

            candidate_non_kraus_parts = [
                part for part in candidate_instr if part["name"] != "kraus"
            ]
            compare_non_kraus_parts = [
                part for part in compare_instr if part["name"] != "kraus"
            ]

            if candidate_non_kraus_parts != compare_non_kraus_parts:
                continue

            candidate_kraus_parts = [
                part for part in candidate_instr if part["name"] == "kraus"
            ]
            compare_kraus_parts = [
                part for part in compare_instr if part["name"] == "kraus"
            ]

            comparing = zip(candidate_kraus_parts, compare_kraus_parts)
            all_equal = True
            for candidate_kraus_part, compare_kraus_part in comparing:
                qubits_equal = (
                    candidate_kraus_part["qubits"] == compare_kraus_part["qubits"]
                )
                # params are numpy arrays, hence we need to check that all elements are equal
                params_equal = array_equal(
                    candidate_kraus_part["params"], compare_kraus_part["params"]
                )

                if qubits_equal and params_equal:
                    continue
                else:
                    all_equal = False
                    break

            if all_equal:
                equal_indexes.append(i)

        for index in equal_indexes:
            group.append(instr_op_prob[index])

        for member in group[1:]:
            instr_op_prob.remove(member)

        groups.append(group)

    return groups


def average_noise_model(
    noise_model: NoiseModel, num_of_qubits: int, num_of_edges_in_coupling_map: int
) -> NoiseModel:
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]

    average_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

    groups = get_instr_groups(noise_model)

    op_to_instr_prob = {}
    for group in groups:
        instr = group[0][0]
        ops = group[0][1]
        if len(ops) > 1:
            raise ValueError("Multiple operations in a group")
        op = ops[0]

        probs = [member[2] for member in group]

        if op == "cx":
            avg_prob = sum(probs) / num_of_edges_in_coupling_map
        else:
            avg_prob = sum(probs) / num_of_qubits

        if op not in op_to_instr_prob:
            op_to_instr_prob[op] = [(instr, avg_prob)]
        else:
            op_to_instr_prob[op].append((instr, avg_prob))

    for op, instr_prob in op_to_instr_prob.items():
        noise_ops = []
        for instr, prob in instr_prob:
            noise_elem = []
            for part in instr:
                name = part["name"]
                qubits = part["qubits"]
                match name:
                    case "id":
                        noise_elem.append((IGate(), qubits))
                    case "x":
                        noise_elem.append((XGate(), qubits))
                    case "y":
                        noise_elem.append((YGate(), qubits))
                    case "z":
                        noise_elem.append((ZGate(), qubits))
                    case "kraus":
                        params = part["params"]
                        noise_elem.append((Kraus(params), qubits))
                    case "reset":
                        noise_elem.append((Reset(), qubits))
                    case "unitary":
                        params = part["params"][0]
                        noise_elem.append((UnitaryGate(params), qubits))
                    case "pauli":
                        params = part["params"][0]
                        noise_elem.append((PauliGate(params), qubits))
                    case _:
                        raise ValueError(f"Unknown instruction: '{name}'")

            noise_ops.append((noise_elem, prob))

        error = QuantumError(noise_ops)
        average_noise_model.add_all_qubit_quantum_error(error, [op])

    # READOUT ERROR
    average_readout_error = [[0.0, 0.0], [0.0, 0.0]]
    for error in original_readout_errors:
        average_readout_error[0][0] += error["probabilities"][0][0]
        average_readout_error[0][1] += error["probabilities"][0][1]
        average_readout_error[1][0] += error["probabilities"][1][0]
        average_readout_error[1][1] += error["probabilities"][1][1]
    average_readout_error[0][0] /= num_of_qubits
    average_readout_error[0][1] /= num_of_qubits
    average_readout_error[1][0] /= num_of_qubits
    average_readout_error[1][1] /= num_of_qubits

    average_noise_model.add_all_qubit_readout_error(average_readout_error)

    return average_noise_model


def best_noise_model(
    noise_model: NoiseModel, num_of_qubits: int, num_of_edges_in_coupling_map: int
):
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]

    best_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

    groups = get_instr_groups(noise_model)

    op_to_instr_prob = {}
    for group in groups:
        instr = group[0][0]
        ops = group[0][1]
        if len(ops) > 1:
            raise ValueError("Multiple operations in a group")
        op = ops[0]

        probs = [member[2] for member in group]

        instr_has_1_part = len(instr) == 1
        instr_is_id = instr[0]["name"] == "id"
        instr_is_pauli_id = (
            instr[0]["name"] == "pauli" and instr[0]["params"][0] == "II"
        )

        if instr_has_1_part and (instr_is_id or instr_is_pauli_id):
            best_prob = max(probs)
        elif op == "cx":
            best_prob = sum(probs) / num_of_edges_in_coupling_map
        else:
            best_prob = sum(probs) / num_of_qubits

        if op not in op_to_instr_prob:
            op_to_instr_prob[op] = [(instr, best_prob)]
        else:
            op_to_instr_prob[op].append((instr, best_prob))

    for op, instr_prob in op_to_instr_prob.items():
        noise_ops = []
        for instr, prob in instr_prob:
            noise_elem = []
            for part in instr:
                name = part["name"]
                qubits = part["qubits"]
                match name:
                    case "id":
                        noise_elem.append((IGate(), qubits))
                    case "x":
                        noise_elem.append((XGate(), qubits))
                    case "y":
                        noise_elem.append((YGate(), qubits))
                    case "z":
                        noise_elem.append((ZGate(), qubits))
                    case "kraus":
                        params = part["params"]
                        noise_elem.append((Kraus(params), qubits))
                    case "reset":
                        noise_elem.append((Reset(), qubits))
                    case "unitary":
                        params = part["params"][0]
                        noise_elem.append((UnitaryGate(params), qubits))
                    case "pauli":
                        params = part["params"][0]
                        noise_elem.append((PauliGate(params), qubits))
                    case _:
                        raise ValueError(f"Unknown instruction: '{name}'")

            noise_ops.append((noise_elem, prob))

        # Normalization
        is_id = lambda gate: isinstance(gate, IGate)
        is_pauli_id = (
            lambda gate: isinstance(gate, PauliGate) and gate.params[0] == "II"
        )

        id_ops = [
            (gate, prob) for gate, prob in noise_ops if is_id(gate) or is_pauli_id(gate)
        ]
        noise_ops = [
            (gate, prob)
            for gate, prob in noise_ops
            if not is_id(gate) and not is_pauli_id(gate)
        ]

        id_prob = sum([prob for _, prob in id_ops])
        noise_prob = sum([prob for _, prob in noise_ops])
        noise_ops_normalized = [
            (gate, prob * (1 - id_prob) / noise_prob) for gate, prob in noise_ops
        ]

        error = QuantumError(id_ops + noise_ops_normalized)
        best_noise_model.add_all_qubit_quantum_error(error, [op])

    # READOUT ERROR
    best_readout_error = [[0.0, 0.0], [0.0, 0.0]]
    for error in original_readout_errors:
        if error["probabilities"][0][0] > best_readout_error[0][0]:
            best_readout_error[0][0] = error["probabilities"][0][0]
            best_readout_error[0][1] = error["probabilities"][0][1]
            best_readout_error[1][0] = error["probabilities"][1][0]
            best_readout_error[1][1] = error["probabilities"][1][1]

    best_noise_model.add_all_qubit_readout_error(best_readout_error)

    return best_noise_model


def worst_noise_model(
    noise_model: NoiseModel, num_of_qubits: int, num_of_edges_in_coupling_map: int
):
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]

    worst_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

    groups = get_instr_groups(noise_model)

    op_to_instr_prob = {}
    for group in groups:
        instr = group[0][0]
        ops = group[0][1]
        if len(ops) > 1:
            raise ValueError("Multiple operations in a group")
        op = ops[0]

        probs = [member[2] for member in group]

        instr_has_1_part = len(instr) == 1
        instr_is_id = instr[0]["name"] == "id"
        instr_is_pauli_id = (
            instr[0]["name"] == "pauli" and instr[0]["params"][0] == "II"
        )

        if instr_has_1_part and (instr_is_id or instr_is_pauli_id):
            worst_prob = min(probs)
        elif op == "cx":
            worst_prob = sum(probs) / num_of_edges_in_coupling_map
        else:
            worst_prob = sum(probs) / num_of_qubits

        if op not in op_to_instr_prob:
            op_to_instr_prob[op] = [(instr, worst_prob)]
        else:
            op_to_instr_prob[op].append((instr, worst_prob))

    for op, instr_prob in op_to_instr_prob.items():
        noise_ops = []
        for instr, prob in instr_prob:
            noise_elem = []
            for part in instr:
                name = part["name"]
                qubits = part["qubits"]
                match name:
                    case "id":
                        noise_elem.append((IGate(), qubits))
                    case "x":
                        noise_elem.append((XGate(), qubits))
                    case "y":
                        noise_elem.append((YGate(), qubits))
                    case "z":
                        noise_elem.append((ZGate(), qubits))
                    case "kraus":
                        params = part["params"]
                        noise_elem.append((Kraus(params), qubits))
                    case "reset":
                        noise_elem.append((Reset(), qubits))
                    case "unitary":
                        params = part["params"][0]
                        noise_elem.append((UnitaryGate(params), qubits))
                    case "pauli":
                        params = part["params"][0]
                        noise_elem.append((PauliGate(params), qubits))
                    case _:
                        raise ValueError(f"Unknown instruction: '{name}'")

            noise_ops.append((noise_elem, prob))

        # Normalization
        is_id = lambda gate: isinstance(gate, IGate)
        is_pauli_id = (
            lambda gate: isinstance(gate, PauliGate) and gate.params[0] == "II"
        )

        id_ops = [
            (gate, prob) for gate, prob in noise_ops if is_id(gate) or is_pauli_id(gate)
        ]
        noise_ops = [
            (gate, prob)
            for gate, prob in noise_ops
            if not is_id(gate) and not is_pauli_id(gate)
        ]

        id_prob = sum([prob for _, prob in id_ops])
        noise_prob = sum([prob for _, prob in noise_ops])
        noise_ops_normalized = [
            (gate, prob * (1 - id_prob) / noise_prob) for gate, prob in noise_ops
        ]

        error = QuantumError(id_ops + noise_ops_normalized)
        worst_noise_model.add_all_qubit_quantum_error(error, [op])

    # READOUT ERROR
    worst_readout_error = [[1.0, 0.0], [0.0, 1.0]]
    for error in original_readout_errors:
        if error["probabilities"][0][0] < worst_readout_error[0][0]:
            worst_readout_error[0][0] = error["probabilities"][0][0]
            worst_readout_error[0][1] = error["probabilities"][0][1]
            worst_readout_error[1][0] = error["probabilities"][1][0]
            worst_readout_error[1][1] = error["probabilities"][1][1]

    worst_noise_model.add_all_qubit_readout_error(worst_readout_error)

    return worst_noise_model


def median_noise_model(
    noise_model: NoiseModel, num_of_qubits: int, num_of_edges_in_coupling_map: int
):
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]

    median_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

    groups = get_instr_groups(noise_model)

    op_to_instr_prob = {}
    for group in groups:
        instr = group[0][0]
        ops = group[0][1]
        if len(ops) > 1:
            raise ValueError("Multiple operations in a group")
        op = ops[0]

        probs = [member[2] for member in group]

        instr_has_1_part = len(instr) == 1
        instr_is_id = instr[0]["name"] == "id"
        instr_is_pauli_id = (
            instr[0]["name"] == "pauli" and instr[0]["params"][0] == "II"
        )

        if instr_has_1_part and (instr_is_id or instr_is_pauli_id):
            num_of_probs = len(probs)
            middle_index = num_of_probs // 2
            median_prob = sorted(probs)[middle_index]
        elif op == "cx":
            median_prob = sum(probs) / num_of_edges_in_coupling_map
        else:
            median_prob = sum(probs) / num_of_qubits

        if op not in op_to_instr_prob:
            op_to_instr_prob[op] = [(instr, median_prob)]
        else:
            op_to_instr_prob[op].append((instr, median_prob))

    for op, instr_prob in op_to_instr_prob.items():
        noise_ops = []
        for instr, prob in instr_prob:
            noise_elem = []
            for part in instr:
                name = part["name"]
                qubits = part["qubits"]
                match name:
                    case "id":
                        noise_elem.append((IGate(), qubits))
                    case "x":
                        noise_elem.append((XGate(), qubits))
                    case "y":
                        noise_elem.append((YGate(), qubits))
                    case "z":
                        noise_elem.append((ZGate(), qubits))
                    case "kraus":
                        params = part["params"]
                        noise_elem.append((Kraus(params), qubits))
                    case "reset":
                        noise_elem.append((Reset(), qubits))
                    case "unitary":
                        params = part["params"][0]
                        noise_elem.append((UnitaryGate(params), qubits))
                    case "pauli":
                        params = part["params"][0]
                        noise_elem.append((PauliGate(params), qubits))
                    case _:
                        raise ValueError(f"Unknown instruction: '{name}'")

            noise_ops.append((noise_elem, prob))

        # Normalization
        is_id = lambda gate: isinstance(gate, IGate)
        is_pauli_id = (
            lambda gate: isinstance(gate, PauliGate) and gate.params[0] == "II"
        )

        id_ops = [
            (gate, prob) for gate, prob in noise_ops if is_id(gate) or is_pauli_id(gate)
        ]
        noise_ops = [
            (gate, prob)
            for gate, prob in noise_ops
            if not is_id(gate) and not is_pauli_id(gate)
        ]

        id_prob = sum([prob for _, prob in id_ops])
        noise_prob = sum([prob for _, prob in noise_ops])
        noise_ops_normalized = [
            (gate, prob * (1 - id_prob) / noise_prob) for gate, prob in noise_ops
        ]

        error = QuantumError(id_ops + noise_ops_normalized)
        median_noise_model.add_all_qubit_quantum_error(error, [op])

    # READOUT ERROR
    median_readout_error = [[1.0, 0.0], [0.0, 1.0]]
    readout_probs = [
        (
            error["probabilities"][0][0],
            error["probabilities"][1][0],
            error["probabilities"][0][1],
            error["probabilities"][1][1],
        )
        for error in original_readout_errors
    ]
    readout_probs.sort()
    num_of_readout_probs = len(readout_probs)
    middle_index = num_of_readout_probs // 2
    median_readout_error[0][0] = readout_probs[middle_index][0]
    median_readout_error[1][0] = readout_probs[middle_index][1]
    median_readout_error[0][1] = readout_probs[middle_index][2]
    median_readout_error[1][1] = readout_probs[middle_index][3]

    median_noise_model.add_all_qubit_readout_error(median_readout_error)

    return median_noise_model


def simulate_single(
    circuit: QuantumCircuit,
    platform: str,
    shots: int,
    noise_model_kind: Literal["average", "best", "worst", "median"],
    with_noise: bool = False,
    final_mapping: dict[LogicalQubit, PhysicalQubit] | None = None,
) -> dict[str, int] | None:
    """
    Given a quantum circuit, simulate it on the given platform with noise.

    Args
    ----
    - circuit (`QuantumCircuit`): The quantum circuit to simulate.
    - platform (`str`): The name of the platform to simulate the circuit on.
    - shots (`int`): The number of shots to simulate.
    - with_noise (`bool`): Whether to simulate with noise. Defaults to `False`.
    - final_mapping (`dict[LogicalQubit, PhysicalQubit] | None`): The final mapping of the circuit. If `None`, the circuit is measured in the active qubits. Defaults to `None`.

    Returns
    --------
    - `dict[str, int]`: A dictionary mapping inputs as bitstrings to the number of times they were measured.
    """

    match platform:
        case "tenerife":
            match noise_model_kind:
                case "average":
                    noise_model = NoiseModel.from_dict(AVG_TENERIFE)
                case "best":
                    noise_model = NoiseModel.from_dict(BEST_TENERIFE)
                case "worst":
                    noise_model = NoiseModel.from_dict(WORST_TENERIFE)
                case "median":
                    noise_model = NoiseModel.from_dict(MEDIAN_TENERIFE)

            noise_model._basis_gates = {"cx", "id", "u1", "u2", "u3"}
        case "cambridge":
            match noise_model_kind:
                case "average":
                    noise_model = NoiseModel.from_dict(AVG_CAMBRIDGE)
                case "best":
                    noise_model = NoiseModel.from_dict(BEST_CAMBRIDGE)
                case "worst":
                    noise_model = NoiseModel.from_dict(WORST_CAMBRIDGE)
                case "median":
                    noise_model = NoiseModel.from_dict(MEDIAN_CAMBRIDGE)
            noise_model._basis_gates = {"cx", "id", "u1", "u2", "u3"}
        case "guadalupe":
            match noise_model_kind:
                case "average":
                    noise_model = NoiseModel.from_dict(AVG_GUADALUPE)
                case "best":
                    noise_model = NoiseModel.from_dict(BEST_GUADALUPE)
                case "worst":
                    noise_model = NoiseModel.from_dict(WORST_GUADALUPE)
                case "median":
                    noise_model = NoiseModel.from_dict(MEDIAN_GUADALUPE)
            noise_model._basis_gates = {"cx", "id", "reset", "rz", "sx", "x"}
        case _:
            print(f"Error: Platform '{platform}' not supported.")
            exit(1)

    circuit_with_id_gates = fill_holes_with_id_gates(circuit)

    if not with_noise:
        noise_model = None

    if noise_model != None:
        for instr in circuit_with_id_gates.data:
            if instr.operation.name not in noise_model.basis_gates:
                return None

    if final_mapping == None:
        circuit_with_id_gates.measure_all()
    else:
        circuit_with_id_gates.barrier()
        register_size = len(final_mapping.keys())
        classical_register = ClassicalRegister(size=register_size, name="measure")
        circuit_with_id_gates.add_register(classical_register)
        sorted_final_mapping = sorted(final_mapping.items(), key=lambda x: x[0].id)
        for q, p in sorted_final_mapping:
            circuit_with_id_gates.measure(p.id, q.id)

    # Perform a noise simulation
    backend = AerSimulator(noise_model=noise_model, method="density_matrix")
    result = backend.run(circuit_with_id_gates, shots=shots).result()

    counts = result.get_counts(0)

    return counts  # type: ignore


def simulate(
    logical_circuit: QuantumCircuit,
    synthesized_circuit: QuantumCircuit,
    synthesized_initial_mapping: dict[LogicalQubit, PhysicalQubit],
    platform: str,
    shots: int,
    synthesized_with_anicillaries: bool = False,
) -> tuple[float | None, float | None, float | None, float | None]:
    """
    Simulate the synthesized circuit on the given platform with noise under all types of noise models ("average", "best", "worst" and "median").

    Args
    ----
    - logical_circuit (`QuantumCircuit`): The logical circuit to simulate.
    - synthesized_circuit (`QuantumCircuit`): The synthesized circuit to simulate.
    - synthesized_initial_mapping (`dict[LogicalQubit, PhysicalQubit]`): The initial mapping of the synthesized circuit.
    - platform (`str`): The name of the platform to simulate the circuit on.
    - shots (`int`): The number of shots to simulate.
    - synthesized_with_anicillaries (`bool`): Whether the synthesized circuit uses ancillary SWAPs. Defaults to `False`.

    Returns
    --------
    - `float`: Hellinger Distance.
    """

    logical_circuit_counts = simulate_single(
        logical_circuit,
        platform,
        shots,
        noise_model_kind="average",
        with_noise=False,
    )

    if logical_circuit_counts == None:
        return None, None, None, None

    synthesized_final_mapping = make_final_mapping(
        synthesized_circuit, synthesized_initial_mapping, synthesized_with_anicillaries
    )
    cx_for_swap_circuit = with_swaps_as_cnots(synthesized_circuit, "q")

    def sim_helper(
        kind: Literal["average", "best", "worst", "median"]
    ) -> dict[str, int] | None:
        return simulate_single(
            cx_for_swap_circuit,
            platform,
            shots,
            kind,
            with_noise=True,
            final_mapping=synthesized_final_mapping,
        )

    avg_synthesized_circuit_counts = sim_helper("average")
    best_synthesized_circuit_counts = sim_helper("best")
    worst_synthesized_circuit_counts = sim_helper("worst")
    median_synthesized_circuit_counts = sim_helper("median")

    avg_distance = (
        hellinger_distance(logical_circuit_counts, avg_synthesized_circuit_counts)
        if avg_synthesized_circuit_counts != None
        else None
    )
    best_distance = (
        hellinger_distance(logical_circuit_counts, best_synthesized_circuit_counts)
        if best_synthesized_circuit_counts != None
        else None
    )
    worst_distance = (
        hellinger_distance(logical_circuit_counts, worst_synthesized_circuit_counts)
        if worst_synthesized_circuit_counts != None
        else None
    )
    median_distance = (
        hellinger_distance(logical_circuit_counts, median_synthesized_circuit_counts)
        if median_synthesized_circuit_counts != None
        else None
    )

    return avg_distance, best_distance, worst_distance, median_distance
