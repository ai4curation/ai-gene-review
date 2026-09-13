"""Tests for the post-enrichment rule-analysis command."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "examples" / "rule_analysis_demo.py"
SPEC = importlib.util.spec_from_file_location("rule_analysis_demo", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
rule_analysis_demo = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rule_analysis_demo
SPEC.loader.exec_module(rule_analysis_demo)


def run_just(
    *args: str,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(extra_env or {})
    return subprocess.run(
        ["just", *args],
        cwd=SCRIPT_PATH.parents[1],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )


def install_recording_uv(tmp_path: Path) -> Path:
    """Install a fake uv executable that records its exact argument vector."""
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

args = sys.argv[1:]
Path(os.environ["RULE_ANALYSIS_UV_MARKER"]).write_text(json.dumps(args))
if "examples/rule_analysis_demo.py" in args and "--output-dir" in args:
    rule_id = args[args.index("examples/rule_analysis_demo.py") + 1]
    output_dir = Path(args[args.index("--output-dir") + 1])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"{rule_id}-analysis.txt").write_text("fake report\\n")
raise SystemExit(int(os.environ.get("RULE_ANALYSIS_UV_EXIT", "0")))
"""
    )
    fake_uv.chmod(0o755)
    return fake_bin


@pytest.mark.parametrize(
    "rule_id",
    [
        "UR000000070",
        "RULE00000001",
        "ARBA123",
    ],
)
def test_rejects_unsupported_rule_ids_before_client_or_output(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    rule_id: str,
) -> None:
    class UnexpectedClient:
        def __init__(self, **_kwargs: object) -> None:
            raise AssertionError("ARBAClient must not be constructed")

    cache_dir = tmp_path / "rule cache"
    output_dir = tmp_path / "analysis output"
    monkeypatch.setattr(rule_analysis_demo, "ARBAClient", UnexpectedClient)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(SCRIPT_PATH),
            rule_id,
            "--cache-dir",
            str(cache_dir),
            "--output-dir",
            str(output_dir),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        rule_analysis_demo.main()

    captured = capsys.readouterr()
    assert exc_info.value.code == 2
    assert "post-enrichment analysis currently supports ARBA######## IDs only" in (
        captured.err
    )
    assert captured.out == ""
    assert not cache_dir.exists()
    assert not output_dir.exists()


def test_accepts_exact_arba_rule_id_format(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "rule cache"
    fetched_ids: list[str] = []

    class LocalClient:
        def __init__(self, *, cache_dir: Path) -> None:
            assert cache_dir == tmp_path / "rule cache"

        def fetch_rule(self, requested_id: str) -> None:
            fetched_ids.append(requested_id)
            return None

    monkeypatch.setattr(rule_analysis_demo, "ARBAClient", LocalClient)
    monkeypatch.setattr(
        sys,
        "argv",
        [str(SCRIPT_PATH), rule_id, "--cache-dir", str(cache_dir), "--no-report"],
    )

    assert rule_analysis_demo.main() == 1
    assert fetched_ids == [rule_id]
    assert not cache_dir.exists()


@pytest.mark.parametrize(
    "rule_id",
    [
        "UR000000070",
        "ARBA00026249; echo unsafe",
    ],
)
def test_analyze_rule_wrapper_rejects_unsupported_ids_before_io(
    tmp_path: Path,
    rule_id: str,
) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import os
from pathlib import Path

Path(os.environ["RULE_ANALYSIS_UV_MARKER"]).write_text("invoked")
raise SystemExit(99)
"""
    )
    fake_uv.chmod(0o755)

    cache_dir = tmp_path / "rule-cache"
    marker = tmp_path / "uv-invoked"
    result = run_just(
        "analyze-rule",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        extra_env={
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        },
    )

    assert result.returncode == 2
    assert "post-enrichment analysis currently supports ARBA######## IDs only" in (
        result.stderr
    )
    assert not cache_dir.exists()
    assert not marker.exists()


def test_analyze_rule_wrapper_preserves_spaced_cache_path_when_skipping(
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "analysis cache (draft), v1?"
    rule_dir = cache_dir / rule_id
    rule_dir.mkdir(parents=True)
    (rule_dir / f"{rule_id}.enriched.json").write_text("{}")
    (rule_dir / f"{rule_id}-analysis.yaml").write_text("analysis: present\n")

    fake_bin = install_recording_uv(tmp_path)
    marker = tmp_path / "uv invocation.json"
    result = run_just(
        "analyze-rule",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        extra_env={
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        },
    )

    assert result.returncode == 0, result.stderr
    assert "skipping expensive rebuild" in result.stdout
    assert not marker.exists()


def test_analyze_rule_wrapper_force_runs_with_exact_arguments(tmp_path: Path) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "analysis cache (draft), v1?"
    rule_dir = cache_dir / rule_id
    rule_dir.mkdir(parents=True)
    (rule_dir / f"{rule_id}.enriched.json").write_text("{}")
    (rule_dir / f"{rule_id}-analysis.yaml").write_text("analysis: present\n")

    fake_bin = install_recording_uv(tmp_path)
    marker = tmp_path / "uv invocation.json"
    result = run_just(
        "analyze-rule",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        "--force",
        extra_env={
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        },
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(marker.read_text()) == [
        "run",
        "python",
        "examples/rule_analysis_demo.py",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        "--output-dir",
        str(rule_dir),
        "--no-report",
    ]


def test_analyze_rule_wrapper_accepts_empty_optional_tail(tmp_path: Path) -> None:
    rule_id = "ARBA00026249"
    working_directory = tmp_path / "isolated working directory"
    working_directory.mkdir()
    fake_bin = install_recording_uv(tmp_path)
    marker = tmp_path / "uv invocation.json"
    env = os.environ.copy()
    env.update(
        {
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        }
    )

    result = subprocess.run(
        [
            "just",
            "--justfile",
            str(SCRIPT_PATH.parents[1] / "justfile"),
            "--working-directory",
            str(working_directory),
            "analyze-rule",
            rule_id,
        ],
        cwd=SCRIPT_PATH.parents[1],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(marker.read_text()) == [
        "run",
        "python",
        "examples/rule_analysis_demo.py",
        rule_id,
        "--cache-dir",
        "rules/arba",
        "--output-dir",
        f"rules/arba/{rule_id}",
        "--no-report",
    ]
    assert (
        working_directory / "rules" / "arba" / rule_id / f"{rule_id}-analysis.txt"
    ).exists()


def test_analyze_rule_wrapper_rejects_unknown_argument_before_io(
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "isolated-cache"
    fake_bin = install_recording_uv(tmp_path)
    marker = tmp_path / "uv invocation.json"
    result = run_just(
        "analyze-rule",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        "--unknown",
        extra_env={
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        },
    )

    assert result.returncode == 2
    assert "unsupported analyze-rule argument '--unknown'" in result.stderr
    assert not cache_dir.exists()
    assert not marker.exists()


def test_analyze_rule_wrapper_rejects_missing_cache_path_before_io(
    tmp_path: Path,
) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "isolated-cache"
    fake_bin = install_recording_uv(tmp_path)
    marker = tmp_path / "uv invocation.json"
    result = run_just(
        "analyze-rule",
        rule_id,
        "--cache-dir",
        str(cache_dir),
        "--cache-dir",
        extra_env={
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "RULE_ANALYSIS_UV_MARKER": str(marker),
        },
    )

    assert result.returncode == 2
    assert "--cache-dir requires a path" in result.stderr
    assert not cache_dir.exists()
    assert not marker.exists()
