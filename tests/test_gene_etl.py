"""Tests for the gene ETL module."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
from ai_gene_review.etl.gene import fetch_gene_data


@pytest.mark.integration
@pytest.mark.parametrize(
    "organism,gene,uniprot_id",
    [
        ("human", "CFAP300", "Q9BRQ4"),
        ("human", "TP53", "P04637"),
        ("human", "BRCA1", "P38398"),
    ],
)
def test_fetch_gene_data_creates_correct_directory_structure(
    organism, gene, uniprot_id
):
    """Test that fetch_gene_data creates the expected directory structure and fetches real data.

    This integration test verifies:
    - Correct directory structure is created
    - UniProt data is fetched and saved
    - GOA data is fetched and saved
    - Files contain expected content
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

        # Call the function with real data
        fetch_gene_data((organism, gene), uniprot_id=uniprot_id, base_path=base_path)

        # Check directory structure
        gene_dir = base_path / "genes" / organism / gene
        assert gene_dir.exists(), f"Directory {gene_dir} was not created"

        # Check UniProt file
        uniprot_file = gene_dir / f"{gene}-uniprot.txt"
        assert uniprot_file.exists(), f"UniProt file {uniprot_file} was not created"

        uniprot_content = uniprot_file.read_text()
        assert len(uniprot_content) > 100, "UniProt file seems too small"
        assert uniprot_id in uniprot_content, (
            f"UniProt ID {uniprot_id} not found in content"
        )

        # Check GOA file
        goa_file = gene_dir / f"{gene}-goa.tsv"
        assert goa_file.exists(), f"GOA file {goa_file} was not created"

        goa_content = goa_file.read_text()
        assert len(goa_content) > 50, "GOA file seems too small"
        # GOA files should have tab-separated headers
        assert "\t" in goa_content, "GOA file should be tab-separated"


@pytest.mark.integration
def test_fetch_gene_data_without_uniprot_id():
    """Test that fetch_gene_data can resolve gene names to UniProt IDs.

    This test uses real UniProt API to resolve gene names.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

        # Call without providing UniProt ID - should resolve automatically
        fetch_gene_data(("human", "CFAP300"), base_path=base_path)

        # Check that files were created
        gene_dir = base_path / "genes" / "human" / "CFAP300"
        assert gene_dir.exists()

        uniprot_file = gene_dir / "CFAP300-uniprot.txt"
        assert uniprot_file.exists()

        # Verify it found the correct UniProt entry
        uniprot_content = uniprot_file.read_text()
        assert "Q9BRQ4" in uniprot_content or "CFAP300" in uniprot_content


@pytest.mark.integration
def test_fetch_gene_data_handles_invalid_gene():
    """Test graceful handling when gene doesn't exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

        # Should raise an exception for non-existent gene
        with pytest.raises(ValueError, match="Could not find.*UniProt ID"):
            fetch_gene_data(("human", "NONEXISTENTGENE12345"), base_path=base_path)


@pytest.mark.integration
def test_fetch_gene_data_handles_invalid_uniprot_id():
    """Test graceful handling when UniProt ID is invalid."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

        # Should raise an exception for invalid UniProt ID
        with pytest.raises(ValueError, match="Failed to fetch UniProt data"):
            fetch_gene_data(
                ("human", "FAKEGENE"), uniprot_id="INVALID123", base_path=base_path
            )


@pytest.mark.integration
@pytest.mark.parametrize(
    "organism,gene",
    [
        ("mouse", "Trp53"),  # Mouse p53
        ("yeast", "CDC28"),  # Yeast cell division control protein
    ],
)
def test_fetch_gene_data_different_organisms(organism, gene):
    """Test fetching genes from different organisms."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

        # This will attempt to resolve the gene name for the organism
        fetch_gene_data((organism, gene), base_path=base_path)

        # Check that files were created
        gene_dir = base_path / "genes" / organism / gene
        assert gene_dir.exists()

        uniprot_file = gene_dir / f"{gene}-uniprot.txt"
        assert uniprot_file.exists()
        assert uniprot_file.read_text()  # Should have content


