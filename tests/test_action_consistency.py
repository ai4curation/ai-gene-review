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
        {"relation": "DESCENDANT", "severity": "OK"},  # old, ambiguous name
        {"relation": "DESCENDANT_OF", "severity": "WARNING"},
        {"relation": "ANCESTOR_OF", "severity": "ERROR"},
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


def test_mirror_image_hierarchical_rules_are_duplicates():
    """ "A ANCESTOR_OF B" and "B DESCENDANT_OF A" state the same rule."""
    raw = _raw(
        action_1="TOO_GENERAL", relation="ANCESTOR_OF", action_2="ACCEPT", severity="OK"
    )
    raw["rules"].append(
        {
            **raw["rules"][0],
            "action_1": "ACCEPT",
            "relation": "DESCENDANT_OF",
            "action_2": "TOO_GENERAL",
        }
    )
    with pytest.raises(ValueError, match="duplicate"):
        parse_rules(raw)


def test_same_direction_with_swapped_actions_is_a_different_rule():
    """Direction matters: these say opposite things about which term is broader."""
    raw = _raw(
        action_1="TOO_GENERAL", relation="ANCESTOR_OF", action_2="ACCEPT", severity="OK"
    )
    raw["rules"].append(
        {**raw["rules"][0], "action_1": "ACCEPT", "action_2": "TOO_GENERAL"}
    )
    assert len(parse_rules(raw)) == 2


def test_packaged_table_puts_too_general_on_the_broader_term():
    rules = [r for r in load_rules() if "TOO_GENERAL" in (r.action_1, r.action_2)]
    assert rules
    for r in rules:
        assert r.describe().startswith("the TOO_GENERAL row's term is an ancestor of")


PB = {"exact": "GO:0005515"}


def test_exception_rule_overrides_general_rule():
    rules = tuple(
        parse_rules(
            {
                "rules": [
                    _raw()["rules"][0],
                    {**_raw()["rules"][0], "term_1": PB, "severity": "OK"},
                ]
            }
        )
    )
    pb = doc(row("ACCEPT", term="GO:0005515"), row("REMOVE", term="GO:0005515"))
    other = doc(row("ACCEPT"), row("REMOVE"))
    assert pairs(pb, rules) == []
    assert pairs(other, rules) == [(0, 1)]


def test_exception_can_also_tighten():
    """A filtered rule may raise severity for one term, not just exempt it."""
    rules = tuple(
        parse_rules(
            {
                "rules": [
                    {**_raw()["rules"][0], "severity": "OK"},
                    {
                        **_raw()["rules"][0],
                        "term_1": {"exact": ["GO:1", "GO:2"]},
                        "severity": "ERROR",
                    },
                ]
            }
        )
    )
    [c] = iter_conflicts(
        doc(row("ACCEPT", term="GO:2"), row("REMOVE", term="GO:2")), rules
    )
    assert c.rule.severity is Severity.ERROR
    assert list(iter_conflicts(doc(row("ACCEPT"), row("REMOVE")), rules)) == []


def test_equally_specific_overlapping_disagreeing_rules_are_ambiguous():
    raw = {
        "rules": [
            {
                **_raw()["rules"][0],
                "term_1": {"exact": ["GO:1", "GO:2"]},
                "severity": "OK",
            },
            {
                **_raw()["rules"][0],
                "term_1": {"exact": ["GO:2", "GO:3"]},
                "severity": "ERROR",
            },
        ]
    }
    with pytest.raises(ValueError, match="ambiguous"):
        parse_rules(raw)


def test_disjoint_filters_are_not_ambiguous():
    raw = {
        "rules": [
            {**_raw()["rules"][0], "term_1": {"exact": "GO:1"}, "severity": "OK"},
            {**_raw()["rules"][0], "term_1": {"exact": "GO:2"}, "severity": "ERROR"},
        ]
    }
    assert len(parse_rules(raw)) == 2


def test_hierarchical_mirror_with_filters_is_a_duplicate():
    """Filters travel with their action when a rule is mirrored."""
    base = _raw(
        action_1="REMOVE",
        relation="ANCESTOR_OF",
        action_2="ACCEPT",
        severity="OK",
        term_1=PB,
    )
    mirror = {
        **base["rules"][0],
        "action_1": "ACCEPT",
        "relation": "DESCENDANT_OF",
        "action_2": "REMOVE",
        "term_2": PB,
    }
    del mirror["term_1"]
    base["rules"].append(mirror)
    with pytest.raises(ValueError, match="duplicate"):
        parse_rules(base)


@pytest.mark.parametrize(
    "overrides",
    [
        {"term_1": {"self_or_descendant": "GO:0005488"}},  # reserved
        {"term_1": {"fuzzy": "GO:0005515"}},
        {"term_1": {"exact": []}},
        {"term_1": "GO:0005515"},
        {"term_2": PB},  # SAME_TERM takes term_1 only
        {"term_3": PB},
    ],
)
def test_malformed_term_filters_fail_fast(overrides):
    with pytest.raises(ValueError):
        parse_rules(_raw(**overrides))


def test_packaged_table_exempts_protein_binding():
    data = doc(row("ACCEPT", term="GO:0005515"), row("REMOVE", term="GO:0005515"))
    assert list(iter_conflicts(data)) == []
