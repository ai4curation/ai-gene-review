"""Regression tests for deterministic BioReason SFT review repair."""

import csv

from pathlib import Path

import yaml

from scripts.auto_review_sft_predictions import (
    EXPECTED_CONFIDENCE,
    LabelCheck,
    RepairStats,
    apply_label_note,
    auto_assess,
    deterministic_reclassification,
    load_aigr_term_actions,
    load_cohort,
    load_goa_terms,
    load_ontology_pair_decisions,
    remaining_conflicts,
    rewrite_prediction_reviews,
    repair_document,
)
from scripts.hf_to_sft_predictions import (
    assess_prediction,
    ontology_label_note,
)


def test_load_aigr_actions_preserves_mixed_decisions(tmp_path):
    review_file = tmp_path / "review.yaml"
    review_file.write_text(
        """
existing_annotations:
  - term: {id: "GO:0000001", label: test}
    review: {action: ACCEPT}
  - term: {id: "GO:0000001", label: test}
    review: {action: REMOVE}
"""
    )

    assert load_aigr_term_actions(review_file) == {
        "GO:0000001": {"ACCEPT", "REMOVE"}
    }


def test_deterministic_reclassification_uses_only_exact_contradictions():
    assert deterministic_reclassification(
        "GO:0000001", "COR", {"GO:0000001"}, set()
    ) == ("CNN", "the exact GO ID is already present in current local GOA")

    negative = {"MARK_AS_OVER_ANNOTATED"}
    assert deterministic_reclassification(
        "GO:0000001", "CNN", {"GO:0000001"}, negative
    )[0] == "NPI"
    assert deterministic_reclassification(
        "GO:0005515", "CNN", {"GO:0005515"}, negative
    )[0] == "REP"

    positive = {"KEEP_AS_NON_CORE"}
    assert deterministic_reclassification(
        "GO:0000001", "NPI", {"GO:0000001"}, positive
    )[0] == "CNN"
    assert (
        deterministic_reclassification(
            "GO:0000001", "UNC", set(), {"UNDECIDED"}
        )
        is None
    )


def test_auto_assess_emits_only_schema_categories():
    negative = {"GO:0000001": {"REMOVE"}}
    assert auto_assess("GO:0000001", {"GO:0000001"}, negative, set())[:2] == (
        "NPI",
        0,
    )

    positive = {"GO:0000001": {"KEEP_AS_NON_CORE"}}
    assert auto_assess("GO:0000001", set(), positive, set())[:2] == ("CNN", 2)
    assert auto_assess("GO:0000001", set(), {}, {"GO:0000001"})[:2] == (
        "COR",
        2,
    )


def test_hf_converter_matches_repair_assessment_rules():
    negative = {"GO:0000001": {"REMOVE"}}
    result = assess_prediction("GO:0000001", {"GO:0000001"}, negative, set())
    assert (result["assessment"], result["confidence_score"]) == ("NPI", 0)

    positive = {"GO:0000001": {"KEEP_AS_NON_CORE"}}
    result = assess_prediction("GO:0000001", set(), positive, set())
    assert (result["assessment"], result["confidence_score"]) == ("CNN", 2)


def test_repair_keeps_raw_term_and_applies_cts2_override():
    raw_term = {
        "id": "GO:0004568",
        "label": "chitinase activity",
    }
    doc = {
        "predictions": [
            {
                "source_version": "wanglab/protein_catalogue",
                "predicted_term": raw_term.copy(),
                "review": {
                    "assessment": "CNN",
                    "confidence_score": 1,
                    "summary": "In GOA, but AIGR recommends REMOVE.",
                },
            }
        ]
    }
    stats = RepairStats()

    changed = repair_document(
        doc,
        "SCHPO",
        "cts2",
        {"GO:0004568"},
        {"GO:0004568": {"REMOVE"}},
        set(),
        "wanglab/protein_catalogue",
        None,
        stats,
    )

    prediction = doc["predictions"][0]
    assert changed is True
    assert prediction["predicted_term"] == raw_term
    assert prediction["review"]["assessment"] == "NPI"
    assert prediction["review"]["confidence_score"] == EXPECTED_CONFIDENCE["NPI"]
    assert prediction["review"]["error_type"] == "PSEUDOENZYME_OVERANNOTATION"


def test_summary_only_manual_override_is_persisted_and_idempotent():
    doc = {
        "predictions": [
            {
                "source_version": "wanglab/protein_catalogue",
                "predicted_term": {
                    "id": "GO:0044183",
                    "label": "protein folding chaperone",
                },
                "review": {
                    "assessment": "UNC",
                    "confidence_score": 1,
                    "summary": "Stale rationale.",
                },
            }
        ]
    }
    stats = RepairStats()

    assert repair_document(
        doc,
        "ECOLI",
        "CpxP",
        set(),
        {},
        set(),
        "wanglab/protein_catalogue",
        None,
        stats,
    )
    assert (
        "Uncertain rather than refuted"
        in doc["predictions"][0]["review"]["summary"]
    )

    assert not repair_document(
        doc,
        "ECOLI",
        "CpxP",
        set(),
        {},
        set(),
        "wanglab/protein_catalogue",
        None,
        RepairStats(),
    )


def test_label_note_is_explicit_idempotent_and_source_preserving():
    review = {"summary": "Correct relative to the authoritative GO ID."}
    check = LabelCheck(
        "MISMATCH",
        "positive regulation of blood vessel endothelial cell proliferation involved "
        "in sprouting angiogenesis",
    )

    assert apply_label_note(
        review,
        "GO:1903589",
        "positive regulation of vascular permeability",
        check,
    )
    first = review["summary"]
    assert "Raw model pair mismatch" in first
    assert "positive regulation of vascular permeability" in first
    assert not apply_label_note(
        review,
        "GO:1903589",
        "positive regulation of vascular permeability",
        check,
    )
    assert review["summary"] == first


