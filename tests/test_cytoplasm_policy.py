"""Tests for the cytoplasm policy (``cytoplasm_policy`` warnings and audit).

The policy is ``projects/CYTOPLASM.md``: in a eukaryote ``GO:0005737`` cytoplasm
includes every organelle, so it is never a core location; in a prokaryote it is the
main localisation contrast and keeps the normal rules.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, FrozenSet

import pytest

from ai_gene_review.validation.cytoplasm_policy import (
    CHECK_TYPE,
    CYTOPLASM,
    asserted_terms,
    audit,
    check_cytoplasm_policy,
    domain_for_review,
    entailing_terms,
    find_cytoplasm_findings,
)
from ai_gene_review.validation.validation_report import ValidationReport

CYTOSOL = "GO:0005829"
MITOCHONDRION = "GO:0005739"
MICROTUBULE = "GO:0005874"
NUCLEUS = "GO:0005634"

#: A fixed is_a/part_of ancestor table, so the logic is tested without the GO database.
#: It mirrors the real GO: cytosol and mitochondrion are under cytoplasm; microtubule
#: is not, because microtubules also occur in the nucleus (the spindle).
ANCESTORS: Dict[str, FrozenSet[str]] = {
    CYTOSOL: frozenset({CYTOPLASM}),
    MITOCHONDRION: frozenset({CYTOPLASM}),
    MICROTUBULE: frozenset(),
    NUCLEUS: frozenset(),
}


def ancestors(term_id: str) -> FrozenSet[str]:
    """Ancestors from :data:`ANCESTORS` (empty for unlisted terms)."""
    return ANCESTORS.get(term_id, frozenset())


def row(
    term_id: str, action: str, evidence: str = "IDA", **extra: Any
) -> Dict[str, Any]:
    """A minimal existing-annotation row."""
    review = {"action": action, **extra.pop("review", {})}
    return {
        "term": {"id": term_id},
        "evidence_type": evidence,
        "review": review,
        **extra,
    }


def doc(*rows: Dict[str, Any], locations: tuple[str, ...] = ()) -> Dict[str, Any]:
    """A review with the given rows and one core function at *locations*."""
    data: Dict[str, Any] = {"existing_annotations": list(rows)}
    if locations:
        data["core_functions"] = [{"locations": [{"id": t} for t in locations]}]
    return data


def categories(
    data: Dict[str, Any], domain: str, with_ontology: bool = True
) -> list[str]:
    """Finding categories for *data* in *domain*."""
    return [
        f.category
        for f in find_cytoplasm_findings(
            data, domain, ancestors if with_ontology else None
        )
    ]


@pytest.mark.parametrize(
    "action,expected",
    [
        ("ACCEPT", ["EUK_ACCEPT"]),
        ("NEW", ["EUK_NEW"]),
        ("KEEP_AS_NON_CORE", []),
        ("MARK_AS_OVER_ANNOTATED", []),
        ("REMOVE", []),
        ("UNDECIDED", []),
    ],
)
def test_eukaryotic_actions(action, expected):
    """ACCEPT and NEW are flagged; the non-core and rejecting actions are not."""
    assert categories(doc(row(CYTOPLASM, action)), "Eukaryota") == expected


@pytest.mark.parametrize("domain", ["Bacteria", "Archaea"])
@pytest.mark.parametrize("action", ["ACCEPT", "NEW", "KEEP_AS_NON_CORE", "MODIFY"])
def test_prokaryotes_keep_the_normal_rules(domain, action):
    """In a prokaryote cytoplasm is informative, so it may be core."""
    data = doc(row(CYTOPLASM, action, "IEA"), locations=(CYTOPLASM,))
    assert categories(data, domain) == []


@pytest.mark.parametrize("domain", ["Bacteria", "Archaea"])
def test_prokaryotic_too_general_is_flagged(domain):
    """Like a root organelle term, prokaryotic cytoplasm is never TOO_GENERAL."""
    data = doc(row(CYTOPLASM, "TOO_GENERAL"), row(CYTOSOL, "ACCEPT"))
    assert categories(data, domain) == ["PROK_TOO_GENERAL"]


@pytest.mark.parametrize("domain", ["Viruses", None, "unknown"])
def test_out_of_scope_lineages_are_skipped(domain):
    data = doc(row(CYTOPLASM, "ACCEPT"), locations=(CYTOPLASM,))
    assert categories(data, domain) == []


def test_not_rows_are_skipped():
    """A NOT cytoplasm row is a negative claim and carries information."""
    assert categories(doc(row(CYTOPLASM, "ACCEPT", negated=True)), "Eukaryota") == []


def test_core_function_location_is_flagged():
    data = doc(row(CYTOSOL, "ACCEPT"), locations=(CYTOSOL, CYTOPLASM))
    (finding,) = find_cytoplasm_findings(data, "Eukaryota", ancestors)
    assert finding.category == "EUK_CORE_LOCATION"
    assert finding.path == "core_functions[0].locations[1]"


@pytest.mark.parametrize("evidence", ["IBA", "IEA", "ISS", "ISO"])
def test_modify_on_a_propagated_row_is_an_audit_finding(evidence):
    """A propagated row's evidence stops at cytoplasm, so it cannot support MODIFY."""
    data = doc(
        row(
            CYTOPLASM,
            "MODIFY",
            evidence,
            review={"proposed_replacement_terms": [{"id": CYTOSOL}]},
        )
    )
    assert categories(data, "Eukaryota") == ["EUK_MODIFY_PROPAGATED"]


