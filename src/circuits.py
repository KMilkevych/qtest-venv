import json
import re

from typing import Any
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Qubit, Instruction, CircuitInstruction


class LogicalQubit:
    def __init__(self, id: int):
        self.id = id

    def __str__(self):
        return f"q_{self.id}"

    def __eq__(self, other):
        if isinstance(other, LogicalQubit):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)


class PhysicalQubit:
    def __init__(self, id: int):
        self.id = id

    def __str__(self):
        return f"p_{self.id}"

    def __eq__(self, other):
        if isinstance(other, PhysicalQubit):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)


type InitialMapping = dict[LogicalQubit, PhysicalQubit]


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


def parse_olsq2_circuit(
    path: str, platform_depth: int, gate_lines: list[str]
) -> tuple[QuantumCircuit, InitialMapping]:
    """
    Parse the circuit from the output file of OLSQ2.
    """
    with open(path, "r") as f:
        data: dict[str, Any] = json.load(f)

    raw_initial_mapping: list[int] = data["initial_mapping"]
    initial_mapping = {
        LogicalQubit(i): PhysicalQubit(raw_initial_mapping[i])
        for i in range(len(raw_initial_mapping))
    }

    gates = []
    for line in gate_lines:
        if line.startswith("SWAP"):
            parts = line.split(" ")
            qubits = list(map(int, parts[4][1:-1].split(",")))
            time = int(parts[7])
            gates.append(("swap", qubits, time))
        else:
            parts = re.search(
                r"Gate (\d+): (\w+) (.+) on (qubits|qubit) (.+) at time (\d+)", line
            )
            if parts is None:
                raise ValueError(f"Could not parse gate line: {line}")
            gate_name = parts.group(2)
            qubits = list(map(int, parts.group(5).split(" and ")))
            time = int(parts.group(6))
            gates.append((gate_name, qubits, time))

    gates = sorted(gates, key=lambda x: x[2])
    register = QuantumRegister(platform_depth, "q")
    result_circuit = QuantumCircuit(register)
    for gate_name, qubits, time in gates:
        match gate_name:
            case "swap":
                result_circuit.swap(qubits[0], qubits[1])
            case "cx":
                result_circuit.cx(qubits[0], qubits[1])
            case "x":
                result_circuit.x(qubits[0])
            case "h":
                result_circuit.h(qubits[0])
            case "t":
                result_circuit.t(qubits[0])
            case "tdg":
                result_circuit.tdg(qubits[0])
            case "s":
                result_circuit.s(qubits[0])
            case "sdg":
                result_circuit.sdg(qubits[0])
            case "y":
                result_circuit.y(qubits[0])
            case "z":
                result_circuit.z(qubits[0])
            case name if name.startswith("rx"):
                angle = float(name.split("_")[1])
                result_circuit.rx(angle, qubits[0])
            case name if name.startswith("rz"):
                angle = float(name.split("_")[1])
                result_circuit.rz(angle, qubits[0])
            case name if name.startswith("u_"):
                theta = float(name.split("_")[1])
                phi = float(name.split("_")[2])
                lam = float(name.split("_")[3])
                result_circuit.u(theta, phi, lam, qubits[0])
            case name if name.startswith("u3"):
                theta = float(name.split("_")[1])
                phi = float(name.split("_")[2])
                lam = float(name.split("_")[3])
                instr = CircuitInstruction(
                    operation=Instruction(
                        name="u3",
                        num_qubits=1,
                        num_clbits=0,
                        params=[theta, phi, lam],
                    ),
                    qubits=(Qubit(register, qubits[0]),),
                    clbits=(),
                )
                result_circuit.append(instr)
            case name if name.startswith("u2"):
                phi = float(name.split("_")[1])
                lam = float(name.split("_")[2])
                instr = CircuitInstruction(
                    operation=Instruction(
                        name="u2",
                        num_qubits=1,
                        num_clbits=0,
                        params=[phi, lam],
                    ),
                    qubits=(Qubit(register, qubits[0]),),
                    clbits=(),
                )
                result_circuit.append(instr)
            case name if name.startswith("u1"):
                lam = float(name.split("_")[1])
                instr = CircuitInstruction(
                    operation=Instruction(
                        name="u1",
                        num_qubits=1,
                        num_clbits=0,
                        params=[lam],
                    ),
                    qubits=(Qubit(register, qubits[0]),),
                    clbits=(),
                )
                result_circuit.append(instr)
            case _:
                raise ValueError(
                    f"Unknown unary gate: '{gate_name}'... Perhaps you should add it to the match statement?"
                )

    return result_circuit, initial_mapping
