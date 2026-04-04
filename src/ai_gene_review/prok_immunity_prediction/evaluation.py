"""Evaluation utilities for Mordret-style benchmark comparisons."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def load_normalized_benchmark(path: Path) -> pd.DataFrame:
    """Load a normalized benchmark table."""
    dataframe = pd.read_csv(path, sep="\t")
    required = {"protein_id", "is_defense"}
    missing = required.difference(dataframe.columns)
    if missing:
        missing_str = ", ".join(sorted(missing))
        raise ValueError(f"Benchmark is missing required columns: {missing_str}")
    dataframe["is_defense"] = coerce_bool_series(dataframe["is_defense"])
    if "is_novel" not in dataframe.columns:
        dataframe["is_novel"] = False
    else:
        dataframe["is_novel"] = coerce_bool_series(dataframe["is_novel"])
    if "family" not in dataframe.columns:
        dataframe["family"] = ""
    return dataframe


def normalize_benchmark_table(
    input_path: Path,
    output_path: Path,
    protein_id_column: str,
    label_column: str,
    family_column: str | None = None,
    novel_column: str | None = None,
    positive_labels: tuple[str, ...] = ("1", "true", "defense", "known", "positive"),
) -> Path:
    """Convert a raw supplement table into the normalized benchmark schema."""
    dataframe = pd.read_csv(input_path, sep=None, engine="python")
    normalized = pd.DataFrame()
    normalized["protein_id"] = dataframe[protein_id_column].astype(str)
    normalized["is_defense"] = dataframe[label_column].astype(str).str.lower().isin(
        {label.lower() for label in positive_labels}
    )
    normalized["family"] = dataframe[family_column].astype(str) if family_column else ""
    normalized["is_novel"] = (
        dataframe[novel_column].astype(str).str.lower().isin({"1", "true", "novel"})
        if novel_column
        else False
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    normalized.to_csv(output_path, sep="\t", index=False)
    return output_path


def evaluate_predictions(
    predictions_path: Path,
    benchmark_path: Path,
    output_path: Path | None = None,
) -> dict[str, float | int]:
    """Compare pipeline predictions against a normalized benchmark."""
    predictions = pd.read_csv(predictions_path, sep="\t")
    benchmark = load_normalized_benchmark(benchmark_path)

    merged = benchmark.merge(
        predictions[
            [
                "protein_id",
                "predicted_family",
                "family_confidence",
                "predicted_novel",
            ]
        ],
        on="protein_id",
        how="left",
    )
    predicted_novel = coerce_bool_series(merged["predicted_novel"])
    predicted_family = merged["predicted_family"].fillna("").astype(str)
    merged["predicted_positive"] = predicted_family.ne("") | predicted_novel

    tp = int(((merged["is_defense"]) & (merged["predicted_positive"])).sum())
    fp = int((~merged["is_defense"] & merged["predicted_positive"]).sum())
    fn = int((merged["is_defense"] & ~merged["predicted_positive"]).sum())
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    family_subset = merged[(merged["is_defense"]) & (merged["family"].astype(str) != "")]
    family_accuracy = float(
        (
            family_subset["family"].astype(str).str.lower()
            == family_subset["predicted_family"].fillna("").astype(str).str.lower()
        ).mean()
        if not family_subset.empty
        else 0.0
    )

    novel_subset = merged[merged["is_novel"]]
    novel_recall = float(
        (coerce_bool_series(novel_subset["predicted_novel"]).sum() / len(novel_subset))
        if not novel_subset.empty
        else 0.0
    )

    metrics: dict[str, float | int] = {
        "n_benchmark": int(len(benchmark)),
        "n_predictions": int(len(predictions)),
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "family_accuracy": round(family_accuracy, 4),
        "novel_recall": round(novel_recall, 4),
    }

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def coerce_bool_series(series: pd.Series) -> pd.Series:
    """Convert common string/int encodings into booleans."""
    lowered = series.astype("string").fillna("false").str.strip().str.lower()
    return lowered.isin({"1", "true", "t", "yes", "y"})
