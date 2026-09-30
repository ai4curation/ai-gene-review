"""Tests for Reactome pathway cache serialization."""

import re

from ai_gene_review.etl.reactome import ReactomePathway


def test_reactome_markdown_strips_trailing_line_whitespace():
    """Reactome API text should produce Git-clean pathway cache files."""
    pathway = ReactomePathway(
        stable_id="R-HSA-123456",
        display_name="Test pathway",
        species="Homo sapiens",
        summary="First summary line.  \nSecond line.\t\n  Indented text stays indented. \r\n",
    )

    markdown = pathway.to_markdown()

    assert not re.search(r"[ \t]+(?=\r?\n|\r?$)", markdown)
    assert "\n  Indented text stays indented.\r\n" in markdown
