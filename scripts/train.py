"""
train.py — Production training entry point.

Week 8 – Reproducibility & Modular Project Design

Run:

    python scripts/train.py --config config.yaml

This script orchestrates the complete machine learning pipeline.

The modelling logic remains identical to the Week 7 notebook.
"""

from __future__ import annotations

import argparse

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
    get_confusion_matrix,
    ESI_LABEL_NAMES,
)

from src.utils import (
    load_config,
    validate_config,
    check_file_exists,
    print_model_summary,
    print_metrics,
    save_confusion_matrix,
    pipeline_complete,
    set_random_seed,
)


# -----------------------------------------------------------------------------
# TRAINING PIPELINE
# -----------------------------------------------------------------------------

def run_pipeline(config_path: str) -> None:
    """
    Execute the complete production pipeline.
    """

    # -------------------------------------------------------------------------
    # CONFIG
    # -------------------------------------------------------------------------

    config = load_config(config_path)

    validate_config(config)

    print_model_summary(config)

    set_random_seed(config["seed"])

    # -------------------------------------------------------------------------
    # DATA
    # -------------------------------------------------------------------------

    dataset_path = config["data"]["path"]

    check_file_exists(dataset_path)

    df = load_dataset(dataset_path)

    # -------------------------------------------------------------------------
    # FEATURES
    # -------------------------------------------------------------------------

    X, y = engineer_features(df)

    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        test_size=config["split"]["test_size"],
        random_state=config["seed"],
    )

    X_train, X_test, scaler = fit_transform_features(
        X_train,
        X_test,
    )

    # -------------------------------------------------------------------------
    # MODEL
    # -------------------------------------------------------------------------

    model = train_logistic_regression(
        X_train=X_train,
        y_train=y_train,
        random_state=config["hyperparameters"]["random_state"],
        max_iter=config["hyperparameters"]["max_iter"],
        class_weight=config["hyperparameters"]["class_weight"],
        solver=config["hyperparameters"]["solver"],
    )

    # -------------------------------------------------------------------------
    # PREDICTION
    # -------------------------------------------------------------------------

    predictions = model.predict(X_test)

    # -------------------------------------------------------------------------
    # METRICS
    # -------------------------------------------------------------------------

    metrics = evaluate_model(
        y_true=y_test,
        y_pred=predictions,
    )

    print_metrics(metrics)

    # -------------------------------------------------------------------------
    # CONFUSION MATRIX
    # -------------------------------------------------------------------------

    cm = get_confusion_matrix(
        y_true=y_test,
        y_pred=predictions,
    )

    if config["output"]["save_confusion_matrix"]:

        save_confusion_matrix(
            cm=cm,
            labels=ESI_LABEL_NAMES,
            filepath=config["output"]["confusion_matrix_path"],
        )

        print(
            f"\nConfusion matrix saved to "
            f"{config['output']['confusion_matrix_path']}"
        )

    pipeline_complete()


# -----------------------------------------------------------------------------
# COMMAND LINE INTERFACE
# -----------------------------------------------------------------------------

def parse_args():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Train the AI-Assisted ED Triage model."
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to config.yaml",
    )

    return parser.parse_args()


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def main():
    """
    Application entry point.
    """

    args = parse_args()

    run_pipeline(args.config)


if __name__ == "__main__":
    main()
