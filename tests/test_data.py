"""
test_data.py

Week 8 – Pytest Sanity Checks

Purpose
-------
Verify that the dataset loads correctly and contains the expected
schema before the training pipeline runs.

Run:

    pytest tests/
"""

from pathlib import Path

from src.data import load_dataset
from src.features import build_feature_list


DATASET = Path("data/yaleemmlc_admissionprediction_triage.csv")


def test_dataset_exists():
    """
    Dataset should exist in the expected location.
    """

    assert DATASET.exists(), (
        "Dataset not found. Place "
        "'yaleemmlc_admissionprediction_triage.csv' "
        "inside the data/ folder."
    )


def test_dataset_loads():
    """
    Dataset should load successfully.
    """

    df = load_dataset(DATASET)

    assert not df.empty


def test_target_column_exists():
    """
    Verify that the target column exists.
    """

    df = load_dataset(DATASET)

    assert "esi" in df.columns


def test_expected_vital_columns_exist():
    """
    Verify that all expected vital-sign columns exist.
    """

    df = load_dataset(DATASET)

    required_columns = [
        "triage_vital_hr",
        "triage_vital_sbp",
        "triage_vital_dbp",
        "triage_vital_rr",
        "triage_vital_o2",
        "triage_vital_temp",
        "triage_glucose",
        "age",
    ]

    for column in required_columns:
        assert column in df.columns


def test_feature_list_is_valid():
    """
    Every generated modelling feature should exist in the dataset.
    """

    df = load_dataset(DATASET)

    features = build_feature_list(df)

    assert len(features) > 0

    missing = [c for c in features if c not in df.columns]

    assert missing == []


def test_dataset_has_rows_and_columns():
    """
    Dataset should contain observations and variables.
    """

    df = load_dataset(DATASET)

    assert df.shape[0] > 0
    assert df.shape[1] > 0
