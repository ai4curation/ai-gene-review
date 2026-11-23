"""Where PTHR24372 members sit on the PANTHER 19 trees, and which PAINT nodes reach them.

Run from the repository root:

    uv run python interpro/panther/PTHR24372/PTHR24372-bioinformatics/lgr_tree_placement.py

Three questions, all answered from public PANTHER and QuickGO data:

1. Clade structure: which subfamilies sit below each PAINT-annotated node of the
   PTHR24372 tree, and below the internal nodes that separate the three LGR types.
2. Tree membership: which reviewed members listed in ``PTHR24372-entries.csv``
   (InterPro's HMM classification) are leaves of the PTHR24372 tree, and, for those
   that are not, whether they are leaves of the PTHR45836 (SLIT HOMOLOG) tree.
3. IBA provenance: for every reviewed member, the PANTHER nodes its QuickGO IBA
   annotations cite, and whether each node is an internal node of the PTHR24372 tree.

Trees come from the PANTHER treeinfo API through ``ai_gene_review.etl.panther_trees``
(cached as small JSON files); IBA rows come from the QuickGO REST API. Nothing is
hard-coded except the node and family identifiers being asked about.
"""

from __future__ import annotations

import argparse
import collections
import csv
import sys
from pathlib import Path

import requests

from ai_gene_review.etl.panther_trees import load_family

FAMILY = "PTHR24372"
FAMILY_DIR = Path("interpro/panther") / FAMILY
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
IBA_ECO = "ECO:0000318"
#: Internal nodes that separate the LGR types in this tree (found by walking it), plus
#: the vertebrate LGR4/5/6 node and the LGR6 clade.
STRUCTURE_NODES = [
    "PTN000689980",
    "PTN001224575",
    "PTN001556595",
    "PTN008402522",
    "PTN002542418",
    "PTN002809239",
    "PTN001223648",
    "PTN001224607",
    "PTN001970551",
    "PTN001222876",
]


def subfamily_counts(tree: dict, node: str) -> str:
    """Return ``SFn:count`` pairs for the leaves below ``node``."""
    leaves = tree["under"].get(node, [])
    counts = collections.Counter(
        tree["leaves"][leaf]["subfamily"].split(":")[-1] for leaf in leaves
    )
    return " ".join(f"{sf}:{n}" for sf, n in sorted(counts.items()))


def paint_nodes(paint_tsv: Path) -> list[tuple[str, str, str]]:
    """Return ``(node, go_id, evidence)`` for every row of the family's PAINT slice."""
    with paint_tsv.open() as fh:
        return [
            (r["node"], r["go_id"], r["evidence"] + ("/NOT" if r["negated"] == "true" else ""))
            for r in csv.DictReader(fh, delimiter="\t")
        ]


def reviewed_members(entries_csv: Path) -> list[dict]:
    """Return the reviewed member rows of the family entries table."""
    with entries_csv.open() as fh:
        return list(csv.DictReader(fh))


def iba_nodes(accessions: list[str]) -> dict[str, list[tuple[str, str]]]:
    """Map accession -> [(PANTHER node, GO id)] for its QuickGO IBA annotations."""
    out: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    page = 1
    while True:
        r = requests.get(
            QUICKGO,
            params={
                "geneProductId": ",".join(accessions),
                "evidenceCode": IBA_ECO,
                "limit": 100,
                "page": page,
            },
            headers={"Accept": "application/json"},
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()
        for row in data["results"]:
            acc = row["geneProductId"].split(":")[-1]
            for group in row.get("withFrom") or []:
                for xref in group["connectedXrefs"]:
                    if xref["db"] == "PANTHER":
                        out[acc].append((xref["id"], row["goId"]))
        if page >= data["pageInfo"]["total"]:
            break
        page += 1
    return out


def main(argv: list[str] | None = None) -> int:
    """Print the three reports."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tree-cache-dir", type=Path, default=Path(".cache/panther_trees"))
    args = parser.parse_args(argv)

    tree = load_family(FAMILY, args.tree_cache_dir)
    slit = load_family("PTHR45836", args.tree_cache_dir)
    if tree is None or slit is None:
        print("PANTHER tree could not be fetched", file=sys.stderr)
        return 1
    print(f"PTHR24372 tree: {len(tree['leaves'])} leaves, {len(tree['under'])} internal nodes")

    print("\n## 1. Subfamilies below PAINT-annotated and structural nodes")
    seen = set()
    for node, go_id, ev in paint_nodes(FAMILY_DIR / f"{FAMILY}-paint.tsv"):
        if node in seen:
            continue
        seen.add(node)
        if node in tree["under"]:
            print(f"{node}\tin PTHR24372 tree\t{len(tree['under'][node])} leaves\t"
                  f"{subfamily_counts(tree, node)}")
        else:
            print(f"{node}\tNOT an internal node of the PTHR24372 tree")
    for node in STRUCTURE_NODES:
        print(f"{node}\tstructure\t{len(tree['under'][node])} leaves\t"
              f"{subfamily_counts(tree, node)}")

    print("\n## 2. Reviewed members: leaf of the PTHR24372 tree, or of PTHR45836")
    leaf_by_acc = {v["uniprot"]: k for k, v in tree["leaves"].items()}
    slit_by_acc = {v["uniprot"]: (k, v["subfamily"]) for k, v in slit["leaves"].items()}
    members = reviewed_members(FAMILY_DIR / f"{FAMILY}-entries.csv")
    for m in sorted(members, key=lambda r: (r["subfamily"], r["id"])):
        acc = m["id"]
        if acc in leaf_by_acc:
            where = f"PTHR24372 leaf {leaf_by_acc[acc]}"
        elif acc in slit_by_acc:
            where = f"PTHR45836 leaf {slit_by_acc[acc][0]} ({slit_by_acc[acc][1]})"
        else:
            where = "not a leaf of either tree"
        print(f"{acc}\t{m['gene'] or '-'}\t{m['source_tax_name']}\t{m['subfamily']}\t{where}")

    print("\n## 3. PANTHER nodes cited by each reviewed member's IBA annotations")
    ibas = iba_nodes([m["id"] for m in members])
    for m in sorted(members, key=lambda r: (r["subfamily"], r["id"])):
        rows = sorted(set(ibas.get(m["id"], [])))
        if not rows:
            continue
        nodes = sorted({n for n, _ in rows})
        tags = [f"{n}({'in' if n.split(':')[-1] in tree['under'] else 'off'}-tree)"
                for n in nodes]
        terms = ",".join(sorted({g for _, g in rows}))
        print(f"{m['id']}\t{m['gene'] or '-'}\t{m['subfamily']}\t{' '.join(tags)}\t{terms}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
