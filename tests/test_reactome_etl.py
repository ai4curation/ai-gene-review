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


def test_reactome_markdown_lists_participants_when_given():
    """A participants section makes "is X a participant?" checkable offline."""
    pathway = ReactomePathway(
        stable_id="R-DME-432535",
        display_name="TIM is phosphorylated by CK2",
        summary="Timeless (TIM) is phosphorylated by casein kinase II (CK2).",
        participants=["UniProt:P11346 Raf", "UniProt:Q24324 Dsor1"],
    )

    markdown = pathway.to_markdown()

    assert "## Participants" in markdown
    assert "- UniProt:P11346 Raf\n" in markdown
    # Not part of the frontmatter, so cached titles and summaries are unchanged.
    assert "participants" not in markdown.split("---")[1]


def test_reactome_markdown_omits_empty_participants():
    """Entries cached without participants keep their previous form."""
    pathway = ReactomePathway(stable_id="R-HSA-1", display_name="Test", summary="S.")

    assert "## Participants" not in pathway.to_markdown()
