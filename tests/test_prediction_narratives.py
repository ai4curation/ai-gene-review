"""Real-file tests for narrative prediction sets without artificial term claims."""

import csv
import gzip
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from ai_gene_review.export.prediction_narratives import collect_narrative_sets


def write_file(root: Path, relative: str, text: str) -> Path:
    """Write a corpus fixture and return its actual path."""
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def write_csv(root: Path, relative: str, rows: list[dict[str, str]]) -> Path:
    """Write benchmark metadata with its real CSV representation."""
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return path


def gene_fixture(root: Path, gene: str = "kinase", accession: str = "P12345") -> Path:
    """Create the curated identity used to join narrative records."""
    path = write_file(
        root,
        f"genes/DROME/{gene}/{gene}-ai-review.yaml",
        yaml.safe_dump(
            {
                "id": accession,
                "gene_symbol": gene,
                "status": "COMPLETE",
                "taxon": {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"},
            }
        ),
    )
    path.with_suffix(".html").write_text("<html>Gene review</html>")
    return path


def rl_fixture(root: Path) -> tuple[Path, Path]:
    """Create a scored review and a raw export with deliberately unrelated GO text."""
    gene_fixture(root)
    raw = write_file(
        root,
        "genes/DROME/kinase/kinase-bioreason-rl-predictions.md",
        "# BioReason Chat Export\n*Exported on March 22, 2026*\n"
        "### Thinking Trace\nDiagnostic trace.\n"
        "### Functional Summary\nAn active protein kinase.\n"
        "### GO Terms\nGO:1234567 unrelated upstream prediction\n",
    )
    review = write_file(
        root,
        "genes/DROME/kinase/kinase-bioreason-rl-review.md",
        "# BioReason-Pro RL Review\n\n- **Correctness**: 4/5\n"
        "- **Completeness**: 3/5\n\n## Functional Summary Review\n"
        "The catalytic function is supported; the cellular context is incomplete.\n",
    )
    return raw, review


def test_rl_scores_and_summary_remain_separate_from_go_claims(tmp_path: Path) -> None:
    """Export current narrative scores and an established raw link, not upstream GO terms."""
    raw, review = rl_fixture(tmp_path)
    write_csv(
        tmp_path,
        "projects/BIOREASON_COMPARISON/benchmark-genes.csv",
        [
            {
                "benchmark": "argo139_rl_narrative",
                "organism": "DROME",
                "gene": "kinase",
                "uniprot_id": "P12345",
                "source_file": review.relative_to(tmp_path).as_posix(),
                "source_version": "app.bioreason.net/RL",
                "correctness": "4",
                "completeness": "3",
            }
        ],
    )
    write_csv(
        tmp_path,
        "projects/BIOREASON_COMPARISON/benchmark-quality.csv",
        [
            {
                "organism": "DROME",
                "gene": "kinase",
                "expected_uniprot_id": "P12345",
                "cached_uniprot_id": "P12345",
                "input_quality": "TRUNCATED",
                "performance_included": "true",
                "review_sha256": hashlib.sha256(review.read_bytes()).hexdigest(),
                "prediction_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
            }
        ],
    )
    rows = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")
    assert len(rows) == 1
    row = rows[0]
    assert row["source_method"] == "BioReason-Pro-RL"
    assert row["output_type"] == "Functional summary"
    assert row["claim_count"] is None
    assert row["assessment_categories"] == []
    assert row["correctness"] == 4
    assert row["completeness"] == 3
    assert row["review_state"] == "Reviewed"
    assert row["input_quality"] == "TRUNCATED"
    assert row["performance_included"] is True
    assert row["metadata_status"] == "Hashes match"
    assert row["prediction_summary"] == "An active protein kinase."
    assert (
        row["summary"]
        == "The catalytic function is supported; the cellular context is incomplete."
    )
    assert "GO:1234567" not in row["summary"]
    assert (
        row["raw_link"] == "../../genes/DROME/kinase/kinase-bioreason-rl-predictions.md"
    )
    assert row["source_link"].endswith("kinase-bioreason-rl-review.md")
    assert row["review_link"].endswith("kinase-ai-review.html")
    assert row["projects"] == ["BIOREASON_COMPARISON"]
    assert row["cohorts"] == ["argo139_rl_narrative"]


def test_stale_metadata_does_not_replace_current_scores_or_hide_input_mismatch(
    tmp_path: Path,
) -> None:
    """Keep actual review scores and expose stale snapshots and wrong-input provenance."""
    _, review = rl_fixture(tmp_path)
    write_csv(
        tmp_path,
        "projects/BIOREASON_COMPARISON/benchmark-genes.csv",
        [
            {
                "benchmark": "argo139_rl_narrative",
                "organism": "DROME",
                "gene": "kinase",
                "uniprot_id": "P12345",
                "source_file": review.relative_to(tmp_path).as_posix(),
                "correctness": "5",
                "completeness": "5",
            }
        ],
    )
    write_csv(
        tmp_path,
        "projects/BIOREASON_COMPARISON/benchmark-quality.csv",
        [
            {
                "organism": "DROME",
                "gene": "kinase",
                "expected_uniprot_id": "P12345",
                "cached_uniprot_id": "Q99999",
                "input_quality": "WRONG_INPUT_SEQUENCE",
                "performance_included": "false",
                "exclusion_reason": "WRONG_INPUT_SEQUENCE",
                "review_sha256": "obsolete-hash",
            }
        ],
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert (row["correctness"], row["completeness"]) == (4, 3)
    assert row["metadata_status"] == "Stale"
    assert row["protein_id"] == "P12345"
    assert row["input_protein_id"] == "Q99999"
    assert row["identity_status"] == "Input mismatch"
    assert row["performance_included"] is False
    assert any("correctness" in note for note in row["quality_notes"])
    assert any("review_sha256" in note for note in row["quality_notes"])


def test_raw_only_record_is_unreviewed_and_identity_is_not_invented(
    tmp_path: Path,
) -> None:
    """An observed raw output remains browsable even without an identity or review."""
    write_file(
        tmp_path,
        "genes/DROME/unknown/unknown-bioreason-rl-predictions.md",
        "### Functional Summary\nA membrane component.\n### GO Terms\nGO:9999999\n",
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["protein_id"] == ""
    assert row["identity_status"] == "Unresolved"
    assert row["review_state"] == "Unreviewed"
    assert row["claim_count"] is None
    assert row["assessment_categories"] == []
    assert row["source_link"] == row["raw_link"]
    assert "correctness" not in row


def test_raw_only_record_keeps_benchmark_identity_and_stable_id(tmp_path: Path) -> None:
    """Removing or adding a review does not change the identity of an observed output."""
    _, review = rl_fixture(tmp_path)
    write_csv(
        tmp_path,
        "projects/BIOREASON_COMPARISON/benchmark-genes.csv",
        [
            {
                "benchmark": "argo139_rl_narrative",
                "organism": "DROME",
                "gene": "kinase",
                "uniprot_id": "P12345",
                "source_file": review.relative_to(tmp_path).as_posix(),
                "source_version": "app.bioreason.net/RL",
                "correctness": "4",
                "completeness": "3",
            }
        ],
    )
    output_dir = tmp_path / "app/predictions"
    reviewed = collect_narrative_sets(tmp_path, output_dir)[0]
    review.unlink()
    review.with_name("kinase-ai-review.yaml").unlink()
    raw_only = collect_narrative_sets(tmp_path, output_dir)[0]
    assert raw_only["set_id"] == reviewed["set_id"]
    assert raw_only["protein_id"] == "P12345"
    assert raw_only["cohorts"] == ["argo139_rl_narrative"]
    assert raw_only["review_state"] == "Unreviewed"
    assert "correctness" not in raw_only


def test_incomplete_narrative_review_does_not_become_unc(tmp_path: Path) -> None:
    """Missing/out-of-range scores remain awaiting review, outside VDCL categories."""
    _, review = rl_fixture(tmp_path)
    review.write_text(
        "# Draft review\n- **Correctness**: 6/5\nNo completeness score.\n"
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["review_state"] == "Awaiting review"
    assert row["document_status"] == "DRAFT"
    assert row["assessment_categories"] == []
    assert "correctness" not in row
    assert "completeness" not in row


@pytest.mark.parametrize("current_index", [True, False])
def test_protnlm_categories_require_exact_index_hash(
    tmp_path: Path, current_index: bool
) -> None:
    """Use the manually indexed narrative categories and exact benchmark target identity."""
    gene_fixture(tmp_path, "receptor", "P33244")
    review = write_file(
        tmp_path,
        "genes/DROME/receptor/receptor-protnlm-function-review.md",
        "# Function review\n\n## Original prediction\n\n> A thyroid hormone receptor.\n\n"
        "## Assessment\nPLI for hormone specificity; UNC here discusses a separate GO prediction.\n",
    )
    write_file(tmp_path, "genes/DROME/receptor/receptor-protnlm-source.json", "{}")
    write_file(
        tmp_path,
        "projects/PROTNLM_EVALUATION/narrative-review-index.yaml",
        yaml.safe_dump(
            {
                "reviews": [
                    {
                        "review_file": review.relative_to(tmp_path).as_posix(),
                        "categories": ["PLI", "SUPPORTED"],
                        "review_sha256": hashlib.sha256(review.read_bytes()).hexdigest()
                        if current_index
                        else "stale",
                    }
                ]
            }
        ),
    )
    write_csv(
        tmp_path,
        "projects/PROTNLM_EVALUATION/family-curation/scope.csv",
        [
            {
                "cohort": "fly_first41",
                "role": "prediction_target",
                "accession": "M9NFK2",
                "species": "DROME",
                "gene_symbol": "receptor",
            }
        ],
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["protein_id"] == "M9NFK2"
    assert row["reference_protein_id"] == "P33244"
    assert row["claim_count"] is None
    assert row["cohorts"] == ["fly_first41"]
    assert row["prediction_summary"] == "A thyroid hormone receptor."
    assert row["summary"].startswith("PLI for hormone specificity")
    assert row["assessment_categories"] == (
        ["PLI", "SUPPORTED"] if current_index else []
    )
    assert row["review_state"] == ("Reviewed" if current_index else "Index stale")


def test_sft_narrative_uses_raw_source_metadata_and_excludes_experiment_copies(
    tmp_path: Path,
) -> None:
    """Retain SFT narrative provenance without recursively ingesting project copies."""
    gene_fixture(tmp_path)
    raw = "    ---\n    source: huggingface.co/datasets/wanglab/protein_catalogue\n    uniprot_id: P12345\n    ---\n\n    ## Functional Summary\n    An active kinase.\n"
    write_file(
        tmp_path, "genes/DROME/kinase/kinase-deep-research-bioreason-sft.md", raw
    )
    review_text = "# SFT Review\n- **Correctness**: 5/5\n- **Completeness**: 2/5\n"
    write_file(
        tmp_path, "genes/DROME/kinase/kinase-bioreason-sft-review.md", review_text
    )
    write_file(
        tmp_path,
        "projects/experiment/genes/DROME/kinase/kinase-bioreason-sft-review.md",
        review_text,
    )
    rows = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")
    assert len(rows) == 1
    assert rows[0]["source_method"] == "BioReason-Pro-SFT"
    assert (
        rows[0]["source_version"] == "huggingface.co/datasets/wanglab/protein_catalogue"
    )
    assert (rows[0]["correctness"], rows[0]["completeness"]) == (5, 2)
    assert rows[0]["prediction_summary"] == "An active kinase."


def test_unreviewed_sft_functional_summary_is_included(tmp_path: Path) -> None:
    """Raw SFT outputs need no completed review to be discoverable."""
    gene_fixture(tmp_path)
    write_file(
        tmp_path,
        "genes/DROME/kinase/kinase-deep-research-bioreason-sft.md",
        "---\nsource: wanglab/protein_catalogue\nuniprot_id: P12345\n---\n"
        "## Functional Summary\nAn active kinase.\n",
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["source_method"] == "BioReason-Pro-SFT"
    assert row["prediction_summary"] == "An active kinase."
    assert row["summary"] == "No review recorded."
    assert row["review_state"] == "Unreviewed"
    assert row["source_link"] == row["raw_link"]
    assert "correctness" not in row


@pytest.mark.parametrize("snapshot_accession", ["P12345", "Q99999"])
def test_manifest_raw_link_requires_exact_accession(
    tmp_path: Path, snapshot_accession: str
) -> None:
    """A cohort snapshot is a raw source only when it actually contains this target."""
    gene_fixture(tmp_path)
    write_file(
        tmp_path,
        "genes/DROME/kinase/kinase-protnlm-function-review.md",
        "# Function review\n\n> An active kinase.\n",
    )
    source = "projects/PROTNLM_EVALUATION/cohort/targets.csv"
    write_csv(
        tmp_path,
        "projects/PROTNLM_EVALUATION/family-curation/scope.csv",
        [
            {
                "cohort": "example",
                "role": "prediction_target",
                "accession": "P12345",
                "species": "DROME",
                "gene_symbol": "kinase",
                "cohort_source": source,
            }
        ],
    )
    write_file(
        tmp_path,
        "projects/PROTNLM_EVALUATION/cohort/targets-manifest.json",
        json.dumps({"prediction_snapshot": "predictions.jsonl.gz"}),
    )
    snapshot = tmp_path / "projects/PROTNLM_EVALUATION/cohort/predictions.jsonl.gz"
    with gzip.open(snapshot, "wt") as stream:
        stream.write(json.dumps({"primaryAccession": snapshot_accession}) + "\n")
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert bool(row["raw_link"]) is (snapshot_accession == "P12345")


def test_protnlm_uncertain_evaluation_is_not_replaced_by_model_claim(
    tmp_path: Path,
) -> None:
    """Keep an unverified transport prediction distinct from the reviewer's uncertainty."""
    gene_fixture(tmp_path, "Dic4", "Q9VVS1")
    write_file(
        tmp_path,
        "genes/DROME/Dic4/Dic4-protnlm-function-review.md",
        "# Dic4 ProtNLM review\n\n## Original prediction\n\n"
        "> Mitochondrial transporter that mediates uptake of thiamine pyrophosphate.\n\n"
        "## Assessment\n\n**UNC — thiamine pyrophosphate transport is unresolved.** "
        "Mitochondrial localization does not establish substrate specificity.\n",
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["summary"].startswith(
        "UNC — thiamine pyrophosphate transport is unresolved."
    )
    assert "mediates uptake" not in row["summary"]
    assert row["prediction_summary"].startswith(
        "Mitochondrial transporter that mediates uptake"
    )


def test_bioreason_evaluation_omits_quoted_model_output(tmp_path: Path) -> None:
    """Do not label an opening model quotation as the reviewer's evaluation."""
    _, review = rl_fixture(tmp_path)
    review.write_text(
        "# RL Review\n- **Correctness**: 2/5\n- **Completeness**: 3/5\n\n"
        "## Functional Summary Review\n\nThe BioReason functional summary states:\n\n"
        "> The protein is a thyroid hormone receptor.\n\n"
        "The hormone specificity is incorrect; this is an unrelated receptor subfamily.\n",
    )
    row = collect_narrative_sets(tmp_path, tmp_path / "app/predictions")[0]
    assert row["summary"].startswith("The hormone specificity is incorrect")
    assert "states:" not in row["summary"]
    assert "protein is a thyroid hormone receptor" not in row["summary"]
