# qtest

A tool for comparing and testing `qt`, `q-synth`, `olsq2`, `tb-olsq2` and `sabre`.

> Note: Works only for UNIX systems.

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

## Updating the patch file

Run in project root:

```bash
git --no-pager diff --no-color --submodule=diff > patch.diff 
```

Note: Remember to delete the old file before generating the new. Also remember to `git add` untracked files before running the command above.
