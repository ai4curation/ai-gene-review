"""List candidate teleost-genome-duplication (TGD) paralogs for reviewed zebrafish genes.

For every gene directory under genes/DANRE/, query the Ensembl Compara REST API
for within-species paralogues whose duplication node is placed at a teleost
taxonomy level (Clupeocephala / Teleostei / Osteoglossocephalai). These are the
nodes Ensembl uses for duplications dating to the TGD, so the output is a
*candidate* list of TGD ohnolog partners, not a curated one: Compara node
placement is a gene-tree inference and should be cross-checked against
conserved synteny (e.g. via the spotted gar orthology bridge) before a pair is
treated as a TGD pair.

Usage (from repo root):
    uv run python projects/DANRE_DUPLICATION/scripts/tgd_paralogs.py \
        > projects/DANRE_DUPLICATION/reviewed_gene_tgd_paralogs.tsv
"""

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ENSEMBL = "https://rest.ensembl.org"
TELEOST_LEVELS = {"Clupeocephala", "Teleostei", "Osteoglossocephalai"}


def get(path: str) -> dict | None:
    url = f"{ENSEMBL}{path}{'&' if '?' in path else '?'}content-type=application/json"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                return None
            time.sleep(2**attempt)
        except urllib.error.URLError:
            time.sleep(2**attempt)
    return None


def symbol_for(gene_id: str, cache: dict[str, str]) -> str:
    if gene_id not in cache:
        rec = get(f"/lookup/id/{gene_id}")
        cache[gene_id] = (rec or {}).get("display_name", "")
    return cache[gene_id]


def main() -> None:
    gene_dirs = sorted(p.name for p in Path("genes/DANRE").iterdir() if p.is_dir())
    cache: dict[str, str] = {}
    print("reviewed_gene\tensembl_gene\tparalog_ensembl_gene\tparalog_symbol\ttaxonomy_level\tparalog_reviewed")
    for gene in gene_dirs:
        data = get(f"/homology/symbol/danio_rerio/{gene}?type=paralogues;format=condensed")
        if not data or not data.get("data"):
            print(f"{gene}\t\t\t\tNOT_FOUND\t")
            continue
        entry = data["data"][0]
        hits = [h for h in entry["homologies"] if h.get("taxonomy_level") in TELEOST_LEVELS]
        if not hits:
            print(f"{gene}\t{entry['id']}\t\t\tNONE\t")
        for h in hits:
            sym = symbol_for(h["id"], cache)
            reviewed = "yes" if sym in gene_dirs else "no"
            print(f"{gene}\t{entry['id']}\t{h['id']}\t{sym}\t{h['taxonomy_level']}\t{reviewed}")
        time.sleep(0.1)


if __name__ == "__main__":
    sys.exit(main())
