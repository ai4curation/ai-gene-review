"""Run research clients without leaving local descendants after a timeout."""

from __future__ import annotations

import os
import signal
import subprocess
from collections.abc import Sequence


def run_research_process(
    command: Sequence[str],
    *,
    timeout: float | None = None,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run a client, cleaning up its local process group on timeout or interruption.

    On POSIX, launchers such as ``uv`` and their client descendants share a new
    session. Kill that entire process group before returning control to a caller
    that may start a fallback. This also handles an exited launcher whose child
    still holds captured output pipes open. Other platforms retain direct-child
    cleanup. This does not promise cancellation of remote provider jobs.

    Output is text when captured; otherwise stdout and stderr are inherited.
    Nonzero exit codes are returned for the wrapper to interpret.
    """
    args = list(command)
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.PIPE if capture_output else None,
        text=True,
        start_new_session=os.name == "posix",
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except BaseException:
        # Unlike subprocess.run(), clean up descendants of uv/uvx as well as
        # the immediate launcher. Kill even if the launcher has already exited.
        if os.name == "posix":
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        else:
            process.kill()
        process.communicate()
        raise
    assert process.returncode is not None
    return subprocess.CompletedProcess(args, process.returncode, stdout, stderr)
