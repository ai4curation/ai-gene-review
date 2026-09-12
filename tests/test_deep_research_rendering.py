"""Tests for deep-research HTML rendering helpers."""

from pathlib import Path

from ai_gene_review import render


def test_extract_deep_research_body_strips_frontmatter_and_output_wrapper() -> None:
    text = (
        "---\n"
        "provider: openscientist\n"
        "model: test-model\n"
        "---\n"
        "## Question\n"
        "Research TEST.\n"
        "\n"
        "## Output\n"
        "        # TEST functional review\n"
        "        Evidence body.\n"
    )

    metadata, body = render.extract_deep_research_body(text)

    assert metadata["provider"] == "openscientist"
    assert "## Output" not in body
    assert body.startswith("# TEST functional review")
    assert "Evidence body." in body


def test_rebase_relative_html_urls_preserves_absolute_urls() -> None:
    html = (
        '<img src="artifacts/figure.png">'
        '<a href="https://example.org/report">external</a>'
        '<a href="#section">anchor</a>'
    )

    rebased = render.rebase_relative_html_urls(html, "../genes/human/TEST")

    assert 'src="../genes/human/TEST/artifacts/figure.png"' in rebased
    assert 'href="https://example.org/report"' in rebased
    assert 'href="#section"' in rebased


def test_collect_deep_research_sections_exposes_metadata_and_artifacts(tmp_path: Path) -> None:
    gene_dir = tmp_path / "genes" / "human" / "TEST"
    gene_dir.mkdir(parents=True)
    report = gene_dir / "TEST-deep-research-openscientist.md"
    report.write_text(
        "---\n"
        "provider: openscientist\n"
        "model: os-test\n"
        "citation_count: 3\n"
        "trajectory_id: traj-1\n"
        "artifact_count: 1\n"
        "artifacts:\n"
        "  - filename: evidence.png\n"
        "    path: TEST-deep-research-openscientist_artifacts/evidence.png\n"
        "    media_type: image/png\n"
        "    description: Evidence matrix\n"
        "---\n"
        "## Output\n"
        "# TEST gene evidence\n"
        "![embedded](TEST-deep-research-openscientist_artifacts/evidence.png)\n",
        encoding="utf-8",
    )
    Path(f"{report}.citations.md").write_text("citations\n", encoding="utf-8")

    sections = render.collect_deep_research_sections(gene_dir, output_dir=gene_dir)

    assert len(sections) == 1
    section = sections[0]
    assert section["provider_label"] == "OpenScientist"
    assert section["model"] == "os-test"
    assert section["citation_count"] == 3
    assert section["citations_href"] == "TEST-deep-research-openscientist.md.citations.md"
    assert section["artifacts"][0]["href"] == (
        "TEST-deep-research-openscientist_artifacts/evidence.png"
    )
    assert 'src="TEST-deep-research-openscientist_artifacts/evidence.png"' in section[
        "content"
    ]


def test_collect_deep_research_sections_includes_hypothesis_reports(
    tmp_path: Path,
) -> None:
    gene_dir = tmp_path / "genes" / "SCHPO" / "pmp20"
    report_dir = (
        gene_dir
        / "pmp20-hypotheses"
        / "function-hypothesis-go-0008379"
    )
    report_dir.mkdir(parents=True)
    report = report_dir / "openscientist.md"
    report.write_text(
        "---\n"
        "provider: openscientist\n"
        "model: openscientist-autonomous\n"
        "citation_count: 13\n"
        "artifact_count: 1\n"
        "artifacts:\n"
        "  - filename: final_report.html\n"
        "    path: openscientist_artifacts/final_report.html\n"
        "    media_type: text/html\n"
        "    description: OpenScientist final report\n"
        "---\n"
        "## Output\n"
        "# Final Report: Evaluation of Thioredoxin Peroxidase Activity\n"
        "The GO:0008379 annotation should be removed.\n",
        encoding="utf-8",
    )
    Path(f"{report}.citations.md").write_text("citations\n", encoding="utf-8")

    sections = render.collect_deep_research_sections(gene_dir, output_dir=gene_dir)

    assert len(sections) == 1
    section = sections[0]
    assert section["provider_label"] == "OpenScientist"
    assert section["filename"] == (
        "pmp20-hypotheses/function-hypothesis-go-0008379/openscientist.md"
    )
    assert section["citations_href"] == (
        "pmp20-hypotheses/function-hypothesis-go-0008379/"
        "openscientist.md.citations.md"
    )
    assert section["artifacts"][0]["href"] == (
        "pmp20-hypotheses/function-hypothesis-go-0008379/"
        "openscientist_artifacts/final_report.html"
    )
    assert "GO:0008379 annotation should be removed" in section["content"]
