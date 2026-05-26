"""
Prepare non-sensitive brain template assets for Python brain plotting.

This script reads local MATLAB reference files from reference_matlab/
and creates a compressed NumPy asset file for the Python pipeline.

Input files, not tracked by Git:
- reference_matlab/MNI152_downsampled.mat
- reference_matlab/Orig_32_update_v2.mat

Output file, tracked by Git:
- assets/brain_template_32ch.npz
"""

from pathlib import Path

import numpy as np
from scipy.io import loadmat


REFERENCE_DIR = Path("reference_matlab")
ASSET_DIR = Path("assets")

MNI_TEMPLATE_FILE = REFERENCE_DIR / "MNI152_downsampled.mat"
CHANNEL_COORD_FILE = REFERENCE_DIR / "Orig_32_update_v2.mat"
OUTPUT_FILE = ASSET_DIR / "brain_template_32ch.npz"


def main():
    if not MNI_TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Missing file: {MNI_TEMPLATE_FILE}")

    if not CHANNEL_COORD_FILE.exists():
        raise FileNotFoundError(f"Missing file: {CHANNEL_COORD_FILE}")

    mni = loadmat(MNI_TEMPLATE_FILE)
    vertices = mni["vertices"].astype(float)
    faces = mni["faces"].astype(int)

    # MATLAB faces are 1-based; Python / matplotlib uses 0-based indexing.
    if faces.min() == 1:
        faces = faces - 1

    coord_mat = loadmat(CHANNEL_COORD_FILE)
    coord_keys = [k for k in coord_mat.keys() if not k.startswith("__")]

    if len(coord_keys) == 0:
        raise ValueError("No channel coordinate variable found.")

    coord_key = coord_keys[0]
    channel_mni = coord_mat[coord_key].astype(float)

    if channel_mni.shape[1] != 3:
        raise ValueError(f"Expected channel coordinates with shape (n_channels, 3), got {channel_mni.shape}")

    channel_names = np.array([f"Ch{i:02d}" for i in range(1, channel_mni.shape[0] + 1)])

    ASSET_DIR.mkdir(exist_ok=True)

    np.savez_compressed(
        OUTPUT_FILE,
        vertices=vertices,
        faces=faces,
        channel_mni=channel_mni,
        channel_names=channel_names,
        source_template=str(MNI_TEMPLATE_FILE),
        source_coordinates=str(CHANNEL_COORD_FILE),
    )

    print(f"Saved: {OUTPUT_FILE}")
    print(f"vertices shape: {vertices.shape}")
    print(f"faces shape: {faces.shape}")
    print(f"channel_mni shape: {channel_mni.shape}")


if __name__ == "__main__":
    main()
