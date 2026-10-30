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
        {r.side_1.actions, r.side_2.actions}
        == {frozenset({"ACCEPT"}), frozenset({"REMOVE"})}
        and r.relation is Relation.SAME_TERM
        and not (r.negated_1 or r.negated_2)
        and r.term_1 is None
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
    rules = [
        r
        for r in load_rules()
        if r.relation is not Relation.SAME_TERM
        and not (r.negated_1 or r.negated_2)
        and "TOO_GENERAL" in r.side_1.actions | r.side_2.actions
    ]
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


# --- NOT annotations -------------------------------------------------------


def not_row(action, **extra):
    return row(action, negated=True, **extra)


@pytest.mark.parametrize(
    "neg_action,pos_action,conflict",
    [
        ("ACCEPT", "ACCEPT", True),
        ("KEEP_AS_NON_CORE", "TOO_GENERAL", True),
        ("ACCEPT", "NEW", True),
        ("REMOVE", "ACCEPT", False),  # doubting the NOT claim is consistent
        ("ACCEPT", "REMOVE", False),  # keeping NOT while removing the positive
        ("REMOVE", "REMOVE", False),  # agnostic
        ("UNDECIDED", "ACCEPT", False),
    ],
)
def test_packaged_table_kept_not_vs_kept_positive(neg_action, pos_action, conflict):
    data = doc(not_row(neg_action), row(pos_action))
    conflicts = list(iter_conflicts(data))
    assert bool(conflicts) is conflict
    if conflict:
        # the NOT row is side 1 of the rule
        assert (conflicts[0].index_1, conflicts[0].index_2) == (0, 1)


def test_positive_only_rule_still_ignores_not_rows():
    """ACCEPT on a NOT row and REMOVE on the positive row agree with each other."""
    assert pairs(doc(not_row("ACCEPT"), row("REMOVE"))) == []


def test_polarity_distinguishes_otherwise_identical_rules():
    raw = {
        "rules": [
            _raw()["rules"][0],
            {**_raw()["rules"][0], "negated_1": True, "severity": "ERROR"},
        ]
    }
    assert len(parse_rules(raw)) == 2


def test_action_lists_overlap_for_ambiguity():
    raw = {
        "rules": [
            {**_raw()["rules"][0], "action_1": ["ACCEPT", "KEEP_AS_NON_CORE"]},
            {**_raw()["rules"][0], "action_1": "KEEP_AS_NON_CORE", "severity": "ERROR"},
        ]
    }
    with pytest.raises(ValueError, match="ambiguous"):
        parse_rules(raw)


@pytest.mark.parametrize(
    "overrides",
    [
        {"action_1": []},
        {"action_1": ["ACCEPT", "ACEPT"]},
        {"negated_1": "yes"},
    ],
)
def test_malformed_lists_and_flags_fail_fast(overrides):
    with pytest.raises(ValueError):
        parse_rules(_raw(**overrides))


# --- per-annotation exceptions and single-row checks ------------------------


def issues(data, ancestors=None):
    report = ValidationReport(file_path="x.yaml", is_valid=True)
    check_action_consistency(data, report, ancestors=ancestors)
    return [i for i in report.issues if i.check_type == "action_consistency"]


def test_consistency_exception_downgrades_to_info_with_reason():
    excepted = not_row("ACCEPT")
    excepted["review"]["consistency_exception"] = {
        "reason": "NOT in roots, positive in shoots"
    }
    [issue] = issues(doc(excepted, row("ACCEPT")))
    assert issue.severity == ValidationSeverity.INFO
    assert "NOT in roots, positive in shoots" in issue.message


def test_stale_consistency_exception_is_flagged():
    stale = row("ACCEPT")
    stale["review"]["consistency_exception"] = {"reason": "left over"}
    [issue] = issues(doc(stale, row("ACCEPT")), ancestors=lambda t: frozenset())
    assert issue.severity == ValidationSeverity.WARNING
    assert "not in any action-consistency conflict" in issue.message


def test_too_general_on_not_row_is_an_error():
    [issue] = issues(doc(not_row("TOO_GENERAL")))
    assert issue.severity == ValidationSeverity.ERROR


# --- hierarchical rules ------------------------------------------------------

#: Toy hierarchy: GO:C part_of GO:B is_a GO:A.
TOY = {"GO:C": frozenset({"GO:B", "GO:A"}), "GO:B": frozenset({"GO:A"})}


def toy(term_id):
    return TOY.get(term_id, frozenset())


def hrows(*specs):
    """specs: (term, action, negated)."""
    return doc(
        *(
            row(action, term=term, negated=True) if neg else row(action, term=term)
            for term, action, neg in specs
        )
    )


