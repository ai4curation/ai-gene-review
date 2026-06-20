#!/usr/bin/env python3
"""Score human genes lacking deep research for falcon prioritization.

Prioritization goals (per user):
  - broad coverage across functional families (avoid clustering on paralog groups)
  - favour less well-studied genes
  - favour genes with NO PAINT (IBA) molecular-function annotation

For each gene we read its GOA tsv and compute:
  has_iba_mf            : any molecular_function row with evidence IBA (PAINT MF)
  n_mf                  : distinct molecular_function GO terms
  n_exp                 : experimental annotations (IDA/IMP/IPI/IGI/IEP/EXP/HDA/HMP/HEP)
  n_pmids               : distinct PMID references (study-depth proxy)
  family                : longest alpha prefix of the symbol (rough paralog grouping)

We then rank candidates so that:
  1. genes WITHOUT a PAINT MF come first,
  2. then less-studied (fewer pmids, fewer experimental annots),
  3. with a per-family cap so the final set spans many families (broad coverage).
"""
import csv
import re
import sys
from pathlib import Path

EXP = {"EXP", "IDA", "IMP", "IPI", "IGI", "IEP", "HDA", "HMP", "HEP", "HGI"}
GENES_DIR = Path("genes/human")


def family(sym: str) -> str:
    m = re.match(r"^([A-Z]+)", sym)
    return m.group(1) if m else sym


def analyze(gene: str) -> dict:
    goa = GENES_DIR / gene / f"{gene}-goa.tsv"
    d = dict(gene=gene, has_iba_mf=0, n_mf=0, n_exp=0, n_pmids=0, n_total=0,
             family=family(gene))
    if not goa.exists():
        d["missing_goa"] = True
        return d
    mf_terms, pmids = set(), set()
    with open(goa) as fh:
        r = csv.DictReader(fh, delimiter="\t")
        for row in r:
            d["n_total"] += 1
            aspect = row.get("GO ASPECT", "")
            ev = row.get("GO EVIDENCE CODE", "")
            ref = row.get("REFERENCE", "")
            if aspect == "molecular_function":
                mf_terms.add(row.get("GO TERM", ""))
                if ev == "IBA":
                    d["has_iba_mf"] = 1
            if ev in EXP:
                d["n_exp"] += 1
            for p in re.findall(r"PMID:\d+", ref):
                pmids.add(p)
    d["n_mf"] = len(mf_terms)
    d["n_pmids"] = len(pmids)
    return d


def main():
    genes = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    rows = [analyze(g) for g in genes]
    # study-depth score: lower = less studied
    for d in rows:
        d["study"] = d["n_pmids"] + d["n_exp"]
    # primary sort: no PAINT MF first; then least studied; then fewest total annots
    rows.sort(key=lambda d: (d["has_iba_mf"], d["study"], d["n_total"]))

    # Greedy selection with per-family cap for broad coverage
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    want = int(sys.argv[2]) if len(sys.argv) > 2 else 47
    chosen, fam_count = [], {}
    # pass 1: respect cap
    for d in rows:
        if len(chosen) >= want:
            break
        if d.get("missing_goa"):
            continue
        f = d["family"]
        if fam_count.get(f, 0) >= cap:
            continue
        fam_count[f] = fam_count.get(f, 0) + 1
        chosen.append(d)
    # pass 2: if short, relax cap
    if len(chosen) < want:
        chosen_set = {d["gene"] for d in chosen}
        for d in rows:
            if len(chosen) >= want:
                break
            if d.get("missing_goa") or d["gene"] in chosen_set:
                continue
            chosen.append(d)
            chosen_set.add(d["gene"])

    print("# gene\thas_iba_mf\tn_mf\tn_exp\tn_pmids\tn_total\tfamily")
    for d in chosen:
        print(f"{d['gene']}\t{d['has_iba_mf']}\t{d['n_mf']}\t{d['n_exp']}\t"
              f"{d['n_pmids']}\t{d['n_total']}\t{d['family']}")
    # also emit just the gene list to stderr summary
    sys.stderr.write(f"selected {len(chosen)} genes; "
                     f"no-PAINT-MF: {sum(1 for d in chosen if not d['has_iba_mf'])}; "
                     f"families: {len(set(d['family'] for d in chosen))}\n")


if __name__ == "__main__":
    main()
