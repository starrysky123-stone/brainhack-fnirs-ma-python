"""
Statistical helper functions for the Python-based fNIRS MA analysis pipeline.

This module translates part of the statistical output logic from the original
MATLAB fNIRS pipeline into Python.

The MATLAB pipeline reports:

1. uncorrected results using p < .05
2. FWE-corrected results using p < .05 / 32
3. significant positive and negative channels for each contrast
"""

import pandas as pd


def get_fwe_threshold(alpha=0.05, n_tests=32):
    """
    Return the Bonferroni-style FWE threshold.

    The original MATLAB pipeline uses p < .05 / 32.
    """
    return alpha / n_tests


def add_significance_flags(
    results_df,
    p_col="p_value",
    effect_col="effect",
    alpha=0.05,
    n_tests=32,
):
    """
    Add uncorrected and FWE-corrected significance flags to a results table.

    Parameters
    ----------
    results_df : pandas.DataFrame
        A channel-wise statistical results table.
    p_col : str
        Name of the p-value column.
    effect_col : str
        Name of the effect-size or contrast-estimate column.
    alpha : float
        Uncorrected alpha level.
    n_tests : int
        Number of tests used for FWE correction.

    Returns
    -------
    pandas.DataFrame
        Results table with additional significance columns.
    """
    df = results_df.copy()

    fwe_alpha = get_fwe_threshold(alpha=alpha, n_tests=n_tests)

    df["significant_uncorrected"] = df[p_col] < alpha
    df["significant_fwe"] = df[p_col] < fwe_alpha
    df["direction"] = df[effect_col].apply(
        lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
    )

    return df


def get_uncorrected_results(results_df, p_col="p_value", alpha=0.05):
    """
    Return channels significant at the uncorrected alpha level.
    """
    return results_df[results_df[p_col] < alpha].copy()


def get_fwe_corrected_results(results_df, p_col="p_value", alpha=0.05, n_tests=32):
    """
    Return channels significant after FWE correction.
    """
    fwe_alpha = get_fwe_threshold(alpha=alpha, n_tests=n_tests)
    return results_df[results_df[p_col] < fwe_alpha].copy()


def split_positive_negative(results_df, effect_col="effect"):
    """
    Split significant results into positive and negative effects.
    """
    positive = results_df[results_df[effect_col] > 0].copy()
    negative = results_df[results_df[effect_col] < 0].copy()

    return positive, negative


if __name__ == "__main__":
    demo = pd.DataFrame({
        "channel": ["Ch01", "Ch02", "Ch03", "Ch04"],
        "contrast": [
            "G4_6_MA_minus_Control",
            "G4_6_MA_minus_Control",
            "G1_3_MA_minus_Control",
            "Group_difference_MA_minus_Control",
        ],
        "effect": [0.35, -0.22, 0.10, -0.40],
        "p_value": [0.001, 0.030, 0.080, 0.0005],
    })

    demo = add_significance_flags(demo)

    print("FWE threshold:", get_fwe_threshold())
    print("\nDemo results:")
    print(demo)

    print("\nUncorrected significant results:")
    print(get_uncorrected_results(demo))

    print("\nFWE-corrected significant results:")
    print(get_fwe_corrected_results(demo))
