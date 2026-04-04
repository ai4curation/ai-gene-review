"""Evaluation utilities for Mordret-style benchmark comparisons."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import pandas as pd

from ai_gene_review.prok_immunity_prediction.classifier import canonicalize_family, load_family_config
from ai_gene_review.prok_immunity_prediction.cross_reference import parse_defense_finder, parse_padloc
from ai_gene_review.prok_immunity_prediction.models import ExternalHit

DATABASE_PARSERS: dict[str, tuple[str, Callable[[Path], list[ExternalHit]]]] = {
    "defensefinder": ("DefenseFinder", parse_defense_finder),
    "padloc": ("PADLOC", parse_padloc),
}


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
    predictions = load_predictions_table(predictions_path)
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

    metrics: dict[str, float | int | str] = {
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


def evaluate_predictions_against_database(
    predictions_path: Path,
    database_dir: Path,
    database: str,
    family_config_path: Path,
    output_path: Path | None = None,
) -> dict[str, float | int | str]:
    """Compare predictions against DefenseFinder or PADLOC results on the same proteome."""
    normalized_database = normalize_database_name(database)
    if normalized_database not in DATABASE_PARSERS:
        valid = ", ".join(sorted(DATABASE_PARSERS))
        raise ValueError(f"Unsupported database '{database}'. Expected one of: {valid}")

    database_label, parser = DATABASE_PARSERS[normalized_database]
    reference_hits = parser(database_dir)
    return evaluate_predictions_against_reference_hits(
        predictions_path=predictions_path,
        reference_hits=reference_hits,
        database_name=database_label,
        family_config_path=family_config_path,
        output_path=output_path,
    )


def evaluate_predictions_against_reference_hits(
    predictions_path: Path,
    reference_hits: list[ExternalHit],
    database_name: str,
    family_config_path: Path,
    output_path: Path | None = None,
) -> dict[str, float | int | str]:
    """Compare predictions against a list of parsed database hits."""
    predictions = load_predictions_table(predictions_path)
    families = load_family_config(family_config_path)
    reference_table = build_reference_table(reference_hits, families=families)

    merged = predictions.merge(reference_table, on="protein_id", how="left")
    merged["reference_family"] = merged["reference_family"].fillna("").astype(str)
    merged["reference_positive"] = merged["reference_family"].ne("")
    merged["predicted_positive"] = merged["predicted_family"].ne("") | merged["predicted_novel"]

    tp = int((merged["predicted_positive"] & merged["reference_positive"]).sum())
    fp = int((merged["predicted_positive"] & ~merged["reference_positive"]).sum())
    fn = int((~merged["predicted_positive"] & merged["reference_positive"]).sum())
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    shared = merged[merged["predicted_positive"] & merged["reference_positive"]].copy()
    comparable_shared = shared[shared["predicted_family"].ne("") & shared["reference_family"].ne("")]
    family_agreement = float(
        (
            comparable_shared["predicted_family"].str.lower()
            == comparable_shared["reference_family"].str.lower()
        ).mean()
        if not comparable_shared.empty
        else 0.0
    )

    metrics: dict[str, float | int | str] = {
        "database": database_name,
        "n_predictions": int(len(predictions)),
        "n_reference_positive": int(reference_table["reference_positive"].sum()) if not reference_table.empty else 0,
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "family_agreement": round(family_agreement, 4),
    }

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        comparison_path = output_path.with_suffix(".comparison.tsv")
        merged.to_csv(comparison_path, sep="\t", index=False)
        metrics["comparison_table"] = str(comparison_path)
        output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def load_predictions_table(path: Path) -> pd.DataFrame:
    """Load the pipeline predictions table and normalize column types."""
    dataframe = pd.read_csv(path, sep="\t")
    required = {"protein_id", "predicted_family"}
    missing = required.difference(dataframe.columns)
    if missing:
        missing_str = ", ".join(sorted(missing))
        raise ValueError(f"Predictions table is missing required columns: {missing_str}")
    dataframe["predicted_family"] = dataframe["predicted_family"].fillna("").astype(str)
    if "predicted_novel" not in dataframe.columns:
        dataframe["predicted_novel"] = False
    dataframe["predicted_novel"] = coerce_bool_series(dataframe["predicted_novel"])
    return dataframe


def build_reference_table(
    reference_hits: list[ExternalHit],
    families: dict[str, object],
) -> pd.DataFrame:
    """Collapse per-hit database evidence into one row per protein."""
    rows: list[dict[str, str]] = []
    for hit in reference_hits:
        label = " ".join(part for part in [hit.system, hit.subtype or "", hit.raw_label or ""] if part)
        canonical = canonicalize_family(label, families) or hit.system or hit.raw_label or hit.subtype or ""
        rows.append(
            {
                "protein_id": hit.protein_id,
                "reference_family": canonical,
                "database": hit.database,
            }
        )

    if not rows:
        return pd.DataFrame(columns=["protein_id", "reference_family", "database", "reference_positive"])

    dataframe = pd.DataFrame(rows)
    collapsed = (
        dataframe.groupby("protein_id", as_index=False)
        .agg(
            reference_family=("reference_family", choose_consensus_label),
            database=("database", lambda values: ",".join(sorted(set(values)))),
        )
    )
    collapsed["reference_positive"] = collapsed["reference_family"].ne("")
    return collapsed


def choose_consensus_label(values: pd.Series) -> str:
    """Choose the most common non-empty family label for a protein."""
    counts = values[values.astype(str) != ""].value_counts()
    if counts.empty:
        return ""
    return str(counts.index[0])


def normalize_database_name(name: str) -> str:
    """Normalize database names for CLI and script usage."""
    return name.lower().replace("-", "").replace("_", "")


def coerce_bool_series(series: pd.Series) -> pd.Series:
    """Convert common string/int encodings into booleans."""
    lowered = series.astype("string").fillna("false").str.strip().str.lower()
    return lowered.isin({"1", "true", "t", "yes", "y"})
