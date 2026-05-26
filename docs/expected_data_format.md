# Expected Data Format

This document describes the expected input data format for the Python-based fNIRS MA analysis pipeline.

## Important privacy note

Raw fNIRS data and subject-level identifiable information should not be uploaded to GitHub.

The GitHub repository should only include code, documentation, simulated data, or fully anonymized demonstration materials.

## Expected processed activation table

The main analysis pipeline expects a processed channel-level activation table.

Each row represents one participant.

Each channel column represents one fNIRS activation value during the morphological awareness (MA) task.

Example structure:

| subject_id | grade | grade_group | Ch01 | Ch02 | Ch03 | ... | Ch24 |
|---|---|---|---|---|---|---|---|
| sub-001 | 1 | G1-3 | 0.12 | -0.03 | 0.25 | ... | 0.08 |
| sub-002 | 4 | G4-6 | 0.30 | 0.15 | 0.40 | ... | 0.20 |

## Required columns

- subject_id: anonymized participant ID
- grade: school grade level
- grade_group: grade group used for analysis
  - G1-3: lower-grade children
  - G4-6: upper-grade children
- Ch01 to ChXX: fNIRS channel-level activation values

## Main analysis variable

The main dependent variables are channel-level MA-related activation values.

The main grouping variable is grade_group.

## Planned statistical analysis

The planned group comparison will test whether MA-related activation differs between G1-3 and G4-6 children for each channel.

The pipeline will generate:

1. uncorrected channel-wise statistical results
2. FWE-corrected results
3. visualization of significant channels
4. exploratory machine learning classification using channel activation features

## Notes

The current demo notebook uses simulated data only. In the real analysis, the simulated table will be replaced by a processed, anonymized activation table generated from the lab fNIRS pipeline.
