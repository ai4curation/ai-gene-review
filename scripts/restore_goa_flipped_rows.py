"""Resolve rows that ``strip_self_goa_support.py`` set to UNDECIDED.

That script set a row to UNDECIDED whenever its only ``supported_by`` item was
the gene's own GOA file, recording the earlier action in the reason
("Previously X; set to UNDECIDED because ..."). For bare ``GO:0005515``
protein-binding rows the earlier action needs no quote to be justified: the
generic protein-binding policy (``validation/protein_binding_policy.py``) says
a touched row is REMOVE unless the cited paper supports a more informative
term. This script applies that to every such row whose earlier action was not
MODIFY (those need curation), replacing the UNDECIDED note.

Edits are made on the text of the row only, and each file is checked against
the same change applied to the parsed original before it is written.

    uv run python scripts/restore_goa_flipped_rows.py --dry-run genes/human/RACK1/RACK1-ai-review.yaml
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

import yaml

NOTE_RE = re.compile(
    r" ?Previously ([A-Z_]+); set to UNDECIDED because the only cited support was the GOA row "
    r"for this annotation, which records the annotation rather than evidence for it\."
)
POLICY_NOTE = (
    "Set to REMOVE under the generic protein-binding policy, since GO:0005515 carries no functional "
    "information, and the only cited support was the GOA row itself. Removal does not mean the "
    "reported interaction is false."
)
PROTEIN_BINDING = "GO:0005515"


def _targets(data: Any) -> List[Tuple[int, str]]:
    """``(row index, earlier action)`` for the protein-binding rows this script resolves."""
    out = []
    for i, ann in enumerate(data.get("existing_annotations") or []):
        review = ann.get("review") or {}
        m = NOTE_RE.search(review.get("reason") or "")
        if (
            m
            and review.get("action") == "UNDECIDED"
            and (ann.get("term") or {}).get("id") == PROTEIN_BINDING
            and m.group(1) != "MODIFY"
        ):
            out.append((i, m.group(1)))
    return out


def _new_reason(reason: str, previous: str) -> str:
    replacement = "" if previous == "REMOVE" else POLICY_NOTE
    m = NOTE_RE.search(reason)
    head, tail = reason[: m.start()], reason[m.end():]
    if replacement:
        joined = f"{head} {replacement}" if head.strip() else replacement
    else:
        joined = head
    return joined + tail


def _row_spans(lines: List[Optional[str]]) -> List[Tuple[int, int]]:
    """Line ranges of the top-level ``existing_annotations`` rows."""
    start = next(i for i, line in enumerate(lines) if line and line.startswith("existing_annotations:"))
    first = next(lines[i] for i in range(start + 1, len(lines)) if (lines[i] or "").strip())
    item = " " * (len(first) - len(first.lstrip(" "))) + "- "
    starts = []
    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i] or ""
        if line.startswith(item):
            starts.append(i)
        elif line.strip() and not line.startswith((" ", "#")):
            end = i
            break
    return [(s, starts[k + 1] if k + 1 < len(starts) else end) for k, s in enumerate(starts)]


def process(path: Path, write: bool) -> Tuple[int, Optional[str]]:
    text = path.read_text()
    data = yaml.safe_load(text)
    targets = _targets(data)
    if not targets:
        return 0, None
    expected = copy.deepcopy(data)
    lines: List[Optional[str]] = list(text.splitlines(keepends=True))
    spans = _row_spans(lines)
    if len(spans) != len(data["existing_annotations"]):
        return 0, "could not locate annotation rows"
    for idx, previous in targets:
        review = expected["existing_annotations"][idx]["review"]
        review["action"] = "REMOVE"
        review["reason"] = _new_reason(review["reason"], previous)
        lo, hi = spans[idx]
        for j in range(lo, hi):
            if re.match(r"^\s+action:\s*UNDECIDED\s*$", lines[j]):
                lines[j] = lines[j].replace("UNDECIDED", "REMOVE")
            m = NOTE_RE.search(lines[j])
            if m:
                # a note on its own line (block scalar) takes no joining space
                own_line = not lines[j][: m.start()].strip()
                if previous == "REMOVE":
                    replacement = ""
                else:
                    replacement = POLICY_NOTE if own_line else " " + POLICY_NOTE
                start = m.start() + (1 if own_line and lines[j][m.start()] == " " else 0)
                lines[j] = lines[j][:start] + replacement + lines[j][m.end():]
                if not lines[j].strip():
                    lines[j] = None
    new_text = "".join(line for line in lines if line is not None)
    try:
        parsed = yaml.safe_load(new_text)
    except yaml.YAMLError:
        return len(targets), "text edit does not parse; left unchanged"
    if parsed != expected:
        return len(targets), "text edit does not match the expected data; left unchanged"
    if write:
        path.write_text(new_text)
    return len(targets), None


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    total = 0
    failed = []
    for path in args.files:
        n, error = process(path, write=not args.dry_run)
        if error:
            failed.append((path, error))
        elif n:
            total += n
            print(f"{path}: {n} rows set to REMOVE")
    print(f"{total} protein-binding rows resolved", file=sys.stderr)
    for path, error in failed:
        print(f"FAILED {path}: {error}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
