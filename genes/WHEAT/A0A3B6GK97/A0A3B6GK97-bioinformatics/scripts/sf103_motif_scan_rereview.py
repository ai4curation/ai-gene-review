"""Scan PANTHER subfamily members (UniProt) in a taxon for patatin catalytic motifs.

Usage: uv run python scripts/sf103_motif_scan_rereview.py --subfamily PTHR32176:SF103 \
           --taxon 147389 --out results_rereview/sf103_triticeae_motifs.tsv
"""

import argparse
import re

import requests

URL = "https://rest.uniprot.org/uniprotkb/search"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--subfamily", required=True)
    p.add_argument("--taxon", required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    r = requests.get(
        URL,
        params={
            "query": f'"{a.subfamily}" AND taxonomy_id:{a.taxon}',
            "format": "fasta",
            "size": 500,
        },
        timeout=120,
    )
    r.raise_for_status()
    rows = ["accession\torganism\tlength\tser_elbow_GxSxG\toxyanion_DGGG"]
    for rec in r.text.split(">")[1:]:
        head, *body = rec.split("\n")
        seq = "".join(body)
        org = re.search(r"OS=(.+?) OX=", head).group(1)
        elbow = ",".join(f"{m.start() + 1}:{m.group()}" for m in re.finditer("G.S.G", seq)) or "none"
        oxy = ",".join(f"{m.start() + 1}" for m in re.finditer("DGGG", seq)) or "none"
        rows.append(f"{head.split('|')[1]}\t{org}\t{len(seq)}\t{elbow}\t{oxy}")
    open(a.out, "w").write("\n".join(rows) + "\n")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
