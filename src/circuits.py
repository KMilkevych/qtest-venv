from qiskit import QuantumCircuit, QuantumRegister


def remove_all_non_cx_gates(circuit: QuantumCircuit) -> QuantumCircuit:
    """
    Remove all non-CX gates from the circuit.
    """
    num_qubits = circuit.num_qubits
    qubit_name = circuit.qregs[0].name
    new_circuit = QuantumCircuit(QuantumRegister(num_qubits, qubit_name))
    for instr in circuit.data:
        if instr[0].name == "cx":
            new_circuit.append(instr[0], instr[1])

    return new_circuit


def count_swaps(circuit: QuantumCircuit):
    """
    Counts SWAP gates in a circuit.
    """
    swaps = 0
    for instr in circuit.data:
        if instr[0].name.startswith("swap"):
            swaps += 1

    return swaps


def with_swaps_as_cnots(circuit: QuantumCircuit, register_name: str):
    """
    Replaces all SWAP gates with CNOT gates.
    """
    new_circuit = QuantumCircuit(QuantumRegister(circuit.num_qubits, register_name))
    for instr in circuit.data:
        if instr[0].name.startswith("swap"):
            new_circuit.cx(instr[1][0]._index, instr[1][1]._index)
            new_circuit.cx(instr[1][1]._index, instr[1][0]._index)
            new_circuit.cx(instr[1][0]._index, instr[1][1]._index)
        else:
            new_circuit.append(instr[0], instr[1])

    return new_circuit


def get_stats(circuit: QuantumCircuit):
    """
    Get circuit statistics.
    """
    cx_circuit = with_swaps_as_cnots(circuit, "q")
    cx_circuit_only = remove_all_non_cx_gates(cx_circuit)
    depth = cx_circuit.depth()
    cx_depth = cx_circuit_only.depth()
    swap_count = count_swaps(circuit)
    return depth, cx_depth, swap_count
