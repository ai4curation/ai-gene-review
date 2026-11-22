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
    assert rows["GO:0004674"]["action"] == "NEW"
    assert rows["GO:0004674"]["qualifier"] == "enables"
    assert out.read_text().startswith("# ai-gene-review commit: ")


def test_unreadable_file_fails_and_leaves_no_output(tmp_path):
    mod = _load()
    _write_genes(tmp_path, {"GENE1": REVIEW, "GENE2": "- just\n- a list\n"})
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "-o", str(out)]) == 1
    assert not out.exists()
    assert not list(tmp_path.glob(".out.tsv.*.tmp"))


def test_missing_organism_directory_is_an_error(tmp_path):
    mod = _load()
    (tmp_path / "genes").mkdir()
    out = tmp_path / "out.tsv"
    assert mod.main(["--genes-dir", str(tmp_path / "genes"), "--organism", "hmuan", "-o", str(out)]) == 2
    assert not out.exists()
