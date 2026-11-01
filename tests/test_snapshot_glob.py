"""Indexed snapshot globs retain the existing path-matching contract."""

import subprocess

import pytest

from ai_gene_review import source_tree as st


@pytest.fixture
def snapshot(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(
        ["git", "-c", "user.name=Test", "-c", "user.email=test@example.org",
         "commit", "--allow-empty", "-qm", "fixture"], cwd=tmp_path, check=True
    )
    tree = st.GitSnapshot(tmp_path, "HEAD")
    # Path matching does not read blobs. Include nested paths, punctuation,
    # Unicode, and neighboring names to exercise prefix boundaries.
    tree.__dict__["_blobs"] = dict.fromkeys([
        "genes/human/TP53/TP53-goa.tsv", "genes/human/TP53/sub/data.yaml",
        "genes/human/TP53extra/TP53extra-goa.tsv", "genes/human/TP54/file.yaml",
        "genes/fly/dl/dl-goa.tsv", "genes/fly/Dl/Dl-goa.tsv",
        "genes/αβ/file.yaml", "genes/bracket[1]/file.yaml", "genes/root.yaml",
        "reports/a.yaml", "reports/a.yml", "root.yaml", "space name.txt",
    ], "unused-blob-id")
    return tree


@pytest.mark.parametrize("pattern", [
    "genes/*/*/*-goa.tsv", "genes/**/*-goa.tsv", "genes/**", "**/*.yaml",
    "genes/human/TP53/*-goa.tsv", "genes/human/TP53/**", "genes/human/TP5?/*",
    "genes/fly/[dD]l/*", "genes/fly/[!D]l/*", "genes/bracket[[]1]/*",
    "genes/αβ/*", "root.yaml", "space name.txt", "*.yaml", "*", "",
    "missing/*", "genes/human/TP53/", "genes/[broken/*",
])
def test_indexed_glob_matches_full_scan(snapshot, pattern):
    expected = sorted(path for path in snapshot._blobs if st.match_path(path, pattern))
    assert snapshot.glob(pattern) == expected
    assert snapshot.glob(pattern) == expected


def test_literal_prefix_narrows_work_and_results_are_defensive_copies(snapshot, monkeypatch):
    checked = []
    original = st.match_path
    def record(path, pattern):
        checked.append(path)
        return original(path, pattern)
    monkeypatch.setattr(st, "match_path", record)
    pattern = "genes/human/TP53/*-goa.tsv"
    first = snapshot.glob(pattern)
    assert first == ["genes/human/TP53/TP53-goa.tsv"]
    assert len(checked) == 2
    assert all(path.startswith("genes/human/TP53/") for path in checked)
    first.clear()
    assert snapshot.glob(pattern) == ["genes/human/TP53/TP53-goa.tsv"]
    assert len(checked) == 2


def test_cache_is_per_snapshot(snapshot, tmp_path):
    pattern = "genes/**/*-goa.tsv"
    assert snapshot.glob(pattern)
    other = st.GitSnapshot(tmp_path, "HEAD")
    assert other.glob(pattern) == []
