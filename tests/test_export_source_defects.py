"""Tests for the source-defect exporter (upstream reporting of source-record errors)."""

import csv
from pathlib import Path

import pytest

from ai_gene_review.tools.export_source_defects import collect, render_report, write_outputs

GENE_REVIEW = """
id: P42760
gene_symbol: GSTF6
existing_annotations:
- term:
    id: GO:2001147
    label: camalexin binding
  evidence_type: IDA
  original_reference_id: PMID:21631432
  qualifier: enables
  review:
    summary: s
    action: UNDECIDED
    source_defects:
    - defect_type: WRONG_GENE_PRODUCT
      resource: TAIR
      asserted_value: UniProtKB:P42760
      corrected_value: UniProtKB:Q9SLM6
      corrected_label: GSTF3
      cause: LEGACY_ALIAS
      confidence: PROBABLE
      explanation: Legacy alias mapped to the wrong locus.
      supported_by:
      - reference_id: PMID:21631432
        supporting_text: GSTF2 and GSTF3
- term:
    id: GO:0005737
    label: cytoplasm
  evidence_type: IDA
  original_reference_id: PMID:1
  review:
    summary: s
    action: ACCEPT
"""

GOCAM_REVIEW = """
id: gomodel:1
activity_reviews:
- activity_id: gomodel:1/2
  gene_product: AGI_LocusCode:AT2G45160
  molecular_function: GO:0043995
  source_defects:
  - defect_type: WRONG_GENE_PRODUCT
    resource: GO_CAM
    asserted_value: AGI_LocusCode:AT2G45160
    corrected_value: AGI_LocusCode:AT5G64610
    confidence: CONFIRMED
    explanation: Symbol collision.
    report_status: FIXED
"""


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    gene = tmp_path / "genes" / "ARATH" / "GSTF6"
    gene.mkdir(parents=True)
    (gene / "GSTF6-ai-review.yaml").write_text(GENE_REVIEW, encoding="utf-8")
    other = tmp_path / "genes" / "ARATH" / "NONE"
    other.mkdir(parents=True)
    (other / "NONE-ai-review.yaml").write_text("id: X\n", encoding="utf-8")
    model = tmp_path / "gocams" / "1"
    model.mkdir(parents=True)
    (model / "1-review.yaml").write_text(GOCAM_REVIEW, encoding="utf-8")
    return tmp_path


def test_collect_reads_gene_and_gocam_defects(repo: Path) -> None:
    rows = collect(repo)
    assert [r["resource"] for r in rows] == ["GO_CAM", "TAIR"]
    gocam, tair = rows
    assert gocam["record"] == "gomodel:1/2"
    assert gocam["subject_id"] == "AGI_LocusCode:AT2G45160"
    assert tair["subject_id"] == "UniProtKB:P42760"
    assert tair["term_id"] == "GO:2001147"
    assert tair["original_reference_id"] == "PMID:21631432"
    assert tair["report_status"] == "NOT_REPORTED"


def test_report_omits_fixed_defects(repo: Path) -> None:
    rows = collect(repo)
    gocam_md = render_report("GO_CAM", [r for r in rows if r["resource"] == "GO_CAM"])
    assert "0 open defect(s)" in gocam_md
    tair_md = render_report("TAIR", [r for r in rows if r["resource"] == "TAIR"])
    assert "UniProtKB:P42760 → UniProtKB:Q9SLM6 (GSTF3)" in tair_md
    assert "> GSTF2 and GSTF3" in tair_md


def test_write_outputs_writes_tsv_and_one_report_per_resource(repo: Path) -> None:
    tsv = repo / "out" / "d.tsv"
    report_dir = repo / "out" / "reports"
    write_outputs(repo, tsv, report_dir)
    with tsv.open(encoding="utf-8") as fh:
        assert len(list(csv.DictReader(fh, delimiter="\t"))) == 2
    assert sorted(p.name for p in report_dir.iterdir()) == ["GO_CAM.md", "TAIR.md"]
