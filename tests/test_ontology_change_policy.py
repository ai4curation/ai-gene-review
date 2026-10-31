"""Tests for the proposed-ontology-change consistency checks."""

from __future__ import annotations

import pytest

from ai_gene_review.validation.ontology_change_policy import (
    iter_ontology_change_violations,
    kgcl_dsl,
    parse_kgcl,
)

GO_A = {"id": "GO:0099022", "label": "vesicle tethering"}
GO_B = {"id": "GO:7770062", "label": "vesicle membrane tethering activity"}


def _change(**kw):
    """A minimally valid change, overridable per test."""
    base = {
        "change_type": "NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT",
        "ontology": "GO",
        "about_node": dict(GO_A),
        "has_direct_replacement": dict(GO_B),
        "justification": "Tethering is a binding activity, not a process.",
        "confidence": "PROBABLE",
    }
    base.update(kw)
    return base


def _codes(data):
    return sorted({code for _, _, code, _, _ in iter_ontology_change_violations(data)})


def test_a_well_formed_obsoletion_with_replacement_passes():
    assert _codes({"proposed_ontology_changes": [_change()]}) == []


def test_direct_replacement_obsoletion_requires_the_replacement():
    data = {"proposed_ontology_changes": [_change(has_direct_replacement=None)]}
    assert "missing_direct_replacement" in _codes(data)


def test_nondirect_obsoletion_must_not_carry_a_direct_replacement():
    data = {
        "proposed_ontology_changes": [
            _change(change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT")
        ]
    }
    assert "unexpected_direct_replacement" in _codes(data)


def test_nondirect_obsoletion_without_any_replacement_is_fine():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
                has_direct_replacement=None,
            )
        ]
    }
    assert _codes(data) == []


def test_merge_requires_a_surviving_term():
    data = {
        "proposed_ontology_changes": [
            _change(change_type="NODE_DIRECT_MERGE", has_direct_replacement=None)
        ]
    }
    assert "missing_direct_replacement" in _codes(data)


@pytest.mark.parametrize(
    "change_type",
    ["NODE_TEXT_DEFINITION_CHANGE", "NODE_RENAME", "MAPPING_PREDICATE_CHANGE"],
)
def test_value_changes_need_both_old_and_new_value(change_type):
    data = {
        "proposed_ontology_changes": [
            _change(change_type=change_type, has_direct_replacement=None, new_value="x")
        ]
    }
    assert "missing_old_value" in _codes(data)


def test_value_changes_need_a_new_value_too():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="NODE_RENAME",
                has_direct_replacement=None,
                old_value="vesicle tethering",
            )
        ]
    }
    assert "missing_new_value" in _codes(data)


def test_a_rename_that_does_not_change_anything_is_flagged():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="NODE_RENAME",
                has_direct_replacement=None,
                old_value="vesicle tethering",
                new_value="vesicle tethering",
            )
        ]
    }
    assert "value_unchanged" in _codes(data)


@pytest.mark.parametrize(
    "change_type", ["EDGE_CREATION", "EDGE_DELETION", "NODE_MOVE", "NODE_DEEPENING"]
)
def test_edge_changes_need_a_subject_and_a_predicate(change_type):
    data = {
        "proposed_ontology_changes": [
            _change(change_type=change_type, has_direct_replacement=None)
        ]
    }
    codes = _codes(data)
    assert "missing_subject" in codes
    assert "missing_predicate" in codes


def test_a_term_must_not_be_replaced_by_itself():
    data = {"proposed_ontology_changes": [_change(has_direct_replacement=dict(GO_A))]}
    assert "self_replacement" in _codes(data)


def test_a_term_must_not_appear_as_its_own_nondirect_replacement():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
                has_direct_replacement=None,
                has_nondirect_replacement=[dict(GO_A), dict(GO_B)],
            )
        ]
    }
    assert "self_replacement" in _codes(data)


def test_complex_change_wants_a_long_justification():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="COMPLEX_CHANGE",
                has_direct_replacement=None,
                justification="Split it.",
            )
        ]
    }
    assert "thin_justification" in _codes(data)


def test_other_change_type_wants_a_long_justification():
    data = {
        "proposed_ontology_changes": [
            _change(
                change_type="OTHER", has_direct_replacement=None, justification="Fix."
            )
        ]
    }
    assert "thin_justification" in _codes(data)


