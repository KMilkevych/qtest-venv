from qiskit_ibm_runtime.fake_provider import FakeTenerife, FakeCambridge, FakeTokyo
from qiskit import QuantumCircuit
from qiskit.circuit import Reset
from qiskit_aer.noise import NoiseModel, QuantumError, pauli_error
from qiskit.circuit.library import IGate, XGate, YGate, ZGate
from qiskit.quantum_info.operators.channel import Kraus
from qiskit.circuit.library.generalized_gates import PauliGate, UnitaryGate
from numpy import array_equal

from typing import Any

circuit = QuantumCircuit.from_qasm_file(
    "qt/benchmarks/transpiled/cambridge/barenco_tof_4.qasm"
)
circuit.measure_active()
platform = FakeCambridge()
directed_connectivity = platform.configuration().coupling_map
num_of_edges = len(directed_connectivity)


num_of_qubits = platform.configuration().n_qubits
backend_noise_model = NoiseModel.from_backend(platform)
backend_errors: list[dict[str, Any]] = backend_noise_model.to_dict()["errors"]

backend_gate_errors = [error for error in backend_errors if error["type"] == "qerror"]

backend_readout_errors = [
    error for error in backend_errors if error["type"] == "roerror"
]

uniform_noise_model = NoiseModel([instr for instr in backend_noise_model.basis_gates])

# GATE ERRORS
instr_op_prob = []
for error in backend_gate_errors:
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
        avg_prob = sum(probs) / num_of_edges
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
    uniform_noise_model.add_all_qubit_quantum_error(error, [op])

# READOUT ERROR
average_readout_error = [[0.0, 0.0], [0.0, 0.0]]
for error in backend_readout_errors:
    average_readout_error[0][0] += error["probabilities"][0][0]
    average_readout_error[0][1] += error["probabilities"][0][1]
    average_readout_error[1][0] += error["probabilities"][1][0]
    average_readout_error[1][1] += error["probabilities"][1][1]
average_readout_error[0][0] /= num_of_qubits
average_readout_error[0][1] /= num_of_qubits
average_readout_error[1][0] /= num_of_qubits
average_readout_error[1][1] /= num_of_qubits

uniform_noise_model.add_all_qubit_readout_error(average_readout_error)

real_result = platform.run(circuit, shots=1000, noise_model=backend_noise_model)
print(real_result.result().get_counts())
uniform_result = platform.run(circuit, shots=1000, noise_model=uniform_noise_model)
print(uniform_result.result().get_counts())

# TODO
# 2. Add unaries
