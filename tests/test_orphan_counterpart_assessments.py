"""Every accession in the fixed project audit has a source-backed disposition."""

import csv
import re
from pathlib import Path

import yaml

from ai_gene_review.datamodel.gene_review_model import GeneReview
from ai_gene_review.validation.local_source_text import find_local_quote_failures


ROOT = Path(__file__).parents[1]


def test_all_audit_entries_have_verified_assessments():
    """Check local source-backed decisions; full sequence recomputation lives in the archive."""
    with (ROOT / "projects/ORPHAN_CURATED/reports/orphan-curated.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    with (
        ROOT / "projects/ORPHAN_CURATED/counterpart-assessments.csv"
    ).open() as handle:
        summaries = {r["accession"]: r for r in csv.DictReader(handle)}
    assert set(summaries) == {r["accession"] for r in rows}
    for row in rows:
        path = ROOT / row["review_paths"]
        gene = path.name.removesuffix("-ai-review.yaml")
        data = yaml.safe_load(path.read_text())
        GeneReview.model_validate(data)
        assert data["id"] == row["accession"]
        alternatives = data.get("alternative_records") or []
        assessments = data.get("reference_proteome_assessments") or []
        assert bool(alternatives) != bool(assessments)
        blocks = {
            k: data[k]
            for k in ("alternative_records", "reference_proteome_assessments")
            if data.get(k)
        }
        assert not find_local_quote_failures(blocks, project_root=ROOT)
        snapshot = yaml.load(
            (path.parent / f"{gene}-record-evidence.yaml").read_text(),
            Loader=yaml.CSafeLoader,
        )
        primary = snapshot["current_records"][0]
        assert primary["primaryAccession"] == row["accession"]
        reference_ids = set(row["reference_proteomes"].split(";"))
        primary_memberships = {
            x["id"]
            for x in primary["uniProtKBCrossReferences"]
            if x["database"] == "Proteomes"
        }
        assert not reference_ids & primary_memberships
        proteomes = snapshot["reference_proteomes"]
        assert {p["id"] for p in proteomes} == reference_ids
        assert all(
            p["proteomeType"] == "Reference proteome"
            and p["taxonomy"]["taxonId"] == primary["organism"]["taxonId"]
            for p in proteomes
        )
        if alternatives:
            alt = alternatives[0]
            target = snapshot["current_records"][1]
            assert (
                alt["id"]
                == target["primaryAccession"]
                == summaries[row["accession"]]["alternative"]
            )
            assert target["organism"]["taxonId"] == primary["organism"]["taxonId"]
            assert any(
                x["database"] == "Proteomes" and x["id"] == alt["reference_proteome"]
                for x in target["uniProtKBCrossReferences"]
            )
        else:
            assert not summaries[row["accession"]]["alternative"]
            assert assessments[0]["status"] == "NO_SUPPORTED_COUNTERPART"
            assert set(assessments[0]["reference_proteomes"]) == reference_ids
        assert snapshot["snapshot_type"] == "uniprot_record_evidence_extract"
        assert re.fullmatch(r"[0-9a-f]{40}", snapshot["archive"]["commit"])
        for source in snapshot["archived_sources"]:
            assert source["url"] == (
                f"{snapshot['archive']['repository']}/blob/{snapshot['archive']['commit']}/{source['path']}"
            )
            assert re.fullmatch(r"[0-9a-f]{64}", source["sha256"])
            for excerpt in source["excerpts"]:
                assert len(excerpt["text"].splitlines()) == excerpt["end_line"] - excerpt["start_line"] + 1
        assert all("value" not in r["sequence"] for r in snapshot["current_records"])
        if alternatives and "comparison" in snapshot:
            selected = next(c for c in snapshot["comparison"]["candidates"] if c["accession"] == alt["id"])
            assert selected["query_length"] == primary["sequence"]["length"]
            assert selected["target_length"] == target["sequence"]["length"]


def test_inactive_reference_alleles_are_not_equivalents():
    for gene in ["FRI", "AOP2"]:
        review = yaml.safe_load(
            (ROOT / f"genes/ARATH/{gene}/{gene}-ai-review.yaml").read_text()
        )
        assert (
            review["alternative_records"][0]["relationship"]
            == "REFERENCE_PROTEOME_LOCUS_COUNTERPART"
        )


def test_rga_mapping_claims_match_the_available_evidence():
    rga5 = yaml.safe_load((ROOT / 'genes/ORYSJ/RGA5/RGA5-ai-review.yaml').read_text())
    assert rga5['alternative_records'][0]['relationship'] == 'REFERENCE_PROTEOME_CANDIDATE'
    rga4 = yaml.safe_load((ROOT / 'genes/ORYSJ/RGA4/RGA4-ai-review.yaml').read_text())
    locus = [e for e in rga4['alternative_records'][0]['evidence'] if e['type'] == 'LOCUS_MAPPING']
    assert len(locus) == 1
    assert any(s['reference_id'] == 'PMID:21251109' for s in locus[0]['supported_by'])


def test_search_descriptions_match_retained_artifacts():
    with (ROOT / 'projects/ORPHAN_CURATED/counterpart-assessments.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        path = ROOT / row['review_path']
        review = yaml.safe_load(path.read_text())
        snapshot = yaml.safe_load((path.parent / f"{row['gene']}-record-evidence.yaml").read_text())
        comparison = snapshot.get("comparison")
        if comparison is None:
            continue
        block = (review.get('alternative_records') or review['reference_proteome_assessments'])[0]
        descriptions = [e['description'] for e in block['evidence'] if e['type'] == 'PROTEOME_SEARCH']
        if not descriptions:  # Earlier POPTR assessments cite their searches via sequence evidence.
            continue
        description = descriptions[0]
        if comparison['candidate_count'] == 0:
            assert 'no alignments were generated' in description
        else:
            retained = comparison["retained_alignment_count"]
            assert f'{retained} detailed alignment files' in description
