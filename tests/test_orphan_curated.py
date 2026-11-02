"""Membership and evidence accounting for the curated-orphan audit."""

import csv
import io
from pathlib import Path

import pytest
import yaml

from ai_gene_review.analysis.orphan_curated import (
    build_report,
    discover_reviews,
    render_csv,
    render_markdown,
)


def review(root: Path, species: str, gene: str, accession: str, taxon: int) -> Path:
    """Write a local review with a NEW row that must not enter source counts."""
    path = root / "genes" / species / gene / f"{gene}-ai-review.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "id": accession,
                "gene_symbol": gene,
                "taxon": {"id": f"NCBITaxon:{taxon}"},
                "existing_annotations": [
                    {"evidence_type": "IDA", "review": {"action": "NEW"}}
                ],
            }
        )
    )
    return path


def goa(path: Path, accession: str) -> None:
    """Write repeated terms with distinct evidence and a negated annotation."""
    path.with_name(path.name.replace("-ai-review.yaml", "-goa.tsv")).write_text(
        "GENE PRODUCT DB\tGENE PRODUCT ID\tGO TERM\tGO EVIDENCE CODE\tQUALIFIER\tDATE\n"
        f"UniProtKB\t{accession}\tGO:0000001\tIDA\tenables\t20260101\n"
        f"UniProtKB\t{accession}\tGO:0000001\tIBA\tenables\t20260102\n"
        f"UniProtKB\t{accession}\tGO:0000002\tIEA\tNOT|enables\t20260103\n"
        "UniProtKB\tOTHER\tGO:0000003\tIDA\tenables\t20260103\n"
    )


def entry(
    accession: str, taxon: int = 3694, proteomes: tuple = (), reviewed: bool = True
) -> dict:
    """Minimal UniProt JSON projection used by the report."""
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)"
        if reviewed
        else "UniProtKB unreviewed (TrEMBL)",
        "organism": {"taxonId": taxon, "scientificName": "Example species"},
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Protein | example"}}
        },
        "uniProtKBCrossReferences": [
            {"database": "Proteomes", "id": p} for p in proteomes
        ],
    }


def test_membership_exact_taxon_and_any_reference(tmp_path):
    for accession, taxon in [
        ("ORPHAN", 3694),
        ("MEMBER", 3694),
        ("STRAIN", 123),
        ("TREMBL", 3694),
        ("MISSING", 3694),
    ]:
        review(tmp_path, "POPTR", accession, accession, taxon)
    entries = [
        entry("ORPHAN", proteomes=("UP_NONREF",)),
        entry("MEMBER", proteomes=("UP_REF2",)),
        entry("STRAIN", taxon=123),
        entry("TREMBL", reviewed=False),
    ]
    result = build_report(
        discover_reviews(tmp_path), entries, {3694: {"UP_REF1", "UP_REF2"}}, tmp_path
    )
    assert [r["accession"] for r in result["candidates"]] == ["ORPHAN"]
    assert result["scope"]["in_reference_proteome"] == 1
    assert result["scope"]["no_exact_taxon_reference"] == 1
    assert result["scope"]["unreviewed"] == 1
    assert result["scope"]["unresolved"] == 1
    assert result["candidates"][0]["goa_status"] == "missing"
    assert result["candidates"][0]["goa_rows"] is None
    assert "MISSING" in str(result["diagnostics"])


