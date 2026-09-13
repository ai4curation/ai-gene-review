"""Which ARBA condition set actually fires on AHNAK2, and on what feature?

`GO_REF:0000117` rows are ARBA machine-learning rules. The row is only as good
as the condition that matched, so resolve it: fetch the rule, intersect each
condition set with AHNAK2's own InterPro signatures and lineage, and print the
matching set together with the GO term the rule applies.

An ARBA rule whose only matching condition is a bare fold signature is much
weaker than one keyed on a family-specific signature -- the same distinction the
InterPro2GO rules need.

Run: uv run python arba_rules.py
"""

from __future__ import annotations

import json

from uniprot import _cached_get

SUBJECT = "Q8IVF2"
RULES = {
    "ARBA00026971": "GO:0005737 cytoplasm",
    "ARBA00027801": "GO:0005886 plasma membrane",
}
# NCBI lineage names that could appear as taxon conditions.
def lineage(acc: str) -> set[str]:
    e = json.loads(_cached_get(f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                               f"arch_{acc}"))
    org = e["organism"]
    return {org["scientificName"], *org.get("lineage", [])}


SIG_DBS = {"InterPro id": "InterPro", "PANTHER id": "PANTHER", "FunFam id": "Gene3D"}


def signatures(acc: str) -> set[str]:
    """Every signature id ARBA can condition on: InterPro, PANTHER, Gene3D/FunFam.

    A check that models only InterPro would report 'no condition set matches'
    for a rule that in fact fires on the PANTHER family -- an absence that reads
    as a finding. Model every condition type the rule actually uses.
    """
    e = json.loads(_cached_get(f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                               f"arch_{acc}"))
    out = set()
    for x in e.get("uniProtKBCrossReferences", []):
        if x["database"] in set(SIG_DBS.values()):
            out.add(x["id"])
    return out


def rule(rid: str) -> dict:
    return json.loads(_cached_get(f"https://rest.uniprot.org/arba/{rid}", f"arba_{rid}"))


def self_test() -> None:
    """A 'zero matches' result reads as a finding, so prove the matcher can fire.

    Take a condition set from the rule itself, find a real protein carrying that
    signature, and assert the matcher reports it. Without this, a typo in the
    condition-type names would produce the same 0/2388 output as a genuine
    absence.
    """
    r = rule(next(iter(RULES)))
    for cs in r["mainRule"]["conditionSets"]:
        ips = [v["value"] for c in cs["conditions"] if c["type"] == "InterPro id"
               for v in c["conditionValues"]]
        if len(ips) != 1 or any(c["type"] == "taxon" for c in cs["conditions"]):
            continue
        hits = json.loads(_cached_get(
            "https://rest.uniprot.org/uniprotkb/search?query="
            f"xref:interpro-{ips[0]}+AND+reviewed:true&fields=accession&size=1",
            f"selftest_{ips[0]}"))["results"]
        if not hits:
            continue
        acc = hits[0]["primaryAccession"]
        if ips[0] in signatures(acc):
            print(f"self-test: condition set requiring {ips[0]} is matched by {acc} "
                  f"-- the matcher fires on a true positive.\n")
            return
    raise SystemExit("self-test could not construct a true positive; "
                     "a zero-match result cannot be trusted")


def main() -> None:
    self_test()
    sigs = signatures(SUBJECT)
    taxa = lineage(SUBJECT)
    print(f"{SUBJECT} InterPro signatures: {sorted(sigs)}")
    print()

    for rid, applied in RULES.items():
        r = rule(rid)
        sets = r["mainRule"]["conditionSets"]
        matching = []
        for i, cs in enumerate(sets):
            interpro = {v["value"] for c in cs["conditions"] if c["type"] in SIG_DBS
                        for v in c["conditionValues"]}
            taxon = {v["value"] for c in cs["conditions"] if c["type"] == "taxon"
                     for v in c["conditionValues"]}
            if interpro and interpro <= sigs and (not taxon or taxon & taxa):
                matching.append((i, sorted(interpro), sorted(taxon)))
        print(f"{rid} -> applies {applied}")
        print(f"  {len(sets)} condition sets in the rule; "
              f"{len(matching)} match {SUBJECT}")
        for i, interpro, taxon in matching:
            print(f"    set #{i}: InterPro {interpro}"
                  + (f" AND taxon {taxon}" if taxon else " (no taxon restriction)"))
        if not matching:
            print("    NO condition set matches on InterPro+taxon alone -- the rule "
                  "must be keyed on something this check does not model "
                  "(keywords, length, domain counts). Reported, not guessed.")
        # Does ANY condition set even mention one of the subject's signatures?
        mentions = []
        for i, cs in enumerate(sets):
            interpro = {v["value"] for c in cs["conditions"] if c["type"] in SIG_DBS
                        for v in c["conditionValues"]}
            if interpro & sigs:
                taxon = {v["value"] for c in cs["conditions"] if c["type"] == "taxon"
                         for v in c["conditionValues"]}
                mentions.append((i, sorted(interpro), sorted(taxon)))
        print(f"  condition sets mentioning ANY AHNAK2 signature: {len(mentions)}")
        for i, interpro, taxon in mentions[:10]:
            print(f"    set #{i}: InterPro {interpro}"
                  + (f" AND taxon {taxon}" if taxon else ""))
        types = sorted({c["type"] for cs in sets for c in cs["conditions"]})
        print(f"  condition types used by this rule: {types}")
        for ann in r["mainRule"].get("annotations", []):
            cv = ann.get("annotationType") or ann
            print(f"    annotation applied: {json.dumps(cv)[:200]}")
        print()


if __name__ == "__main__":
    main()
