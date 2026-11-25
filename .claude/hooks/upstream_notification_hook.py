#!/usr/bin/env python3
"""Block tool calls that would notify people on upstream trackers.

Two kinds of call are checked with ``ai_gene_review.shadow_issues.guard``:

- Bash commands that publish text to GitHub (``git commit``,
  ``gh pr|issue create|edit|comment|review``, ``gh release create``, and ``gh api``
  with ``-f``/``-F``/``--field``/``--raw-field``/``--input``): the command text
  itself, plus any file it reads a message or body from (``-F``/``--file``,
  ``--body-file``, ``--input``, ``field=@file``).
- GitHub MCP tools (``mcp__github*``, as used by claude-code-action for comments,
  issues and pull requests): every string in the tool input.

A hazard (upstream issue URL, ``org/repo#N``, an at-mention other than cmungall)
exits 2, which blocks the call and shows the reason.

The guard is imported from this checkout's ``src`` by path, so the hook needs only
the standard library. It does not use ``hook_paths.repo_root_for``: that helper
finds the repository from the file being edited, and a Bash or MCP call has no
such file. The guard copy beside this hook is the right one in any checkout.
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
    r"\bgit\s+commit\b"
    r"|\bgh\s+(pr|issue)\s+(create|edit|comment|review)\b"
    r"|\bgh\s+api\b.*\s(-[fF]|--field|--raw-field|--input)(\s|=)"
    r"|\bgh\s+release\s+create\b"
)
FILE_OPTIONS = {"-F", "--file", "--body-file", "--input"}


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
        elif token.startswith(("--body-file=", "--input=", "--file=")):
            candidate = token.split("=", 1)[1]
        elif "=@" in token:
            candidate = token.split("=@", 1)[1]
        if candidate and candidate != "-":
            path = (cwd / candidate).expanduser()
            if path.is_file():
                paths.append(path)
    return paths


def strings_in(value: object) -> list[str]:
    """Every string nested in a tool input.

    >>> strings_in({"body": "a", "items": [{"x": "b"}, 3]})
    ['a', 'b']
    """
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in strings_in(v)]
    if isinstance(value, list):
        return [s for v in value for s in strings_in(v)]
    return []


def texts_to_check(data: dict) -> list[tuple[str, str]]:
    """(name, text) pairs to scan for one tool call; empty when it publishes nothing."""
    tool = data.get("tool_name", "Bash")
    tool_input = data.get("tool_input", {})
    if tool.startswith("mcp__github"):
        return [(tool, text) for text in strings_in(tool_input)]
    command = tool_input.get("command", "")
    if not PUBLISHING.search(command):
        return []
    cwd = Path(data.get("cwd") or ".")
    return [("command", command)] + [
        (str(p), p.read_text(errors="replace")) for p in referenced_files(command, cwd)
    ]


def main() -> int:
    data = json.load(sys.stdin)
    hazards = [
        (name, h)
        for name, text in texts_to_check(data)
        for h in find_notification_hazards(text)
    ]
    if not hazards:
        return 0
    for name, hazard in hazards:
        print(f"{name}: {hazard}", file=sys.stderr)
    print(
        "Blocked: this text would cross-reference or at-mention upstream (it notifies "
        "curators). Refer to an upstream issue as issues/<tracker>/<number> or "
        "'go-annotation 1234', and mention no one but cmungall. "
        "See projects/GO_ANNOTATION_TRACKER.md.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
