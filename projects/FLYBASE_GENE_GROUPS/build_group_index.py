#!/usr/bin/env python3
"""Build a YAML index of every FlyBase gene group with UniProt-mapped members.

Covers the three FlyBase group reports (gene groups, metabolic pathway groups
and signaling pathway groups) for one release. For each group the index records
its parent(s), children, direct members and all members of its subtree. Each
member gene is mapped to a UniProtKB accession: the Swiss-Prot entry carrying
the FlyBase cross-reference when there is one, otherwise the longest TrEMBL
entry from the D. melanogaster reference proteome.

The index is the input to ``triage_groups.py`` and to module generation.

Usage (from the repository root)::

    uv run python projects/FLYBASE_GENE_GROUPS/build_group_index.py \
        -o projects/FLYBASE_GENE_GROUPS/group_index.yaml
"""

from __future__ import annotations

import argparse
import collections
import gzip
import urllib.request
from pathlib import Path

import yaml

BASE = "https://s3ftp.flybase.org/releases/{dir}/precomputed_files/genes/{name}_{release}.tsv.gz"
SOURCES = {
    "gene_group": "gene_group_data",
    "metabolic_pathway": "metabolic_pathway_group_data",
    "signaling_pathway": "signaling_pathway_group_data",
}
UNIPROT = (
    "https://rest.uniprot.org/uniprotkb/stream?query=organism_id:7227+AND+"
    "(reviewed:true+OR+proteome:UP000000803)&fields=accession,reviewed,"
    "gene_primary,protein_name,xref_flybase,length&format=tsv"
)


def cached(url: str, path: Path) -> Path:
    if not path.exists():
        with urllib.request.urlopen(url, timeout=600) as resp:
            path.write_bytes(resp.read())
    return path


def read_groups(path: Path):
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            yield (line.rstrip("\n").split("\t") + [""] * 7)[:7]


def load_uniprot(path: Path) -> dict[str, dict]:
    """FBgn -> best UniProt entry (Swiss-Prot first, then longest TrEMBL)."""
    best: dict[str, dict] = {}
    with open(path) as fh:
        next(fh)
        for line in fh:
            acc, reviewed, gene, name, fb, length = line.rstrip("\n").split("\t")
            entry = {
                "accession": acc,
                "reviewed": reviewed == "reviewed",
                "protein_name": name.split(" (")[0],
                "length": int(length or 0),
            }
            for fbgn in filter(None, fb.split(";")):
                cur = best.get(fbgn)
                key = (entry["reviewed"], entry["length"])
                if cur is None or key > (cur["reviewed"], cur["length"]):
                    best[fbgn] = entry
    return best


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--release", default="fb_2026_03")
    ap.add_argument("--cache", type=Path, default=Path(".cache/flybase"))
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    rdir = args.release.replace("fb_", "FB")

    uniprot = load_uniprot(cached(UNIPROT, args.cache / "uniprot_dmel.tsv"))

    groups: dict[str, dict] = {}
    for source, name in SOURCES.items():
        fname = f"{name}_{args.release}.tsv.gz"
        path = cached(BASE.format(dir=rdir, name=name, release=args.release), args.cache / fname)
        for gid, sym, gname, pid, _psym, fbgn, gsym in read_groups(path):
            g = groups.setdefault(gid, {
                "id": gid, "symbol": sym, "name": gname, "sources": [],
                "parents": [], "children": [], "members": {},
            })
            if source not in g["sources"]:
                g["sources"].append(source)
            if pid and pid not in g["parents"]:
                g["parents"].append(pid)
            if fbgn:
                g["members"][fbgn] = gsym
    for gid, g in groups.items():
        for pid in g["parents"]:
            if pid in groups and gid not in groups[pid]["children"]:
                groups[pid]["children"].append(gid)

    memo: dict[str, set[str]] = {}

    def subtree(gid: str) -> set[str]:
        if gid not in memo:
            memo[gid] = set(groups[gid]["members"]).union(
                *[subtree(c) for c in groups[gid]["children"]])
        return memo[gid]

    genes: dict[str, dict] = {}
    out = []
    for gid in sorted(groups):
        g = groups[gid]
        for fbgn in subtree(gid):
            if fbgn not in genes:
                sym = next(x["members"][fbgn] for x in groups.values() if fbgn in x["members"])
                up = uniprot.get(fbgn)
                genes[fbgn] = {
                    "symbol": sym,
                    "uniprot": up["accession"] if up else None,
                    "swissprot": up["reviewed"] if up else False,
                    "protein_name": up["protein_name"] if up else None,
                }
        out.append({
            "id": gid,
            "symbol": g["symbol"],
            "name": g["name"],
            "sources": g["sources"],
            "parents": sorted(g["parents"]),
            "children": sorted(g["children"]),
            "direct_members": sorted(g["members"]),
            "n_subtree_members": len(subtree(gid)),
        })
    doc = {
        "release": args.release,
        "n_groups": len(out),
        "groups": out,
        "genes": dict(sorted(genes.items())),
    }
    args.output.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
    print(f"wrote {args.output}: {len(out)} groups, {len(genes)} genes")


if __name__ == "__main__":
    main()
