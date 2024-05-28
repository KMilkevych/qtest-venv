from simulator import (
    best_noise_model,
    average_noise_model,
    worst_noise_model,
    median_noise_model,
)
from qiskit_ibm_runtime.fake_provider import FakeTenerife, FakeCambridge, FakeGuadalupe
from qiskit_aer.noise import NoiseModel

backend = FakeGuadalupe()

coupling_map = backend.configuration().coupling_map
num_of_qubits = backend.configuration().n_qubits
num_of_edges_in_coupling_map = len(coupling_map)
original_noise_model = NoiseModel.from_backend(backend)

new_noise_model = median_noise_model(
    original_noise_model, num_of_qubits, num_of_edges_in_coupling_map
)
print(new_noise_model.to_dict())
