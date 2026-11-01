"""Tests for the proposed-ontology-change exporter (upstream term-tracker requests)."""

import csv
from pathlib import Path

import pytest

from ai_gene_review.tools.export_ontology_changes import (
    COLUMNS,
    collect,
    render_report,
    write_outputs,
)

GENE_REVIEW = """
id: Q96RI1
gene_symbol: NR1H4
proposed_ontology_changes:
- change_type: NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT
  ontology: GO
  about_node:
    id: GO:0010903
    label: negative regulation of very-low-density lipoprotein particle remodeling
  has_nondirect_replacement:
  - id: GO:0070328
    label: triglyceride homeostasis
  justification: Remodeling is post-secretory; the evidence is about secretion.
  confidence: PROBABLE
  affected_annotations:
  - genes/human/NR1H4/NR1H4-ai-review.yaml
  supported_by:
  - reference_id: PMID:27471003
    supporting_text: CDCA treatment lowered hepatic VLDL-TG secretion
"""

MODULE_REVIEW = """
id: MODULE:vesicle_tethering
title: Vesicle tethering
module:
  id: MODULE:vesicle_tethering
proposed_ontology_changes:
- change_type: NODE_OBSOLETION_WITH_DIRECT_REPLACEMENT
  ontology: GO
  about_node:
    id: GO:0099022
    label: vesicle tethering
  has_direct_replacement:
    id: GO:7770062
    label: vesicle membrane tethering activity
  change_dsl: obsolete GO:0099022 with replacement GO:7770062
  justification: Tethering is a binding activity, not a process.
  confidence: CONFIRMED
  report_status: REPORTED
  term_tracker_issue: https://github.com/geneontology/go-ontology/issues/1
- change_type: REMOVE_MAPPING
  ontology: GO
  about_node:
    id: GO:0090522
    label: vesicle tethering involved in exocytosis
  old_value: InterPro:IPR007225
  justification: The InterPro2GO mapping sends annotations to a term being obsoleted.
  confidence: PROBABLE
"""

UBERON_REVIEW = """
id: P00001
gene_symbol: FAKE
proposed_ontology_changes:
- change_type: NODE_RENAME
  ontology: UBERON
  about_node:
    id: UBERON:0000001
    label: old label
  old_value: old label
  new_value: new label
  justification: The label is miscased.
  confidence: SUSPECTED
"""


@pytest.fixture
def root(tmp_path: Path) -> Path:
    """A miniature repository holding one gene review and one module review."""
    gene = tmp_path / "genes" / "human" / "NR1H4"
    gene.mkdir(parents=True)
    (gene / "NR1H4-ai-review.yaml").write_text(GENE_REVIEW)
    other = tmp_path / "genes" / "human" / "FAKE"
    other.mkdir(parents=True)
    (other / "FAKE-ai-review.yaml").write_text(UBERON_REVIEW)
    modules = tmp_path / "modules"
    modules.mkdir()
    (modules / "vesicle_tethering.yaml").write_text(MODULE_REVIEW)
    return tmp_path


def test_collect_finds_changes_in_gene_and_module_reviews(root: Path):
    rows = collect(root)
    assert len(rows) == 4
    assert {r["about_node"] for r in rows} == {
        "GO:0010903",
        "GO:0099022",
        "GO:0090522",
        "UBERON:0000001",
    }


def test_rows_carry_their_source_path(root: Path):
    rows = collect(root)
    by_term = {r["about_node"]: r for r in rows}
    assert by_term["GO:0099022"]["source_path"] == "modules/vesicle_tethering.yaml"
    assert (
        by_term["GO:0010903"]["source_path"] == "genes/human/NR1H4/NR1H4-ai-review.yaml"
    )


def test_gene_symbol_is_recorded_for_gene_reviews_only(root: Path):
    by_term = {r["about_node"]: r for r in collect(root)}
    assert by_term["GO:0010903"]["gene_symbol"] == "NR1H4"
    assert by_term["GO:0099022"]["gene_symbol"] == ""


def test_report_status_defaults_to_not_reported(root: Path):
    by_term = {r["about_node"]: r for r in collect(root)}
    assert by_term["GO:0010903"]["report_status"] == "NOT_REPORTED"
    assert by_term["GO:0099022"]["report_status"] == "REPORTED"


def test_dsl_is_generated_when_absent_and_kept_when_given(root: Path):
    by_term = {r["about_node"]: r for r in collect(root)}
    # given verbatim in the module review
    assert by_term["GO:0099022"]["change_dsl"] == (
        "obsolete GO:0099022 with replacement GO:7770062"
    )
    # derived for the gene review, which did not state one
    assert by_term["GO:0010903"]["change_dsl"] == "obsolete GO:0010903"


def test_rows_are_grouped_by_ontology(root: Path):
    rows = collect(root)
    assert {r["ontology"] for r in rows} == {"GO", "UBERON"}


def test_collect_is_sorted_stably(root: Path):
    assert collect(root) == collect(root)


def test_write_outputs_writes_a_tsv_and_one_report_per_ontology(
    root: Path, tmp_path: Path
):
    tsv = tmp_path / "out" / "changes.tsv"
    reports = tmp_path / "out" / "changes"
    rows = write_outputs(root, tsv, reports)
    assert len(rows) == 4
    with tsv.open() as fh:
        read = list(csv.DictReader(fh, delimiter="\t"))
    assert len(read) == 4
    assert list(read[0]) == COLUMNS
    assert (reports / "GO.md").is_file()
    assert (reports / "UBERON.md").is_file()


