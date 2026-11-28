"""Tests over the benchmarks committed under benchmarks/ (no network).

The benchmark code is the ``aigr-benchmark`` workspace package
(``packages/aigr-benchmark``); its own unit tests live there. These tests check
this repository's data with it, through ``ai-gene-review benchmark``.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from aigr_benchmark.checks import SCHEMA, validate_schema
from aigr_benchmark.predictions import read_prediction_set, verdicts
from aigr_benchmark.run import score
from ai_gene_review.cli import app

EXAMPLE = Path("benchmarks/human-goa-2025-06")


SUFFIX_CLASSES = {
    "-spec.yaml": "BenchmarkSpec",
    "-check-report.yaml": "CheckReport",
    "-agent-evaluation.yaml": "AgentEvaluation",
    "-scores.yaml": "ScoreReport",
}


def committed_benchmark_files() -> list[tuple[Path, str]]:
    """Every committed benchmark document with its schema class."""
    out = []
    for path in sorted(Path("benchmarks").glob("*/*.yaml")):
        cls = next(
            (c for suffix, c in SUFFIX_CLASSES.items() if path.name.endswith(suffix)),
            None,
        )
        out.append(
            (path, cls or ("Benchmark" if path.stem == path.parent.name else ""))
        )
    return out


@pytest.mark.parametrize("path,cls", committed_benchmark_files(), ids=lambda v: str(v))
def test_committed_benchmark_files_validate(path: Path, cls: str) -> None:
    assert cls, f"{path} has no recognised benchmark file name"
    result = CliRunner().invoke(app, ["benchmark", "validate", str(path), "--class", cls])
    assert result.exit_code == 0, result.output


def test_example_is_committed() -> None:
    names = {p.name for p, _ in committed_benchmark_files()}
    assert {"human-goa-2025-06.yaml", "human-goa-2025-06-check-report.yaml"} <= names


def test_example_report_has_no_failures() -> None:
    report = yaml.safe_load(
        (EXAMPLE / "human-goa-2025-06-check-report.yaml").read_text()
    )
    assert all(s["failed"] == 0 for s in report["summary"])
    assert json.dumps(report["stats"])  # serialisable


@pytest.mark.parametrize("suffix", ["-check-report.yaml", "-scores.yaml"])
def test_committed_reports_match_their_benchmark(suffix: str) -> None:
    """A committed report must describe the committed benchmark, not an earlier draw."""
    for bench_path in sorted(Path("benchmarks").glob("*/*.yaml")):
        if bench_path.stem != bench_path.parent.name:
            continue
        report_path = bench_path.with_name(bench_path.stem + suffix)
        if not report_path.exists():
            continue
        bench = yaml.safe_load(bench_path.read_text())
        report = yaml.safe_load(report_path.read_text())
        assert report["benchmark_id"] == bench["id"]
        items = bench["items"]
        targets = [t for i in items for t in i["target_annotations"]]
        if suffix == "-check-report.yaml":
            assert report["stats"]["n_items"] == len(items)
            assert report["stats"]["n_targets"] == len(targets)
        else:
            ids = {i["id"] for i in items}
            assert {r["item_id"] for r in report["item_scores"]} <= ids
            decoys = sum(len(i.get("decoys") or []) for i in items)
            for row in report["condition_scores"]:
                if row["role"] == "DECOY":
                    assert row["n"] == decoys


def committed_prediction_files() -> list[Path]:
    return sorted(Path("benchmarks").glob("*/predictions/*"))


@pytest.mark.parametrize("path", committed_prediction_files(), ids=str)
def test_committed_predictions_validate(path: Path) -> None:
    result = CliRunner().invoke(
        app, ["benchmark", "validate", str(path), "--class", "PredictionSet"]
    )
    assert result.exit_code == 0, result.output


@pytest.mark.parametrize("path", committed_prediction_files(), ids=str)
def test_committed_predictions_parse_with_pydantic(path: Path) -> None:
    from aigr_benchmark.datamodel.benchmark_model import Prediction

    for record in read_prediction_set(path)["predictions"]:
        assert Prediction.model_validate(record).item_id == record["item_id"]


def test_committed_scores_reproduce_from_committed_predictions() -> None:
    """The committed score report is exactly what its committed prediction files give."""
    for scores_path in sorted(Path("benchmarks").glob("*/*-scores.yaml")):
        report = yaml.safe_load(scores_path.read_text())
        bench_path = scores_path.with_name(f"{report['benchmark_id']}.yaml")
        files = [Path(i.split(" sha256:")[0]) for i in report["inputs"]]
        benchmark = yaml.safe_load(bench_path.read_text())
        predictions = [
            p for path in files for p in read_prediction_set(path)["predictions"]
        ]
        again = score(benchmark, verdicts(benchmark, predictions), [])
        assert again["condition_scores"] == report["condition_scores"]
        assert again["item_scores"] == report["item_scores"]


@pytest.mark.parametrize("bad_date", [None, "2025-13-45", "June 2025"])
def test_bundled_json_schema_matches_linkml_on_the_example(bad_date: str | None) -> None:
    """The example benchmark, with and without a bad date, validates as LinkML says.

    It has date-formatted and date-patterned slots, which the package's own
    data-free equivalence test does not cover.
    """
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    benchmark = yaml.safe_load((EXAMPLE / "human-goa-2025-06.yaml").read_text())
    if bad_date:
        benchmark["spec"]["cutoff_date"] = bad_date
    validator = Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    expected = [r.message for r in validator.validate(benchmark, "Benchmark").results]
    assert sorted(validate_schema(benchmark, "Benchmark")) == sorted(expected)
    assert bool(expected) == bool(bad_date)