class _FakeOntologyAdapter:
    def label(self, go_id):
        return "canonical label"

    def entity_aliases(self, go_id):
        return ["canonical label", "accepted synonym"]


def test_converter_flags_mismatch_but_accepts_synonym():
    adapter = _FakeOntologyAdapter()
    assert ontology_label_note("GO:0000001", "accepted synonym", adapter) is None
    note = ontology_label_note("GO:0000001", "wrong label", adapter)
    assert "Raw model pair mismatch" in note
    assert "wrong label" in note


def test_focused_writer_leaves_unchanged_prediction_text_intact():
    original = """predictions:
- source_method: BioReason-Pro-SFT
  predicted_term:
    id: GO:0000001
    label: first raw label
  review:
    assessment: UNC
    confidence_score: 1
    summary: First hand-written rationale stays exactly as formatted.
- source_method: BioReason-Pro-SFT
  predicted_term:
    id: GO:0000002
    label: second raw label
  review:
    assessment: UNC
    confidence_score: 2
    summary: Second rationale.
"""
    from ruamel.yaml import YAML

    doc = YAML().load(original)
    doc["predictions"][1]["review"]["confidence_score"] = 1
    updated = rewrite_prediction_reviews(original, doc, {1})

    first_block = original.split("- source_method: BioReason-Pro-SFT", 2)[1]
    assert first_block in updated
    assert "id: GO:0000002\n    label: second raw label" in updated
    assert "confidence_score: 1" in updated


def test_committed_argo95_has_no_deterministic_category_conflicts():
    root = Path(__file__).resolve().parents[1]
    cohort = load_cohort(root / "projects/BIOREASON_COMPARISON/genes.csv")
    conflicts = []

    for species, gene in sorted(cohort):
        gene_dir = root / "genes" / species / gene
        path = gene_dir / f"{gene}-sft-predictions.yaml"
        if not path.exists():
            continue
        document = yaml.safe_load(path.read_text())
        goa_terms = load_goa_terms(gene_dir / f"{gene}-goa.tsv")
        actions = load_aigr_term_actions(gene_dir / f"{gene}-ai-review.yaml")
        for prediction in document.get("predictions", []):
            if prediction.get("source_version") != "wanglab/protein_catalogue":
                continue
            go_id = prediction["predicted_term"]["id"]
            found = list(
                remaining_conflicts(
                    go_id,
                    prediction["review"],
                    goa_terms,
                    actions.get(go_id, set()),
                )
            )
            conflicts.extend((species, gene, go_id, conflict) for conflict in found)

    assert conflicts == []


def test_ontology_pair_adjudications_are_applied_to_committed_reviews():
    root = Path(__file__).resolve().parents[1]
    audit_path = (
        root
        / "projects"
        / "BIOREASON_COMPARISON"
        / "argo95-ontology-pair-adjudication.tsv"
    )
    decisions = load_ontology_pair_decisions(audit_path)
    assert len(decisions) == 65

    for (species, gene, go_id, raw_label), decision in decisions.items():
        path = root / "genes" / species / gene / f"{gene}-sft-predictions.yaml"
        document = yaml.safe_load(path.read_text())
        matches = [
            prediction["review"]
            for prediction in document["predictions"]
            if prediction.get("source_version") == "wanglab/protein_catalogue"
            and prediction["predicted_term"]["id"] == go_id
            and prediction["predicted_term"]["label"] == raw_label
        ]
        assert len(matches) == 1, (species, gene, go_id, raw_label)
        assert matches[0]["assessment"] == decision.assessment
        assert matches[0].get("error_type") == decision.error_type
        assert f"classified {decision.assessment}" in matches[0]["summary"]


def test_ontology_pair_audit_covers_every_current_nonnegative_mismatch():
    root = Path(__file__).resolve().parents[1]
    audit_path = (
        root
        / "projects"
        / "BIOREASON_COMPARISON"
        / "argo95-ontology-pair-adjudication.tsv"
    )
    with audit_path.open() as handle:
        audited = {
            (row["species"], row["gene"], row["go_id"], row["raw_label"])
            for row in csv.DictReader(handle, delimiter="\t")
        }

    cohort = load_cohort(root / "projects/BIOREASON_COMPARISON/genes.csv")
    uncovered = []
    for species, gene in sorted(cohort):
        path = root / "genes" / species / gene / f"{gene}-sft-predictions.yaml"
        if not path.exists():
            continue
        document = yaml.safe_load(path.read_text())
        for prediction in document.get("predictions", []):
            if prediction.get("source_version") != "wanglab/protein_catalogue":
                continue
            review = prediction["review"]
            if review["assessment"] in {"NPI", "PLI", "REP"}:
                continue
            if "[ONTOLOGY_LABEL_AUDIT]" not in str(review.get("summary", "")):
                continue
            term = prediction["predicted_term"]
            key = (species, gene, term["id"], term["label"])
            if key not in audited:
                uncovered.append(key)

    assert uncovered == []


def test_frequency_bias_is_reserved_for_repetition_in_argo95():
    root = Path(__file__).resolve().parents[1]
    cohort = load_cohort(root / "projects/BIOREASON_COMPARISON/genes.csv")

    for species, gene in sorted(cohort):
        path = root / "genes" / species / gene / f"{gene}-sft-predictions.yaml"
        if not path.exists():
            continue
        document = yaml.safe_load(path.read_text())
        for prediction in document.get("predictions", []):
            if prediction.get("source_version") != "wanglab/protein_catalogue":
                continue
            review = prediction["review"]
            if review.get("error_type") == "FREQUENCY_BIAS":
                assert review["assessment"] == "REP", (species, gene, prediction)
