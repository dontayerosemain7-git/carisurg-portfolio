"""
utils.py — Shared utility functions.

Refactored for:
    Week 8 – Reproducibility & Modular Project Design

Purpose
-------
Shared helper functions used across the project.

These utilities intentionally contain no modelling logic.
"""

from __future__ import annotations

from pathlib import Path
from time import perf_counter

import yaml
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import ConfusionMatrixDisplay


# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------

def load_config(config_path: str) -> dict:
    """
    Load a YAML configuration file.

    Parameters
    ----------
    config_path : str

    Returns
    -------
    dict
    """

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# -----------------------------------------------------------------------------
# DIRECTORIES
# -----------------------------------------------------------------------------

def ensure_directory(directory: str | Path) -> None:
    """
    Create a directory if it does not already exist.
    """

    Path(directory).mkdir(
        parents=True,
        exist_ok=True,
    )


# -----------------------------------------------------------------------------
# TIMING
# -----------------------------------------------------------------------------

class Timer:
    """
    Simple timer for benchmarking.

    Example
    -------
    timer = Timer()

    timer.start()

    ...

    elapsed = timer.stop()
    """

    def __init__(self):

        self._start = None

    def start(self):

        self._start = perf_counter()

    def stop(self) -> float:

        if self._start is None:
            raise RuntimeError("Timer has not been started.")

        return perf_counter() - self._start


# -----------------------------------------------------------------------------
# RANDOM SEED
# -----------------------------------------------------------------------------

def set_random_seed(seed: int) -> None:
    """
    Set the NumPy random seed.

    Parameters
    ----------
    seed : int
    """

    np.random.seed(seed)


# -----------------------------------------------------------------------------
# CONFUSION MATRIX
# -----------------------------------------------------------------------------

def save_confusion_matrix(
    cm,
    labels,
    filepath: str,
):
    """
    Save a confusion matrix image.

    Parameters
    ----------
    cm
        Confusion matrix array.

    labels
        Class labels.

    filepath
        Output PNG path.
    """

    output = Path(filepath)

    ensure_directory(output.parent)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=labels,
    )

    fig, ax = plt.subplots(figsize=(7, 6))

    disp.plot(
        ax=ax,
        colorbar=False,
    )

    fig.tight_layout()

    fig.savefig(
        output,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)


# -----------------------------------------------------------------------------
# RESULTS
# -----------------------------------------------------------------------------

def print_metrics(metrics: dict) -> None:
    """
    Pretty-print evaluation metrics.
    """

    print("\nEvaluation Results")
    print("-" * 40)

    print(f"Accuracy          : {metrics['accuracy']:.4f}")
    print(f"Macro Precision   : {metrics['macro_precision']:.4f}")
    print(f"Macro Recall      : {metrics['macro_recall']:.4f}")
    print(f"Macro F1          : {metrics['macro_f1']:.4f}")
    print(f"Weighted F1       : {metrics['weighted_f1']:.4f}")
    print(f"ESI 1 Recall      : {metrics['esi1_recall']:.4f}")

    print("\nClassification Report")
    print("-" * 40)

    print(metrics["classification_report"])


# -----------------------------------------------------------------------------
# FILE VALIDATION
# -----------------------------------------------------------------------------

def check_file_exists(path: str) -> None:
    """
    Raise FileNotFoundError if a file is missing.
    """

    if not Path(path).exists():
        raise FileNotFoundError(path)


# -----------------------------------------------------------------------------
# PROJECT INFORMATION
# -----------------------------------------------------------------------------

def project_banner() -> str:
    """
    Banner displayed when the training pipeline starts.
    """

    return (
        "\n"
        "AI-Assisted Emergency Department Triage\n"
        "Week 8 – Reproducibility & Modular Project Design\n"
        "CarISurg MedTech Pathways\n"
    )


# -----------------------------------------------------------------------------
# MODEL SUMMARY
# -----------------------------------------------------------------------------

def print_model_summary(config: dict) -> None:
    """
    Display the pinned production model.
    """

    print(project_banner())

    print("Pinned Model")
    print("-" * 40)

    print(config["model"]["name"])

    print("\nHyperparameters")

    for key, value in config["hyperparameters"].items():
        print(f"{key}: {value}")


# -----------------------------------------------------------------------------
# CONFIG VALIDATION
# -----------------------------------------------------------------------------

def validate_config(config: dict) -> None:
    """
    Verify required configuration keys are present.
    """

    required = [
        "seed",
        "data",
        "split",
        "model",
        "hyperparameters",
    ]

    missing = [
        key for key in required
        if key not in config
    ]

    if missing:
        raise KeyError(
            f"Missing configuration entries: {missing}"
        )


# -----------------------------------------------------------------------------
# PIPELINE COMPLETE
# -----------------------------------------------------------------------------

def pipeline_complete() -> None:
    """
    Final status message.
    """

    print("\nPipeline completed successfully.")
