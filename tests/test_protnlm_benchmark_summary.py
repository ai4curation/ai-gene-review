"""Regression coverage for corpus scope and mixed narrative judgments."""

import importlib.util
import shutil
from pathlib import Path
from types import ModuleType

import pytest
import yaml

from ai_gene_review.source_tree import ReviewSnapshot, WorkingTree, review_snapshot_tree

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_summary_module() -> ModuleType:
    """Load the project summary generator without writing repository artifacts."""
    path = REPO_ROOT / "projects/PROTNLM_EVALUATION/build_benchmark_summary.py"
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


def test_benchmark_summary_keeps_output_types_and_scopes_separate(
    forbid_working_tree_genes: None,
) -> None:
    """Count each exact target once and exclude prose mentions of unrelated GO claims."""
    module = load_summary_module()
    # Pinned at review_snapshot_commit in benchmark-policy.yaml.
    data = module.collect(review_snapshot_tree(REPO_ROOT), WorkingTree(REPO_ROOT))
    assert data["distinct_records"] == 282
    assert data["prediction_targets"] == 242
    assert sum(data["go_counts"].values()) == 288
    assert data["go_counts"] == {
        "COR": 52, "CNN": 32, "LSP": 84, "UNC": 98, "NPI": 20, "PLI": 2, "REP": 0
    }
    narratives = {r["gene"]: r["categories"] for r in data["narrative_reviews"]}
    assert narratives["human/NARF"] == ["PLI"]
    assert narratives["DANRE/dcxr"] == ["PLI"]
    assert "rat/Mtmr12" not in narratives
    assert narratives["DROME/dati"] == ["CNN"]
    assert narratives["NEUCR/NCU04637"] == ["NPI"]
    assert data["narrative_counts"]["PLI"] == 13
    assert len(narratives) == 57
    assert data["cohort_memberships"] > data["distinct_records"]


CONFIG_FILES = (
    "projects/PROTNLM_EVALUATION/family-curation/scope.csv",
    "projects/PROTNLM_EVALUATION/narrative-review-index.yaml",
)


@pytest.fixture
def config_copy(tmp_path: Path) -> Path:
    """A copy of the working-tree benchmark config, safe to edit."""
    for name in CONFIG_FILES:
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / name, tmp_path / name)
    return tmp_path


def test_scope_edits_take_effect_without_touching_working_tree_genes(
    config_copy: Path, forbid_working_tree_genes: None
) -> None:
    """Scope is curator config: a new row changes the report even though genes are pinned.

    ``forbid_working_tree_genes`` proves a plain gene-review edit still cannot matter.
    """
    scope = config_copy / CONFIG_FILES[0]
    with scope.open("a", encoding="utf-8") as handle:
        handle.write("extra,prediction_target,PNEW,DROME,new,,\n")
    data = load_summary_module().collect(
        review_snapshot_tree(REPO_ROOT), WorkingTree(config_copy)
    )
    assert data["prediction_targets"] == 243
    assert data["distinct_records"] == 283


def test_narrative_index_edit_without_snapshot_refresh_fails_loudly(
    config_copy: Path, forbid_working_tree_genes: None
) -> None:
    """An index hash that no longer matches the snapshot review bytes must fail."""
    index = config_copy / CONFIG_FILES[1]
    registry = yaml.safe_load(index.read_text(encoding="utf-8"))
    registry["reviews"][0]["review_sha256"] = "0" * 64
    index.write_text(yaml.safe_dump(registry), encoding="utf-8")
    with pytest.raises(AssertionError, match="Narrative index needs review"):
        load_summary_module().collect(
            review_snapshot_tree(REPO_ROOT), WorkingTree(config_copy)
        )


def test_empty_reviews_are_counted_separately_from_emitted_go_claims(
    tmp_path: Path,
) -> None:
    """Reviewed zero output is retained without becoming a claim or a missing review."""
    base = write_summary_fixture(tmp_path)
    module = load_summary_module()
    data = module.collect(WorkingTree(tmp_path), WorkingTree(tmp_path))

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

    module.write_report(tmp_path, data, ReviewSnapshot("0" * 40, "2026-01-01"))
    report = (base / "benchmark-results.md").read_text()
    assert "as of 2026-01-01 (commit `0000000000`)" in report
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
        load_summary_module().collect(WorkingTree(tmp_path), WorkingTree(tmp_path))


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
        load_summary_module().collect(WorkingTree(tmp_path), WorkingTree(tmp_path))