@pytest.mark.parametrize(
    "specs,expected",
    [
        # kept NOT on an ancestor of a kept positive term: conflict
        ((("GO:A", "ACCEPT", True), ("GO:C", "ACCEPT", False)), [(0, 1)]),
        ((("GO:B", "KEEP_AS_NON_CORE", True), ("GO:C", "NEW", False)), [(0, 1)]),
        # row order does not matter; index_1 is always the NOT (action_1) row
        ((("GO:C", "ACCEPT", False), ("GO:A", "ACCEPT", True)), [(1, 0)]),
        # NOT on a descendant of a positive term is consistent
        ((("GO:C", "ACCEPT", True), ("GO:A", "ACCEPT", False)), []),
        # doubting the NOT claim is consistent
        ((("GO:A", "REMOVE", True), ("GO:C", "ACCEPT", False)), []),
        # unrelated terms
        ((("GO:A", "ACCEPT", True), ("GO:X", "ACCEPT", False)), []),
    ],
)
def test_packaged_not_ancestor_rule(specs, expected):
    conflicts = [c for c in iter_conflicts(hrows(*specs), ancestors=toy) if c.term_id_2]
    assert [(c.index_1, c.index_2) for c in conflicts] == expected


def test_hierarchical_rules_need_an_ancestor_lookup():
    data = hrows(("GO:A", "ACCEPT", True), ("GO:C", "ACCEPT", False))
    assert list(iter_conflicts(data)) == []


def test_hierarchical_conflict_message_names_both_terms():
    report = ValidationReport(file_path="x.yaml", is_valid=True)
    data = hrows(("GO:A", "ACCEPT", True), ("GO:C", "ACCEPT", False))
    check_action_consistency(data, report, ancestors=toy)
    [issue] = [i for i in report.issues if i.check_type == "action_consistency"]
    assert "GO:A" in issue.message and "GO:C" in issue.message
    assert "is an ancestor of" in issue.message


def test_hierarchical_term_filter_exception():
    general = _raw(
        action_1="ACCEPT",
        relation="ANCESTOR_OF",
        action_2="ACCEPT",
        negated_1=True,
    )["rules"][0]
    rules = tuple(
        parse_rules(
            {
                "rules": [
                    general,
                    {**general, "term_1": {"exact": "GO:A"}, "severity": "OK"},
                ]
            }
        )
    )
    flagged = hrows(("GO:B", "ACCEPT", True), ("GO:C", "ACCEPT", False))
    exempt = hrows(("GO:A", "ACCEPT", True), ("GO:C", "ACCEPT", False))
    assert len(list(iter_conflicts(flagged, rules, toy))) == 1
    assert list(iter_conflicts(exempt, rules, toy)) == []


def test_exception_not_called_stale_when_hierarchy_was_not_checked():
    excepted = row("ACCEPT", term="GO:A", negated=True)
    excepted["review"]["consistency_exception"] = {"reason": "context-specific"}
    data = doc(excepted, row("ACCEPT", term="GO:C"))
    assert issues(data) == []  # hierarchy not evaluated: no conflict, no stale flag
    report = ValidationReport(file_path="x.yaml", is_valid=True)
    check_action_consistency(data, report, ancestors=toy)
    [issue] = [i for i in report.issues if i.check_type == "action_consistency"]
    assert issue.severity == ValidationSeverity.INFO


@pytest.mark.integration
def test_real_go_hierarchy_uses_part_of():
    """WIPI2-shaped case: autophagosome membrane is part_of autophagosome."""
    from ai_gene_review.validation.action_consistency import go_ancestors

    data = hrows(
        ("GO:0005776", "ACCEPT", True), ("GO:0000421", "KEEP_AS_NON_CORE", False)
    )
    [conflict] = iter_conflicts(data, ancestors=go_ancestors())
    assert (conflict.term_id, conflict.term_id_2) == ("GO:0005776", "GO:0000421")


def test_go_ancestors_fails_fast_on_a_bad_adapter():
    """A broken ontology must raise, never silently skip hierarchical rules."""
    from ai_gene_review.validation.action_consistency import GoAncestors

    with pytest.raises(Exception):
        GoAncestors("sqlite:/nonexistent/path/go.db").load()


@pytest.mark.parametrize(
    "specs,flagged",
    [
        # justified by an accepted descendant
        ((("GO:A", "TOO_GENERAL", False), ("GO:C", "ACCEPT", False)), False),
        # no descendant at all
        ((("GO:A", "TOO_GENERAL", False), ("GO:X", "ACCEPT", False)), True),
        # the only descendant is removed, so nothing more specific is asserted
        ((("GO:A", "TOO_GENERAL", False), ("GO:C", "REMOVE", False)), True),
        # a NOT descendant asserts nothing positive
        ((("GO:A", "TOO_GENERAL", False), ("GO:C", "ACCEPT", True)), True),
    ],
)
def test_too_general_needs_an_asserted_descendant(specs, flagged):
    found = [
        i
        for i in issues(hrows(*specs), ancestors=toy)
        if "no more specific term is asserted" in i.message
    ]
    assert bool(found) is flagged


def test_too_general_precondition_needs_the_ontology():
    data = hrows(("GO:A", "TOO_GENERAL", False))
    assert issues(data) == []


@pytest.mark.integration
@pytest.mark.parametrize("gene", ["SCHPO/gaa1", "PSEAE/rhlB", "AGKCO/fibrolase"])
def test_worked_examples_are_clean_with_real_go(gene):
    """The docs' worked examples must pass every check, hierarchical ones included."""
    from ai_gene_review.validation.action_consistency import go_ancestors

    org, symbol = gene.split("/")
    path = (
        Path(__file__).parent.parent / f"genes/{org}/{symbol}/{symbol}-ai-review.yaml"
    )
    data = yaml.safe_load(path.read_text())
    assert issues(data, ancestors=go_ancestors()) == []
