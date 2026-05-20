"""Test the BestPractices ``inconsistent_review_actions`` validator check.

The check fires when a single GO term carries divergent ``review.action`` values
across multiple rows in ``existing_annotations``. That's a useful signal for
catching curator inconsistency, but it has a well-documented false positive
class: when each row is anchored to a distinct primary reference (different
``original_reference_id``) and the evidence is IPI ("Inferred from Physical
Interaction"), the divergent actions reflect *per-reference* evidence
assessment, not a curation error.

The canonical example is GO:0042802 (identical protein binding): each IPI
row in GOA comes from a distinct IntAct interaction paper, and reviewers
correctly diverge — ACCEPT on rows where the cited paper genuinely
demonstrates self-association, MARK_AS_OVER_ANNOTATED on rows where the
cited paper supports a different (e.g. heterotypic) interaction. Both
RB1 and BRAF reviews carry this pattern intentionally. Silencing the
divergence at the YAML level would degrade curation quality.

This module locks in the targeted exemption: IPI evidence + all distinct
PMIDs → no warning. Every other configuration still warns.
"""

from pathlib import Path
import tempfile

import yaml

from ai_gene_review.validation import validate_gene_review


def _build_yaml(term_id: str, rows: list[dict]) -> dict:
    """Construct a minimal review YAML covering the inconsistent-action case."""

    annotations = []
    for row in rows:
        annotations.append(
            {
                "term": {"id": term_id, "label": "identical protein binding"},
                "evidence_type": row["evidence_type"],
                "original_reference_id": row["pmid"],
                "review": {
                    "action": row["action"],
                    "reason": row.get("reason", "test"),
                },
            }
        )

    return {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene",
        "references": [{"id": row["pmid"], "title": "Paper"} for row in rows],
        "existing_annotations": annotations,
    }


def _has_inconsistent_action_warning(report) -> bool:
    return any(
        issue.check_type == "inconsistent_review_actions" for issue in report.issues
    )


def _validate(yaml_data: dict) -> object:
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "TEST-ai-review.yaml"
        path.write_text(yaml.dump(yaml_data))
        return validate_gene_review(path, check_best_practices=True)


def test_ipi_distinct_pmid_divergence_suppressed():
    """The RB1/BRAF GO:0042802 pattern: IPI rows, distinct PMIDs, divergent actions.

    Each row is independently evaluated against a distinct primary reference,
    so the divergence is a valid curation outcome rather than a defect. The
    validator must not raise an ``inconsistent_review_actions`` warning here.
    """
    yaml_data = _build_yaml(
        "GO:0042802",
        [
            {"evidence_type": "IPI", "pmid": "PMID:19727074", "action": "ACCEPT"},
            {
                "evidence_type": "IPI",
                "pmid": "PMID:35512704",
                "action": "MARK_AS_OVER_ANNOTATED",
            },
        ],
    )
    report = _validate(yaml_data)
    assert not _has_inconsistent_action_warning(report), (
        "IPI rows with distinct PMIDs should not trigger the inconsistent-actions warning"
    )


def test_ipi_same_pmid_divergence_still_warns():
    """Same PMID across IPI rows with divergent actions remains a real defect.

    If two rows cite the *same* paper but disagree on the curation action,
    that's curator inconsistency, not evidence-differentiated reasoning.
    The validator must still warn.
    """
    yaml_data = _build_yaml(
        "GO:0042802",
        [
            {"evidence_type": "IPI", "pmid": "PMID:19727074", "action": "ACCEPT"},
            {
                "evidence_type": "IPI",
                "pmid": "PMID:19727074",
                "action": "MARK_AS_OVER_ANNOTATED",
            },
        ],
    )
    report = _validate(yaml_data)
    assert _has_inconsistent_action_warning(report), (
        "Same PMID with divergent IPI actions should still trigger the warning"
    )


def test_mixed_evidence_divergence_still_warns():
    """Mixed evidence types (e.g. IPI + IDA) on the same term remain flagged.

    The exemption is narrowly scoped to IPI evidence because that's where
    the per-reference IntAct semantics make divergence valid. Mixed evidence
    types on the same term should still consolidate; divergence there is
    likely a real curation issue.
    """
    yaml_data = _build_yaml(
        "GO:0042802",
        [
            {"evidence_type": "IPI", "pmid": "PMID:19727074", "action": "ACCEPT"},
            {
                "evidence_type": "IDA",
                "pmid": "PMID:25155755",
                "action": "MARK_AS_OVER_ANNOTATED",
            },
        ],
    )
    report = _validate(yaml_data)
    assert _has_inconsistent_action_warning(report), (
        "Mixed evidence types with divergent actions should still trigger the warning"
    )


def test_ipi_distinct_pmid_consistent_actions_no_warning():
    """Sanity check: consistent IPI actions across distinct PMIDs never warn.

    This is the common case (multiple IntAct rows, all ACCEPTed) and should
    not trigger the inconsistent-actions warning under any version of the
    check — the exemption is irrelevant here.
    """
    yaml_data = _build_yaml(
        "GO:0042802",
        [
            {"evidence_type": "IPI", "pmid": "PMID:19727074", "action": "ACCEPT"},
            {"evidence_type": "IPI", "pmid": "PMID:25155755", "action": "ACCEPT"},
        ],
    )
    report = _validate(yaml_data)
    assert not _has_inconsistent_action_warning(report)
