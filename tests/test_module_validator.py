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
    iter_cited_ptn_sources,
    count_ungrounded_families,
    iter_all_representative_accessions,
    iter_family_member_uses,
    iter_taxon_descriptors,
    load_goa_attested_ptns,
    iter_terms,
    iter_typed_go_terms,
    validate_cited_ptn_sources,
    validate_family_members,
    validate_paint_ptns,
    validate_go_branches,
    validate_taxon_context,
    validate_terms,
    validate_module_file,
    load_oak_adapter_map,
    load_term_label_aliases,
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
    assert "no ancestry relation" in warnings[0]


def test_validate_paint_ptns_accepts_a_more_specific_node_term():
    """A node annotated to a child term does support the parent claim."""
    doc = {
        "function": {"term": {"id": "GO:0003674", "label": "molecular_function"}},
        "family": {
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {"PANTHER:PTN000000001": [_paint_row(go_id="GO:0004672", aspect="F")]}
    ancestors = {"GO:0004672": {"GO:0004672", "GO:0003674"}}.get

    errors, warnings = validate_paint_ptns(
        list(iter_ancestral_node_uses(doc)), index,
        lambda t: ancestors(t) or {t},
    )

    assert (errors, warnings) == ([], [])


def test_validate_paint_ptns_flags_a_node_silent_in_the_asserted_aspect():
    """The common shape: node attests the pathway role, not the claimed MF."""
    doc = {
        "function": {"term": {"id": "GO:0004714", "label": "kinase"}},
        "family": {
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "node"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {"PANTHER:PTN000000001": [_paint_row(go_id="GO:0007173", aspect="P")]}

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []
    assert len(warnings) == 1
    assert "attests nothing in GO aspect F" in warnings[0]
    assert "needs separate support" in warnings[0]


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


def test_validate_terms_accepts_reviewed_label_alias():
    terms = [("GO:0005774", "new live label")]
    resolver = _resolver_factory({"GO:0005774": ("stale snapshot label", set())})
    aliases = {"GO:0005774": {"new live label"}}
    errors, warnings = validate_terms(
        terms, {"GO": "real"}, resolver, label_aliases=aliases
    )
    assert errors == []
    assert warnings == []


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


def test_load_term_label_aliases():
    aliases = load_term_label_aliases(PROJECT_ROOT / "conf" / "oak_config.yaml")
    assert aliases["GO:0008883"] == {
        "glutamyl-tRNA reductase (NADP+) activity"
    }


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


# --------------------------------------------------------------------------- #
# supporting_text snippet validation
# --------------------------------------------------------------------------- #

from ai_gene_review.validation.module_validator import (  # noqa: E402
    iter_evidence_snippets,
    validate_supporting_text,
)

PUBLICATIONS_DIR = PROJECT_ROOT / "publications"


def test_iter_evidence_snippets_only_literature_with_text():
    """Only PMID/DOI EvidenceItems carrying a non-empty quote are yielded."""
    doc = {
        "module": {
            "annotons": [
                {
                    "evidence": [
                        {"source_id": "PMID:123", "supporting_text": "a real quote"},
                        {"source_id": "GO:0001", "supporting_text": "grounding, skip"},
                        {"source_id": "PMID:999", "statement": "no quote here"},
                        {"source_id": "DOI:10.1/x", "supporting_text": "doi quote"},
                    ]
                }
            ]
        }
    }
    got = sorted(iter_evidence_snippets(doc))
    assert got == [("DOI:10.1/x", "doi quote"), ("PMID:123", "a real quote")]


def test_validate_supporting_text_no_literature_is_noop():
    doc = {"module": {"evidence": [{"source_id": "GO:1", "supporting_text": "x"}]}}
    errors, warnings = validate_supporting_text(doc)
    assert errors == [] and warnings == []


def test_validate_supporting_text_fetch_exception_is_warning(monkeypatch):
    class RaisingValidator:
        def validate(self, supporting_text, source_id):
            raise RuntimeError("transient fetch failure")

    monkeypatch.setattr(
        "ai_gene_review.validation.module_validator._build_supporting_text_validator",
        lambda publications_dir: (RaisingValidator(), None),
    )
    doc = {
        "module": {
            "evidence": [
                {"source_id": "PMID:123", "supporting_text": "a real quote"}
            ]
        }
    }
    errors, warnings = validate_supporting_text(doc)
    assert errors == []
    assert any("transient fetch failure" in warning for warning in warnings)


@pytest.mark.integration
def test_validate_supporting_text_verbatim_pass():
    """A quote that is a verbatim substring of the cached abstract passes."""
    pytest.importorskip("linkml_reference_validator")
    if not (PUBLICATIONS_DIR / "PMID_10049358.md").exists():
        pytest.skip("cached publication PMID_10049358 not present")
    doc = {
        "module": {
            "evidence": [
                {
                    "source_id": "PMID:10049358",
                    "supporting_text": "Bmp4 homozygous null embryos contain no PGCs",
                }
            ]
        }
    }
    errors, warnings = validate_supporting_text(doc, publications_dir=PUBLICATIONS_DIR)
    assert errors == [], errors


@pytest.mark.integration
def test_validate_supporting_text_flags_fabricated_quote():
    """A quote absent from the cached publication is a blocking error."""
    pytest.importorskip("linkml_reference_validator")
    if not (PUBLICATIONS_DIR / "PMID_10049358.md").exists():
        pytest.skip("cached publication PMID_10049358 not present")
    doc = {
        "module": {
            "evidence": [
                {
                    "source_id": "PMID:10049358",
                    "supporting_text": "this fabricated sentence appears in no abstract",
                }
            ]
        }
    }
    errors, _ = validate_supporting_text(doc, publications_dir=PUBLICATIONS_DIR)
    assert any("mismatch" in e.lower() for e in errors), errors


# --------------------------------------------------------------------------- #
# reference title validation
# --------------------------------------------------------------------------- #

from ai_gene_review.validation.module_validator import (  # noqa: E402
    iter_reference_titles,
    validate_reference_titles,
)


def test_iter_reference_titles_only_literature():
    """Only PMID/DOI ids/source_ids with a title are yielded; local ids ignored."""
    doc = {
        "id": "MODULE:x",
        "title": "My module",  # MODULE: prefix -> ignored
        "references": [{"id": "PMID:5", "title": "Real Paper"}],
        "module": {
            "id": "node1",  # local id -> ignored
            "label": "n",
            "evidence": [
                {"source_id": "DOI:10.1/y", "title": "Doi Paper"},
                {"source_id": "GO:0001", "title": "grounding"},  # ignored
            ],
        },
    }
    assert sorted(iter_reference_titles(doc)) == [
        ("DOI:10.1/y", "Doi Paper"),
        ("PMID:5", "Real Paper"),
    ]


def test_validate_reference_titles_no_literature_is_noop():
    doc = {"references": [{"id": "GO:1", "title": "x"}]}
    assert validate_reference_titles(doc) == ([], [])


def test_validate_reference_titles_fetch_exception_is_warning(monkeypatch):
    class RaisingValidator:
        def validate_title(self, ref_id, title):
            raise RuntimeError("transient fetch failure")

    monkeypatch.setattr(
        "ai_gene_review.validation.module_validator._build_supporting_text_validator",
        lambda publications_dir: (RaisingValidator(), None),
    )
    errors, warnings = validate_reference_titles(
        {"references": [{"id": "PMID:123", "title": "A real title"}]}
    )
    assert errors == []
    assert any("transient fetch failure" in warning for warning in warnings)


@pytest.mark.integration
def test_validate_reference_titles_correct_passes():
    pytest.importorskip("linkml_reference_validator")
    if not (PUBLICATIONS_DIR / "PMID_10049358.md").exists():
        pytest.skip("cached publication PMID_10049358 not present")
    doc = {
        "references": [
            {
                "id": "PMID:10049358",
                "title": "Bmp4 is required for the generation of primordial germ cells in the mouse embryo.",
            }
        ]
    }
    errors, _ = validate_reference_titles(doc, publications_dir=PUBLICATIONS_DIR)
    assert errors == [], errors


@pytest.mark.integration
def test_validate_reference_titles_wrong_title_errors():
    pytest.importorskip("linkml_reference_validator")
    if not (PUBLICATIONS_DIR / "PMID_10049358.md").exists():
        pytest.skip("cached publication PMID_10049358 not present")
    doc = {
        "references": [
            {"id": "PMID:10049358", "title": "An unrelated wrong title"}
        ]
    }
    errors, _ = validate_reference_titles(doc, publications_dir=PUBLICATIONS_DIR)
    assert any("title mismatch" in e.lower() for e in errors), errors


# --------------------------------------------------------------------------- #
# PANTHER family/member consistency and evidence-cited PTNs
# --------------------------------------------------------------------------- #


def _family_doc(family_id: str, accession: str) -> dict:
    return {
        "family": {
            "term": {"id": family_id, "label": "some family"},
            "representative_members": [
                {"term": {"id": f"UniProtKB:{accession}", "label": "rep"}}
            ],
        }
    }


def test_iter_family_member_uses_requires_both_family_and_member():
    with_member = _family_doc("PANTHER:PTHR13337", "O14521")
    assert len(list(iter_family_member_uses(with_member))) == 1

    no_member = {"family": {"term": {"id": "PANTHER:PTHR13337", "label": "f"}}}
    assert list(iter_family_member_uses(no_member)) == []

    no_family = {
        "family": {
            "representative_members": [{"term": {"id": "UniProtKB:O14521", "label": "r"}}]
        }
    }
    assert list(iter_family_member_uses(no_family)) == []


def test_validate_family_members_accepts_member_in_declared_family():
    uses = list(iter_family_member_uses(_family_doc("PANTHER:PTHR13337", "O14521")))

    errors, warnings = validate_family_members(uses, {"O14521": "PTHR13337:SF6"})

    assert errors == []
    assert warnings == []


def test_validate_family_members_rejects_member_in_a_different_family():
    """The SDHD/ANP32 case: a real id whose label describes another protein."""
    uses = list(iter_family_member_uses(_family_doc("PANTHER:PTHR11375", "O14521")))

    errors, warnings = validate_family_members(uses, {"O14521": "PTHR13337:SF6"})

    assert warnings == []
    assert len(errors) == 1
    assert "PANTHER:PTHR11375" in errors[0]
    assert "O14521 is in PANTHER:PTHR13337:SF6" in errors[0]


def test_validate_family_members_matches_on_family_when_declared_as_subfamily():
    uses = list(iter_family_member_uses(_family_doc("PANTHER:PTHR13337:SF6", "O14521")))

    errors, _ = validate_family_members(uses, {"O14521": "PTHR13337:SF6"})

    assert errors == []


def test_validate_family_members_warns_when_accession_is_unindexed():
    """An uncited protein must not fail the build, only warn."""
    uses = list(iter_family_member_uses(_family_doc("PANTHER:PTHR13337", "Q00000")))

    errors, warnings = validate_family_members(uses, {"O14521": "PTHR13337:SF6"})

    assert errors == []
    assert len(warnings) == 1
    assert "Q00000" in warnings[0]


def test_validate_terms_skips_ptn_ids():
    """PTNs share the PANTHER prefix but are checked against PAINT, not the OBO."""
    terms = [("PANTHER:PTN000000001", "PTN000000001")]

    def resolver(curie):
        raise AssertionError(f"PTN {curie} must not be routed to the OBO adapter")

    errors, warnings = validate_terms(
        terms, {"PANTHER": "simpleobo:panther.obo"}, resolver
    )

    assert errors == []
    assert warnings == []


def test_iter_cited_ptn_sources_finds_evidence_source_ids():
    doc = {
        "family": {
            "evidence": [
                {"source_id": "PANTHER:PTN000000001"},
                {"source_id": "GO_REF:0000033"},
            ]
        }
    }

    assert list(iter_cited_ptn_sources(doc)) == [
        ("$.family.evidence[0].source_id", "PANTHER:PTN000000001")
    ]


def test_validate_cited_ptn_sources_rejects_unknown_node():
    cited = [("$.evidence[0].source_id", "PANTHER:PTN999999999")]

    errors = validate_cited_ptn_sources(cited, {"PANTHER:PTN000000001": [_paint_row()]})

    assert len(errors) == 1
    assert "PTN999999999" in errors[0]


def test_validate_cited_ptn_sources_accepts_known_node_without_positive_ibd():
    """IRD/IKR nodes are legitimate provenance; only existence is required."""
    row = _paint_row(evidence="IRD", negated=True)
    cited = [("$.evidence[0].source_id", "PANTHER:PTN000000001")]

    assert validate_cited_ptn_sources(cited, {"PANTHER:PTN000000001": [row]}) == []


def test_validate_cited_ptn_sources_accepts_goa_attested_node():
    """A GOA-attested node is machine-sourced, so it is trusted even when the
    current PAINT snapshot no longer carries it (release skew)."""
    cited = [("$.evidence[0].source_id", "PANTHER:PTN002225929")]

    assert (
        validate_cited_ptn_sources(cited, {}, {"PANTHER:PTN002225929"}) == []
    )


def test_load_goa_attested_ptns_reads_with_from_column(tmp_path):
    gene_dir = tmp_path / "PSEPK" / "mutL"
    gene_dir.mkdir(parents=True)
    (gene_dir / "mutL-goa.tsv").write_text(
        "SYMBOL\tQUALIFIER\tGO TERM\tWITH/FROM\n"
        "mutL\tinvolved_in\tGO:0006298\tPANTHER:PTN002225929|UniProtKB:P23367\n"
    )

    assert load_goa_attested_ptns(tmp_path) == {"PANTHER:PTN002225929"}


def test_validate_family_members_warns_on_partial_membership():
    """A functional grouping PANTHER splits across families is advisory only."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR24320", "label": "RETINOL DEHYDROGENASE"},
            "representative_members": [
                {"term": {"id": "UniProtKB:Q96NR8", "label": "RDH12"}},
                {"term": {"id": "UniProtKB:Q9NYR8", "label": "RDH8"}},
            ],
        }
    }
    uses = list(iter_family_member_uses(doc))

    errors, warnings = validate_family_members(
        uses, {"Q96NR8": "PTHR24320:SF275", "Q9NYR8": "PTHR43391:SF8"}
    )

    assert errors == []
    assert len(warnings) == 1
    assert "Q9NYR8 is in PANTHER:PTHR43391:SF8" in warnings[0]


def test_validate_family_members_defers_to_paint_corroboration():
    """UniProt and PAINT disagree for some proteins; a PAINT-backed grounding
    is corroborated by a second machine source, so it warns rather than fails."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR16515", "label": "PR DOMAIN ZINC FINGER PROTEIN"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P10069", "label": "BrlA"}}
            ],
            "ancestral_nodes": [
                {"term": {"id": "PANTHER:PTN004463661", "label": "PTN004463661"}}
            ],
        }
    }
    uses = list(iter_family_member_uses(doc))
    assert uses[0].ancestral_node_curies == frozenset({"PANTHER:PTN004463661"})
    paint = {"PANTHER:PTN004463661": [_paint_row(family="PTHR16515")]}

    errors, warnings = validate_family_members(
        uses, {"P10069": "PTHR14003:SF19"}, paint
    )

    assert errors == []
    assert len(warnings) == 1
    assert "disagree" in warnings[0]


def test_validate_family_members_still_errors_without_corroboration():
    """A PAINT node in some *other* family does not rescue a bad grounding."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR11375", "label": "x"},
            "representative_members": [
                {"term": {"id": "UniProtKB:O14521", "label": "SDHD"}}
            ],
            "ancestral_nodes": [
                {"term": {"id": "PANTHER:PTN000000001", "label": "PTN000000001"}}
            ],
        }
    }
    paint = {"PANTHER:PTN000000001": [_paint_row(family="PTHR99999")]}

    errors, _ = validate_family_members(
        list(iter_family_member_uses(doc)), {"O14521": "PTHR13337:SF6"}, paint
    )

    assert len(errors) == 1


def test_compare_label_flags_divergent_mismatch_as_likely_wrong_id():
    """A label naming a different entity points at the id, not the label."""
    message = compare_label(
        "PANTHER:PTHR11375",
        "SUCCINATE DEHYDROGENASE CYTOCHROME B SMALL SUBUNIT",
        "ACIDIC LEUCINE-RICH NUCLEAR PHOSPHOPROTEIN 32",
        set(),
    )
    assert message is not None
    assert "usually means the ID is wrong" in message


def test_compare_label_omits_hint_for_near_miss_labels():
    message = compare_label(
        "PANTHER:PTHR11732", "ALDO-KETO REDUCTASE", "ALDO/KETO REDUCTASE", set()
    )
    assert message is not None
    assert "usually means the ID is wrong" not in message


def test_count_ungrounded_families_counts_only_member_bearing_descriptors():
    """Keeps the not-yet-grounded backlog countable without a suppression file."""
    doc = {
        "parts": [
            # no id, but names members -> counted
            {
                "family": {
                    "preferred_term": "some family",
                    "representative_members": [
                        {"term": {"id": "UniProtKB:P1", "label": "m"}}
                    ],
                }
            },
            # has an id -> not counted
            {
                "family": {
                    "term": {"id": "PANTHER:PTHR1", "label": "x"},
                    "representative_members": [
                        {"term": {"id": "UniProtKB:P2", "label": "m"}}
                    ],
                }
            },
            # no id and no members -> nothing to ground, not counted
            {"family": {"preferred_term": "vague"}},
        ]
    }

    assert count_ungrounded_families(doc) == 1


def test_count_ungrounded_families_sees_family_terms_only_grounding():
    """A descriptor grounded only via family_terms[] is grounded, not a backlog item.

    Three real modules use that shape. Reading only `family` -> `term` counts
    them as ungrounded and inflates the figure -- the same family_terms blind
    spot that has bitten this file before.
    """
    doc = {
        "family": {
            "family_terms": [{"id": "PANTHER:PTHR38761:SF1", "label": "x"}],
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "m"}}
            ],
        }
    }

    assert count_ungrounded_families(doc) == 0


def test_count_ungrounded_families_treats_non_panther_term_as_grounded():
    """The counter measures 'no id at all', not 'no PANTHER id'."""
    doc = {
        "family": {
            "term": {"id": "InterPro:IPR000719", "label": "x"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "m"}}
            ],
        }
    }

    assert count_ungrounded_families(doc) == 0


def test_validate_paint_ptns_rejects_inheriting_a_lost_function():
    """The ERBB3 case: PAINT recorded IRD loss of the very term asserted.

    Pseudoenzymes keep the fold and the family membership while losing the
    ancestral activity, so a node that records the loss cannot support
    inheriting it.
    """
    doc = {
        "function": {
            "term": {"id": "GO:0004714", "label": "kinase"},
        },
        "family": {
            "term": {"id": "PANTHER:PTHR24416", "label": "f"},
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "n"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(go_id="GO:0038131", aspect="F"),
            _paint_row(go_id="GO:0004714", aspect="F", evidence="IRD", negated=True),
        ]
    }

    errors, _ = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert len(errors) == 1
    assert "LOST" in errors[0]
    assert "GO:0004714" in errors[0]
    assert "GO:0038131" in errors[0]  # names what the node does retain


def test_validate_paint_ptns_allows_retained_function_alongside_a_loss():
    """A node with both losses and retained terms still supports the retained ones."""
    doc = {
        "function": {"term": {"id": "GO:0038131", "label": "neuregulin receptor"}},
        "family": {
            "term": {"id": "PANTHER:PTHR24416", "label": "f"},
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "n"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(go_id="GO:0038131", aspect="F"),
            _paint_row(go_id="GO:0004714", aspect="F", evidence="IRD", negated=True),
        ]
    }

    errors, _ = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []


def test_validate_family_members_advises_subfamily_for_heterogeneous_family():
    """PTHR24416 grounds 13 different receptor kinases; the family says little."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR24416", "label": "TYROSINE-PROTEIN KINASE RECEPTOR"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P00533", "label": "EGFR"}}
            ],
        }
    }
    uses = list(iter_family_member_uses(doc))

    errors, warnings = validate_family_members(
        uses, {"P00533": "PTHR24416:SF91"}, subfamily_counts={"PTHR24416": 96}
    )

    assert errors == []
    assert len(warnings) == 1
    assert "96 subfamilies" in warnings[0]
    assert "PANTHER:PTHR24416:SF91" in warnings[0]


