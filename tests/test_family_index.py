"""Family catalog coverage, provenance, and project-render integration."""

from pathlib import Path

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
        "---\ntitle: Protein Families\nautolink_gene_symbols: false\n---\nBrowse families.\n"
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