@patch("ai_gene_review.etl.gene.resolve_gene_to_uniprot")
@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
def test_fetch_gene_data_reuses_existing_review_accession(
    mock_fetch_uniprot, mock_fetch_goa, mock_resolve, tmp_path
):
    """Existing reviews must not depend on a fresh UniProt symbol lookup."""
    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    (gene_dir / "dca7-ai-review.yaml").write_text(
        "id: O74763\ngene_symbol: dca7\n"
    )
    mock_fetch_uniprot.return_value = (
        "ID   DCA7_SCHPO Reviewed; 500 AA.\n"
        "AC   O74763;\n"
        "OS   Schizosaccharomyces pombe.\n"
    )
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("SCHPO", "dca7"),
        base_path=tmp_path,
        seed_annotations=False,
    )

    mock_resolve.assert_not_called()
    mock_fetch_uniprot.assert_called_once_with("O74763")
    mock_fetch_goa.assert_called_once_with("O74763")


@patch("ai_gene_review.etl.gene.resolve_gene_to_uniprot")
@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
def test_explicit_accession_overrides_existing_review_accession(
    mock_fetch_uniprot, mock_fetch_goa, mock_resolve, tmp_path
):
    """An explicit --uniprot-id remains authoritative over the local review."""
    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    (gene_dir / "dca7-ai-review.yaml").write_text(
        "id: O74763\ngene_symbol: dca7\n"
    )
    mock_fetch_uniprot.return_value = (
        "ID   EXPLICIT Reviewed; 100 AA.\n"
        "AC   P12345;\n"
    )
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("SCHPO", "dca7"),
        uniprot_id="P12345",
        base_path=tmp_path,
        seed_annotations=False,
    )

    mock_resolve.assert_not_called()
    mock_fetch_uniprot.assert_called_once_with("P12345")
    mock_fetch_goa.assert_called_once_with("P12345")


@pytest.mark.parametrize(
    "review_content",
    [
        None,
        "gene_symbol: dca7\n",
        "id: '  '\ngene_symbol: dca7\n",
        "id: URS000075D95B_9606\ngene_symbol: XIST\n",
        "id: [\n",
    ],
)
@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
@patch("ai_gene_review.etl.gene.resolve_gene_to_uniprot")
def test_fetch_gene_data_falls_back_when_review_has_no_protein_accession(
    mock_resolve, mock_fetch_uniprot, mock_fetch_goa, review_content, tmp_path
):
    """Missing, invalid, ncRNA, and malformed review IDs use symbol resolution."""
    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    if review_content is not None:
        (gene_dir / "dca7-ai-review.yaml").write_text(review_content)
    mock_resolve.return_value = "P12345"
    mock_fetch_uniprot.return_value = "AC   P12345;\n"
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("SCHPO", "dca7"),
        base_path=tmp_path,
        seed_annotations=False,
    )

    mock_resolve.assert_called_once_with("dca7", "SCHPO")
    mock_fetch_uniprot.assert_called_once_with("P12345")
    mock_fetch_goa.assert_called_once_with("P12345")


@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
@patch("ai_gene_review.etl.gene.resolve_gene_to_uniprot")
def test_stale_review_accession_is_resolved_before_fetching_goa(
    mock_resolve, mock_fetch_uniprot, mock_fetch_goa, tmp_path
):
    """QuickGO must receive the current primary accession, not a stale review ID."""
    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    (gene_dir / "dca7-ai-review.yaml").write_text(
        "id: O74763\ngene_symbol: dca7\n"
    )
    mock_fetch_uniprot.return_value = "AC   P12345; O74763;\n"
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("SCHPO", "dca7"),
        base_path=tmp_path,
        seed_annotations=False,
    )

    mock_resolve.assert_not_called()
    mock_fetch_uniprot.assert_called_once_with("O74763")
    mock_fetch_goa.assert_called_once_with("P12345")


@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
@patch("ai_gene_review.etl.gene.resolve_gene_to_uniprot")
def test_dead_review_accession_falls_back_to_symbol_resolution(
    mock_resolve, mock_fetch_uniprot, mock_fetch_goa, tmp_path
):
    """A deleted review accession must not prevent a self-healing refresh."""
    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    (gene_dir / "dca7-ai-review.yaml").write_text(
        "id: O74763\ngene_symbol: dca7\n"
    )
    mock_resolve.return_value = "P12345"
    mock_fetch_uniprot.side_effect = [
        ValueError("deleted accession"),
        "AC   P12345;\n",
    ]
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("SCHPO", "dca7"),
        base_path=tmp_path,
        seed_annotations=False,
    )

    mock_resolve.assert_called_once_with("dca7", "SCHPO")
    assert [call.args[0] for call in mock_fetch_uniprot.call_args_list] == [
        "O74763",
        "P12345",
    ]
    mock_fetch_goa.assert_called_once_with("P12345")
