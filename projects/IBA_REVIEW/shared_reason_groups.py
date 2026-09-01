"""Count identical `review.reason` strings shared across annotations.

Exists because the "a shared reason is suspicious only under a corrective action"
paragraph in projects/IBA_REVIEW.md quotes figures that a reader cannot re-derive with
grep: `reason` is usually a folded block scalar, so line-wise tools see fragments, not
values. Every figure in that paragraph should come from this script.

PREDICATE (one, stated here, applied to every figure):
  * group annotations by the EXACT `review.reason` string, across all files in the glob
  * a group qualifies when its rows span >=3 distinct GO term ids
  * counts reported are of ANNOTATION ROWS, not of distinct terms

The threshold is on TERMS, not rows, and that is the whole point: a reason applied three
times to one term under three evidence codes is one judgement recorded three times, not
boilerplate. Spanning >=3 distinct terms means the same sentence is being asked to
justify verdicts on genuinely different annotations. A row threshold would be dead code
here -- >=3 distinct terms already implies >=3 rows -- so there isn't one.

No minimum reason length is applied. Terse tags ("Stale ISO transfer.") count like any
other string; filtering them out is a tuning knob that makes figures irreproducible
unless the cutoff travels with them.

Usage:  python3 projects/IBA_REVIEW/shared_reason_groups.py [glob ...] [--action ACTION] [--list]
Defaults to genes/mouse/*/*-ai-review.yaml.
  --action REMOVE   restrict to rows whose review.action is REMOVE (the scoped figure)
  --list            print each qualifying group: rows, genes, and the reason's first line

Exits 2 if the glob matches no files or the self-test fails; otherwise 0. This is a
measurement tool, not a checker -- it has no notion of a finding.
"""
import glob
import sys
from collections import defaultdict

import yaml

DEFAULT_GLOB = "genes/mouse/*/*-ai-review.yaml"
MIN_TERMS = 3


def collect(paths, action=None):
    """Return {reason: [(gene, term_id), ...]} for rows carrying a reason."""
    groups = defaultdict(list)
    for path in paths:
        with open(path) as handle:
            doc = yaml.safe_load(handle) or {}
        gene = doc.get("gene_symbol") or path.split("/")[-2]
        for ann in doc.get("existing_annotations") or []:
            review = ann.get("review") or {}
            reason = review.get("reason")
            if not reason:
                continue
            if action is not None and review.get("action") != action:
                continue
            groups[reason].append((gene, (ann.get("term") or {}).get("id")))
    return groups


def qualifying(groups):
    """Apply the predicate. Returns {reason: rows} for groups that qualify."""
    return {
        reason: rows
        for reason, rows in groups.items()
        if len({term for _gene, term in rows}) >= MIN_TERMS
    }


def _self_test():
    """Assert the predicate bites, on constructed input.

    Each arm can fail on its own: loosening MIN_TERMS admits the one-term group,
    tightening it rejects the three-term group, and counting distinct terms rather
    than rows changes the reported number for the qualifying group. The two-row arm
    is the inflation case a rows-based threshold would wave through.
    """
    three_terms = {"r": [("G", "GO:1"), ("G", "GO:2"), ("G", "GO:3")]}
    one_term = {"r": [("G", "GO:1"), ("G", "GO:1"), ("G", "GO:1")]}
    two_terms = {"r": [("G", "GO:1"), ("G", "GO:2"), ("G", "GO:2")]}
    if not qualifying(three_terms):
        return "three rows over three terms should qualify"
    if qualifying(one_term):
        return "three rows on one term should NOT qualify (one judgement, thrice)"
    if qualifying(two_terms):
        return "three rows over only two terms should NOT qualify"
    if len(qualifying(three_terms)["r"]) != 3:
        return "qualifying() must report ROW count, not distinct-term count"
    return None


def main(argv):
    failure = _self_test()
    if failure:
        print(f"self-test failed: {failure}")
        return 2

    action = None
    show = False
    patterns = []
    rest = list(argv)
    while rest:
        arg = rest.pop(0)
        if arg == "--list":
            show = True
        elif arg == "--action":
            if not rest:
                print("--action needs a value, e.g. --action REMOVE")
                return 2
            action = rest.pop(0)
        elif arg.startswith("--action="):
            action = arg.split("=", 1)[1]
        elif arg.startswith("--"):
            print(f"unrecognized flag: {arg}")
            return 2
        else:
            patterns.append(arg)
    if action is not None and not action.strip():
        print("--action: empty value. Give an action, e.g. --action REMOVE")
        return 2

    paths = sorted({p for pattern in (patterns or [DEFAULT_GLOB]) for p in glob.glob(pattern)})
    if not paths:
        print(f"no files matched: {' '.join(patterns or [DEFAULT_GLOB])}")
        return 2

    groups = qualifying(collect(paths, action))
    rows = sum(len(v) for v in groups.values())
    largest = max((len(v) for v in groups.values()), default=0)
    scope = f"action={action}" if action else "all actions"
    print(f"{len(paths)} files, {scope}: {len(groups)} groups over {rows} rows, "
          f"largest {largest} rows")
    if show:
        for reason, members in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            genes = sorted({gene for gene, _term in members})
            print(f"  {len(members):4d}  {','.join(genes)}  :: {reason.splitlines()[0][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
