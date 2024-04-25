from typing import Any
from qiskit import ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, QuantumError, pauli_error
from qiskit_ibm_runtime.fake_provider import FakeTenerife, FakeTokyo
from qiskit.circuit.library import IGate, XGate, YGate, ZGate

from circuits import (
    LogicalQubit,
    PhysicalQubit,
    make_final_mapping,
    with_swaps_as_cnots,
)

ACCEPTED_PLATFORMS = ["tokyo", "tenerife"]


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
            ibm_platform = FakeTenerife()
        case "tokyo":
            ibm_platform = FakeTokyo()
        case _:
            print(f"Error: Platform '{platform}' not supported.")
            exit(1)

    noise_model = (
        average_noise_model(NoiseModel.from_backend(ibm_platform))
        if with_noise
        else None
    )
    if noise_model != None:
        for instr in circuit.data:
            if instr.operation.name not in noise_model.basis_gates:
                return None

    if final_mapping == None:
        circuit.measure_active()
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


def process_counts(
    control_counts: dict[str, int],
    noise_counts: dict[str, int],
) -> tuple[int, int]:
    """
    Given two dictionaries of counts, return the number of correct and wrong measurements.

    Args
    ----
    - control_counts (`dict[str, int]`): The counts of the control circuit.
    - noise_counts (`dict[str, int]`): The counts of the noise circuit.

    Returns
    --------
    - `tuple[int, int]`: A tuple of the number of correct and wrong measurements respectively.
    """

    correct = 0
    wrong = 0
    for measurement, count in noise_counts.items():
        if measurement in control_counts.keys():
            correct += count
        else:
            wrong += count

    return correct, wrong


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
    - `float`: The percentage of correct measurements.
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

    correct, _ = process_counts(logical_circuit_counts, synthesized_circuit_counts)
    return correct / shots * 100


def average_noise_model(noise_model: NoiseModel) -> NoiseModel:
    original_errors: list[dict[str, Any]] = noise_model.to_dict()["errors"]

    original_cx_errors = [
        error
        for error in original_errors
        if error["type"] == "qerror" and error["operations"][0] == "cx"
    ]
    original_unary_gate_errors = [
        error
        for error in original_errors
        if error["type"] == "qerror" and error["operations"][0] != "cx"
    ]
    original_readout_errors = [
        error for error in original_errors if error["type"] == "roerror"
    ]
    num_of_qubits = len(original_readout_errors)

    if len(original_errors) != len(original_cx_errors) + len(
        original_unary_gate_errors
    ) + len(original_readout_errors):
        raise ValueError(
            "Original errors are not disjoint or they are incomplete. (Perhaps there are other binary gates that CX in the noise model?)"
        )

    average_noise_model = NoiseModel([instr for instr in noise_model.basis_gates])

    # UNARY GATE ERROR
    average_unary_gate_error = {}
    for error in original_unary_gate_errors:
        gate_name = error["operations"][0]
        if gate_name not in average_unary_gate_error:
            average_unary_gate_error[gate_name] = [0.0] * 4
        average_unary_gate_error[gate_name][0] += error["probabilities"][0]
        average_unary_gate_error[gate_name][1] += error["probabilities"][1]
        average_unary_gate_error[gate_name][2] += error["probabilities"][2]
        average_unary_gate_error[gate_name][3] += error["probabilities"][3]

    for gate_name in average_unary_gate_error:
        for i in range(4):
            average_unary_gate_error[gate_name][i] /= num_of_qubits

    for gate_name in average_unary_gate_error:
        average_noise_model.add_all_qubit_quantum_error(
            QuantumError(
                noise_ops=[
                    (IGate(), average_unary_gate_error[gate_name][0]),
                    (XGate(), average_unary_gate_error[gate_name][1]),
                    (YGate(), average_unary_gate_error[gate_name][2]),
                    (ZGate(), average_unary_gate_error[gate_name][3]),
                ],
            ),
            [gate_name],
        )

    # CX GATE ERROR
    average_cx_error = [0.0] * 16
    for error in original_cx_errors:
        average_cx_error[0] += error["probabilities"][0]
        average_cx_error[1] += error["probabilities"][1]
        average_cx_error[2] += error["probabilities"][2]
        average_cx_error[3] += error["probabilities"][3]
        average_cx_error[4] += error["probabilities"][4]
        average_cx_error[5] += error["probabilities"][5]
        average_cx_error[6] += error["probabilities"][6]
        average_cx_error[7] += error["probabilities"][7]
        average_cx_error[8] += error["probabilities"][8]
        average_cx_error[9] += error["probabilities"][9]
        average_cx_error[10] += error["probabilities"][10]
        average_cx_error[11] += error["probabilities"][11]
        average_cx_error[12] += error["probabilities"][12]
        average_cx_error[13] += error["probabilities"][13]
        average_cx_error[14] += error["probabilities"][14]
        average_cx_error[15] += error["probabilities"][15]

    for i in range(16):
        average_cx_error[i] /= len(original_cx_errors)

    average_noise_model.add_all_qubit_quantum_error(
        pauli_error(
            [
                ("II", average_cx_error[0]),
                ("IX", average_cx_error[1]),
                ("IY", average_cx_error[2]),
                ("IZ", average_cx_error[3]),
                ("XI", average_cx_error[4]),
                ("XX", average_cx_error[5]),
                ("XY", average_cx_error[6]),
                ("XZ", average_cx_error[7]),
                ("YI", average_cx_error[8]),
                ("YX", average_cx_error[9]),
                ("YY", average_cx_error[10]),
                ("YZ", average_cx_error[11]),
                ("ZI", average_cx_error[12]),
                ("ZX", average_cx_error[13]),
                ("ZY", average_cx_error[14]),
                ("ZZ", average_cx_error[15]),
            ]
        ),
        ["cx"],
    )

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
