# BrainHack Python fNIRS MA Analysis Pipeline

This repository contains a Python-based fNIRS analysis pipeline for the BrainHack final project.

## Project topic

This project examines brain activation differences during morphological awareness (MA) tasks between typically developing children in lower grades (G1–3) and upper grades (G4–6).

## Main goals

1. Build a Python / Jupyter Notebook-based fNIRS analysis pipeline.
2. Reconstruct key steps from an existing MATLAB-based fNIRS pipeline.
3. Compare MA-related brain activation between G1–3 and G4–6 children.
4. Generate both uncorrected and FWE-corrected statistical results.
5. Visualize significant channels and brain activation patterns.
6. Conduct an exploratory machine learning analysis using MA-related activation features to classify grade groups.

## Repository structure

- data/: raw and processed data, not tracked by Git
- notebooks/: Jupyter notebooks for step-by-step analysis
- src/: reusable Python functions
- scripts/: Python scripts for running analysis
- results/: statistical results
- figures/: visualization outputs
- docs/: notes and documentation

## Notes

The original MATLAB pipeline is kept in a separate repository for thesis-related analysis. This repository is designed specifically for the BrainHack final project and focuses on reproducible Python-based brain data analysis.
