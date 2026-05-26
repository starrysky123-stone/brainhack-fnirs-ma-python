# Expected Data Format

This document describes the provisional input data format for the Python-based fNIRS MA analysis pipeline.

## Important note

The final data format should be based on the output structure of the original MATLAB fNIRS pipeline.

At the current stage, this document only describes the expected processed data format for the Python prototype. The structure may be revised after reviewing the original MATLAB scripts and output files.

## Privacy note

Raw fNIRS data, subject-level identifiable information, and sensitive metadata should not be uploaded to GitHub.

The GitHub repository should only include code, documentation, simulated data, or fully anonymized demonstration materials.

## Provisional processed activation table

The Python prototype currently assumes a processed channel-level activation table.

Each row represents one anonymized participant.

Each channel column represents one fNIRS activation value during the morphological awareness (MA) task.

Example structure:

| subject_id | grade | grade_group | Ch01 | Ch02 | Ch03 | ... | Ch24 |
|---|---|---|---|---|---|---|---|
| sub-001 | 1 | G1-3 | 0.12 | -0.03 | 0.25 | ... | 0.08 |
| sub-002 | 4 | G4-6 | 0.30 | 0.15 | 0.40 | ... | 0.20 |

## Provisional columns

- subject_id: anonymized participant ID
- grade: school grade level
- grade_group: predefined grade group
  - G1-3: lower-grade children
  - G4-6: upper-grade children
- Ch01 to ChXX: fNIRS channel-level activation values

## Main analysis variable

The main dependent variables are MA-related channel-level activation values.

The main grouping variable is the predefined grade_group.

## Planned statistical analysis

The planned group comparison will test whether MA-related activation differs between G1-3 and G4-6 children for each channel.

The pipeline will generate:

1. uncorrected channel-wise statistical results
2. FWE-corrected results
3. visualization of significant channels and activation patterns

## Optional exploratory analysis

An exploratory machine learning analysis may be added later. This would not be used to define the participant groups, because the groups are already predefined.

Instead, it would test whether MA-related activation features contain enough information to distinguish lower-grade and upper-grade children.

## Next step

This document should be revised after reviewing the original MATLAB fNIRS pipeline and confirming the actual MATLAB output format.
