"""Tests for the gene ETL module."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import requests
import yaml
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


@patch("ai_gene_review.etl.gene.fetch_goa_data")
@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
def test_accession_fetch_records_uniprot_gene_name(mock_fetch_uniprot, mock_fetch_goa, tmp_path):
    """Fetching an alt-ORF peptide by accession records its host gene symbol.

    Alternative-ORF peptides live in ``<HOST>__<ACC>`` folders; the stub's
    gene_symbol should be UniProt's gene name, not the accession or folder name.
    """
    mock_fetch_uniprot.return_value = (
        "ID   ALTMF_HUMAN Reviewed; 70 AA.\n"
        "AC   L0R8F8;\n"
        "GN   Name=MIEF1 {ECO:0000312|HGNC:HGNC:25979};\n"
        "OS   Homo sapiens (Human).\n"
    )
    mock_fetch_goa.return_value = "GO TERM\tGO NAME\n"

    fetch_gene_data(
        ("human", "L0R8F8"),
        uniprot_id="L0R8F8",
        base_path=tmp_path,
        alias="MIEF1__L0R8F8",
        fetch_titles=False,
    )

    review = yaml.safe_load(
        (tmp_path / "genes" / "human" / "MIEF1__L0R8F8" / "MIEF1__L0R8F8-ai-review.yaml").read_text()
    )
    assert review["id"] == "L0R8F8"
    assert review["gene_symbol"] == "MIEF1"


# ---------------------------------------------------------------------------
# GOA JSON -> TSV conversion and taxon-name backfill
# ---------------------------------------------------------------------------

from ai_gene_review.etl.gene import (  # noqa: E402
    GOA_TSV_HEADER,
    _goa_results_to_tsv,
    _resolve_taxon_name,
)


def test_goa_empty_results_is_header_only():
    """No annotations yields the header row only (the demerged-accession case)."""
    out = _goa_results_to_tsv([])
    assert out == GOA_TSV_HEADER + "\n"


def test_goa_taxon_name_backfilled_from_taxon_id():
    """TAXON NAME is backfilled from taxonId when QuickGO omits taxonName.

    QuickGO's includeFields=taxonName path returns HTTP 500, so results arrive
    without a taxonName; the human taxon id must still resolve to 'Homo sapiens'.
    """
    results = [
        {
            "geneProductId": "UniProtKB:P12345",
            "symbol": "SLC26A2",
            "qualifier": "enables",
            "goId": "GO:0015116",
            "goName": "sulfate transmembrane transporter activity",
            "goAspect": "molecular_function",
            "evidenceCode": "ECO:0000501",
            "goEvidence": "IEA",
            "reference": "GO_REF:0000002",
            "taxonId": 9606,  # no taxonName supplied
            "assignedBy": "InterPro",
            "name": "Sulfate transporter",
            "date": "20240101",
        }
    ]
    lines = _goa_results_to_tsv(results).splitlines()
    assert lines[0] == GOA_TSV_HEADER
    cols = lines[1].split("\t")
    assert cols[0] == "UniProtKB"  # GENE PRODUCT DB
    assert cols[1] == "P12345"  # GENE PRODUCT ID
    assert cols[4] == "GO:0015116"  # GO TERM
    assert cols[5] == "sulfate transmembrane transporter activity"  # GO NAME
    assert cols[11] == "9606"  # TAXON ID
    assert cols[12] == "Homo sapiens"  # TAXON NAME (backfilled)
    assert cols[14] == "Sulfate transporter"  # GENE NAME


def test_goa_existing_taxon_name_is_preserved():
    """A taxonName already supplied by QuickGO is used verbatim, not overwritten."""
    results = [
        {"geneProductId": "UniProtKB:P1", "goId": "GO:1", "taxonId": 9606,
         "taxonName": "Homo sapiens (custom)"},
    ]
    cols = _goa_results_to_tsv(results).splitlines()[1].split("\t")
    assert cols[12] == "Homo sapiens (custom)"


def test_goa_rows_deduplicated_after_projection():
    """Rows identical after projection (e.g. differing only in extensions) collapse."""
    base = {"geneProductId": "UniProtKB:P1", "goId": "GO:1", "taxonId": 9606,
            "goEvidence": "IDA"}
    results = [dict(base, extensions=["a"]), dict(base, extensions=["b"])]
    body = [ln for ln in _goa_results_to_tsv(results).splitlines()[1:]]
    assert len(body) == 1


def test_resolve_taxon_name_human_offline():
    assert _resolve_taxon_name("9606") == "Homo sapiens"


def test_resolve_taxon_name_strain_level_offline():
    """TAXON NAME must be QuickGO's UniProt-style name (with strain), not the
    NCBITaxon label. 559292 resolves offline and must carry the strain qualifier
    exactly as QuickGO (and the committed genes/yeast/*-goa.tsv) spell it."""
    assert (
        _resolve_taxon_name("559292")
        == "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    )


def test_resolve_taxon_name_blank_for_nonnumeric():
    assert _resolve_taxon_name("") == ""
    assert _resolve_taxon_name("notanid") == ""


# ---------------------------------------------------------------------------
# GOA fetch control flow: retry-on-500, fail-loud, shortfall guard
# ---------------------------------------------------------------------------

import requests as _requests  # noqa: E402
from unittest.mock import Mock as _Mock  # noqa: E402
from ai_gene_review.etl.gene import fetch_goa_data  # noqa: E402


def _ok_response(rows, number_of_hits=None):
    resp = _Mock()
    resp.raise_for_status.return_value = None
    resp.json.return_value = {
        "results": rows,
        "numberOfHits": len(rows) if number_of_hits is None else number_of_hits,
    }
    return resp


def _error_response(status_code):
    resp = _Mock()
    err = _requests.exceptions.HTTPError()
    err.response = _Mock(status_code=status_code)
    resp.raise_for_status.side_effect = err
    return resp


def _include_fields(call):
    return [v for (k, v) in call.kwargs["params"] if k == "includeFields"]


def test_goa_fetch_omits_unreliable_taxonname_field():
    """Do not request QuickGO's unreliable taxonName display field.

    TAXON NAME is backfilled from taxonId instead.
    """
    row = {"geneProductId": "UniProtKB:P1", "goId": "GO:1", "taxonId": 9606}
    with patch(
        "ai_gene_review.etl.gene.requests.get",
        return_value=_ok_response([row]),
    ) as mget:
        tsv = fetch_goa_data("P1")
    assert "goName" in _include_fields(mget.call_args)
    assert "name" in _include_fields(mget.call_args)
    assert "taxonName" not in _include_fields(mget.call_args)
    assert tsv.splitlines()[1].split("\t")[12] == "Homo sapiens"  # backfilled


def test_goa_fetch_raises_on_page1_failure_not_taxonname():
    """A non-taxonName error that exhausts the transient retries raises rather
    than silently returning a header-only GOA."""
    with (
        patch(
            "ai_gene_review.etl.gene.requests.get",
            return_value=_error_response(503),
        ),
        patch("ai_gene_review.etl.gene.time.sleep"),
    ):
        with pytest.raises(ValueError):
            fetch_goa_data("P1")


def test_goa_fetch_raises_on_short_read():
    """Fewer annotations than numberOfHits raises rather than writing a truncated
    GOA file."""
    row = {
        "geneProductId": "UniProtKB:P1",
        "goId": "GO:1",
        "taxonId": 9606,
        "taxonName": "Homo sapiens",
    }
    with patch(
        "ai_gene_review.etl.gene.requests.get",
        return_value=_ok_response([row], number_of_hits=5),
    ):
        with pytest.raises(ValueError):
            fetch_goa_data("P1")


# ---------------------------------------------------------------------------
# Fail loudly on a persistent QuickGO outage (from #6488). A persistent outage
# must raise rather than write an empty or truncated GOA file.
# ---------------------------------------------------------------------------


class _FailingResponse:
    """A QuickGO response that fails the way the service did on 2026-11-17."""

    status_code = 500

    def raise_for_status(self) -> None:
        err = requests.exceptions.HTTPError("500 Server Error")
        err.response = self  # carry the status so the 500 is recognised
        raise err


def test_fetch_goa_data_raises_on_persistent_quickgo_error(monkeypatch):
    """A persistent QuickGO error (every page) must raise rather than come back
    as an empty or truncated GOA table."""
    from ai_gene_review.etl import gene

    monkeypatch.setattr(gene.requests, "get", lambda *a, **k: _FailingResponse())
    monkeypatch.setattr(gene.time, "sleep", lambda *a, **k: None)
    with pytest.raises(ValueError, match="QuickGO"):
        gene.fetch_goa_data("P00000")


@patch("ai_gene_review.etl.gene.fetch_uniprot_data")
def test_fetch_gene_data_keeps_existing_goa_file_when_quickgo_errors(
    mock_fetch_uniprot, monkeypatch, tmp_path
):
    """Re-fetching during a QuickGO outage must not blank an existing GOA file."""
    from ai_gene_review.etl import gene

    gene_dir = tmp_path / "genes" / "SCHPO" / "dca7"
    gene_dir.mkdir(parents=True)
    (gene_dir / "dca7-ai-review.yaml").write_text("id: O74763\ngene_symbol: dca7\n")
    goa_file = gene_dir / "dca7-goa.tsv"
    goa_file.write_text("GO TERM\tGO NAME\nGO:0005634\tnucleus\n")
    mock_fetch_uniprot.return_value = (
        "ID   DCA7_SCHPO Reviewed; 500 AA.\nAC   O74763;\nOS   Schizosaccharomyces pombe.\n"
    )
    monkeypatch.setattr(gene.requests, "get", lambda *a, **k: _FailingResponse())
    monkeypatch.setattr(gene.time, "sleep", lambda *a, **k: None)

    with pytest.raises(ValueError, match="QuickGO"):
        fetch_gene_data(("SCHPO", "dca7"), base_path=tmp_path, seed_annotations=False)
    assert goa_file.read_text() == "GO TERM\tGO NAME\nGO:0005634\tnucleus\n"


def _full_first_page():
    row = {
        "geneProductId": "UniProtKB:P0",
        "goId": "GO:1",
        "taxonId": 9606,
        "taxonName": "Homo sapiens",
    }
    resp = _Mock()
    resp.raise_for_status.return_value = None
    resp.json.return_value = {"results": [row] * 200, "numberOfHits": 400}
    return resp


def _is_later_page(kwargs):
    return any(k == "page" for (k, _) in kwargs.get("params", []))


def test_fetch_goa_data_raises_on_persistent_mid_pagination_error(monkeypatch):
    """Page 1 succeeds but page >= 2 fails on every attempt -> raise, never a
    truncated GOA (the mid-pagination case #6488's parametrize used to cover)."""
    from ai_gene_review.etl import gene

    def fake_get(*args, **kwargs):
        return _error_response(500) if _is_later_page(kwargs) else _full_first_page()

    monkeypatch.setattr(gene.requests, "get", fake_get)
    monkeypatch.setattr(gene.time, "sleep", lambda *a, **k: None)
    with pytest.raises(ValueError, match="QuickGO"):
        gene.fetch_goa_data("P0")


def test_fetch_goa_data_raises_on_short_read_across_pages(monkeypatch):
    """A trailing page reporting no results and numberOfHits:0 must not disarm the
    shortfall guard set by page 1 (expected_total is kept as the running max)."""
    from ai_gene_review.etl import gene

    def _empty_last_page():
        resp = _Mock()
        resp.raise_for_status.return_value = None
        resp.json.return_value = {"results": [], "numberOfHits": 0}
        return resp

    def fake_get(*args, **kwargs):
        return _empty_last_page() if _is_later_page(kwargs) else _full_first_page()

    monkeypatch.setattr(gene.requests, "get", fake_get)
    with pytest.raises(ValueError, match="Incomplete"):
        gene.fetch_goa_data("P0")
