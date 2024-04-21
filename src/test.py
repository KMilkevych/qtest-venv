import os
import subprocess
import argparse
import time
from typing import Literal

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Qubit
from qiskit.transpiler.passes import SabreLayout
from qiskit.transpiler import CouplingMap, Layout
from qiskit.converters import circuit_to_dag, dag_to_circuit
from itertools import takewhile
from check import check_qcec, connectivity_check, equality_check
from circuits import (
    LogicalQubit,
    PhysicalQubit,
    get_stats,
    parse_olsq2_circuit,
    InitialMapping,
    reinsert_unary_gates,
    remove_all_non_cx_gates,
    save_circuit,
)
from platforms import PLATFORMS
from simulator import ACCEPTED_PLATFORMS, simulate


DEFAULT_TIME_LIMIT_S = 600
TOOLS = ["qt-gl", "qt-cd", "q-synth", "olsq2", "tb-olsq2", "sabre"]


def run(command: str, path: str, time_limit: int):
    """
    Run a command in a given path.
    """
    print(f"Running '{command}' in '{path}'")
    command_string = f"cd {path}; source .venv/bin/activate; {command}"
    return subprocess.check_output(
        f'/bin/bash -c "{command_string} 2> /dev/null"', shell=True, timeout=time_limit
    ).decode("utf-8")


CSV_OUTPUT_FILE = "tmp/output.csv"
if not os.path.exists(CSV_OUTPUT_FILE):
    os.makedirs(os.path.dirname(CSV_OUTPUT_FILE), exist_ok=True)
    line = f"Tool;CX optimal;SWAP optimal;Ancillaries;Input;Platform;Solver time (s);Total time (s);Depth;CX depth;SWAPs;Success rate (%)"
    with open(CSV_OUTPUT_FILE, "a") as f:
        f.write(line + "\n")


def output_csv(
    tool: str,
    cx_opt: bool,
    swap_opt: bool,
    anc: bool,
    input: str,
    platform: str,
    result: (
        tuple[float | None, float, int, int, int, float | None] | Literal["ERROR", "TO"]
    ),
):
    line = f"{tool};{cx_opt};{swap_opt};{anc};{input};{platform};"
    if isinstance(result, str):
        line += f";{result};;;;;"
    else:
        solver_time = result[0]
        total_time = result[1]
        depth = result[2]
        cx_depth = result[3]
        swaps = result[4]
        success_rate = result[5]

        if solver_time == None:
            line += f";"
        else:
            line += f"{solver_time:.3f};"
        line += f"{total_time:.3f};{depth};{cx_depth};{swaps};"
        if success_rate != None:
            line += f"{success_rate:.3f}"
    with open(CSV_OUTPUT_FILE, "a") as f:
        f.write(line + "\n")


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


