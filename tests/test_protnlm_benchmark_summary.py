"""Regression coverage for corpus scope and mixed narrative judgments."""

import importlib.util
from pathlib import Path


def test_benchmark_summary_keeps_output_types_and_scopes_separate() -> None:
    """Count each exact target once and exclude prose mentions of unrelated GO claims."""
    path = Path("projects/PROTNLM_EVALUATION/build_benchmark_summary.py")
    spec = importlib.util.spec_from_file_location("benchmark_summary", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = module.collect(Path.cwd())
    assert data["distinct_records"] == 282
    assert data["prediction_targets"] == 242
    assert sum(data["go_counts"].values()) == 288
    assert data["go_counts"]["PLI"] == 0
    narratives = {r["gene"]: r["categories"] for r in data["narrative_reviews"]}
    assert narratives["human/NARF"] == ["PLI"]
    assert narratives["DANRE/dcxr"] == ["PLI"]
    assert "rat/Mtmr12" not in narratives
    assert narratives["DROME/dati"] == ["CNN"]
    assert narratives["NEUCR/NCU04637"] == ["NPI"]
    assert data["narrative_counts"]["PLI"] == 13
    assert len(narratives) == 57
    assert data["cohort_memberships"] > data["distinct_records"]
