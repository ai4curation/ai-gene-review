#!/usr/bin/env python3
"""Place PTHR10977 members on the PANTHER family tree and report PAINT node ancestry.

Fetches the live PANTHER tree for a family (pantherdb.org treeinfo service) and,
for each query UniProt accession, reports either its ancestor path (if the
accession is a leaf of the PANTHER reference tree) or, if it is not a leaf, the
UniRef50 cluster it belongs to and any tree leaves that share that cluster
(UniProt REST). It then reports whether each placed protein descends from a
given PAINT node.

Only the standard library is used. Nothing is cached or hard-coded: every
result is computed from the two web services at run time.

Usage:
    python3 -I panther_tree_placement.py PTHR10977 PTN000104601 D4GXZ3 Q6KZB1 Q9HJS1 Q97UL5
"""
import json
import sys
import urllib.parse
import urllib.request

TREE_URL = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={fam}"
UNIREF_URL = "https://rest.uniprot.org/uniref/search?"
HEADERS = {"User-Agent": "python-urllib/panther-tree-placement"}


def _open(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=120)


def get_json(url):
    with _open(url) as r:
        return json.load(r)


def get_text(url):
    with _open(url) as r:
        return r.read().decode()


def kids(node):
    c = node.get("children")
    if not c:
        return []
    a = c.get("annotation_node")
    if isinstance(a, dict):
        return [a]
    return a or []


def leaf_acc(node):
    name = node.get("node_name") or ""
    return name.split("UniProtKB=")[-1] if "UniProtKB=" in name else None


def index_tree(root):
    """Return {accession: (leaf_node, [ancestor nodes root->leaf])}."""
    out = {}

    def walk(n, path):
        p = path + [n]
        if not kids(n):
            acc = leaf_acc(n)
            if acc:
                out[acc] = (n, p)
        for k in kids(n):
            walk(k, p)

    walk(root, [])
    return out


def uniref50(acc):
    q = urllib.parse.urlencode(
        {"query": f"uniprot_id:{acc} AND identity:0.5", "fields": "id,count", "format": "tsv"}
    )
    lines = get_text(UNIREF_URL + q).strip().splitlines()
    return lines[1].split("\t")[0] if len(lines) > 1 else None


def uniref_members(cluster_id):
    url = f"https://rest.uniprot.org/uniref/{cluster_id}/members?format=json&size=500"
    accs = set()
    while url:
        with _open(url) as r:
            d = json.load(r)
            link = r.headers.get("Link")
        for m in d.get("results", []):
            for a in m.get("accessions", []) or []:
                accs.add(a)
            if m.get("memberId"):
                accs.add(m["memberId"])
        url = None
        if link and 'rel="next"' in link:
            url = link.split(";")[0].strip("<> ")
    return accs


def describe(n):
    return (
        f"{n.get('persistent_id')} [{n.get('species') or n.get('taxonomic_range') or '-'}; "
        f"{n.get('event_type') or n.get('tree_node_type')}]"
    )


def main():
    fam, paint_node, *queries = sys.argv[1:]
    d = get_json(TREE_URL.format(fam=fam))
    print(f"PANTHER product: {d['search']['product']}")
    root = d["search"]["tree_topology"]["annotation_node"]
    idx = index_tree(root)
    print(f"Tree leaves with UniProt accession: {len(idx)}")
    for q in queries:
        print(f"\n== {q}")
        placed = []
        if q in idx:
            placed.append((q, "query is a tree leaf"))
        else:
            cl = uniref50(q)
            print(f"   not a leaf of the {fam} reference tree; UniRef50 cluster: {cl}")
            if cl:
                mates = sorted(uniref_members(cl) & set(idx))
                print(f"   tree leaves in the same UniRef50 cluster: {mates or 'none'}")
                placed += [(m, f"UniRef50 cluster-mate of {q}") for m in mates]
        for acc, why in placed:
            leaf, path = idx[acc]
            ids = [n.get("persistent_id") for n in path]
            print(f"   {acc} ({leaf.get('organism')}; {leaf.get('definition')}) - {why}")
            print("   path: " + " > ".join(describe(n) for n in path))
            print(f"   descends from {paint_node}: {paint_node in ids}")
            parent = path[-2] if len(path) > 1 else None
            if parent is not None:
                sibs = []

                def collect(n):
                    if not kids(n):
                        sibs.append(f"{leaf_acc(n)} ({n.get('organism')}; {n.get('definition')})")
                    for k in kids(n):
                        collect(k)

                collect(parent)
                if len(sibs) <= 6:
                    print(f"   leaves under parent {parent.get('persistent_id')}: " + "; ".join(sibs))
                else:
                    print(f"   leaves under parent {parent.get('persistent_id')}: {len(sibs)}")


if __name__ == "__main__":
    main()
