"""Canonical prediction exports preserve coverage, provenance and review state."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.export.prediction_export import collect_prediction_data


def write_review(
    root: Path, filename: str, predictions: object = (), **fields: object
) -> Path:
    """Write an actual prediction document beneath the canonical gene tree."""
    path = root / "genes/TEST/gene" / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "id": "P12345",
        "gene_symbol": "gene",
        "taxon": {"id": "NCBITaxon:1", "label": "Test species"},
        **fields,
    }
    if predictions != ():
        data["predictions"] = predictions
    path.write_text(yaml.safe_dump(data))
    return path


def prediction(
    method: str = "ProtNLM2",
    version: str = "snapshot",
    assessment: str = "CNN",
    summary: str = "An enzyme assay establishes this activity.",
    **review_fields: object,
) -> dict:
    """Provide a small independently reviewable term prediction."""
    return {
        "source_method": method,
        "source_version": version,
        "predicted_term": {"id": "GO:0000001", "label": "test term"},
        "predicted_term_type": "GO_BP",
        "review": {
            "assessment": assessment,
            "confidence_score": 2,
            "summary": summary,
            **review_fields,
        },
    }


def test_empty_output_is_preserved_without_fabricated_claims_or_version(
    tmp_path: Path,
) -> None:
    """An explicit empty list is an assessed absence, not a missing document."""
    write_review(
        tmp_path,
        "gene-protnlm-predictions-review.yaml",
        [],
        status="COMPLETE",
        description="ProtNLM2 snapshot 2026-09-08 emitted no GO predictions; binding is a supported omission.",
    )
    data = collect_prediction_data(tmp_path, tmp_path / "app/predictions")
    assert data["claims"] == []
    (row,) = data["sets"]
    assert row["source_method"] == "ProtNLM2"
    assert row["source_version"] == ""
    assert row["output_state"] == "No GO/EC predictions"
    assert row["review_state"] == "Reviewed"
    assert row["claim_count"] == 0
    assert row["assessment_categories"] == []
    assert (
        row["source_link"]
        == "../../genes/TEST/gene/gene-protnlm-predictions-review.yaml"
    )
    assert "2026-09-08" in row["summary"]


@pytest.mark.parametrize("predictions", [(), None])
def test_missing_list_and_complete_without_rationale_are_not_completed_reviews(
    tmp_path: Path,
    predictions: object,
) -> None:
    """Status alone establishes neither no output nor a completed assessment."""
    write_review(
        tmp_path, "gene-protnlm-predictions-review.yaml", predictions, status="COMPLETE"
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app/predictions")["sets"]
    assert row["output_state"] == "Not recorded"
    assert row["review_state"] == "Unreviewed"
    assert row["claim_count"] is None


def test_mixed_methods_and_versions_form_distinct_stable_sets(tmp_path: Path) -> None:
    """A file can contain several methods; filtering must not erase their identity."""
    rows = [prediction(), prediction("DeepECTF", "v1"), prediction("ProtNLM2", "later")]
    path = write_review(tmp_path, "gene-combined-predictions-review.yaml", rows)
    first = collect_prediction_data(tmp_path, tmp_path / "app")
    assert len(first["sets"]) == len(first["claims"]) == 3
    assert {(r["source_method"], r["source_version"]) for r in first["sets"]} == {
        ("ProtNLM2", "snapshot"),
        ("DeepECTF", "v1"),
        ("ProtNLM2", "later"),
    }
    ids = {
        (r["source_method"], r["source_version"]): r["set_id"] for r in first["sets"]
    }
    doc = yaml.safe_load(path.read_text())
    doc["predictions"].reverse()
    path.write_text(yaml.safe_dump(doc))
    second = collect_prediction_data(tmp_path, tmp_path / "app")
    assert ids == {
        (r["source_method"], r["source_version"]): r["set_id"] for r in second["sets"]
    }
    assert all(r["set_link"].endswith(r["set_id"]) for r in first["claims"])


@pytest.mark.parametrize(
    ("assessment", "summary", "status", "expected"),
    [
        ("UNC", "Requires manual assessment.", "COMPLETE", "Awaiting review"),
        (
            "CNN",
            "Deterministic exact-match comparison: current AIGR retains this GO term.",
            "COMPLETE",
            "Automatic comparison",
        ),
        (
            "UNC",
            "Available biochemistry does not distinguish the competing substrates.",
            "DRAFT",
            "Reviewed",
        ),
        ("UNC", "", "COMPLETE", "Unreviewed"),
        (
            "CNN",
            "The automatic comparator was not used; the purified enzyme assay supports the term.",
            "COMPLETE",
            "Reviewed",
        ),
    ],
)
def test_review_state_preserves_curated_unc_and_identifies_pending_templates(
    tmp_path: Path, assessment: str, summary: str, status: str, expected: str
) -> None:
    """Biological uncertainty and unperformed review remain separate dimensions."""
    write_review(
        tmp_path,
        "gene-sft-predictions.yaml",
        [prediction(assessment=assessment, summary=summary)],
        status=status,
    )
    data = collect_prediction_data(tmp_path, tmp_path / "app")
    (row,) = data["claims"]
    assert row["assessment"] == assessment
    assert row["review_state"] == expected
    assert data["sets"][0]["review_state"] == expected


def test_score_mismatch_is_reported_without_rewriting_score_or_category(
    tmp_path: Path,
) -> None:
    """The export exposes source quality problems without modifying curation."""
    write_review(
        tmp_path,
        "gene-det-predictions-review.yaml",
        [
            prediction(
                assessment="UNC",
                confidence_score=0,
                supported_by=[
                    {"reference_id": "PMID:1", "supporting_text": "Measured activity."}
                ],
            )
        ],
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["claims"]
    assert row["review_score"] == 0
    assert row["assessment"] == "UNC"
    assert any("score" in note.lower() for note in row["quality_notes"])
    assert "PMID:1" in row["evidence"] and "Measured activity." in row["evidence"]
    assert "model_score" not in row


def test_leaf_preference_only_supersedes_same_method_version(tmp_path: Path) -> None:
    """Full and leaf variants of the same run are retained with one default view."""
    write_review(
        tmp_path, "gene-gogpt-predictions.yaml", [prediction("GO-GPT", "run1")]
    )
    write_review(
        tmp_path, "gene-gogpt-leaf-predictions.yaml", [prediction("GO-GPT", "run1")]
    )
    write_review(
        tmp_path, "gene-other-gogpt-predictions.yaml", [prediction("GO-GPT", "run2")]
    )
    data = collect_prediction_data(tmp_path, tmp_path / "app")
    full = next(
        r
        for r in data["sets"]
        if r["representation"] == "full" and r["source_version"] == "run1"
    )
    leaf = next(r for r in data["sets"] if r["representation"] == "leaf")
    other = next(r for r in data["sets"] if r["source_version"] == "run2")
    assert full["default_visible"] is False and full["superseded_by"] == leaf["set_id"]
    assert leaf["default_visible"] is True and other["default_visible"] is True
    assert len(data["claims"]) == 3
    assert (
        next(r for r in data["claims"] if r["set_id"] == full["set_id"])[
            "default_visible"
        ]
        is False
    )


def test_canonical_discovery_excludes_project_copies_and_nonprediction_documents(
    tmp_path: Path,
) -> None:
    """Discover new schema-shaped prediction filenames without scanning experiment copies."""
    write_review(
        tmp_path,
        "gene-newmethod-predictions-review.yaml",
        [prediction("New method", "v1")],
    )
    write_review(tmp_path, "gene-ai-review.yaml", [prediction()])
    copy = tmp_path / "projects/EXPERIMENT/genes/TEST/gene/gene-sft-predictions.yaml"
    copy.parent.mkdir(parents=True)
    copy.write_text(
        (
            tmp_path / "genes/TEST/gene/gene-newmethod-predictions-review.yaml"
        ).read_text()
    )
    unrelated = tmp_path / "genes/TEST/gene/gene-predictions-statistics.yaml"
    unrelated.write_text("counts: 3\n")
    data = collect_prediction_data(tmp_path, tmp_path / "app")
    assert len(data["sets"]) == 1
    assert data["sets"][0]["source_method"] == "New method"


def test_links_memberships_and_local_raw_sources_are_resolved(tmp_path: Path) -> None:
    """Relative sources and the ProtNLM cohort registry produce usable local links."""
    path = write_review(
        tmp_path,
        "gene-protnlm-predictions-review.yaml",
        [prediction()],
        source_documents=[
            "gene-protnlm-source.json",
            "projects/PROTNLM_EVALUATION/fly-benchmark/manifest.json",
        ],
    )
    (path.parent / "gene-protnlm-source.json").write_text("{}")
    (path.parent / "gene-ai-review.html").write_text("<p>Review</p>")
    scope = tmp_path / "projects/PROTNLM_EVALUATION/family-curation/scope.csv"
    scope.parent.mkdir(parents=True)
    scope.write_text(
        "cohort,role,accession,species,gene_symbol\nFLY,prediction_target,P12345,TEST,gene\nREF,reference,P12345,TEST,gene\n"
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app/predictions")["sets"]
    assert row["projects"] == ["PROTNLM_EVALUATION"]
    assert row["cohorts"] == ["FLY"]
    assert row["raw_link"] == "../../genes/TEST/gene/gene-protnlm-source.json"
    assert row["review_link"] == "../../genes/TEST/gene/gene-ai-review.html"
    assert row["taxon_label"] == "Test species" and row["species"] == "TEST"


def test_missing_review_is_exported_without_inventing_an_assessment(
    tmp_path: Path,
) -> None:
    """Unassessed predictions remain visible without a manufactured UNC verdict."""
    row = prediction()
    row.pop("review")
    write_review(tmp_path, "gene-new-predictions.yaml", [row], status="COMPLETE")
    (claim,) = collect_prediction_data(tmp_path, tmp_path / "app")["claims"]
    assert claim["assessment"] == "" and claim["review_score"] is None
    assert claim["review_state"] == "Unreviewed"


def test_bioreason_membership_uses_exact_registry_sources_without_cross_run_cohorts(
    tmp_path: Path,
) -> None:
    """Shared project membership does not make SFT terms part of an RL narrative cohort."""
    write_review(
        tmp_path,
        "gene-sft-predictions.yaml",
        [prediction("BioReason-Pro-SFT", "catalogue")],
    )
    registry = tmp_path / "projects/BIOREASON_COMPARISON/benchmark-genes.csv"
    registry.parent.mkdir(parents=True)
    registry.write_text(
        "benchmark,organism,gene,uniprot_id,source_file,source_version\nSFT95,TEST,gene,P12345,genes/TEST/gene/gene-sft-predictions.yaml,catalogue\nRL139,TEST,gene,P12345,genes/TEST/gene/gene-rl-review.md,rl\nWRONG,TEST,gene,P99999,genes/TEST/gene/gene-sft-predictions.yaml,catalogue\n"
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["sets"]
    assert row["projects"] == ["BIOREASON_COMPARISON"]
    assert row["cohorts"] == ["SFT95"]


def test_unavailable_raw_and_gene_links_are_blank_with_quality_notes(
    tmp_path: Path,
) -> None:
    """A deployment must not present guessed raw-output and gene-page links."""
    write_review(
        tmp_path,
        "gene-sft-predictions.yaml",
        [prediction()],
        source_documents=["gene-raw-predictions.md"],
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["sets"]
    assert row["raw_link"] == "" and row["review_link"] == ""
    assert any("raw" in note.lower() for note in row["quality_notes"])
    assert any("gene review" in note.lower() for note in row["quality_notes"])


def test_narrative_sets_join_browser_without_manufactured_term_claims(
    tmp_path: Path,
) -> None:
    """A functional-summary review is a set, never an invented GO prediction."""
    path = write_review(tmp_path, "gene-ai-review.yaml", status="COMPLETE")
    (path.parent / "gene-bioreason-rl-predictions.md").write_text(
        "# BioReason Chat Export\n### Functional Summary\nA conserved enzyme.\n"
    )
    (path.parent / "gene-bioreason-rl-review.md").write_text(
        "# BioReason-Pro RL Review\n- **Correctness**: 4/5\n- **Completeness**: 3/5\n"
    )
    data = collect_prediction_data(tmp_path, tmp_path / "app/predictions")
    (row,) = data["sets"]
    assert row["output_type"] == "Functional summary"
    assert row["claim_count"] is None
    assert row["correctness"] == 4
    assert row["completeness"] == 3
    assert data["claims"] == []
    assert data["metadata"]["set_count"] == 1
    assert data["metadata"]["claim_count"] == 0


def test_deepectf_project_association_requires_existing_explicit_project_pages(
    tmp_path: Path,
) -> None:
    """Known method associations are disclosed and do not invent cohort membership."""
    write_review(
        tmp_path, "gene-det-predictions-review.yaml", [prediction("DeepECTF", "2023")]
    )
    projects = tmp_path / "projects"
    projects.mkdir()
    (projects / "BIOREASON_COMPARISON.md").write_text(
        "DeepECTF evaluation of selected E. coli proteins."
    )
    (projects / "VALIDATING_ECOLI_PREDICTIONS.md").write_text(
        "DeepECTransformer predictions."
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["sets"]
    assert row["projects"] == ["BIOREASON_COMPARISON", "VALIDATING_ECOLI_PREDICTIONS"]
    assert row["cohorts"] == []
    assert any(
        "project" in note.lower() and "method" in note.lower()
        for note in row["quality_notes"]
    )


def test_protnlm_project_fallback_does_not_invent_cohort_membership(
    tmp_path: Path,
) -> None:
    """Canonical ProtNLM reviews remain discoverable outside the frozen cohort scope."""
    write_review(tmp_path, "gene-protnlm-predictions-review.yaml", [prediction()])
    projects = tmp_path / "projects"
    projects.mkdir()
    (projects / "PROTNLM_EVALUATION.md").write_text("ProtNLM prediction evaluation.")
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["sets"]
    assert row["projects"] == ["PROTNLM_EVALUATION"]
    assert row["cohorts"] == []
    assert any("method" in note.lower() for note in row["quality_notes"])


def test_scope_join_preserves_accession_named_folders_with_biological_gene_symbols(
    tmp_path: Path,
) -> None:
    """Canonical directory identity can differ from the curated biological symbol."""
    write_review(
        tmp_path,
        "gene-protnlm-predictions-review.yaml",
        [prediction()],
        gene_symbol="BIOLOGICAL_SYMBOL",
    )
    scope = tmp_path / "projects/PROTNLM_EVALUATION/family-curation/scope.csv"
    scope.parent.mkdir(parents=True)
    scope.write_text(
        "cohort,role,accession,species,gene_symbol\nARGO50,prediction_target,P12345,TEST,gene\n"
    )
    (row,) = collect_prediction_data(tmp_path, tmp_path / "app")["sets"]
    assert row["gene_symbol"] == "BIOLOGICAL_SYMBOL"
    assert row["cohorts"] == ["ARGO50"]
