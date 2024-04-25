from qiskit_ibm_runtime.fake_provider import FakeTenerife
from qiskit import QuantumCircuit
from qiskit_aer.noise import NoiseModel, QuantumError, pauli_error
from qiskit.circuit.library import IGate, XGate, YGate, ZGate

from typing import Any

circuit = QuantumCircuit.from_qasm_file("qt/benchmarks/transpiled/tenerife/adder.qasm")
circuit.measure_active()
platform = FakeTenerife()
num_of_qubits = platform.configuration().n_qubits
backend_noise_model = NoiseModel.from_backend(platform)
backend_errors: list[dict[str, Any]] = backend_noise_model.to_dict()["errors"]

backend_cx_errors = [
    error
    for error in backend_errors
    if error["type"] == "qerror" and error["operations"][0] == "cx"
]
backend_unary_gate_errors = [
    error
    for error in backend_errors
    if error["type"] == "qerror" and error["operations"][0] != "cx"
]
backend_readout_errors = [
    error for error in backend_errors if error["type"] == "roerror"
]

if len(backend_errors) != len(backend_cx_errors) + len(backend_unary_gate_errors) + len(
    backend_readout_errors
):
    raise ValueError("Backend errors are not disjoint or incomplete.")

uniform_noise_model = NoiseModel([instr for instr in backend_noise_model.basis_gates])

# UNARY GATE ERROR
average_unary_gate_error = {}
for error in backend_unary_gate_errors:
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
    uniform_noise_model.add_all_qubit_quantum_error(
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
for error in backend_cx_errors:
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
    average_cx_error[i] /= len(backend_cx_errors)

uniform_noise_model.add_all_qubit_quantum_error(
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
