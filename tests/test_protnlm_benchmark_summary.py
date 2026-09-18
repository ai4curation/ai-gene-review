"""Regression coverage for corpus scope and mixed narrative judgments."""

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest
import yaml


def load_summary_module() -> ModuleType:
    """Load the project summary generator without writing repository artifacts."""
    path = Path("projects/PROTNLM_EVALUATION/build_benchmark_summary.py")
    spec = importlib.util.spec_from_file_location("benchmark_summary", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_summary_fixture(root: Path) -> Path:
    """Create overlapping cohorts containing an assessment, an omission, and no review."""
    base = root / "projects/PROTNLM_EVALUATION"
    (base / "family-curation").mkdir(parents=True)
    (base / "family-curation/scope.csv").write_text(
        "cohort,accession,role,species,gene_symbol\n"
        "first,P1,prediction_target,DROME,assessed\n"
        "first,P2,prediction_target,DROME,empty\n"
        "first,P3,prediction_target,DROME,unreviewed\n"
        "overlap,P2,prediction_target,DROME,empty\n"
    )
    (base / "narrative-review-index.yaml").write_text("reviews: []\n")
    for accession, gene, predictions in (
        (
            "P1",
            "assessed",
            [
                {"predicted_term_type": "GO_MF", "review": {"assessment": "CNN"}},
                {"predicted_term_type": "GO_BP", "review": {"assessment": "UNC"}},
            ],
        ),
        ("P2", "empty", []),
    ):
        directory = root / "genes/DROME" / gene
        directory.mkdir(parents=True)
        (directory / f"{gene}-protnlm-predictions-review.yaml").write_text(
            yaml.safe_dump(
                {
                    "id": accession,
                    "gene_symbol": gene,
                    "status": "COMPLETE",
                    "description": "Review of frozen ProtNLM output.",
                    "predictions": predictions,
                }
            )
        )
    return base


def test_benchmark_summary_keeps_output_types_and_scopes_separate() -> None:
    """Count each exact target once and exclude prose mentions of unrelated GO claims."""
    module = load_summary_module()
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


def test_empty_reviews_are_counted_separately_from_emitted_go_claims(
    tmp_path: Path,
) -> None:
    """Reviewed zero output is retained without becoming a claim or a missing review."""
    base = write_summary_fixture(tmp_path)
    module = load_summary_module()
    data = module.collect(tmp_path)

    assert data["prediction_targets"] == 3
    assert data["prediction_review_files"] == data["go_review_files"] == 2
    assert data["records_with_go_assessments"] == 1
    assert data["records_with_zero_go_predictions"] == 1
    assert data["zero_go_prediction_reviews"] == [
        {
            "gene": "DROME/empty",
            "accession": "P2",
            "review_file": "genes/DROME/empty/empty-protnlm-predictions-review.yaml",
        }
    ]
    assert sum(data["go_counts"].values()) == 2
    assert data["go_counts"]["CNN"] == data["go_counts"]["UNC"] == 1
    assert sum(data["narrative_counts"].values()) == 0
    cohorts = {row["cohort"]: row for row in data["cohorts"]}
    assert cohorts["first"]["records_with_go_assessments"] == 1
    assert cohorts["first"]["records_with_zero_go_predictions"] == 1
    assert cohorts["overlap"]["records_with_go_assessments"] == 0
    assert cohorts["overlap"]["records_with_zero_go_predictions"] == 1
    assert sum(cohorts["overlap"]["go_counts"].values()) == 0

    module.write_report(tmp_path, data)
    report = (base / "benchmark-results.md").read_text()
    assert "1 record with zero emitted GO predictions" in report
    assert "| DROME/empty | P2 |" in report
    assert "| **Total** | **2** |" in report


@pytest.mark.parametrize("predictions", [None, "missing"])
def test_absent_prediction_list_is_not_a_reviewed_omission(
    tmp_path: Path, predictions: None | str
) -> None:
    """Require an explicit list to distinguish reviewed empty output from absent data."""
    write_summary_fixture(tmp_path)
    path = tmp_path / "genes/DROME/empty/empty-protnlm-predictions-review.yaml"
    doc = yaml.safe_load(path.read_text())
    if predictions is None:
        doc["predictions"] = None
    else:
        del doc["predictions"]
    path.write_text(yaml.safe_dump(doc))

    with pytest.raises(AssertionError, match="Explicit predictions list required"):
        load_summary_module().collect(tmp_path)


@pytest.mark.parametrize(
    "changes",
    [
        {"status": "IN_PROGRESS"},
        {"status": None},
        {"description": ""},
        {"description": "   "},
        {"description": None},
    ],
)
def test_empty_reviews_require_completed_summary(
    tmp_path: Path, changes: dict[str, str | None]
) -> None:
    """An unfinished or unexplained empty record is not a reviewed omission."""
    write_summary_fixture(tmp_path)
    path = tmp_path / "genes/DROME/empty/empty-protnlm-predictions-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc.update(changes)
    path.write_text(yaml.safe_dump(doc))

    with pytest.raises(
        AssertionError, match="Completed zero-output review with description required"
    ):
        load_summary_module().collect(tmp_path)
