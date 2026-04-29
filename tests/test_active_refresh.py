"""Tests for active review publication refresh."""

import tempfile
from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.publication_refresh import find_active_review_pmids


def test_find_active_review_pmids_in_progress():
    """Should collect PMIDs from IN_PROGRESS reviews."""
    with tempfile.TemporaryDirectory() as tmpdir:
        genes_dir = Path(tmpdir)

        gene_dir = genes_dir / "human" / "TP53"
        gene_dir.mkdir(parents=True)
        review = {
            "id": "P04637",
            "gene_symbol": "TP53",
            "status": "IN_PROGRESS",
            "references": [
                {"id": "PMID:11111"},
                {"id": "PMID:22222"},
            ],
            "existing_annotations": [
                {"term": {"id": "GO:0005515"}, "original_reference_id": "PMID:33333"},
            ],
        }
        review_file = gene_dir / "TP53-ai-review.yaml"
        with open(review_file, "w") as f:
            yaml.dump(review, f)

        result = find_active_review_pmids(genes_dir)

        assert set(result["pmids"]) == {"11111", "22222", "33333"}
        assert len(result["reviews"]) == 1
        assert result["reviews"][0]["gene"] == "TP53"


def test_find_active_review_pmids_draft():
    """Should collect PMIDs from DRAFT reviews."""
    with tempfile.TemporaryDirectory() as tmpdir:
        genes_dir = Path(tmpdir)

        gene_dir = genes_dir / "human" / "BRCA1"
        gene_dir.mkdir(parents=True)
        review = {
            "id": "P38398",
            "gene_symbol": "BRCA1",
            "status": "DRAFT",
            "references": [{"id": "PMID:44444"}],
        }
        with open(gene_dir / "BRCA1-ai-review.yaml", "w") as f:
            yaml.dump(review, f)

        result = find_active_review_pmids(genes_dir)

        assert "44444" in result["pmids"]


def test_find_active_review_pmids_skips_complete():
    """Should NOT collect PMIDs from COMPLETE reviews."""
    with tempfile.TemporaryDirectory() as tmpdir:
        genes_dir = Path(tmpdir)

        gene_dir = genes_dir / "human" / "CDK1"
        gene_dir.mkdir(parents=True)
        review = {
            "id": "P06493",
            "gene_symbol": "CDK1",
            "status": "COMPLETE",
            "references": [{"id": "PMID:55555"}],
        }
        with open(gene_dir / "CDK1-ai-review.yaml", "w") as f:
            yaml.dump(review, f)

        result = find_active_review_pmids(genes_dir)

        assert "55555" not in result["pmids"]
        assert len(result["reviews"]) == 0


def test_find_active_review_pmids_deduplicates():
    """PMIDs shared across reviews should appear only once."""
    with tempfile.TemporaryDirectory() as tmpdir:
        genes_dir = Path(tmpdir)

        for gene in ("A", "B"):
            gene_dir = genes_dir / "human" / gene
            gene_dir.mkdir(parents=True)
            review = {
                "id": f"Q{gene}",
                "gene_symbol": gene,
                "status": "IN_PROGRESS",
                "references": [{"id": "PMID:77777"}],
            }
            with open(gene_dir / f"{gene}-ai-review.yaml", "w") as f:
                yaml.dump(review, f)

        result = find_active_review_pmids(genes_dir)

        assert result["pmids"].count("77777") == 1


@pytest.mark.parametrize("status", ["INITIALIZED", "COMPLETE"])
def test_find_active_review_pmids_excludes_non_active(status):
    """Should exclude INITIALIZED and COMPLETE reviews."""
    with tempfile.TemporaryDirectory() as tmpdir:
        genes_dir = Path(tmpdir)
        gene_dir = genes_dir / "human" / "TEST"
        gene_dir.mkdir(parents=True)
        review = {
            "id": "Q99999",
            "gene_symbol": "TEST",
            "status": status,
            "references": [{"id": "PMID:88888"}],
        }
        with open(gene_dir / "TEST-ai-review.yaml", "w") as f:
            yaml.dump(review, f)

        result = find_active_review_pmids(genes_dir)

        assert len(result["pmids"]) == 0
