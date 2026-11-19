"""Tests for Reactome pathway cache serialization."""

import re

from ai_gene_review.etl import reactome
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


def test_forced_recache_keeps_an_existing_participants_section(tmp_path, monkeypatch):
    """Re-downloading an entry must not drop the participants reviews quote."""
    calls = []

    def fake_fetch(
        reactome_id, use_cache=True, cache_dir=None, include_participants=False
    ):
        calls.append(include_participants)
        return ReactomePathway(
            stable_id=reactome_id,
            display_name="Event",
            participants=["UniProt:P11346 Raf"] if include_participants else [],
        )

    monkeypatch.setattr(reactome, "fetch_reactome_data", fake_fetch)

    # A fresh entry is cached without participants unless asked for.
    assert reactome.cache_reactome_pathway("R-DME-1", output_dir=tmp_path)
    assert "## Participants" not in (tmp_path / "R-DME-1.md").read_text()

    # An entry that has the section keeps it on a forced re-download.
    (tmp_path / "R-DME-2.md").write_text(
        "# Event\n\n## Participants\n\n- UniProt:P11346 Raf\n"
    )
    assert reactome.cache_reactome_pathway("R-DME-2", output_dir=tmp_path, force=True)
    assert "- UniProt:P11346 Raf" in (tmp_path / "R-DME-2.md").read_text()
    assert calls == [False, True]
