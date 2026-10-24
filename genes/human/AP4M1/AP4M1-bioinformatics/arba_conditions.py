"""Can the three ARBA rules cited on AP4M1 be reproduced from AP4M1's own signatures?

GOA gives AP4M1 three IEA rows whose WITH/FROM names an ARBA rule. This script pulls
each rule from the UniProt ARBA API, pulls AP4M1's signature cross-references from its
UniProt record, and reports for each rule how many condition sets it has, which
condition types those sets use, and how many sets are fully satisfied by AP4M1's own
signatures plus its taxonomy.

A rule that cannot be reproduced is not thereby wrong -- ARBA condition sets can key on
signature systems not exposed in the entry's DR lines -- but recording the gap keeps the
review's statements about these rows honest.
"""

from __future__ import annotations

import json

import requests

RULES = {
    "ARBA00026971": "GO:0005737 cytoplasm",
    "ARBA00028630": "GO:0006605 protein targeting",
    "ARBA00028253": "GO:0008104 intracellular protein localization",
}
TARGET = "O00189"

# taxonomy strings an ARBA `taxon` condition could legitimately match for human
TAXA = {
    "cellular organisms", "Eukaryota", "Opisthokonta", "Metazoa", "Eumetazoa",
    "Bilateria", "Deuterostomia", "Chordata", "Craniata", "Vertebrata",
    "Euteleostomi", "Mammalia", "Eutheria", "Euarchontoglires", "Primates",
    "Haplorrhini", "Catarrhini", "Hominidae", "Homo", "Homo sapiens",
}


def target_signatures() -> set[str]:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{TARGET}.json", timeout=60)
    r.raise_for_status()
    sigs = set()
    for x in r.json().get("uniProtKBCrossReferences", []):
        sigs.add(x["id"])
        for p in x.get("properties", []):
            if p.get("key") in {"MatchStatus", "EntryName"}:
                continue
    return sigs


def main() -> int:
    sigs = target_signatures()
    print(f"{TARGET} signature cross-reference ids: {len(sigs)}")
    print("  InterPro:", sorted(s for s in sigs if s.startswith("IPR")))
    print("  Pfam/PROSITE/PANTHER:",
          sorted(s for s in sigs if s.startswith(("PF", "PS", "PTHR", "PIRSF", "PR0", "SSF", "cd")))[:20])
    print("  FunFam:", sorted(s for s in sigs if ":FF:" in s))

    universe = sigs | TAXA
    for rule, term in RULES.items():
        d = requests.get(f"https://rest.uniprot.org/arba/{rule}", timeout=60).json()
        main_rule = d.get("mainRule", {})
        ann = main_rule.get("annotations") or d.get("annotations") or []
        go_ids = [
            a["dbReference"]["id"]
            for a in ann
            if a.get("dbReference", {}).get("database") == "GO"
        ]
        sets = main_rule.get("conditionSets") or []
        types: set[str] = set()
        satisfied = 0
        mentions = 0
        for cs in sets:
            vals_ok = True
            touched = False
            for cond in cs["conditions"]:
                types.add(cond["type"])
                vs = {v["value"] for v in cond["conditionValues"]}
                if vs & sigs:
                    touched = True
                if cond.get("isNegative"):
                    if vs & universe:
                        vals_ok = False
                elif not (vs & universe):
                    vals_ok = False
            if touched:
                mentions += 1
            if vals_ok:
                satisfied += 1
        print(f"\n{rule} -> {go_ids} (GOA says {term})")
        print(f"  condition sets: {len(sets)}; condition types used: {sorted(types)}")
        print(f"  sets mentioning any AP4M1 signature: {mentions}")
        print(f"  sets fully satisfied by AP4M1's signatures + taxonomy: {satisfied}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
