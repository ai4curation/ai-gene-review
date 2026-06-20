"""Tests for the Proteostasis Network tree browser renderer."""

from pathlib import Path

from ai_gene_review.tools import render_pn_tree_browser as browser
from ai_gene_review.tools.report_pn_projected_annotations import PNWorkbookRow


def test_tree_browser_embeds_leaf_iba_annotations_and_gene_accessions(
    monkeypatch,
    tmp_path: Path,
) -> None:
    """Leaf-node details should carry existing IBA rows and external-link accessions."""
    pn_code = (
        "Autophagy-Lysosome Pathway|Autophagic lysosome reformation|"
        "Efflux of autophagy products"
    )
    workbook_row = PNWorkbookRow(
        order=1,
        gene_symbol="SPNS1",
        gene_name="spinster homolog 1",
        branch="Autophagy-Lysosome Pathway",
        class_name="Autophagic lysosome reformation",
        group="Efflux of autophagy products",
        type_name="",
        subtype="",
        uniprot_id="Q9H2V7",
        notes="Lysosome efflux permease required for ALR after starvation.",
        references=(
            "Membrane Trafficking in Autophagy - ScienceDirect",
            "Spinster is required for autophagic lysosome reformation and mTOR reactivation following starvation | PNAS",
        ),
    )

    def fake_workbook_context(workbook_path: Path | None, workbook_sheet: str):
        return (
            [workbook_row],
            {"SPNS1": "Q9H2V7"},
            {"SPNS1": "spinster homolog 1"},
            {pn_code: [workbook_row]},
        )

    def fake_iba_annotations(workbook_rows, duckdb_path):
        return {
            ("SPNS1", "Q9H2V7"): [
                {
                    "go_id": "GO:0033700",
                    "go_label": "phospholipid efflux",
                    "aspect": "BP",
                    "references": "GO_REF:0000033",
                }
            ]
        }

    monkeypatch.setattr(browser, "build_workbook_context", fake_workbook_context)
    monkeypatch.setattr(browser, "load_existing_iba_annotations", fake_iba_annotations)
    review_path = tmp_path / "genes" / "human" / "SPNS1" / "SPNS1-ai-review.html"
    review_path.parent.mkdir(parents=True)
    review_path.write_text("<!doctype html><title>SPNS1 review</title>", encoding="utf-8")

    data = browser.build_data(
        coverage_rows=[
            {
                "level": "group",
                "code": pn_code,
                "status": "mapped",
                "curation_files": "",
                "curation_subjects": "",
            }
        ],
        projection_rows=[
            {
                "gene_symbol": "SPNS1",
                "gene_name": "spinster homolog 1",
                "pn_code": pn_code,
                "target_go_id": "GO:0007041",
                "target_go_label": "lysosomal transport",
                "goa_status": "new_to_goa",
                "mapping_scope": "ok_for_propagation_to_go",
                "mapping_subject_code": pn_code,
            }
        ],
        audit_rows=[],
        mapping_dir=tmp_path,
        review_root=tmp_path / "genes",
    )

    node = data["nodes"][pn_code]
    assert data["projection_rows"][0]["uniprot_id"] == "Q9H2V7"
    assert data["projection_rows"][0]["review_path"].endswith(
        "genes/human/SPNS1/SPNS1-ai-review.html"
    )
    assert node["source_evidence_row_count"] == 1
    assert node["source_reference_count"] == 2
    assert node["source_workbook_evidence"][0]["notes"].startswith("Lysosome efflux")
    assert node["existing_iba_gene_count"] == 1
    assert node["existing_iba_annotation_count"] == 1
    assert node["existing_iba_by_gene"][0]["terms"][0]["go_id"] == "GO:0033700"

    html = browser.render_html(data, Path("projects/PROTEOSTASIS/pn.html"))
    assert "Source Workbook Evidence" in html
    assert "Spinster is required for autophagic lysosome reformation" in html
    assert 'const REPO_ROOT_HREF = "../../";' in html
    assert '"review_path":"genes/human/SPNS1/SPNS1-ai-review.html"' in html
    assert ">Review</a>" in html
    assert "functionome.geneontology.org" in html
    assert "Q9H2V7" in html


def test_render_html_targets_served_deploy_path() -> None:
    """Hrefs must resolve from where the page is served, not where it is written.

    The committed page lives at ``projects/PROTEOSTASIS/pn.html`` but is copied
    verbatim into ``pages/projects/PROTEOSTASIS/pn.html`` (one level deeper) for
    deployment. ``served_path`` lets href computation target the deployed depth so
    repo-root links (gene reviews) and the project-page link resolve correctly.
    """
    data = {"root_codes": [], "tree": [], "summary": {}}
    html = browser.render_html(
        data,
        Path("projects/PROTEOSTASIS/pn.html"),
        served_path=Path("pages/projects/PROTEOSTASIS/pn.html"),
    )
    # Repo-root prefix for gene-review links: three levels up from
    # pages/projects/PROTEOSTASIS/ reaches the deployed repo root.
    assert 'const REPO_ROOT_HREF = "../../../";' in html
    # Project page sits beside the PROTEOSTASIS/ folder in pages/projects/.
    assert 'href="../PROTEOSTASIS.html"' in html
    # Report TSVs live in the repo-root projects/ tree, not under pages/.
    assert (
        'href="../../../projects/PROTEOSTASIS/reports/'
        'pn_mapping_coverage/pn_mapping_code_coverage.tsv"' in html
    )
    assert (
        'href="../../../projects/PROTEOSTASIS/reports/'
        'pn_mapping_audit/unusual_propagations.tsv"' in html
    )


def test_render_html_defaults_served_path_to_output_path() -> None:
    """Without served_path, hrefs are computed relative to the output path."""
    data = {"root_codes": [], "tree": [], "summary": {}}
    html = browser.render_html(data, Path("projects/PROTEOSTASIS/pn.html"))
    assert 'const REPO_ROOT_HREF = "../../";' in html
