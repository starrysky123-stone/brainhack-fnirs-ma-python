# MATLAB Pipeline Summary

This document summarizes the original MATLAB-based fNIRS MA analysis pipeline and identifies which parts should be translated into Python.

## Purpose of this document

The goal of this document is to understand the original MATLAB pipeline before rebuilding the analysis workflow in Python.

The Python pipeline should follow the logic of the MATLAB pipeline as closely as possible, rather than creating a completely separate analysis.

## Source MATLAB pipeline

Original MATLAB script or pipeline file:

- To be added after reviewing the MATLAB code

## Overall MATLAB pipeline logic

At the current stage, the MATLAB pipeline still needs to be reviewed in detail.

The expected summary will include:

1. What input files the MATLAB pipeline uses.
2. How subject information is loaded or organized.
3. How fNIRS data are loaded.
4. How morphological awareness (MA) task conditions are defined.
5. How activation values are computed.
6. How group comparison is performed.
7. How uncorrected results are generated.
8. How FWE-corrected results are generated.
9. How significant channels or brain activation patterns are visualized.

## MATLAB pipeline step-by-step summary

| Step | MATLAB code section | Purpose | Python translation plan | Status |
|---|---|---|---|---|
| 1 | To be reviewed | Load input files | To be implemented | Not started |
| 2 | To be reviewed | Organize subject information | pandas DataFrame | Not started |
| 3 | To be reviewed | Load fNIRS data | To be determined | Not started |
| 4 | To be reviewed | Define MA task or contrast | pandas / numpy indexing | Not started |
| 5 | To be reviewed | Compute channel-level activation values | To be determined | Not started |
| 6 | To be reviewed | Compare G1–3 vs G4–6 | scipy / statsmodels | Prototype demo created |
| 7 | To be reviewed | Generate uncorrected results | pandas DataFrame | Prototype demo created |
| 8 | To be reviewed | Apply FWE correction | MATLAB-equivalent method to be confirmed | Prototype demo created |
| 9 | To be reviewed | Visualize significant channels | matplotlib | Prototype demo created |

## Notes for Python translation

The Python translation should prioritize reproducibility and clarity.

The current Python demo notebook uses simulated data only. It demonstrates the expected statistical workflow but does not yet reproduce the full MATLAB pipeline.

After reviewing the MATLAB code, this document should be updated with more precise details.
