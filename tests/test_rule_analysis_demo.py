"""Tests for the post-enrichment rule-analysis command."""

from __future__ import annotations

import importlib.util
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
