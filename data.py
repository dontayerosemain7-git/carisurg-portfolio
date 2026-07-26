"""
data.py — Dataset loading and cleaning functions.

Refactored from:
  - notebooks/week0_final_notebook.ipynb  (Gender, DBP cleaning)
  - notebooks/week5_final_notebook.ipynb  (Yale dataset loading, feature selection)
  - notebooks/week6_final_notebook.ipynb  (train/test split)

All functions have explicit named parameters and produce no side effects at import time.
No globals, no top-level print statements.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# ── FEATURE CONFIGURATION ─────────────────────────────────────────────────────

VITAL_COLS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
    "triage_glucose",
]

TARGET_COL = "esi"


# ── LOADING ───────────────────────────────────────────────────────────────────

def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Load the Yale EMMLC triage CSV into a DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Raw dataset as loaded from disk. No cleaning applied.

    Raises
    ------
    FileNotFoundError
        If the path does not exist.
    ValueError
        If the loaded file is empty.
    """
    df = pd.read_csv(filepath)
    if df.empty:
        raise ValueError(f"Loaded dataset from '{filepath}' is empty.")
    return df


# ── FEATURE SELECTION ─────────────────────────────────────────────────────────

def get_feature_cols(df: pd.DataFrame) -> list:
    """
    Return the ordered list of feature column names used for modelling.

    Includes all seven triage vitals, patient age, and all chief complaint
    binary columns (columns whose names begin with 'cc_').

    Insurance status and employment status are intentionally excluded — both
    variables correlate with race and socioeconomic position and carry
    proxy-variable bias risk documented in the Week 4 risk register
    (Obermeyer et al., 2019).

    Parameters
    ----------
    df : pd.DataFrame
        The dataset. Used to detect cc_* columns dynamically.

    Returns
    -------
    list
        Ordered list of feature column names.
    """
    cc_cols = sorted([c for c in df.columns if c.startswith("cc_")])
    return VITAL_COLS + ["age"] + cc_cols


def get_X_y(
    df: pd.DataFrame,
    feature_cols: list = None,
    target_col: str = TARGET_COL,
) -> tuple:
    """
    Extract feature matrix X and target vector y from a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset.
    feature_cols : list, optional
        Columns to use as features. If None, derived via get_feature_cols(df).
    target_col : str, optional
        Name of the target column. Defaults to 'esi'.

    Returns
    -------
    tuple[pd.DataFrame, pd.Series]
        (X, y) — feature matrix and target vector.

    Raises
    ------
    ValueError
        If target_col is not present in df, or if any feature_col is missing.
    """
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in dataset.")

    if feature_cols is None:
        feature_cols = get_feature_cols(df)

    missing = [c for c in feature_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Feature columns not found in dataset: {missing}")

    X = df[feature_cols].copy()
    y = df[target_col].copy()
    return X, y


# ── CLEANING — GENDER (Week 0) ────────────────────────────────────────────────

GENDER_MAPPING = {
    "Male": 1, "male": 1, "M": 1, "m": 1,
    "Female": 0, "female": 0, "F": 0, "f": 0,
}


def clean_gender(
    df: pd.DataFrame,
    col: str = "Gender",
    output_col: str = "Gender_clean",
    mapping: dict = None,
) -> pd.DataFrame:
    """
    Standardise the Gender column to binary format (1=Male, 0=Female).

    Refactored from Week 0 notebook. The original column is replaced by
    output_col after mapping. Any variant not found in the mapping becomes NaN.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset. Modified copy is returned.
    col : str
        Name of the raw gender column. Defaults to 'Gender'.
    output_col : str
        Name for the cleaned output column. Defaults to 'Gender_clean'.
    mapping : dict, optional
        Custom string-to-int mapping. Defaults to GENDER_MAPPING.

    Returns
    -------
    pd.DataFrame
        Dataset with the raw column replaced by output_col.
    """
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in dataset.")

    if mapping is None:
        mapping = GENDER_MAPPING

    df = df.copy()
    df[col] = df[col].map(mapping)
    df = df.rename(columns={col: output_col})
    return df


# ── CLEANING — DBP (Week 0 / Week 2) ─────────────────────────────────────────

def clean_dbp(
    df: pd.DataFrame,
    col: str = "DBP",
    lower_bound: float = 30.0,
    upper_bound: float = 150.0,
) -> pd.DataFrame:
    """
    Clean the Diastolic Blood Pressure column.

    Converts the column to numeric, replaces values outside the valid clinical
    range [lower_bound, upper_bound] with NaN, then imputes NaN values with
    the column median.

    Valid clinical range 30–150 mmHg is the same range used in the Week 2
    cleaning notebook and justified in the Week 3 clinical context write-up.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset. Modified copy is returned.
    col : str
        Name of the DBP column. Defaults to 'DBP'.
    lower_bound : float
        Minimum clinically valid DBP. Defaults to 30.0.
    upper_bound : float
        Maximum clinically valid DBP. Defaults to 150.0.

    Returns
    -------
    pd.DataFrame
        Dataset with the DBP column cleaned and imputed.
    """
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in dataset.")

    df = df.copy()
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df.loc[df[col] < lower_bound, col] = float("nan")
    df.loc[df[col] > upper_bound, col] = float("nan")
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)
    return df


# ── SPLITTING ─────────────────────────────────────────────────────────────────

def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.20,
    random_state: int = 42,
) -> tuple:
    """
    Split features and target into stratified train and test sets.

    Stratification is applied on y to preserve class proportions — critical
    for ESI 1 (n=77 in the full dataset) which would be underrepresented
    or absent from the test set without stratification.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix.
    y : pd.Series
        Target vector.
    test_size : float
        Proportion of data to reserve for testing. Defaults to 0.20.
    random_state : int
        Random seed for reproducibility. Defaults to 42.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]
        (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )
