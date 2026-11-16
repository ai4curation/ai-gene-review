"""Tests for the feedback-to-resources and annotation-rules landing pages."""

from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.render_hubs import (
    collection_members,
    projects_where,
    render_feedback,
    render_rules,
)

GENE_REVIEW = {
    "id": "P04637",
    "gene_symbol": "TP53",
    "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
    "existing_annotations": [
        {
            "term": {"id": "GO:0005789", "label": "endoplasmic reticulum membrane"},
            "evidence_type": "IDA",
            "original_reference_id": "PMID:1101155",
            "review": {
                "action": "REMOVE",
                "source_defects": [
                    {
                        "defect_type": "WRONG_REFERENCE",
                        "resource": "MGI",
                        "confidence": "CONFIRMED",
                        "asserted_value": "PMID:1101155",
                        "corrected_value": "PMID:11011155",
                        "explanation": "Transposed digits in the PMID.",
                    }
                ],
            },
        }
    ],
    "proposed_new_terms": [
        {
            "proposed_name": "widget holdase activity",
            "proposed_definition": "Holding a widget.",
            "justification": "No term exists.",
        }
    ],
}

OBSOLETION_PAGE = """---
title: "Widget Binding Obsoletion"
maturity: SCOPING
tags: [OBSOLETION]
proposed_ontology_changes:
  - change_type: NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT
    ontology: GO
    origin: SELF_PROPOSED
    about_node:
      id: GO:0000001
      label: widget binding
    justification: Uninformative.
---
# Widget Binding Obsoletion
"""


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    _write(
        tmp_path,
        "genes/human/TP53/TP53-ai-review.yaml",
        yaml.safe_dump(GENE_REVIEW),
    )
    _write(tmp_path, "projects/WIDGET_OBSOLETION.md", OBSOLETION_PAGE)
    _write(
        tmp_path,
        "projects/MAPPING_REVIEWS.md",
        '---\ntitle: "Mapping Reviews"\ncollections: [MAPPINGS]\n---\n# Mapping Reviews\n',
    )
    _write(
        tmp_path,
        "projects/WIDGET2GO.md",
        '---\ntitle: "Widget to GO"\nmaturity: IN_PROGRESS\ncollections: [MAPPINGS]\n---\n# W\n',
    )
    _write(tmp_path, "projects/OTHER.md", '---\ntitle: "Other"\n---\n# Other\n')
    _write(
        tmp_path,
        "projects/collections.yaml",
        "MAPPINGS:\n  title: Mapping reviews\n  index: MAPPING_REVIEWS\n",
    )
    _write(
        tmp_path,
        "rules/curated/CR-0001.yaml",
        yaml.safe_dump(
            {
                "id": "CR-0001",
                "title": "Widgets bind gadgets",
                "status": "PROPOSED",
                "go_annotations": [
                    {"go_id": "GO:0000002", "go_label": "gadget binding"}
                ],
                "replaces": [
                    {"source_type": "INTERPRO2GO", "source_id": "InterPro:IPR1"}
                ],
                "gene_reviews": ["genes/human/TP53/TP53-ai-review.yaml"],
            }
        ),
    )
    _write(tmp_path, "rules/arba/ARBA1/ARBA1-review.yaml", "id: ARBA1\n")
    return tmp_path


def test_projects_selected_from_frontmatter(repo: Path) -> None:
    projects_dir = repo / "projects"
    assert [p["slug"] for p in projects_where(projects_dir, "tags", "OBSOLETION")] == [
        "WIDGET_OBSOLETION"
    ]
    # The collection's own index page is not one of its members.
    assert [p["slug"] for p in collection_members(projects_dir, "MAPPINGS")] == [
        "WIDGET2GO"
    ]


def test_feedback_pages(repo: Path) -> None:
    output_dir = repo / "pages" / "feedback"
    render_feedback(root=repo, output_dir=output_dir)

    index = (output_dir / "index.html").read_text()
    assert ">1</strong>ontology changes" in index
    assert ">1</strong>proposed new terms" in index
    assert ">1</strong>open source defects" in index
    assert ">1</strong>mapping reviews" in index
    assert ">1</strong>rule reviews" in index
    assert 'href="source-defects/MGI.html"' in index
    assert (
        'href="../projects/WIDGET_OBSOLETION.html">Widget Binding Obsoletion<' in index
    )
    assert 'href="../projects/WIDGET2GO.html">Widget to GO<' in index
    assert 'href="../projects/MAPPING_REVIEWS.html"' in index
    assert "Other<" not in index

    mgi = (output_dir / "source-defects" / "MGI.html").read_text()
    assert "PMID:1101155 → PMID:11011155" in mgi
    assert "Transposed digits in the PMID." in mgi

    requests = (output_dir / "ontology-changes" / "GO-requests.html").read_text()
    assert "GO:0000001" in requests

    terms = (output_dir / "proposed-new-terms.html").read_text()
    assert "widget holdase activity" in terms
    assert (output_dir / "proposed-new-terms.tsv").is_file()
    assert (output_dir / "source-defects.tsv").is_file()


def test_rules_page(repo: Path) -> None:
    page = render_rules(root=repo, output_dir=repo / "pages" / "rules").read_text()
    assert 'href="../../rules/curated/CR-0001.yaml">CR-0001<' in page
    assert "Widgets bind gadgets" in page
    assert "gadget binding" in page
    assert "InterPro:IPR1" in page
    assert "ARBA rule reviews</a> (1)" in page
    assert "Function requirement rules" not in page


def test_cli_renders_hubs(repo: Path) -> None:
    pages_dir = repo / "site"
    result = CliRunner().invoke(
        app, ["render-hubs", "--root", str(repo), "--pages-dir", str(pages_dir)]
    )
    assert result.exit_code == 0, result.output
    assert (pages_dir / "feedback" / "index.html").is_file()
    assert (pages_dir / "rules" / "index.html").is_file()
