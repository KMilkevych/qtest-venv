from qiskit import QuantumCircuit
from check import check_qcec, connectivity_check, equality_check
from circuits import get_stats
from platforms import PLATFORMS
from simulator import ACCEPTED_PLATFORMS, simulate
from test import output_csv, test

EXPERIMENTS = [
    # tenerife (5)
    ("4gt13_92.qasm", "tenerife"),
    ("4mod5-v1_22.qasm", "tenerife"),
    ("adder.qasm", "tenerife"),
    ("mod5mils_65.qasm", "tenerife"),
    ("or.qasm", "tenerife"),
    ("qaoa5.qasm", "tenerife"),
    ("toffoli.qasm", "tenerife"),
    # melbourne (14)
    ("4gt13_92.qasm", "melbourne"),
    ("4mod5-v1_22.qasm", "melbourne"),
    ("adder.qasm", "melbourne"),
    ("barenco_tof_4.qasm", "melbourne"),
    ("barenco_tof_5.qasm", "melbourne"),
    ("mod_mult_55.qasm", "melbourne"),
    ("mod5mils_65.qasm", "melbourne"),
    ("or.qasm", "melbourne"),
    ("qaoa5.qasm", "melbourne"),
    ("qft_8.qasm", "melbourne"),
    ("rc_adder_6.qasm", "melbourne"),
    ("tof_4.qasm", "melbourne"),
    ("tof_5.qasm", "melbourne"),
    ("toffoli.qasm", "melbourne"),
    ("vbe_adder_3.qasm", "melbourne"),
    # tokyo (20)
    ("4gt13_92.qasm", "tokyo"),
    ("4mod5-v1_22.qasm", "tokyo"),
    ("adder.qasm", "tokyo"),
    ("barenco_tof_4.qasm", "tokyo"),
    ("barenco_tof_5.qasm", "tokyo"),
    ("mod_mult_55.qasm", "tokyo"),
    ("mod5mils_65.qasm", "tokyo"),
    ("or.qasm", "tokyo"),
    ("qaoa5.qasm", "tokyo"),
    ("qft_8.qasm", "tokyo"),
    ("rc_adder_6.qasm", "tokyo"),
    ("tof_4.qasm", "tokyo"),
    ("tof_5.qasm", "tokyo"),
    ("toffoli.qasm", "tokyo"),
    ("vbe_adder_3.qasm", "tokyo"),
    # sycamore (54)
    ("4gt13_92.qasm", "sycamore"),
    ("4mod5-v1_22.qasm", "sycamore"),
    ("adder.qasm", "sycamore"),
    ("barenco_tof_4.qasm", "sycamore"),
    ("barenco_tof_5.qasm", "sycamore"),
    ("mod_mult_55.qasm", "sycamore"),
    ("mod5mils_65.qasm", "sycamore"),
    ("or.qasm", "sycamore"),
    ("qaoa5.qasm", "sycamore"),
    ("qft_8.qasm", "sycamore"),
    ("rc_adder_6.qasm", "sycamore"),
    ("tof_4.qasm", "sycamore"),
    ("tof_5.qasm", "sycamore"),
    ("toffoli.qasm", "sycamore"),
    ("vbe_adder_3.qasm", "sycamore"),
    # rigetti (80)
    ("4gt13_92.qasm", "rigetti80"),
    ("4mod5-v1_22.qasm", "rigetti80"),
    ("adder.qasm", "rigetti80"),
    ("barenco_tof_4.qasm", "rigetti80"),
    ("barenco_tof_5.qasm", "rigetti80"),
    ("mod_mult_55.qasm", "rigetti80"),
    ("mod5mils_65.qasm", "rigetti80"),
    ("or.qasm", "rigetti80"),
    ("qaoa5.qasm", "rigetti80"),
    ("qft_8.qasm", "rigetti80"),
    ("rc_adder_6.qasm", "rigetti80"),
    ("tof_4.qasm", "rigetti80"),
    ("tof_5.qasm", "rigetti80"),
    ("toffoli.qasm", "rigetti80"),
    ("vbe_adder_3.qasm", "rigetti80"),
    # eagle (127)
    ("4gt13_92.qasm", "eagle"),
    ("4mod5-v1_22.qasm", "eagle"),
    ("adder.qasm", "eagle"),
    ("barenco_tof_4.qasm", "eagle"),
    ("barenco_tof_5.qasm", "eagle"),
    ("mod_mult_55.qasm", "eagle"),
    ("mod5mils_65.qasm", "eagle"),
    ("or.qasm", "eagle"),
    ("qaoa5.qasm", "eagle"),
    ("qft_8.qasm", "eagle"),
    ("rc_adder_6.qasm", "eagle"),
    ("tof_4.qasm", "eagle"),
    ("tof_5.qasm", "eagle"),
    ("toffoli.qasm", "eagle"),
    ("vbe_adder_3.qasm", "eagle"),
]
EXPERIMENTS_TRANSPILED = [
    # tenerife (5)
    ("transpiled/tenerife/4gt13_92.qasm", "tenerife"),
    ("transpiled/tenerife/4mod5-v1_22.qasm", "tenerife"),
    ("transpiled/tenerife/adder.qasm", "tenerife"),
    ("transpiled/tenerife/mod5mils_65.qasm", "tenerife"),
    ("transpiled/tenerife/or.qasm", "tenerife"),
    ("transpiled/tenerife/qaoa5.qasm", "tenerife"),
    ("transpiled/tenerife/toffoli.qasm", "tenerife"),
    # melbourne (14)
    ("transpiled/melbourne/4gt13_92.qasm", "melbourne"),
    ("transpiled/melbourne/4mod5-v1_22.qasm", "melbourne"),
    ("transpiled/melbourne/adder.qasm", "melbourne"),
    ("transpiled/melbourne/barenco_tof_4.qasm", "melbourne"),
    ("transpiled/melbourne/barenco_tof_5.qasm", "melbourne"),
    ("transpiled/melbourne/mod_mult_55.qasm", "melbourne"),
    ("transpiled/melbourne/mod5mils_65.qasm", "melbourne"),
    ("transpiled/melbourne/or.qasm", "melbourne"),
    ("transpiled/melbourne/qaoa5.qasm", "melbourne"),
    ("transpiled/melbourne/qft_8.qasm", "melbourne"),
    ("transpiled/melbourne/rc_adder_6.qasm", "melbourne"),
    ("transpiled/melbourne/tof_4.qasm", "melbourne"),
    ("transpiled/melbourne/tof_5.qasm", "melbourne"),
    ("transpiled/melbourne/toffoli.qasm", "melbourne"),
    ("transpiled/melbourne/vbe_adder_3.qasm", "melbourne"),
    # tokyo (20)
    ("transpiled/tokyo/4gt13_92.qasm", "tokyo"),
    ("transpiled/tokyo/4mod5-v1_22.qasm", "tokyo"),
    ("transpiled/tokyo/adder.qasm", "tokyo"),
    ("transpiled/tokyo/barenco_tof_4.qasm", "tokyo"),
    ("transpiled/tokyo/barenco_tof_5.qasm", "tokyo"),
    ("transpiled/tokyo/mod_mult_55.qasm", "tokyo"),
    ("transpiled/tokyo/mod5mils_65.qasm", "tokyo"),
    ("transpiled/tokyo/or.qasm", "tokyo"),
    ("transpiled/tokyo/qaoa5.qasm", "tokyo"),
    ("transpiled/tokyo/qft_8.qasm", "tokyo"),
    ("transpiled/tokyo/rc_adder_6.qasm", "tokyo"),
    ("transpiled/tokyo/tof_4.qasm", "tokyo"),
    ("transpiled/tokyo/tof_5.qasm", "tokyo"),
    ("transpiled/tokyo/toffoli.qasm", "tokyo"),
    ("transpiled/tokyo/vbe_adder_3.qasm", "tokyo"),
]
VQE_EXPERIMENTS = [
    # melbourne (14)
    ("vqe/vqe_8_0_5_100.qasm", "melbourne"),
    ("vqe/vqe_8_0_10_100.qasm", "melbourne"),
    ("vqe/vqe_8_1_5_100.qasm", "melbourne"),
    ("vqe/vqe_8_1_10_100.qasm", "melbourne"),
    ("vqe/vqe_8_2_5_100.qasm", "melbourne"),
    ("vqe/vqe_8_2_10_100.qasm", "melbourne"),
    ("vqe/vqe_8_3_5_100.qasm", "melbourne"),
    ("vqe/vqe_8_3_10_100.qasm", "melbourne"),
    ("vqe/vqe_8_4_5_100.qasm", "melbourne"),
    ("vqe/vqe_8_4_10_100.qasm", "melbourne"),
    # tokyo (20)
    ("vqe/vqe_8_0_5_100.qasm", "tokyo"),
    ("vqe/vqe_8_0_10_100.qasm", "tokyo"),
    ("vqe/vqe_8_1_5_100.qasm", "tokyo"),
    ("vqe/vqe_8_1_10_100.qasm", "tokyo"),
    ("vqe/vqe_8_2_5_100.qasm", "tokyo"),
    ("vqe/vqe_8_2_10_100.qasm", "tokyo"),
    ("vqe/vqe_8_3_5_100.qasm", "tokyo"),
    ("vqe/vqe_8_3_10_100.qasm", "tokyo"),
    ("vqe/vqe_8_4_5_100.qasm", "tokyo"),
    ("vqe/vqe_8_4_10_100.qasm", "tokyo"),
    # sycamore (54)
    ("vqe/vqe_8_0_5_100.qasm", "sycamore"),
    ("vqe/vqe_8_0_10_100.qasm", "sycamore"),
    ("vqe/vqe_8_1_5_100.qasm", "sycamore"),
    ("vqe/vqe_8_1_10_100.qasm", "sycamore"),
    ("vqe/vqe_8_2_5_100.qasm", "sycamore"),
    ("vqe/vqe_8_2_10_100.qasm", "sycamore"),
    ("vqe/vqe_8_3_5_100.qasm", "sycamore"),
    ("vqe/vqe_8_3_10_100.qasm", "sycamore"),
    ("vqe/vqe_8_4_5_100.qasm", "sycamore"),
    ("vqe/vqe_8_4_10_100.qasm", "sycamore"),
    # rigetti (80)
    ("vqe/vqe_8_0_5_100.qasm", "rigetti80"),
    ("vqe/vqe_8_0_10_100.qasm", "rigetti80"),
    ("vqe/vqe_8_1_5_100.qasm", "rigetti80"),
    ("vqe/vqe_8_1_10_100.qasm", "rigetti80"),
    ("vqe/vqe_8_2_5_100.qasm", "rigetti80"),
    ("vqe/vqe_8_2_10_100.qasm", "rigetti80"),
    ("vqe/vqe_8_3_5_100.qasm", "rigetti80"),
    ("vqe/vqe_8_3_10_100.qasm", "rigetti80"),
    ("vqe/vqe_8_4_5_100.qasm", "rigetti80"),
    ("vqe/vqe_8_4_10_100.qasm", "rigetti80"),
    # eagle (127)
    ("vqe/vqe_8_0_5_100.qasm", "eagle"),
    ("vqe/vqe_8_0_10_100.qasm", "eagle"),
    ("vqe/vqe_8_1_5_100.qasm", "eagle"),
    ("vqe/vqe_8_1_10_100.qasm", "eagle"),
    ("vqe/vqe_8_2_5_100.qasm", "eagle"),
    ("vqe/vqe_8_2_10_100.qasm", "eagle"),
    ("vqe/vqe_8_3_5_100.qasm", "eagle"),
    ("vqe/vqe_8_3_10_100.qasm", "eagle"),
    ("vqe/vqe_8_4_5_100.qasm", "eagle"),
    ("vqe/vqe_8_4_10_100.qasm", "eagle"),
]
VQE_EXPERIMENTS_TRANSPILED = [
    # melbourne (14)
    ("transpiled/melbourne/vqe/vqe_8_0_5_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_0_10_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_1_5_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_1_10_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_2_5_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_2_10_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_3_5_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_3_10_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_4_5_100.qasm", "melbourne"),
    ("transpiled/melbourne/vqe/vqe_8_4_10_100.qasm", "melbourne"),
    # tokyo (20)
    ("transpiled/tokyo/vqe/vqe_8_0_5_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_0_10_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_1_5_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_1_10_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_2_5_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_2_10_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_3_5_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_3_10_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_4_5_100.qasm", "tokyo"),
    ("transpiled/tokyo/vqe/vqe_8_4_10_100.qasm", "tokyo"),
]
QUEKO_EXPERIMENTS = [
    # tokyo (20)
    ("queko/16QBT_05CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_10CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_15CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_20CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_25CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_30CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_35CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_40CYC_TFL_0.qasm", "tokyo"),
    ("queko/16QBT_45CYC_TFL_0.qasm", "tokyo"),
    # sycamore (54)
    ("queko/16QBT_05CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_10CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_15CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_20CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_25CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_30CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_35CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_40CYC_TFL_0.qasm", "sycamore"),
    ("queko/16QBT_45CYC_TFL_0.qasm", "sycamore"),
    ("queko/54QBT_05CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_10CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_15CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_20CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_25CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_30CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_35CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_40CYC_QSE_0.qasm", "sycamore"),
    ("queko/54QBT_45CYC_QSE_0.qasm", "sycamore"),
    # rigetti (80)
    ("queko/16QBT_05CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_10CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_15CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_20CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_25CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_30CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_35CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_40CYC_TFL_0.qasm", "rigetti80"),
    ("queko/16QBT_45CYC_TFL_0.qasm", "rigetti80"),
    ("queko/54QBT_05CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_10CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_15CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_20CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_25CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_30CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_35CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_40CYC_QSE_0.qasm", "rigetti80"),
    ("queko/54QBT_45CYC_QSE_0.qasm", "rigetti80"),
    # eagle (127)
    ("queko/16QBT_05CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_10CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_15CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_20CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_25CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_30CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_35CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_40CYC_TFL_0.qasm", "eagle"),
    ("queko/16QBT_45CYC_TFL_0.qasm", "eagle"),
    ("queko/54QBT_05CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_10CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_15CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_20CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_25CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_30CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_35CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_40CYC_QSE_0.qasm", "eagle"),
    ("queko/54QBT_45CYC_QSE_0.qasm", "eagle"),
]