@pytest.mark.parametrize("evidence", ["IDA", "EXP", "HDA", "TAS", "IC"])
def test_modify_on_an_experimental_or_curator_row_is_not_flagged(evidence):
    """Whether the paper resolves the sub-location is a judgement the check cannot make."""
    data = doc(
        row(
            CYTOPLASM,
            "MODIFY",
            evidence,
            review={"proposed_replacement_terms": [{"id": CYTOSOL}]},
        )
    )
    assert categories(data, "Eukaryota") == []


def test_too_general_needs_an_entailing_term():
    """TOO_GENERAL is right when a cytosol row entails cytoplasm, not otherwise."""
    entailed = doc(row(CYTOPLASM, "TOO_GENERAL", "IEA"), row(CYTOSOL, "ACCEPT"))
    assert categories(entailed, "Eukaryota") == []
    unentailed = doc(row(CYTOPLASM, "TOO_GENERAL", "IEA"), row(MICROTUBULE, "ACCEPT"))
    assert categories(unentailed, "Eukaryota") == ["EUK_TOO_GENERAL_UNENTAILED"]


def test_too_general_is_not_judged_without_the_ontology():
    data = doc(row(CYTOPLASM, "TOO_GENERAL", "IEA"))
    assert categories(data, "Eukaryota", with_ontology=False) == []


def test_entailing_terms_follow_the_ontology_and_ignore_rejected_rows():
    data = doc(
        row(CYTOPLASM, "ACCEPT"),
        row(MITOCHONDRION, "KEEP_AS_NON_CORE"),
        row(CYTOSOL, "REMOVE"),
        row(MICROTUBULE, "ACCEPT"),
        row(NUCLEUS, "ACCEPT"),
    )
    assert entailing_terms(data, 0, ancestors) == [MITOCHONDRION]


def test_a_modify_replacement_counts_as_asserted():
    data = doc(
        row(
            MITOCHONDRION,
            "MODIFY",
            review={"proposed_replacement_terms": [{"id": CYTOSOL}]},
        )
    )
    assert asserted_terms(data) == {CYTOSOL}


def test_accept_finding_carries_the_entailing_terms():
    data = doc(row(CYTOPLASM, "ACCEPT", "IBA"), row(CYTOSOL, "ACCEPT", "IDA"))
    (finding,) = find_cytoplasm_findings(data, "Eukaryota", ancestors)
    assert finding.entailing == (CYTOSOL,)


def to_cytoplasm(term_id: str, **extra: Any) -> Dict[str, Any]:
    """A MODIFY row on *term_id* whose replacement is cytoplasm (the MCL1 shape)."""
    return row(
        term_id,
        "MODIFY",
        "IEA",
        review={"proposed_replacement_terms": [{"id": CYTOPLASM}]},
        **extra,
    )


def test_modify_to_cytoplasm_is_flagged_in_eukaryotes():
    """A replacement of cytoplasm asserts cytoplasm just as a NEW row does."""
    (finding,) = find_cytoplasm_findings(doc(to_cytoplasm(CYTOSOL)), "Eukaryota")
    assert finding.category == "EUK_MODIFY_TO_CYTOPLASM"
    assert finding.term_id == CYTOSOL
    assert finding.path == (
        "existing_annotations[0].review.proposed_replacement_terms[0]"
    )


@pytest.mark.parametrize("domain", ["Bacteria", "Archaea"])
def test_modify_to_cytoplasm_is_allowed_in_prokaryotes(domain):
    """A membrane-to-cytoplasm correction in a bacterium is a real lateral fix."""
    assert categories(doc(to_cytoplasm("GO:0005886")), domain) == []


def test_modify_to_cytoplasm_on_a_not_row_is_skipped():
    assert categories(doc(to_cytoplasm(CYTOSOL, negated=True)), "Eukaryota") == []


