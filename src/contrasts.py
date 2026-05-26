"""
Contrast definitions for the Python-based fNIRS MA analysis pipeline.

This module translates the MA-related contrast logic from the original
MATLAB fNIRS pipeline into Python.

Condition order follows the MATLAB group-level model output:

1. G4_6 Control
2. G1_3 Control
3. G4_6 MA
4. G1_3 MA
5. G4_6 PA
6. G1_3 PA
"""

import numpy as np


CONDITION_ORDER = [
    "G4_6_Control",
    "G1_3_Control",
    "G4_6_MA",
    "G1_3_MA",
    "G4_6_PA",
    "G1_3_PA",
]


CONTRASTS = {
    # G4_6 MA - G4_6 Control
    "G4_6_MA_minus_Control": np.array([-1, 0, 1, 0, 0, 0]),

    # G1_3 MA - G1_3 Control
    "G1_3_MA_minus_Control": np.array([0, -1, 0, 1, 0, 0]),

    # (G4_6 MA - G4_6 Control) - (G1_3 MA - G1_3 Control)
    "Group_difference_MA_minus_Control": np.array([-1, 1, 1, -1, 0, 0]),
}


def get_condition_order():
    """Return the condition order used by the contrast matrix."""
    return CONDITION_ORDER


def get_contrast(name):
    """Return one contrast vector by name."""
    if name not in CONTRASTS:
        available = ", ".join(CONTRASTS.keys())
        raise ValueError(f"Unknown contrast: {name}. Available contrasts: {available}")
    return CONTRASTS[name]


def get_all_contrasts():
    """Return all contrast vectors."""
    return CONTRASTS


if __name__ == "__main__":
    print("Condition order:")
    for i, condition in enumerate(CONDITION_ORDER, start=1):
        print(f"{i}. {condition}")

    print("\nAvailable contrasts:")
    for name, vector in CONTRASTS.items():
        print(f"{name}: {vector}")
