# type: ignore
# fmt: off

from numpy import array
from typing import Any

AVG_CAMBRIDGE: Any = {
    "errors": [
        {
            "type": "qerror",
            "id": "73fd9193241f4480a4a7f789bf6bda4c",
            "operations": ["cx"],
            "instructions": [
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99913477 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9949157 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04158976 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04176613 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.09164248 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.9986754 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99218018 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.0514533 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.05179013 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.11356179 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99923529 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99551086 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03910041 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03924669 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08612678 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99877485 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99277454 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.04948543 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.04978452 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.1091797 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99922187 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.9954315 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03944176 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03959194 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08688277 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99932259 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99602681 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.03680169 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.03692347 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.08103859 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [1],
                    },
                ],
            ],
            "probabilities": [
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                1.4136978326388662e-06,
                1.0790293364589064e-06,
                0.00011752110083606528,
                1.1534556829170375e-06,
                5.992088365847677e-07,
                9.424105846382302e-05,
                0.00011724821219162134,
                9.09117612875024e-05,
                0.009733097449949104,
                4.377424347463187e-05,
                1.5163807351641785e-05,
                0.005530910948208437,
                1.526743687299101e-05,
                5.5787700187859874e-06,
                0.0020864133964559888,
                0.005617150850146443,
                0.0021018648366846098,
                0.7322249010945349,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                1.8645334910289632e-07,
                1.0409718773902649e-07,
                2.7995134252967506e-05,
                0.00010706639881533789,
                5.9775332927224874e-05,
                0.016075539663076965,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                2.4391684510494724e-07,
                6.751223026017402e-08,
                2.8527903674415344e-05,
                0.0001373043128361001,
                3.800360889350379e-05,
                0.01605876875369034,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                1.7543327442009853e-07,
                9.802532088165083e-08,
                2.9861589070925435e-05,
                9.439465924211015e-05,
                5.2744080575981415e-05,
                0.016067502211855166,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                2.3690631791848685e-07,
                6.560487748436894e-08,
                3.0006701119228694e-05,
                0.00012671830378758003,
                3.509124985797816e-05,
                0.016050218928301625,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.849307059976311e-06,
                5.944637747129384e-06,
                0.0011003171663040046,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
                4.217990964500892e-06,
                5.175840178571842e-06,
                0.0011017172799680384,
            ],
        },
        {
            "type": "qerror",
            "id": "bea6fa37b28c41c6b0bbd294a683be42",
            "operations": ["u3"],
            "instructions": [
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                5.752100254037511e-07,
                2.50008590405868e-07,
                0.0003910732786767138,
                5.752100254037511e-07,
                2.50008590405868e-07,
                0.0003910732786767138,
                5.752100254037511e-07,
                2.50008590405868e-07,
                0.0003910732786767138,
                0.0010717617915906807,
                0.0004930824922283668,
                0.782973745938589,
                0.0004722242394377645,
                0.00027264455800843113,
                0.17782655977398237,
                1.2374878225979597e-05,
                1.2374878225979597e-05,
                1.2374878225979597e-05,
                0.03567716107960777,
            ],
        },
        {
            "type": "qerror",
            "id": "2f6427698e894131bc5bddf75ac49f24",
            "operations": ["u2"],
            "instructions": [
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                0.0005365363802255368,
                0.0002470958213857314,
                0.7843431705564249,
                0.00023630271510258606,
                0.00013669273663272872,
                0.17819843311969327,
                6.183679538001909e-06,
                6.183679538001909e-06,
                6.183679538001909e-06,
                0.03569573467567171,
            ],
        },
        {
            "type": "qerror",
            "id": "324e7441feed4db9bea5f8b0c70fd5c5",
            "operations": ["id"],
            "instructions": [
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                1.4374232833281988e-07,
                6.248564996019364e-08,
                0.00019562142410495844,
                0.0005365363802255368,
                0.0002470958213857314,
                0.7843431705564249,
                0.00023630271510258606,
                0.00013669273663272872,
                0.17819843311969327,
                6.183679538001909e-06,
                6.183679538001909e-06,
                6.183679538001909e-06,
                0.03569573467567171,
            ],
        },
        {
            "type": "roerror",
            "operations": ["measure"],
            "probabilities": [
                [0.8847142857142857, 0.1152857142857143],
                [0.13835714285714285, 0.8616428571428572],
            ],
        },
    ]
}

