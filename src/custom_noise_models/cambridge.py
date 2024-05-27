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

BEST_CAMBRIDGE = {'errors': [{'type': 'qerror', 'id': 'ec10a4d90e2947b99d99110adc323500', 'operations': ['cx'], 'instructions': [[{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}]], 'probabilities': [1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 4.3774243474631865e-05, 1.5163807351641782e-05, 0.005530910948208436, 1.5267436872991008e-05, 5.578770018785987e-06, 0.0020864133964559883, 0.005617150850146442, 0.0021018648366846093, 0.7322249010945348, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 0.00010706639881533786, 5.977533292722486e-05, 0.01607553966307696, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 0.00013730431283610008, 3.800360889350378e-05, 0.016058768753690337, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 9.439465924211012e-05, 5.27440805759814e-05, 0.016067502211855163, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 0.00012671830378758, 3.509124985797815e-05, 0.01605021892830162, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382]}, {'type': 'qerror', 'id': 'a4068bd88aad44f39a6bec854a04bfe2', 'operations': ['u3'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [3.1611420662132524e-07, 1.3739549679996144e-07, 0.0002149194446548734, 3.1611420662132524e-07, 1.3739549679996144e-07, 0.0002149194446548734, 3.1611420662132524e-07, 1.3739549679996144e-07, 0.0002149194446548734, 0.000589000736205751, 0.0002709799446214928, 0.4302934816356385, 0.00025951701848806857, 0.0001498353894022638, 0.54816381272259, 6.800776481069209e-06, 6.800776481069209e-06, 6.800776481069209e-06, 0.01960685136053591]}, {'type': 'qerror', 'id': '048459ba92ba48a8b14f8607628ca396', 'operations': ['u2'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 0.00029471480415566, 0.000135727602621776, 0.4308329358844175, 0.000129799042468723, 7.508414077957139e-05, 0.548591490224512, 3.396641814367791e-06, 3.396641814367791e-06, 3.396641814367791e-06, 0.019607359056828186]}, {'type': 'qerror', 'id': 'e8c750238d444713806fa0859ac3441b', 'operations': ['id'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 7.895642067305484e-08, 3.4322828365928385e-08, 0.00010745316034209922, 0.00029471480415566, 0.000135727602621776, 0.4308329358844175, 0.000129799042468723, 7.508414077957139e-05, 0.548591490224512, 3.396641814367791e-06, 3.396641814367791e-06, 3.396641814367791e-06, 0.019607359056828186]}, {'type': 'roerror', 'operations': ['measure'], 'probabilities': [[0.994, 0.006000000000000005], [0.038, 0.962]]}]}

WORST_CAMBRIDGE: Any = {'errors': [{'type': 'qerror', 'id': '61f21b22376e479796c89b5c1342d8fc', 'operations': ['cx'], 'instructions': [[{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}]], 'probabilities': [1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 4.3774243474631865e-05, 1.5163807351641782e-05, 0.005530910948208436, 1.5267436872991008e-05, 5.578770018785987e-06, 0.0020864133964559883, 0.005617150850146442, 0.0021018648366846093, 0.7322249010945348, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 0.00010706639881533786, 5.977533292722486e-05, 0.01607553966307696, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 0.00013730431283610008, 3.800360889350378e-05, 0.016058768753690337, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 9.439465924211012e-05, 5.27440805759814e-05, 0.016067502211855163, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 0.00012671830378758, 3.509124985797815e-05, 0.01605021892830162, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382]}, {'type': 'qerror', 'id': '5434c301533a424b9b79c540c14e9c9a', 'operations': ['u3'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [3.1704995334250236e-07, 1.378022086241759e-07, 0.00021555563930048105, 3.1704995334250236e-07, 1.378022086241759e-07, 0.00021555563930048105, 3.1704995334250236e-07, 1.378022086241759e-07, 0.00021555563930048105, 0.0005907442690686561, 0.0002717820869781888, 0.4315672165901284, 0.00026028522881855446, 0.0001502789252238519, 0.546826308042642, 6.8209078265143764e-06, 6.8209078265143764e-06, 6.8209078265143764e-06, 0.019664890659273303]}, {'type': 'qerror', 'id': '3b43f57bc22941a5af95313ef5f3e77b', 'operations': ['u2'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 0.0002951515158413569, 0.00013592872529800658, 0.43147134893673383, 0.00012999138013835844, 7.519540129728747e-05, 0.5479225880571886, 3.401674996113482e-06, 3.401674996113482e-06, 3.401674996113482e-06, 0.019636413460288858]}, {'type': 'qerror', 'id': '33a66750c0f74325b07cf7040c7f01bf', 'operations': ['id'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 7.907341917833017e-08, 3.437368831603002e-08, 0.00010761238563422834, 0.0002951515158413569, 0.00013592872529800658, 0.43147134893673383, 0.00012999138013835844, 7.519540129728747e-05, 0.5479225880571886, 3.401674996113482e-06, 3.401674996113482e-06, 3.401674996113482e-06, 0.019636413460288858]}, {'type': 'roerror', 'operations': ['measure'], 'probabilities': [[0.352, 0.648], [0.13, 0.87]]}]}

MEDIAN_CAMBRIDGE: Any = {'errors': [{'type': 'qerror', 'id': '3ba17a080b634cbeac3686c64c01edf9', 'operations': ['cx'], 'instructions': [[{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99913477+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9949157 +0.j]]), array([[-0.04158976+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04176613+0.j]]), array([[0.        +0.j, 0.09164248+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.9986754 +0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99218018+0.j]]), array([[-0.0514533 +0.j,  0.        +0.j],
       [ 0.        +0.j,  0.05179013+0.j]]), array([[0.        +0.j, 0.11356179+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99923529+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99551086+0.j]]), array([[-0.03910041+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03924669+0.j]]), array([[0.        +0.j, 0.08612678+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['II'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99877485+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99277454+0.j]]), array([[-0.04948543+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.04978452+0.j]]), array([[0.       +0.j, 0.1091797+0.j],
       [0.       +0.j, 0.       +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'reset', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'z', 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'kraus', 'params': [array([[-0.99922187+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.9954315 +0.j]]), array([[-0.03944176+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03959194+0.j]]), array([[0.        +0.j, 0.08688277+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}, {'name': 'id', 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['ZI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['YI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['XI'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IZ'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IY'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'reset', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}], [{'name': 'pauli', 'params': ['IX'], 'qubits': [0, 1]}, {'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99932259+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99602681+0.j]]), array([[-0.03680169+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.03692347+0.j]]), array([[0.        +0.j, 0.08103859+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [1]}]], 'probabilities': [1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 1.413697832638866e-06, 1.0790293364589062e-06, 0.00011752110083606525, 1.1534556829170373e-06, 5.992088365847676e-07, 9.4241058463823e-05, 0.00011724821219162132, 9.091176128750238e-05, 0.009733097449949102, 4.3774243474631865e-05, 1.5163807351641782e-05, 0.005530910948208436, 1.5267436872991008e-05, 5.578770018785987e-06, 0.0020864133964559883, 0.005617150850146442, 0.0021018648366846093, 0.7322249010945348, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 1.8645334910289627e-07, 1.0409718773902646e-07, 2.79951342529675e-05, 0.00010706639881533786, 5.977533292722486e-05, 0.01607553966307696, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 2.439168451049472e-07, 6.751223026017401e-08, 2.8527903674415337e-05, 0.00013730431283610008, 3.800360889350378e-05, 0.016058768753690337, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 1.754332744200985e-07, 9.80253208816508e-08, 2.986158907092543e-05, 9.439465924211012e-05, 5.27440805759814e-05, 0.016067502211855163, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 2.369063179184868e-07, 6.560487748436892e-08, 3.0006701119228688e-05, 0.00012671830378758, 3.509124985797815e-05, 0.01605021892830162, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.84930705997631e-06, 5.944637747129382e-06, 0.0011003171663040044, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382, 4.217990964500891e-06, 5.175840178571841e-06, 0.0011017172799680382]}, {'type': 'qerror', 'id': 'fcb3682bbcad458a881291fb4d847c61', 'operations': ['u3'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99979569+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99880723+0.j]]), array([[-0.02021349+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.0202335 +0.j]]), array([[0.        +0.j, 0.04443784+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [3.1629305818603973e-07, 1.374732326279397e-07, 0.00021504104209706028, 3.1629305818603973e-07, 1.374732326279397e-07, 0.00021504104209706028, 3.1629305818603973e-07, 1.374732326279397e-07, 0.00021504104209706028, 0.0005893339819159465, 0.00027113326005650536, 0.43053693371993274, 0.0002596638484117304, 0.00014992016349113068, 0.5479081721743432, 6.804624234474262e-06, 6.804624234474262e-06, 6.804624234474262e-06, 0.019617944553981522]}, {'type': 'qerror', 'id': '6320f80b0cdd4db9a12e988a5b576221', 'operations': ['u2'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 0.0002947982936107186, 0.0001357660527553272, 0.4309549861056181, 0.00012983581310653977, 7.510541128892091e-05, 0.5484636111700547, 3.397604045548961e-06, 3.397604045548961e-06, 3.397604045548961e-06, 0.01961291360549595]}, {'type': 'qerror', 'id': 'bcf92b306a5e4cfa91a278e1df0c50cd', 'operations': ['id'], 'instructions': [[{'name': 'z', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'reset', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'id', 'qubits': [0]}], [{'name': 'reset', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}], [{'name': 'z', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'y', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'x', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}], [{'name': 'id', 'qubits': [0]}, {'name': 'kraus', 'params': [array([[-0.99989773+0.j,  0.        +0.j],
       [ 0.        +0.j, -0.99940353+0.j]]), array([[-0.01430164+0.j,  0.        +0.j],
       [ 0.        +0.j,  0.01430871+0.j]]), array([[0.        +0.j, 0.03143006+0.j],
       [0.        +0.j, 0.        +0.j]])], 'qubits': [0]}]], 'probabilities': [7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 7.897878815660986e-08, 3.433255164482695e-08, 0.00010748360063785224, 0.0002947982936107186, 0.0001357660527553272, 0.4309549861056181, 0.00012983581310653977, 7.510541128892091e-05, 0.5484636111700547, 3.397604045548961e-06, 3.397604045548961e-06, 3.397604045548961e-06, 0.01961291360549595]}, {'type': 'roerror', 'operations': ['measure'], 'probabilities': [[0.958, 0.042], [0.06000000000000005, 0.94]]}]}
