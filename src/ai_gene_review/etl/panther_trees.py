"""PANTHER family trees: fetch, cache and query leaf/ancestor relations.

PAINT annotates internal tree nodes (``PTN`` ids), but ``IBD.gaf`` carries no tree, so
asking "which proteins sit below node X" or "which nodes sit above protein P" needs the
family tree from the PANTHER API (``treeinfo``). Trees are cached as a compact JSON under
``.cache/panther_trees/`` (git-ignored): ``{"leaves": {ptn: info}, "under": {ptn: [leaf ptns]}}``.
"""

from __future__ import annotations

import gzip
import json
import sys
import time
from pathlib import Path
from typing import Any

import requests

TREE_URL = "https://pantherdb.org/services/oai/pantherdb/treeinfo"
DEFAULT_CACHE = Path(".cache") / "panther_trees"


def _children(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (the API returns a dict for a single child)."""
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def compact_tree(tree: dict) -> dict[str, Any]:
    """Reduce a treeinfo response to ``{"leaves": {ptn: info}, "under": {ptn: [leaf ptns]}}``.

    ``under`` lists, for every internal node, the leaf PTNs below it. A leaf's
    ``uniprot`` is parsed from ``node_name`` (``ORG|DB=id|UniProtKB=ACC``).

    >>> leaf = {"persistent_id": "PTN3", "node_name": "HUMAN|HGNC=1|UniProtKB=P1",
    ...         "organism": "Homo sapiens", "gene_symbol": "A"}
    >>> root = {"persistent_id": "PTN1", "children": {"annotation_node": [
    ...     {"persistent_id": "PTN2", "children": {"annotation_node": leaf}}]}}
    >>> t = compact_tree({"search": {"tree_topology": {"annotation_node": root}}})
    >>> t["under"], t["leaves"]["PTN3"]["uniprot"]
    ({'PTN2': ['PTN3'], 'PTN1': ['PTN3']}, 'P1')
    """
    leaves: dict[str, dict] = {}
    under: dict[str, list[str]] = {}

    def walk(n: dict) -> list[str]:
        pid = n.get("persistent_id", "")
        kids = _children(n)
        if not kids:
            acc = ""
            for tok in n.get("node_name", "").split("|"):
                if tok.startswith("UniProtKB="):
                    acc = tok.split("=", 1)[1]
            leaves[pid] = {
                "uniprot": acc,
                "organism": n.get("organism", ""),
                "symbol": n.get("gene_symbol", ""),
                "subfamily": n.get("prop_sf_id", "") or n.get("sf_id", ""),
            }
            return [pid]
        below: list[str] = []
        for c in kids:
            below.extend(walk(c))
        under[pid] = below
        return below

    sys.setrecursionlimit(100000)
    walk(tree["search"]["tree_topology"]["annotation_node"])
    return {"leaves": leaves, "under": under}


def load_family(family: str, cache_dir: Path = DEFAULT_CACHE) -> dict[str, Any] | None:
    """Return the compact tree for a PANTHER family, from cache or the PANTHER API.

    Returns ``None`` when the tree cannot be fetched (the API is retried four times).
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{family}.json.gz"
    if path.exists():
        with gzip.open(path, "rt") as fh:
            return json.load(fh)
    for attempt in range(4):
        try:
            r = requests.get(TREE_URL, params={"family": family}, timeout=300)
            if r.status_code == 200:
                data = compact_tree(r.json())
                with gzip.open(path, "wt") as fh:
                    json.dump(data, fh)
                return data
        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"{family}: {e}", file=sys.stderr)
        time.sleep(5 * (attempt + 1))
    print(f"{family}: tree not fetched", file=sys.stderr)
    return None


def leaves_below(tree: dict[str, Any], node: str) -> list[str]:
    """Leaf PTNs at or below ``node`` (a leaf is its own clade).

    >>> t = {"leaves": {"PTN3": {}}, "under": {"PTN1": ["PTN3"]}}
    >>> leaves_below(t, "PTN1"), leaves_below(t, "PTN3"), leaves_below(t, "PTN9")
    (['PTN3'], ['PTN3'], [])
    """
    return [node] if node in tree["leaves"] else list(tree["under"].get(node, []))


def leaf_nodes_for(tree: dict[str, Any], accession: str) -> list[str]:
    """Leaf PTNs whose UniProt accession is ``accession`` (isoform suffixes ignored).

    >>> leaf_nodes_for({"leaves": {"PTN3": {"uniprot": "P1"}}, "under": {}}, "P1-2")
    ['PTN3']
    """
    base = accession.split("-")[0]
    return [pid for pid, info in tree["leaves"].items() if info.get("uniprot") == base]


def ancestors_of(tree: dict[str, Any], leaf: str) -> set[str]:
    """Internal nodes whose clade contains ``leaf``, plus the leaf itself.

    >>> t = {"leaves": {"PTN3": {}, "PTN4": {}}, "under": {"PTN1": ["PTN3", "PTN4"], "PTN2": ["PTN4"]}}
    >>> sorted(ancestors_of(t, "PTN4"))
    ['PTN1', 'PTN2', 'PTN4']
    """
    return {node for node, below in tree["under"].items() if leaf in below} | {leaf}
