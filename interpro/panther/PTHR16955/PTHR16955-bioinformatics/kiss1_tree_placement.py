"""Where PTHR16955 (KISS1) members sit on the PANTHER tree, and which PAINT nodes reach them.

Run from the repository root:

    uv run python interpro/panther/PTHR16955/PTHR16955-bioinformatics/kiss1_tree_placement.py

Three questions, answered from public PANTHER and QuickGO data:

1. Tree structure: the leaves of the PTHR16955 tree (species, symbol, subfamily) and,
   for every internal node, how many leaves sit below it and which leaves it leaves out
   relative to the root.
2. PAINT coverage: for every row of ``PTHR16955-paint.tsv``, the node it is placed at
   and the leaves below that node.
3. IBA provenance: for the reviewed members in ``PTHR16955-entries.csv`` plus any leaf
   that is a PAINT seed organism's KISS1 (zebrafish kiss1), the PANTHER nodes their
   QuickGO IBA annotations cite.

Trees come from the PANTHER treeinfo API through ``ai_gene_review.etl.panther_trees``;
IBA rows come from the QuickGO REST API. Nothing is hard-coded except the family id,
the extra accession asked about, and the evidence code.
"""

from __future__ import annotations

import collections
import csv
from pathlib import Path

import requests

from ai_gene_review.etl.panther_trees import load_family

FAMILY = "PTHR16955"
FAMILY_DIR = Path("interpro/panther") / FAMILY
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
IBA_ECO = "ECO:0000318"
#: Unreviewed tree leaves whose IBA provenance is also reported: zebrafish kiss1, the
#: only non-mammalian leaf and the organism of one PAINT seed (ZFIN:ZDB-GENE-080128-1).
EXTRA_ACCESSIONS = ["A8C5J1"]


def leaf_label(tree: dict, leaf: str) -> str:
    """Return ``PTN (organism symbol accession subfamily)`` for a leaf."""
    info = tree["leaves"][leaf]
    return f"{leaf} ({info['organism']} {info['symbol'] or '-'} {info['uniprot']} {info['subfamily']})"


def iba_rows(accession: str) -> list[tuple[str, str, str]]:
    """Return ``(GO id, GO name, PANTHER node)`` for the QuickGO IBA rows of ``accession``."""
    params = {
        "geneProductId": accession,
        "evidenceCode": IBA_ECO,
        "evidenceCodeUsage": "exact",
        "limit": 100,
        "includeFields": "goName",
    }
    r = requests.get(QUICKGO, params=params, headers={"Accept": "application/json"}, timeout=120)
    r.raise_for_status()
    out = []
    for row in r.json().get("results", []):
        nodes = [
            w["connectedXrefs"][0]["id"]
            for w in row.get("withFrom") or []
            if w.get("connectedXrefs") and w["connectedXrefs"][0].get("db") == "PANTHER"
        ]
        out.append((row["goId"], row.get("goName") or "", ",".join(nodes) or "-"))
    return sorted(set(out))


def main() -> None:
    """Print the tree structure, PAINT coverage and IBA provenance for the family."""
    tree = load_family(FAMILY)
    if tree is None:
        print(f"{FAMILY}: tree could not be fetched")
        return
    under = tree["under"]
    root = max(under, key=lambda n: len(under[n]))
    all_leaves = set(under[root])

    print(f"# {FAMILY}: {len(tree['leaves'])} leaves, {len(under)} internal nodes, root {root}")
    print("\n## Leaves")
    sf_counts = collections.Counter(tree["leaves"][leaf]["subfamily"] for leaf in all_leaves)
    print("subfamilies:", dict(sf_counts))
    for leaf in sorted(all_leaves, key=lambda x: tree["leaves"][x]["organism"]):
        print(" ", leaf_label(tree, leaf))

    print("\n## Internal nodes (leaves below; leaves of the root NOT below)")
    for node in sorted(under, key=lambda n: -len(under[n])):
        missing = sorted(all_leaves - set(under[node]))
        if len(missing) <= 3:
            excluded = "; ".join(leaf_label(tree, m) for m in missing) or "none"
        else:
            excluded = f"{len(missing)} leaves"
        print(f"  {node}: {len(under[node])} leaves; not below: {excluded}")

    print("\n## PAINT rows")
    with (FAMILY_DIR / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            node = row["node"]
            below = under.get(node, [node] if node in tree["leaves"] else [])
            print(
                f"  {node} {row['go_id']} {row['evidence']} negated={row['negated']}"
                f" taxon={row['taxon']} seeds={row['seeds']}: {len(below)} leaves below"
                f"{' (root)' if node == root else ''}"
            )

    print("\n## IBA provenance (QuickGO)")
    with (FAMILY_DIR / f"{FAMILY}-entries.csv").open() as fh:
        accessions = [r["id"] for r in csv.DictReader(fh)] + EXTRA_ACCESSIONS
    for acc in accessions:
        rows = iba_rows(acc)
        print(f"  {acc}: {len(rows)} IBA rows")
        for go_id, name, nodes in rows:
            print(f"    {go_id} {name} <- {nodes}")


if __name__ == "__main__":
    main()
