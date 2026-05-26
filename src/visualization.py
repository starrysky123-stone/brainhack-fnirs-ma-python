"""
Visualization helper functions for the Python-based fNIRS MA analysis pipeline.

This module provides simplified channel-level visualization functions.

The original MATLAB pipeline visualizes significant channels on a 3D brain template.
For the BrainHack Python version, we first implement a simplified channel map using
channel-level results. A more advanced brain-template visualization can be added later.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_demo_channel_layout(n_channels=32, n_cols=8):
    """
    Create a simple 2D channel layout for demonstration.

    This is not a real anatomical layout. It is only used to visualize
    channel-wise statistical results in a reproducible way.
    """
    rows = []

    for idx in range(n_channels):
        channel_number = idx + 1
        channel = f"Ch{channel_number:02d}"

        x = idx % n_cols
        y = -(idx // n_cols)

        rows.append({
            "channel": channel,
            "x": x,
            "y": y,
        })

    return pd.DataFrame(rows)


def merge_results_with_layout(results_df, layout_df, channel_col="channel"):
    """
    Merge channel-wise statistical results with channel layout information.
    """
    merged = results_df.merge(layout_df, on=channel_col, how="left")

    missing = merged[merged["x"].isna()][channel_col].tolist()
    if missing:
        raise ValueError(f"Missing layout information for channels: {missing}")

    return merged


def plot_channel_effects(
    results_df,
    layout_df,
    effect_col="effect",
    p_col="p_value",
    title="Channel-level effects",
    save_path=None,
):
    """
    Plot channel-level effect values on a simple 2D channel layout.

    Parameters
    ----------
    results_df : pandas.DataFrame
        Channel-wise results table.
    layout_df : pandas.DataFrame
        Channel layout table with columns: channel, x, y.
    effect_col : str
        Column containing effect or contrast estimate.
    p_col : str
        Column containing p-values.
    title : str
        Figure title.
    save_path : str or pathlib.Path, optional
        Path for saving the figure.

    Returns
    -------
    matplotlib.figure.Figure
        The generated figure.
    """
    df = merge_results_with_layout(results_df, layout_df)

    fig, ax = plt.subplots(figsize=(8, 5))

    scatter = ax.scatter(
        df["x"],
        df["y"],
        s=250,
        c=df[effect_col],
    )

    for _, row in df.iterrows():
        ax.text(
            row["x"],
            row["y"],
            row["channel"],
            ha="center",
            va="center",
            fontsize=8,
        )

    ax.set_title(title)
    ax.set_xlabel("Approximate channel position")
    ax.set_ylabel("Approximate channel row")
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label(effect_col)

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig


def plot_significant_channels(
    results_df,
    layout_df,
    significance_col="significant_fwe",
    direction_col="direction",
    title="Significant channels",
    save_path=None,
):
    """
    Plot significant positive and negative channels on a simple 2D layout.

    Non-significant channels are shown as background points.
    Significant positive and negative channels are marked separately.
    """
    df = merge_results_with_layout(results_df, layout_df)

    fig, ax = plt.subplots(figsize=(8, 5))

    nonsig = df[~df[significance_col]]
    positive = df[(df[significance_col]) & (df[direction_col] == "positive")]
    negative = df[(df[significance_col]) & (df[direction_col] == "negative")]

    ax.scatter(nonsig["x"], nonsig["y"], s=120, alpha=0.35, label="Not significant")
    ax.scatter(positive["x"], positive["y"], s=260, marker="o", label="Positive significant")
    ax.scatter(negative["x"], negative["y"], s=260, marker="s", label="Negative significant")

    for _, row in df.iterrows():
        ax.text(
            row["x"],
            row["y"],
            row["channel"],
            ha="center",
            va="center",
            fontsize=8,
        )

    ax.set_title(title)
    ax.set_xlabel("Approximate channel position")
    ax.set_ylabel("Approximate channel row")
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc="best")

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig


if __name__ == "__main__":
    demo_results = pd.DataFrame({
        "channel": [f"Ch{i:02d}" for i in range(1, 33)],
        "effect": [0.0] * 32,
        "p_value": [0.10] * 32,
        "significant_fwe": [False] * 32,
        "direction": ["zero"] * 32,
    })

    demo_results.loc[0, ["effect", "p_value", "significant_fwe", "direction"]] = [
        0.55, 0.0008, True, "positive"
    ]
    demo_results.loc[10, ["effect", "p_value", "significant_fwe", "direction"]] = [
        -0.48, 0.0010, True, "negative"
    ]

    layout = create_demo_channel_layout(n_channels=32)

    plot_channel_effects(
        demo_results,
        layout,
        title="Demo channel-level effects",
        save_path="figures/channel_plots/demo_channel_effects.png",
    )

    plot_significant_channels(
        demo_results,
        layout,
        title="Demo FWE-significant channels",
        save_path="figures/channel_plots/demo_significant_channels.png",
    )

    print("Saved demo figures to figures/channel_plots/")
