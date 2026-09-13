"""Launch BioReason's Python with ai-gene-review code and dependencies available."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import sysconfig
from typing import NoReturn


REPOSITORY_SITE_ENV = "AIGR_REPOSITORY_SITE_PACKAGES"


def _python_version(python: Path) -> tuple[int, int]:
    try:
        result = subprocess.run(
            [
                str(python),
                "-S",
                "-c",
                "import sys; print('%d.%d' % sys.version_info[:2])",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() or str(error)
        raise SystemExit(f"Could not inspect BioReason Python: {detail}") from error
    version = result.stdout.strip()
    major, minor = (int(part) for part in version.split("."))
    return major, minor


def _pythonpath_entries(
    repo_root: Path,
    inherited: str | None,
) -> list[str]:
    candidates = [
        str(repo_root / "src"),
        str(repo_root / "src" / "ai_gene_review" / "_bioreason_sitecustomize"),
        *(inherited.split(os.pathsep) if inherited else []),
    ]
    return list(dict.fromkeys(entry for entry in candidates if entry))


def main(argv: list[str] | None = None) -> NoReturn:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        raise SystemExit("usage: run_bioreason_python PYTHON_ARGS...")

    repo_root = Path(__file__).resolve().parents[2]
    source_root = repo_root / "src"
    shim_root = source_root / "ai_gene_review" / "_bioreason_sitecustomize"
    if not source_root.is_dir() or not shim_root.is_dir():
        raise SystemExit(
            "BioReason dependency bridge requires an ai-gene-review source checkout"
        )
    configured = os.environ.get("BIOREASON_PYTHON")
    bioreason_python = Path(configured).expanduser() if configured else (
        Path.home() / "repos" / "BioReason-Pro" / ".venv" / "bin" / "python"
    )
    if not bioreason_python.is_file():
        raise SystemExit(
            f"BioReason Python not found at {bioreason_python}; "
            "set BIOREASON_PYTHON to its virtual-environment interpreter"
        )

    bioreason_version = _python_version(bioreason_python)
    repository_version = sys.version_info[:2]
    if bioreason_version != repository_version:
        raise SystemExit(
            "BioReason and repository Python minor versions must match before "
            "sharing compiled dependencies: "
            f"BioReason is {bioreason_version[0]}.{bioreason_version[1]}, "
            f"repository is {repository_version[0]}.{repository_version[1]}"
        )
    repository_site = Path(sysconfig.get_paths()["purelib"])
    oaklib_spec = importlib.util.find_spec("oaklib")
    oaklib_origin = oaklib_spec.origin if oaklib_spec else None
    if not oaklib_origin or not Path(oaklib_origin).is_relative_to(repository_site):
        raise SystemExit(
            f"oaklib is not installed in repository environment {repository_site}; "
            "launch through the public just wrapper or run `uv sync` first"
        )

    environment = os.environ.copy()
    environment[REPOSITORY_SITE_ENV] = str(repository_site)
    environment["PYTHONPATH"] = os.pathsep.join(
        _pythonpath_entries(repo_root, environment.get("PYTHONPATH"))
    )
    os.execve(
        bioreason_python,
        [str(bioreason_python), *args],
        environment,
    )
    # Only reachable when tests replace os.execve with a recording stub.
    raise RuntimeError("os.execve returned without replacing the process")


if __name__ == "__main__":
    main()
