"""
model.py — Model training and evaluation functions.

Refactored from:
  - notebooks/week6_final_notebook.ipynb  (LR, DT, Dummy classifiers)
  - notebooks/week7_final_notebook.ipynb  (Random Forest, benchmark table)

All functions have explicit named parameters and produce no side effects at
import time. No globals, no top-level print statements.

Pinned model: Logistic Regression (Week 7 decision).
Justification: highest ESI 1 Recall (0.6250) across all models evaluated.
Full reasoning in docs/decisions/2026-week-7-model-choice.md.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


# ── ESI CLASS LABELS ──────────────────────────────────────────────────────────

ESI_LABELS      = [1.0, 2.0, 3.0, 4.0, 5.0]
ESI_LABEL_NAMES = ["ESI 1", "ESI 2", "ESI 3", "ESI 4", "ESI 5"]


# ── TRAINING ──────────────────────────────────────────────────────────────────

def train_dummy(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42,
) -> DummyClassifier:
    """
    Train a stratified random dummy classifier (floor baseline).

    Parameters
    ----------
    X_train : pd.DataFrame
    y_train : pd.Series
    random_state : int

    Returns
    -------
    DummyClassifier
        Fitted dummy classifier.
    """
    clf = DummyClassifier(strategy="stratified", random_state=random_state)
    clf.fit(X_train, y_train)
    return clf


def train_logistic_regression(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42,
    max_iter: int = 1000,
    class_weight: str = "balanced",
    solver: str = "lbfgs",
) -> LogisticRegression:
    """
    Train a Logistic Regression classifier.

    This is the pinned Phase 3 model (Week 7 decision). Uses balanced class
    weights to correct for ESI class imbalance (ESI 1: 77 patients vs
    ESI 3: 27,010 in the full dataset).

    Parameters
    ----------
    X_train : pd.DataFrame
    y_train : pd.Series
    random_state : int
        Defaults to 42.
    max_iter : int
        Maximum iterations for convergence. Defaults to 1000.
    class_weight : str
        Weight strategy. Defaults to 'balanced'.
    solver : str
        Optimisation solver. Defaults to 'lbfgs'.

    Returns
    -------
    LogisticRegression
        Fitted logistic regression classifier.
    """
    clf = LogisticRegression(
        max_iter=max_iter,
        random_state=random_state,
        class_weight=class_weight,
        solver=solver,
    )
    clf.fit(X_train, y_train)
    return clf


def train_decision_tree(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42,
    max_depth: int = 8,
    class_weight: str = "balanced",
) -> DecisionTreeClassifier:
    """
    Train a Decision Tree classifier.

    Used as a Week 6 baseline. max_depth=8 is bounded to prevent overfitting
    on 208 features.

    Parameters
    ----------
    X_train : pd.DataFrame
    y_train : pd.Series
    random_state : int
    max_depth : int
        Maximum tree depth. Defaults to 8.
    class_weight : str

    Returns
    -------
    DecisionTreeClassifier
        Fitted decision tree.
    """
    clf = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=random_state,
        class_weight=class_weight,
    )
    clf.fit(X_train, y_train)
    return clf


def train_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42,
    n_estimators: int = 200,
    max_depth: int = 12,
    min_samples_leaf: int = 5,
    class_weight: str = "balanced",
    n_jobs: int = -1,
) -> RandomForestClassifier:
    """
    Train a Random Forest classifier.

    Used as the Week 7 complex model. Does not outperform Logistic Regression
    on the primary metric (ESI 1 Recall: 0.5000 vs 0.6250) — LR retained
    as the recommended model.

    Parameters
    ----------
    X_train : pd.DataFrame
    y_train : pd.Series
    random_state : int
    n_estimators : int
        Number of trees. Defaults to 200.
    max_depth : int
        Maximum tree depth. Defaults to 12.
    min_samples_leaf : int
        Minimum samples per leaf. Defaults to 5.
    class_weight : str
    n_jobs : int
        Parallel jobs. -1 uses all available cores.

    Returns
    -------
    RandomForestClassifier
        Fitted random forest.
    """
    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        class_weight=class_weight,
        random_state=random_state,
        n_jobs=n_jobs,
    )
    clf.fit(X_train, y_train)
    return clf


# ── EVALUATION ────────────────────────────────────────────────────────────────

def evaluate_model(
    y_true: pd.Series,
    y_pred: np.ndarray,
    labels: list = None,
    label_names: list = None,
) -> dict:
    """
    Compute standard evaluation metrics for a fitted classifier.

    Parameters
    ----------
    y_true : pd.Series
        Ground truth labels.
    y_pred : np.ndarray
        Model predictions.
    labels : list, optional
        Ordered list of class label values. Defaults to ESI_LABELS.
    label_names : list, optional
        Human-readable class names. Defaults to ESI_LABEL_NAMES.

    Returns
    -------
    dict
        Dictionary with keys: accuracy, macro_precision, macro_recall,
        macro_f1, weighted_f1, esi1_recall, classification_report.
    """
    if labels is None:
        labels = ESI_LABELS
    if label_names is None:
        label_names = ESI_LABEL_NAMES

    return {
        "accuracy":              round(accuracy_score(y_true, y_pred), 4),
        "macro_precision":       round(precision_score(y_true, y_pred, average="macro",    zero_division=0), 4),
        "macro_recall":          round(recall_score(y_true, y_pred,    average="macro",    zero_division=0), 4),
        "macro_f1":              round(f1_score(y_true, y_pred,        average="macro",    zero_division=0), 4),
        "weighted_f1":           round(f1_score(y_true, y_pred,        average="weighted", zero_division=0), 4),
        "esi1_recall":           round(recall_score(y_true, y_pred, labels=[1.0], average="macro", zero_division=0), 4),
        "classification_report": classification_report(
            y_true, y_pred, labels=labels, target_names=label_names, digits=4
        ),
    }


def get_esi1_recall(
    y_true: pd.Series,
    y_pred: np.ndarray,
) -> float:
    """
    Return ESI Level 1 recall — the primary clinical metric.

    ESI 1 = Immediate danger. Missing an ESI 1 patient (false negative) means
    a critically ill patient joins a queue intended for less urgent cases.
    This is the metric used to select the Phase 3 model.

    Parameters
    ----------
    y_true : pd.Series
    y_pred : np.ndarray

    Returns
    -------
    float
        ESI 1 recall, rounded to 4 decimal places.
    """
    return round(
        recall_score(y_true, y_pred, labels=[1.0], average="macro", zero_division=0),
        4,
    )


def get_confusion_matrix(
    y_true: pd.Series,
    y_pred: np.ndarray,
    labels: list = None,
) -> np.ndarray:
    """
    Return a confusion matrix with ESI class labels.

    Parameters
    ----------
    y_true : pd.Series
    y_pred : np.ndarray
    labels : list, optional
        Defaults to ESI_LABELS.

    Returns
    -------
    np.ndarray
        Confusion matrix array.
    """
    if labels is None:
        labels = ESI_LABELS
    return confusion_matrix(y_true, y_pred, labels=labels)
