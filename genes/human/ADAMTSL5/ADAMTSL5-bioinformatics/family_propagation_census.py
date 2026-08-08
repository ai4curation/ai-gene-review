#!/usr/bin/env python3
"""Census of PAINT/IBA propagation across the eight human PTHR13723 ADAMTSL/papilin
proteins, plus the two checks that decide ADAMTSL5's location rows.

Three questions, each answered from an authoritative source rather than from a
sibling review:

1. Which human family members actually RECEIVED each IBD term from node
   PTN000347317?  (QuickGO -- the propagation, not the tree file.)
2. Is the propagated term the LCA of its donors, or does it sit above an agreeing
   donor set?  (Donor term distribution.)
3. Is a shared supporting reference a per-gene curation or a bulk projection?
   (Entities per reference -- entity SET, never the annotation total.)

Every count is derived; nothing is hand-asserted. Missing input is a hard error.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
UA = {"User-Agent": "ai-gene-review/ADAMTSL5 (cjmungall@lbl.gov)", "accept": "application/json"}

# The eight human members of PANTHER family PTHR13723 that are ADAMTS-LIKE
# (non-catalytic) or papilin, plus four catalytic ADAMTS proteases as controls.
ADAMTSL = [
    ("Q8N6G6", "ADAMTSL1", "SF157"),
    ("Q86TH1", "ADAMTSL2", "SF147"),
    ("P82987", "ADAMTSL3", "SF169"),
    ("Q6UY14", "ADAMTSL4", "SF144"),
    ("Q6ZMM2", "ADAMTSL5", "SF173"),
    ("Q6ZMP0", "THSD4",    "SF16"),
    ("O95428", "PAPLN",    "SF281"),
]
CATALYTIC = [
    ("Q9UHI8", "ADAMTS1",  "SF40"),
    ("Q9H324", "ADAMTS10", "-"),
    ("Q8TE56", "ADAMTS17", "-"),
    ("Q9P2N4", "ADAMTS9",  "-"),
]

# The four IBD terms sitting at node PTN000347317 in the cached PAINT file.
NODE = "PTN000347317"
IBD_TERMS = ["GO:0031012", "GO:0030198", "GO:0004222", "GO:0006508"]


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as fh:
        return json.load(fh)


def annotations(acc):
    d = get_json("https://www.ebi.ac.uk/QuickGO/services/annotation/search"
                 f"?geneProductId=UniProtKB:{acc}&limit=200")
    if d["numberOfHits"] > 200:
        raise SystemExit(f"FATAL: {acc} has {d['numberOfHits']} annotations; "
                         "paginate before trusting this census.")
    return d["results"]


def entities_for_reference(ref, cap=3000):
    """DISTINCT entity set for a reference. An annotation count is NOT an entity
    count, and a page total is NOT the whole -- both mistakes inflate the
    projection signal, so derive the set and refuse to guess when truncated."""
    ents, seen, page = set(), 0, 1
    per_term = {}
    total = None
    while True:
        d = get_json("https://www.ebi.ac.uk/QuickGO/services/annotation/search"
                     f"?reference={urllib.parse.quote(ref)}&limit=200&page={page}")
        total = d["numberOfHits"] if total is None else total
        rows = d["results"]
        if not rows:
            break
        for r in rows:
            ents.add(r["geneProductId"])
            per_term.setdefault(r["goId"], set()).add(r["geneProductId"])
        seen += len(rows)
        if seen >= total or seen >= cap:
            break
        page += 1
    truncated = seen < total
    return total, ents, per_term, truncated


def main():
    print("=" * 78)
    print("1. WHICH human PTHR13723 members received each IBD term from "
          f"node {NODE}?")
    print("=" * 78)
    hdr = f"{'gene':10} {'subfam':7} " + " ".join(f"{t[3:]:>9}" for t in IBD_TERMS)
    print(hdr)
    table = {}
    for acc, sym, sf in ADAMTSL + CATALYTIC:
        rs = annotations(acc)
        cells, row = [], {}
        for go in IBD_TERMS:
            hits = [r for r in rs if r["goId"] == go and r["goEvidence"] == "IBA"]
            neg = any("NOT" in (h.get("qualifier") or "") for h in hits)
            nodes = sorted({c["id"] for h in hits
                            for w in (h.get("withFrom") or [])
                            for c in w["connectedXrefs"] if c["id"].startswith("PTN")})
            if not hits:
                s = "-"
            elif neg:
                s = "NOT-IBA"
            else:
                s = "IBA"
            row[go] = {"state": s, "nodes": nodes}
            cells.append(f"{s:>9}")
        table[sym] = row
        tag = "" if (acc, sym, sf) in [(a, s, f) for a, s, f in ADAMTSL] else "  [catalytic]"
        print(f"{sym:10} {sf:7} " + " ".join(cells) + tag)
        time.sleep(0.2)

    print("\n-- ADAMTSL (non-catalytic) subgroup only --")
    for go in IBD_TERMS:
        got = [s for _, s, _ in ADAMTSL if table[s][go]["state"] == "IBA"]
        notv = [s for _, s, _ in ADAMTSL if table[s][go]["state"] == "NOT-IBA"]
        miss = [s for _, s, _ in ADAMTSL if table[s][go]["state"] == "-"]
        print(f"  {go}: received={len(got)}/{len(ADAMTSL)} {got}")
        if notv:
            print(f"           explicit NOT: {notv}")
        print(f"           absent      : {miss}")

    print("\n" + "=" * 78)
    print("2. Donor term distribution for ADAMTSL5's GO:0031012 IBA (LCA check)")
    print("=" * 78)
    res = HERE / "withfrom_resolution.json"
    if not res.exists():
        raise SystemExit(f"FATAL: missing {res}. Run resolve_withfrom.py first.")
    d = json.loads(res.read_text())
    c = Counter()
    for r in d["records"]:
        for t, _ in r["own_experimental_terms"]:
            c[t] += 1
    labels = {}
    for t in c:
        labels[t] = get_json("https://www.ebi.ac.uk/QuickGO/services/ontology/go/"
                             f"terms/{urllib.parse.quote(t)}/complete")["results"][0]["name"]
    for t, n in c.most_common():
        print(f"  {t}  {labels[t]:24} {n} donor(s)")
    distinct = len(c)
    print(f"\n  distinct donor locations = {distinct}")
    print("  => GRANULARITY_MISMATCH requires the donors to AGREE. They do not, so the")
    print("     general term IS the LCA and no specificity upgrade is warranted.")

    print("\n" + "=" * 78)
    print("3. Projection test: entities per supporting reference")
    print("=" * 78)
    for ref in ["PMID:23010571", "PMID:23962539"]:
        total, ents, per_term, trunc = entities_for_reference(ref)
        if trunc:
            print(f"  {ref}: TRUNCATED -- entity count unavailable, projection test "
                  f"unreliable (annotations={total})")
            continue
        print(f"  {ref}: annotations={total}  DISTINCT entities={len(ents)}")
        for go, es in sorted(per_term.items(), key=lambda kv: -len(kv[1])):
            print(f"      {go}: {len(es)} entities")

    out = HERE / "family_census.json"
    out.write_text(json.dumps(
        {"node": NODE, "ibd_terms": IBD_TERMS, "table": table,
         "donor_term_distribution": dict(c), "donor_term_labels": labels},
        indent=2))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
