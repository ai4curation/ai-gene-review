"""Apply the generic protein-binding policy to every bare GO:0005515 row of a review.

``validation/protein_binding_policy.py`` permits only MODIFY, REMOVE or UNDECIDED
on a bare ``GO:0005515`` row and asks that touched reviews be migrated. This
script sets every ACCEPT, KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED row to
REMOVE, and gives it (and any row an earlier pass removed under the policy) a
reason that says why, replacing reasons that still argued for keeping the row.
``summary`` and ``supported_by`` are left as they are, so the interaction
itself stays recorded.

Edits are made on the text of the row only, and each file is checked against
the same change applied to the parsed original before it is written.

    uv run python scripts/migrate_protein_binding_rows.py --dry-run genes/human/UFM1/UFM1-ai-review.yaml
"""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

import yaml

from restore_goa_flipped_rows import _row_spans

PROTEIN_BINDING = "GO:0005515"
NON_COMPLIANT = {"ACCEPT", "KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED"}
EARLIER_NOTE = "Set to REMOVE under the generic protein-binding policy"
REASON = (
    "Bare GO:0005515 protein binding carries no functional information, so under the "
    "generic protein-binding policy this row is REMOVE. Removal does not mean the reported "
    "interaction is false; the summary and any supporting text keep it on record."
)


def _targets(data: Any) -> List[int]:
    out = []
    for i, ann in enumerate(data.get("existing_annotations") or []):
        if (ann.get("term") or {}).get("id") != PROTEIN_BINDING:
            continue
        review = ann.get("review") or {}
        if review.get("action") in NON_COMPLIANT or (
            review.get("action") == "REMOVE" and EARLIER_NOTE in (review.get("reason") or "")
        ):
            out.append(i)
    return out


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


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
    for idx in targets:
        review = expected["existing_annotations"][idx]["review"]
        review["action"] = "REMOVE"
        review["reason"] = REASON
        lo, hi = spans[idx]
        review_line = next(
            j for j in range(lo, hi) if lines[j] and lines[j].lstrip().startswith("review:")
        )
        key_indent = _indent(lines[review_line]) + 2
        has_reason = False
        for j in range(review_line + 1, hi):
            line = lines[j]
            if not line or _indent(line) != key_indent:
                continue
            key = line.strip().split(":", 1)[0]
            if key == "action":
                lines[j] = " " * key_indent + "action: REMOVE\n"
                action_at = j
            elif key == "reason":
                has_reason = True
                k = j + 1
                while k < hi and lines[k] is not None and (
                    not lines[k].strip() or _indent(lines[k]) > key_indent
                ):
                    lines[k] = None
                    k += 1
                lines[j] = " " * key_indent + f"reason: {REASON}\n"
        if not has_reason:
            lines[action_at] += " " * key_indent + f"reason: {REASON}\n"
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
            print(f"{path}: {n} rows")
    print(f"{total} protein-binding rows set to REMOVE with the policy reason", file=sys.stderr)
    for path, error in failed:
        print(f"FAILED {path}: {error}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
