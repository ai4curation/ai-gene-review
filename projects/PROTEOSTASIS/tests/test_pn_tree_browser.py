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
    )

    node = data["nodes"][pn_code]
    assert data["projection_rows"][0]["uniprot_id"] == "Q9H2V7"
    assert node["existing_iba_gene_count"] == 1
    assert node["existing_iba_annotation_count"] == 1
    assert node["existing_iba_by_gene"][0]["terms"][0]["go_id"] == "GO:0033700"

    html = browser.render_html(data, tmp_path / "pn.html")
    assert "functionome.geneontology.org" in html
    assert "Q9H2V7" in html
