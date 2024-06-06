# qtest

A tool for comparing and testing `qt` (QuilLS), `q-synth`, `olsq2`, `tb-olsq2` and `sabre`.

> Note: Works only for UNIX systems.

> Note: QuilLS was previously named qt.

## Installation

It is important to carry out the installation in this order:

```bash
git clone https://github.com/anbclausen/qtest.git --recurse-submodules
cd qtest
git submodule update --recursive --init 
patch -p1 < patch.diff
cd qt
poetry install
cd ..
cd Q-Synth
poetry install
cd ..
cd OLSQ2
poetry install
cd ..
poetry install
```

## Usage

```text
usage: ./test [-h] [-t TIME_LIMIT] [-cx] [-swap] [-anc] tool input platform

A tool for testing and comparing qt, q-synth, olsq2, tb-olsq2 and sabre.

positional arguments:
  tool                  the tool to use, one of qt-gl, qt-cd, q-synth, olsq2, tb-olsq2, sabre
  input                 the path to the input file
  platform              the platform to run on, one of tenerife, melbourne, guadalupe, tokyo, cambridge, sycamore, rigetti80, eagle

options:
  -h, --help            show this help message and exit
  -t TIME_LIMIT, --time_limit TIME_LIMIT
                        the time limit in seconds, default is 600s
  -cx, --cx_optimal     whether to optimize for cx-depth
  -swap, --swap_optimal
                        whether to optimize for swap count after finding a depth-optimal circuit
  -anc, --ancillaries   whether to allow ancillary SWAPs or not
```

## Sample run

If you run one of the transpiled benchmarks in `qt`, `qtest` will also perform a noise simulation. It will perform noise simulation based on the noise models of IBM's quantum computers from the Qiskit package. Since the noise profiles vary a lot between qubits in the noise models, we use an averaged model. We also provide a "best" model (all qubits are modelled after the least noisy), a "worst" model and a "median" model.

```text
$ ./test sabre qt/benchmarks/transpiled/tenerife/adder.qasm tenerife -swap -cx -anc
Running sabre on qt/benchmarks/transpiled/tenerife/adder.qasm on tenerife with time limit 600s
  CX-optimal: True
  Swap-optimal: True
  Ancillary SWAPs: True

OUTPUT
  ✓ Input and output circuits are equivalent.
Solver time: N/A
Total time: 0.002s
Depth: 15
CX-depth: 10
Swap count: 1
Average Hellinger distance: 0.673
Best Hellinger distance: 0.524
Worst Hellinger distance: 0.805
Median Hellinger distance: 0.626
```
