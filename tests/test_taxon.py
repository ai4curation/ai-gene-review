"""Tests for NCBITaxon helpers used to fill the bound ``taxon`` slot."""

from pathlib import Path

import pytest

from ai_gene_review.taxon import (
    is_ncbitaxon_curie,
    ncbitaxon_label,
    ncbitaxon_term,
    review_taxon,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("NCBITaxon:3055", True),
        ("NCBITaxon:9606", True),
        ("NCBITaxon:DESVH", False),
        ("uniprot:ARATH", False),
        ("9606", False),
        (9606, False),
        (None, False),
    ],
)
def test_is_ncbitaxon_curie(value, expected):
    assert is_ncbitaxon_curie(value) is expected


def test_review_taxon_reads_gene_review(tmp_path: Path):
    review = tmp_path / "BRI1-ai-review.yaml"
    review.write_text(
        "id: O22476\ngene_symbol: BRI1\ntaxon:\n  id: NCBITaxon:3702\n  label: Arabidopsis thaliana\n"
    )
    assert review_taxon(review) == {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"}


@pytest.mark.parametrize(
    "taxon_yaml",
    [
        "taxon:\n  id: uniprot:ARATH\n  label: ARATH\n",
        "taxon:\n  id: NCBITaxon:DESVH\n  label: Desvh\n",
        "taxon:\n  id: NCBITaxon:3702\n",
        "",
    ],
)
def test_review_taxon_rejects_non_ncbitaxon(tmp_path: Path, taxon_yaml: str):
    review = tmp_path / "X-ai-review.yaml"
    review.write_text("id: P1\ngene_symbol: X\n" + taxon_yaml)
    with pytest.raises(ValueError):
        review_taxon(review)


def test_review_taxon_missing_file(tmp_path: Path):
    with pytest.raises(ValueError):
        review_taxon(tmp_path / "missing-ai-review.yaml")


def test_ncbitaxon_label_rejects_malformed_curie():
    with pytest.raises(ValueError):
        ncbitaxon_label("NCBITaxon:CHLRE")


@pytest.mark.integration
def test_ncbitaxon_term_resolves_label():
    assert ncbitaxon_term(3055) == {"id": "NCBITaxon:3055", "label": "Chlamydomonas reinhardtii"}


def test_resolve_taxon_term_prefers_uniprot_ox_line():
    from ai_gene_review.etl.gene import resolve_taxon_term

    assert resolve_taxon_term("CHLRE", "ID   X\nOX   NCBI_TaxID=9606;\n//") == {
        "id": "NCBITaxon:9606",
        "label": "Homo sapiens",
    }


def test_resolve_taxon_term_refuses_placeholder():
    """An organism with no OX line, no table entry and no code form must not yield NCBITaxon:<name>."""
    from ai_gene_review.etl.gene import resolve_taxon_term

    with pytest.raises(ValueError):
        resolve_taxon_term("unknown-organism")


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "src/ai_gene_review/schema/gene_review.yaml"


def _term_validate_offline(path: Path):
    """Run linkml-term-validator on ``path`` against the committed caches only."""
    import subprocess

    return subprocess.run(
        [
            "uv", "run", "linkml-term-validator", "validate-data", str(path),
            "-s", str(SCHEMA), "-t", "GeneReview", "--labels",
            "-c", str(REPO_ROOT / "conf/oak_config.yaml"), "--offline",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize(
    "fixture,expected",
    [
        ("GeneReview-placeholder_taxon_id.yaml", "NCBITaxon:DESVH"),
        ("GeneReview-taxon_label_mismatch.yaml", "Label mismatch for 'NCBITaxon:3055'"),
    ],
)
def test_taxon_binding_rejects_invalid_fixture(fixture: str, expected: str):
    """The NCBITaxonEnum binding rejects a placeholder id and a wrong label."""
    result = _term_validate_offline(REPO_ROOT / "tests/data/invalid" / fixture)
    assert result.returncode != 0
    assert expected in result.stdout + result.stderr


def test_taxon_binding_accepts_valid_fixture():
    result = _term_validate_offline(REPO_ROOT / "tests/data/valid/GeneReview-minimal.yaml")
    assert result.returncode == 0, result.stdout + result.stderr
