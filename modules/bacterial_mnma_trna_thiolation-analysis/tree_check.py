"""List the PANTHER tree leaves under every PAINT node of the Tus relay / MnmA families.

Run from the repository root:

    uv run python modules/bacterial_mnma_trna_thiolation-analysis/tree_check.py

Writes modules/bacterial_mnma_trna_thiolation-analysis/tree-check.txt. Trees are loaded
with ``ai_gene_review.etl.panther_trees.load_family`` (the cached compact reference-genome
tree under ``.cache/panther_trees/`` or the PANTHER treeinfo service). PAINT rows come from
each family's ``<PTHR>-paint.tsv``. Nothing is hard-coded: every line is derived from the
tree and the PAINT table. Families with no PAINT rows still get a leaf inventory.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from ai_gene_review.etl.panther_trees import leaves_below, load_family

FAMILIES = ["PTHR33279", "PTHR34874", "PTHR38780", "PTHR37526", "PTHR37010", "PTHR11933"]
PANTHER = Path("interpro/panther")
OUT = Path("modules/bacterial_mnma_trna_thiolation-analysis/tree-check.txt")


def fmt(info: dict) -> str:
    return f"UniProtKB:{info['uniprot']} {info['symbol']} [{info['organism']}] {info['subfamily']}"


def main() -> None:
    lines: list[str] = []
    for fam in FAMILIES:
        tree = load_family(fam)
        if tree is None:
            lines.append(f"{fam}: tree could not be loaded")
            continue
        leaves = tree["leaves"]
        sfc = Counter(v["subfamily"] for v in leaves.values())
        lines.append(f"== {fam}: {len(leaves)} reference-tree leaves; subfamilies "
                     + ", ".join(f"{k}={v}" for k, v in sorted(sfc.items())))
        for leaf in sorted(leaves, key=lambda x: (leaves[x]["subfamily"], leaves[x]["organism"])):
            lines.append(f"  leaf {leaf}: {fmt(leaves[leaf])}")
        paint = PANTHER / fam / f"{fam}-paint.tsv"
        rows = list(csv.DictReader(open(paint), delimiter="\t")) if paint.exists() else []
        seen: set[str] = set()
        for r in rows:
            node = r["node"]
            if node in seen:
                continue
            seen.add(node)
            terms = "; ".join(f"{x['go_id']} {x['evidence']}{' NOT' if x['negated'] == 'true' else ''}"
                              for x in rows if x["node"] == node)
            clade = leaves_below(tree, node)
            lines.append(f"  node {node} ({terms}): {len(clade)} leaves")
            for leaf in sorted(clade):
                lines.append(f"    {fmt(leaves[leaf])}")
    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
