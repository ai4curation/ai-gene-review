#!/usr/bin/env python3
"""Summarise FlyBase gene groups and their overlap with DROME gene reviews.

Downloads the FlyBase precomputed gene-group report (if not already cached),
then writes a YAML summary of:

* overall group statistics (counts, size distribution, top-level roots);
* coverage of each terminal group by existing reviews in ``genes/DROME``;
* GO annotations (from QuickGO) for every member of the groups named with
  ``--detail``, plus the fly genes outside the group that carry the same
  MF/BP terms, so a group can be compared against its GO footprint.

Nothing is hardcoded: every number in the output is computed from the
downloaded files at run time.

Usage (from the repository root)::

    uv run python projects/FLYBASE_GENE_GROUPS/fb_gene_groups.py \
        --release fb_2026_03 --detail GLUE \
        -o projects/FLYBASE_GENE_GROUPS/fb_gene_groups_summary.yaml
"""

from __future__ import annotations

import argparse
import collections
import csv
import gzip
import io
import json
import statistics
import urllib.request
from pathlib import Path

import yaml

FB_URL = (
    "https://s3ftp.flybase.org/releases/{dir}/precomputed_files/genes/"
    "gene_group_data_{release}.tsv.gz"
)
UNIPROT_URL = (
    "https://rest.uniprot.org/uniprotkb/search?query=organism_id:7227+AND+"
    "reviewed:{reviewed}+AND+gene_exact:{symbol}&fields=accession&format=tsv&size=1"
)
QUICKGO_URL = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?"
    "geneProductId={acc}&downloadLimit=1000"
)
QUICKGO_TERM_URL = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?"
    "goId={go}&taxonId=7227&goUsage=descendants&downloadLimit=50000"
)


def fb_url(release: str) -> str:
    # files are named fb_2026_03 but live under the FB2026_03 release directory
    return FB_URL.format(dir=release.replace("fb_", "FB"), release=release)


def fetch(url: str, accept: str | None = None) -> bytes:
    req = urllib.request.Request(url, headers={"Accept": accept} if accept else {})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def load_groups(path: Path):
    groups: dict[str, dict] = {}
    members: dict[str, set[str]] = collections.defaultdict(set)
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            cols = (line.rstrip("\n").split("\t") + [""] * 7)[:7]
            gid, sym, name, pid, _psym, _fbgn, gene = cols
            groups[gid] = {"symbol": sym, "name": name, "parent": pid or None}
            if gene:
                members[gid].add(gene)
    return groups, members


def root_of(gid: str, groups: dict) -> str:
    while groups[gid]["parent"] and groups[gid]["parent"] in groups:
        gid = groups[gid]["parent"]
    return gid


def uniprot_accession(symbol: str) -> str | None:
    """Swiss-Prot accession if one exists, else the first TrEMBL hit."""
    for reviewed in ("true", "false"):
        rows = fetch(UNIPROT_URL.format(reviewed=reviewed, symbol=symbol)).decode().splitlines()
        if len(rows) > 1:
            return rows[1].strip()
    return None


def go_labels(ids: set[str]) -> dict[str, str]:
    if not ids:
        return {}
    url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + ",".join(sorted(ids))
    data = json.loads(fetch(url, accept="application/json"))
    return {t["id"]: t["name"] for t in data["results"]}


def quickgo_rows(url: str) -> list[dict]:
    text = fetch(url, accept="text/tsv").decode()
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--release", default="fb_2026_03")
    ap.add_argument("--cache", type=Path, default=Path(".cache/flybase"))
    ap.add_argument("--genes-dir", type=Path, default=Path("genes/DROME"))
    ap.add_argument("--detail", nargs="*", default=[], help="group symbols to expand with GO")
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args()

    args.cache.mkdir(parents=True, exist_ok=True)
    tsv = args.cache / f"gene_group_data_{args.release}.tsv.gz"
    if not tsv.exists():
        tsv.write_bytes(fetch(fb_url(args.release)))
    groups, members = load_groups(tsv)
    reviewed = {p.name for p in args.genes_dir.iterdir() if p.is_dir()}

    all_genes = set().union(*members.values())
    sizes = [len(m) for m in members.values()]
    roots = collections.Counter(root_of(g, groups) for g in members)

    coverage = []
    for gid, mem in members.items():
        hit = sorted(mem & reviewed)
        if hit:
            coverage.append({
                "id": gid, "symbol": groups[gid]["symbol"], "name": groups[gid]["name"],
                "n_members": len(mem), "n_reviewed": len(hit), "reviewed": hit,
            })
    coverage.sort(key=lambda c: (-c["n_reviewed"] / c["n_members"], -c["n_reviewed"]))

    summary = {
        "source": fb_url(args.release),
        "release": args.release,
        "n_groups": len(groups),
        "n_terminal_groups_with_members": len(members),
        "n_member_genes": len(all_genes),
        "group_size": {
            "median": statistics.median(sizes), "max": max(sizes),
            "n_groups_le_10_members": sum(s <= 10 for s in sizes),
        },
        "n_groups_named_complex": sum("COMPLEX" in groups[g]["name"] for g in members),
        "n_groups_named_unclassified": sum("UNCLASSIFIED" in groups[g]["name"] for g in members),
        "top_level_roots": [
            {"id": r, "symbol": groups[r]["symbol"], "name": groups[r]["name"], "n_terminal_groups": n}
            for r, n in roots.most_common(15)
        ],
        "drome_reviews": {
            "n_reviewed_genes": len(reviewed),
            "n_reviewed_in_any_group": len(reviewed & all_genes),
            "n_groups_with_any_review": len(coverage),
            "n_groups_fully_reviewed": sum(c["n_reviewed"] == c["n_members"] for c in coverage),
        },
        "group_coverage": coverage,
        "group_detail": [],
    }

    by_symbol = {v["symbol"]: k for k, v in groups.items()}
    for sym in args.detail:
        gid = by_symbol[sym]
        detail = {"id": gid, "symbol": sym, "name": groups[gid]["name"], "members": [], "go_footprint": {}}
        go_ids: set[str] = set()
        mf_bp: set[str] = set()
        for gene in sorted(members[gid]):
            acc = uniprot_accession(gene)
            annots = []
            if acc:
                for r in quickgo_rows(QUICKGO_URL.format(acc=acc)):
                    go_ids.add(r["GO TERM"])
                    if r["GO ASPECT"] != "C":
                        mf_bp.add(r["GO TERM"])
                    annots.append({
                        "qualifier": r["QUALIFIER"], "term": r["GO TERM"],
                        "evidence": r["GO EVIDENCE CODE"], "reference": r["REFERENCE"],
                        "with_from": r["WITH/FROM"] or None,
                    })
            detail["members"].append({
                "symbol": gene, "uniprot": acc, "reviewed_in_repo": gene in reviewed,
                "go_annotations": annots,
            })
        labels = go_labels(go_ids)
        for m in detail["members"]:
            for a in m["go_annotations"]:
                a["label"] = labels.get(a["term"])
        # Which fly genes carry the group's MF/BP terms but are not group members?
        # Component terms are skipped: they are usually too broad to be informative.
        for go in sorted(mf_bp):
            carriers = sorted({r["SYMBOL"] for r in quickgo_rows(QUICKGO_TERM_URL.format(go=go))})
            detail["go_footprint"][go] = {
                "label": labels.get(go),
                "fly_genes_annotated": carriers,
                "not_in_group": sorted(set(carriers) - members[gid]),
            }
        summary["group_detail"].append(detail)

    args.output.write_text(yaml.safe_dump(summary, sort_keys=False, width=100))
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
