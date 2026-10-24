"""Remove GOA files from the ``supported_by`` lists of a review.

A GOA table records annotations, so it is never evidence for one (see
``ai_gene_review.validation.goa_support``). For each review this script deletes
every ``supported_by`` item citing a ``-goa.tsv`` file, the review's own or
another gene's. When that leaves an existing annotation's review with no support
at all, the action becomes ``UNDECIDED`` and the reason records the previous
action. An emptied ``supported_by`` key is dropped.

Edits are made on the text so the rest of each file is left byte-for-byte as it
was. Each rewritten file is then parsed and compared with the same
transformation applied to the parsed original; any mismatch is reported and the
file is left untouched.

    uv run python scripts/strip_self_goa_support.py genes/PSEPK/coaD/coaD-ai-review.yaml
    uv run python scripts/strip_self_goa_support.py --all
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

import yaml

from ai_gene_review.validation.local_source_text import PROJECT_ROOT
from ai_gene_review.validation.goa_support import _gene_dir, is_goa_file

NOTE = (
    "Previously {action}; set to UNDECIDED because the only cited support was the GOA row "
    "for this annotation, which records the annotation rather than evidence for it."
)


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_blank(line: str) -> bool:
    return not line.strip() or line.lstrip().startswith("#")


def transform_data(data: Any, gene_dir: str) -> Tuple[Any, int]:
    """The expected parsed result, and how many support items were removed."""
    data = copy.deepcopy(data)
    removed = 0

    def strip(node: Any) -> None:
        nonlocal removed
        if isinstance(node, dict):
            sb = node.get("supported_by")
            if isinstance(sb, list):
                kept = [s for s in sb if not (isinstance(s, dict) and is_goa_file(s.get("reference_id")))]
                removed += len(sb) - len(kept)
                if len(kept) != len(sb):
                    if kept:
                        node["supported_by"] = kept
                    else:
                        del node["supported_by"]
                        action = node.get("action")
                        if action is not None and action != "UNDECIDED":
                            note = NOTE.format(action=action)
                            reason = node.get("reason")
                            if reason:
                                tail = reason[len(reason.rstrip()):]
                                node["reason"] = f"{reason.rstrip()} {note}{tail}"
                            else:
                                node["reason"] = note
                            node["action"] = "UNDECIDED"
            for value in node.values():
                strip(value)
        elif isinstance(node, list):
            for value in node:
                strip(value)

    strip(data)
    return data, removed


def _block_end(lines: List[str], start: int, indent: int) -> int:
    """Index after the block that starts at ``start`` and owns lines indented past ``indent``."""
    end = start + 1
    while end < len(lines) and (_is_blank(lines[end]) or _indent(lines[end]) > indent):
        end += 1
    while end > start + 1 and _is_blank(lines[end - 1]):
        end -= 1
    return end


def _siblings(lines: List[str], at: int) -> Tuple[int, int]:
    """Range of the mapping that contains the key on line ``at``."""
    indent = _indent(lines[at])
    lo = at
    while lo > 0:
        prev = lines[lo - 1]
        # deeper lines, sibling keys, and a sibling's zero-offset list items
        if _is_blank(prev) or _indent(prev) >= indent:
            lo -= 1
            continue
        if _indent(prev) == indent - 2 and prev.lstrip().startswith("- "):
            lo -= 1  # the "- key:" line that opens this mapping
        break
    hi = _block_end(lines, at, indent - 1)
    return lo, hi


def _key_line(lines: List[str], lo: int, hi: int, indent: int, key: str) -> Optional[int]:
    pattern = re.compile(rf"^(\s*(- )?){re.escape(key)}:(\s|$)")
    for i in range(lo, hi):
        m = pattern.match(lines[i])
        if m and len(m.group(1)) == indent:
            return i
    return None


def _append_reason(lines: List[str], lo: int, hi: int, indent: int, action_at: int, note: str) -> None:
    at = _key_line(lines, lo, hi, indent, "reason")
    if at is None:
        lines.insert(action_at + 1, " " * indent + f"reason: {note}\n")
        return
    end = _block_end(lines, at, indent)
    value = lines[at].split("reason:", 1)[1].strip()
    if value[:1] == ">":
        body = next(lines[i] for i in range(at + 1, end) if not _is_blank(lines[i]))
        lines.insert(end, " " * _indent(body) + note + "\n")
        return
    if value[:1] == "|":
        last = max(i for i in range(at + 1, end) if lines[i].strip())
        lines[last] = lines[last].rstrip() + " " + note + "\n"
        return
    last = end - 1
    text = lines[last].rstrip("\n")
    if value[:1] in ("'", '"'):
        quote = text.rstrip()[-1]
        lines[last] = text.rstrip()[:-1] + " " + note + quote + "\n"
    else:
        lines[last] = text.rstrip() + " " + note + "\n"


def transform_text(text: str, gene_dir: str) -> str:
    """Apply the edit to the file text."""
    lines = text.splitlines(keepends=True)
    item = re.compile(r"^(\s*)- reference_id:\s*['\"]?(file:\S+?)['\"]?\s*$")
    i = 0
    while i < len(lines):
        m = item.match(lines[i])
        if not (m and is_goa_file(m.group(2))):
            i += 1
            continue
        indent = len(m.group(1))
        end = _block_end(lines, i, indent)
        del lines[i:end]
        # find the owning supported_by key and check whether its list is now empty
        k = i - 1
        while k >= 0 and (
            _is_blank(lines[k])
            or _indent(lines[k]) > indent
            or (_indent(lines[k]) == indent and lines[k].lstrip().startswith("- "))
        ):
            k -= 1
        if k < 0 or not re.match(r"^\s*(- )?supported_by:\s*$", lines[k]):
            continue
        nxt = k + 1
        while nxt < len(lines) and _is_blank(lines[nxt]):
            nxt += 1
        key_indent = len(re.match(r"^(\s*(- )?)", lines[k]).group(1))
        still_listed = (
            nxt < len(lines)
            and lines[nxt].lstrip().startswith("- ")
            and _indent(lines[nxt]) in (key_indent, key_indent + 2)
        )
        if still_listed:
            continue
        lo, hi = _siblings(lines, k)
        if lines[k].lstrip().startswith("- "):
            raise ValueError(f"supported_by opens a list item at line {k + 1}")
        del lines[k]
        hi -= 1
        action_at = _key_line(lines, lo, hi, key_indent, "action")
        if action_at is None:
            i = k
            continue
        action = lines[action_at].split("action:", 1)[1].strip().strip("'\"")
        if action != "UNDECIDED":
            lines[action_at] = lines[action_at].replace(action, "UNDECIDED", 1)
            _append_reason(lines, lo, hi, key_indent, action_at, NOTE.format(action=action))
        i = k
    return "".join(lines)


def process(path: Path, write: bool) -> Tuple[int, Optional[str]]:
    """Fix one review. Returns (items removed, error message or None)."""
    gene_dir = _gene_dir(path, PROJECT_ROOT)
    if gene_dir is None:
        return 0, "not under genes/"
    text = path.read_text()
    data = yaml.safe_load(text)
    expected, removed = transform_data(data, gene_dir)
    if not removed:
        return 0, None
    new_text = transform_text(text, gene_dir)
    if yaml.safe_load(new_text) != expected:
        return removed, "text edit does not match the expected data; left unchanged"
    if write:
        path.write_text(new_text)
    return removed, None


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--all", action="store_true", help="every genes/**/*-ai-review.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    files = sorted((PROJECT_ROOT / "genes").glob("*/*/*-ai-review.yaml")) if args.all else args.files
    total = changed = 0
    failed = []
    for path in files:
        removed, error = process(path, write=not args.dry_run)
        if error:
            failed.append((path, error))
        elif removed:
            total += removed
            changed += 1
            print(f"{path}: removed {removed}")
    print(f"{total} support items removed from {changed} reviews", file=sys.stderr)
    for path, error in failed:
        print(f"FAILED {path}: {error}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
