"""Tests for building rule review stubs from ARBA rule JSON."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ai_gene_review.datamodel.gene_review_model import EmbeddedRule
from ai_gene_review.etl.rule_review_init import (
    _create_review_stub,
    extract_condition_sets,
    extract_rule_annotations,
)

INPUT_DIR = Path(__file__).parent / "input" / "arba"


def load_rule(rule_id: str) -> dict:
    """Load a raw ARBA rule JSON fixture (as returned by rest.uniprot.org/arba)."""
    return json.loads((INPUT_DIR / f"{rule_id}.json").read_text())


@pytest.mark.parametrize("rule_id", ["ARBA00067001", "ARBA00052213"])
def test_extract_condition_sets_reads_main_rule(rule_id: str) -> None:
    condition_sets = extract_condition_sets(load_rule(rule_id))
    assert len(condition_sets) == 1
    conditions = condition_sets[0]["conditions"]
    assert [(c["condition_type"], c["value"]) for c in conditions] == [
        ("FUNFAM", "3.40.50.720:FF:000411"),
        ("TAXON", "Archaea"),
    ]
    assert all(c["negated"] is False for c in conditions)


def test_extract_condition_sets_keeps_negation() -> None:
    rule = {
        "mainRule": {
            "conditionSets": [
                {
                    "conditions": [
                        {
                            "type": "InterPro id",
                            "conditionValues": [{"value": "IPR000001"}],
                            "isNegative": True,
                        }
                    ]
                }
            ]
        }
    }
    [condition] = extract_condition_sets(rule)[0]["conditions"]
    assert condition["condition_type"] == "INTERPRO"
    assert condition["negated"] is True


def test_extract_name_annotation_with_ec_only() -> None:
    annotations = extract_rule_annotations(load_rule("ARBA00067001"))
    assert annotations["protein_name_annotations"] == [
        {"name_type": "RECOMMENDED", "ec_numbers": ["1.2.1.75"]}
    ]
    assert annotations["catalytic_activity_annotations"] == []
    assert annotations["go_annotations"] == []


def test_extract_catalytic_activity_annotation() -> None:
    annotations = extract_rule_annotations(load_rule("ARBA00052213"))
    assert annotations["catalytic_activity_annotations"] == [
        {
            "reaction_name": "3-oxopropanoate + NADP(+) + CoA = malonyl-CoA + NADPH + H(+)",
            "rhea_id": "RHEA:26446",
            "ec_number": "1.2.1.75",
        }
    ]
    assert annotations["protein_name_annotations"] == []


def test_extract_go_and_full_name_annotations() -> None:
    rule = {
        "mainRule": {
            "conditionSets": [],
            "annotations": [
                {
                    "annotationType": "ANNOTATION",
                    "dbReference": {"database": "GO", "id": "GO:0004073", "label": "x"},
                },
                {
                    "annotationType": "ANNOTATION",
                    "proteinDescription": {
                        "alternativeNames": [
                            {
                                "fullName": {"value": "ASA dehydrogenase"},
                                "shortNames": [{"value": "ASADH"}],
                            }
                        ]
                    },
                },
            ],
        }
    }
    annotations = extract_rule_annotations(rule)
    assert annotations["go_annotations"] == [{"go_id": "GO:0004073", "go_label": "x"}]
    assert annotations["protein_name_annotations"] == [
        {
            "name_type": "ALTERNATIVE",
            "full_name": "ASA dehydrogenase",
            "short_names": ["ASADH"],
        }
    ]


@pytest.mark.parametrize("rule_id", ["ARBA00067001", "ARBA00052213"])
def test_review_stub_rule_block_is_schema_valid(rule_id: str) -> None:
    """The embedded rule is complete and valid; the review fields stay TODO placeholders."""
    stub = _create_review_stub(rule_id, "ARBA", load_rule(rule_id))
    # entries is added later by sync-rule-review-single
    rule = EmbeddedRule(**stub["rule"], entries=[])
    assert rule.condition_sets[0].conditions[0].value == "3.40.50.720:FF:000411"
    assert rule.unreviewed_protein_count == 38
    assert rule.created_date == "2025-03-21"
    consequents = (rule.protein_name_annotations or []) + (
        rule.catalytic_activity_annotations or []
    )
    assert len(consequents) == 1


def test_arba_client_round_trip_keeps_protein_description() -> None:
    """Name rules must survive ARBARule parsing and caching."""
    from ai_gene_review.etl.arba import ARBARule

    raw = load_rule("ARBA00067001")
    round_tripped = ARBARule.from_json(raw).to_json()
    annotations = extract_rule_annotations(round_tripped)
    assert annotations["protein_name_annotations"] == [
        {"name_type": "RECOMMENDED", "ec_numbers": ["1.2.1.75"]}
    ]


def test_rendered_review_shows_name_rule_consequents_and_assessments(tmp_path: Path) -> None:
    """A rule with no GO consequent still renders its name and assessment sections."""
    import yaml

    from ai_gene_review.etl.rule_analysis import render_rule_review_html

    rule_id = "ARBA00067001"
    stub = _create_review_stub(rule_id, "ARBA", load_rule(rule_id))
    stub["rule"]["entries"] = []
    stub["annotation_assessments"] = [
        {
            "annotation_kind": "EC_NUMBER",
            "value": "EC:1.2.1.75",
            "assessment": "PARTIALLY_CORRECT",
            "matched_protein_count": 38,
            "incorrect_protein_count": 17,
            "incorrect_examples": ["A4YHF3"],
            "discriminating_features": ["CDD:cd23940"],
        }
    ]
    rule_dir = tmp_path / rule_id
    rule_dir.mkdir()
    (rule_dir / f"{rule_id}-review.yaml").write_text(yaml.safe_dump(stub))
    html = render_rule_review_html(rule_id, tmp_path).read_text()
    assert "Protein Name Annotations" in html
    assert "1.2.1.75" in html
    assert "Annotation Assessments" in html
    assert "PARTIALLY_CORRECT" in html
    assert "A4YHF3" in html
    assert "CDD:cd23940" in html
