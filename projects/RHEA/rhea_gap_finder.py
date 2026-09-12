#!/usr/bin/env python3
"""Find Swiss-Prot enzymes whose RHEA reaction has no rhea2go mapping AND whose
GO molecular function is missing or only high-level.

This is the candidate-selection step behind RHEA-GAP-CASES.md, made reproducible
so the cases are not hand-picked. Pipeline (all live, nothing hardcoded):

1. Stream reviewed (Swiss-Prot) enzymes for an organism that have a catalytic
   activity (UniProt REST ``stream``), pulling EC, GO ids, and the
   ``cc_catalytic_activity`` text (which carries the ``Rhea:RHEA-nnnnn`` xrefs).
2. Keep entries where *every* annotated RHEA reaction is absent from ``rhea2go``
   (so the specific activity cannot have propagated via the RHEA pipeline), and
   that carry a complete EC number (real catalysis, excludes most transporters).
3. Look up the GO aspect of each entry's GO ids (QuickGO) and flag entries whose
   molecular-function terms are absent or fall entirely inside a high-level /
   enzyme-class blocklist -- i.e. the GO MF is missing or ultra-high-level.

Usage:
    uv run python rhea_gap_finder.py --organism 9606 --limit 40

Note: "MF only in blocklist" is a heuristic for "high-level"; confirm each hit by
reading the actual terms (the script prints them). Closure-aware depth scoring
would be stronger but needs the GO graph; this is deliberately a triage filter.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
UNIPROT_STREAM = "https://rest.uniprot.org/uniprotkb/stream"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"

# High-level molecular-function terms: enzyme-class roots and near-root nodes.
# An entry whose only MF terms are in here has effectively no specific activity.
HIGH_LEVEL_MF = {
    "GO:0003674",  # molecular_function
    "GO:0003824",  # catalytic activity
    "GO:0016491",  # oxidoreductase activity
    "GO:0016740",  # transferase activity
    "GO:0016787",  # hydrolase activity
    "GO:0016829",  # lyase activity
    "GO:0016853",  # isomerase activity
    "GO:0016874",  # ligase activity
    "GO:0140657",  # ATP-dependent activity
    "GO:0005488",  # binding
    "GO:0016788",  # hydrolase activity, acting on ester bonds
    "GO:0016772",  # transferase activity, transferring P-containing groups
    "GO:0016741",  # transferase activity, transferring one-carbon groups
    "GO:0016301",  # kinase activity
    "GO:0008146",  # sulfotransferase activity
    "GO:0016746",  # acyltransferase activity
    "GO:0016757",  # glycosyltransferase activity
}


def _get(url: str, accept: str | None = None, timeout: int = 120) -> str:
    headers = {"User-Agent": "ai-gene-review-rhea/1.0"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode()


def load_unmapped_predicate():
    mapped = set()
    for line in _get(RHEA2GO_URL).splitlines():
        m = re.match(r"RHEA:(\d+) ", line)
        if m:
            mapped.add(m.group(1))
    return lambda rid: rid not in mapped


def stream_enzymes(organism: str):
    q = f"reviewed:true AND organism_id:{organism} AND cc_catalytic_activity:*"
    params = urllib.parse.urlencode(
        {
            "query": q,
            "format": "tsv",
            "fields": "accession,gene_primary,protein_name,ec,go_id,cc_catalytic_activity",
        }
    )
    text = _get(f"{UNIPROT_STREAM}?{params}")
    rows = [r.split("\t") for r in text.splitlines()[1:]]
    return [r for r in rows if len(r) >= 6]


def go_aspects(go_ids):
    info = {}
    ids = sorted(go_ids)
    for i in range(0, len(ids), 50):
        batch = ids[i : i + 50]
        try:
            res = json.loads(_get(QUICKGO + ",".join(batch), accept="application/json"))
            for t in res.get("results", []):
                info[t["id"]] = (t.get("aspect"), t.get("name"))
        except Exception:
            pass
        time.sleep(0.3)
    return info


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--organism", default="9606", help="NCBI taxon id (default human)")
    ap.add_argument("--limit", type=int, default=40, help="max hits to print")
    args = ap.parse_args(argv)

    is_unmapped = load_unmapped_predicate()
    rows = stream_enzymes(args.organism)
    cands = []
    for acc, gene, name, ec, gos, cat in (r[:6] for r in rows):
        if not ec or ec.endswith("-"):  # require a complete EC
            continue
        rheas = set(re.findall(r"RHEA:(\d+)", cat))
        if not rheas or not all(is_unmapped(r) for r in rheas):
            continue
        cands.append((acc, gene, ec, sorted(rheas), gos.split("; ") if gos else []))

    info = go_aspects({g for c in cands for g in c[4]})
    print(f"# organism={args.organism}  enzymes(all-RHEA-unmapped, complete EC)={len(cands)}")
    print("# acc\tgene\tEC\tn_RHEA\tMF_terms")
    hits = 0
    for acc, gene, ec, rheas, gos in cands:
        mf = [(g, info.get(g, (None, "?"))[1]) for g in gos if info.get(g, (None,))[0] == "molecular_function"]
        # Judge CATALYTIC specificity: ignore cofactor/substrate "... binding"
        # terms, which otherwise mask an enzyme whose only activity term is a root.
        specific = [
            g for g, n in mf
            if g not in HIGH_LEVEL_MF and not (n or "").lower().endswith("binding")
        ]
        if specific:  # has a specific catalytic MF term -> not a (clear) gap
            continue
        hits += 1
        names = " | ".join(n for _, n in mf) or "(no MF term)"
        print(f"{acc}\t{gene}\t{ec}\t{len(rheas)}\t{names}")
        if hits >= args.limit:
            break
    print(f"# flagged (MF missing or only high-level): {hits}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
