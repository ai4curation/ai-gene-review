# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Fetch PANTHER 19 trees (treeinfo API) for PTHR47593 and PTHR45730 and report:
(1) the root-to-leaf path of each soybean leaf in PTHR47593 (event types, taxa, subfamily
boundaries); (2) which tree contains the PAINT nodes listed in
interpro/panther/PTHR47593/PTHR47593-paint.tsv (PTN008158895, PTN009184003);
(3) which tree contains Arabidopsis ZFP7 (Q39266) and ZFP4 (Q39263); (4) the species
codes of leaves in PTHR47593. Trees are cached as JSON beside this script."""
import json
import os
import requests

FAMS = ["PTHR47593", "PTHR45730"]
PTNS = ["PTN008158895", "PTN009184003"]
PROBES = ["Q39266", "Q39263", "C6T1A2"]


def load(fam: str) -> dict:
    fn = f"panther19_tree_{fam}.json"
    if not os.path.exists(fn):
        r = requests.get(
            "https://pantherdb.org/services/oai/pantherdb/treeinfo",
            params={"family": fam},
            timeout=300,
        )
        r.raise_for_status()
        open(fn, "w").write(r.text)
    return json.load(open(fn))


def kids(n: dict) -> list:
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def walk(n: dict, path: list, out: list) -> None:
    p = path + [n]
    if not kids(n):
        out.append(p)
    for k in kids(n):
        walk(k, p, out)


def main() -> None:
    for fam in FAMS:
        d = load(fam)
        root = d["search"]["tree_topology"]["annotation_node"]
        paths: list = []
        walk(root, [], paths)
        ids = {n.get("persistent_id") for p in paths for n in p}
        names = [p[-1].get("node_name", "") for p in paths]
        print(f"## {fam}: {len(paths)} leaves (PANTHER version {d['search']['product']['version']})")
        for t in PTNS:
            print(f"  PAINT node {t} present: {t in ids}")
        for pr in PROBES:
            hits = [nm for nm in names if f"UniProtKB={pr}" in nm]
            print(f"  leaf {pr} present: {bool(hits)}")
        codes = sorted({nm.split('|')[0] for nm in names})
        print(f"  species codes: {','.join(codes)}")
        if fam == "PTHR47593":
            for p in paths:
                leaf = p[-1]
                if leaf.get("node_name", "").startswith("SOYBN"):
                    steps = " > ".join(
                        f"{n.get('persistent_id')}[{n.get('event_type') or 'LEAF'}|{n.get('species') or ''}|{n.get('sf_id') or ''}]"
                        for n in p
                    )
                    print(f"  {leaf['node_name']} ({leaf.get('prop_sf_id')}): {steps}")


if __name__ == "__main__":
    main()