def test_duplicate_reviews_do_not_inflate_evidence(tmp_path):
    for species in ("POPTR", "poplar"):
        path = review(tmp_path, species, "GENE", "ORPHAN", 3694)
        goa(path, "ORPHAN")
    result = build_report(
        discover_reviews(tmp_path), [entry("ORPHAN")], {3694: {"UP_REF"}}, tmp_path
    )
    row = result["candidates"][0]
    assert result["scope"]["review_files"] == 2
    assert result["scope"]["accessions"] == 1
    assert len(row["review_paths"]) == 2
    assert row["evidence_counts"] == {"IDA": 1, "IBA": 1, "IEA": 1}
    assert row["goa_rows"] == 3
    assert row["go_terms"] == 2
    assert row["non_iea_rows"] == 2
    assert row["experimental_rows"] == 1
    assert row["not_rows"] == 1
    assert row["goa_date_min"] == "20260101"
    assert "OTHER" in str(result["diagnostics"])
    result["sources"] = []
    result["generated_at"] = "2026-10-18T00:00:00+00:00"
    result["selection"] = "all repository reviews"
    output = list(csv.DictReader(io.StringIO(render_csv(result))))
    assert output[0]["goa_IDA"] == "1"
    assert output[0]["goa_rows"] == "3"
    md = render_markdown(result)
    assert "https://www.uniprot.org/uniprotkb/ORPHAN/entry" in md
    assert (
        "https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AORPHAN"
        in md
    )
    assert "Protein &#124; example" in md
    assert "| IBA | 1 |" in md


def test_taxon_mismatch_is_diagnostic_not_a_silent_exclusion(tmp_path):
    review(tmp_path, "POPTR", "GENE", "ORPHAN", 999)
    result = build_report(
        discover_reviews(tmp_path), [entry("ORPHAN")], {3694: {"UP_REF"}}, tmp_path
    )
    assert len(result["candidates"]) == 1  # Live taxonomy wins, with a diagnostic.
    assert "taxon" in str(result["diagnostics"]).lower()


def test_empty_goa_is_unknown_but_header_only_is_zero(tmp_path):
    path = review(tmp_path, "POPTR", "GENE", "ORPHAN", 3694)
    cache = path.with_name("GENE-goa.tsv")
    cache.write_text("")
    result = build_report(
        discover_reviews(tmp_path), [entry("ORPHAN")], {3694: {"UP_REF"}}, tmp_path
    )
    assert result["candidates"][0]["goa_rows"] is None
    cache.write_text("GENE PRODUCT ID\tGO TERM\tGO EVIDENCE CODE\tQUALIFIER\n")
    result = build_report(
        discover_reviews(tmp_path), [entry("ORPHAN")], {3694: {"UP_REF"}}, tmp_path
    )
    assert result["candidates"][0]["goa_rows"] == 0


def test_malformed_review_fails_instead_of_dropping_gene(tmp_path):
    path = review(tmp_path, "POPTR", "GENE", "ORPHAN", 3694)
    path.write_text("gene_symbol: GENE\n")
    with pytest.raises(ValueError, match="GENE-ai-review.yaml"):
        discover_reviews(tmp_path)


def test_entry_name_resolved_only_from_matching_flatfile_and_rna_excluded(tmp_path):
    path = review(tmp_path, "AILME", "GENE", "A0A7N5KEZ3_AILME", 9646)
    path.with_name("GENE-uniprot.txt").write_text(
        "ID   A0A7N5KEZ3_AILME Unreviewed; 419 AA.\nAC   A0A7N5KEZ3;\n"
    )
    review(tmp_path, "human", "XIST", "URS000075D95B_9606", 9606)
    reviews = discover_reviews(tmp_path)
    assert set(reviews) == {"A0A7N5KEZ3", "URS000075D95B_9606"}
    result = build_report(
        reviews, [entry("A0A7N5KEZ3", taxon=9646, reviewed=False)], {}, tmp_path
    )
    assert result["scope"]["non_protein"] == 1
    assert result["scope"]["unresolved"] == 0
    assert "A0A7N5KEZ3_AILME" in str(result["diagnostics"])
    path.with_name("GENE-uniprot.txt").write_text(
        "ID   WRONG_AILME Unreviewed; 419 AA.\nAC   A0A7N5KEZ3;\n"
    )
    assert "A0A7N5KEZ3_AILME" in discover_reviews(tmp_path)
