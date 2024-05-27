import argparse
import os

from qiskit import QuantumCircuit
from qiskit.qasm3 import dumps
from qiskit.exceptions import QiskitError
from check import check_qcec, connectivity_check, equality_check
from circuits import (
    get_stats,
)
from platforms import PLATFORMS
from simulator import ACCEPTED_PLATFORMS, simulate
from test import DEFAULT_TIME_LIMIT_S, TOOLS, output_csv, test


parser = argparse.ArgumentParser(
    description="A tool for testing and comparing qt, q-synth, olsq2, tb-olsq2 and sabre.",
    prog="./test",
)

parser.add_argument(
    "-t",
    "--time_limit",
    type=int,
    help=f"the time limit in seconds, default is {DEFAULT_TIME_LIMIT_S}s",
    default=DEFAULT_TIME_LIMIT_S,
)

parser.add_argument(
    "-cx",
    "--cx_optimal",
    help=f"whether to optimize for cx-depth",
    action="store_true",
)

parser.add_argument(
    "-swap",
    "--swap_optimal",
    help=f"whether to optimize for swap count after finding a depth-optimal circuit",
    action="store_true",
)

parser.add_argument(
    "-anc",
    "--ancillaries",
    help=f"whether to allow ancillary SWAPs or not",
    action="store_true",
)

parser.add_argument(
    "tool",
    type=str,
    help=f"the tool to use, one of {', '.join(TOOLS)}",
)

parser.add_argument(
    "input",
    type=str,
    help="the path to the input file",
)

parser.add_argument(
    "platform",
    type=str,
    help=f"the platform to run on, one of {', '.join(PLATFORMS.keys())}",
)

args = parser.parse_args()


"""
TODO
- Fix simulations
  - Try "./test {qt, olsq2, q-synth} qt/benchmarks/adder.qasm melbourne -swap -cx -anc"
- Write out experiments file
"""

print(
    f"Running {args.tool} on {args.input} on {args.platform} with time limit {args.time_limit}s"
)
print(f"  CX-optimal: {args.cx_optimal}")
print(f"  Swap-optimal: {args.swap_optimal}")
print(f"  Ancillary SWAPs: {args.ancillaries}")
result = test(
    args.tool,
    args.input,
    args.platform,
    args.time_limit,
    args.cx_optimal,
    args.swap_optimal,
    args.ancillaries,
)

print()
print("OUTPUT")

if result == "TO":
    print("Timeout.")
    output_csv(
        args.tool,
        args.cx_optimal,
        args.swap_optimal,
        args.ancillaries,
        args.input,
        args.platform,
        "TO",
    )
    exit(0)

if result == "ERROR":
    print("Error.")
    output_csv(
        args.tool,
        args.cx_optimal,
        args.swap_optimal,
        args.ancillaries,
        args.input,
        args.platform,
        "ERROR",
    )
    exit(0)

solver_time, total_time, circuit, initial_mapping = result
depth, cx_depth, swap_count = get_stats(circuit)

input_circuit = QuantumCircuit.from_qasm_file(args.input)

platform_data = PLATFORMS[args.platform]
num_qubits = platform_data[0]
coupling_map = platform_data[1]
bidirectional_map = [[connection[0], connection[1]] for connection in coupling_map] + [
    [connection[1], connection[0]] for connection in coupling_map
]
correct_connectivity = connectivity_check(circuit, (num_qubits, bidirectional_map))
correct_output = equality_check(
    input_circuit,
    circuit,
    initial_mapping,
    args.ancillaries,
)
correct_qcec = check_qcec(
    input_circuit.copy(),
    circuit,
    initial_mapping,
    args.ancillaries,
)

everything_correct = correct_connectivity and correct_output and correct_qcec

if not everything_correct:
    print("  ✗ Input and output circuits are not equivalent!")
    print("ERROR.")
    output_csv(
        args.tool,
        args.cx_optimal,
        args.swap_optimal,
        args.ancillaries,
        args.input,
        args.platform,
        "ERROR",
    )

    exit(0)

print("  ✓ Input and output circuits are equivalent.")

# Output circuit to qasm file
folder_exists = os.path.exists("output_circuits")
if not folder_exists:
    os.makedirs("output_circuits")

circuit_name = args.input.split("/")[-1].split(".")[0]
output_circuit_path = f"output_circuits/{args.tool}_{circuit_name}_{args.platform}{"_cxopt" if args.cx_optimal else ""}{"_swapopt" if args.swap_optimal else ""}{'_anc' if args.ancillaries else ''}.qasm"
output_circuit_qasm = dumps(circuit)
with open(output_circuit_path, "w") as f:
    f.write(output_circuit_qasm)
    f.write("\n")
    for l, p in initial_mapping.items():
        f.write(f"// {l} -> {p}\n")

try:
    dist = (
        simulate(
            input_circuit,
            circuit,
            initial_mapping,
            args.platform,
            100000,
            args.ancillaries,
        )
        if args.platform in ACCEPTED_PLATFORMS
        else None
    )
except QiskitError:
    dist = "OOM"

if solver_time is not None:
    print(f"Solver time: {solver_time:.03f}s")
else:
    print("Solver time: N/A")
print(f"Total time: {total_time:.03f}s")
print(f"Depth: {depth}")
print(f"CX-depth: {cx_depth}")
print(f"Swap count: {swap_count}")
match dist:
    case "OOM":
        print("Hellinger distance: Out of memory in simulation")
    case None:
        print("Hellinger distance: N/A")
    case _:
        print(f"Hellinger distance: {dist:.03f}")

result = (solver_time, total_time, depth, cx_depth, swap_count, dist)
output_csv(
    args.tool,
    args.cx_optimal,
    args.swap_optimal,
    args.ancillaries,
    args.input,
    args.platform,
    result,
)
