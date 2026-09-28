"""Draw a reproducible random sample of PANTHER TGD pairs for review.

Sampling frame: every 1:1 pair in panther_tgd_pairs.tsv whose tgd_call is
TGD_tree (duplication placed on Neopterygii|Teleostei). The frame is shuffled
with a fixed seed and pairs are taken in that order. A drawn pair is skipped,
and the skip is recorded, only if either gene has no GOA annotation on any of
its UniProt accessions (nothing to review). Unnamed genes (si:, zgc:, LOC...)
are NOT excluded, so the sample is not biased toward well-studied genes.

For each accepted gene the script also picks the UniProt accession holding the
most experimental GOA rows (then most rows overall), using the same helpers as
accession_audit.py, and reports rows that exist only on other accessions.

Usage (from repo root):
    uv run python projects/DANRE_DUPLICATION/scripts/sample_pairs.py --n 8 --seed 20260928 \
        > projects/DANRE_DUPLICATION/batch3_sample.tsv
"""

import argparse
import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from accession_audit import EXPERIMENTAL, annotations, key  # noqa: E402

PAIRS = Path("projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv")


def best_accession(primary: str) -> tuple[str, int, int, int]:
    """Best accession for the gene behind a PANTHER UniProt accession.

    Candidates are that accession plus every UniProt entry sharing its ZFIN gene
    cross-reference. Returns (accession, experimental rows, all rows, experimental
    or IBA rows present only on other candidates).
    """
    import json
    import urllib.parse
    import urllib.request

    q = urllib.parse.urlencode({"query": f"accession:{primary}", "fields": "gene_names,xref_zfin",
                                "format": "json"})
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/search?{q}", timeout=60) as r:
        res = json.load(r)["results"]
    zfin = [x["id"] for x in (res[0].get("uniProtKBCrossReferences", []) if res else []) if x["database"] == "ZFIN"]
    candidates = {primary}
    for z in zfin:
        q = urllib.parse.urlencode({"query": f"xref:zfin-{z} AND organism_id:7955", "fields": "accession",
                                    "format": "json", "size": 100})
        with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/search?{q}", timeout=60) as r:
            candidates |= {x["primaryAccession"] for x in json.load(r)["results"]}
    scored = []
    union: set = set()
    for acc in sorted(candidates):
        anns = annotations(acc)
        keys = {key(a) for a in anns}
        union |= keys
        scored.append((sum(a["goEvidence"] in EXPERIMENTAL for a in anns), len(anns), acc, keys))
    scored.sort(key=lambda s: (-s[0], -s[1], s[2]))
    n_exp, n_all, acc, keys = scored[0]
    elsewhere = sum(1 for k in union - keys if k[1] in EXPERIMENTAL or k[1] == "IBA")
    return acc, n_exp, n_all, elsewhere


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--seed", type=int, default=20260928)
    args = ap.parse_args()

    frame = [r for r in csv.DictReader(PAIRS.open(), delimiter="\t")
             if r["tgd_call"] == "TGD_tree" and r["pair_class"] == "1:1"]
    frame.sort(key=lambda r: (r["uniprot_a"], r["uniprot_b"]))
    random.Random(args.seed).shuffle(frame)

    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["draw", "status", "family", "family_name", "gene_a", "gene_b",
                  "accession_a", "exp_a", "goa_a", "missing_elsewhere_a",
                  "accession_b", "exp_b", "goa_b", "missing_elsewhere_b",
                  "human_orthologs_a", "human_orthologs_b"])
    accepted = 0
    for i, r in enumerate(frame, start=1):
        a = best_accession(r["uniprot_a"])
        b = best_accession(r["uniprot_b"])
        status = "accepted" if a[2] and b[2] else "skipped_no_goa"
        if status == "accepted":
            accepted += 1
        out.writerow([i, status, r["family"], r["family_name"], r["gene_a"], r["gene_b"],
                      *a, *b, r["human_orthologs_a"], r["human_orthologs_b"]])
        if accepted >= args.n:
            break
    print(f"# frame size {len(frame)}; seed {args.seed}; accepted {accepted}", file=sys.stderr)


if __name__ == "__main__":
    main()
