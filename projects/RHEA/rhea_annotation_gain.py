#!/usr/bin/env python3
"""Estimate the annotation gain from the curated RHEA->GO mappings.

For every GO-bearing mapping in rhea2go.sssom.yaml (exactMatch / broadMatch;
sssom:NoTermFound rows are skipped), ask UniProtKB how many entries carry the
RHEA reaction but do NOT already have the mapped GO term -- i.e. how many GO
molecular-function annotations would be *gained* if the mapping were added to
rhea2go and propagated.

Counts use the UniProtKB REST search `x-total-results` header (no records
fetched). Note: UniProt's `go:<id>` query is **closure-aware** (matches the term
and its descendants), so `with-go` already excludes entries that carry a more
specific child -- the gain is a closure-filtered estimate, not a naive
exact-match one.

  gain = N(rhea) - N(rhea AND go)

**Gain is measured from Swiss-Prot (reviewed) by default** -- the curation-
relevant, trustworthy number. The all-of-UniProtKB figure (mostly TrEMBL,
inheriting the reliability of automated RHEA annotations) is reported as
secondary context.

Usage:
    uv run python rhea_annotation_gain.py [--sssom rhea2go.sssom.yaml] [--reviewed-only]
"""
from __future__ import annotations

import argparse
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

SEARCH = "https://rest.uniprot.org/uniprotkb/search"


def count(query: str, timeout: int = 40) -> int | None:
    params = urllib.parse.urlencode({"query": query, "size": 0})
    req = urllib.request.Request(
        f"{SEARCH}?{params}", headers={"User-Agent": "ai-gene-review-rhea/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            val = resp.headers.get("x-total-results")
            return int(val) if val is not None else None
    except Exception:
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sssom", type=Path, default=Path(__file__).with_name("rhea2go.sssom.yaml"))
    ap.add_argument("--reviewed-only", action="store_true", help="only the Swiss-Prot subset")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args(argv)

    doc = yaml.safe_load(args.sssom.read_text())
    pairs = [
        (m["subject_id"].split(":")[1], m["object_id"], m["object_label"], m["predicate_id"])
        for m in doc.get("mappings", [])
        if str(m.get("object_id", "")).startswith("GO:")
    ]

    print("rhea\tgo\tpredicate\tN_rhea\tN_with_go\tgain\tN_rhea_rev\tN_with_go_rev\tgain_rev\tlabel")
    tot = tot_rev = 0
    nonzero = 0
    for rhea, go, label, pred in pairs:
        goid = go.split(":")[1]
        n_all = count(f"rhea:{rhea}")
        n_all_go = count(f"rhea:{rhea} AND go:{goid}")
        n_rev = count(f"rhea:{rhea} AND reviewed:true")
        n_rev_go = count(f"rhea:{rhea} AND go:{goid} AND reviewed:true")
        gain = (n_all - n_all_go) if (n_all is not None and n_all_go is not None) else None
        gain_rev = (n_rev - n_rev_go) if (n_rev is not None and n_rev_go is not None) else None
        if gain:
            tot += gain
            nonzero += 1
        if gain_rev:
            tot_rev += gain_rev
        pl = "exact" if pred.endswith("exactMatch") else "broad"
        print(f"{rhea}\t{go}\t{pl}\t{n_all}\t{n_all_go}\t{gain}\t{n_rev}\t{n_rev_go}\t{gain_rev}\t{label}")
        time.sleep(args.sleep)

    print(f"\n# mappings scored: {len(pairs)}  (non-zero all-UniProt gain: {nonzero})")
    print(f"# TOTAL new annotations, Swiss-Prot (reviewed) [PRIMARY]: {tot_rev}")
    print(f"# TOTAL new annotations, all UniProtKB (secondary/TrEMBL): {tot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
