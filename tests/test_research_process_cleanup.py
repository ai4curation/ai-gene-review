"""Exercise research timeout cleanup with real parent and child processes."""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

import pytest

from scripts import deep_research_wrapper


@pytest.mark.skipif(os.name != "posix", reason="Process-group cleanup is POSIX-specific")
def test_gene_timeout_stops_child_before_fallback(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A timed-out launcher must not leave a client writing during fallback."""
    late_output = tmp_path / "late-primary.md"
    child_started = tmp_path / "child-started"
    client = tmp_path / "client.py"
    client.write_text(
        "import pathlib, subprocess, sys, time\n"
        f"late = pathlib.Path({str(late_output)!r})\n"
        f"started = pathlib.Path({str(child_started)!r})\n"
        "provider = sys.argv[sys.argv.index('--provider') + 1]\n"
        "if provider == 'falcon':\n"
        "    code = 'import pathlib,time; pathlib.Path(' + repr(str(started)) + ').touch(); time.sleep(2.5); pathlib.Path(' + repr(str(late)) + ').write_text(\"late report\")'\n"
        "    subprocess.Popen([sys.executable, '-c', code])\n"
        "    time.sleep(60)\n"
        "else:\n"
        "    time.sleep(1)\n"
        "    sys.exit(17 if late.exists() else 0)\n"
    )
    monkeypatch.setenv("DEEP_RESEARCH_CLIENT_CMD", shlex.join([sys.executable, str(client)]))

    result = deep_research_wrapper.run_deep_research(
        organism="SCHPO",
        gene_id="TEST",
        gene_symbol="TEST",
        provider="falcon",
        output_path=tmp_path / "TEST-deep-research-falcon.md",
        timeout=2,
        fallback_providers=["perplexity-lite"],
    )

    assert child_started.exists(), "The real descendant must start to exercise cleanup"
    assert not late_output.exists(), "Timed-out client wrote after the wrapper moved on"
    assert result == 0


@pytest.mark.skipif(os.name != "posix", reason="Process-group cleanup is POSIX-specific")
@pytest.mark.parametrize("capture_output,launcher_exits", [(False, False), (True, False), (True, True)])
def test_timeout_kills_descendant_with_inherited_pipes(
    tmp_path: Path, capture_output: bool, launcher_exits: bool
) -> None:
    """Captured pipes must not keep a timed-out client's descendants alive."""
    import subprocess
    import time

    from ai_gene_review.utils.research_process import run_research_process

    late_output = tmp_path / "late.md"
    started = tmp_path / "started"
    child_code = (
        "import pathlib,time; "
        f"pathlib.Path({str(started)!r}).touch(); "
        "time.sleep(2); "
        f"pathlib.Path({str(late_output)!r}).write_text('late')"
    )
    parent_code = (
        "import subprocess,sys,time; "
        f"subprocess.Popen([sys.executable, '-c', {child_code!r}]); "
        "print('client started', flush=True); "
        + ("sys.exit(0)" if launcher_exits else "time.sleep(60)")
    )
    with pytest.raises(subprocess.TimeoutExpired):
        run_research_process(
            [sys.executable, "-c", parent_code], timeout=1, capture_output=capture_output
        )
    assert started.exists()
    # Wait past the child's real write deadline; this detects surviving clients.
    time.sleep(1.2)
    assert not late_output.exists()


def test_research_process_returns_captured_output_and_exit_code() -> None:
    from ai_gene_review.utils.research_process import run_research_process

    result = run_research_process(
        [sys.executable, "-c", "import sys; print('report'); print('diagnostic', file=sys.stderr); sys.exit(7)"],
        capture_output=True,
        timeout=5,
    )
    assert result.returncode == 7
    assert result.stdout == "report\n"
    assert result.stderr == "diagnostic\n"
