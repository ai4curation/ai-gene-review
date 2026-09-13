"""Before proposing a new term, ENUMERATE the plausible parents' children.

A failed keyword search is not evidence a term is absent: OLS/QuickGO search is
token-based, so `"TNFSF12 binding"` cannot match a term named
`tumor necrosis factor ligand superfamily member 12 binding`, and a proposal
would then duplicate something that already exists. This lists every child of
each plausible parent and prints them in full, so the absence is a reading of the
list rather than of a search result.

Also runs the reference-projection check on the papers behind the NEW biological
process rows: a reference that annotates a complex plus its subunits with
identical evidence is one finding distributed, not N findings.

Run: uv run python proposed_term_check.py
"""

from __future__ import annotations

import json
from collections import Counter

from uniprot import _cached_get

QG = "https://www.ebi.ac.uk/QuickGO/services"

# Every parent under which a TNFSF12-binding term could plausibly already sit.
PARENTS = {
    "GO:0019955": "cytokine binding (the proposed parent)",
    "GO:0043120": "tumor necrosis factor binding (where GO:0038057 TNFSF11 binding sits)",
    "GO:0005102": "signaling receptor binding",
}
PROPOSED = "TNFSF12"
ALIASES = ("tnfsf12", "tweak", "tumor necrosis factor ligand superfamily member 12")

# The NEW biological-process rows and the paper each rests on.
NEW_BP = {
    "GO:0000381": "PMID:40035560",
    "GO:0010508": "PMID:27513923",
    "GO:0010595": "PMID:27513923",
    "GO:0051897": "PMID:34551592",
}


def qg(path: str, key: str) -> dict:
    d = json.loads(_cached_get(f"{QG}/{path}", key))
    if "results" in d and d.get("numberOfHits", 0) > len(d["results"]):
        d["_truncated"] = True
    return d


def term(go_id: str) -> dict:
    return qg(f"ontology/go/terms/{go_id}/complete", f"ptc_{go_id.replace(':', '_')}")["results"][0]


def check_proposed() -> None:
    print(f"=== does a {PROPOSED} binding term already exist? ===")
    print("Enumerating children, not searching -- search is token-based and would")
    print("miss a term whose name spells the ligand out in full.")
    total = 0
    hits = []
    for parent, why in PARENTS.items():
        t = term(parent)
        kids = [c["id"] for c in (t.get("children") or [])]
        print(f"\n{parent} {t['name']} -- {why}: {len(kids)} child term(s)")
        for kid in kids:
            k = term(kid)
            total += 1
            name = k["name"]
            defn = (k.get("definition") or {}).get("text", "")
            if any(a in name.lower() or a in defn.lower() for a in ALIASES):
                hits.append((kid, name))
            print(f"    {kid}  {name}")
    print()
    if hits:
        print(f"ALREADY EXISTS -- do NOT propose: {hits}")
        raise SystemExit(1)
    print(f"{total} child terms enumerated across {len(PARENTS)} parents; none names or "
          f"defines {PROPOSED}/TWEAK. The proposal is not a duplicate.")
    print()


def check_projection() -> None:
    print("=== reference-projection check on the papers behind the NEW BP rows ===")
    print("A reference that annotates a complex plus its subunits with identical")
    print("evidence is one finding distributed, not N findings.")
    for go_id, ref in NEW_BP.items():
        d = qg(f"annotation/search?reference={ref}&limit=100", f"ptc_ref_{ref.replace(':', '_')}")
        n = d.get("numberOfHits", 0)
        if d.get("_truncated"):
            print(f"  {ref} (for {go_id}): {n} annotations -- paginated, entity count "
                  "UNAVAILABLE, projection test not run")
            continue
        ents = sorted({r["geneProductId"] for r in d["results"]})
        ev = Counter(r["goEvidence"] for r in d["results"])
        syms = sorted({r.get("symbol") or r["geneProductId"] for r in d["results"]})
        print(f"  {ref} (for {go_id}): {n} annotation(s) over {len(ents)} entit(y/ies); "
              f"evidence {dict(ev)}")
        if ents:
            print(f"      entities: {', '.join(syms)}")
        if n == 0:
            print("      -> produced no GO annotation at all, so nothing to project.")
        elif len(ents) > 5 and len(ev) == 1:
            print("      -> MANY entities with ONE evidence code: inspect for projection.")
        else:
            print("      -> not a projection pattern.")
    print()


def main() -> None:
    check_proposed()
    check_projection()


if __name__ == "__main__":
    main()
