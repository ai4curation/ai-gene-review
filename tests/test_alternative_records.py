"""Curated alternative accessions retain the review identity and cite evidence."""

from copy import deepcopy
from pathlib import Path

from bs4 import BeautifulSoup
from pydantic import ValidationError
import pytest
import yaml

from ai_gene_review.datamodel.gene_review_model import GeneReview
from ai_gene_review.render import enrich_gene_data, render_gene_review, render_html
from ai_gene_review.validation import validate_gene_review
from ai_gene_review.validation.local_source_text import find_local_quote_failures


def review_data():
    """Two distinct source claims support one manually assessed counterpart."""
    return {
        "id": "O65922",
        "gene_symbol": "CCOAOMT2",
        "taxon": {"id": "NCBITaxon:3694", "label": "Populus trichocarpa"},
        "references": [{"id": "file:evidence.yaml", "title": "Record snapshot"}],
        "alternative_records": [
            {
                "id": "A0A2K2C664",
                "relationship": "REFERENCE_PROTEOME_EQUIVALENT",
                "reference_proteome": "UP000006729",
                "reviewed_on": "2026-10-18",
                "reason": "Same sequence and corresponding locus in the reference proteome.",
                "evidence": [
                    {
                        "type": "SEQUENCE_COMPARISON",
                        "description": "Both sequences are identical.",
                        "supported_by": [
                            {
                                "reference_id": "file:evidence.yaml",
                                "supporting_text": "identical: true",
                            }
                        ],
                    },
                    {
                        "type": "PROTEOME_MEMBERSHIP",
                        "description": "The alternative is in the reference proteome.",
                        "supported_by": [
                            {
                                "reference_id": "file:evidence.yaml",
                                "supporting_text": "proteome: UP000006729",
                            }
                        ],
                    },
                ],
            }
        ],
    }


def test_alternative_roundtrip_keeps_primary_accession():
    data = GeneReview.model_validate(review_data()).model_dump(
        mode="json", exclude_none=True
    )
    assert data["id"] == "O65922"
    alt = data["alternative_records"][0]
    assert alt["id"] == "A0A2K2C664"
    assert alt["reviewed_on"] == "2026-10-18"
    assert alt["evidence"][0]["supported_by"][0]["supporting_text"] == "identical: true"


def test_candidate_relationship_remains_distinct_from_equivalence(tmp_path):
    data = review_data()
    data["alternative_records"][0]["relationship"] = "REFERENCE_PROTEOME_CANDIDATE"
    parsed = GeneReview.model_validate(data).model_dump(mode="json")
    assert (
        parsed["alternative_records"][0]["relationship"]
        == "REFERENCE_PROTEOME_CANDIDATE"
    )
    data["alternative_records"][0]["evidence"] = []
    report = validate(data, tmp_path)
    assert any(
        i.is_error() and i.check_type == "alternative_records" for i in report.issues
    )


def test_no_counterpart_assessment_needs_no_invented_accession(tmp_path):
    data = review_data()
    alternative = data.pop("alternative_records")[0]
    data["reference_proteome_assessments"] = [
        {
            "reference_proteomes": ["UP000006729"],
            "status": "NO_SUPPORTED_COUNTERPART",
            "reviewed_on": "2026-10-18",
            "reason": "Search returned no sufficiently supported counterpart.",
            "evidence": [
                {**alternative["evidence"][0], "type": "PROTEOME_SEARCH"},
                alternative["evidence"][1],
            ],
        }
    ]
    parsed = GeneReview.model_validate(data).model_dump(mode="json")
    assert parsed["alternative_records"] is None
    assert (
        parsed["reference_proteome_assessments"][0]["status"]
        == "NO_SUPPORTED_COUNTERPART"
    )
    template = (
        Path(__file__).parents[1] / "src/ai_gene_review/templates/gene_review.html.j2"
    )
    soup = BeautifulSoup(
        render_html(enrich_gene_data(deepcopy(data)), template), "html.parser"
    )
    assert (
        "NO SUPPORTED COUNTERPART"
        in soup.select_one("#review-alternative-records").get_text()
    )
    report = validate(data, tmp_path)
    assert not any(
        i.is_error() and i.check_type == "alternative_records" for i in report.issues
    )
    data["reference_proteome_assessments"][0]["evidence"] = alternative["evidence"]
    report = validate(data, tmp_path)
    assert any(
        i.is_error() and i.check_type == "alternative_records" for i in report.issues
    )


def test_locus_counterpart_is_not_functional_equivalence():
    data = review_data()
    data["alternative_records"][0]["relationship"] = (
        "REFERENCE_PROTEOME_LOCUS_COUNTERPART"
    )
    parsed = GeneReview.model_validate(data).model_dump(mode="json")
    assert (
        parsed["alternative_records"][0]["relationship"]
        == "REFERENCE_PROTEOME_LOCUS_COUNTERPART"
    )


@pytest.mark.parametrize(
    "field,value",
    [
        ("relationship", "ORTHOLOG"),
        ("reference_proteome", "3694"),
        ("reviewed_on", "yesterday"),
        ("id", "UP000006729"),
    ],
)
def test_bad_record_fields_rejected(field, value):
    data = review_data()
    data["alternative_records"][0][field] = value
    with pytest.raises(ValidationError):
        GeneReview.model_validate(data)


def validate(data, tmp_path):
    """Run actual best-practice checks with a local source, without remote GOA."""
    (tmp_path / "evidence.yaml").write_text("identical: true\nproteome: UP000006729\n")
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump(data))
    return validate_gene_review(path, check_goa=False, check_supporting_text=False)


