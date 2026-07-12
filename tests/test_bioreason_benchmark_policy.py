"""Regression tests for the audited BioReason benchmark denominator."""
from __future__ import annotations

import csv
import importlib.util
import json
import re
from pathlib import Path

import yaml

from ai_gene_review.bioreason_ontology import (
    FROZEN_GO_ADAPTER,
    GO_RELEASE,
    GO_RELEASE_URL,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = REPO_ROOT / "projects" / "BIOREASON_COMPARISON"
SCORE_RE = re.compile(
    r"\*\*(Correctness|Completeness)\*\*:\s*([1-5])\s*/\s*5",
    re.IGNORECASE,
)


def _load_sidecar_module():
    path = PROJECT_DIR / "write_benchmark_sidecars.py"
    spec = importlib.util.spec_from_file_location("write_benchmark_sidecars", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_argo139_quality_policy_is_complete_and_explicit() -> None:
    module = _load_sidecar_module()
    policy = yaml.safe_load((PROJECT_DIR / "benchmark-policy.yaml").read_text())
    genes = module.read_rl_gene_list()
    rows = module.rl_quality_rows(genes, policy)

    assert len(rows) == 139
    assert sum(row["performance_included"] == "true" for row in rows) == 138
    assert [
        (row["organism"], row["gene"], row["exclusion_reason"])
        for row in rows
        if row["performance_included"] == "false"
    ] == [("worm", "csr-1", "WRONG_INPUT_SEQUENCE")]


def test_benchmark_and_refresh_commands_share_frozen_go_release() -> None:
    policy = yaml.safe_load((PROJECT_DIR / "benchmark-policy.yaml").read_text())
    frozen = policy["cohorts"]["argo139_rl_narrative"]["frozen_inputs"]

    assert frozen["ontology_release"] == GO_RELEASE
    assert frozen["ontology_url"] == GO_RELEASE_URL
    assert FROZEN_GO_ADAPTER == "frozen-go-2026-03-25"


def test_argo139_truncated_sequences_are_flagged_not_excluded() -> None:
    module = _load_sidecar_module()
    policy = yaml.safe_load((PROJECT_DIR / "benchmark-policy.yaml").read_text())
    rows = module.rl_quality_rows(module.read_rl_gene_list(), policy)
    truncated = {
        (row["organism"], row["gene"])
        for row in rows
        if row["input_quality"] == "TRUNCATED_AT_MODEL_LIMIT"
    }

    assert truncated == {
        ("DROME", "Dscam1"),
        ("human", "BRCA2"),
        ("human", "HTT"),
        ("human", "LRRK2"),
        ("human", "NOTCH1"),
        ("mouse", "Notch1"),
        ("yeast", "TOR1"),
    }
    assert all(
        row["performance_included"] == "true"
        for row in rows
        if row["input_quality"] == "TRUNCATED_AT_MODEL_LIMIT"
    )


def test_generated_sidecars_match_current_sources(tmp_path: Path) -> None:
    module = _load_sidecar_module()
    module.main(tmp_path)

    for filename in (
        "benchmark-cohorts.csv",
        "benchmark-genes.csv",
        "benchmark-quality.csv",
        "benchmark-metrics.json",
    ):
        assert (tmp_path / filename).read_bytes() == (PROJECT_DIR / filename).read_bytes(), (
            f"{filename} is stale; run "
            "python projects/BIOREASON_COMPARISON/write_benchmark_sidecars.py"
        )


def test_generated_quality_sidecar_has_expected_denominators() -> None:
    with (PROJECT_DIR / "benchmark-quality.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 139
    assert sum(row["performance_included"] == "true" for row in rows) == 138
    assert sum(row["input_quality"] != "FULL_LENGTH_MATCH" for row in rows) == 8
    assert sum(row["interpro_input_present"] == "true" for row in rows) == 136
    assert sum(row["gogpt_input_present"] == "true" for row in rows) == 139
    assert all(row["goa_latest_annotation_date"] for row in rows)


def test_all_narrative_reviews_have_two_in_range_scores() -> None:
    for kind, expected in (("rl", 139), ("sft", 45)):
        paths = sorted(REPO_ROOT.glob(f"genes/*/*/*bioreason-{kind}-review.md"))
        assert len(paths) == expected
        for path in paths:
            scores = {name.lower(): int(value) for name, value in SCORE_RE.findall(path.read_text())}
            assert scores.keys() == {"correctness", "completeness"}, path


def test_second_review_sample_and_metrics_are_current() -> None:
    path = PROJECT_DIR / "analyze_second_review.py"
    spec = importlib.util.spec_from_file_location("analyze_second_review", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    expected = module.analyze(REPO_ROOT)
    committed = json.loads(
        (PROJECT_DIR / "second-review-agreement.json").read_text()
    )
    assert committed == json.loads(json.dumps(expected))


def test_publication_headlines_match_generated_metrics() -> None:
    metrics = json.loads((PROJECT_DIR / "benchmark-metrics.json").read_text())
    rl = metrics["rl_narrative"]
    sft = metrics["argo95_sft_terms"]
    gogpt = metrics["argo139_gogpt_terms"]
    project = (REPO_ROOT / "projects" / "BIOREASON_COMPARISON.md").read_text()
    manuscript = (PROJECT_DIR / "article" / "manuscript.tex").read_text()
    supplement = (PROJECT_DIR / "article" / "supplemental-benchmark-details.md").read_text()
    slides = (PROJECT_DIR / "article" / "slides.md").read_text()

    assert (
        f"**Overall correctness: {rl['mean_correctness']:.1f}/5** | "
        f"**Overall completeness: {rl['mean_completeness']:.1f}/5**"
    ) in project
    for score in range(5, 0, -1):
        correctness = rl["correctness_distribution"].get(str(score), 0)
        completeness = rl["completeness_distribution"].get(str(score), 0)
        c_text = f"{correctness} ({round(100 * correctness / rl['n'])}%)"
        p_text = f"{completeness} ({round(100 * completeness / rl['n'])}%)"
        c_tex = c_text.replace("%", "\\%")
        p_tex = p_text.replace("%", "\\%")
        assert f"| {score} | {c_text} | {p_text} |" in project
        assert f"{score} & {c_tex} & {p_tex}" in manuscript

    assessments = sft["assessment_distribution"]
    assert all(
        f"{assessments[category]} ({100 * assessments[category] / sft['n_predictions']:.1f}%)"
        in supplement
        for category in ("CNN", "NPI", "PLI", "COR", "LSP", "REP", "UNC")
    )
    assert all(
        f"{value:,}" in project
        for value in (
            gogpt["n_predictions"],
            gogpt["assessment_distribution"]["CNN"],
            gogpt["assessment_distribution"]["NPI"],
            gogpt["assessment_distribution"]["UNC"],
        )
    )
    assert sft["cnn_exact_frozen_goa"] == 629
    assert sft["cnn_other_established_basis"] == 29
    assert sft["cor_exact_frozen_goa"] == 0
    assert sft["ontology_pair_adjudication"] == {
        "n_reviewed": 76,
        "n_changed": 56,
    }
    assert all(f"{value:,}" in project for value in assessments.values())

    categories = ("CNN", "NPI", "PLI", "COR", "LSP", "REP", "UNC")
    for key in (
        "argo95_sft_terms",
        "supplement_sft_terms_argo139_mixed_sources",
    ):
        summary = metrics[key]
        cells = []
        for category in categories:
            count = summary["assessment_distribution"].get(category, 0)
            percent = 100 * count / summary["n_predictions"]
            cells.append(f"{count:,} ({percent:.1f}%)")
        assert " | ".join(cells) in supplement

    for key in (
        "supplement_sft_terms_hf_catalogue_all",
        "supplement_sft_terms_union_all",
    ):
        summary = metrics[key]
        for category in categories:
            count = summary["assessment_distribution"].get(category, 0)
            percent = 100 * count / summary["n_predictions"]
            assert f"| {category} | {count:,} | {percent:.1f} |" in supplement

    overlap = metrics["supplement_gogpt_overlap_300"]
    assert overlap["n_genes"] == 300
    assert overlap["n_predictions"] == 8910
    assert (
        f"| Raw GOA | {overlap['goa']['n_reference_terms']:,} | "
        f"{overlap['goa']['n_overlap']:,} | 11.7 |"
    ) in supplement
    assert (
        f"| All GO-valued AIGR core-function slots | "
        f"{overlap['core']['n_reference_terms']:,} | "
        f"{overlap['core']['n_overlap']:,} | 3.8 |"
    ) in supplement
    assert "**68.9% CNN**" in slides
    assert "**16.6% NPI/PLI/REP**" in slides
