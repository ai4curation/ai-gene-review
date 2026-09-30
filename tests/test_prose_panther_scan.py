"""Tests for the prose PANTHER claim scan.

The scan had doctest-only coverage for five commits. Its doctests pin the
pairing rule, but nothing exercised ``main``'s three outcomes -- contradicted,
known-absent, and never-looked-up -- and those are what the exit code keys off,
which matters because the exit code is intended to gate CI.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.panther_families import write_member_index
from ai_gene_review.validation.prose_panther_scan import (
    Claim,
    collect_claims,
    extract_claims,
    iter_prose,
    main,
)


@pytest.fixture
def modules_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "modules"
    directory.mkdir()
    return directory


def write_module(directory: Path, name: str, notes: str) -> Path:
    path = directory / name
    path.write_text(yaml.safe_dump({"module": {"id": "m", "notes": notes}}))
    return path


# --------------------------------------------------------------------------- #
# claim extraction
# --------------------------------------------------------------------------- #


def test_iter_prose_reads_prose_slots_only():
    """A PANTHER id in a term label is validated elsewhere; prose is not."""
    document = {
        "notes": "HSD17B4 P51659 PTHR45024",
        "term": {"id": "PANTHER:PTHR1", "label": "not prose"},
        "parts": [{"description": "SCPx P22307 PTHR42870"}],
    }
    assert sorted(iter_prose(document)) == [
        "HSD17B4 P51659 PTHR45024",
        "SCPx P22307 PTHR42870",
    ]


@pytest.mark.parametrize(
    "text,expected",
    [
        # plain adjacency
        ("HSD17B4 (P51659 PTHR45024)", [("P51659", "PTHR45024")]),
        # the id belongs to the protein it follows, not the earlier one
        ("PNP P00491, GO:1); GDA Q9Y2T3 PTHR11271", [("Q9Y2T3", "PTHR11271")]),
        # too far away to be a claim about it
        ("P51659 " + "x" * 40 + " PTHR45024", []),
        # an id with no accession before it is not a claim
        ("the PTHR11493 clade", []),
        # subfamily ids reduce to their family
        ("RDH11 (Q8TC12 PTHR24320:SF227)", [("Q8TC12", "PTHR24320")]),
    ],
)
def test_extract_claims_pairing(text, expected):
    claims = list(extract_claims("m.yaml", text))
    assert [(c.accession, c.claimed_family) for c in claims] == expected


def test_collect_claims_walks_a_directory(modules_dir):
    write_module(modules_dir, "a.yaml", "XDH P47989 PTHR11908")
    write_module(modules_dir, "b.yaml", "nothing here")
    assert collect_claims(modules_dir) == [
        Claim(module="a.yaml", accession="P47989", claimed_family="PTHR11908")
    ]


# --------------------------------------------------------------------------- #
# main(): the three outcomes the exit code keys off
# --------------------------------------------------------------------------- #


def _run(monkeypatch, modules_dir, index, unresolved=None, consulted_uniprot=True):
    """Point the scan at a temporary members file and modules directory."""
    members = modules_dir.parent / "panther-members.tsv"
    write_member_index(index, members, unresolved, consulted_uniprot)
    monkeypatch.setattr(
        "ai_gene_review.validation.prose_panther_scan.REPO_ROOT",
        modules_dir.parent,
    )
    (modules_dir.parent / "interpro" / "panther").mkdir(parents=True, exist_ok=True)
    members.replace(modules_dir.parent / "interpro" / "panther" / "panther-members.tsv")
    return main(["--modules-dir", str(modules_dir)])


def test_main_passes_when_claims_agree(monkeypatch, modules_dir, capsys):
    write_module(modules_dir, "a.yaml", "XDH P47989 PTHR11908")
    code = _run(monkeypatch, modules_dir, {"P47989": "PTHR11908:SF80"})
    assert code == 0
    assert "contradicted                   : 0" in capsys.readouterr().out


def test_main_fails_on_a_contradicted_claim(monkeypatch, modules_dir, capsys):
    write_module(modules_dir, "a.yaml", "XDH P47989 PTHR45444")
    code = _run(monkeypatch, modules_dir, {"P47989": "PTHR11908:SF80"})
    assert code == 1
    assert "PTHR11908:SF80" in capsys.readouterr().out


def test_main_fails_when_an_accession_was_never_looked_up(
    monkeypatch, modules_dir, capsys
):
    """'Could not check' must not read as 'checked and clean'."""
    write_module(modules_dir, "a.yaml", "XDH P47989 PTHR11908")
    code = _run(monkeypatch, modules_dir, {})
    assert code == 1
    assert "NOT checked" in capsys.readouterr().out


def test_main_does_not_fail_when_no_panther_family_exists(
    monkeypatch, modules_dir, capsys
):
    """A lookup that ran and came back empty is a fact, not a gap.

    Treating it as unresolvable would fail the scan permanently while advising a
    refresh that has already been run.
    """
    write_module(modules_dir, "a.yaml", "orphan Q88ND1 PTHR11908")
    code = _run(monkeypatch, modules_dir, {}, unresolved={"Q88ND1"})
    out = capsys.readouterr().out
    assert code == 0
    assert "no PANTHER family exists       : 1" in out
    assert "cannot be adjudicated" in out


def test_main_fails_when_uniprot_was_never_consulted(monkeypatch, modules_dir, capsys):
    """A skipped lookup must not be reported as "no PANTHER family exists".

    The artifact's prose and its machine-readable marker have to agree. With a
    shared marker, a `refresh-panther-members --no-uniprot-fallback` run makes
    the scan announce that PANTHER has no family for a protein nobody asked
    about, and return 0 -- moving the false claim out of the file and into the
    tool output, where it is harder to notice. This is the composition test for
    that pair of fixes.
    """
    write_module(modules_dir, "a.yaml", "orphan Q88ND1 PTHR11908")
    code = _run(
        monkeypatch, modules_dir, {}, unresolved={"Q88ND1"}, consulted_uniprot=False
    )
    out = capsys.readouterr().out

    assert code == 1, "an unchecked accession must not pass"
    assert "no PANTHER family exists       : 0" in out
    assert "unresolvable (not looked up)   : 1" in out
    assert "cannot be adjudicated" not in out


def test_main_does_not_double_count_an_online_resolved_accession(
    monkeypatch, modules_dir, capsys
):
    """--online resolving a recorded-absent accession must move it, not clone it.

    `absent` reads the file while `checked` reads the index after the online
    update, so without a not-in-index guard the same claim is counted under both
    headings and the figures stop partitioning the claim total.
    """
    write_module(modules_dir, "a.yaml", "orphan Q88ND1 PTHR11908")
    monkeypatch.setattr(
        "ai_gene_review.validation.prose_panther_scan.fetch_panther_from_uniprot",
        lambda accessions: {"Q88ND1": "PTHR11908:SF1"},
    )
    members = modules_dir.parent / "interpro" / "panther"
    members.mkdir(parents=True, exist_ok=True)
    write_member_index({}, members / "panther-members.tsv", {"Q88ND1"})
    monkeypatch.setattr(
        "ai_gene_review.validation.prose_panther_scan.REPO_ROOT", modules_dir.parent
    )

    code = main(["--modules-dir", str(modules_dir), "--online"])
    out = capsys.readouterr().out

    assert code == 0
    assert "checked                        : 1" in out
    assert "no PANTHER family exists       : 0" in out, "must not be counted twice"
    assert "unresolvable (not looked up)   : 0" in out
