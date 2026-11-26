"""Map this family's PAINT rows onto the PANTHER tree and onto experimental GO evidence.

Run from the repository root:

    uv run python interpro/panther/PTHR10780/tree_check.py

Writes ``<FAMILY>-tree-check.txt`` beside this script. Nothing is hard-coded: the family
is the folder name, the tree comes from the PANTHER ``treeinfo`` service (refused if it
serves another release than the repo's pinned ``PANTHER_RELEASE``), the PAINT rows from
``<FAMILY>-paint.tsv`` and the annotations from QuickGO.

The report has four parts:

1. every internal node with its event type (speciation or duplication), taxon, leaf count
   and leaf subfamilies, indented by depth;
2. every leaf with accession, MOD id, organism and subfamily;
3. for each PAINT row, the clade below the node and, for the seeds, their leaves and the
   last common ancestor of those leaves;
4. the manual experimental GO annotations of every leaf (QuickGO), and for each PAINT
   term the leaves annotated to it or to a descendant, preceded by a positive control:
   the same query must return a hit for at least one seed, otherwise the script stops.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Any

import requests

from ai_gene_review.etl.panther_families import PANTHER_RELEASE, same_release
from ai_gene_review.etl.panther_trees import TREE_URL, served_release

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HGI", "HEP", "HTP"}


def children(node: dict) -> list[dict]:
    """Child nodes of a treeinfo node (the API returns a dict for a single child)."""
    kids = node.get("children", {}).get("annotation_node", [])
    return [kids] if isinstance(kids, dict) else kids


def fetch_tree() -> dict:
    """Fetch the family tree root node, refusing a release other than the pinned one."""
    payload = requests.get(TREE_URL, params={"family": FAMILY}, timeout=300).json()
    served = served_release(payload)
    if served is None or not same_release(served, PANTHER_RELEASE):
        raise SystemExit(f"PANTHER serves release {served}, repo is pinned to {PANTHER_RELEASE}")
    return payload["search"]["tree_topology"]["annotation_node"]


def index_tree(root: dict) -> tuple[dict[str, dict], dict[str, str | None], dict[str, list[str]]]:
    """Return ``(node by id, parent id by id, leaf ids below each id)`` for the tree."""
    nodes: dict[str, dict] = {}
    parent: dict[str, str | None] = {}
    below: dict[str, list[str]] = {}

    def walk(node: dict, up: str | None) -> list[str]:
        pid = node["persistent_id"]
        nodes[pid], parent[pid] = node, up
        kids = children(node)
        below[pid] = [pid] if not kids else [leaf for kid in kids for leaf in walk(kid, pid)]
        return below[pid]

    walk(root, None)
    return nodes, parent, below


def leaf_ids(node: dict) -> dict[str, str]:
    """Parse a leaf ``node_name`` (``ORG|DB=id|UniProtKB=ACC``) into its parts."""
    org, mod, acc = (node["node_name"].split("|") + ["", ""])[:3]
    return {"org": org, "mod": mod.replace("=", ":", 1).replace("=", ":"), "acc": acc.split("=", 1)[-1]}


def depth(pid: str, parent: dict[str, str | None]) -> int:
    """Number of ancestors of a node."""
    count = 0
    while parent[pid] is not None:
        pid, count = parent[pid], count + 1  # type: ignore[assignment]
    return count


def last_common_ancestor(leaves: list[str], parent: dict[str, str | None]) -> str:
    """Deepest node whose clade holds all the given leaves."""
    paths = []
    for leaf in leaves:
        path, pid = [], leaf
        while pid is not None:
            path.append(pid)
            pid = parent[pid]  # type: ignore[assignment]
        paths.append(path[::-1])
    lca = paths[0][0]
    for step in zip(*paths):
        if len(set(step)) > 1:
            break
        lca = step[0]
    return lca


def quickgo(params: dict[str, Any]) -> list[dict]:
    """All QuickGO annotation rows for a query (paged)."""
    rows: list[dict] = []
    page = 1
    while True:
        response = requests.get(
            f"{QUICKGO}/annotation/search",
            params={**params, "limit": 200, "page": page},
            headers={"Accept": "application/json"},
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        rows.extend(data["results"])
        if page >= data["pageInfo"]["total"]:
            return rows
        page += 1


def go_names(ids: set[str]) -> dict[str, str]:
    """GO term names for a set of ids (QuickGO ontology service)."""
    names: dict[str, str] = {}
    ordered = sorted(ids)
    for i in range(0, len(ordered), 25):
        response = requests.get(
            f"{QUICKGO}/ontology/go/terms/{','.join(ordered[i:i + 25])}",
            headers={"Accept": "application/json"},
            timeout=120,
        )
        response.raise_for_status()
        names.update({t["id"]: t["name"] for t in response.json()["results"]})
    return names


def seed_leaves(seed: str, nodes: dict[str, dict], below: dict[str, list[str]], root: str) -> list[str]:
    """Leaves whose UniProt accession or MOD id matches a PAINT seed id."""
    bare = seed.split(":", 1)[1]
    hits = []
    for leaf in below[root]:
        ids = leaf_ids(nodes[leaf])
        if ids["acc"] == bare or ids["mod"].endswith(bare):
            hits.append(leaf)
    return hits


def describe(pid: str, nodes: dict[str, dict], below: dict[str, list[str]]) -> str:
    """One-line description of an internal node."""
    node = nodes[pid]
    sf = Counter(nodes[x].get("sf_id") or nodes[x].get("prop_sf_id") for x in below[pid])
    return (
        f"{pid} {node.get('event_type')} taxon={node.get('species') or '-'} leaves={len(below[pid])} "
        + " ".join(f"{k}={v}" for k, v in sorted(sf.items()))
    )


def main() -> None:
    """Write the tree check report for FAMILY."""
    root_node = fetch_tree()
    nodes, parent, below = index_tree(root_node)
    root = root_node["persistent_id"]
    leaves = below[root]
    internal = [pid for pid in nodes if children(nodes[pid])]
    out = [
        f"tree {FAMILY} PANTHER release {PANTHER_RELEASE}: leaves {len(leaves)}, internal nodes {len(internal)}, "
        f"duplications {sum(nodes[p].get('event_type') == 'DUPLICATION' for p in internal)}",
        "",
        "== internal nodes (indented by depth) ==",
    ]
    for pid in nodes:  # insertion order is depth-first
        if pid in internal:
            out.append("  " * depth(pid, parent) + describe(pid, nodes, below))
    out += ["", "== leaves =="]
    acc_of: dict[str, str] = {}
    for leaf in leaves:
        ids = leaf_ids(nodes[leaf])
        acc_of[leaf] = ids["acc"]
        out.append(
            f"leaf {leaf} UniProtKB:{ids['acc']} {ids['mod']} {nodes[leaf].get('gene_symbol') or '-'} "
            f"[{nodes[leaf].get('organism')}] {nodes[leaf].get('sf_id') or nodes[leaf].get('prop_sf_id')}"
        )

    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        paint = [r for r in csv.DictReader(fh, delimiter="\t") if r["node"].startswith("PTN")]
    out += ["", "== PAINT rows =="]
    for row in paint:
        node = row["node"]
        orgs = Counter(nodes[x].get("organism") for x in below[node])
        dups = [p for p in internal if p != node and set(below[p]) <= set(below[node])
                and nodes[p].get("event_type") == "DUPLICATION"]
        out.append(f"{row['evidence']} {row['go_id']} negated={row['negated']} date={row['date']} at {describe(node, nodes, below)}")
        out.append(f"  species below: {len(orgs)}; duplications below: {len(dups)}; "
                   f"leaves outside this node: {len(leaves) - len(below[node])}")
        found: list[str] = []
        for seed in row["seeds"].split("|"):
            hits = seed_leaves(seed, nodes, below, root)
            found += hits
            inside = all(h in below[node] for h in hits) and bool(hits)
            out.append(f"  seed {seed}: leaf {','.join(hits) or 'NOT_IN_TREE'} below_node={inside}")
        if found:
            out.append(f"  last common ancestor of seeds: {describe(last_common_ancestor(found, parent), nodes, below)}")

    out += ["", "== manual experimental GO annotations of tree leaves (QuickGO) =="]
    accessions = sorted(set(acc_of.values()))
    rows: list[dict] = []
    for i in range(0, len(accessions), 30):
        rows += quickgo({"geneProductId": ",".join(f"UniProtKB:{a}" for a in accessions[i:i + 30])})
    if not rows:
        raise SystemExit("QuickGO returned no annotation for any leaf; query cannot be trusted")
    out.append(f"all annotations returned for {len(accessions)} leaf accessions: {len(rows)}; "
               f"by evidence: " + " ".join(f"{k}={v}" for k, v in sorted(Counter(r['goEvidence'] for r in rows).items())))
    exp = [r for r in rows if r["goEvidence"] in EXPERIMENTAL and r["goId"] != "GO:0005515"]
    names = go_names({r["goId"] for r in rows} | {r["go_id"] for r in paint})
    leaf_of = {acc: leaf for leaf, acc in acc_of.items()}
    seen: set[tuple] = set()
    for r in sorted(exp, key=lambda r: (r["taxonId"], r["symbol"], r["goAspect"], r["goId"], r["reference"])):
        acc = r["geneProductId"].split(":")[1]
        key = (acc, r["goId"], r["goEvidence"], r["reference"], r["qualifier"])
        if key in seen:
            continue
        seen.add(key)
        out.append(f"exp {leaf_of[acc]} {acc} {r['symbol']} taxon:{r['taxonId']} {r['qualifier']} {r['goId']} "
                   f"{names.get(r['goId'], '?')} {r['goEvidence']} {r['reference']} {r['assignedBy']} {r['date']}")
    without = sorted(a for a in accessions if a not in {r["geneProductId"].split(":")[1] for r in exp})
    out.append(f"leaves with no manual experimental annotation (protein binding ignored): {len(without)} of {len(accessions)}")

    out += ["", "== IBA rows now in GOA for tree leaves, by source node =="]
    iba = Counter()
    for r in rows:
        if r["goEvidence"] == "IBA":
            ptn = [x["id"] for w in r["withFrom"] or [] for x in w["connectedXrefs"] if x["id"].startswith("PTN")]
            iba[(r["goId"], ",".join(ptn), r["date"])] += 1
    for (go, ptn, date), n in sorted(iba.items()):
        out.append(f"iba {go} {names.get(go, '?')} from {ptn} date {date}: {n} leaf annotations")
    for row in paint:
        if not any(go == row["go_id"] and row["node"] in ptn for go, ptn, _ in iba):
            out.append(f"iba none in GOA yet for PAINT row {row['node']} {row['go_id']} ({row['date']})")

    out += ["", "== experimental support per PAINT term (term or descendants, by term id) =="]
    for row in paint:
        hits = []
        for i in range(0, len(accessions), 30):
            hits += quickgo({"goId": row["go_id"], "goUsage": "descendants", "goUsageRelationships": "is_a,part_of",
                             "geneProductId": ",".join(f"UniProtKB:{a}" for a in accessions[i:i + 30])})
        hits = [h for h in hits if h["goEvidence"] in EXPERIMENTAL]
        seed_accs = {acc_of[x] for s in row["seeds"].split("|") for x in seed_leaves(s, nodes, below, root)}
        control = sorted({h["geneProductId"].split(":")[1] for h in hits} & seed_accs)
        if not control:
            raise SystemExit(f"positive control failed for {row['go_id']}: no seed returned by the query")
        out.append(f"{row['node']} {row['go_id']} {names.get(row['go_id'], '?')}: positive control ok "
                   f"(seeds returned: {','.join(control)}); seeds not returned: "
                   f"{','.join(sorted(seed_accs - set(control))) or 'none'}")
        for key in sorted({(h["geneProductId"].split(":")[1], h["symbol"], h["goId"], h["goEvidence"], h["reference"]) for h in hits}):
            inside = leaf_of[key[0]] in below[row["node"]]
            out.append(f"  {key[0]} {key[1]} {key[2]} {names.get(key[2], '?')} {key[3]} {key[4]} below_node={inside}")

    (HERE / f"{FAMILY}-tree-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