time_limit = 7200

for tool in ["sabre", "qt-cd", "qt-gl", "q-synth", "tb-olsq2", "olsq2"]:
    for benchmark, platform in (
        EXPERIMENTS
        #+ EXPERIMENTS_TRANSPILED
        + VQE_EXPERIMENTS
        #+ VQE_EXPERIMENTS_TRANSPILED
        + QUEKO_EXPERIMENTS
    ):
        match tool:
            case "sabre":
                configurations = [(True, True, True)]
            case "q-synth":
                configurations = [
                    (True, True, False),
                    (True, True, True),
                ]
            case tool_name if tool_name.endswith("olsq2"):
                configurations = [
                    (False, False, True),
                    (False, True, True),
                    (True, False, True),
                    (True, True, True),
                ]
            case tool_name if tool_name.startswith("qt"):
                configurations = [
                    (False, False, False),
                    (False, False, True),
                    (False, True, False),
                    (False, True, True),
                    (True, False, False),
                    (True, False, True),
                    (True, True, False),
                    (True, True, True),
                ]
            case _:
                raise ValueError(f"Unknown tool: {tool}")

        for cx, swap, anc in configurations:
            input = f"qt/benchmarks/{benchmark}"
            result = test(tool, input, platform, time_limit, cx, swap, anc)

            print(
                f"Running {tool} with {benchmark} on {platform} with CX={cx}, SWAP={swap}, ANC={anc}"
            )

            if result == "TO":
                output_csv(
                    tool,
                    cx,
                    swap,
                    anc,
                    input,
                    platform,
                    "TO",
                )
                print("Timeout.")
                continue
            if result == "ERROR":
                output_csv(
                    tool,
                    cx,
                    swap,
                    anc,
                    input,
                    platform,
                    "ERROR",
                )
                print("Error.")
                continue

            solver_time, total_time, circuit, initial_mapping = result
            depth, cx_depth, swap_count = get_stats(circuit)

            input_circuit = QuantumCircuit.from_qasm_file(input)

            platform_data = PLATFORMS[platform]
            num_qubits = platform_data[0]
            coupling_map = platform_data[1]
            bidirectional_map = [
                [connection[0], connection[1]] for connection in coupling_map
            ] + [[connection[1], connection[0]] for connection in coupling_map]
            correct_connectivity = connectivity_check(
                circuit, (num_qubits, bidirectional_map)
            )
            correct_output = equality_check(
                input_circuit,
                circuit,
                initial_mapping,
                anc,
            )
            correct_qcec = check_qcec(
                input_circuit.copy(),
                circuit,
                initial_mapping,
                anc,
            )

            everything_correct = (
                correct_connectivity and correct_output and correct_qcec
            )

            if not everything_correct:
                print("  ✗ Input and output circuits are not equivalent!")
                output_csv(
                    tool,
                    cx,
                    swap,
                    anc,
                    input,
                    platform,
                    "ERROR",
                )
                continue
            print("  ✓ Input and output circuits are equivalent.")
            success_rate = (
                simulate(
                    input_circuit,
                    circuit,
                    initial_mapping,
                    platform,
                    10000,
                    anc,
                )
                if platform in ACCEPTED_PLATFORMS
                else None
            )

            result = (
                solver_time,
                total_time,
                depth,
                cx_depth,
                swap_count,
                success_rate,
            )
            output_csv(
                tool,
                cx,
                swap,
                anc,
                input,
                platform,
                result,
            )
            succ_str = f", success rate: {success_rate}"
            print(f"Time: {total_time:.03f}s, depth: {depth}, CX depth: {cx_depth}, SWAPs: {swap_count}{succ_str if success_rate != None else ''}")