def test_validate_family_members_no_subfamily_advice_for_small_family():
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "f"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "m"}}
            ],
        }
    }
    errors, warnings = validate_family_members(
        list(iter_family_member_uses(doc)),
        {"P1": "PTHR1:SF2"},
        subfamily_counts={"PTHR1": 3},
    )
    assert (errors, warnings) == ([], [])


def test_validate_family_members_no_subfamily_advice_when_already_specific():
    """A descriptor already grounded at subfamily level needs no advice."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR24416:SF91", "label": "EGFR"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P00533", "label": "EGFR"}}
            ],
        }
    }
    errors, warnings = validate_family_members(
        list(iter_family_member_uses(doc)),
        {"P00533": "PTHR24416:SF91"},
        subfamily_counts={"PTHR24416": 96},
    )
    assert (errors, warnings) == ([], [])


def test_validate_paint_ptns_seed_overlap_is_vacuous_without_uniprot_seeds():
    """PAINT seeds are often MGI/SGD/FB ids; an empty UniProt set proves nothing."""
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "f"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "rep"}}
            ],
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "n"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(seeds="MGI:MGI:88314|SGD:S000003865")
        ]
    }

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []
    assert len(warnings) == 1
    assert "not checked" in warnings[0]
    assert "MGI:MGI:88314" in warnings[0]


def test_validate_paint_ptns_seed_overlap_still_flags_a_real_miss():
    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "f"},
            "representative_members": [
                {"term": {"id": "UniProtKB:P1", "label": "rep"}}
            ],
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "n"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }
    index = {"PANTHER:PTN000000001": [_paint_row(seeds="UniProtKB:P99999")]}

    errors, warnings = validate_paint_ptns(list(iter_ancestral_node_uses(doc)), index)

    assert errors == []
    assert len(warnings) == 1
    assert "no representative UniProtKB accession" in warnings[0]


def _loss_doc(asserted_go: str) -> dict:
    return {
        "function": {"term": {"id": asserted_go, "label": "f"}},
        "family": {
            "term": {"id": "PANTHER:PTHR1", "label": "f"},
            "ancestral_nodes": [
                {
                    "term": {"id": "PANTHER:PTN000000001", "label": "n"},
                    "evidence": [{"source_id": "GO_REF:0000033"}],
                }
            ],
        },
    }


# Real GO relation: GO:0004714 (transmembrane receptor protein tyrosine kinase
# activity) is_a GO:0004713 (protein tyrosine kinase activity). GO:0004713 is
# the BROADER term -- worth stating, because getting this backwards is exactly
# how a test can pass while encoding a false ontology fact.
_PTK_ANCESTORS = {
    "GO:0004714": {"GO:0004714", "GO:0004713", "GO:0003674"},
    "GO:0004713": {"GO:0004713", "GO:0003674"},
}


def _ptk_ancestors(term: str) -> set:
    return _PTK_ANCESTORS.get(term, {term})


def test_validate_paint_ptns_rejects_a_descendant_of_a_lost_term():
    """Asserting a specialisation of a struck-out term must not evade the check.

    Losing the broad GO:0004713 also rules out the narrower GO:0004714.
    """
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(go_id="GO:0038131", aspect="F"),
            _paint_row(go_id="GO:0004713", aspect="F", evidence="IRD", negated=True),
        ]
    }

    errors, _ = validate_paint_ptns(
        list(iter_ancestral_node_uses(_loss_doc("GO:0004714"))),
        index,
        _ptk_ancestors,
    )

    assert len(errors) == 1
    assert "LOST" in errors[0]


def test_validate_paint_ptns_allows_an_ancestor_of_a_lost_term():
    """Asserting something broader than what was lost is not contradicted.

    ERBB3 loses the narrow GO:0004714, but a family whose other members retain
    tyrosine kinase activity is still validly described by the broader
    GO:0004713.
    """
    index = {
        "PANTHER:PTN000000001": [
            _paint_row(go_id="GO:0004713", aspect="F"),
            _paint_row(go_id="GO:0004714", aspect="F", evidence="IRD", negated=True),
        ]
    }

    errors, _ = validate_paint_ptns(
        list(iter_ancestral_node_uses(_loss_doc("GO:0004713"))),
        index,
        _ptk_ancestors,
    )

    assert errors == []


def test_iter_all_representative_accessions_includes_ungrounded_descriptors():
    """The members of an UNGROUNDED descriptor are the ones most needing lookup.

    iter_family_member_uses requires a family id, so building the member index
    from it excluded exactly the descriptors whose id was dropped for being
    wrong -- the index could not tell you what the id should have been.
    """
    doc = {
        "parts": [
            {  # grounded
                "family": {
                    "term": {"id": "PANTHER:PTHR1", "label": "x"},
                    "representative_members": [
                        {"term": {"id": "UniProtKB:P1", "label": "m"}}
                    ],
                }
            },
            {  # ungrounded -- previously invisible to the index builder
                "family": {
                    "preferred_term": "family we could not establish",
                    "representative_members": [
                        {"term": {"id": "UniProtKB:O14521", "label": "SDHD"}}
                    ],
                }
            },
        ]
    }

    assert set(iter_all_representative_accessions(doc)) == {"P1", "O14521"}
    # the grounded-only view still misses the second one
    grounded = set()
    for use in iter_family_member_uses(doc):
        grounded.update(use.representative_accessions)
    assert grounded == {"P1"}