def test(
    tool: str,
    input: str,
    platform: str,
    time_limit: int,
    cx_optimal: bool,
    swap_optimal: bool,
    ancillaries: bool,
) -> tuple[float | None, float, QuantumCircuit, InitialMapping] | Literal["TO"] | Literal["ERR"]:
    """
    Run a tool on an input file on a platform with a time limit.

    Args:
        - `tool` (str): the tool to use, one of qt, olsq2, tb-olsq2, q-synth and sabre.
        - `input` (str): the path to the input file.
        - `platform` (str): the platform to run on, one of tenerife, melbourne, tokyo, sycamore, rigetti80, eagle.
        - `time_limit` (int): the time limit in seconds.
        - `cx_optimal` (bool): whether to optimize for cx-depth.
        - `swap_optimal` (bool): whether to optimize for swap count after finding a depth-optimal circuit.

    Returns:
        - `tuple[float | None, float, QuantumCircuit, InitialMapping]`: a tuple containing the following:
            - solver time (optional)
            - the total time
            - the output circuit
            - the initial mapping of the output circuit
    """

    if tool not in TOOLS:
        raise ValueError(f"Unknown tool: '{tool}'.")
    if platform not in PLATFORMS.keys():
        raise ValueError(f"Unknown platform: '{platform}'.")
    if not os.path.exists(input):
        raise ValueError(f"Input file '{input}' does not exist.")

    os.makedirs("tmp", exist_ok=True)
    with open("tmp/output.txt", "w") as f:
        f.write("")

    match tool:
        case tool if tool in ["qt-gl", "qt-cd"]:
            command = f"./qt ../{input} -p {platform} -t {time_limit} -m sat -s {"glucose42" if tool == "qt-gl" else "cadical153"} {'-cx' if cx_optimal else ''} {'-swap' if swap_optimal else ''} {'-anc' if ancillaries else ''} -out ../tmp/output.qasm -init ../tmp/initial_mapping.txt"
            try:
                output = run(command, "qt", time_limit)
            except subprocess.TimeoutExpired:
                return "TO"
            
            try:
                lines = output.split("\n")
                if lines[-3].endswith("Timeout."):
                    return "TO"

                match swap_optimal:
                    case True:
                        total_time_line = list(
                            filter(lambda line: line.startswith("Total solver time"), lines)
                        )[0]
                    case False:
                        total_time_line = list(
                            filter(lambda line: line.startswith("Solver time"), lines)
                        )[0]
                total_time_line = list(
                    filter(lambda line: line.startswith("Total time"), lines)
                )[0]

                total_time = float(total_time_line.split(": ")[1].split(" ")[0])
                total_time = float(total_time_line.split(": ")[1].split(" ")[0])

                circuit = QuantumCircuit.from_qasm_file("tmp/output.qasm")
                with open("tmp/initial_mapping.txt", "r") as f:
                    lines = f.readlines()
                raw_initial_mapping = [line.split(" -> ") for line in lines]
                initial_mapping = {
                    LogicalQubit(int(raw[0])): PhysicalQubit(int(raw[1]))
                    for raw in raw_initial_mapping
                }
                return total_time, total_time, circuit, initial_mapping
            except Exception as e:
                print(f"Error in parsing output: {e}")
                return "ERR"
        case "q-synth":
            if not cx_optimal:
                raise ValueError("Q-Synth always looks at CX-only circuits.")
            if not swap_optimal:
                raise ValueError("Q-Synth is always SWAP-optimal.")

            command = f"poetry run python q-synth.py -b1 {'-a1' if ancillaries else '-a0'} -m sat -s cd153 -p {'rigetti-80' if platform == 'rigetti80' else platform} -v3 ../{input} ../tmp/output.qasm -t {time_limit}"
            try:
                output = run(command, "Q-Synth", time_limit)
            except subprocess.TimeoutExpired:
                return "TO"

            try: 
                lines = output.split("\n")

                total_time_line = list(
                    filter(lambda line: line.startswith("Encoding time: "), lines)
                )[0]
                total_time = float(total_time_line.split(": ")[1])

                initial_mapping_lines: list[str] = list(
                    filter(lambda line: line.startswith("...initially mapping"), lines)
                )
                raw_initial_mapping = [
                    (line.split(" ")[2], line.split(" ")[4])
                    for line in initial_mapping_lines
                ]
                initial_mapping = {
                    LogicalQubit(int(raw[0][1:])): PhysicalQubit(int(raw[1][1:]))
                    for raw in raw_initial_mapping
                }

                # remove measurements from output file
                with open("tmp/output.qasm", "r") as f:
                    lines = f.readlines()
                with open("tmp/output.qasm", "w") as f:
                    for line in lines:
                        measure_line = line.startswith("measure")
                        barrier_line = line.startswith("barrier")
                        if not measure_line and not barrier_line:
                            f.write(line)

                circuit = QuantumCircuit.from_qasm_file("tmp/output.qasm")
                return None, total_time, circuit, initial_mapping
            except Exception as e:
                print(f"Error in parsing output: {e}")
                return "ERR"
        case "olsq2":
            if not ancillaries:
                raise ValueError("OLSQ2 always uses ancillary SWAPs.")
            if cx_optimal:
                input_circuit = QuantumCircuit.from_qasm_file(input)
                only_cx_circuit = remove_all_non_cx_gates(input_circuit)
                save_circuit(only_cx_circuit, "tmp/tmp_circuit.qasm")
                circuit_path = "tmp/tmp_circuit.qasm"
            else:
                circuit_path = input

            command = f"poetry run python run_olsq.py --dt {platform} --qf ../{circuit_path} --swap_duration 3 {'--swap' if swap_optimal else ''} --f ../tmp --sabre"

            try:
                output = run(command, "OLSQ2", time_limit)
            except subprocess.TimeoutExpired:
                return "TO"

            try:
                lines = output.split("\n")
                total_time_line = list(
                    filter(lambda line: line.startswith("Total compilation time"), lines)
                )[0]
                total_time = float(total_time_line.split(" = ")[1][:-1])

                gate_lines = list(
                    filter(
                        lambda line: line.startswith("SWAP") or line.startswith("Gate"),
                        lines,
                    )
                )

                # OLSQ2 outputs gates many times.
                # We want the final gate list.
                # We reverse the list so these gates appear at the beginning.
                gate_lines.reverse()
                gate_0_index = gate_lines.index(
                    list(filter(lambda line: line.startswith("Gate 0"), gate_lines))[0]
                )
                stop_index = (
                    gate_0_index
                    + len(
                        list(
                            takewhile(
                                lambda s: s.startswith("SWAP"),
                                gate_lines[gate_0_index + 1 :],
                            )
                        )
                    )
                    + 1
                )
                gate_lines = gate_lines[:stop_index]

                input_name = circuit_path.split("/")[-1].split(".")[0]
                platform_depth = PLATFORMS[platform][0]
                circuit, initial_mapping = parse_olsq2_circuit(
                    f"tmp/{platform}_{input_name}.json", platform_depth, gate_lines
                )
                if cx_optimal:
                    result_circuit = reinsert_unary_gates(
                        input_circuit, circuit, initial_mapping, ancillaries=True
                    )
                else:
                    result_circuit = circuit

                return None, total_time, result_circuit, initial_mapping
            except Exception as e:
                print(f"Error in parsing output: {e}")
                return "ERR"
        case "tb-olsq2":
            if not ancillaries:
                raise ValueError("TB-OLSQ2 always uses ancillary SWAPs.")
            if cx_optimal:
                input_circuit = QuantumCircuit.from_qasm_file(input)
                only_cx_circuit = remove_all_non_cx_gates(input_circuit)
                save_circuit(only_cx_circuit, "tmp/tmp_circuit.qasm")
                circuit_path = "tmp/tmp_circuit.qasm"
            else:
                circuit_path = input
            command = f"poetry run python run_olsq.py --dt {platform} --qf ../{circuit_path} --swap_duration 3 {'--swap' if swap_optimal else ''} --f ../tmp --tran --sabre"

            try:
                output = run(command, "OLSQ2", time_limit)
            except subprocess.TimeoutExpired:
                return "TO"

            try:
                lines = output.split("\n")
                total_time_line = list(
                    filter(lambda line: line.startswith("Total compilation time"), lines)
                )[0]
                total_time = float(total_time_line.split(" = ")[1][:-1])

                gate_lines = list(
                    filter(
                        lambda line: line.startswith("SWAP") or line.startswith("Gate"),
                        lines,
                    )
                )

                # OLSQ2 outputs gates many times.
                # We want the final gate list.
                # We reverse the list so these gates appear at the beginning.
                gate_lines.reverse()
                gate_0_index = gate_lines.index(
                    list(filter(lambda line: line.startswith("Gate 0"), gate_lines))[0]
                )
                stop_index = (
                    gate_0_index
                    + len(
                        list(
                            takewhile(
                                lambda s: s.startswith("SWAP"),
                                gate_lines[gate_0_index + 1 :],
                            )
                        )
                    )
                    + 1
                )
                gate_lines = gate_lines[:stop_index]

                input_name = circuit_path.split("/")[-1].split(".")[0]
                platform_depth = PLATFORMS[platform][0]
                circuit, initial_mapping = parse_olsq2_circuit(
                    f"tmp/{platform}_{input_name}.json", platform_depth, gate_lines
                )
                if cx_optimal:
                    # TODO: something is wrong with the initial mapping that tb-olsq2 gives out
                    result_circuit = reinsert_unary_gates(
                        input_circuit, circuit, initial_mapping, ancillaries=True
                    )
                else:
                    result_circuit = circuit

                return None, total_time, result_circuit, initial_mapping
            except Exception as e:
                print(f"Error in parsing output: {e}")
                return "ERR"
        case "sabre":
            if not cx_optimal:
                raise ValueError("SABRE always looks at CX-only circuits.")
            if not swap_optimal:
                raise ValueError("SABRE always tries to optimize SWAPs.")
            if not ancillaries:
                raise ValueError("SABRE always uses ancillary SWAPs.")
            coupling_map = PLATFORMS[platform][1]
            circuit = QuantumCircuit.from_qasm_file(input)
            sabre = SabreLayout(
                CouplingMap(coupling_map), swap_trials=8, seed=0
            )
            dag = circuit_to_dag(circuit)

            before = time.time()
            res = sabre.run(dag)
            after = time.time()
            total_time = after - before
            if total_time > time_limit:
                return "TO"

            result_circuit = dag_to_circuit(res)
            initial_mapping: InitialMapping = {}
            sabre_layout = sabre.property_set.get("layout")

            # make the type checker happy
            if isinstance(sabre_layout, Layout):
                for p, q in sabre_layout.get_physical_bits().items():
                    # make the type checker happy
                    if (
                        isinstance(q, Qubit)
                        and isinstance(q._register, QuantumRegister)
                        and isinstance(q._index, int)
                        and isinstance(p, int)
                    ):
                        if q._register.name == "q":
                            initial_mapping[LogicalQubit(q._index)] = PhysicalQubit(p)
                    else:
                        raise ValueError(
                            f"Something is wrong in SABRE's initial mapping:\n{sabre_layout}"
                        )
            else:
                raise ValueError(f"SABRE did not produce an initial mapping")

            return None, total_time, result_circuit, initial_mapping
        case _:
            raise ValueError(f"Unknown tool: '{tool}'.")


