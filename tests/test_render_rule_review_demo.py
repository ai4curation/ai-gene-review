"""Tests for the rule-analysis and HTML-rendering demo command."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "examples" / "render_rule_review_demo.py"
)
SPEC = importlib.util.spec_from_file_location("render_rule_review_demo", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
render_rule_review_demo = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = render_rule_review_demo
SPEC.loader.exec_module(render_rule_review_demo)


@pytest.mark.parametrize(
    ("rule_id", "extra_args"),
    [
        ("UR000000070", []),
        ("UR000000070", ["--skip-analysis"]),
        ("RULE00000001", []),
        ("ARBA123", []),
    ],
)
def test_rejects_unsupported_rule_ids_before_client_or_output(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    rule_id: str,
    extra_args: list[str],
) -> None:
    class UnexpectedClient:
        def __init__(self, **_kwargs: object) -> None:
            raise AssertionError("ARBAClient must not be constructed")

    output_dir = tmp_path / "rendered output"
    monkeypatch.setattr(render_rule_review_demo, "ARBAClient", UnexpectedClient)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(SCRIPT_PATH),
            rule_id,
            "--output-dir",
            str(output_dir),
            *extra_args,
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        render_rule_review_demo.main()

    captured = capsys.readouterr()
    assert exc_info.value.code == 2
    assert "post-enrichment analysis currently supports ARBA######## IDs only" in (
        captured.err
    )
    assert captured.out == ""
    assert not output_dir.exists()
