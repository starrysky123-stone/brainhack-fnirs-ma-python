# BrainHack Python fNIRS MA Analysis Pipeline

This repository contains a Python-based fNIRS analysis project for the BrainHack final project.

## Project topic

This project aims to rebuild key components of an existing MATLAB-based fNIRS morphological awareness (MA) analysis pipeline in Python.

The research topic focuses on comparing brain activation during morphological awareness tasks between typically developing children in lower grades (G1–3) and upper grades (G4–6).

## Project direction

The main purpose of this repository is not to create a completely new analysis from scratch. Instead, this project uses the original MATLAB fNIRS pipeline as the reference standard and attempts to reconstruct the key analysis steps in Python.

The original MATLAB pipeline is kept in a separate repository for thesis-related analysis. This GitHub repository is created specifically for the BrainHack final project and focuses on reproducible Python-based implementation.

## Main goals

1. Review the original MATLAB fNIRS pipeline.
2. Summarize the major analysis steps in the MATLAB pipeline.
3. Build a Python / Jupyter Notebook-based project structure.
4. Reconstruct key MATLAB pipeline steps in Python.
5. Read or organize channel-level MA-related activation values.
6. Compare MA-related activation between G1–3 and G4–6 children.
7. Generate uncorrected channel-wise statistical results.
8. Generate FWE-corrected statistical results.
9. Visualize significant channels and activation patterns.
10. Optionally conduct an exploratory machine learning analysis using MA-related activation features.

## Repository structure

- data/: raw and processed data, not tracked by Git
- notebooks/: Jupyter notebooks for step-by-step analysis and documentation
- src/: reusable Python functions
- scripts/: Python scripts for running analysis
- results/: statistical results, not tracked by Git
- figures/: visualization outputs, not tracked by Git
- docs/: notes and documentation

## Privacy and ethics

This project uses lab-based fNIRS data from children. Raw data, subject information, and sensitive metadata must not be uploaded to GitHub.

The repository should only include code, documentation, simulated data, or fully anonymized demonstration materials.

## Current status

The current notebooks provide project documentation and a simulated channel-level fNIRS analysis demo. The simulated demo is not the final analysis pipeline. The next step is to examine the original MATLAB pipeline and map each MATLAB analysis step to a Python equivalent.
