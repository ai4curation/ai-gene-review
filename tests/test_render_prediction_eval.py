from bs4 import BeautifulSoup
from pathlib import Path
import subprocess
import sys

import yaml

from ai_gene_review.render_prediction_eval import compute_stats, render_prediction_eval


def test_render_prediction_eval_has_no_trailing_whitespace():
    html = render_prediction_eval(
        [
            {
                "id": "P0A6Y8",
                "gene_symbol": "DnaK",
                "taxon": {"label": "Escherichia coli"},
                "predictions": [],
            }
        ]
    )

    assert html.endswith("\n")
    assert all(line == line.rstrip() for line in html.splitlines())


def test_empty_prediction_evaluation_shows_summary_without_score():
    """An assessed absence has a summary but no VDCL prediction or score."""
    proteins = [
        {
            "id": "P0A6Y8",
            "gene_symbol": "DnaK",
            "taxon": {"label": "Escherichia coli"},
            "status": "COMPLETE",
            "description": "No GO predictions despite established chaperone activity.",
            "predictions": [],
        }
    ]
    soup = BeautifulSoup(render_prediction_eval(proteins), "html.parser")
    row = soup.select_one(".no-pred-row")
    assert row is not None
    assert "No GO/EC predictions in the reviewed source" in row.get_text()
    assert proteins[0]["description"] in row.get_text()
    assert len(row.select("td")) == 8
    assert row.select("td")[4].get_text(strip=True) == ""
    assert row.select("td")[5].get_text(strip=True) == ""
    stats = compute_stats(proteins)
    assert stats["total_predictions"] == 0
    assert not any(stats["counts"].values())
    mean_stat = next(
        stat for stat in soup.select(".summary-stat") if "Mean CS" in stat.get_text()
    )
    assert mean_stat.select_one(".value").get_text() == "N/A"


def test_default_cli_discovers_review_sidecars_across_species(tmp_path: Path) -> None:
    """The default glob reaches species/gene directories, including empty reviews."""
    for species, gene in (("DROME", "Dic4"), ("WHEAT", "A0A3B6GK97")):
        gene_dir = tmp_path / "genes" / species / gene
        gene_dir.mkdir(parents=True)
        (gene_dir / f"{gene}-protnlm-predictions-review.yaml").write_text(
            yaml.safe_dump({
                "id": gene, "gene_symbol": gene, "taxon": {"label": species},
                "status": "COMPLETE", "description": "Reviewed absence of GO output.",
                "predictions": [],
            })
        )
    output = tmp_path / "eval.html"
    result = subprocess.run(
        [sys.executable, "-m", "ai_gene_review.render_prediction_eval",
         "--root", str(tmp_path), "-o", str(output)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    soup = BeautifulSoup(output.read_text(), "html.parser")
    assert len(soup.select(".no-pred-row")) == 2
    assert "DROME" in soup.get_text()
    assert "WHEAT" in soup.get_text()
