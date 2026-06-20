"""Tests for the module (ModuleReview) term-label validator.

The unit tests exercise the pure logic (term discovery, prefix routing, label
comparison) using an in-memory resolver function so they run offline. An
integration test exercises the real oaklib-backed resolver against the
committed nicotine module.
"""

from pathlib import Path

import pytest

from ai_gene_review.validation.module_validator import (
    compare_label,
    iter_terms,
    validate_terms,
    validate_module_file,
    load_oak_adapter_map,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = PROJECT_ROOT / "modules"


# --------------------------------------------------------------------------- #
# iter_terms
# --------------------------------------------------------------------------- #


def test_iter_terms_finds_nested_terms():
    doc = {
        "module": {
            "concepts": [{"preferred_term": "x", "term": {"id": "GO:1", "label": "a"}}],
            "parts": [
                {
                    "node": {
                        "annotons": [
                            {
                                "function": {
                                    "term": {"id": "GO:2", "label": "b"},
                                    "substrates": [
                                        {"term": {"id": "CHEBI:1", "label": "c"}}
                                    ],
                                }
                            }
                        ]
                    }
                }
            ],
        }
    }
    found = set(iter_terms(doc))
    assert found == {("GO:1", "a"), ("GO:2", "b"), ("CHEBI:1", "c")}


def test_iter_terms_requires_string_id_and_label():
    # A term under `term:` whose id/label are not both strings is ignored.
    doc = {"term": {"id": 5, "label": "n"}, "other": {"id": "GO:1"}}
    assert list(iter_terms(doc)) == []


def test_iter_terms_ignores_node_and_annoton_ids():
    # Module nodes/annotons carry id+label that are NOT ontology terms; only
    # values under a `term:` key are real terms.
    doc = {
        "id": "odc_step",
        "label": "a reaction node",
        "annotons": [
            {
                "id": "odc_activity",
                "label": "an annoton",
                "function": {"term": {"id": "GO:0004586", "label": "ODC activity"}},
            }
        ],
    }
    assert list(iter_terms(doc)) == [("GO:0004586", "ODC activity")]


# --------------------------------------------------------------------------- #
# compare_label
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "provided,primary,aliases,expect_ok",
    [
        ("root", "root", set(), True),  # exact
        ("Root", "root", set(), True),  # case-insensitive
        ("vacuole", "vacuolar membrane", {"vacuole"}, True),  # alias match
        ("WRONG", "root", {"radix"}, False),  # genuine mismatch
    ],
)
def test_compare_label(provided, primary, aliases, expect_ok):
    err = compare_label("X:1", provided, primary, aliases)
    assert (err is None) == expect_ok


# --------------------------------------------------------------------------- #
# validate_terms (pure, injected resolver)
# --------------------------------------------------------------------------- #


def _resolver_factory(known):
    """Build a real resolver function backed by an in-memory dict.

    known: {curie: (primary_label, aliases) or None-if-not-found}
    Returns (status, primary, aliases) where status is 'ok'|'not_found'.
    """

    def resolve(curie):
        entry = known.get(curie, "missing")
        if entry == "missing":
            return ("not_found", None, set())
        return ("ok", entry[0], entry[1])

    return resolve


def test_validate_terms_passes_on_correct_labels():
    terms = [("GO:0005774", "vacuolar membrane"), ("PO:0009005", "root")]
    resolver = _resolver_factory(
        {
            "GO:0005774": ("vacuolar membrane", set()),
            "PO:0009005": ("root", set()),
        }
    )
    adapters = {"GO": "real", "PO": "real"}
    errors, warnings = validate_terms(terms, adapters, resolver)
    assert errors == []


def test_validate_terms_flags_wrong_label():
    terms = [("GO:0005774", "WRONG LABEL")]
    resolver = _resolver_factory({"GO:0005774": ("vacuolar membrane", set())})
    errors, warnings = validate_terms(terms, {"GO": "real"}, resolver)
    assert len(errors) == 1
    assert "GO:0005774" in errors[0]


def test_validate_terms_flags_unresolvable_id():
    terms = [("GO:9999999", "nonexistent")]
    resolver = _resolver_factory({})  # nothing known -> not_found
    errors, warnings = validate_terms(terms, {"GO": "real"}, resolver)
    assert len(errors) == 1
    assert "not found" in errors[0].lower()


def test_validate_terms_treats_unavailable_as_warning():
    terms = [("GO:0005774", "vacuolar membrane")]

    def resolver(curie):
        return ("unavailable", None, set())

    errors, warnings = validate_terms(terms, {"GO": "real"}, resolver)
    assert errors == []
    assert len(warnings) == 1
    assert "unavailable" in warnings[0].lower()


def test_validate_terms_skips_null_prefix_silently():
    terms = [("UniProtKB:P12345", "some protein")]
    resolver = _resolver_factory({})
    # UniProtKB mapped to None (null) -> skipped, no error, no warning
    errors, warnings = validate_terms(terms, {"UniProtKB": None}, resolver)
    assert errors == []
    assert warnings == []


def test_validate_terms_warns_on_unconfigured_prefix():
    terms = [("FOO:1", "bar")]
    resolver = _resolver_factory({})
    errors, warnings = validate_terms(terms, {}, resolver)
    assert errors == []
    assert any("FOO" in w for w in warnings)


# --------------------------------------------------------------------------- #
# config loading
# --------------------------------------------------------------------------- #


def test_load_oak_adapter_map():
    cfg = load_oak_adapter_map(PROJECT_ROOT / "conf" / "oak_config.yaml")
    assert cfg["GO"] == "sqlite:obo:go"
    assert cfg["PMID"] is None
    # PO and SBO must be configured so module terms get validated.
    assert "PO" in cfg
    assert "SBO" in cfg


# --------------------------------------------------------------------------- #
# Integration: real oaklib against the committed modules
# --------------------------------------------------------------------------- #


@pytest.mark.integration
def test_nicotine_module_terms_resolve_for_real():
    path = MODULES_DIR / "nicotine_biosynthesis.yaml"
    result = validate_module_file(path)
    assert result.errors == [], "\n".join(result.errors)
