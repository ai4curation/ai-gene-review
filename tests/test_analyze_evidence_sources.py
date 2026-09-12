"""Offline tests for the evidence-source analyzer (no network)."""

from pathlib import Path

import yaml

from ai_gene_review.tools.analyze_evidence_sources import (
    build_report,
    collect_pmids_from_review,
    collect_rows,
    resolve_publication_type,
)

REVIEW = {
    "gene_symbol": "TEST",
    "references": [
        {"id": "PMID:111", "title": "primary", "findings": []},
        {"id": "PMID:222", "title": "review"},
        {"id": "GO_REF:0000043", "title": "phylo"},
        {"id": "file:human/TEST/TEST-deep-research-openai.md", "title": "dr"},
    ],
    "existing_annotations": [
        {
            "term": {"id": "GO:0001"},
            "original_reference_id": "PMID:111",
            "review": {
                "action": "ACCEPT",
                "supported_by": [
                    {"reference_id": "PMID:111", "reference_section_type": "ABSTRACT"},
                    {"reference_id": "PMID:222", "reference_section_type": "DISCUSSION"},
                ],
            },
        },
        {
            "term": {"id": "GO:0002"},
            "original_reference_id": "PMID:111",
            "review": {
                "action": "REMOVE",
                "supported_by": [
                    {"reference_id": "PMID:111", "reference_section_type": "RESULTS"},
                ],
            },
        },
    ],
    "core_functions": [
        {"supported_by": [{"reference_id": "PMID:111", "reference_section_type": "RESULTS"}]}
    ],
}

TYPE_CACHE = {
    "111": ["Journal Article"],
    "222": ["Journal Article", "Review"],
}


def test_resolve_publication_type():
    assert resolve_publication_type("PMID:111", TYPE_CACHE) == "PRIMARY_RESEARCH"
    assert resolve_publication_type("PMID:222", TYPE_CACHE) == "REVIEW"
    assert resolve_publication_type("GO_REF:0000043", TYPE_CACHE) == "DATABASE"
    assert (
        resolve_publication_type("file:x-deep-research-openai.md", TYPE_CACHE)
        == "DEEP_RESEARCH"
    )
    # PMID absent from cache -> UNKNOWN
    assert resolve_publication_type("PMID:999", TYPE_CACHE) == "UNKNOWN"


def test_collect_pmids_from_review():
    assert collect_pmids_from_review(REVIEW) == ["111", "222"]


def test_collect_rows_and_report(tmp_path: Path):
    path = tmp_path / "TEST-ai-review.yaml"
    path.write_text(yaml.dump(REVIEW))

    frames = collect_rows([path], TYPE_CACHE)

    refs = frames["references"]
    anns = frames["annotations"]
    snips = frames["snippets"]

    assert len(refs) == 4
    assert set(refs["publication_type"]) == {
        "PRIMARY_RESEARCH",
        "REVIEW",
        "DATABASE",
        "DEEP_RESEARCH",
    }

    # ACCEPT annotation: supported by both primary and review; not all-shallow
    accept = anns[anns["action"] == "ACCEPT"].iloc[0]
    assert accept["has_review"]
    assert accept["has_primary"]
    assert not accept["all_shallow"]  # has a DISCUSSION snippet
    assert accept["any_narrative"]

    # REMOVE annotation: RESULTS only -> not shallow, no review
    remove = anns[anns["action"] == "REMOVE"].iloc[0]
    assert not remove["has_review"]
    assert remove["any_deep"]

    # snippets include annotation + core_function contexts
    assert set(snips["context"]) == {"annotation", "core_function"}

    report = build_report(frames, "test")
    assert "Evidence-source analysis (test)" in report
    assert "Deep-research references" in report
