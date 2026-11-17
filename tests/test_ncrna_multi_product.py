"""One ncRNA review covering several RNAcentral sequences of a gene."""

from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
import requests
import yaml

from ai_gene_review.etl.gene import fetch_goa_data
from ai_gene_review.validation.goa_validator import GOAValidator

HEADER = (
    "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\tECO ID\t"
    "GO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\tGENE NAME\tDATE"
)
MATURE, DUPLICATE, PRECURSOR = "URS0000338542_9606", "URS0000D54CAD_9606", "URS000062749E_9606"


def row(product: str, go_id: str, eco: str, code: str, ref: str) -> str:
    return "\t".join(
        ["RNAcentral", product, "miR-155", "involved_in", go_id, "x", "P", eco, code, ref, "",
         "9606", "Homo sapiens", "BHF-UCL", "hsa-miR-155-5p", "20200101"]
    )


@pytest.fixture
def seeded(tmp_path):
    goa = tmp_path / "MIR155-goa.tsv"
    goa.write_text(
        "\n".join(
            [
                HEADER,
                row(MATURE, "GO:0035195", "ECO:0000314", "IDA", "PMID:1"),
                # the same claim made on the duplicate 5p sequence
                row(DUPLICATE, "GO:0035195", "ECO:0000314", "IDA", "PMID:1"),
                row(DUPLICATE, "GO:0045087", "ECO:0000315", "IMP", "PMID:2"),
                row(PRECURSOR, "GO:0016442", "ECO:0000256", "IEA", "GO_REF:0000115"),
            ]
        )
        + "\n"
    )
    review = tmp_path / "MIR155-ai-review.yaml"
    review.write_text(yaml.safe_dump({"id": MATURE, "gene_symbol": "MIR155", "existing_annotations": []}))
    GOAValidator().seed_missing_annotations(review, goa_file=goa)
    rows = yaml.safe_load(review.read_text())["existing_annotations"]
    return {r["term"]["id"]: r for r in rows}


def test_a_claim_made_on_two_sequences_lists_both(seeded):
    assert seeded["GO:0035195"]["gene_products"] == [MATURE, DUPLICATE]


def test_rows_from_other_sequences_record_their_source(seeded):
    assert seeded["GO:0045087"]["gene_products"] == [DUPLICATE]
    assert seeded["GO:0016442"]["gene_products"] == [PRECURSOR]


def test_single_product_review_is_unchanged(tmp_path):
    goa = tmp_path / "X-goa.tsv"
    goa.write_text(HEADER + "\n" + row(MATURE, "GO:0035195", "ECO:0000314", "IDA", "PMID:1") + "\n")
    review = tmp_path / "X-ai-review.yaml"
    review.write_text(yaml.safe_dump({"id": MATURE, "gene_symbol": "X", "existing_annotations": []}))
    GOAValidator().seed_missing_annotations(review, goa_file=goa)
    (only,) = yaml.safe_load(review.read_text())["existing_annotations"]
    assert "gene_products" not in only


@pytest.mark.parametrize("failing_page", [1, 2])
def test_a_failed_quickgo_request_raises_instead_of_writing_a_short_file(failing_page):
    full_page = Mock(status_code=200)
    full_page.json.return_value = {
        "numberOfHits": 400,
        "results": [{"geneProductId": f"UniProtKB:P{i}", "goId": "GO:0005515"} for i in range(200)],
    }
    calls = iter([full_page] if failing_page == 2 else [])

    def get(*args, **kwargs):
        response = next(calls, None)
        if response is None:
            raise requests.exceptions.ConnectionError("QuickGO down")
        return response

    with patch("ai_gene_review.etl.gene.requests.get", side_effect=get):
        with pytest.raises(ValueError, match=f"page {failing_page}"):
            fetch_goa_data("P04637")
