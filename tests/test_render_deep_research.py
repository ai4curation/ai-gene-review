"""Tests for deep-research rendering helpers."""

from ai_gene_review.render import (
    collect_deep_research_sections,
    extract_deep_research_body,
    find_markdown_files,
    render_gene_review,
)


def test_extract_deep_research_body_strips_frontmatter_and_output_prompt():
    text = """---
provider: falcon
model: Edison Scientific Literature
citation_count: 3
---

## Question

# Gene Research for Functional Annotation

Prompt text that should not render.

## Output

Question: You are an expert researcher.

# Gene Research for Functional Annotation

More prompt text that should not render.

## Research Report: TEST1

Curated report body.
"""

    metadata, body = extract_deep_research_body(text)

    assert metadata["provider"] == "falcon"
    assert metadata["citation_count"] == 3
    assert body.startswith("## Research Report: TEST1")
    assert "## Question" not in body
    assert "More prompt text" not in body
    assert "Curated report body." in body


def test_collect_deep_research_sections_rebases_artifact_links(tmp_path):
    gene_dir = tmp_path / "genes" / "human" / "TEST1"
    output_dir = tmp_path / "pages"
    gene_dir.mkdir(parents=True)
    output_dir.mkdir()

    report_path = gene_dir / "TEST1-deep-research-falcon.md"
    report_path.write_text(
        """---
provider: falcon
model: Edison Scientific Literature
citation_count: 7
trajectory_id: abc-123
artifact_count: 1
artifacts:
  - filename: plot.png
    path: TEST1-deep-research-falcon_artifacts/plot.png
    media_type: image/png
    description: Summary plot
---

## Output

# Useful TEST1 Report

![Existing image](TEST1-deep-research-falcon_artifacts/plot.png)
""",
        encoding="utf-8",
    )
    (gene_dir / "TEST1-deep-research-falcon-citations.md").write_text(
        "# Citations\n",
        encoding="utf-8",
    )

    sections = collect_deep_research_sections(gene_dir, output_dir=output_dir)

    assert len(sections) == 1
    section = sections[0]
    assert section["title"] == "Falcon"
    assert section["subtitle"] == "Useful TEST1 Report"
    assert section["model"] == "Edison Scientific Literature"
    assert section["citation_count"] == 7
    assert section["trajectory_id"] == "abc-123"
    assert (
        section["citations_href"]
        == "../genes/human/TEST1/TEST1-deep-research-falcon-citations.md"
    )
    assert (
        section["artifacts"][0]["href"]
        == "../genes/human/TEST1/TEST1-deep-research-falcon_artifacts/plot.png"
    )
    assert (
        'src="../genes/human/TEST1/TEST1-deep-research-falcon_artifacts/plot.png"'
        in section["content"]
    )


def test_find_markdown_files_excludes_deep_research_and_citations(tmp_path):
    gene_dir = tmp_path / "TEST1"
    gene_dir.mkdir()
    (gene_dir / "TEST1-notes.md").write_text("# Notes\n", encoding="utf-8")
    (gene_dir / "TEST1-deep-research-falcon.md").write_text(
        "# Report\n", encoding="utf-8"
    )
    (gene_dir / "TEST1-deep-research-falcon-citations.md").write_text(
        "# Citations\n", encoding="utf-8"
    )

    files = find_markdown_files(gene_dir)

    assert files == [("Notes", gene_dir / "TEST1-notes.md")]


def test_render_gene_review_includes_dedicated_deep_research_section(tmp_path):
    gene_dir = tmp_path / "human" / "TEST1"
    gene_dir.mkdir(parents=True)
    yaml_path = gene_dir / "TEST1-ai-review.yaml"
    yaml_path.write_text(
        """id: UniProtKB:TEST1
gene_symbol: TEST1
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
description: Test gene.
""",
        encoding="utf-8",
    )
    (gene_dir / "TEST1-deep-research-openai.md").write_text(
        """---
provider: openai
model: o3
citation_count: 4
---

## Output

# TEST1 Report

Rendered deep research.
""",
        encoding="utf-8",
    )

    output_path = render_gene_review(yaml_path)
    html = output_path.read_text(encoding="utf-8")

    assert "Deep Research" in html
    assert "OpenAI" in html
    assert "o3" in html
    assert "4 citations" in html
    assert "Rendered deep research." in html
    assert "## Output" not in html
