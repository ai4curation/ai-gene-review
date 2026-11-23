"""Map the PAINT GO:0004370 (glycerol kinase activity) gain and losses in PTHR10196 onto
PANTHER subfamilies, using the family tree.

Run from the repository root:

    uv run python interpro/panther/PTHR10196/tree_check.py

Writes interpro/panther/PTHR10196/PTHR10196-tree-check.txt. The tree is loaded with
``ai_gene_review.etl.panther_trees.load_family`` (the cached compact tree under
``.cache/panther_trees/`` or, if absent, the PANTHER treeinfo service). PAINT rows are
read from PTHR10196-paint.tsv and subfamily names from panther.obo. Nothing about the
result is hard-coded: each subfamily is classified from the leaves the tree places under
the IBD node and under each IRD/IKR node.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from ai_gene_review.etl.panther_trees import leaves_below, load_family

FAMILY = "PTHR10196"
TERM = "GO:0004370"
HERE = Path("interpro/panther") / FAMILY
OBO = Path("interpro/panther/panther.obo")


def obo_names() -> dict[str, str]:
    """Return PANTHER id -> official name from panther.obo."""
    names: dict[str, str] = {}
    current = None
    for line in OBO.read_text().splitlines():
        if line.startswith("id: "):
            current = line[4:].strip()
        elif line.startswith("name: ") and current:
            names[current] = line[6:].strip()
    return names


def main() -> None:
    """Classify every subfamily in the tree against the PAINT gain/loss calls."""
    tree = load_family(FAMILY)
    if tree is None:
        raise SystemExit(f"{FAMILY}: tree could not be loaded")
    leaves = tree["leaves"]
    names = obo_names()
    rows = [
        r
        for r in csv.DictReader(open(HERE / f"{FAMILY}-paint.tsv"), delimiter="\t")
        if r["go_id"] == TERM
    ]
    gains = [r["node"] for r in rows if r["negated"] == "false"]
    losses = [(r["node"], r["evidence"]) for r in rows if r["negated"] == "true"]

    def sf(leaf: str) -> str:
        return leaves[leaf]["subfamily"]

    lines = [
        f"tree {FAMILY} leaves {len(leaves)} (compact tree via ai_gene_review.etl.panther_trees.load_family)",
        f"term {TERM}: IBD nodes {', '.join(gains)}; negated nodes "
        + ", ".join(f"{n} ({e})" for n, e in losses),
    ]
    under_gain: set[str] = set()
    for n in gains:
        clade = leaves_below(tree, n)
        under_gain |= set(clade)
        counts = Counter(sf(x) for x in clade)
        lines.append(
            f"IBD {n}: leaves {len(clade)}; leaf subfamilies "
            + ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        )
    negated_leaf: dict[str, str] = {}
    for n, ev in losses:
        clade = leaves_below(tree, n)
        for x in clade:
            negated_leaf[x] = n
        counts = Counter(sf(x) for x in clade)
        lines.append(
            f"{ev} {n}: leaves {len(clade)}; leaf subfamilies "
            + (
                ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
                or "none (node not in tree)"
            )
        )
        if len(clade) > 5:
            continue
        for x in clade:
            info = leaves[x]
            lines.append(
                f"  leaf of {n}: {x} UniProtKB:{info['uniprot']} {info['symbol']} "
                f"{info['organism']} {info['subfamily']}"
            )
    by_sf: dict[str, list[str]] = defaultdict(list)
    for leaf in leaves:
        by_sf[sf(leaf)].append(leaf)
    lines.append("subfamily classification (total / under IBD / under a negated node):")
    for s in sorted(by_sf, key=lambda k: (len(k), k)):
        members = by_sf[s]
        n_gain = sum(1 for x in members if x in under_gain)
        neg = [x for x in members if x in negated_leaf]
        if n_gain == 0:
            verdict = "OUTSIDE_GAIN"
        elif len(neg) == len(members):
            verdict = "NEGATED"
        elif n_gain == len(members) and not neg:
            verdict = "INHERITS"
        elif n_gain == len(members):
            verdict = "INHERITS_WITH_LEAF_EXCEPTIONS"
        else:
            verdict = "MIXED"
        label = names.get(f"PANTHER:{s}", "?")
        extra = (
            " negated leaves: "
            + ", ".join(
                f"UniProtKB:{leaves[x]['uniprot']} ({negated_leaf[x]})" for x in neg
            )
            if neg and len(neg) < len(members)
            else ""
        )
        lines.append(
            f"  {s} [{label}] {len(members)} / {n_gain} / {len(neg)} {verdict}{extra}"
        )
    out = HERE / f"{FAMILY}-tree-check.txt"
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
