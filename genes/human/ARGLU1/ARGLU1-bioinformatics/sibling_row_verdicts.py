#!/usr/bin/env python3
"""How have already-merged reviews in this repository resolved the same rows?

An inconsistency between merged reviews is a defect even when each is
individually defensible (the AADACL2/3/4 lesson: one identical row, three
different verdicts, nobody noticed). Before choosing an action for a row that
many genes share, check what the corpus already decided.

Reports, for each (GO term, reference) pair of interest, the distribution of
``review.action`` across every ``*-ai-review.yaml`` in ``genes/``.

Run from anywhere in the repo:  uv run python sibling_row_verdicts.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import yaml

# Rows ARGLU1 shares with many other genes.
PAIRS = [
    ("GO:0045296", "PMID:25468996"),   # cadherin binding from the E-cadherin BioID screen
    ("GO:0005739", "GO_REF:0000033"),  # mitochondrion by IBA
    ("GO:0045893", "GO_REF:0000108"),  # positive regulation of transcription by inter-ontology link
]


def repo_root() -> Path:
    """Derive the repository root; never hardcode a worktree path.

    A shared script with a hardcoded root resolves against another agent's
    checkout and returns confident wrong answers.
    """
    for base in [Path.cwd(), Path(__file__).resolve()]:
        for p in [base, *base.parents]:
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit(
        "cannot locate the repository root (a directory containing both "
        "'genes/' and 'src/') from cwd or from this script's path."
    )


def main() -> int:
    root = repo_root()
    files = sorted(root.glob("genes/*/*/*-ai-review.yaml"))
    if not files:
        raise SystemExit(f"no review YAML found under {root / 'genes'}")
    print(f"repo root: {root}")
    print(f"scanning {len(files)} review files\n")

    out = {}
    for go_id, ref in PAIRS:
        actions: Counter = Counter()
        genes: list[str] = []
        for f in files:
            try:
                d = yaml.safe_load(f.read_text())
            except yaml.YAMLError as exc:
                raise SystemExit(f"{f}: unparseable YAML: {exc}")
            if not isinstance(d, dict):
                continue
            for a in d.get("existing_annotations") or []:
                if (a.get("term") or {}).get("id") != go_id:
                    continue
                if a.get("original_reference_id") != ref:
                    continue
                act = (a.get("review") or {}).get("action")
                actions[act] += 1
                genes.append(f"{f.parent.parent.name}/{f.parent.name}")
        out[f"{go_id}|{ref}"] = {
            "n_rows": sum(actions.values()),
            "n_genes": len(set(genes)),
            "actions": dict(actions),
        }
        print(f"{go_id} from {ref}: {sum(actions.values())} rows "
              f"across {len(set(genes))} genes")
        for act, n in actions.most_common():
            print(f"    {act}: {n}")
        print()

    dest = Path(__file__).resolve().parent / "sibling_verdicts.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
