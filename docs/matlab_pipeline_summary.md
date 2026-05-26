# MATLAB Pipeline Summary

This document summarizes the original MATLAB-based fNIRS morphological awareness (MA) analysis pipeline and identifies which parts should be translated into Python.

## Purpose of this document

The goal of this document is to understand the original MATLAB pipeline before rebuilding the analysis workflow in Python.

The Python pipeline should follow the logic of the MATLAB pipeline as closely as possible, rather than creating a completely separate analysis.

## Source MATLAB pipeline

The current summary is based on the MATLAB script:

- fNIRS_MAPA_UMcaps_MA_only_python.m

The original MATLAB script is kept as a local reference file and should not be uploaded to the public GitHub repository.

## Overall MATLAB pipeline logic

The MATLAB pipeline performs the following major steps:

1. Load raw fNIRS data from a selected data directory.
2. Rename stimulus conditions into meaningful task labels.
3. Check whether MA and Control markers are complete.
4. Exclude datasets with incomplete MA or Control markers.
5. Preprocess the fNIRS data.
6. Run subject-level GLM analysis.
7. Run group-level mixed-effects GLM analysis.
8. Define MA-related contrasts.
9. Generate FWE-corrected and uncorrected statistical results.
10. Visualize significant activation patterns on a 3D brain template.

## Step-by-step MATLAB pipeline summary

| Step | MATLAB pipeline section | Purpose | Python translation plan | Current status |
|---|---|---|---|---|
| 1 | Define data directory and load raw dataset | Select data folder and load fNIRS files with Group and Subject metadata | Use a Python data-loading function after confirming the actual file format | Not started |
| 2 | Rename conditions | Rename stim_channel1, stim_channel2, and stim_channel3 as MA, PA, and Control | Create a condition-mapping dictionary in Python | Not started |
| 3 | Check markers | Check whether MA and Control markers exist and contain the expected number of trials | Use Python validation code to inspect event markers | Not started |
| 4 | Exclude incomplete datasets | Remove participants or files with incomplete MA / Control markers | Use pandas or Python lists to filter invalid subjects | Not started |
| 5 | Label short-separation channels | Identify short-separation channels for later regression | Need to confirm Python fNIRS package support | Not started |
| 6 | Resample data | Resample raw data to 2 Hz | Use MNE / MNE-NIRS or scipy-based resampling if raw data are available | Not started |
| 7 | Convert to optical density | Convert raw intensity data to optical density | Use MNE-NIRS or custom Python implementation | Not started |
| 8 | Apply Modified Beer-Lambert Law | Convert optical density to hemoglobin concentration | Use MNE-NIRS or custom Python implementation | Not started |
| 9 | Trim baseline | Trim 5 seconds before and after baseline periods | Use Python time-series indexing | Not started |
| 10 | Subject-level GLM | Run first-level GLM using AR-IRLS and short-separation regressors | Need Python equivalent; possibly MNE-NIRS / nilearn-style GLM / statsmodels | Not started |
| 11 | HRF basis setting | Use canonical HRF, no derivative, peak time set to 6 seconds | Recreate HRF basis in Python if implementing GLM | Not started |
| 12 | Group-level mixed-effects model | Run mixed-effects model with formula beta ~ -1 + Group:cond + (1|Subject) | Use statsmodels MixedLM or another equivalent approach | Not started |
| 13 | Define contrasts | Define MA vs Control contrasts for G4–6, G1–3, and their group difference | Recreate contrast matrix using numpy | Prototype demo created |
| 14 | Corrected results | Apply FWE correction using p < .05 / 32 | Recreate Bonferroni-style FWE correction in Python | Prototype demo created |
| 15 | Uncorrected results | Extract channels with p < .05 before correction | Use pandas filtering | Prototype demo created |
| 16 | Visualization | Plot significant activation on a 3D brain template using coordinate file | Start with channel-level matplotlib visualization; 3D visualization to be determined | Prototype demo created |

## Conditions in the MATLAB pipeline

The MATLAB script renames the stimulus channels as:

| Original marker | Renamed condition |
|---|---|
| stim_channel1 | MA |
| stim_channel2 | PA |
| stim_channel3 | Control |

The current BrainHack project focuses on MA-related activation, especially MA versus Control.

## Marker checking logic

The MATLAB pipeline checks whether each dataset includes complete markers for:

- MA
- Control

The expected number of trials is 16 for each of these conditions.

Datasets with missing or incomplete MA / Control markers are excluded before preprocessing.

## Preprocessing pipeline

The MATLAB preprocessing pipeline includes:

1. Label short-separation channels.
2. Resample data to 2 Hz.
3. Convert raw signal to optical density.
4. Apply the Modified Beer-Lambert Law.
5. Trim baseline using 5 seconds before and after the baseline period.

## Subject-level GLM

The MATLAB pipeline runs a subject-level GLM using:

- AR-IRLS estimation
- short-separation regressors
- canonical HRF basis
- HRF peak time set to 6 seconds
- no temporal or dispersion derivatives

The output is saved as subject-level statistics.

## Group-level model

The group-level model uses a mixed-effects model with the following logic:

- dependent variable: beta
- fixed effects: Group by condition
- random effect: Subject

The model formula is conceptually:

```text
beta ~ -1 + Group:cond + (1|Subject)
MA-related contrasts

The contrast matrix is designed for the following condition order:

Column	Condition
1	G4_6 Control
2	G1_3 Control
3	G4_6 MA
4	G1_3 MA
5	G4_6 PA
6	G1_3 PA

The main contrasts are:

G4_6 MA - G4_6 Control
G1_3 MA - G1_3 Control
(G4_6 MA - G4_6 Control) - (G1_3 MA - G1_3 Control)
Statistical outputs

The MATLAB pipeline generates both:

FWE-corrected results using p < .05 / 32
uncorrected results using p < .05

For each contrast, the script extracts significant positive and negative channels.

Visualization

The MATLAB pipeline visualizes significant channels using a 3D brain template and a local coordinate file.

The Python pipeline will first reproduce a simpler channel-level visualization. A more advanced brain-template visualization can be added later if the coordinate information can be safely used.

Notes for Python translation

The current Python demo notebook uses simulated data only. It demonstrates the expected statistical workflow but does not yet reproduce the full MATLAB pipeline.

The next major step is to translate the MATLAB contrast logic and group-level statistical output structure into Python.
