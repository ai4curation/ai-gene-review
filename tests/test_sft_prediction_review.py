"""Regression tests for deterministic BioReason SFT review repair."""

import csv

import pytest

from pathlib import Path

import yaml

from scripts.auto_review_sft_predictions import (
    EXPECTED_CONFIDENCE,
    MANUAL_OVERRIDES,
    ManualOverride,
    ONTOLOGY_ADJUDICATION_MARKER,
    ONTOLOGY_PAIR_DECISIONS,
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
    load_aigr_review,
    load_goa_terms as load_hf_goa_terms,
    ontology_label_note,
)
from scripts.gogpt_predict import deterministic_assessment, load_review_decisions
from ai_gene_review.sft_prediction_evidence import (
    NEGATED_ACTION_PREFIX,
    PROVENANCE_LIMITED_NEGATIVE,
    split_action_evidence,
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


def test_load_aigr_actions_preserves_negated_annotations(tmp_path):
    review_file = tmp_path / "review.yaml"
    review_file.write_text(
        """
existing_annotations:
  - term: {id: "GO:0000001", label: absent activity}
    negated: true
    review: {action: ACCEPT}
"""
    )

    assert load_aigr_term_actions(review_file) == {
        "GO:0000001": {f"{NEGATED_ACTION_PREFIX}ACCEPT"}
    }


def test_negated_goa_and_aigr_do_not_count_as_positive_support(tmp_path):
    goa_file = tmp_path / "gene-goa.tsv"
    goa_file.write_text(
        "DB\tID\tSYMBOL\tNOT|enables\tGO:0000001\tPMID:1\tIDA\n"
    )
    actions = {"GO:0000001": {f"{NEGATED_ACTION_PREFIX}ACCEPT"}}

    assert load_goa_terms(goa_file) == set()
    assert auto_assess("GO:0000001", set(), actions, set())[:2] == ("NPI", 0)
    assert deterministic_reclassification(
        "GO:0000001", "NPI", set(), actions
    ) is None
    review = {"assessment": "NPI", "confidence_score": 0}
    assert list(remaining_conflicts("GO:0000001", review, set(), actions)) == []


def test_split_action_evidence_separates_accepted_negations():
    actions = {
        "REMOVE",
        "ACCEPT",
        f"{NEGATED_ACTION_PREFIX}ACCEPT",
        f"{NEGATED_ACTION_PREFIX}REMOVE",
        PROVENANCE_LIMITED_NEGATIVE,
    }

    assert split_action_evidence(actions) == (
        {"REMOVE", "ACCEPT"},
        {"ACCEPT"},
    )


def test_positive_and_negated_goa_rows_keep_positive_term(tmp_path):
    goa_file = tmp_path / "gene-goa.tsv"
    goa_file.write_text(
        "DB\tID\tSYMBOL\tenables\tGO:0000001\tPMID:1\tIDA\n"
        "DB\tID\tSYMBOL\tNOT|enables\tGO:0000001\tPMID:2\tIDA\n"
    )

    assert load_goa_terms(goa_file) == {"GO:0000001"}
    assert load_hf_goa_terms(goa_file) == {"GO:0000001"}


def test_negated_aigr_drives_all_sft_assessment_paths_to_npi():
    actions = {"GO:0000001": {f"{NEGATED_ACTION_PREFIX}ACCEPT"}}

    assert assess_prediction("GO:0000001", set(), actions, set())["assessment"] == "NPI"
    assert deterministic_reclassification(
        "GO:0000001", "CNN", set(), actions["GO:0000001"]
    )[0] == "NPI"
    review = {"assessment": "CNN", "confidence_score": 2}
    assert "nonnegative_assessment_vs_negated_AIGR" in list(
        remaining_conflicts(
            "GO:0000001", review, set(), actions["GO:0000001"]
        )
    )


def test_mixed_positive_and_negated_evidence_is_stably_uncertain():
    exact_actions = {"ACCEPT", f"{NEGATED_ACTION_PREFIX}ACCEPT"}
    actions = {"GO:0000001": exact_actions}

    assert auto_assess("GO:0000001", {"GO:0000001"}, actions, set())[:2] == (
        "UNC",
        1,
    )
    assert assess_prediction("GO:0000001", {"GO:0000001"}, actions, set())[
        "assessment"
    ] == "UNC"
    assert deterministic_assessment("GO:0000001", actions)[0] == "UNC"
    assert deterministic_reclassification(
        "GO:0000001", "UNC", {"GO:0000001"}, exact_actions
    ) is None
    review = {"assessment": "UNC", "confidence_score": 1}
    assert list(
        remaining_conflicts("GO:0000001", review, {"GO:0000001"}, exact_actions)
    ) == []


def test_load_aigr_actions_marks_only_negative_miscitation_decisions(tmp_path):
    review_file = tmp_path / "review.yaml"
    review_file.write_text(
        """
references:
  - id: PMID:1
    reference_review: {correctness: MISCITED}
  - id: PMID:2
    reference_review: {correctness: WRONG_IDENTIFIER}
  - id: PMID:3
    reference_review: {correctness: VERIFIED}
  - id: PMID:4
    reference_review:
  - reference_review: {correctness: MISCITED}
existing_annotations:
  - term: {id: "GO:0000001", label: miscited negative}
    original_reference_id: PMID:1
    review: {action: REMOVE}
  - term: {id: "GO:0000002", label: wrong-identifier negative}
    original_reference_id: PMID:2
    review: {action: MARK_AS_OVER_ANNOTATED}
  - term: {id: "GO:0000003", label: verified negative}
    original_reference_id: PMID:3
    review: {action: REMOVE}
  - term: {id: "GO:0000004", label: unreviewed negative}
    original_reference_id: PMID:4
    review: {action: REMOVE}
  - term: {id: "GO:0000005", label: positive despite miscitation}
    original_reference_id: PMID:1
    review: {action: ACCEPT}
"""
    )

    expected = {
        "GO:0000001": {PROVENANCE_LIMITED_NEGATIVE},
        "GO:0000002": {PROVENANCE_LIMITED_NEGATIVE},
        "GO:0000003": {"REMOVE"},
        "GO:0000004": {"REMOVE"},
        "GO:0000005": {"ACCEPT"},
    }
    assert load_aigr_term_actions(review_file) == expected
    assert load_aigr_review(review_file)[0] == expected
    assert load_review_decisions(review_file) == expected


def test_provenance_limited_negative_defaults_to_uncertain():
    actions = {"GO:0000001": {PROVENANCE_LIMITED_NEGATIVE}}
    assert auto_assess("GO:0000001", {"GO:0000001"}, actions, set())[:2] == (
        "UNC",
        1,
    )
    result = assess_prediction("GO:0000001", {"GO:0000001"}, actions, set())
    assert (result["assessment"], result["confidence_score"]) == ("UNC", 1)
    assert deterministic_assessment("GO:0000001", actions)[0] == "UNC"


def test_verified_negative_remains_decisive_alongside_provenance_limited_action():
    exact_actions = {"REMOVE", PROVENANCE_LIMITED_NEGATIVE}
    actions = {"GO:0000001": exact_actions}
    assert auto_assess("GO:0000001", {"GO:0000001"}, actions, set())[:2] == (
        "NPI",
        0,
    )
    result = assess_prediction("GO:0000001", {"GO:0000001"}, actions, set())
    assert (result["assessment"], result["confidence_score"]) == ("NPI", 0)
    assert deterministic_assessment("GO:0000001", actions)[0] == "NPI"


def test_modify_remains_less_precise_alongside_provenance_limited_action():
    actions = {"GO:0000001": {"MODIFY", PROVENANCE_LIMITED_NEGATIVE}}
    assert auto_assess("GO:0000001", {"GO:0000001"}, actions, set())[:2] == (
        "LSP",
        2,
    )
    result = assess_prediction("GO:0000001", {"GO:0000001"}, actions, set())
    assert (result["assessment"], result["confidence_score"]) == ("LSP", 2)


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


def test_drome_git_override_uses_canonical_symbol():
    assert ("DROME", "Git", "GO:0005515") in MANUAL_OVERRIDES
    assert ("DROME", "git", "GO:0005515") not in MANUAL_OVERRIDES


def test_skp_folding_uses_ontology_pair_decision_not_dead_manual_override():
    manual_key = ("ECOLI", "Skp", "GO:0061077")
    pair_key = (*manual_key, "chaperone-mediated protein folding")
    assert manual_key not in MANUAL_OVERRIDES
    expected_assessment = ONTOLOGY_PAIR_DECISIONS[pair_key].assessment

    doc = {
        "predictions": [
            {
                "source_version": "wanglab/protein_catalogue",
                "predicted_term": {
                    "id": "GO:0061077",
                    "label": "chaperone-mediated protein folding",
                },
                "review": {
                    "assessment": "UNC",
                    "confidence_score": 1,
                    "summary": "Historical rationale.",
                },
            }
        ]
    }

    changed = repair_document(
        doc,
        "ECOLI",
        "Skp",
        {"GO:0006457"},
        {"GO:0006457": {"ACCEPT"}},
        set(),
        "wanglab/protein_catalogue",
        None,
        RepairStats(),
    )

    review = doc["predictions"][0]["review"]
    assert changed is True
    assert review["assessment"] == expected_assessment
    assert review["confidence_score"] == EXPECTED_CONFIDENCE[expected_assessment]
    assert ONTOLOGY_ADJUDICATION_MARKER in review["summary"]


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
                    species=species,
                    gene=gene,
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


@pytest.mark.parametrize('gene,go_id,label,expected', [
    ('Uggt1', 'GO:0051082', 'unfolded protein binding', 'CNN'),
    ('Casp3', 'GO:0005123', 'death receptor binding', 'UNC'),
])
def test_explicit_biological_judgments_survive_annotation_suitability_rejections(
    gene, go_id, label, expected
):
    """An over-annotation call cannot erase a documented biological adjudication."""
    document = {'predictions': [{
        'source_version': 'wanglab/protein_catalogue',
        'predicted_term': {'id': go_id, 'label': label},
        'review': {'assessment': 'CNN', 'confidence_score': 2,
                   'summary': 'Term is in GOA — already a known curated annotation.'},
    }]}
    stats = RepairStats()
    assert repair_document(
        document, species='rat', gene=gene, goa_terms={go_id},
        aigr_actions={go_id: {'MARK_AS_OVER_ANNOTATED'}}, aigr_core=set(),
        source_version='wanglab/protein_catalogue', label_checker=None, stats=stats,
    )
    review = document['predictions'][0]['review']
    assert review['assessment'] == expected
    assert review['confidence_score'] == EXPECTED_CONFIDENCE[expected]
    assert not stats.remaining_conflicts
    assert not repair_document(
        document, species='rat', gene=gene, goa_terms={go_id},
        aigr_actions={go_id: {'MARK_AS_OVER_ANNOTATED'}}, aigr_core=set(),
        source_version='wanglab/protein_catalogue', label_checker=None, stats=RepairStats(),
    )


@pytest.mark.parametrize('gene,actions,change,expected_conflict', [
    ('Uggt1', {'MARK_AS_OVER_ANNOTATED'}, {'summary': 'Unreviewed text'}, 'manual_adjudication_rationale'),
    ('Uggt1', {'MARK_AS_OVER_ANNOTATED'}, {'assessment': 'NPI'}, 'manual_adjudication_category'),
    ('Uggt1', {'MARK_AS_OVER_ANNOTATED'}, {'confidence_score': 0}, 'assessment_confidence'),
    ('Uggt1', {'REMOVE'}, {}, 'nonnegative_assessment_vs_negative_AIGR'),
    ('Uggt1', {f'{NEGATED_ACTION_PREFIX}ACCEPT'}, {}, 'nonnegative_assessment_vs_negated_AIGR'),
    ('Casp3', {'MARK_AS_OVER_ANNOTATED'}, {}, 'nonnegative_assessment_vs_negative_AIGR'),
])
def test_scoped_adjudications_keep_conflict_checks(gene, actions, change, expected_conflict):
    """Registered rationale, identity, action scope, and confidence remain checked."""
    override = MANUAL_OVERRIDES[('rat', 'Uggt1', 'GO:0051082')]
    review = {'assessment': 'CNN', 'confidence_score': 2, 'summary': override.summary}
    review.update(change)
    assert expected_conflict in set(remaining_conflicts(
        'GO:0051082', review, {'GO:0051082'}, actions, species='rat', gene=gene,
    ))
    # Supplying the rationale alone cannot opt an unknown context out of checks.
    assert 'nonnegative_assessment_vs_negative_AIGR' in set(remaining_conflicts(
        'GO:0051082', {'assessment': 'CNN', 'confidence_score': 2, 'summary': override.summary},
        {'GO:0051082'}, {'MARK_AS_OVER_ANNOTATED'},
    ))


@pytest.mark.parametrize('actions', [
    {'REMOVE'},
    {'MARK_AS_OVER_ANNOTATED', 'REMOVE'},
    {f'{NEGATED_ACTION_PREFIX}ACCEPT'},
])
def test_repair_does_not_write_an_out_of_scope_manual_override(actions):
    """A stronger reference action must not be overwritten by a scoped CNN call."""
    go_id = 'GO:0051082'
    document = {'predictions': [{
        'source_version': 'wanglab/protein_catalogue',
        'predicted_term': {'id': go_id, 'label': 'unfolded protein binding'},
        'review': {'assessment': 'CNN', 'confidence_score': 2,
                   'summary': 'Original current review'},
    }]}
    stats = RepairStats()
    assert repair_document(
        document, species='rat', gene='Uggt1', goa_terms={go_id},
        aigr_actions={go_id: actions}, aigr_core=set(),
        source_version='wanglab/protein_catalogue', label_checker=None, stats=stats,
    )
    review = document['predictions'][0]['review']
    assert review['assessment'] == 'NPI'
    assert review['confidence_score'] == 0
    assert review['summary'] != MANUAL_OVERRIDES[('rat', 'Uggt1', go_id)].summary
    assert not stats.remaining_conflicts
    assert not repair_document(
        document, species='rat', gene='Uggt1', goa_terms={go_id},
        aigr_actions={go_id: actions}, aigr_core=set(),
        source_version='wanglab/protein_catalogue', label_checker=None, stats=RepairStats(),
    )


@pytest.mark.parametrize('fields', [
    {'assessment': 'CNN'},
    {'summary': 'A rationale without a category'},
])
def test_scoped_registry_entries_require_category_and_rationale(fields):
    with pytest.raises(ValueError, match='assessment and rationale'):
        ManualOverride(annotation_action_exceptions=frozenset({'MARK_AS_OVER_ANNOTATED'}), **fields)
