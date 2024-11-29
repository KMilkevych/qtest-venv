#!/usr/bin/env sh

# Update and patch submodules
git submodule update --recursive --init
patch -p1 < venvpatch.diff

# Create environments and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

cd qt
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..

cd Q-Synth
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..

cd OLSQ2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..
