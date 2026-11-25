"""Tests for the optional sequence-only read (ai_gene_review.sequence_read).

No model is called: the CLI tests point ``--claude-bin`` at a stub that answers
the two prompts deterministically from the sequence it is given.
"""

import json
import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.sequence_read import core

PTEN_UNIPROT = Path("genes/human/PTEN/PTEN-uniprot.txt")
STUB = Path("tests/input/sequence_read/stub_claude.py").resolve()


@pytest.fixture
def pten() -> core.ProteinRecord:
    return core.read_uniprot(PTEN_UNIPROT)


@pytest.fixture
def genes_root(tmp_path: Path, pten: core.ProteinRecord, monkeypatch) -> Path:
    d = tmp_path / "human" / "PTEN"
    d.mkdir(parents=True)
    shutil.copy(PTEN_UNIPROT, d / "PTEN-uniprot.txt")
    monkeypatch.setenv("SEQREAD_STUB_REAL", pten.sequence)
    return tmp_path


def test_prompts_are_fs2f_verbatim():
    """The prompts must stay identical to the benchmarked ones (fs2f @ 442bd92)."""
    # SHA-256 of the string P in experiments/features/ask.py and experiments/pseudo/ask.py,
    # computed from those files in a checkout of fable-sequence-to-function at 442bd92
    # (not from this module), so a match shows the constants are that text verbatim.
    assert (
        core.sha256(core.FEAT_PROMPT)
        == "b03b98845ad2ebd1e169fb60b413fee9c5ab657df3087b046ae444f81243661e"
    )
    assert (
        core.sha256(core.PSEUDO_PROMPT)
        == "bfad171fd98e297ef954bca9cedda4e005c462f0e026188ee9f26fd666b57fe5"
    )


def test_choose_probe_targets_active_site_and_avoids_sites(pten: core.ProteinRecord):
    wt = {
        "enzyme_family": "protein tyrosine phosphatase",
        "catalytic_residues": [
            {"role": "nucleophile", "residue": "C", "position": 124}
        ],
        "substituted_or_missing": [],
    }
    probe, why = core.choose_probe(pten, wt)
    assert probe is not None, why
    assert (probe.target_position, probe.target_residue, probe.new_residue) == (
        124,
        "C",
        "A",
    )
    assert probe.target_source == "UniProt ACT_SITE"
    assert probe.decoy_position is not None
    assert pten.sequence[probe.decoy_position - 1] == "C"
    sites = [
        p for f in pten.of_type(*core.SITE_FEATURES) for p in range(f.start, f.end + 1)
    ]
    assert all(abs(probe.decoy_position - p) > core.DECOY_MARGIN for p in sites)
    # deterministic
    assert core.choose_probe(pten, wt)[0] == probe


def test_choose_probe_uses_model_residue_only_if_present(pten: core.ProteinRecord):
    no_site = core.ProteinRecord(
        accession="X", sequence=pten.sequence, crc64="", sequence_version=1
    )
    wrong = {
        "enzyme_family": "x",
        "catalytic_residues": [{"residue": "H", "position": 124}],
    }
    assert core.choose_probe(no_site, wrong)[0] is None
    right = {
        "enzyme_family": "x",
        "catalytic_residues": [{"residue": "C", "position": 124}],
    }
    probe = core.choose_probe(no_site, right)[0]
    assert probe is not None and probe.target_source.startswith("residue named")


@pytest.mark.parametrize(
    "wt,mut,decoy,mrep,drep,verdict",
    [
        ("yes", "no", "yes", True, False, "TRACKS_CATALYTIC_RESIDUE"),
        ("yes", "yes", "yes", True, False, "REPORTS_BUT_NOT_INACTIVE"),
        ("yes", "uncertain", "yes", True, False, "REPORTS_BUT_NOT_INACTIVE"),
        ("yes", "no", "no", True, False, "REJECTS_ANY_CHANGE"),
        ("yes", "yes", "yes", False, False, "INSENSITIVE"),
        ("no", "no", "no", False, False, "WILD_TYPE_NOT_CALLED_ACTIVE"),
        ("yes", None, "yes", False, False, "INCOMPLETE"),
    ],
)
def test_probe_verdict(wt, mut, decoy, mrep, drep, verdict):
    assert core.probe_verdict(wt, mut, decoy, mrep, drep) == verdict


def test_cli_run_with_stub(genes_root: Path):
    runner = CliRunner()
    args = [
        "sequence-read",
        "run",
        "human",
        "PTEN",
        "--claude-bin",
        str(STUB),
        "--no-interpro",
        "--model",
        "stub-model",
        "--genes-root",
        str(genes_root),
    ]
    res = runner.invoke(app, args)
    assert res.exit_code == 0, res.output
    out = genes_root / "human/PTEN/PTEN-bioinformatics/sequence-read"
    doc = json.loads((out / "stub-model-high.json").read_text())
    conds = sorted(c["condition"] for c in doc["calls"])
    assert conds == ["catalytic_mutant", "decoy", "real", "shuffled", "wild_type"]
    assert all(core.usable(c) for c in doc["calls"])
    assert doc["checks"]["shuffled"]["pfam_domains"] == 0
    assert doc["checks"]["features"]["pfam"][0]["verdict"] == "IN_UNIPROT"
    assert doc["checks"]["probe"]["target"] == "C124A"
    assert doc["checks"]["probe"]["verdict"] == "TRACKS_CATALYTIC_RESIDUE"
    act = doc["checks"]["activity"]["catalytic_residues"][0]
    assert act["present_in_sequence"] and act["uniprot"] == "ACT_SITE"
    results = (out / "RESULTS.md").read_text()
    assert "**Not literature evidence.**" in results
    assert "- Probe verdict: TRACKS_CATALYTIC_RESIDUE" in results
    # A second run for the same model and effort is refused without --force.
    again = runner.invoke(app, args)
    assert again.exit_code != 0
    assert "--force" in again.output
    # render alone needs no model
    res = runner.invoke(
        app,
        ["sequence-read", "render", "human", "PTEN", "--genes-root", str(genes_root)],
    )
    assert res.exit_code == 0, res.output


def test_cli_run_requires_uniprot_file(tmp_path: Path):
    res = CliRunner().invoke(
        app,
        ["sequence-read", "run", "human", "NOPE", "--genes-root", str(tmp_path)],
    )
    assert res.exit_code != 0
    assert "fetch-gene" in res.output


def test_choose_probe_prefers_acidic_binding_residue():
    """With no ACT_SITE (ADPRH), an acidic UniProt BINDING residue beats list order."""
    adprh = core.read_uniprot(Path("genes/human/ADPRH/ADPRH-uniprot.txt"))
    assert not adprh.of_type("ACT_SITE")
    wt = {
        "enzyme_family": "ADP-ribosylhydrolase",
        "catalytic_residues": [
            {"role": "Mg2+ coordination", "residue": "S", "position": 54},
            {"role": "Mg2+ coordination", "residue": "D", "position": 55},
        ],
    }
    probe = core.choose_probe(adprh, wt)[0]
    assert probe is not None
    assert probe.label(probe.target_position) == "D55A"
