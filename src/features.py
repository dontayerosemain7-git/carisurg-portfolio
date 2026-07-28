"""
features.py — Feature engineering functions.

Refactored from:
    - notebooks/week5_final_notebook.ipynb
    - notebooks/week6_final_notebook.ipynb
    - notebooks/week7_final_notebook.ipynb

Purpose
-------
Contains all feature engineering logic used by the production pipeline.

No model training should occur here.

All functions are import-safe:
    - no notebook globals
    - no print statements
    - no side effects at import time
"""

from __future__ import annotations

import pandas as pd

from sklearn.preprocessing import StandardScaler


# -----------------------------------------------------------------------------
# FEATURE CONFIGURATION
# -----------------------------------------------------------------------------

VITAL_COLUMNS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
    "triage_glucose",
]

AGE_COLUMN = "age"

TARGET_COLUMN = "esi"


# -----------------------------------------------------------------------------
# FEATURE DISCOVERY
# -----------------------------------------------------------------------------

def get_chief_complaint_columns(df: pd.DataFrame) -> list[str]:
    """
    Return every one-hot encoded chief complaint column.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    list[str]
    """

    return sorted([c for c in df.columns if c.startswith("cc_")])


def build_feature_list(df: pd.DataFrame) -> list[str]:
    """
    Construct the complete modelling feature list.

    Includes

    - vital signs
    - age
    - chief complaint one-hot columns

    Excludes

    - insurance variables
    - employment variables

    due to proxy-variable bias identified during Week 4.
    """

    return VITAL_COLUMNS + [AGE_COLUMN] + get_chief_complaint_columns(df)


# -----------------------------------------------------------------------------
# FEATURE VALIDATION
# -----------------------------------------------------------------------------

def validate_features(
    df: pd.DataFrame,
    feature_columns: list[str],
) -> None:
    """
    Ensure every modelling feature exists.

    Raises
    ------
    ValueError
        If one or more columns are missing.
    """

    missing = [c for c in feature_columns if c not in df.columns]

    if missing:
        raise ValueError(
            f"Missing feature columns: {missing}"
        )


# -----------------------------------------------------------------------------
# FEATURE EXTRACTION
# -----------------------------------------------------------------------------

def prepare_features(
    df: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
):
    """
    Produce X and y for modelling.

    Parameters
    ----------
    df : DataFrame

    target_column : str

    Returns
    -------
    X, y
    """

    feature_columns = build_feature_list(df)

    validate_features(df, feature_columns)

    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' not found."
        )

    X = df[feature_columns].copy()

    y = df[target_column].copy()

    return X, y


# -----------------------------------------------------------------------------
# NUMERIC SCALING
# -----------------------------------------------------------------------------

def fit_scaler(
    X_train: pd.DataFrame,
) -> StandardScaler:
    """
    Fit a StandardScaler using training data only.
    """

    scaler = StandardScaler()

    scaler.fit(X_train)

    return scaler


def transform_features(
    scaler: StandardScaler,
    X: pd.DataFrame,
) -> pd.DataFrame:
    """
    Transform features using an existing scaler.

    Returns
    -------
    DataFrame
    """

    transformed = scaler.transform(X)

    return pd.DataFrame(
        transformed,
        columns=X.columns,
        index=X.index,
    )


def fit_transform_features(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
):
    """
    Fit scaler on training data and transform both
    train and test datasets.

    Returns
    -------
    X_train_scaled
    X_test_scaled
    scaler
    """

    scaler = fit_scaler(X_train)

    X_train_scaled = transform_features(
        scaler,
        X_train,
    )

    X_test_scaled = transform_features(
        scaler,
        X_test,
    )

    return (
        X_train_scaled,
        X_test_scaled,
        scaler,
    )


# -----------------------------------------------------------------------------
# PIPELINE ENTRY
# -----------------------------------------------------------------------------

def engineer_features(
    df: pd.DataFrame,
):
    """
    Convenience wrapper for the production pipeline.

    Returns
    -------
    X
    y
    """

    return prepare_features(df)


# -----------------------------------------------------------------------------
# SCHEMA CHECK
# -----------------------------------------------------------------------------

def expected_feature_count(
    df: pd.DataFrame,
) -> int:
    """
    Return the expected number of modelling features.

    Useful for pytest schema checks.
    """

    return len(build_feature_list(df))


# -----------------------------------------------------------------------------
# RANDOM SEED PLACEHOLDER
# -----------------------------------------------------------------------------

def get_random_seed(
    config: dict,
) -> int:
    """
    Obtain the random seed from config.

    The production pipeline should define the seed
    in config.yaml rather than hard-coding it.
    """

    return int(config["seed"])
