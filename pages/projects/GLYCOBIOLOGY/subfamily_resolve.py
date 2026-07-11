#!/usr/bin/env python3
"""Subfamily-resolve the poly-specific cazy2go families via InterPro co-occurrence.

dbCAN-sub's subfamily->EC table is the canonical route but its server does not serve the files from
here. Instead we resolve subfamilies from data we already have: each reviewed UniProt member of a CAZy
family carries BOTH its EC(s) and its InterPro signature(s). Within a POLY-specific family (cazy2go
gives >1 GO MF), a specific activity is usually marked by a specific InterPro signature. So for each
family F and specific GO MF term G reachable from F's members' ECs, we find the InterPro signature(s)
S that, among F's members, co-occur with G at high precision:

    precision(S->G | F) = |members of F with S and G| / |members of F with S|
    support             = |members of F with S|

A high-precision, supported S is a sub-family marker for G -- a safe, signature-level attribution of
the specific activity (the unsafe family-level term resolved to a subfamily). Each such S->G is then
checked against interpro2go:
    CONFIRMS  : interpro2go already maps S -> G (or a descendant)  -> validates the method
    PROPOSED  : interpro2go does not                                -> candidate interpro2go addition

Output: TSV to stdout (family, GO, InterPro, support, precision, status).

Usage:  uv run python projects/GLYCOBIOLOGY/subfamily_resolve.py > projects/GLYCOBIOLOGY/cazy2go.subfamily.tsv
"""
from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict

sys.path.insert(0, "projects/GLYCOBIOLOGY")
from build_cazy2go import GENERIC_PARENTS, load_ec2go  # noqa: E402
from compare_cazy_interpro import cazy_go_for_family, load_interpro2go  # noqa: E402
from oaklib import get_adapter  # noqa: E402
from oaklib.datamodels.vocabulary import IS_A  # noqa: E402

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
UA = {"User-Agent": "ai-gene-review-cazy2go/1.0"}
MIN_SUPPORT = 2
MIN_PRECISION = 0.8


def load_members():
    """Per reviewed member: (accession, set(cazy_fams), set(ecs), set(iprs))."""
    out = []
    params = {
        "query": "reviewed:true AND database:cazy AND ec:*",
        "fields": "accession,ec,xref_cazy,xref_interpro",
        "format": "tsv", "size": "500",
    }
    url = UNIPROT_URL + "?" + urllib.parse.urlencode(params)
    while url:
        resp = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
        for line in resp.read().decode("utf-8", "replace").splitlines()[1:]:
            p = line.split("\t")
            if len(p) < 4:
                continue
            ecs = {e.strip() for e in p[1].split(";") if e.strip()}
            fams = {f.strip() for f in p[2].split(";") if f.strip()}
            iprs = set(re.findall(r"IPR\d+", p[3]))
            if ecs and fams:
                out.append((p[0], fams, ecs, iprs))
        m = re.search(r'<([^>]+)>;\s*rel="next"', resp.headers.get("Link", ""))
        url = m.group(1) if m else None
    return out


def main():
    ec2go = load_ec2go()
    ipr2go = load_interpro2go()
    members = load_members()
    go = get_adapter("sqlite:obo:go")
    _anc: dict[str, set[str]] = {}

    def anc(c):
        if c not in _anc:
            a = set(go.ancestors(c, predicates=[IS_A])); a.discard(c); _anc[c] = a
        return _anc[c]

    # index members by family; and how many distinct families each InterPro signature spans
    fam_members = defaultdict(list)
    sig_family_spread: dict[str, set[str]] = defaultdict(set)
    for acc, fams, ecs, iprs in members:
        for f in fams:
            fam_members[f].append((acc, ecs, iprs))
        for s in iprs:
            sig_family_spread[s].update(fams)
    fam_ec = defaultdict(set)
    for acc, fams, ecs, iprs in members:
        for f in fams:
            fam_ec[f].update(ecs)

    rows = []
    n_poly = 0
    for fam, mem in fam_members.items():
        if fam.startswith("CBM"):
            continue
        cg = cazy_go_for_family(fam_ec[fam], ec2go)
        if len(cg) <= 1:
            continue  # only poly-specific families need subfamily resolution
        n_poly += 1
        # member -> set of specific GO terms (drop generic parents)
        mem_go = []
        for acc, ecs, iprs in mem:
            gos = set()
            for ec in ecs:
                for g, _ in ec2go.get(ec, []):
                    if g not in GENERIC_PARENTS:
                        gos.add(g)
            mem_go.append((acc, gos, iprs))
        # candidate signatures
        sig_total = defaultdict(int)            # S -> #members of F with S
        sig_go = defaultdict(lambda: defaultdict(int))  # S -> G -> #members with S and G
        go_total = defaultdict(int)             # G -> #members of F with G
        for acc, gos, iprs in mem_go:
            for g in gos:
                go_total[g] += 1
            for s in iprs:
                sig_total[s] += 1
                for g in gos:
                    sig_go[s][g] += 1
        for s, gmap in sig_go.items():
            if sig_total[s] < MIN_SUPPORT:
                continue
            for g, a in gmap.items():
                prec = a / sig_total[s]
                if prec < MIN_PRECISION:
                    continue
                # status vs interpro2go
                cur = ipr2go.get(s, set())
                if g in cur or any(g in anc(i) for i in cur):
                    status = "CONFIRMS"
                elif any(i in anc(g) for i in cur):
                    status = "PROPOSED_specific"  # interpro2go gives only an ancestor
                elif cur:
                    status = "PROPOSED_other"      # interpro2go gives unrelated terms
                else:
                    status = "PROPOSED_new"        # interpro2go silent on S
                spread = len(sig_family_spread[s])
                specific = "family-specific" if spread <= 2 else "broad"
                rows.append((fam, g, go.label(g), s, sig_total[s], a, go_total[g],
                             round(prec, 2), spread, specific, status))

    rows.sort(key=lambda r: (r[0], -r[4]))
    cols = ["family", "GO_id", "GO_label", "InterPro", "support", "n_S_and_G",
            "n_G_in_fam", "precision", "sig_family_spread", "sig_specificity", "status"]
    print("\t".join(cols))
    for r in rows:
        print("\t".join(map(str, r)))
    from collections import Counter
    st = Counter(r[10] for r in rows)
    spec = Counter(r[9] for r in rows)
    # the trustworthy set: family-specific signature AND a proposed/confirmed gain
    good_new = [r for r in rows if r[9] == "family-specific" and r[10].startswith("PROPOSED")]
    print(f"\n# poly-specific families={n_poly}; signature->GO rows={len(rows)}; "
          f"families_resolved={len({r[0] for r in rows})}", file=sys.stderr)
    print(f"# status={dict(st)}; signature_specificity={dict(spec)}", file=sys.stderr)
    print(f"# trustworthy proposals (family-specific signature, not yet in interpro2go)={len(good_new)} "
          f"across {len({r[0] for r in good_new})} families", file=sys.stderr)


if __name__ == "__main__":
    main()
