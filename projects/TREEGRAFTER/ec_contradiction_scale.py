#!/usr/bin/env python3
"""How far does each corpus EC contradiction reach across UniProtKB?

``propagation_rules.py`` flags reviewed TreeGrafter MF annotations whose GO EC
cross-reference contradicts the protein's own UniProt EC number
(``ec_contradiction``). This script takes each distinct (UniProt EC, GO term)
pair behind those hits and asks UniProt and QuickGO how common the same
pairing is outside the review corpus:

  with_term          UniProtKB entries with that EC number that also carry the
                     GO term (any evidence; UniProt's own ``go:`` search)
  with_term_reviewed the same, Swiss-Prot only
  contradicted       with_term minus entries that also carry the GO term's own
                     EC number (fused or multifunctional proteins, for which
                     the term may be right); the number to read
  ec_total           all UniProtKB entries with that EC number
  sample, sample_sources
                     up to 40 accessions drawn (fixed seed) from the first 500
                     ``contradicted`` hits, and the GOA references behind the GO
                     term on each, from QuickGO; GO_REF:0000118 is
                     TreeGrafter, GO_REF:0000120 the merged multi-pipeline call

Only fully specified UniProt EC numbers are queried; a pair whose protein has
a partial EC (``2.3.1.-``) is skipped. Needs network access.

Run (after propagation_rules.py):
  python3 projects/TREEGRAFTER/ec_contradiction_scale.py
"""
from __future__ import annotations

import csv
import json
import os
import random
import re
import time
import urllib.parse
import urllib.request
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
HITS = os.path.join(HERE, "propagation_rule_hits.tsv")
OUT = os.path.join(HERE, "ec_contradiction_scale.tsv")
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
FULL_EC = re.compile(r"^\d+\.\d+\.\d+\.\d+$")


def _get(url: str, head: bool = False):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, method="HEAD" if head else "GET")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.headers if head else resp.read().decode()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def uniprot_count(query: str) -> int:
    url = f"{UNIPROT}?{urllib.parse.urlencode({'query': query, 'size': 1})}"
    return int(_get(url, head=True).get("x-total-results", 0))


def uniprot_accessions(query: str, n: int = 500) -> list[str]:
    url = f"{UNIPROT}?{urllib.parse.urlencode({'query': query, 'fields': 'accession', 'format': 'list', 'size': n})}"
    return _get(url).split()


def quickgo_sources(accs: list[str], go_id: str) -> Counter:
    c = Counter()
    for i in range(0, len(accs), 20):
        chunk = accs[i:i + 20]
        params = {"geneProductId": ",".join(chunk), "goId": go_id,
                  "goUsage": "exact", "limit": 100}
        d = json.loads(_get(f"{QUICKGO}?{urllib.parse.urlencode(params)}"))
        per: dict = {}
        for r in d.get("results", []):
            per.setdefault(r["geneProductId"].split(":", 1)[1], set()).add(r["reference"])
        for a in chunk:
            c["+".join(sorted(per.get(a, ()))) or "absent"] += 1
    return c


def main() -> None:
    pairs: dict = {}
    for h in csv.DictReader(open(HITS), delimiter="\t"):
        if h["rule"] != "ec_contradiction":
            continue
        go_part, uni_part = h["detail"].split(" vs UniProt ", 1)
        go_ecs = [e for e in go_part[3:].split(",") if FULL_EC.match(e)]
        uni = uni_part.split(",")
        for ec in uni:
            if FULL_EC.match(ec):
                key = (ec, h["term_id"])
                p = pairs.setdefault(key, {"label": h["term_label"], "genes": set(),
                                           "actions": Counter(), "go_ecs": go_ecs})
                p["genes"].add(f"{h['species']}/{h['gene']}")
                p["actions"][h["action"]] += 1
    rows = []
    for (ec, go_id), p in sorted(pairs.items()):
        q = f"(ec:{ec}) AND (go:{go_id.split(':')[1]})"
        with_term = uniprot_count(q)
        reviewed = uniprot_count(f"{q} AND (reviewed:true)")
        excl = "".join(f" NOT (ec:{e})" for e in p["go_ecs"])
        contradicted = uniprot_count(q + excl) if excl else with_term
        ec_total = uniprot_count(f"(ec:{ec})")
        sources = Counter()
        sample = 0
        if with_term:
            accs = uniprot_accessions(q + excl) or uniprot_accessions(q)
            random.seed(0)
            samp = random.sample(accs, min(40, len(accs)))
            sample = len(samp)
            sources = quickgo_sources(samp, go_id)
        rows.append({
            "uniprot_ec": ec, "go_term": go_id, "go_label": p["label"],
            "corpus_genes": ";".join(sorted(p["genes"])),
            "corpus_actions": ";".join(f"{k}:{v}" for k, v in sorted(p["actions"].items())),
            "with_term": with_term, "with_term_reviewed": reviewed,
            "contradicted": contradicted, "ec_total": ec_total,
            "pct_of_ec": f"{100 * contradicted / ec_total:.1f}" if ec_total else "",
            "sample": sample,
            "sample_sources": ";".join(f"{k}:{v}" for k, v in sources.most_common()),
        })
        print(ec, go_id, with_term, contradicted, ec_total, dict(sources))
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {OUT} ({len(rows)} pairs)")


if __name__ == "__main__":
    main()
