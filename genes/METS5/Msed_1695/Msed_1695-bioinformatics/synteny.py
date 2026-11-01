"""Compare gene neighbourhoods of the M. sedula CdvB1/B2-family genes with those of
S. acidocaldarius cdvB1 (Saci_0451) and cdvB2 (Saci_1416).

For each focal locus, queries UniProt REST for loci within +/-3 positions (by ordered
locus number) and prints accession, protein name and eggNOG arCOG. Shared arCOGs
between neighbourhoods indicate conserved synteny.

Run: python3 synteny.py
"""

import json
import re
import urllib.parse
import urllib.request

FOCAL = ["Msed_1695", "Saci_1416", "Msed_2179", "Saci_0451"]
WINDOW = 3


def lookup(locus: str) -> tuple[str, str, str] | None:
    q = urllib.parse.quote(f"gene:{locus}")
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query="
        f"{q}&fields=accession,protein_name,xref_eggnog&format=json"
    )
    with urllib.request.urlopen(url, timeout=60) as fh:
        res = json.load(fh)["results"]
    if not res:
        return None
    r = res[0]
    name = r.get("proteinDescription", {})
    rec = name.get("recommendedName") or (name.get("submissionNames") or [{}])[0]
    pname = rec.get("fullName", {}).get("value", "")
    cogs = [x["id"] for x in r.get("uniProtKBCrossReferences", []) if x["database"] == "eggNOG"]
    return r["primaryAccession"], pname, ";".join(cogs)


def neighbourhood(locus: str) -> dict[str, tuple]:
    prefix, num = re.match(r"(\w+_)(\d+)", locus).groups()
    out = {}
    for d in range(-WINDOW, WINDOW + 1):
        loc = f"{prefix}{int(num) + d:0{len(num)}d}"
        out[loc] = lookup(loc)
    return out


def main() -> None:
    cog_sets = {}
    for f in FOCAL:
        print(f"== {f}")
        nb = neighbourhood(f)
        cogs = set()
        for loc, hit in nb.items():
            if hit is None:
                print(f"  {loc}\t(not found)")
                continue
            acc, pname, cog = hit
            print(f"  {loc}\t{acc}\t{pname}\t{cog}")
            if loc != f and cog:
                cogs.update(cog.split(";"))
        cog_sets[f] = cogs
    for a, b in [("Msed_1695", "Saci_1416"), ("Msed_1695", "Saci_0451"),
                 ("Msed_2179", "Saci_0451"), ("Msed_2179", "Saci_1416")]:
        shared = sorted(cog_sets[a] & cog_sets[b])
        print(f"shared neighbour arCOGs {a} vs {b}: {len(shared)} {shared}")


if __name__ == "__main__":
    main()
