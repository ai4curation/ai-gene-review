#!/usr/bin/env python3
"""Block Bash commands that would notify people on upstream trackers.

Runs before every Bash call. Commands that publish text to GitHub (``git commit``,
``gh pr|issue create|edit|comment|review``, ``gh api`` with fields) are checked with
``ai_gene_review.shadow_issues.guard``: the command text itself, plus any file it
reads a message or body from (``-F``/``--file``, ``--body-file``, ``field=@file``).
A hazard (upstream issue URL, ``org/repo#N``, ``@mention`` other than cmungall)
exits 2, which blocks the call and shows the reason.

The guard is imported from this checkout's ``src`` by path, so the hook needs only
the standard library.
"""

import json
import re
import shlex
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(
        Path(__file__).resolve().parents[2] / "src" / "ai_gene_review" / "shadow_issues"
    ),
)
from guard import find_notification_hazards  # noqa: E402

PUBLISHING = re.compile(
    r"\bgit\s+commit\b|\bgh\s+(pr|issue)\s+(create|edit|comment|review)\b|\bgh\s+api\b.*\s-[fF]\b|\bgh\s+release\s+create\b"
)
FILE_OPTIONS = {"-F", "--file", "--body-file"}


def referenced_files(command: str, cwd: Path) -> list[Path]:
    """Files the command reads a message or body from."""
    try:
        tokens = shlex.split(command)
    except ValueError:
        tokens = command.split()
    paths = []
    for i, token in enumerate(tokens):
        candidate = None
        if token in FILE_OPTIONS and i + 1 < len(tokens):
            candidate = tokens[i + 1]
        elif token.startswith("--body-file="):
            candidate = token.split("=", 1)[1]
        elif "=@" in token:
            candidate = token.split("=@", 1)[1]
        if candidate and candidate != "-":
            path = (cwd / candidate).expanduser()
            if path.is_file():
                paths.append(path)
    return paths


def main() -> int:
    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")
    if not PUBLISHING.search(command):
        return 0
    cwd = Path(data.get("cwd") or ".")
    texts = [("command", command)] + [
        (str(p), p.read_text(errors="replace")) for p in referenced_files(command, cwd)
    ]
    hazards = [
        (name, h) for name, text in texts for h in find_notification_hazards(text)
    ]
    if not hazards:
        return 0
    for name, hazard in hazards:
        print(f"{name}: {hazard}", file=sys.stderr)
    print(
        "Blocked: this text would cross-reference or @mention upstream (it notifies curators). "
        "Refer to an upstream issue as issues/<tracker>/<number> or 'go-annotation 1234', "
        "and mention no one but @cmungall. See projects/GO_ANNOTATION_TRACKER.md.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