def test_validator_sees_a_review_whose_only_cytoplasm_is_a_replacement(tmp_path):
    """The review has no cytoplasm row, so the validator must not skip it."""
    review = write_review(tmp_path / "M", "OC   Eukaryota; Metazoa; Chordata;")
    report = ValidationReport(file_path=review, is_valid=True)
    check_cytoplasm_policy(doc(to_cytoplasm(CYTOSOL)), report, review, ancestors)
    (issue,) = [i for i in report.issues if i.check_type == CHECK_TYPE]
    assert CYTOSOL in issue.message
    assert "laterally" in issue.suggestion


@pytest.mark.parametrize(
    "cytosol_isoform,entailed",
    [("P1-2", False), ("P1-1", True), (None, True)],
)
def test_entailment_does_not_cross_isoforms(cytosol_isoform, entailed):
    """As in action_consistency, a row on another isoform makes an independent claim."""
    cytosol = row(CYTOSOL, "ACCEPT")
    if cytosol_isoform:
        cytosol["isoform"] = cytosol_isoform
    data = doc(row(CYTOPLASM, "ACCEPT", isoform="P1-1"), cytosol)
    (finding,) = find_cytoplasm_findings(data, "Eukaryota", ancestors)
    assert finding.entailing == ((CYTOSOL,) if entailed else ())


def write_review(folder: Path, oc_line: str) -> Path:
    """A gene folder holding a review path and a UniProt record with *oc_line*."""
    folder.mkdir(parents=True)
    (folder / "X-uniprot.txt").write_text(
        f"ID   X_HUMAN\n{oc_line}\nOX   NCBI_TaxID=1;\n"
    )
    return folder / "X-ai-review.yaml"


def test_domain_is_read_from_the_uniprot_record(tmp_path):
    review = write_review(tmp_path / "X", "OC   Eukaryota; Metazoa; Chordata;")
    assert domain_for_review(review) == "Eukaryota"
    assert domain_for_review(tmp_path / "missing" / "Y-ai-review.yaml") is None


def test_validator_warns_with_tailored_advice(tmp_path):
    review = write_review(tmp_path / "X", "OC   Eukaryota; Metazoa; Chordata;")
    data = doc(
        row(CYTOPLASM, "ACCEPT", "IBA"),
        row(CYTOSOL, "ACCEPT"),
        row(CYTOPLASM, "MODIFY", "IEA"),
        locations=(CYTOPLASM,),
    )
    report = ValidationReport(file_path=review, is_valid=True)
    check_cytoplasm_policy(data, report, review, ancestors)
    issues = [i for i in report.issues if i.check_type == CHECK_TYPE]
    # The propagated MODIFY row is audit-only, so two warnings, not three.
    assert [i.path for i in issues] == [
        "existing_annotations[0].review.action",
        "core_functions[0].locations[0]",
    ]
    assert "TOO_GENERAL" in issues[0].suggestion
    assert CYTOSOL in issues[0].suggestion
    assert report.is_valid


def test_validator_is_silent_for_bacteria(tmp_path):
    review = write_review(tmp_path / "Y", "OC   Bacteria; Pseudomonadota;")
    report = ValidationReport(file_path=review, is_valid=True)
    check_cytoplasm_policy(doc(row(CYTOPLASM, "ACCEPT")), report, review, ancestors)
    assert not [i for i in report.issues if i.check_type == CHECK_TYPE]


def test_audit_tallies_rows_and_findings(tmp_path):
    import yaml

    euk = write_review(tmp_path / "E", "OC   Eukaryota; Fungi;")
    euk.write_text(
        yaml.safe_dump(doc(row(CYTOPLASM, "ACCEPT"), row(CYTOSOL, "ACCEPT")))
    )
    bac = write_review(tmp_path / "B", "OC   Bacteria; Bacillota;")
    bac.write_text(yaml.safe_dump(doc(row(CYTOPLASM, "ACCEPT"))))
    rows, by_action, by_category = audit([euk, bac], ancestors)
    assert [r[2] for r in rows[1:]] == ["EUK_ACCEPT"]
    assert rows[1][-1] == CYTOSOL
    assert by_action == {("Eukaryota", "ACCEPT"): 1, ("Bacteria", "ACCEPT"): 1}
    assert dict(by_category) == {"EUK_ACCEPT": 1}


@pytest.mark.integration
def test_real_go_places_organelles_but_not_the_cytoskeleton_under_cytoplasm():
    """The entailment the TOO_GENERAL check relies on, read from the GO snapshot."""
    from ai_gene_review.validation.action_consistency import go_ancestors

    lookup = go_ancestors().load()
    assert CYTOPLASM in lookup(CYTOSOL)
    assert CYTOPLASM in lookup(MITOCHONDRION)
    assert CYTOPLASM not in lookup(MICROTUBULE)
    assert CYTOPLASM not in lookup(NUCLEUS)