def test_report_names_the_change_and_its_justification(root: Path):
    rows = [r for r in collect(root) if r["ontology"] == "GO"]
    md = render_report("GO", rows)
    assert "GO:0099022" in md
    assert "obsolete GO:0099022 with replacement GO:7770062" in md
    assert "Tethering is a binding activity" in md
    assert "CDCA treatment lowered hepatic VLDL-TG secretion" in md


def test_report_lists_affected_annotations(root: Path):
    rows = [r for r in collect(root) if r["ontology"] == "GO"]
    md = render_report("GO", rows)
    assert "genes/human/NR1H4/NR1H4-ai-review.yaml" in md


def test_report_links_a_filed_tracker_issue(root: Path):
    rows = [r for r in collect(root) if r["ontology"] == "GO"]
    md = render_report("GO", rows)
    assert "https://github.com/geneontology/go-ontology/issues/1" in md


def test_report_excludes_fixed_and_declined_changes():
    base = {c: "" for c in COLUMNS}
    rows = [
        {
            **base,
            "ontology": "GO",
            "about_node": "GO:1",
            "report_status": "FIXED",
            "justification": "done",
            "change_type": "NODE_RENAME",
        },
        {
            **base,
            "ontology": "GO",
            "about_node": "GO:2",
            "report_status": "NOT_REPORTED",
            "justification": "open",
            "change_type": "NODE_RENAME",
        },
    ]
    md = render_report("GO", rows)
    assert "GO:2" in md
    assert "GO:1" not in md


def test_a_repo_with_no_changes_yields_nothing(tmp_path: Path):
    (tmp_path / "genes").mkdir()
    assert collect(tmp_path) == []


def test_a_mapping_removal_does_not_render_an_arrow_to_nothing():
    """REMOVE_MAPPING has no new value, so `X → ` would be noise."""
    base = {c: "" for c in COLUMNS}
    rows = [
        {
            **base,
            "ontology": "GO",
            "about_node": "GO:1",
            "change_type": "REMOVE_MAPPING",
            "old_value": "InterPro:IPR1",
            "report_status": "NOT_REPORTED",
            "justification": "Sends IEAs to an obsolete term.",
            "supported_by": "[]",
        }
    ]
    md = render_report("GO", rows)
    assert "**Mapping to remove:** `InterPro:IPR1`" in md
    assert "→" not in md


def test_a_value_change_still_renders_the_arrow():
    base = {c: "" for c in COLUMNS}
    rows = [
        {
            **base,
            "ontology": "GO",
            "about_node": "GO:1",
            "change_type": "NODE_RENAME",
            "old_value": "old",
            "new_value": "new",
            "report_status": "NOT_REPORTED",
            "justification": "Miscased.",
            "supported_by": "[]",
        }
    ]
    assert "`old` → `new`" in render_report("GO", rows)


PROJECT_PAGE = """---
title: Vesicle tethering obsoletion
proposed_ontology_changes:
- change_type: NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT
  ontology: GO
  about_node:
    id: GO:0099044
    label: vesicle tethering to endoplasmic reticulum
  has_nondirect_replacement:
  - id: GO:7770062
    label: vesicle membrane tethering activity
  justification: Tethering is a binding activity, not a process.
  confidence: CONFIRMED
  report_status: FIXED
- change_type: NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT
  ontology: GO
  about_node:
    id: GO:0099069
    label: synaptic vesicle tethering involved in synaptic vesicle exocytosis
  justification: Same rationale as its parent term.
  confidence: CONFIRMED
---

# Body text
"""

MALFORMED_PROJECT_PAGE = """---
title: Broken
proposed_ontology_changes:
- change_type: NOT_A_REAL_TYPE
  ontology: GO
  about_node:
    id: GO:0000001
    label: x
  justification: nope
  confidence: PROBABLE
---

# Body
"""


def test_project_page_frontmatter_is_collected(tmp_path: Path):
    (tmp_path / "projects").mkdir()
    (tmp_path / "projects" / "VESICLE.md").write_text(PROJECT_PAGE)
    rows = collect(tmp_path)
    assert {r["about_node"] for r in rows} == {"GO:0099044", "GO:0099069"}
    assert all(r["source_path"] == "projects/VESICLE.md" for r in rows)


def test_project_pages_in_subfolders_are_collected(tmp_path: Path):
    nested = tmp_path / "projects" / "VESICLE"
    nested.mkdir(parents=True)
    (nested / "sub.md").write_text(PROJECT_PAGE)
    rows = collect(tmp_path)
    assert len(rows) == 2
    assert rows[0]["source_path"] == "projects/VESICLE/sub.md"


def test_a_malformed_project_entry_is_not_exported(tmp_path: Path):
    """The renderer reports it as a page warning; the exporter must not ship it."""
    (tmp_path / "projects").mkdir()
    (tmp_path / "projects" / "BROKEN.md").write_text(MALFORMED_PROJECT_PAGE)
    assert collect(tmp_path) == []


def test_a_project_page_without_changes_is_skipped(tmp_path: Path):
    (tmp_path / "projects").mkdir()
    (tmp_path / "projects" / "PLAIN.md").write_text("---\ntitle: x\n---\n# Body\n")
    assert collect(tmp_path) == []


def test_project_rows_carry_no_gene_symbol(tmp_path: Path):
    (tmp_path / "projects").mkdir()
    (tmp_path / "projects" / "VESICLE.md").write_text(PROJECT_PAGE)
    assert all(r["gene_symbol"] == "" for r in collect(tmp_path))
