import importlib.util
import sqlite3
import sys
from pathlib import Path

import pytest


SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_fitness_data.py"
SPEC = importlib.util.spec_from_file_location("fetch_fitness_data", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
fitness = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fitness)


def prepare_gene(tmp_path: Path) -> Path:
    gene_dir = tmp_path / "genes" / "ECOLI" / "SlyD"
    gene_dir.mkdir(parents=True)
    return gene_dir


def stub_empty_queries(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(fitness, "query_sqlite", lambda *_: None)
    monkeypatch.setattr(fitness, "query_html_dir", lambda *_: None)
    monkeypatch.setattr(fitness, "try_bulk_download", lambda *_: None)
    monkeypatch.setattr(fitness, "resolve_locus_tag", lambda *_: "b3349")


def test_unreachable_sources_fail_without_writing_artifact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    gene_dir = prepare_gene(tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fitness, "FEBA_DB", tmp_path / "missing.db")
    monkeypatch.setattr(fitness, "find_feba_html_dir", lambda *_: None)
    stub_empty_queries(monkeypatch)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "ECOLI", "SlyD"])

    with pytest.raises(SystemExit) as exc:
        fitness.main()

    assert exc.value.code == 1
    assert "no FEBA data source was reachable" in capsys.readouterr().err
    assert not (gene_dir / "SlyD-fitness.md").exists()


def test_reachable_source_without_gene_writes_placeholder(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    gene_dir = prepare_gene(tmp_path)
    database = tmp_path / "feba.db"
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE Gene (id INTEGER)")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fitness, "FEBA_DB", database)
    stub_empty_queries(monkeypatch)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "ECOLI", "SlyD"])

    with pytest.raises(SystemExit) as exc:
        fitness.main()

    assert exc.value.code == 0
    artifact = gene_dir / "SlyD-fitness.md"
    assert artifact.exists()
    assert "No fitness data found for keio/b3349" in artifact.read_text()


def test_corrupt_database_is_not_a_reachable_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    gene_dir = prepare_gene(tmp_path)
    database = tmp_path / "feba.db"
    database.write_text("not a sqlite database")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fitness, "FEBA_DB", database)
    monkeypatch.setattr(fitness, "find_feba_html_dir", lambda *_: None)
    stub_empty_queries(monkeypatch)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "ECOLI", "SlyD"])

    with pytest.raises(SystemExit) as exc:
        fitness.main()

    assert exc.value.code == 1
    assert not (gene_dir / "SlyD-fitness.md").exists()


def test_empty_remote_result_is_a_reachable_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    gene_dir = prepare_gene(tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fitness, "FEBA_DB", tmp_path / "missing.db")
    monkeypatch.setattr(fitness, "find_feba_html_dir", lambda *_: None)
    monkeypatch.setattr(fitness, "query_sqlite", lambda *_: None)
    monkeypatch.setattr(fitness, "query_html_dir", lambda *_: None)
    monkeypatch.setattr(
        fitness,
        "try_bulk_download",
        lambda *_: {
            "gene": {"locusId": "b3349"},
            "fitness": [],
            "cofitness": [],
            "specific_phenotypes": [],
        },
    )
    monkeypatch.setattr(fitness, "resolve_locus_tag", lambda *_: "b3349")
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), "ECOLI", "SlyD"])

    with pytest.raises(SystemExit) as exc:
        fitness.main()

    assert exc.value.code == 0
    assert (gene_dir / "SlyD-fitness.md").exists()


@pytest.mark.parametrize(
    "content",
    [
        "<!DOCTYPE html><html><body>challenge</body></html>",
        "name\tdescription\nset1\terror page\n",
    ],
)
def test_bulk_download_rejects_html_and_invalid_headers(
    content: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

        def read(self) -> bytes:
            return content.encode()

    monkeypatch.setattr("urllib.request.urlopen", lambda *_args, **_kwargs: Response())

    assert fitness.try_bulk_download("keio", "b3349") is None


@pytest.mark.parametrize(
    "content",
    [
        "name\tfit\tt\nset1\t\t2.0\n",
        "name\tfit\tt\nset1\tnot-a-number\t2.0\n",
        "name\tfit\tt\nset1\t1.0\t\n",
    ],
)
def test_bulk_download_rejects_invalid_numeric_cells(
    content: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

        def read(self) -> bytes:
            return content.encode()

    monkeypatch.setattr("urllib.request.urlopen", lambda *_args, **_kwargs: Response())

    assert fitness.try_bulk_download("keio", "b3349") is None
