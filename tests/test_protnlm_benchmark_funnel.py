"""Consistency checks for the ProtNLM2 benchmark-provenance figures."""

import importlib.util
import json
from pathlib import Path
from types import ModuleType

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT = REPO_ROOT / "projects/PROTNLM_EVALUATION"


def load_funnel_module() -> ModuleType:
    """Load the figure generator without running its CLI."""
    path = PROJECT / "build_benchmark_funnel.py"
    spec = importlib.util.spec_from_file_location("benchmark_funnel", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def funnel() -> dict:
    return json.loads((PROJECT / "benchmark-funnel.json").read_text())


@pytest.fixture(scope="module")
def module() -> ModuleType:
    return load_funnel_module()


@pytest.mark.parametrize("stem", ["benchmark-funnel", "benchmark-cohorts", "benchmark-outcomes"])
def test_committed_figures_match_renderer(module: ModuleType, funnel: dict, stem: str) -> None:
    """Editing the JSON without re-rendering (or vice versa) fails here."""
    rendered = module.render_all(funnel)[stem]
    assert rendered == (PROJECT / "figures" / f"{stem}.svg").read_text()


def test_every_summary_cohort_is_described() -> None:
    """A cohort in benchmark-summary.json must appear in the cohort sidecar."""
    summary = json.loads((PROJECT / "benchmark-summary.json").read_text())
    spec = yaml.safe_load((PROJECT / "benchmark-cohorts.yaml").read_text())
    described = {c["id"] for c in spec["cohorts"]} | set(spec["not_drawn_from_release"])
    assert {c["cohort"] for c in summary["cohorts"]} <= described


def test_snapshot_cohort_claims_sum_to_total(funnel: dict) -> None:
    """In-snapshot cohort GO claims add up to the project total (claim-bearing cohorts do not overlap)."""
    in_snapshot = sum(c["go_claims"] for c in funnel["cohorts"] if c["in_snapshot"])
    assert in_snapshot == sum(funnel["go_counts"].values())


def test_outside_set_breakdown_is_consistent(funnel: dict) -> None:
    outside = funnel["prediction_targets_outside_go_set"]
    assert outside["total"] == outside["not_on_list"] + outside["listed_without_go_or_function"]
    assert sum(outside["not_on_list_by_species"].values()) == outside["not_on_list"]


def test_categories_cover_every_count(module: ModuleType, funnel: dict) -> None:
    """No assessment code can silently drop out of the outcome bars."""
    for cohort in funnel["cohorts"]:
        assert set(cohort["go_counts"]) <= set(module.CATEGORIES)
    assert set(funnel["go_counts"]) <= set(module.CATEGORIES)
