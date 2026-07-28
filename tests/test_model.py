"""
test_model.py

Week 8 – Pytest Sanity Checks

Purpose
-------
Run a lightweight end-to-end smoke test of the machine learning
pipeline.

This test verifies that the pipeline executes without errors on a
small subset of the dataset. It is not intended to assess model
performance.

Run:

    pytest tests/
"""

from pathlib import Path

from src.data import (
    load_dataset,
    split_data,
)

from src.features import (
    engineer_features,
    fit_transform_features,
)

from src.model import (
    train_logistic_regression,
    evaluate_model,
)


DATASET = Path("data/yaleemmlc_admissionprediction_triage.csv")


def test_training_pipeline_smoke():
    """
    Verify the complete training pipeline executes successfully.
    """

    # ------------------------------------------------------------------
    # Load dataset
    # ------------------------------------------------------------------

    df = load_dataset(DATASET)

    # Use a small sample large enough for stratification
    sample_size = min(len(df), 200)

    df = df.sample(
        n=sample_size,
        random_state=42,
    )

    # ------------------------------------------------------------------
    # Feature engineering
    # ------------------------------------------------------------------

    X, y = engineer_features(df)

    # ------------------------------------------------------------------
    # Train/test split
    # ------------------------------------------------------------------

    X_train, X_test, y_train, y_test = split_data(
        X=X,
        y=y,
        test_size=0.20,
        random_state=42,
    )

    # ------------------------------------------------------------------
    # Scale features
    # ------------------------------------------------------------------

    X_train_scaled, X_test_scaled, _ = fit_transform_features(
        X_train,
        X_test,
    )

    # ------------------------------------------------------------------
    # Train model
    # ------------------------------------------------------------------

    model = train_logistic_regression(
        X_train=X_train_scaled,
        y_train=y_train,
        random_state=42,
        max_iter=1000,
        solver="lbfgs",
        class_weight="balanced",
    )

    # ------------------------------------------------------------------
    # Predictions
    # ------------------------------------------------------------------

    predictions = model.predict(X_test_scaled)

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    metrics = evaluate_model(
        y_true=y_test,
        y_pred=predictions,
    )

    # ------------------------------------------------------------------
    # Assertions
    # ------------------------------------------------------------------

    assert model is not None

    assert len(predictions) == len(y_test)

    assert isinstance(metrics, dict)

    required_metrics = [
        "accuracy",
        "macro_precision",
        "macro_recall",
        "macro_f1",
        "weighted_f1",
        "esi1_recall",
    ]

    for metric in required_metrics:
        assert metric in metrics
        assert 0.0 <= metrics[metric] <= 1.0