BEST_CAMBRIDGE = {
    "errors": [
        {
            "type": "qerror",
            "id": "0f630efe085b443b859acd80610d8c08",
            "operations": ["id"],
            "instructions": [
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                0.9994805709188078,
                0.0001731430270640534,
                0.0001731430270640534,
                0.0001731430270640534,
            ],
        },
        {
            "type": "qerror",
            "id": "751dd21222de4ff1980846df69cc47ab",
            "operations": ["u2"],
            "instructions": [
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99989773 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99940353 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.01430164 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.01430871 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.03143006 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                0.9994805709188078,
                0.0001731430270640534,
                0.0001731430270640534,
                0.0001731430270640534,
            ],
        },
        {
            "type": "qerror",
            "id": "c3e51aef5f24453ca251cf4fb2b48f58",
            "operations": ["u3"],
            "instructions": [
                [
                    {"name": "id", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "x", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "y", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
                [
                    {"name": "z", "qubits": [0]},
                    {
                        "name": "kraus",
                        "params": [
                            array(
                                [
                                    [-0.99979569 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, -0.99880723 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [-0.02021349 + 0.0j, 0.0 + 0.0j],
                                    [0.0 + 0.0j, 0.0202335 + 0.0j],
                                ]
                            ),
                            array(
                                [
                                    [0.0 + 0.0j, 0.04443784 + 0.0j],
                                    [0.0 + 0.0j, 0.0 + 0.0j],
                                ]
                            ),
                        ],
                        "qubits": [0],
                    },
                ],
            ],
            "probabilities": [
                0.9989605102290177,
                0.0003464965903274287,
                0.0003464965903274287,
                0.0003464965903274287,
            ],
        },
        {
            "type": "qerror",
            "id": "138c5d26e4184d04ba5b3079af23fbd3",
            "operations": ["cx"],
            "instructions": [
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
            ],
            "probabilities": [
                0.9799922276326362,
                0.0015836192135615464,
                0.004904975886318028,
                0.0005973339734906188,
                9.652623058225006e-07,
                2.9897265033701213e-06,
                0.005431056084421664,
                8.776319365304793e-06,
                2.718307184505054e-05,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
                0.0004904407088211882,
                7.925280504297261e-07,
                2.4547131932340414e-06,
                2.9893798042603955e-07,
                4.830690653634693e-10,
                1.496219606798751e-09,
                2.7179919601259124e-06,
                4.392141252751564e-09,
                1.3603868120290279e-08,
            ],
        },
        {
            "type": "roerror",
            "operations": ["measure"],
            "probabilities": [[0.994, 0.006000000000000005], [0.038, 0.962]],
        },
    ]
}

WORST_CAMBRIDGE: Any = {
    "errors": [
        {
            "type": "qerror",
            "id": "9bf21169449749b3bc7e15ff558fe8d5",
            "operations": ["id"],
            "instructions": [
                [{"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9960321606412671,
                0.001807840490695461,
                0.002159998868037416,
            ],
        },
        {
            "type": "qerror",
            "id": "22ac1d616d84413a8d02d85ff1a61ebb",
            "operations": ["u2"],
            "instructions": [
                [{"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9960321606412671,
                0.001807840490695461,
                0.002159998868037416,
            ],
        },
        {
            "type": "qerror",
            "id": "535fdb760d65499f954ef97b4d3aeedb",
            "operations": ["u3"],
            "instructions": [
                [{"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}],
                [{"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9920833333189507,
                0.0036013345400843287,
                0.0043153321409649115,
            ],
        },
        {
            "type": "qerror",
            "id": "3bf3f645b9d0412c9353fb7af7d8010c",
            "operations": ["cx"],
            "instructions": [
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
            ],
            "probabilities": [
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
                0.06285939372891144,
                0.00030406544607429833,
                0.0006365771965756013,
                0.0019735919647702804,
                9.546721429171476e-06,
                1.9986569478155138e-05,
                0.0008507738607572967,
                4.1153902087435895e-06,
                8.615788461726543e-06,
            ],
        },
        {
            "type": "roerror",
            "operations": ["measure"],
            "probabilities": [[0.352, 0.648], [0.13, 0.87]],
        },
    ]
}

MEDIAN_CAMBRIDGE: Any = {
    "errors": [
        {
            "type": "qerror",
            "id": "e4a1a02c974448d8a965c515bb978aec",
            "operations": ["id"],
            "instructions": [
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9985984648765001,
                0.0001635493953543603,
                0.0005046978313279704,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
            ],
        },
        {
            "type": "qerror",
            "id": "9e77a7042bc64185a4c03335fd2d7c2c",
            "operations": ["u2"],
            "instructions": [
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9985984648765001,
                0.0001635493953543603,
                0.0005046978313279704,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
                0.0002442658398754209,
                4.000559967042486e-08,
                1.2345346401856996e-07,
            ],
        },
        {
            "type": "qerror",
            "id": "1a2bc53d77b842bd93792d8f4149add6",
            "operations": ["u3"],
            "instructions": [
                [{"name": "id", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "id", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "x", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "y", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "id", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "z", "qubits": [0]}],
                [{"name": "z", "qubits": [0]}, {"name": "reset", "qubits": [0]}],
            ],
            "probabilities": [
                0.9971979977178819,
                0.000326640047901193,
                0.0010083998316788847,
                0.000488333690676956,
                1.5995754151084267e-07,
                4.938192942712729e-07,
                0.000488333690676956,
                1.5995754151084267e-07,
                4.938192942712729e-07,
                0.000488333690676956,
                1.5995754151084267e-07,
                4.938192942712729e-07,
            ],
        },
        {
            "type": "qerror",
            "id": "b048f277f0234966be3642381836f05c",
            "operations": ["cx"],
            "instructions": [
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["II"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["IZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["XZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["YZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZI"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZX"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZY"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "id", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "z", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "id", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "z", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
                [
                    {"name": "pauli", "params": ["ZZ"], "qubits": [0, 1]},
                    {"name": "reset", "qubits": [0]},
                    {"name": "reset", "qubits": [1]},
                ],
            ],
            "probabilities": [
                0.9610873061061969,
                0.007314478404025963,
                0.005985260215408579,
                0.0024837093918074027,
                1.8902589382701003e-05,
                1.5467530280520513e-05,
                0.007218834369450084,
                5.4939866297379396e-05,
                4.495595964964236e-05,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
                0.0010270192887472012,
                7.816262227512393e-06,
                6.395857743975467e-06,
                2.65409545711649e-06,
                2.019933442046406e-08,
                1.6528625283518923e-08,
                7.71405687349414e-06,
                5.870882078049861e-08,
                4.8040003661459116e-08,
            ],
        },
        {
            "type": "roerror",
            "operations": ["measure"],
            "probabilities": [[0.958, 0.042], [0.06000000000000005, 0.94]],
        },
    ]
}
