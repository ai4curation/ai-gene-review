"""Tests for the litscan module-member scan engine (offline)."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.litscan import module_member
from ai_gene_review.litscan.europepmc import Publication, publication_from_record
from ai_gene_review.litscan.module_index import (
    ModuleEntity,
    load_modules,
    module_entity_from_doc,
)
from ai_gene_review.litscan.scoring import (
    MEMBERSHIP_SIGNALS,
    build_module_query,
    select_query_terms,
    extract_signal_sentences,
    is_distinctive,
)

MODULES_DIR = Path(__file__).resolve().parents[1] / "modules"

TINY_MODULE = yaml.safe_load(
    """
id: MODULE:demo
title: Demo trafficking complex module
evidence:
  - source_id: PMID:17574030
    title: A paper
  - source_id: file:modules/demo-notes.md
    title: notes
module:
  label: Demo trafficking complex
  parts:
    - annotons:
        - preferred_term: DemoSome
          term:
            id: GO:0001234
            label: demosome assembly
        - participant:
            descriptor:
              preferred_term: BBS10
              term:
                id: UniProtKB:Q8TAM1
                label: Bardet-Biedl syndrome 10 protein
"""
)


def test_module_entity_extracts_terms_and_citations():
    entity = module_entity_from_doc(TINY_MODULE, Path("modules/demo.yaml"))
    assert entity.id == "MODULE:demo"
    assert entity.cited_pmids == {"PMID:17574030"}  # file: source_id ignored
    assert "DemoSome" in entity.terms
    assert "BBS10" in entity.terms
    assert "demosome assembly" in entity.terms
    assert "Demo trafficking complex module" in entity.terms


def test_load_real_modules_includes_bbsome():
    entities = load_modules(MODULES_DIR)
    assert len(entities) >= 5
    by_id = {e.id: e for e in entities}
    bbsome = by_id["MODULE:bbsome"]
    assert any(t.casefold() == "bbsome" for t in bbsome.terms)
    # A known BBSome evidence PMID is collected as a cited reference.
    assert "PMID:17574030" in bbsome.cited_pmids


@pytest.mark.parametrize(
    "term,expected",
    [
        ("BBSome", True),
        ("intraciliary transport", True),
        ("Calvin-Benson", True),
        ("complex", False),
        ("protein", False),
        ("protein folding chaperone", False),
        ("GTP-dependent recruitment of the BBSome to the ciliary membrane", False),
        ("ciliary GPCR cargo (e.g. SSTR3, MCHR1, NPY2R)", False),
        ("ab", False),
    ],
)
def test_is_distinctive(term, expected):
    assert is_distinctive(term) is expected


def test_select_query_terms_prefers_named_entities_and_drops_generic():
    chosen = select_query_terms(
        ["complex", "intraciliary transport", "BBSome", "BBS10"], max_terms=5
    )
    assert "complex" not in chosen
    # proper-noun named entities (acronyms/symbols) rank ahead of lowercase phrases
    assert chosen[0] in {"BBSome", "BBS10"}
    assert "BBSome" in chosen and "BBS10" in chosen
    assert "intraciliary transport" in chosen


def test_build_module_query_uses_distinctive_terms_and_exclusions():
    query = build_module_query(["BBSome", "complex"], "2026-01-01", "2026-06-19")
    assert 'TITLE_ABS:"BBSome"' in query
    assert 'TITLE_ABS:"complex"' not in query
    assert 'TITLE:"genome-wide identification"' in query
    assert "FIRST_PDATE:[2026-01-01 TO 2026-06-19]" in query


def test_build_module_query_raises_without_distinctive_terms():
    with pytest.raises(ValueError):
        build_module_query(["complex", "protein"], "2026-01-01", "2026-06-19")


def test_extract_membership_sentences():
    text = (
        "We identify a novel subunit of the BBSome. "
        "Mice show an obesity phenotype. "
        "The crystal structure reveals the assembly factor binds tubby."
    )
    signals = extract_signal_sentences(text, MEMBERSHIP_SIGNALS)
    sentences = [s["sentence"] for s in signals]
    assert any("novel subunit" in s for s in sentences)
    assert any("crystal structure" in s for s in sentences)
    assert not any("obesity phenotype" in s for s in sentences)


def test_publication_already_cited_flag():
    pub = publication_from_record(
        {"source": "MED", "id": "17574030", "title": "x", "abstractText": "y"}
    )
    assert pub.pmid == "17574030"
    assert pub.reference_id == "PMID:17574030"


def test_render_markdown_marks_new_and_cited():
    packet = {
        "generated_at": "2026-06-19T00:00:00+00:00",
        "date_from": "2026-03-21",
        "date_to": "2026-06-19",
        "module_count": 1,
        "total_records": 2,
        "modules": [
            {
                "module_id": "MODULE:bbsome",
                "module_title": "BBSome module",
                "module_path": "modules/bbsome.yaml",
                "query": "...",
                "query_terms": ["BBSome"],
                "hit_count": 25,
                "cited_pmid_count": 6,
                "record_count": 2,
                "records": [
                    {
                        "pmid": "99999999",
                        "doi": "",
                        "title": "A novel subunit of the BBSome",
                        "journal": "J",
                        "publication_date": "2026-06-01",
                        "authors": "",
                        "pubmed_url": "",
                        "abstract": "",
                        "already_cited": False,
                        "membership_score": 1,
                        "membership_signals": [
                            {
                                "categories": ["new_member"],
                                "sentence": "A novel subunit of the BBSome",
                            }
                        ],
                    },
                    {
                        "pmid": "17574030",
                        "doi": "",
                        "title": "Old paper",
                        "journal": "J",
                        "publication_date": "2026-05-01",
                        "authors": "",
                        "pubmed_url": "",
                        "abstract": "",
                        "already_cited": True,
                        "membership_score": 0,
                        "membership_signals": [],
                    },
                ],
            }
        ],
    }
    md = module_member.render_markdown(packet)
    assert "[NEW] PMID:99999999" in md
    assert "[cited] PMID:17574030" in md
    assert "novel subunit" in md


def _plain_pub(pmid: str, publication_date: str) -> Publication:
    """A publication with no title/abstract signals (membership_score == 0)."""
    return Publication(
        pmid=pmid,
        doi="",
        title="",
        journal="J",
        publication_date=publication_date,
        authors="",
        abstract="",
        source="MED",
        record_id=pmid,
    )


def test_scan_module_preserves_newest_first_on_ties(monkeypatch):
    """When records tie on already_cited and membership_score, the sort must
    preserve europepmc.search's newest-first ordering (regression: the old
    tertiary date key sorted oldest-first)."""
    # Europe PMC returns newest-first; all three tie on already_cited (not cited)
    # and membership_score (0, since title/abstract carry no membership signals).
    newest_first = [
        _plain_pub("30000003", "2026-06-03"),
        _plain_pub("20000002", "2026-06-02"),
        _plain_pub("10000001", "2026-06-01"),
    ]
    monkeypatch.setattr(
        module_member.europepmc,
        "search",
        lambda *args, **kwargs: (3, newest_first),
    )
    entity = ModuleEntity(
        id="MODULE:demo",
        title="Demo",
        path="modules/demo.yaml",
        terms=["BBSome"],
        cited_pmids=set(),
    )
    result = module_member.scan_module(
        entity,
        "2026-06-01",
        "2026-06-30",
        max_records=40,
        max_terms=10,
        timeout=30.0,
    )
    order = [r["pmid"] for r in result["records"]]
    assert order == ["30000003", "20000002", "10000001"]
    # Newest publication ranks first after the scan.
    assert result["records"][0]["publication_date"] == "2026-06-03"
