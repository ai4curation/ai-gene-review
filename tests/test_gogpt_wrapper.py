"""Regression tests for the repository GO-GPT just wrappers."""

from pathlib import Path
import json
import os
import subprocess
import sys
import sysconfig

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "project.justfile"


def test_gogpt_inference_wrappers_use_dependency_bridge() -> None:
    """Every GO-GPT inference call must include repository dependencies."""
    repository_only_modes = {"--check-web-exports", "--refresh-web-exports"}
    command_lines = [
        line.strip()
        for line in PROJECT_JUSTFILE.read_text().splitlines()
        if "scripts/gogpt_predict.py" in line
        and not line.lstrip().startswith("#")
        and not any(mode in line for mode in repository_only_modes)
    ]

    assert command_lines, "expected at least one BioReason GO-GPT invocation"
    missing = [
        line
        for line in command_lines
        if not line.startswith(
            "uv run python -m ai_gene_review.run_bioreason_python "
        )
    ]
    assert not missing, f"BioReason invocations without dependency bridge: {missing}"


def test_dependency_bridge_builds_minimal_pythonpath() -> None:
    """Only source and the site shim are injected ahead of standard paths."""
    from ai_gene_review.run_bioreason_python import _pythonpath_entries

    entries = _pythonpath_entries(
        REPO_ROOT,
        "/inherited",
    )

    assert entries == [
        str(REPO_ROOT / "src"),
        str(REPO_ROOT / "src" / "ai_gene_review" / "_bioreason_sitecustomize"),
        "/inherited",
    ]


def test_dependency_bridge_honors_expanded_override(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from ai_gene_review import run_bioreason_python as launcher

    interpreter = tmp_path / "bio" / "bin" / "python"
    interpreter.parent.mkdir(parents=True)
    interpreter.touch()
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("BIOREASON_PYTHON", "~/bio/bin/python")
    monkeypatch.setattr(
        launcher,
        "_python_version",
        lambda path: launcher.sys.version_info[:2],
    )
    call: dict[str, object] = {}

    def fake_execve(path: Path, args: list[str], env: dict[str, str]) -> None:
        call.update(path=path, args=args, env=env)

    monkeypatch.setattr(launcher.os, "execve", fake_execve)

    with pytest.raises(RuntimeError, match="execve returned"):
        launcher.main(["-c", "pass"])

    assert call["path"] == interpreter
    assert call["args"] == [str(interpreter), "-c", "pass"]
    assert isinstance(call["env"], dict)
    assert launcher.REPOSITORY_SITE_ENV in call["env"]


def test_dependency_bridge_rejects_missing_interpreter(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from ai_gene_review import run_bioreason_python as launcher

    missing = tmp_path / "missing-python"
    monkeypatch.setenv("BIOREASON_PYTHON", str(missing))

    with pytest.raises(SystemExit, match="set BIOREASON_PYTHON"):
        launcher.main(["-c", "pass"])


def test_dependency_bridge_rejects_python_version_mismatch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from ai_gene_review import run_bioreason_python as launcher

    interpreter = tmp_path / "python"
    interpreter.touch()
    monkeypatch.setenv("BIOREASON_PYTHON", str(interpreter))
    monkeypatch.setattr(
        launcher,
        "_python_version",
        lambda path: (3, 11),
    )

    with pytest.raises(SystemExit, match="minor versions must match"):
        launcher.main(["-c", "pass"])


def test_dependency_bridge_requires_python_args() -> None:
    from ai_gene_review.run_bioreason_python import main

    with pytest.raises(SystemExit, match="usage:"):
        main([])


def test_sitecustomize_appends_repository_site_and_processes_pth(
    tmp_path: Path,
) -> None:
    repository_site = tmp_path / "repository-site"
    pth_target = tmp_path / "pth-target"
    repository_site.mkdir()
    pth_target.mkdir()
    (repository_site / "bridge-test.pth").write_text(f"{pth_target}\n")
    shim = REPO_ROOT / "src" / "ai_gene_review" / "_bioreason_sitecustomize"
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(shim)
    environment["AIGR_REPOSITORY_SITE_PACKAGES"] = str(repository_site)

    result = subprocess.run(
        [sys.executable, "-c", "import json, sys; print(json.dumps(sys.path))"],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    child_path = json.loads(result.stdout)

    assert child_path.index(str(repository_site)) > child_path.index(
        sysconfig.get_paths()["purelib"]
    )
    assert str(pth_target) in child_path


def test_sitecustomize_is_stdlib_only_and_chains_existing_customizer(
    tmp_path: Path,
) -> None:
    repository_site = tmp_path / "repository-site"
    existing_site = tmp_path / "existing-site"
    marker = tmp_path / "chained.txt"
    repository_site.mkdir()
    existing_site.mkdir()
    (existing_site / "sitecustomize.py").write_text(
        "from pathlib import Path\n"
        f"Path({str(marker)!r}).write_text('ran')\n"
    )
    shim = REPO_ROOT / "src" / "ai_gene_review" / "_bioreason_sitecustomize"
    environment = os.environ.copy()
    environment["PYTHONPATH"] = os.pathsep.join((str(shim), str(existing_site)))
    environment["AIGR_REPOSITORY_SITE_PACKAGES"] = str(repository_site)

    subprocess.run(
        [sys.executable, "-c", "pass"],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )

    assert marker.read_text() == "ran"
