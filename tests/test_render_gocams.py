"""Tests for rendering GO-CAM reviews to HTML pages and an index."""

from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.render_gocams import (
    iter_review_files,
    modules_by_model,
    render_all_gocams,
)

MODEL = "aaaaaaaa00000001"

REVIEW = {
    "model": f"gomodel:{MODEL}",
    "title": "Example kinase cascade (C. elegans)",
    "taxon": "NCBITaxon:6239",
    "status": "COMPLETE",
    "summary": "A linear kinase chain.",
    "activity_reviews": [
        {
            "activity_id": f"gomodel:{MODEL}/a1",
            "gene_product": "WB:WBGene00000001",
            "molecular_function": "GO:0004707",
            "verdict": "OK",
            "consistency": "CONSISTENT",
            "gene_review": "file:worm/kin-1/kin-1-ai-review.yaml",
        },
        {
            "activity_id": f"gomodel:{MODEL}/a2",
            "gene_product": "WB:WBGene00000002",
            "molecular_function": "GO:0005515",
            "verdict": "WRONG",
            "consistency": "CONFLICT",
            "qc_flags": ["BARE_PROTEIN_BINDING"],
            "source_defects": [
                {
                    "defect_type": "WRONG_REFERENCE",
                    "resource": "GO_CAM",
                    "asserted_value": "PMID:1",
                    "explanation": "The cited paper is about another gene.",
                }
            ],
        },
    ],
}

SRC = {
    "id": f"gomodel:{MODEL}",
    "objects": [
        {"id": "WB:WBGene00000001", "label": "kin-1 Cele"},
        {"id": "GO:0004707", "label": "MAP kinase activity"},
    ],
}


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repository with one reviewed model, one gene review and one module."""
    model_dir = tmp_path / "gocams" / MODEL
    model_dir.mkdir(parents=True)
    (model_dir / f"{MODEL}-review.yaml").write_text(yaml.safe_dump(REVIEW))
    (model_dir / f"{MODEL}-src.yaml").write_text(yaml.safe_dump(SRC))
    # An unreviewed cached model counts towards the total but gets no page.
    (tmp_path / "gocams" / "bbbbbbbb00000002").mkdir()
    gene_dir = tmp_path / "genes" / "worm" / "kin-1"
    gene_dir.mkdir(parents=True)
    (gene_dir / "kin-1-ai-review.yaml").write_text("id: X\n")
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    (modules_dir / "kinase_cascade.yaml").write_text(
        f"id: MODULE:kinase_cascade\ntitle: Kinase cascade module\n"
        f"notes: grounded in gomodel:{MODEL}\n"
    )
    (modules_dir / "unrelated.yaml").write_text("id: MODULE:unrelated\ntitle: Other\n")
    return tmp_path


def _render(repo: Path) -> Path:
    output_dir = repo / "pages" / "gocams"
    render_all_gocams(
        gocams_dir=repo / "gocams",
        output_dir=output_dir,
        genes_dir=repo / "genes",
        modules_dir=repo / "modules",
        pages_modules_dir=repo / "pages" / "modules",
    )
    return output_dir


def test_review_page_shows_labels_verdicts_and_links(repo: Path) -> None:
    page = (_render(repo) / f"{MODEL}.html").read_text()
    assert "Example kinase cascade (C. elegans)" in page
    assert "MAP kinase activity" in page
    assert "kin-1 Cele" in page
    # An id with no label in the cached model still appears.
    assert "WB:WBGene00000002" in page
    assert "1 OK" in page and "1 wrong" in page
    assert "BARE_PROTEIN_BINDING" in page
    assert 'href="../../genes/worm/kin-1/kin-1-ai-review.html"' in page
    assert 'href="../modules/kinase_cascade.html">Kinase cascade module<' in page
    assert "Unrelated" not in page and "Other</a>" not in page
    assert "The cited paper is about another gene." in page
    assert f'href="https://model.geneontology.org/{MODEL}"' in page


def test_index_lists_reviewed_models_with_totals(repo: Path) -> None:
    index = (_render(repo) / "index.html").read_text()
    assert f'href="{MODEL}.html"' in index
    assert "1 of 2 cached models have been reviewed" in index
    assert ">1</strong>source defects reported" in index


def test_stale_pages_are_removed(repo: Path) -> None:
    output_dir = repo / "pages" / "gocams"
    output_dir.mkdir(parents=True)
    (output_dir / "deleted0000000000.html").write_text("old")
    _render(repo)
    assert sorted(p.name for p in output_dir.glob("*.html")) == [
        f"{MODEL}.html",
        "index.html",
    ]


def test_iter_review_files_ignores_mismatched_names(repo: Path) -> None:
    (repo / "gocams" / MODEL / "other-review.yaml").write_text("model: x\n")
    assert [p.name for p in iter_review_files(repo / "gocams")] == [
        f"{MODEL}-review.yaml"
    ]


def test_modules_by_model(repo: Path) -> None:
    index = modules_by_model(repo / "modules")
    assert [p.name for p in index[MODEL]] == ["kinase_cascade.yaml"]


def test_cli_renders_pages(repo: Path) -> None:
    output_dir = repo / "out"
    result = CliRunner().invoke(
        app,
        [
            "render-gocams",
            "--gocams-dir",
            str(repo / "gocams"),
            "--genes-dir",
            str(repo / "genes"),
            "--modules-dir",
            str(repo / "modules"),
            "--output-dir",
            str(output_dir),
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Rendered 1 GO-CAM review page(s)" in result.output
    assert (output_dir / f"{MODEL}.html").is_file()
    assert (output_dir / "index.html").is_file()
