# qtest

A tool for comparing and testing `qt`, `q-synth`, `olsq2`, `tb-olsq2` and `sabre`.

## Usage

```bash
usage: ./test [-h] [-t TIME_LIMIT] [-cx] [-swap] tool input platform

A tool for testing and comparing qt, q-synth, olsq2, tb-olsq2 and sabre.

positional arguments:
  tool                  the tool to use, one of qt, q-synth, olsq2, tb-olsq2, sabre
  input                 the path to the input file
  platform              the platform to run on, one of melbourne

options:
  -h, --help            show this help message and exit
  -t TIME_LIMIT, --time_limit TIME_LIMIT
                        the time limit in seconds, default is 600s
  -cx, --cx_optimal     whether to optimize for cx-depth
  -swap, --swap_optimal
                        whether to optimize for swap count after finding a depth-optimal circuit
```

## Installation

```bash
git clone https://github.com/anbclausen/qtest.git --recurse-submodules
patch -p1 < patch.diff
```
