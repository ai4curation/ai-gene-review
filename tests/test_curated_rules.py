"""Tests for curated annotation rules (rules/curated/)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from ai_gene_review.curated_rules import (
    CURATED_RULES_DIR,
    ProteinFeatures,
    check_rule,
    rule_fires,
    to_uniprot_query,
)
from ai_gene_review.datamodel.gene_review_model import CuratedRule

REPO_ROOT = Path(__file__).resolve().parents[1]

EUKARYOTE = ProteinFeatures(
    signatures={"INTERPRO": {"IPR005024"}},
    taxon_ids={"NCBITaxon:131567", "NCBITaxon:2759"},
)
ARCHAEON = ProteinFeatures(
    signatures={"INTERPRO": {"IPR005024", "IPR053492"}},
    taxon_ids={"NCBITaxon:131567", "NCBITaxon:2157"},
)


def make_rule(*condition_sets: list[dict]) -> dict:
    """Build a minimal rule dict from lists of conditions."""
    return {
        "id": "CR-9999",
        "title": "test",
        "status": "DRAFT",
        "condition_sets": [
            {"number": i, "conditions": conds} for i, conds in enumerate(condition_sets, 1)
        ],
    }


SNF7_EUK = make_rule(
    [
        {"condition_type": "INTERPRO", "value": "IPR005024"},
        {"condition_type": "TAXON", "value": "NCBITaxon:2759"},
    ]
)


def test_taxon_condition_gates_the_domain() -> None:
    assert rule_fires(SNF7_EUK, EUKARYOTE)
    assert not rule_fires(SNF7_EUK, ARCHAEON)


def test_condition_sets_are_ored() -> None:
    rule = make_rule(
        [{"condition_type": "INTERPRO", "value": "IPR053654"}],
        [{"condition_type": "INTERPRO", "value": "IPR053492"}],
    )
    assert rule_fires(rule, ARCHAEON)
    assert not rule_fires(rule, EUKARYOTE)


def test_negated_condition() -> None:
    rule = make_rule(
        [
            {"condition_type": "INTERPRO", "value": "IPR005024"},
            {"condition_type": "TAXON", "value": "NCBITaxon:2157", "negated": True},
        ]
    )
    assert rule_fires(rule, EUKARYOTE)
    assert not rule_fires(rule, ARCHAEON)


MODULE_RULE = make_rule(
    [
        {"condition_type": "INTERPRO", "value": "IPR005024"},
        {"condition_type": "MODULE_CONTEXT", "value": "MODULE:ubiquitin_transfer_relay"},
    ]
)


@pytest.mark.parametrize(
    ("context", "fires"),
    [
        ({"MODULE:ubiquitin_transfer_relay": False}, False),
        ({"MODULE:ubiquitin_transfer_relay": True}, True),
        ({"MODULE:ubiquitin_transfer_relay": None}, True),
        ({}, True),
        (None, True),
    ],
)
def test_module_context_is_exclusion_only(context: dict | None, fires: bool) -> None:
    """Only a module evaluated as unsatisfiable blocks the rule."""
    assert rule_fires(MODULE_RULE, EUKARYOTE, context) is fires


def test_uniprot_query_single_set() -> None:
    assert to_uniprot_query(SNF7_EUK) == "(xref:interpro-IPR005024 AND taxonomy_id:2759)"


def test_uniprot_query_or_negation_funfam_and_module_omitted() -> None:
    rule = make_rule(
        [
            {"condition_type": "FUNFAM", "value": "3.40.50.720:FF:000411"},
            {"condition_type": "CDD", "value": "cd23940"},
            {"condition_type": "TAXON", "value": "NCBITaxon:2157"},
        ],
        [
            {"condition_type": "NCBIFAM", "value": "NF041005"},
            {"condition_type": "PFAM", "value": "PF03357", "negated": True},
            {"condition_type": "MODULE_CONTEXT", "value": "MODULE:ubiquitin_transfer_relay"},
        ],
    )
    assert to_uniprot_query(rule) == (
        '("3.40.50.720:FF:000411" AND xref:cdd-cd23940 AND taxonomy_id:2157)'
        " OR (xref:ncbifam-NF041005 AND NOT xref:pfam-PF03357)"
    )


@pytest.mark.parametrize(
    ("conditions", "expected"),
    [
        (
            [
                {"condition_type": "INTERPRO", "value": "IPR005024"},
                {"condition_type": "MODULE_CONTEXT", "value": "MODULE:ubiquitin_transfer_relay", "negated": True},
            ],
            "cannot be negated",
        ),
        (
            [{"condition_type": "TAXON", "value": "NCBITaxon:2759"}],
            "no sequence-feature condition",
        ),
        (
            [
                {"condition_type": "INTERPRO", "value": "IPR005024"},
                {"condition_type": "MODULE_CONTEXT", "value": "MODULE:no_such_module"},
            ],
            "unknown module",
        ),
        (
            [{"condition_type": "TAXON", "value": "2759"}, {"condition_type": "INTERPRO", "value": "IPR005024"}],
            "NCBITaxon",
        ),
    ],
)
def test_check_rule_reports_problems(conditions: list[dict], expected: str) -> None:
    errors = check_rule(make_rule(conditions), modules_dir=REPO_ROOT / "modules")
    assert any(expected in e for e in errors), errors


def test_check_rule_accepts_known_module() -> None:
    assert check_rule(MODULE_RULE, modules_dir=REPO_ROOT / "modules") == []


RULE_FILES = sorted((REPO_ROOT / CURATED_RULES_DIR).glob("CR-*.yaml"))


def test_curated_rules_exist() -> None:
    assert RULE_FILES


@pytest.mark.parametrize("path", RULE_FILES, ids=lambda p: p.stem)
def test_curated_rule_files_are_valid(path: Path) -> None:
    data = yaml.safe_load(path.read_text())
    assert data["id"] == path.stem
    CuratedRule(**data)
    assert check_rule(data, modules_dir=REPO_ROOT / "modules") == []
