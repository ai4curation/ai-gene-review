"""Tests for derived module QC statistics (ai_gene_review.module_qc)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_qc import (
    base_accession,
    collect_module_qc,
    collect_uniprot_groundings,
    index_gene_reviews,
    is_leaf_node,
    iter_nodes,
    leaf_nodes_missing_representatives,
    module_deep_research,
    module_gene_review_summary,
    node_representative_groundings,
    review_completeness,
    run_data_qc,
)

MODULES_DIR = Path("modules")
SCHEMA_PATH = Path("src/ai_gene_review/schema/gene_review.yaml")


def load_module(name: str) -> dict:
    return yaml.safe_load((MODULES_DIR / name).read_text())


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "value,expected",
    [
        ("UniProtKB:Q9NPJ1", "Q9NPJ1"),
        ("UniProtKB:P19544-1", "P19544"),
        ("Q9NPJ1", "Q9NPJ1"),
        (None, None),
        ("", None),
    ],
)
def test_base_accession(value, expected):
    assert base_accession(value) == expected


def test_is_leaf_node():
    assert is_leaf_node({"id": "a"})
    assert not is_leaf_node({"id": "a", "parts": [{"node": {"id": "b"}}]})
    assert not is_leaf_node(
        {"id": "a", "variant_sets": [{"id": "v", "variants": [{"id": "b"}]}]}
    )


# ---------------------------------------------------------------------------
# Tree traversal
# ---------------------------------------------------------------------------

def test_iter_nodes_visits_nested_parts():
    data = {
        "module": {
            "id": "root",
            "parts": [
                {"node": {"id": "child1"}},
                {
                    "node": {
                        "id": "child2",
                        "variant_sets": [
                            {"id": "vs", "variants": [{"id": "grandchild"}]}
                        ],
                    }
                },
            ],
        }
    }
    ids = {node["id"] for node in iter_nodes(data)}
    assert ids == {"root", "child1", "child2", "grandchild"}


# ---------------------------------------------------------------------------
# Representative-member / leaf grounding
# ---------------------------------------------------------------------------

def test_node_representative_groundings_concrete_gene_product():
    node = {
        "id": "n",
        "annotons": [
            {
                "participant": {
                    "selector_type": "GENE_PRODUCT",
                    "gene_product": {
                        "preferred_term": "BBS1",
                        "term": {"id": "UniProtKB:Q8NFJ9", "label": "BBS1"},
                    },
                }
            }
        ],
    }
    groundings = node_representative_groundings(node)
    assert groundings == [{"id": "UniProtKB:Q8NFJ9", "label": "BBS1"}]


def test_node_representative_groundings_family_with_members():
    node = {
        "id": "n",
        "annotons": [
            {
                "participant": {
                    "selector_type": "FAMILY",
                    "family": {
                        "preferred_term": "Ras GTPases",
                        "representative_members": [
                            {
                                "preferred_term": "HRAS",
                                "term": {"id": "UniProtKB:P01112"},
                            }
                        ],
                    },
                }
            }
        ],
    }
    groundings = node_representative_groundings(node)
    assert groundings == [{"id": "UniProtKB:P01112", "label": "HRAS"}]


def test_family_without_representatives_is_not_grounded():
    node = {
        "id": "n",
        "annotons": [
            {
                "participant": {
                    "selector_type": "FAMILY",
                    "family": {"preferred_term": "SOS Ras GEFs"},
                }
            }
        ],
    }
    assert node_representative_groundings(node) == []


def test_protein_complex_active_units_grounded():
    node = {
        "id": "n",
        "annotons": [
            {
                "participant": {
                    "selector_type": "PROTEIN_COMPLEX",
                    "protein_complex": {
                        "preferred_term": "BBSome",
                        "active_units": [
                            {
                                "participant": {
                                    "selector_type": "GENE_PRODUCT",
                                    "gene_product": {
                                        "preferred_term": "BBS1",
                                        "term": {"id": "UniProtKB:Q8NFJ9"},
                                    },
                                }
                            }
                        ],
                    },
                }
            }
        ],
    }
    groundings = node_representative_groundings(node)
    assert groundings == [{"id": "UniProtKB:Q8NFJ9", "label": "BBS1"}]


def test_bbsome_leaf_grounding():
    # bbsome.yaml grounds most subunits to concrete UniProt accessions, but the
    # cargo-trafficking leaf references the BBSome only by its GO complex term
    # (no active_units / representative members), so it is correctly flagged.
    data = load_module("bbsome.yaml")
    flagged = leaf_nodes_missing_representatives(data)
    flagged_ids = {item["id"] for item in flagged}
    assert "bbsome_cargo_trafficking" in flagged_ids
    # The octamer leaf lists concrete subunits, so it must not be flagged.
    assert "bbsome_core_octamer" not in flagged_ids


def test_ras_mapk_flags_abstract_family_leaves():
    # erk_cascade.yaml uses some FAMILY selectors without representatives.
    data = load_module("erk_cascade.yaml")
    flagged = leaf_nodes_missing_representatives(data)
    # At least one leaf (e.g. the SOS GEF step) lacks representative members.
    assert any(
        "FAMILY" in item["selector_types"] for item in flagged
    ), flagged


# ---------------------------------------------------------------------------
# UniProt grounding collection
# ---------------------------------------------------------------------------

def test_collect_uniprot_groundings_dedupes_on_base_accession():
    data = {
        "module": {
            "id": "root",
            "annotons": [
                {
                    "participant": {
                        "gene_product": {"term": {"id": "UniProtKB:Q8NFJ9"}}
                    }
                },
                {
                    "participant": {
                        "gene_product": {"term": {"id": "UniProtKB:Q8NFJ9-2"}}
                    }
                },
            ],
        }
    }
    groundings = collect_uniprot_groundings(data)
    assert [g["accession"] for g in groundings] == ["Q8NFJ9"]


def test_collect_uniprot_groundings_bbsome():
    data = load_module("bbsome.yaml")
    accessions = {g["accession"] for g in collect_uniprot_groundings(data)}
    assert "Q8NFJ9" in accessions  # BBS1
    assert "Q9NPJ1" in accessions  # MKKS/BBS6


# ---------------------------------------------------------------------------
# Gene-review index and join
# ---------------------------------------------------------------------------

def test_index_gene_reviews_and_completeness(tmp_path):
    genes = tmp_path / "genes"
    gene_dir = genes / "human" / "FOO"
    gene_dir.mkdir(parents=True)
    review = gene_dir / "FOO-ai-review.yaml"
    review.write_text(
        "id: Q12345\n"
        "gene_symbol: FOO\n"
        "existing_annotations:\n"
        "  - term: {id: 'GO:0001', label: x}\n"
        "    review: {action: ACCEPT}\n"
        "  - term: {id: 'GO:0002', label: y}\n"
        "    review: {action: PENDING}\n"
    )
    (gene_dir / "FOO-deep-research-openai.md").write_text("# research\n")

    index = index_gene_reviews(genes)
    assert index == {"Q12345": review}

    completeness = review_completeness(review)
    assert completeness["total_annotations"] == 2
    assert completeness["reviewed_annotations"] == 1
    assert completeness["complete"] is False
    assert completeness["has_deep_research"] is True


def test_module_gene_review_summary_join(tmp_path):
    genes = tmp_path / "genes"
    gene_dir = genes / "human" / "FOO"
    gene_dir.mkdir(parents=True)
    (gene_dir / "FOO-ai-review.yaml").write_text(
        "id: Q12345\n"
        "gene_symbol: FOO\n"
        "existing_annotations:\n"
        "  - term: {id: 'GO:0001', label: x}\n"
        "    review: {action: ACCEPT}\n"
    )

    data = {
        "module": {
            "id": "root",
            "annotons": [
                {"participant": {"gene_product": {"term": {"id": "UniProtKB:Q12345"}}}},
                {"participant": {"gene_product": {"term": {"id": "UniProtKB:Q99999"}}}},
            ],
        }
    }
    summary = module_gene_review_summary(data, genes_dir=genes)
    assert summary["total_genes"] == 2
    assert summary["with_review"] == 1
    assert summary["without_review"] == 1
    assert summary["complete_reviews"] == 1
    # Q99999 has no review; Q12345 has a review but no deep research file.
    assert summary["without_deep_research"] == 1


# ---------------------------------------------------------------------------
# Module-level deep research
# ---------------------------------------------------------------------------

def test_module_deep_research_present():
    result = module_deep_research(MODULES_DIR / "photosynthesis.yaml")
    assert result["has_deep_research"] is True
    assert any(r["provider"] == "falcon" for r in result["reports"])


def test_module_deep_research_absent():
    result = module_deep_research(MODULES_DIR / "bbsome.yaml")
    assert result["has_deep_research"] is False
    assert result["reports"] == []


# ---------------------------------------------------------------------------
# linkml-data-qc
# ---------------------------------------------------------------------------

def test_run_data_qc_returns_compliance():
    result = run_data_qc(MODULES_DIR / "bbsome.yaml", schema_path=SCHEMA_PATH)
    assert "global_compliance" in result
    assert isinstance(result["global_compliance"], float)
    assert isinstance(result["missing"], list)
    assert "status" in result["recommended_slots"]


def test_collect_module_qc_smoke():
    yaml_path = MODULES_DIR / "bbsome.yaml"
    data = load_module("bbsome.yaml")
    qc = collect_module_qc(yaml_path, data, schema_path=SCHEMA_PATH)
    assert set(qc) == {
        "data_qc",
        "leaf_nodes_missing_representatives",
        "conformance_violations",
        "reaction_chaining",
        "gene_reviews",
        "module_deep_research",
    }
    assert qc["module_deep_research"]["has_deep_research"] is False


# ---------------------------------------------------------------------------
# Reaction chaining check (advisory; GO MF -> RHEA -> equation)
# ---------------------------------------------------------------------------

from ai_gene_review.module_qc import reaction_chaining_findings  # noqa: E402


def _chain_module(connection_extra: dict | None = None) -> dict:
    """A 3-step linear pathway: s1 -> s2 -> s3, each a one-annoton reaction."""
    conn12 = {"source": "s1", "target": "s2", "connection_type": "PRECEDES"}
    if connection_extra:
        conn12.update(connection_extra)
    return {
        "module": {
            "parts": [
                {"order": 1, "node": {"id": "s1", "annotons": [
                    {"function": {"term": {"id": "GO:1"}}}]}},
                {"order": 2, "node": {"id": "s2", "annotons": [
                    {"function": {"term": {"id": "GO:2"}}}]}},
                {"order": 3, "node": {"id": "s3", "annotons": [
                    {"function": {"term": {"id": "GO:3"}}}]}},
            ],
            "connections": [
                conn12,
                {"source": "s2", "target": "s3", "connection_type": "PRECEDES"},
            ],
        }
    }


# GO:1 makes (2E)-enoyl-CoA; GO:2 consumes it -> (3S)-3-hydroxyacyl-CoA;
# GO:3 deliberately does NOT consume that intermediate (a real break s2->s3).
_EQS = {
    "R:1": "an acyl-CoA = a (2E)-enoyl-CoA",
    "R:2": "a (2E)-enoyl-CoA + H2O = a (3S)-3-hydroxyacyl-CoA",
    "R:3": "acetoacetyl-CoA + CoA = 2 acetyl-CoA",
}
_MF = {"GO:1": ["R:1"], "GO:2": ["R:2"], "GO:3": ["R:3"]}


def _resolvers():
    return (lambda g: _MF.get(g, []), lambda r: _EQS.get(r))


def test_chaining_detects_shared_intermediate():
    mf, eq = _resolvers()
    findings = reaction_chaining_findings(_chain_module(), mf, eq)
    by_edge = {(f["source"], f["target"]): f for f in findings}
    ok = by_edge[("s1", "s2")]
    assert ok["severity"] == "info"
    assert "2eenoylcoa" in ok["shared"]


def test_chaining_warns_on_unacknowledged_break():
    mf, eq = _resolvers()
    findings = reaction_chaining_findings(_chain_module(), mf, eq)
    by_edge = {(f["source"], f["target"]): f for f in findings}
    broken = by_edge[("s2", "s3")]
    assert broken["severity"] == "warning"
    assert broken["status"] == "UNVERIFIED"


@pytest.mark.parametrize("status", ["KNOWLEDGE_GAP", "MAPPING_GAP", "NOT_APPLICABLE"])
def test_chaining_override_suppresses_warning(status):
    """An acknowledged break is reported as info, not warning."""
    mf, eq = _resolvers()
    # Put the override on the s2->s3 break by swapping which edge carries it:
    data = _chain_module()
    for c in data["module"]["connections"]:
        if (c["source"], c["target"]) == ("s2", "s3"):
            c["chaining_status"] = status
            c["chaining_note"] = "known gap"
    findings = reaction_chaining_findings(data, mf, eq)
    broken = {(f["source"], f["target"]): f for f in findings}[("s2", "s3")]
    assert broken["severity"] == "info"
    assert broken["status"] == status


def test_chaining_verified_override_suppresses_warning():
    """A curator VERIFIED is trusted over the string matcher (it cannot see
    ChEBI class subsumption, e.g. acetoacetyl-CoA is a 3-oxoacyl-CoA), so an
    explicit VERIFIED suppresses the advisory warning."""
    mf, eq = _resolvers()
    data = _chain_module()
    for c in data["module"]["connections"]:
        if (c["source"], c["target"]) == ("s2", "s3"):
            c["chaining_status"] = "VERIFIED"
    findings = reaction_chaining_findings(data, mf, eq)
    broken = {(f["source"], f["target"]): f for f in findings}[("s2", "s3")]
    assert broken["severity"] == "info"
    assert broken["status"] == "VERIFIED"


def test_chaining_unresolvable_mf_is_not_a_warning():
    """If a GO MF has no RHEA mapping, the edge is 'not checked', not a warning."""
    mf = lambda g: [] if g == "GO:2" else _MF.get(g, [])  # noqa: E731
    eq = lambda r: _EQS.get(r)  # noqa: E731
    findings = reaction_chaining_findings(_chain_module(), mf, eq)
    for f in findings:
        if "s2" in (f["source"], f["target"]):
            assert f["severity"] == "info"
            assert f["status"] == "NOT_CHECKED"