def test_a_filed_report_needs_a_tracker_link():
    data = {"proposed_ontology_changes": [_change(report_status="REPORTED")]}
    assert "missing_tracker_issue" in _codes(data)


def test_a_filed_report_with_a_tracker_link_passes():
    data = {
        "proposed_ontology_changes": [
            _change(
                report_status="REPORTED",
                term_tracker_issue="https://github.com/geneontology/go-ontology/issues/1",
            )
        ]
    }
    assert _codes(data) == []


def test_a_change_dsl_that_contradicts_the_structured_slots_is_flagged():
    data = {
        "proposed_ontology_changes": [
            _change(change_dsl="obsolete GO:0000001 with replacement GO:7770062")
        ]
    }
    assert "dsl_disagrees" in _codes(data)


def test_a_change_dsl_that_agrees_passes():
    data = {
        "proposed_ontology_changes": [
            _change(change_dsl="obsolete GO:0099022 with replacement GO:7770062")
        ]
    }
    assert _codes(data) == []


def test_proposing_a_change_to_a_term_the_review_also_accepts_is_flagged():
    """A review should not accept a term on one row and ask for its obsoletion."""
    data = {
        "existing_annotations": [
            {"term": dict(GO_A), "review": {"action": "ACCEPT"}},
        ],
        "proposed_ontology_changes": [_change()],
    }
    assert "obsoletion_of_accepted_term" in _codes(data)


def test_proposing_obsoletion_of_a_term_the_review_modifies_is_consistent():
    data = {
        "existing_annotations": [
            {
                "term": dict(GO_A),
                "review": {
                    "action": "MODIFY",
                    "proposed_replacement_terms": [dict(GO_B)],
                },
            },
        ],
        "proposed_ontology_changes": [_change()],
    }
    assert _codes(data) == []


def test_module_reviews_are_checked_too():
    data = {
        "module": {"id": "x"},
        "proposed_ontology_changes": [_change(has_direct_replacement=None)],
    }
    assert "missing_direct_replacement" in _codes(data)


def test_no_changes_is_not_a_violation():
    assert _codes({"existing_annotations": []}) == []


