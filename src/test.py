import os
import argparse

DEFAULT_TIME_LIMIT_S = 600
TOOLS = ["qt", "q-synth", "olsq2", "tb-olsq2", "sabre"]
PLATFORMS = ["melbourne"]

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
    "tool",
    type=str,
    help=f"the tool to use, one of {", ".join(TOOLS)}",
)

parser.add_argument(
    "input",
    type=str,
    help="the path to the input file",
)

parser.add_argument(
    "platform",
    type=str,
    help=f"the platform to run on, one of {", ".join(PLATFORMS)}",
)

args = parser.parse_args()


def test(
    tool: str,
    input: str,
    platform: str,
    time_limit: int,
    cx_optimal: bool,
    swap_optimal: bool,
) -> tuple[float | None, float, int, int, int]:
    """
    Run a tool on an input file on a platform with a time limit.
    
    Args:
        - `tool` (str): the tool to use, one of {", ".join(TOOLS)}.
        - `input` (str): the path to the input file.
        - `platform` (str): the platform to run on, one of {", ".join(PLATFORMS)}.
        - `time_limit` (int): the time limit in seconds.
        - `cx_optimal` (bool): whether to optimize for cx-depth.
        - `swap_optimal` (bool): whether to optimize for swap count after finding a depth-optimal circuit.

    Returns:
        - `tuple[float | None, float, int, int, int]`: a tuple containing the following: 
            - solver time (optional)
            - the total time
            - the depth of the output circuit
            - the cx-depth of the output circuit
            - the swap count of the output circuit
    """

    if tool not in TOOLS:
        raise ValueError(f"Unknown tool: '{tool}'.")
    if platform not in PLATFORMS:
        raise ValueError(f"Unknown platform: '{platform}'.")
    
    os.makedirs("tmp", exist_ok=True)
    with open("tmp/output.txt", "w") as f:
        f.write("")
    
    match tool:
        case "qt":
            command = f"cd qt && ./qt ../{input} -p {platform} -t {time_limit} -m sat -s glucose42 {'-cx' if cx_optimal else ''} {'-swap' if swap_optimal else ''} -anc > ../tmp/output.txt"
            os.system(command)

            with open("tmp/output.txt", "r") as f:
                output = f.read()

            lines = output.split("\n")
            solver_time_line = list(filter(lambda line: line.startswith("Solver time"), lines))[0]
            total_time_line = list(filter(lambda line: line.startswith("Total time"), lines))[0]
            depth_line = list(filter(lambda line: line.startswith("Depth"), lines))[1]

            solver_time = float(solver_time_line.split(": ")[1].split(" ")[0])
            total_time = float(total_time_line.split(": ")[1].split(" ")[0])

            def extract_number(line):
                return int(line.split(": ")[1])
            depth, cx_depth, swap_count = map(extract_number, depth_line.split(", "))
            return solver_time, total_time, depth, cx_depth, swap_count
        case "q-synth":
            if cx_optimal:
                raise ValueError("CX-optimal is not supported by q-synth.")
            if not swap_optimal:
                raise ValueError("Swap-optimal must be enabled for q-synth.")
            
            command = f"poetry run python q-synth.py -b1 -a1 -m sat -s cd153 -p {platform} -v1 {input} -t {time_limit} > tmp/output.txt" 
            os.system(command)

            with open("tmp/output.txt", "r") as f:
                output = f.read()

            lines = output.split("\n")
            raise NotImplementedError("Q-Synth is not yet implemented.")
        case "olsq2":
            raise NotImplementedError("OLSQ2 is not yet implemented.")
        case "tb-olsq2":
            raise NotImplementedError("TB-OLSQ2 is not yet implemented.")
        case "sabre":
            raise NotImplementedError("Sabre is not yet implemented.")
        case _:
            raise ValueError(f"Unknown tool: '{tool}'.")


print(f"Running {args.tool} on {args.input} on {args.platform} with time limit {args.time_limit}s")
print(f"  CX-optimal: {args.cx_optimal}")
print(f"  Swap-optimal: {args.swap_optimal}")
solver_time, total_time, depth, cx_depth, swap_count = test(args.tool, args.input, args.platform, args.time_limit, args.cx_optimal, args.swap_optimal)

print()
print("OUTPUT")
print(f"Solver time: {solver_time}s")
print(f"Total time: {total_time}s")
print(f"Depth: {depth}")
print(f"CX-depth: {cx_depth}")
print(f"Swap count: {swap_count}")
