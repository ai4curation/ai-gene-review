"""Tests for the module (ModuleReview) term-label validator.

The unit tests exercise the pure logic (term discovery, prefix routing, label
comparison) using an in-memory resolver function so they run offline. An
integration test exercises the real oaklib-backed resolver against the
committed nicotine module.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.module_validator import (
    PaintAnnotationRow,
    compare_label,
    iter_ancestral_node_uses,
    iter_taxon_descriptors,
    iter_terms,
    iter_typed_go_terms,
    validate_paint_ptns,
    validate_go_branches,
    validate_taxon_context,
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


def test_iter_terms_finds_direct_family_terms():
    doc = {
        "family": {
            "family_terms": [
                {"id": "PANTHER:PTHR1", "label": "family 1"},
                {"id": "PANTHER:PTHR2", "label": "family 2"},
            ]
        }
    }
    assert list(iter_terms(doc)) == [
        ("PANTHER:PTHR1", "family 1"),
        ("PANTHER:PTHR2", "family 2"),
    ]


def test_iter_typed_go_terms_finds_only_known_branch_slots():
    doc = {
        "module": {
            "concepts": [
                {"preferred_term": "signaling", "term": {"id": "GO:1", "label": "x"}}
            ],
            "annotons": [
                {
                    "function": {"term": {"id": "GO:2", "label": "activity"}},
                    "processes": [
                        {"term": {"id": "GO:3", "label": "process"}},
                    ],
                    "locations": [
                        {"term": {"id": "GO:4", "label": "location"}},
                    ],
                }
            ],
        }
    }
    found = [(t.path, t.curie, t.constraint.root_id) for t in iter_typed_go_terms(doc)]
    assert found == [
        ("$.module.annotons[0].function.term", "GO:2", "GO:0003674"),
        ("$.module.annotons[0].processes[0].term", "GO:3", "GO:0008150"),
        ("$.module.annotons[0].locations[0].term", "GO:4", "GO:0110165"),
    ]


# --------------------------------------------------------------------------- #
# Taxon context validation
# --------------------------------------------------------------------------- #


def test_iter_taxon_descriptors_finds_taxa_and_taxon_slots():
    doc = {
        "module": {
            "context": {"taxa": [{"preferred_term": "Mammalia"}]},
            "annotons": [{"participant": {"taxon": {"preferred_term": "Homo sapiens"}}}],
        }
    }
    found = [(path, descriptor["preferred_term"]) for path, descriptor in iter_taxon_descriptors(doc)]
    assert found == [
        ("$.module.context.taxa[0]", "Mammalia"),
        ("$.module.annotons[0].participant.taxon", "Homo sapiens"),
    ]


def test_validate_taxon_context_rejects_experimental_system_label():
    doc = {
        "module": {
            "context": {
                "taxa": [
                    {
                        "preferred_term": "mammals (defined in human cell lines)",
                    }
                ]
            }
        }
    }
    errors = validate_taxon_context(doc)
    assert len(errors) == 1
    assert "taxon context must name an in-vivo taxon or clade" in errors[0]


def test_validate_taxon_context_allows_cell_line_evidence_statement():
    doc = {
        "module": {
            "context": {
                "taxa": [
                    {
                        "preferred_term": "Mammalia",
                        "term": {"id": "NCBITaxon:40674", "label": "Mammalia"},
                    }
                ]
            }
        },
        "evidence": [
            {
                "source_id": "PMID:1",
                "statement": "Genome-wide CRISPR screens in human cell-line systems defined the core mechanism.",
            }
        ],
    }
    assert validate_taxon_context(doc) == []


# --------------------------------------------------------------------------- #
# PANTHER/PAINT ancestral node validation
# --------------------------------------------------------------------------- #


def _paint_row(
    *,
    ptn="PANTHER:PTN000000001",
    family="PTHR1",
    go_id="GO:0003674",
    aspect="F",
    evidence="IBD",
    negated=False,
    seeds="UniProtKB:P1",
):
    return PaintAnnotationRow(
        family=family,
        node_curie=ptn,
        go_id=go_id,
        aspect=aspect,
        evidence=evidence,
        negated=negated,
        seeds=seeds,
        source_path=Path("PTHR1-paint.tsv"),
    )


def test_iter_ancestral_node_uses_collects_family_context():
    doc = {
        "annotons": [
            {
                "function": {
                    "term": {"id": "GO:0003674", "label": "molecular_function"}
                },
                "locations": [
                    {"term": {"id": "GO:0005829", "label": "cytosol"}},
                ],
                "participant": {
                    "selector_type": "FAMILY",
                    "family": {
                        "term": {"id": "PANTHER:PTHR1", "label": "family"},
                        "family_terms": [
                            {"id": "PANTHER:PTHR2", "label": "related family"}
                        ],
                        "representative_members": [
                            {
                                "term": {
                                    "id": "UniProtKB:P1",
                                    "label": "representative",
                                }
                            }
                        ],
                        "ancestral_nodes": [
                            {
                                "term": {
                                    "id": "PANTHER:PTN000000001",
                                    "label": "node",
                                },
                                "evidence": [{"source_id": "GO_REF:0000033"}],
                            }
                        ],
                    },
                },
            }
        ]
    }

    uses = list(iter_ancestral_node_uses(doc))

    assert len(uses) == 1
    use = uses[0]
    assert use.path == "$.annotons[0].participant.family.ancestral_nodes[0].term"
    assert use.ptn_curie == "PANTHER:PTN000000001"
    assert use.family_curie == "PANTHER:PTHR1"
    assert use.family_term_curies == frozenset({"PANTHER:PTHR1", "PANTHER:PTHR2"})
    assert use.representative_uniprot_accessions == frozenset({"P1"})
    assert use.has_go_ref_0000033 is True
    assert {(a.aspect, a.curie) for a in use.asserted_go_terms} == {
        ("F", "GO:0003674"),
        ("C", "GO:0005829"),
    }


def test_validate_paint_ptns_accepts_exact_positive_ibd():
    doc = {
        "function": {"term": {"id": "GO:0003674", "label": "molecular_function"}},
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "family"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "representative"}}
            ],
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    uses = list(iter_ancestral_node_uses(doc))
    index = {"PANTHER:PTN000000001": [_paint_row()]}

    errors, warnings = validate_paint_ptns(uses, index)

    assert errors == []
    assert warnings == []


def test_validate_paint_ptns_requires_well_formed_ptn():
    doc = {"ancestral_nodes": [{"term": {"id": "PANTHER:PTHR1", "label": "bad"}}]}

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), {})

    assert warnings == []
    assert len(errors) == 1
    assert "PANTHER:PTN<digits>" in errors[0]


def test_validate_paint_ptns_requires_positive_ibd():
    doc = {
        "ancestral_nodes": [
            {
                "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                "evidence": [{"source_id": "GO_REF:0000033"}],
            }
        ]
    }
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(evidence="IRD", negated=True, go_id="GO:0008150", aspect="P")
        ]
    }

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert warnings == []
    assert len(errors) == 1
    assert "no positive non-negated IBD" in errors[0]


def test_validate_paint_ptns_warns_on_no_exact_go_overlap():
    doc = {
        "function": {"term": {"id": "GO:0008150", "label": "biological_process"}},
        "family": {
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {"PANTHER:PTN000000001": [_paint_row()]}

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []
    assert len(warnings) == 1
    assert "no exact GO overlap" in warnings[0]


def test_validate_paint_ptns_accepts_any_declared_family_term():
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "family 1"},
            "family_terms": [
                {"id": "PANTHER:PTHR1", "label": "family 1"},
                {"id": "PANTHER:PTHR2", "label": "family 2"},
            ],
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {"PANTHER:PTN000000001": [_paint_row(family="PTHR2")]}

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []
    assert warnings == []


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
# validate_go_branches (pure, injected resolver)
# --------------------------------------------------------------------------- #


def test_validate_go_branches_flags_wrong_known_slot_branch():
    doc = {"function": {"term": {"id": "GO:0008150", "label": "biological_process"}}}

    def branch_resolver(curie, root):
        return "not_in_branch"

    errors, warnings = validate_go_branches(
        list(iter_typed_go_terms(doc)), branch_resolver
    )
    assert warnings == []
    assert len(errors) == 1
    assert "molecular function" in errors[0]
    assert "GO:0008150" in errors[0]


def test_validate_go_branches_ignores_generic_concepts():
    doc = {"concepts": [{"term": {"id": "GO:0008150", "label": "biological_process"}}]}

    def branch_resolver(curie, root):
        raise AssertionError("generic concepts must not be branch-checked")

    errors, warnings = validate_go_branches(
        list(iter_typed_go_terms(doc)), branch_resolver
    )
    assert errors == []
    assert warnings == []


def test_validate_go_branches_requires_go_curie_in_known_slot():
    doc = {"required_function": {"term": {"id": "CHEBI:1", "label": "chemical"}}}

    def branch_resolver(curie, root):
        raise AssertionError("non-GO terms should fail before branch lookup")

    errors, warnings = validate_go_branches(
        list(iter_typed_go_terms(doc)), branch_resolver
    )
    assert warnings == []
    assert len(errors) == 1
    assert "expected molecular function GO term" in errors[0]


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


# --------------------------------------------------------------------------- #
# Conformance is enforced through validate_module_file (offline, injected resolver)
# --------------------------------------------------------------------------- #


def _skip_label_resolver(curie):
    """Resolver that treats labels as unvalidated, isolating the conformance check.

    Label checking degrades to advisory warnings, so any remaining *errors* come
    solely from conformance.
    """
    return ("unavailable", None, set())


def test_validate_module_file_passes_conformant_module():
    # erk_cascade's erk_relay bundle conforms EXACTly to mapk_relay, so with
    # label checking skipped the file should validate with no errors.
    result = validate_module_file(
        MODULES_DIR / "erk_cascade.yaml", resolver=_skip_label_resolver
    )
    assert result.errors == [], "\n".join(result.errors)


def test_validate_module_file_flags_bad_conformance(tmp_path):
    # A node conforming to a non-existent template must produce a hard error.
    doc = {
        "id": "MODULE:bad",
        "title": "bad",
        "module": {
            "id": "bad",
            "label": "bad",
            "parts": [
                {
                    "node": {
                        "id": "relay",
                        "label": "relay",
                        "conforms_to": [{"template": "no_such_motif"}],
                    }
                }
            ],
        },
    }
    path = tmp_path / "bad_module.yaml"
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    result = validate_module_file(path, resolver=_skip_label_resolver)
    assert not result.is_valid
    assert any(
        "conformance" in e.lower() and "template" in e.lower() for e in result.errors
    )
