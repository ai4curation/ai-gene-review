"""Preserve a real ECO-only source assertion through fetch, seed and validation."""

from unittest.mock import Mock, patch

import pytest
import yaml
from pydantic import ValidationError

from ai_gene_review.datamodel.gene_review_model import ExistingAnnotation
from ai_gene_review.etl.gene import fetch_goa_data
from ai_gene_review.validation.goa_validator import GOAAnnotation, GOAValidator


def source_row(go_code=None):
    """Shape returned by QuickGO for A5FI22 on 2026-11-07."""
    return {
        "geneProductId": "UniProtKB:A5FI22",
        "symbol": "Fjoh_2111",
        "qualifier": "acts_upstream_of_or_within_positive_effect",
        "goId": "GO:0042953",
        "goName": "lipoprotein transport",
        "goEvidence": go_code,
        "goAspect": "biological_process",
        "evidenceCode": "ECO:0007744",
        "reference": "PMID:40050408",
        "withFrom": [{"connectedXrefs": [{"db": "UniProtKB", "id": "P61316"}]}],
        "taxonId": 376686,
        "taxonName": None,
        "assignedBy": "CACAO",
        "name": None,
        "date": "20250407",
    }


def downloaded_tsv(row):
    response = Mock()
    rows = row if isinstance(row, list) else [row]
    response.json.return_value = {"results": rows, "numberOfHits": len(rows)}
    with patch("ai_gene_review.etl.gene.requests.get", return_value=response):
        return fetch_goa_data("A5FI22")


def test_null_go_code_preserves_raw_eco_and_empty_columns():
    fields = downloaded_tsv(source_row()).splitlines()[1].split("\t")
    assert len(fields) == 16
    assert fields[7:9] == ["ECO:0007744", ""]
    assert fields[12] == fields[14] == ""
    parsed = GOAAnnotation.from_tsv_row(fields)
    assert parsed.evidence_code == parsed.evidence_type == "ECO:0007744"
    assert parsed.qualifier == "acts_upstream_of_or_within_positive_effect"
    assert parsed.reference == "PMID:40050408"
    assert parsed.with_from == "UniProtKB:P61316"


def test_go_shorthand_still_takes_precedence():
    row = source_row("IDA")
    row["evidenceCode"] = "ECO:0000314"
    fields = downloaded_tsv(row).splitlines()[1].split("\t")
    parsed = GOAAnnotation.from_tsv_row(fields)
    assert parsed.evidence_code == "IDA"
    assert parsed.evidence_type == "ECO:0000314"


def test_eco_only_seed_is_schema_valid_idempotent_and_strictly_matched(tmp_path):
    raw = downloaded_tsv(source_row())
    goa = tmp_path / "Fjoh_2111-goa.tsv"
    goa.write_text(raw)
    review = tmp_path / "Fjoh_2111-ai-review.yaml"
    review.write_text(yaml.safe_dump({
        "id": "A5FI22", "gene_symbol": "Fjoh_2111",
        "taxon": {"id": "NCBITaxon:376686", "label": "Flavobacterium johnsoniae UW101"},
        "description": "A lipoprotein carrier.",
    }))
    validator = GOAValidator(strict_mode=True)
    assert validator.seed_missing_annotations(review, goa)[0] == 1
    document = yaml.safe_load(review.read_text())
    annotation = document["existing_annotations"][0]
    assert annotation["evidence_type"] == "ECO:0007744"
    assert annotation["qualifier"] == "acts_upstream_of_or_within_positive_effect"
    assert annotation["supporting_entities"] == ["UniProtKB:P61316"]
    ExistingAnnotation.model_validate(annotation)
    assert validator.validate_against_goa(review, goa).is_valid
    before = review.read_bytes()
    assert validator.seed_missing_annotations(review, goa)[0] == 0
    assert review.read_bytes() == before
    assert goa.read_text() == raw
    annotation["evidence_type"] = "IMP"
    review.write_text(yaml.safe_dump(document))
    assert not validator.validate_against_goa(review, goa).is_valid


def test_unknown_evidence_is_not_silently_accepted():
    with pytest.raises(ValidationError):
        ExistingAnnotation.model_validate({
            "term": {"id": "GO:0042953", "label": "lipoprotein transport"},
            "evidence_type": "ECO:9999999",
            "original_reference_id": "PMID:40050408",
        })


def test_null_date_and_go_id_sort_with_non_null_rows():
    nulls = {**source_row(), "date": None, "goId": None}
    fields = [line.split("\t") for line in downloaded_tsv([nulls, source_row()]).splitlines()[1:]]
    assert fields[0][4] == "GO:0042953"
    assert fields[1][4] == fields[1][15] == ""


def test_whitespace_go_code_falls_back_but_explicit_cacao_exp_is_preserved():
    fields = downloaded_tsv(source_row("  ")).splitlines()[1].split("\t")
    assert GOAAnnotation.from_tsv_row(fields).evidence_code == "ECO:0007744"
    fields[8] = " EXP "
    parsed = GOAAnnotation.from_tsv_row(fields)
    assert parsed.evidence_code == "EXP"
    assert parsed.evidence_type == "ECO:0007744"


def test_eco_only_is_experimental_in_literature_and_tabular_export():
    from ai_gene_review.export.tabular import TabularExporter
    from ai_gene_review.validation.goa_validator import EXPERIMENTAL_EVIDENCE_CODES, referenced_pmids

    parsed = GOAAnnotation.from_tsv_row(downloaded_tsv(source_row()).splitlines()[1].split("\t"))
    assert referenced_pmids([parsed], EXPERIMENTAL_EVIDENCE_CODES) == {
        "PMID:40050408": {"ECO:0007744"}
    }
    assert TabularExporter()._derive_method(parsed.evidence_code, parsed.reference) == "Experimental"
    assert parsed.evidence_code == "ECO:0007744"


def test_raw_eco_only_counts_and_target_coverage(tmp_path):
    from ai_gene_review.analysis.orphan_curated import goa_counts
    from ai_gene_review.export.propagation_rows import EXPERIMENTAL, iter_target_evidence
    from ai_gene_review.tools.wrong_gene_leads import candidate_rows

    folder = tmp_path / "genes/FLAJ1/Fjoh_2111"
    folder.mkdir(parents=True)
    path = folder / "Fjoh_2111-goa.tsv"
    raw = downloaded_tsv(source_row())
    path.write_text(raw)
    (folder / "Fjoh_2111-uniprot.txt").write_text(
        "ID   EXAMPLE\nAC   A5FI22;\nOX   NCBI_TaxID=376686;\nGN   Name=Fjoh_2111;\n//\n"
    )
    counts = goa_counts("A5FI22", [{"path": "genes/FLAJ1/Fjoh_2111/Fjoh_2111-ai-review.yaml"}], tmp_path, [])
    assert counts["experimental_rows"] == 1
    assert counts["evidence_counts"] == {"ECO:0007744": 1}
    evidence = list(iter_target_evidence(tmp_path / "genes"))
    assert evidence == [("FLAJ1", "Fjoh_2111", "GO:0042953", "ECO:0007744")]
    assert evidence[0][3] in EXPERIMENTAL
    assert len(candidate_rows(folder)[1]) == 1
    assert path.read_text() == raw
