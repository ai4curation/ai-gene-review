"""Family catalog coverage, provenance, and project-render integration."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.family_index import collect_family_reviews
from ai_gene_review.render_projects import render_project


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data))


def test_catalog_merges_reports_and_preserves_unresolved_scope(tmp_path):
    folder = tmp_path / "interpro/panther/PTHR1"
    write_yaml(
        folder / "PTHR1-review.yaml",
        {
            "family_id": "PANTHER:PTHR1",
            "family_name": "Official name",
            "preferred_name": "Readable name",
            "summary": "A family summary",
            "review_status": "COMPLETE",
            "functional_coherence": "HETEROGENEOUS",
            "term_assessments": [
                {
                    "assessed_term": {"id": "GO:1", "label": "Test function"},
                    "scope": "UNRESOLVED",
                }
            ],
        },
    )
    (folder / "PTHR1-review.md").write_text("# Report\n")
    (folder / "PTHR1-deep-research-falcon.md").write_text("Research")
    rows = collect_family_reviews(tmp_path)
    assert len(rows) == 1
    row = rows[0]
    assert row["name"] == "Readable name"
    assert row["status"] == "COMPLETE"
    assert row["scopes"] == {"UNRESOLVED": 1}
    assert row["research"] is True
    assert len(row["sources"]) == 2
    assert "Official name" in row["search"] and "GO:1" in row["search"]


def test_catalog_includes_pfam_and_prose_reports_but_not_source_only_entries(
    tmp_path,
):
    write_yaml(
        tmp_path / "interpro/pfam/PF1/PF1-review.yaml",
        {
            "pfam_id": "PF1",
            "pfam_name": "Pfam name",
            "pfam_description": "A domain",
            "proposed_annotations": [
                {
                    "term": {"id": "GO:2", "label": "Proposed function"},
                    "status": "PROPOSED",
                }
            ],
        },
    )
    write_yaml(
        tmp_path / "interpro/panther/PTHR2/PTHR2-metadata.yaml",
        {"metadata": {"name": {"name": "Source only"}}},
    )
    folder = tmp_path / "interpro/panther/PTHR3"
    folder.mkdir(parents=True)
    (folder / "PTHR3-review.md").write_text("# Family report\n")
    rows = collect_family_reviews(tmp_path)
    assert {r["id"] for r in rows} == {"PF1", "PTHR3"}
    pfam = next(r for r in rows if r["id"] == "PF1")
    assert pfam["status"] == "NOT_RECORDED"
    assert pfam["scopes"] == {}
    assert "Proposed function" in pfam["search"]


def test_project_render_builds_escaped_searchable_catalog(tmp_path):
    projects = tmp_path / "projects"
    projects.mkdir()
    source = projects / "FAMILIES.md"
    source.write_text(
        "---\ntitle: Protein Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\nBrowse families.\n"
    )
    write_yaml(
        tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml",
        {
            "family_id": "PANTHER:PTHR1",
            "family_name": '<script>alert("x")</script>',
            "summary": "Example",
            "review_status": "COMPLETE",
        },
    )
    output, warnings = render_project(
        source, tmp_path / "pages/projects", tmp_path / "genes"
    )
    html = output.read_text()
    assert 'id="family-search"' in html
    assert 'id="family-table"' in html
    assert "&lt;script&gt;" in html
    assert '<script>alert("x")</script>' not in html
    assert "Browse families." in html
    assert not warnings


@pytest.mark.parametrize("content", ["", "# Review not started yet\n"])
def test_empty_review_yaml_renders_as_unrecorded(tmp_path, content):
    """Scaffolded YAML must not break the family catalog or project build."""
    folder = tmp_path / "interpro/panther/PTHR1"
    folder.mkdir(parents=True)
    (folder / "PTHR1-review.yaml").write_text(content)
    projects = tmp_path / "projects"
    projects.mkdir()
    source = projects / "FAMILIES.md"
    source.write_text(
        "---\ntitle: Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\n"
    )
    rows = collect_family_reviews(tmp_path)
    assert len(rows) == 1
    assert rows[0]["status"] == "NOT_RECORDED"
    assert rows[0]["coherence"] == "NOT_RECORDED"
    assert rows[0]["terms"] == 0
    output, warnings = render_project(
        source, tmp_path / "pages/projects", tmp_path / "genes"
    )
    assert "PTHR1" in output.read_text()
    assert not warnings


def test_pfam_mapping_assessment_is_distinct_from_coherence(tmp_path):
    write_yaml(
        tmp_path / "interpro/pfam/PF1/PF1-review.yaml",
        {
            "pfam_id": "PF1",
            "pfam_name": "Example",
            "interpro": {
                "id": "InterPro:IPR1",
                "go_status": "ABSENT",
                "mapping_viability": "NOT_VIABLE",
                "viability_reason": "Mixed catalytic members",
            },
        },
    )
    row = collect_family_reviews(tmp_path)[0]
    assert row["mapping_viability"] == "NOT_VIABLE"
    assert row["go_status"] == "ABSENT"
    assert row["viability_reason"] == "Mixed catalytic members"
    assert row["coherence"] == "NOT_RECORDED"


def test_catalog_source_links_support_preview_revision(tmp_path):
    write_yaml(tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml", {})
    row = collect_family_reviews(tmp_path, source_ref="feature/catalog")[0]
    assert "/blob/feature%2Fcatalog/" in row["sources"][0]["url"]


@pytest.mark.parametrize("relative", ["CATALOG.md", "nested/CATALOG.md"])
def test_family_template_frontmatter_works_for_renamed_and_relative_paths(
    tmp_path, monkeypatch, relative
):
    projects = tmp_path / "projects"
    source = projects / relative
    source.parent.mkdir(parents=True)
    source.write_text(
        "---\ntitle: Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\n"
    )
    write_yaml(
        tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml",
        {"family_name": "Example"},
    )
    monkeypatch.chdir(projects)
    output, _ = render_project(
        Path(relative),
        tmp_path / "pages/projects",
        tmp_path / "genes",
        projects_dir=projects,
    )
    assert 'id="family-table"' in output.read_text()
    assert "PTHR1" in output.read_text()


def test_unknown_project_template_fails_explicitly(tmp_path):
    source = tmp_path / "project.md"
    source.write_text("---\ntitle: Catalog\ntemplate: family_typo\n---\n")
    with pytest.raises(ValueError, match="Unknown project template"):
        render_project(source, tmp_path / "out", tmp_path / "genes")


def test_preview_revision_applies_to_catalog_related_links_and_footer(
    tmp_path, monkeypatch
):
    projects = tmp_path / "projects"
    projects.mkdir()
    source = projects / "FAMILIES.md"
    source.write_text(
        "---\ntitle: Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\n"
        "[Report](https://github.com/ai4curation/ai-gene-review/tree/main/reports)\n"
    )
    write_yaml(tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml", {})
    monkeypatch.setenv("AI_GENE_REVIEW_SOURCE_REF", "feature/catalog")
    output, _ = render_project(
        source,
        tmp_path / "pages/projects",
        tmp_path / "genes",
        source_ref="feature/catalog",
    )
    html = output.read_text()
    assert "/blob/feature%2Fcatalog/interpro/" in html
    assert "/tree/feature%2Fcatalog/reports" in html

    assert '/tree/feature%2Fcatalog/interpro"' in html
    output, _ = render_project(source, tmp_path / "production", tmp_path / "genes")
    assert '/tree/main/interpro"' in output.read_text()


@pytest.mark.parametrize("render_all", [False, True])
def test_cli_threads_source_ref_through_project_rendering(
    tmp_path, monkeypatch, render_all
):
    from typer.testing import CliRunner
    from ai_gene_review.cli import app

    projects = tmp_path / "projects"
    projects.mkdir()
    (projects / "FAMILIES.md").write_text(
        "---\ntitle: Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\n"
    )
    write_yaml(tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml", {})
    monkeypatch.chdir(tmp_path)
    args = ["render-projects", "--source-ref", "feature/catalog"]
    args += ["--all"] if render_all else ["projects/FAMILIES.md"]
    result = CliRunner().invoke(app, args)
    assert result.exit_code == 0, result.output
    html = (tmp_path / "pages/projects/FAMILIES.html").read_text()
    assert "/blob/feature%2Fcatalog/interpro/" in html
    assert '/tree/feature%2Fcatalog/interpro"' in html


def test_mapping_filter_options_come_only_from_pfam(tmp_path):
    projects = tmp_path / "projects"
    projects.mkdir()
    source = projects / "FAMILIES.md"
    source.write_text(
        "---\ntitle: Families\ntemplate: family_index\nautolink_gene_symbols: false\n---\n"
    )
    write_yaml(tmp_path / "interpro/panther/PTHR1/PTHR1-review.yaml", {})
    write_yaml(
        tmp_path / "interpro/pfam/PF1/PF1-review.yaml",
        {"pfam_id": "PF1", "interpro": {"mapping_viability": "NOT_VIABLE"}},
    )
    output, _ = render_project(source, tmp_path / "pages/projects", tmp_path / "genes")
    options = (
        output.read_text()
        .split('id="filter-mapping_viability"', 1)[1]
        .split("</select>", 1)[0]
    )
    assert 'value="NOT_VIABLE"' in options
    assert 'value="NOT_RECORDED"' not in options
