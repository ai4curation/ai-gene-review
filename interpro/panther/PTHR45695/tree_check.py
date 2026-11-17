"""Locate the PAINT nodes of PTHR45695-paint.tsv and the reviewed members of
PTHR45695-entries.csv in the PANTHER family trees.

Run from the repository root:

    uv run python interpro/panther/PTHR45695/tree_check.py

Writes interpro/panther/PTHR45695/PTHR45695-tree-check.txt.

Why this exists: the PAINT slice for PTHR45695 is built from the leaf IBA rows of
the proteins that InterPro/UniProt classify in PTHR45695 (the entries file), so a
node lands in the slice whenever one of those proteins inherits an IBA from it.
That is only the family's own node if PANTHER's tree places the protein in the
same family as InterPro's HMM classification does. This script checks that, for
every node and every member, against PANTHER's own trees.

Trees are loaded with ``ai_gene_review.etl.panther_trees.load_family`` (the cached
compact tree under ``.cache/panther_trees/`` or, if absent, the PANTHER treeinfo
service). Besides PTHR45695, the families named in OTHER_FAMILIES are loaded so
that a node or member absent from PTHR45695 can be located. If PANTHER's own
node-to-family table (PAINT_TreeGrafter_Annotations_TOTAL.txt.gz, downloaded to
``.cache/panther/`` by ``just fetch-panther-paint``) is present, its row for each
node is printed too. Subfamily names come from panther.obo. Nothing about the
result is hard-coded: a node or member that is not found is reported as not found.
"""

from __future__ import annotations

import csv
import gzip
from collections import Counter
from pathlib import Path

from ai_gene_review.etl.panther_trees import leaf_nodes_for, leaves_below, load_family

FAMILY = "PTHR45695"
# Families that PANTHER's TreeGrafter table assigns the out-of-family nodes to.
OTHER_FAMILIES = ["PTHR24230", "PTHR24241", "PTHR24243", "PTHR24228"]
HERE = Path("interpro/panther") / FAMILY
OBO = Path("interpro/panther/panther.obo")
TREEGRAFTER = Path(".cache/panther/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz")
SHOWN_ORGANISMS = {
    "Homo sapiens",
    "Mus musculus",
    "Rattus norvegicus",
    "Danio rerio",
    "Drosophila melanogaster",
    "Caenorhabditis elegans",
}


def obo_names() -> dict[str, str]:
    """Return PANTHER id -> official name from panther.obo."""
    names: dict[str, str] = {}
    current = None
    for line in OBO.read_text().splitlines():
        if line.startswith("id: "):
            current = line[4:].strip().removeprefix("PANTHER:")
        elif line.startswith("name: ") and current:
            names[current] = line[6:].strip()
    return names


def treegrafter_rows(nodes: set[str]) -> dict[str, str]:
    """Return PTN -> 'PTHRnnnnn:ANn PTHRnnnnn:SFn' from PANTHER's node table, if cached."""
    if not TREEGRAFTER.exists():
        return {}
    out: dict[str, str] = {}
    with gzip.open(TREEGRAFTER, "rt") as fh:
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) >= 2 and cols[-1] in nodes:
                an = cols[0]
                sf = cols[1].split()[0] if cols[1].strip().startswith("PTHR") else "(no SF)"
                out[cols[-1]] = f"{an} {sf}"
    return out


def root_of(tree: dict) -> str:
    """Internal node whose clade holds every leaf."""
    n = len(tree["leaves"])
    for node, below in tree["under"].items():
        if len(below) == n:
            return node
    return "?"


def main() -> None:
    names = obo_names()
    trees: dict[str, dict] = {}
    for fam in [FAMILY, *OTHER_FAMILIES]:
        tree = load_family(fam)
        if tree is not None:
            trees[fam] = tree

    paint = list(csv.DictReader(open(HERE / f"{FAMILY}-paint.tsv"), delimiter="\t"))
    nodes = sorted({r["node"] for r in paint})
    tg = treegrafter_rows(set(nodes))
    members = list(csv.DictReader(open(HERE / f"{FAMILY}-entries.csv")))

    lines: list[str] = []
    for fam, tree in trees.items():
        lines.append(
            f"tree {fam} ({names.get(fam, '?')}) root {root_of(tree)} "
            f"leaves {len(tree['leaves'])}"
        )
    missing = [f for f in [FAMILY, *OTHER_FAMILIES] if f not in trees]
    if missing:
        lines.append(f"trees not loaded: {', '.join(missing)}")
    lines.append(
        "TreeGrafter node table: "
        + ("read from " + str(TREEGRAFTER) if TREEGRAFTER.exists() else "not cached")
    )
    lines.append("")

    lines.append("== PAINT nodes of PTHR45695-paint.tsv")
    for node in nodes:
        rows = [r for r in paint if r["node"] == node]
        terms = ", ".join(
            f"{r['go_id']} {r['evidence']}{' NOT' if r['negated'] == 'true' else ''}"
            for r in rows
        )
        homes = [fam for fam, t in trees.items() if node in t["under"] or node in t["leaves"]]
        lines.append(f"node {node}: PAINT rows {terms}")
        lines.append(f"  TreeGrafter: {tg.get(node, 'no row')}")
        if not homes:
            lines.append("  not found in any loaded tree")
            continue
        for fam in homes:
            tree = trees[fam]
            below = leaves_below(tree, node)
            sfs = Counter(tree["leaves"][leaf]["subfamily"] for leaf in below)
            sf_text = ", ".join(
                f"{sf} {names.get(sf, '?')}={n}" for sf, n in sorted(sfs.items())
            )
            lines.append(f"  in tree {fam}; leaves {len(below)}; leaf subfamilies: {sf_text}")
            shown = sorted(
                (tree["leaves"][leaf]["organism"], tree["leaves"][leaf]["symbol"],
                 tree["leaves"][leaf]["uniprot"], tree["leaves"][leaf]["subfamily"])
                for leaf in below
                if tree["leaves"][leaf]["organism"] in SHOWN_ORGANISMS
            )
            for org, sym, acc, sf in shown:
                lines.append(f"    {org} | {sym} | {acc} | {sf}")
    lines.append("")

    lines.append("== Reviewed members of PTHR45695-entries.csv")
    for m in sorted(members, key=lambda r: (r["subfamily"], r["source_tax_name"], r["gene"])):
        acc = m["id"]
        placed = []
        for fam, tree in trees.items():
            for leaf in leaf_nodes_for(tree, acc):
                inherits = sorted(
                    n for n in nodes if leaf in tree["under"].get(n, []) or n == leaf
                )
                placed.append(
                    f"leaf {leaf} of {fam} in {tree['leaves'][leaf]['subfamily']}; "
                    f"below PAINT nodes {inherits if inherits else 'none'}"
                )
        where = "; ".join(placed) if placed else "not a leaf of any loaded tree"
        lines.append(
            f"{acc} {m['gene'] or '-'} | {m['source_tax_name']} | entries subfamily "
            f"{m['subfamily']} | {where}"
        )

    out = HERE / f"{FAMILY}-tree-check.txt"
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
