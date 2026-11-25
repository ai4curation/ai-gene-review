"""Tests for scripts/export_goa_changeset.py (the GOA change-set exporter)."""

import csv
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "export_goa_changeset.py"


def _load():
    spec = importlib.util.spec_from_file_location("export_goa_changeset", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REVIEW = """\
id: P00001
gene_symbol: GENE1
existing_annotations:
  - term: {id: GO:0005788, label: endoplasmic reticulum lumen}
    qualifier: located_in
    evidence_type: IEA
    original_reference_id: GO_REF:0000044
    review: {action: ACCEPT}
  - term: {id: GO:0003674, label: molecular_function}
    qualifier: enables
    evidence_type: ND
    original_reference_id: GO_REF:0000015
    retired: true
    review: {action: REMOVE}
  - term: {id: GO:0016301, label: kinase activity}
    qualifier: enables
    evidence_type: IBA
    original_reference_id: GO_REF:0000033
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: NTR, label: proposed specific kinase activity}
  - term: {id: GO:0004672, label: protein kinase activity}
    qualifier: enables
    evidence_type: IEA
    original_reference_id: GO_REF:0000002
    negated: true
    isoform: P00001-2
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: GO:0004674, label: protein serine/threonine kinase activity}
  - term: {id: GO:0004553, label: hydrolase activity, hydrolyzing O-glycosyl compounds}
    qualifier: enables
    evidence_type: IEA
    original_reference_id: GO_REF:0000002
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: GO:0106407, label: Glc2Man9GlcNAc2 oligosaccharide glucosidase activity}
        - {id: NTR, label: proposed second-step glucosidase activity}
        - {id: NTR, label: another proposed activity}
  - term: {id: NTR, label: proposed process}
    qualifier: involved_in
    evidence_type: NEW
    original_reference_id: PMID:2
    review: {action: NEW}
  - term: {id: GO:0004674, label: protein serine/threonine kinase activity}
    qualifier: enables
    evidence_type: NEW
    original_reference_id: PMID:1
    review: {action: NEW}
core_functions:
  - molecular_function: {id: GO:0004674, label: protein serine/threonine kinase activity}
    locations:
      - {id: GO:0005788, label: endoplasmic reticulum lumen}
"""


def _write_genes(tmp_path, files):
    for name, text in files.items():
        folder = tmp_path / "genes" / "human" / name
        folder.mkdir(parents=True)
        (folder / f"{name}-ai-review.yaml").write_text(text)


def _read(path):
    lines = [line for line in path.read_text().splitlines() if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def test_rows_carry_qualifier_retired_and_ntr(tmp_path):
    mod = _load()
    _write_genes(tmp_path, {"GENE1": REVIEW})
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 0
    rows = {r["term_id"]: r for r in _read(out)}
    assert rows["GO:0005788"]["qualifier"] == "located_in"
    assert rows["GO:0005788"]["is_core_function_term"] == "true"
    assert rows["GO:0003674"]["retired"] == "true"
    assert rows["GO:0016301"]["replacement_term_ids"] == "NTR"
    assert rows["GO:0016301"]["replacement_is_proposed_term"] == "true"
    assert rows["GO:0004672"]["replacement_term_ids"] == "GO:0004674"
    assert rows["GO:0004672"]["replacement_is_proposed_term"] == ""
    assert rows["GO:0004672"]["negated"] == "true"
    assert rows["GO:0004672"]["isoform"] == "P00001-2"
    assert rows["GO:0004553"]["replacement_term_ids"] == "GO:0106407|NTR"
    assert rows["GO:0004553"]["replacement_is_proposed_term"] == ""
    assert rows["NTR"]["term_is_proposed_term"] == "true"
    assert rows["GO:0004674"]["term_is_proposed_term"] == ""
    assert rows["GO:0004674"]["action"] == "NEW"
    assert rows["GO:0004674"]["qualifier"] == "enables"
    assert out.read_text().startswith("# ai-gene-review commit: ")


def test_unreadable_file_fails_and_leaves_no_output(tmp_path):
    mod = _load()
    _write_genes(tmp_path, {"GENE1": REVIEW, "GENE2": "- just\n- a list\n"})
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 1
    assert not out.exists()
    out.write_text("previous good export\n")
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 1
    assert out.read_text() == "previous good export\n"
    assert not list(tmp_path.glob(".out.tsv.*.tmp"))


def test_missing_organism_directory_is_an_error(tmp_path):
    mod = _load()
    (tmp_path / "genes").mkdir()
    out = tmp_path / "out.tsv"
    argv = ["--genes-dir", str(tmp_path / "genes"), "--organism", "hmuan", "-o", str(out)]
    assert mod.main(argv) == 2
    assert not out.exists()


def test_empty_organism_directory_leaves_previous_export_untouched(tmp_path):
    mod = _load()
    (tmp_path / "genes" / "human").mkdir(parents=True)
    out = tmp_path / "out.tsv"
    out.write_text("previous good export\n")
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 2
    assert out.read_text() == "previous good export\n"


def test_output_is_world_readable(tmp_path):
    mod = _load()
    _write_genes(tmp_path, {"GENE1": REVIEW})
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 0
    assert out.stat().st_mode & 0o777 == 0o644


ORDERING_REVIEW = """\
id: P00002
gene_symbol: GENE2
existing_annotations:
  - term: {id: GO:0016787, label: hydrolase activity}
    evidence_type: IEA
    original_reference_id: GO_REF:0000002
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: NTR, label: proposed activity}
        - {id: GO:0004553, label: hydrolase activity, hydrolyzing O-glycosyl compounds}
  - term: {id: GO:0016301, label: kinase activity}
    evidence_type: IEA
    original_reference_id: GO_REF:0000002
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: GO:0004674, label: protein serine/threonine kinase activity}
        - {id: GO:0004713, label: protein tyrosine kinase activity}
  - term: {id: GO:0003824, label: catalytic activity}
    evidence_type: IEA
    original_reference_id: GO_REF:0000002
    review:
      action: MODIFY
      proposed_replacement_terms:
        - {id: NEW_TERM_001, label: proposed catalytic activity}
"""


def test_replacements_keep_order_and_pass_unknown_ids_through(tmp_path):
    mod = _load()
    _write_genes(tmp_path, {"GENE2": ORDERING_REVIEW})
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 0
    rows = {r["term_id"]: r for r in _read(out)}
    # NTR listed before a GO replacement: order kept, a GO id remains.
    assert rows["GO:0016787"]["replacement_term_ids"] == "NTR|GO:0004553"
    assert rows["GO:0016787"]["replacement_is_proposed_term"] == ""
    # Two GO replacements, in review order.
    assert rows["GO:0016301"]["replacement_term_ids"] == "GO:0004674|GO:0004713"
    # A non-GO placeholder other than NTR is passed through verbatim.
    assert rows["GO:0003824"]["replacement_term_ids"] == "NEW_TERM_001"
    assert rows["GO:0003824"]["replacement_is_proposed_term"] == "true"
