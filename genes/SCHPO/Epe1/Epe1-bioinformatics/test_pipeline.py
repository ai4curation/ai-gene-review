#!/usr/bin/env python3
"""
Tests for the feature-driven JmjC pipeline.

They check that domain boundaries and Fe(II) ligands are read from UniProt
features (not guessed from an H.[DE] motif), that the same code gives the
canonical H-(D/E)-H ligand set for an active demethylase, and that the
analysis scripts no longer carry the retracted hardcoded conclusions.

Run with:  uv run python -m pytest -q test_pipeline.py   (or: just test)
"""

import importlib.util
import re
from pathlib import Path

import pytest

from uniprot_features import ligand_residues, parse_uniprot_json, parse_uniprot_txt

HERE = Path(__file__).parent
EPE1_TXT = HERE.parent / "Epe1-uniprot.txt"
SCRIPTS = ["02_jmjc_domain_analysis.py", "03_conservation_analysis.py",
           "04_functional_regions_analysis.py", "05_structural_features.py"]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), HERE / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_epe1_features_from_uniprot():
    feats = parse_uniprot_txt(EPE1_TXT)
    assert feats["jmjc"] == (243, 402)
    assert ligand_residues(feats) == ["H297", "E299"]
    (pos, expected, found), = feats["caution_positions"]
    assert (pos, expected, found) == (370, "His", "Tyr")
    assert feats["sequence"][pos - 1] == "Y"


@pytest.mark.skipif(not (HERE / "data" / "kdm4a_human.json").exists(),
                    reason="run 01_fetch_sequences.py first")
def test_active_demethylase_has_canonical_triad():
    rec = parse_uniprot_json(HERE / "data" / "kdm4a_human.json")
    assert rec["accession"] == "O75164"
    residues = [rec["sequence"][p - 1] for p in rec["fe_ligands"]]
    assert len(residues) == 3
    assert residues[0] == "H" and residues[1] in "DE" and residues[2] == "H"


def test_motif_scan_hit_at_280_is_not_the_iron_site():
    hits = load_script("02_jmjc_domain_analysis.py").motif_hits(parse_uniprot_txt(EPE1_TXT))
    labelled = {pos: is_fe for pos, _motif, is_fe in hits}
    assert labelled[280] is False  # H280-V281-D282: a motif match, not a ligand
    assert labelled[297] is True   # H297 is the annotated Fe ligand


@pytest.mark.parametrize("script", SCRIPTS)
def test_no_retracted_hardcoded_conclusions(script):
    text = (HERE / script).read_text(encoding="utf-8")
    for phrase in ["HVD motif at position", "Non-catalytic JmjC", "non-catalytic JmjC domain",
                   "catalytic activity lost", "Pseudo-enzyme?", "abolishes catalytic activity"]:
        assert phrase not in text, f"{script} still contains {phrase!r}"
    assert not re.search(r'jmjc_start\s*=\s*\d', text), f"{script} hardcodes a JmjC start"


if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__]))
