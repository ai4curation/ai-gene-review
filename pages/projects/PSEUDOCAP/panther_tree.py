"""Inspect a PANTHER family tree around a PAINT node (PTN).

Fetches the family's tree topology from the PANTHER API
(``/services/oai/pantherdb/treeinfo``) into the git-ignored
``.cache/paint/trees/`` directory, then reports what sits below a given
annotation node: the event that created it, its subfamily composition, and
every leaf with organism, symbol and definition. This is what a node-level
``source_defects`` call needs in order to say whether an IBD's term suits the
clade, rather than inferring it from the leaf GAF alone.

The family that holds a node is resolved from one of the node's IBD seeds
(``.cache/paint/IBD.gaf``) through the PANTHER ``geneinfo`` service, and the
PTN-to-family map is cached alongside the trees.

Usage::

    uv run python projects/PSEUDOCAP/panther_tree.py node PTN000764516
    uv run python projects/PSEUDOCAP/panther_tree.py node PTN000241400 --depth 3
    uv run python projects/PSEUDOCAP/panther_tree.py node PTN000764516 \
        --contains O50175,P76216      # smallest clade holding these accessions
    uv run python projects/PSEUDOCAP/panther_tree.py family PTHR30420
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".cache" / "paint" / "trees"
IBD = ROOT / ".cache" / "paint" / "IBD.gaf"
MAP = CACHE / "ptn_family.json"
API = "https://pantherdb.org/services/oai/pantherdb"


def _get(url: str, params: dict) -> dict:
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=120)
            r.raise_for_status()
            return r.json()
        except Exception:  # noqa: BLE001 - transient API failures are expected
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")


def fetch_family(family: str) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{family}.json"
    if not path.exists():
        data = _get(f"{API}/treeinfo", {"family": family})
        path.write_text(json.dumps(data), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def seeds_of(node: str) -> list[str]:
    """Accessions in the WITH/FROM of every IBD at this node."""
    out: list[str] = []
    if not IBD.exists():
        return out
    for line in IBD.open():
        if line.startswith("!"):
            continue
        f = line.rstrip("\n").split("\t")
        if len(f) > 7 and f[1] == node:
            for s in f[7].split("|"):
                acc = s.removeprefix("UniProtKB:")
                if s.startswith("UniProtKB:") and acc not in out:
                    out.append(acc)
    return out


def families_of_accession(acc: str) -> list[str]:
    """PANTHER families cross-referenced from the accession's UniProt entry."""
    data = _get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json",
        {"fields": "xref_panther"},
    )
    out: list[str] = []
    for ref in data.get("uniProtKBCrossReferences", []) or []:
        if ref.get("database") == "PANTHER":
            fam = str(ref.get("id", "")).split(":")[0]
            if fam.startswith("PTHR") and fam not in out:
                out.append(fam)
    return out


def family_of_node(node: str, hint: str | None = None) -> str:
    if hint:
        return hint
    cache = json.loads(MAP.read_text(encoding="utf-8")) if MAP.exists() else {}
    if node in cache:
        return cache[node]
    for acc in seeds_of(node):
        for fam in families_of_accession(acc):
            try:
                tree = fetch_family(fam)
            except Exception:  # noqa: BLE001
                continue
            if not find_node(root_of(tree), node):
                continue
            CACHE.mkdir(parents=True, exist_ok=True)
            cache[node] = fam
            MAP.write_text(json.dumps(cache, indent=0, sort_keys=True), encoding="utf-8")
            return fam
    raise SystemExit(
        f"Could not resolve a family for {node}. Pass --family PTHRxxxxx "
        "(the node may sit in a family none of its seeds is assigned to)."
    )


def root_of(tree: dict) -> dict:
    return tree["search"]["tree_topology"]["annotation_node"]


def children(node: dict) -> list[dict]:
    kids = node.get("children", {}).get("annotation_node", [])
    return kids if isinstance(kids, list) else [kids]


def find_node(node: dict, ptn: str) -> dict | None:
    if node.get("persistent_id") == ptn:
        return node
    for kid in children(node):
        hit = find_node(kid, ptn)
        if hit:
            return hit
    return None


def leaves(node: dict) -> list[dict]:
    kids = children(node)
    if not kids:
        return [node] if node.get("tree_node_type") == "LEAF" or "organism" in node else []
    out: list[dict] = []
    for kid in kids:
        out.extend(leaves(kid))
    return out