class TestKgclDsl:
    """Rendering structured slots into KGCL's controlled English.

    Every string is validated by KGCL's own parser, so these tests pin what the
    grammar actually accepts rather than what looks plausible.
    """

    def test_obsoletion_with_replacement(self):
        assert kgcl_dsl(_change()) == "obsolete GO:0099022 with replacement GO:7770062"

    def test_obsoletion_without_replacement(self):
        change = _change(
            change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
            has_direct_replacement=None,
        )
        assert kgcl_dsl(change) == "obsolete GO:0099022"

    def test_nondirect_replacements_are_absent_from_the_dsl(self):
        """KGCL's grammar has no syntax for `consider`, so a correct DSL omits it."""
        change = _change(
            change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
            has_direct_replacement=None,
            has_nondirect_replacement=[dict(GO_B)],
        )
        assert kgcl_dsl(change) == "obsolete GO:0099022"

    def test_merge_has_no_dsl_form(self):
        """KGCL models NodeDirectMerge but its DSL grammar has no merge statement."""
        assert kgcl_dsl(_change(change_type="NODE_DIRECT_MERGE")) is None

    def test_mapping_removal_has_no_dsl_form(self):
        change = _change(
            change_type="REMOVE_MAPPING",
            has_direct_replacement=None,
            old_value="InterPro:IPR007225",
        )
        assert kgcl_dsl(change) is None

    def test_rename(self):
        change = _change(
            change_type="NODE_RENAME",
            has_direct_replacement=None,
            old_value="vesicle tethering",
            new_value="vesicle membrane tethering",
        )
        assert kgcl_dsl(change) == (
            "rename GO:0099022 from 'vesicle tethering' to 'vesicle membrane tethering'"
        )

    def test_definition_change_uses_the_grammars_to_only_form(self):
        """The grammar is `change definition of X to Y` - there is no `from` clause."""
        change = _change(
            change_type="NODE_TEXT_DEFINITION_CHANGE",
            has_direct_replacement=None,
            old_value="an old definition",
            new_value="a new definition",
        )
        assert kgcl_dsl(change) == (
            "change definition of GO:0099022 to 'a new definition'"
        )

    def test_new_synonym(self):
        change = _change(
            change_type="NEW_SYNONYM", has_direct_replacement=None, new_value="tethering"
        )
        assert kgcl_dsl(change) == "create synonym 'tethering' for GO:0099022"

    def test_edge_creation(self):
        change = _change(
            change_type="EDGE_CREATION",
            has_direct_replacement=None,
            subject={"id": "GO:0016192", "label": "vesicle-mediated transport"},
            predicate="BFO:0000050",
        )
        assert kgcl_dsl(change) == "create edge GO:0099022 BFO:0000050 GO:0016192"

    def test_deepening(self):
        change = _change(
            change_type="NODE_DEEPENING",
            has_direct_replacement=None,
            old_value="GO:0016192",
            subject={"id": "GO:0006888", "label": "ER to Golgi transport"},
            predicate="rdfs:subClassOf",
        )
        assert kgcl_dsl(change) == "deepen GO:0099022 from GO:0016192 to GO:0006888"

    def test_other_has_no_dsl(self):
        change = _change(change_type="OTHER", has_direct_replacement=None)
        assert kgcl_dsl(change) is None

    def test_every_rendered_dsl_parses_as_kgcl(self):
        """The renderer must never emit a string KGCL cannot read."""
        for change_type in [
            "NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT",
            "NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
            "NODE_RENAME",
            "NODE_TEXT_DEFINITION_CHANGE",
            "NEW_SYNONYM",
            "EDGE_CREATION",
            "EDGE_DELETION",
            "NODE_DEEPENING",
            "NODE_SHALLOWING",
            "NODE_MOVE",
            "NODE_DIRECT_MERGE",
            "REMOVE_MAPPING",
            "MAPPING_PREDICATE_CHANGE",
            "COMPLEX_CHANGE",
            "OTHER",
        ]:
            change = _change(
                change_type=change_type,
                old_value="GO:0016192",
                new_value="a new value",
                subject={"id": "GO:0006888", "label": "t"},
                predicate="rdfs:subClassOf",
            )
            dsl = kgcl_dsl(change)
            if dsl is not None:
                assert parse_kgcl(dsl) is not None, f"{change_type} rendered unparseable: {dsl}"


class TestDslAgreement:
    """The stated DSL is checked against the structured slots via the parser."""

    def test_unparseable_dsl_is_flagged(self):
        data = {"proposed_ontology_changes": [_change(change_dsl="obsoletify GO:0099022")]}
        assert "dsl_unparseable" in _codes(data)

    def test_a_merge_dsl_is_unparseable_and_flagged(self):
        data = {
            "proposed_ontology_changes": [
                _change(
                    change_type="NODE_DIRECT_MERGE",
                    change_dsl="merge GO:0099022 into GO:7770062",
                )
            ]
        }
        assert "dsl_unparseable" in _codes(data)

    def test_dsl_about_a_different_term_is_flagged(self):
        data = {
            "proposed_ontology_changes": [
                _change(change_dsl="obsolete GO:0000001 with replacement GO:7770062")
            ]
        }
        assert "dsl_disagrees" in _codes(data)

    def test_dsl_with_a_different_replacement_is_flagged(self):
        data = {
            "proposed_ontology_changes": [
                _change(change_dsl="obsolete GO:0099022 with replacement GO:0000002")
            ]
        }
        assert "dsl_disagrees" in _codes(data)

    def test_dsl_of_the_wrong_kind_is_flagged(self):
        """A bare `obsolete` under the with-replacement change type is the wrong class."""
        data = {"proposed_ontology_changes": [_change(change_dsl="obsolete GO:0099022")]}
        assert "dsl_wrong_kind" in _codes(data)

    def test_an_agreeing_dsl_passes(self):
        data = {
            "proposed_ontology_changes": [
                _change(change_dsl="obsolete GO:0099022 with replacement GO:7770062")
            ]
        }
        assert _codes(data) == []

    def test_a_nondirect_obsoletion_dsl_passes_without_its_alternatives(self):
        data = {
            "proposed_ontology_changes": [
                _change(
                    change_type="NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT",
                    has_direct_replacement=None,
                    has_nondirect_replacement=[dict(GO_B)],
                    change_dsl="obsolete GO:0099022",
                )
            ]
        }
        assert _codes(data) == []