"""
TODO
- Fix simulations
  - Try "./test {qt, olsq2, q-synth} qt/benchmarks/adder.qasm melbourne -swap -cx -anc"
- Write out experiments file

- Figure out what is wrong with init-map in TB-OLSQ2

# I think fixed?
- Why does Q-synth write out two times?
  - Some legacy from when I was trying things - I cleaned up the code
- How to choose model / solver for qt?
  - I added two different versions of qt
- Hack for SABRE timeouts
  - Fine, it will never be a problem
- Broken pipe error after timeout (OLSQ2)
  - Problem was that child process would die with an error and return it to the parent (our terminal)
  - I fixed this by redirecting the error to /dev/null
- SABRE tries!
  - Removed layout tries, since then SABRE is only run "once"
  - Picked swap_trials=8, since SABRE defaults to the number of processors of which 8 is typical and now we have reproducibility
  - Also set seed=0 for reproducibility
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

if result == "ERR":
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
success_rate = (
    simulate(
        input_circuit,
        circuit,
        initial_mapping,
        args.platform,
        10000,
        args.ancillaries,
    )
    if args.platform in ACCEPTED_PLATFORMS
    else None
)

if solver_time is not None:
    print(f"Solver time: {solver_time:.03f}s")
else:
    print("Solver time: N/A")
print(f"Total time: {total_time:.03f}s")
print(f"Depth: {depth}")
print(f"CX-depth: {cx_depth}")
print(f"Swap count: {swap_count}")
print(f"Success rate: {success_rate:.03f}%")

result = (solver_time, total_time, depth, cx_depth, swap_count, success_rate)
output_csv(
    args.tool,
    args.cx_optimal,
    args.swap_optimal,
    args.ancillaries,
    args.input,
    args.platform,
    result,
)