def leaf_line(leaf: dict) -> str:
    acc = ""
    for part in str(leaf.get("node_name", "")).split("|"):
        if part.startswith("UniProtKB="):
            acc = part.split("=", 1)[1]
    return (
        f"    {acc or '-':<12} {leaf.get('gene_symbol', '-') or '-':<14} "
        f"{(leaf.get('organism') or '-')[:34]:<34} "
        f"{(leaf.get('prop_sf_id') or leaf.get('sf_id') or '-'):<16} "
        f"{(leaf.get('definition') or leaf.get('sf_name') or '')[:50]}"
    )


def summarise(node: dict, depth: int, indent: int = 0, path: str = "") -> None:
    lv = leaves(node)
    sfs: dict[str, int] = {}
    for leaf in lv:
        sfs[leaf.get("prop_sf_id") or leaf.get("sf_id") or "-"] = (
            sfs.get(leaf.get("prop_sf_id") or leaf.get("sf_id") or "-", 0) + 1
        )
    label = node.get("persistent_id", "?")
    kind = node.get("event_type") or node.get("tree_node_type") or "?"
    sp = node.get("species") or node.get("organism") or ""
    head = f"{'  ' * indent}{path}{label}  {kind}  {sp}"
    if node.get("tree_node_type") == "LEAF":
        print(head.rstrip())
        print(leaf_line(node))
        return
    print(f"{head.rstrip()}  [{len(lv)} leaves; " + ", ".join(f"{k}:{v}" for k, v in sorted(sfs.items())) + "]")
    if depth <= 0:
        return
    for i, kid in enumerate(children(node)):
        summarise(kid, depth - 1, indent + 1, f"{i + 1}. ")


def accessions(leaf: dict) -> str:
    for part in str(leaf.get("node_name", "")).split("|"):
        if part.startswith("UniProtKB="):
            return part.split("=", 1)[1]
    return ""


def minimal_clade(root: dict, wanted: set[str]) -> dict | None:
    """Smallest node whose leaves contain every wanted accession."""
    if not wanted <= {accessions(leaf) for leaf in leaves(root)}:
        return None
    for kid in children(root):
        hit = minimal_clade(kid, wanted)
        if hit:
            return hit
    return root


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("node", help="report the clade below a PAINT node")
    n.add_argument("ptn")
    n.add_argument("--family", help="PTHRxxxxx, when the seeds do not resolve it")
    n.add_argument("--depth", type=int, default=2, help="levels of subclade summary (default 2)")
    n.add_argument("--leaves", action="store_true", help="list every leaf")
    n.add_argument("--contains", help="comma-separated accessions; report their smallest shared clade")

    f = sub.add_parser("family", help="report a whole family tree")
    f.add_argument("family")
    f.add_argument("--depth", type=int, default=2)

    args = ap.parse_args()

    if args.cmd == "family":
        tree = fetch_family(args.family)
        print(f"# {args.family}")
        summarise(root_of(tree), args.depth)
        return

    fam = family_of_node(args.ptn, args.family)
    tree = fetch_family(fam)
    node = find_node(root_of(tree), args.ptn)
    if node is None:
        raise SystemExit(f"{args.ptn} is not in {fam}")
    lv = leaves(node)
    print(f"# {args.ptn} in {fam}: {len(lv)} leaves, event {node.get('event_type') or node.get('tree_node_type')}")
    print(f"# seeds in IBD.gaf: {', '.join(seeds_of(args.ptn)) or 'none'}")
    summarise(node, args.depth)
    if args.leaves:
        print("\n# leaves")
        for leaf in sorted(lv, key=lambda x: (x.get("prop_sf_id") or "", x.get("organism") or "")):
            print(leaf_line(leaf))
    if args.contains:
        wanted = {a.strip() for a in args.contains.split(",") if a.strip()}
        hit = minimal_clade(root_of(tree), wanted)
        if hit is None:
            missing = wanted - {accessions(x) for x in leaves(root_of(tree))}
            print(f"\n# smallest clade containing {sorted(wanted)}: not all in {fam} (missing {sorted(missing)})")
        else:
            print(
                f"\n# smallest clade containing {sorted(wanted)}: {hit.get('persistent_id')} "
                f"({len(leaves(hit))} leaves, event {hit.get('event_type') or hit.get('tree_node_type')})"
            )


if __name__ == "__main__":
    main()
    sys.exit(0)
