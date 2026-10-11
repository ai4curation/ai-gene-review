"""Review actions on rows sharing a term must not contradict each other.

The motivating case is SCHPO/gaa1: GPI-anchor transamidase complex was ACCEPTed from
its IBA row and REMOVEd from its IEA and NAS rows, as if the review's job were to pick
the best evidence code. The existing ``inconsistent_review_actions`` warning exempted
that case because the REMOVE rows cited a different reference.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.action_consistency import (
    ConsistencyRule,
    Relation,
    Severity,
    check_action_consistency,
    iter_conflicts,
    load_rules,
    parse_rules,
)
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

ACCEPT_REMOVE = ConsistencyRule(
    "ACCEPT", "REMOVE", Relation.SAME_TERM, Severity.WARNING, "contradiction"
)


def row(action, term="GO:0042765", evidence="IEA", ref="GO_REF:0000002", **extra):
    return {
        "term": {"id": term, "label": "GPI-anchor transamidase complex"},
        "evidence_type": evidence,
        "original_reference_id": ref,
        "review": {"action": action},
        **extra,
    }


def doc(*rows):
    return {"existing_annotations": list(rows)}


def pairs(data, rules=(ACCEPT_REMOVE,)):
    return [(c.index_1, c.index_2) for c in iter_conflicts(data, rules)]


def test_gaa1_pattern_is_flagged_even_with_distinct_references():
    data = doc(
        row("ACCEPT", evidence="IBA", ref="GO_REF:0000033"),
        row("REMOVE", evidence="IEA", ref="GO_REF:0000002"),
        row("REMOVE", evidence="NAS", ref="PMID:15003443"),
    )
    assert pairs(data) == [(0, 1), (0, 2)]


@pytest.mark.parametrize(
    "actions",
    [
        ("ACCEPT", "ACCEPT"),
        ("REMOVE", "REMOVE"),
        ("ACCEPT", "KEEP_AS_NON_CORE"),
        ("MODIFY", "REMOVE"),  # not in the table yet
    ],
)
def test_unlisted_or_agreeing_pairs_pass(actions):
    assert pairs(doc(*(row(a) for a in actions))) == []


def test_order_of_rows_does_not_matter():
    assert pairs(doc(row("REMOVE"), row("ACCEPT"))) == [(1, 0)]


def test_different_terms_are_not_compared():
    assert pairs(doc(row("ACCEPT"), row("REMOVE", term="GO:0016020"))) == []


def test_negated_rows_are_not_compared():
    assert pairs(doc(row("ACCEPT"), row("REMOVE", negated=True))) == []


@pytest.mark.parametrize(
    "iso_1,iso_2,conflict",
    [("P1-1", "P1-2", False), ("P1-1", "P1-1", True), ("P1-1", None, True)],
)
def test_isoforms(iso_1, iso_2, conflict):
    data = doc(row("ACCEPT", isoform=iso_1), row("REMOVE", isoform=iso_2))
    assert bool(pairs(data)) is conflict


def test_ok_rules_report_nothing():
    ok = ConsistencyRule("ACCEPT", "REMOVE", Relation.SAME_TERM, Severity.OK, "fine")
    assert pairs(doc(row("ACCEPT"), row("REMOVE")), (ok,)) == []


def test_report_uses_table_severity_and_points_at_second_row():
    report = ValidationReport(file_path="x.yaml", is_valid=True)
    check_action_consistency(doc(row("ACCEPT"), row("REMOVE")), report)
    [issue] = [i for i in report.issues if i.check_type == "action_consistency"]
    assert issue.severity == ValidationSeverity.WARNING
    assert issue.path == "existing_annotations[1].review.action"
    assert "ACCEPT on row 0" in issue.message and "REMOVE on row 1" in issue.message


def test_packaged_table_loads_and_has_accept_remove():
    rules = load_rules()
    assert any(
        {r.action_1, r.action_2} == {"ACCEPT", "REMOVE"}
        and r.relation is Relation.SAME_TERM
        for r in rules
    )


def _raw(**overrides):
    base = {
        "action_1": "ACCEPT",
        "action_2": "REMOVE",
        "relation": "SAME_TERM",
        "severity": "WARNING",
        "rationale": "x",
    }
    return {"rules": [{**base, **overrides}]}


@pytest.mark.parametrize(
    "overrides",
    [
        {"action_1": "ACEPT"},
        {"relation": "SIBLING"},
        {"severity": "FATAL"},
        {"relation": "DESCENDANT", "severity": "WARNING"},
    ],
)
def test_malformed_rules_fail_fast(overrides):
    with pytest.raises(ValueError):
        parse_rules(_raw(**overrides))


def test_same_term_duplicates_are_unordered():
    raw = _raw()
    raw["rules"].append({**raw["rules"][0], "action_1": "REMOVE", "action_2": "ACCEPT"})
    with pytest.raises(ValueError, match="duplicate"):
        parse_rules(raw)


def test_gaa1_review_is_consistent():
    path = Path(__file__).parent.parent / "genes/SCHPO/gaa1/gaa1-ai-review.yaml"
    assert list(iter_conflicts(yaml.safe_load(path.read_text()))) == []
