"""Does human AMN1 (Q8IY45) contain an F-box like the donors of its PAINT IBAs?

1. For each IBA row in ../AMN1-goa.tsv, every WITH/FROM gene donor is resolved to a UniProt entry
   (MGI, FlyBase, ZFIN, Araport, SGD cross-references, or a UniProtKB accession) and its UniProt
   F-box DOMAIN feature is reported.
2. AMN1 is aligned pairwise (MAFFT L-INS-i) to three human F-box donors to see which AMN1 residues,
   if any, align to their F-box.
Requires `mafft` on PATH. Run: uv run python fbox_check.py
"""
import json
import re
import subprocess
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

TARGET = "Q8IY45"
ALIGN_TO = {"FBXL15": "Q9H469", "FBXL7": "Q9UJT9", "FBXL5": "Q9UKA1"}
XREF = {"MGI": "mgi", "FB": "flybase", "ZFIN": "zfin", "AGI_LocusCode": "araport", "SGD": "sgd"}


def get(url: str) -> dict:
    return json.load(urllib.request.urlopen(url))


def resolve(donor: str):
    db, ident = donor.split(":", 1)
    if db == "UniProtKB":
        return ident
    ident = ident.split(":", 1)[1] if db == "MGI" else ident
    q = urllib.parse.quote(f"xref:{XREF[db]}-{ident}")
    for extra in ("+AND+reviewed:true", ""):
        r = get(f"https://rest.uniprot.org/uniprotkb/search?query={q}{extra}&fields=accession&format=json&size=1")["results"]
        if r:
            return r[0]["primaryAccession"]
    return None


def entry(acc: str) -> dict:
    return get(f"https://rest.uniprot.org/uniprotkb/{acc}.json")


def fbox(e: dict):
    for f in e.get("features", []):
        if f["type"] == "Domain" and "F-box" in f.get("description", ""):
            return f["location"]["start"]["value"], f["location"]["end"]["value"]
    return None


def panther_sf(e: dict) -> str:
    ids = [x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
    sf = [i for i in ids if ":SF" in i]
    return sf[0] if sf else (ids[0] + " (no subfamily)" if ids else "none")


def gene(e: dict) -> str:
    g = e.get("genes") or [{}]
    return (g[0].get("geneName") or {}).get("value", "-")


goa = Path(__file__).resolve().parent.parent / "AMN1-goa.tsv"
rows = [ln.split("\t") for ln in goa.read_text().splitlines()[1:] if ln.split("\t")[8] == "IBA"]
for row in rows:
    term, label = row[4], row[5]
    donors = [d for d in row[10].split("|") if not d.startswith("PANTHER:")]
    print(f"\n## {term} {label}: {len(donors)} donors\n")
    print("| donor | UniProt | gene | organism | length | PANTHER | F-box |")
    print("|---|---|---|---|---|---|---|")
    for d in donors:
        acc = resolve(d)
        if acc is None:
            print(f"| {d} | unresolved | - | - | - | - | - |")
            continue
        e = entry(acc)
        fb = fbox(e)
        print(f"| {d} | {acc} | {gene(e)} | {e['organism']['scientificName']} | {e['sequence']['length']} | {panther_sf(e)} | {f'{fb[0]}-{fb[1]}' if fb else 'none'} |")

t = entry(TARGET)
tseq = t["sequence"]["value"]
print(f"\n## AMN1 alignment\n\nAMN1 {TARGET}: length {len(tseq)}; PANTHER {panther_sf(t)}; UniProt F-box feature: {fbox(t)}\n")
print("| donor | accession | donor F-box | AMN1 residues aligned to it | identical | aligned (non-gap) |")
print("|---|---|---|---|---|---|")
for name, acc in ALIGN_TO.items():
    d = entry(acc)
    fb = fbox(d)
    if fb is None:
        print(f"| {name} | {acc} | none | - | - | - |")
        continue
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        fh.write(f">t\n{tseq}\n>d\n{d['sequence']['value']}\n")
    out = subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", fh.name], capture_output=True, text=True, check=True).stdout
    ta, da = [s.replace("\n", "") for s in re.split(r">\w+\n", out)[1:]]
    ti = di = 0
    tpos, ident = [], 0
    for x, y in zip(ta, da):
        ti += x != "-"
        di += y != "-"
        if y != "-" and fb[0] <= di <= fb[1] and x != "-":
            tpos.append(ti)
            ident += x == y
    span = f"{min(tpos)}-{max(tpos)}" if tpos else "none"
    print(f"| {name} | {acc} | {fb[0]}-{fb[1]} | {span} | {ident} | {len(tpos)} of {fb[1]-fb[0]+1} |")
