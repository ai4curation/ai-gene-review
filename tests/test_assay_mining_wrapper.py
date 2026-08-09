"""End-to-end tests for the public ASSAY_TO_FUNCTION mining wrappers."""

from __future__ import annotations

import csv
import os
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def make_assay_fixture(root: Path) -> tuple[Path, Path, Path]:
    """Create one annotation whose supporting paper, but not primary, has a readout."""
    genes_dir = root / "genes with spaces"
    gene_dir = genes_dir / "TEST" / "GENE"
    gene_dir.mkdir(parents=True)
    (gene_dir / "GENE-ai-review.yaml").write_text(
        """
id: UniProtKB:TEST
gene_symbol: GENE
existing_annotations:
  - term:
      id: GO:0006986
      label: response to unfolded protein
    evidence_type: IDA
    original_reference_id: PMID:1
    review:
      action: ACCEPT
      summary: |-
        UPRE
          reporter assay
      supported_by:
        - reference_id: PMID:2
"""
    )
    (gene_dir / "GENE-goa.tsv").write_text(
        "GO TERM\tGO ASPECT\nGO:0006986\tbiological_process\n"
    )

    pubs_dir = root / "publications with spaces"
    pubs_dir.mkdir()
    (pubs_dir / "PMID_1.md").write_text(
        "full_text_available: true\nNo assay vocabulary here.\n"
    )
    (pubs_dir / "PMID_2.md").write_text(
        "full_text_available: true\n"
        "A UPRE reporter assay, a UPRE   reporter assay, and a UPRE\n"
        "  reporter assay were performed.\n"
    )

    catalog = root / "catalog with spaces.yaml"
    catalog.write_text(
        r"""
readouts:
  UPR_ER_STRESS:
    proximity: phenotypic
    convergence: high
    aligned_label_regex: 'unfolded protein'
    commonly_overmapped_to: [GO:0006986]
    patterns:
      - '\bUPRE[ \t]+reporter'
      - '\bUPRE\n[ \t]+reporter'
"""
    )
    return genes_dir, pubs_dir, catalog


def run_just(
    *args: str, extra_env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(extra_env or {})
    return subprocess.run(
        ["just", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )


def test_assay_mine_preserves_shared_paths_for_both_miners(tmp_path: Path) -> None:
    genes_dir, _pubs_dir, catalog = make_assay_fixture(tmp_path)
    out_dir = tmp_path / "canonical output with spaces"

    result = run_just(
        "assay-mine",
        "--genes-dir",
        str(genes_dir),
        "--catalog",
        str(catalog),
        "--out-dir",
        str(out_dir),
    )

    assert result.returncode == 0, result.stderr
    with (out_dir / "readout_matches.tsv").open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert [row["matched"] for row in rows] == ["UPRE reporter"]
    assert [row["snippet"] for row in rows] == ["UPRE reporter assay"]
    assert len((out_dir / "readout_matches.tsv").read_text().splitlines()) == 2
    with (out_dir / "matched_string_counts.tsv").open(newline="") as handle:
        counts = list(csv.DictReader(handle, delimiter="\t"))
    assert counts == [
        {
            "readout_class": "UPR_ER_STRESS",
            "matched_string": "upre reporter",
            "count": "1",
        }
    ]
    assert (out_dir / "paper_readout_matches.tsv").exists()


def test_assay_mine_supporting_paper_matched_string_counts_once_per_paper(
    tmp_path: Path,
) -> None:
    genes_dir, pubs_dir, catalog = make_assay_fixture(tmp_path)
    out_dir = tmp_path / "supporting output with spaces"

    result = run_just(
        "assay-mine-supporting",
        "--genes-dir",
        str(genes_dir),
        "--pubs-dir",
        str(pubs_dir),
        "--catalog",
        str(catalog),
        "--out-dir",
        str(out_dir),
    )

    assert result.returncode == 0, result.stderr
    with (out_dir / "paper_readout_matches.tsv").open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert [(row["pmid"], row["ref_role"]) for row in rows] == [
        ("2", "supporting")
    ]
    with (out_dir / "paper_matched_string_counts.tsv").open(newline="") as handle:
        counts = list(csv.DictReader(handle, delimiter="\t"))
    assert counts == [
        {
            "readout_class": "UPR_ER_STRESS",
            "matched_string": "upre reporter",
            "papers": "1",
        }
    ]
    assert len(
        (out_dir / "paper_matched_string_counts.tsv").read_text().splitlines()
    ) == 2
    assert sorted(path.name for path in out_dir.iterdir()) == [
        "paper_action_crosstab_aligned.tsv",
        "paper_action_crosstab_all.tsv",
        "paper_matched_string_counts.tsv",
        "paper_readout_matches.tsv",
    ]


def test_supporting_paper_rows_follow_catalog_order_across_hash_seeds(
    tmp_path: Path,
) -> None:
    genes_dir = tmp_path / "ordered genes"
    gene_dir = genes_dir / "TEST" / "GENE"
    gene_dir.mkdir(parents=True)
    (gene_dir / "GENE-ai-review.yaml").write_text(
        """
id: UniProtKB:TEST
gene_symbol: GENE
existing_annotations:
  - term:
      id: GO:0006986
      label: response to unfolded protein
    evidence_type: IDA
    original_reference_id: PMID:1
    review:
      action: ACCEPT
      supported_by:
        - reference_id: PMID:2
"""
    )
    (gene_dir / "GENE-goa.tsv").write_text(
        "GO TERM\tGO ASPECT\nGO:0006986\tbiological_process\n"
    )

    pubs_dir = tmp_path / "ordered publications"
    pubs_dir.mkdir()
    (pubs_dir / "PMID_1.md").write_text(
        "full_text_available: true\nMTT assay and LC3 puncta were measured.\n"
    )
    (pubs_dir / "PMID_2.md").write_text(
        "full_text_available: true\nUPRE reporter and MTT assay were measured.\n"
    )

    catalog = tmp_path / "nonlexical catalog.yaml"
    catalog.write_text(
        r"""
readouts:
  UPR_ER_STRESS:
    patterns: ['\bUPRE reporter']
  VIABILITY_PROLIFERATION:
    patterns: ['\bMTT assay']
  AUTOPHAGY_FLUX:
    patterns: ['\bLC3 puncta']
"""
    )

    outputs = []
    for seed in ("1", "2"):
        out_dir = tmp_path / f"seed {seed} output"
        result = run_just(
            "assay-mine-supporting",
            "--genes-dir",
            str(genes_dir),
            "--pubs-dir",
            str(pubs_dir),
            "--catalog",
            str(catalog),
            "--out-dir",
            str(out_dir),
            extra_env={"PYTHONHASHSEED": seed},
        )
        assert result.returncode == 0, result.stderr
        outputs.append(out_dir / "paper_readout_matches.tsv")

    assert outputs[0].read_bytes() == outputs[1].read_bytes()
    with outputs[0].open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert [
        (row["readout_class"], row["pmid"], row["ref_role"])
        for row in rows
    ] == [
        ("UPR_ER_STRESS", "2", "supporting"),
        ("VIABILITY_PROLIFERATION", "1", "primary"),
        ("AUTOPHAGY_FLUX", "1", "primary"),
    ]
