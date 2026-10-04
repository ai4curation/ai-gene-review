"""Does human AMN1 (Q8IY45) contain an F-box like its PAINT IBA donors?

Fetches sequences and UniProt F-box DOMAIN features from UniProt, aligns AMN1 to each donor
with MAFFT L-INS-i (pairwise, two sequences), and reports which AMN1 residues, if any, align to
the donor's annotated F-box, and their identity. Requires `mafft` on PATH.
Run: uv run python fbox_check.py
"""
import json
import re
import subprocess
import tempfile
import urllib.request

TARGET = "Q8IY45"
DONORS = {"FBXL15": "Q9H469", "FBXL7": "Q9UJT9", "FBXL5": "Q9UKA1"}


def entry(acc: str) -> dict:
    return json.load(urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))


def fbox(e: dict):
    for f in e.get("features", []):
        if f["type"] == "Domain" and "F-box" in f.get("description", ""):
            return f["location"]["start"]["value"], f["location"]["end"]["value"]
    return None


def align(a: str, b: str):
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        fh.write(f">t\n{a}\n>d\n{b}\n")
    out = subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", fh.name], capture_output=True, text=True, check=True).stdout
    seqs = re.split(r">\w+\n", out)[1:]
    return [s.replace("\n", "") for s in seqs]


t = entry(TARGET)
tseq = t["sequence"]["value"]
print(f"AMN1 {TARGET}: length {len(tseq)}; UniProt F-box feature: {fbox(t)}")
print()
print("| donor | accession | donor F-box | AMN1 residues aligned to it | identical | aligned (non-gap) |")
print("|---|---|---|---|---|---|")
for name, acc in DONORS.items():
    d = entry(acc)
    fb = fbox(d)
    ta, da = align(tseq, d["sequence"]["value"])
    ti = di = 0
    tpos, ident, aligned = [], 0, 0
    for x, y in zip(ta, da):
        if x != "-":
            ti += 1
        if y != "-":
            di += 1
        if y != "-" and fb[0] <= di <= fb[1]:
            if x != "-":
                aligned += 1
                tpos.append(ti)
                ident += x == y
    span = f"{min(tpos)}-{max(tpos)}" if tpos else "none"
    print(f"| {name} | {acc} | {fb[0]}-{fb[1]} | {span} | {ident} | {aligned} of {fb[1]-fb[0]+1} |")
