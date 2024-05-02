from typing import Any
from qiskit import ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, QuantumError
from qiskit.circuit.library import IGate, XGate, YGate, ZGate
from qiskit.quantum_info.operators.channel import Kraus
from qiskit.circuit.library.generalized_gates import PauliGate, UnitaryGate
from qiskit.quantum_info import hellinger_distance
from avg_noise_models import AVG_TENERIFE, AVG_CAMBRIDGE, AVG_TOKYO, AVG_GUADALUPE
from qiskit.circuit import Reset
from numpy import array_equal

from circuits import (
    LogicalQubit,
    PhysicalQubit,
    make_final_mapping,
    with_swaps_as_cnots,
)

ACCEPTED_PLATFORMS = ["tokyo", "tenerife", "cambridge", "guadalupe"]


def average_noise_model(
    noise_model: NoiseModel, num_of_qubits: int, num_of_edges_in_coupling_map: int
) -> NoiseModel:
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_gate_errors = [
        error for error in original_errors if error["type"] == "qerror"
    ]

    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]

    average_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

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


def simulate_single(
    circuit: QuantumCircuit,
    platform: str,
    shots: int,
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
            noise_model = NoiseModel.from_dict(AVG_TENERIFE)
        case "tokyo":
            noise_model = NoiseModel.from_dict(AVG_TOKYO)
        case "cambridge":
            noise_model = NoiseModel.from_dict(AVG_CAMBRIDGE)
        case "guadalupe":
            noise_model = NoiseModel.from_dict(AVG_GUADALUPE)
        case _:
            print(f"Error: Platform '{platform}' not supported.")
            exit(1)

    if not with_noise:
        noise_model = None

    if noise_model != None:
        for instr in circuit.data:
            if instr.operation.name not in noise_model.basis_gates:
                return None

    if final_mapping == None:
        circuit.measure_all()
    else:
        circuit.barrier()
        register_size = len(final_mapping.keys())
        classical_register = ClassicalRegister(size=register_size, name="measure")
        circuit.add_register(classical_register)
        for q, p in final_mapping.items():
            circuit.measure(p.id, q.id)

    # Perform a noise simulation
    backend = AerSimulator(noise_model=noise_model)
    result = backend.run(circuit, shots=shots).result()

    counts = result.get_counts(0)

    return counts  # type: ignore


def simulate(
    logical_circuit: QuantumCircuit,
    synthesized_circuit: QuantumCircuit,
    synthesized_initial_mapping: dict[LogicalQubit, PhysicalQubit],
    platform: str,
    shots: int,
    synthesized_with_anicillaries: bool = False,
) -> float | None:
    """
    Simulate the synthesized circuit on the given platform with noise.

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
        with_noise=False,
    )

    synthesized_final_mapping = make_final_mapping(
        synthesized_circuit, synthesized_initial_mapping, synthesized_with_anicillaries
    )
    cx_for_swap_circuit = with_swaps_as_cnots(synthesized_circuit, "q")
    synthesized_circuit_counts = simulate_single(
        cx_for_swap_circuit,
        platform,
        shots,
        with_noise=True,
        final_mapping=synthesized_final_mapping,
    )

    if logical_circuit_counts == None or synthesized_circuit_counts == None:
        return None

    return hellinger_distance(logical_circuit_counts, synthesized_circuit_counts)
