from pathlib import Path

from ai_gene_review.tools import fetch_gene_panther_family


def _write_uniprot(base_path: Path, organism: str, gene: str, text: str) -> None:
    gene_dir = base_path / "genes" / organism / gene
    gene_dir.mkdir(parents=True)
    (gene_dir / f"{gene}-uniprot.txt").write_text(text, encoding="utf-8")


def test_find_panther_family_reads_cached_uniprot(tmp_path: Path) -> None:
    _write_uniprot(
        tmp_path,
        "yeast",
        "YDJ1",
        "DR   PANTHER; PTHR43888; DNAJ-LIKE-2, ISOFORM A-RELATED; 1.\n",
    )

    assert (
        fetch_gene_panther_family.find_panther_family("yeast", "YDJ1", tmp_path)
        == "PTHR43888"
    )


def test_main_fetches_resolved_family(tmp_path: Path, monkeypatch) -> None:
    _write_uniprot(
        tmp_path,
        "yeast",
        "YDJ1",
        "DR   PANTHER; PTHR43888; DNAJ-LIKE-2, ISOFORM A-RELATED; 1.\n",
    )
    calls: list[tuple[str, Path]] = []

    def fake_fetch(family_id: str, base_path: Path) -> bool:
        calls.append((family_id, base_path))
        return True

    monkeypatch.setattr(
        fetch_gene_panther_family,
        "_fetch_panther_family_data",
        fake_fetch,
    )

    result = fetch_gene_panther_family.main(
        ["yeast", "YDJ1", "--base-path", str(tmp_path)]
    )

    assert result == 0
    assert calls == [("PTHR43888", tmp_path)]


def test_main_fails_when_uniprot_record_is_missing(
    tmp_path: Path, capsys
) -> None:
    result = fetch_gene_panther_family.main(
        ["yeast", "YDJ1", "--base-path", str(tmp_path)]
    )

    assert result == 1
    assert "UniProt record not found" in capsys.readouterr().err
