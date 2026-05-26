# MATLAB-to-Python Translation Plan

This document describes how the original MATLAB-based fNIRS MA analysis pipeline will be translated into a Python-based workflow for the BrainHack final project.

## Main project logic

The Python pipeline should be based on the original MATLAB fNIRS pipeline.

The goal is not to create a completely separate analysis, but to reconstruct the major steps of the MATLAB pipeline in Python and document which parts have been translated.

## Planned workflow

1. Read and understand the original MATLAB fNIRS pipeline.
2. Identify the main input files used in the MATLAB pipeline.
3. Identify the major preprocessing or data organization steps.
4. Identify how MA-related activation values are computed.
5. Identify how grade groups are defined.
6. Reconstruct the corresponding Python workflow.
7. Run channel-wise group comparison between G1–3 and G4–6.
8. Generate uncorrected results.
9. Generate FWE-corrected results.
10. Visualize significant channels and activation patterns.
11. Optionally conduct exploratory machine learning analysis.

## MATLAB-to-Python mapping table

| MATLAB pipeline step | Purpose | Python equivalent | Current status |
|---|---|---|---|
| Load fNIRS data | Import original or processed fNIRS data | To be determined after reviewing MATLAB script | Not started |
| Organize subject information | Define subject-level variables and groups | pandas DataFrame | Not started |
| Define MA-related conditions | Select MA task or contrast of interest | pandas / numpy indexing | Not started |
| Compute activation values | Obtain channel-level activation estimates | To be determined based on MATLAB output | Not started |
| Run group comparison | Compare G1–3 vs G4–6 | scipy / statsmodels | Prototype demo created |
| Multiple-comparison correction | Control family-wise error | Bonferroni or MATLAB-equivalent FWE method | Prototype demo created |
| Visualize significant channels | Display significant fNIRS channels | matplotlib-based visualization | Prototype demo created |
| Machine learning analysis | Exploratory add-on only | scikit-learn | Optional |

## Important note

The current `02_fnirs_pipeline_demo.ipynb` notebook uses simulated data only. It is used to demonstrate the expected Python workflow for channel-wise statistics and FWE correction.

The final Python pipeline should be revised after reviewing the original MATLAB pipeline.