@pytest.mark.parametrize(
    "problem",
    ["self", "duplicate", "history_only", "no_membership", "uncited", "empty_evidence"],
)
def test_unsound_alternative_relationship_rejected(tmp_path, problem):
    data = review_data()
    alt = data["alternative_records"][0]
    if problem == "self":
        alt["id"] = data["id"]
    elif problem == "duplicate":
        data["alternative_records"].append(deepcopy(alt))
    elif problem == "history_only":
        alt["evidence"] = [{**alt["evidence"][0], "type": "RECORD_HISTORY"}]
    elif problem == "no_membership":
        alt["evidence"] = alt["evidence"][:1]
    elif problem == "uncited":
        alt["evidence"][0]["supported_by"][0]["reference_id"] = "file:undeclared.yaml"
    elif problem == "empty_evidence":
        alt["evidence"] = []
    report = validate(data, tmp_path)
    assert any(
        i.is_error() and i.check_type == "alternative_records" for i in report.issues
    )


def test_alternative_quotes_are_checked_against_source(tmp_path):
    (tmp_path / "evidence.yaml").write_text("identical: true\nproteome: UP000006729\n")
    data = review_data()
    assert not find_local_quote_failures(data, project_root=tmp_path)
    data["alternative_records"][0]["evidence"][0]["supported_by"][0][
        "supporting_text"
    ] = "identical: false"
    failures = find_local_quote_failures(data, project_root=tmp_path)
    assert len(failures) == 1
    assert "alternative_records" in failures[0][0]


def test_alternative_records_render_with_evidence():
    template = (
        Path(__file__).parents[1] / "src/ai_gene_review/templates/gene_review.html.j2"
    )
    soup = BeautifulSoup(
        render_html(enrich_gene_data(review_data()), template), "html.parser"
    )
    section = soup.select_one("#review-alternative-records")
    assert section is not None
    assert "Both sequences are identical" in section.get_text()
    assert section.select_one(
        'a[href="https://www.uniprot.org/uniprotkb/A0A2K2C664/entry"]'
    )
    assert section.select_one('a[href="https://www.uniprot.org/proteomes/UP000006729"]')
    assert "O65922" in soup.select_one(".header").get_text()


def test_alternative_snapshot_link_resolves_from_custom_output(tmp_path):
    gene_dir = tmp_path / "genes" / "POPTR" / "CCOAOMT2"
    gene_dir.mkdir(parents=True)
    data = review_data()
    (tmp_path / "evidence.yaml").write_text("identical: true\n")
    review_path = gene_dir / "CCOAOMT2-ai-review.yaml"
    review_path.write_text(yaml.safe_dump(data))
    output = tmp_path / "rendered.html"
    render_gene_review(review_path, output)
    soup = BeautifulSoup(output.read_text(), "html.parser")
    assert soup.select_one('#review-alternative-records a[href="evidence.yaml"]')


@pytest.mark.parametrize("gene", ["CCOAOMT1", "CCOAOMT2"])
def test_curated_poplar_pairs_match_archived_extracts(gene):
    """The local extracts retain identity and locus observations without FASTAs."""
    root = Path(__file__).parents[1]
    folder = root / "genes" / "POPTR" / gene
    data = yaml.safe_load((folder / f"{gene}-ai-review.yaml").read_text())
    snapshot = yaml.safe_load((folder / f"{gene}-record-evidence.yaml").read_text())
    alt = data["alternative_records"][0]
    primary, counterpart = snapshot["current_records"]
    assert data["id"] == primary["primaryAccession"]
    assert alt["id"] == counterpart["primaryAccession"]
    assert primary["sequence"] == counterpart["sequence"]
    assert primary["sequence"]["length"] == 247
    assert snapshot["observations"]["sequence_identical"]
    assert snapshot["observations"]["shared_uniparc_id"]
    loci = [
        {x["id"] for x in record["uniProtKBCrossReferences"] if x["database"] == "Gramene"}
        for record in (primary, counterpart)
    ]
    assert loci[0] & loci[1]
    assert not find_local_quote_failures(
        {"alternative_records": data["alternative_records"]}, project_root=root
    )


@pytest.mark.parametrize("gene", ["PRX2", "WIN6", "PAL", "MAOX"])
def test_nonidentical_poplar_counterparts_keep_differences_and_uncertainty(gene):
    root = Path(__file__).parents[1]
    folder = root / "genes" / "POPTR" / gene
    data = yaml.safe_load((folder / f"{gene}-ai-review.yaml").read_text())
    alt = data["alternative_records"][0]
    snapshot = yaml.safe_load((folder / f"{gene}-record-evidence.yaml").read_text())
    primary, counterpart = snapshot["current_records"]
    assert primary["sequence"]["sha256"] != counterpart["sequence"]["sha256"]
    expected = "REFERENCE_PROTEOME_CANDIDATE" if gene == "WIN6" else "REFERENCE_PROTEOME_EQUIVALENT"
    assert alt["relationship"] == expected
    selected = next(c for c in snapshot["comparison"]["candidates"] if c["accession"] == alt["id"])
    assert selected["identity_percent"] < 100
    assert any(s["path"].endswith("/comparison.yaml") for s in snapshot["archived_sources"])
    assert not find_local_quote_failures(
        {"alternative_records": data["alternative_records"]}, project_root=root
    )
