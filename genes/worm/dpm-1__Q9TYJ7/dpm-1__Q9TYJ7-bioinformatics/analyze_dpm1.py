# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Sequence-level checks for C. elegans DPM-1 (Q9TYJ7) versus characterised DPM1s.

Fetches sequences and PANTHER cross-references live from UniProt REST and reports:
- PANTHER family/subfamily for each protein
- whether the U4PF58 fragment is an exact substring of Q9TYJ7
- position of the conserved acidic motifs (V-D-D-x-S and M-D-A-D) in each sequence
- maximal 19-residue Kyte-Doolittle hydropathy window (>1.6 suggests a TM helix)
- worm proteins carrying the DPM2 (PF07297) or DPM3 (PF08285) Pfam domains

Run: uv run --script analyze_dpm1.py
"""
import re
import urllib.request

ACCS = {"Q9TYJ7": "worm dpm-1", "U4PF58": "worm dpm-1 fragment",
        "O60762": "human DPM1", "P14020": "yeast Dpm1"}
KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def get(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def entry(acc: str) -> tuple[str, list[str]]:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt")
    seq = "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].split()).rstrip("/")
    panther = [line.split(";")[1].strip() for line in txt.splitlines()
               if line.startswith("DR   PANTHER;")]
    return seq, panther


def max_kd(seq: str, w: int = 19) -> tuple[float, int]:
    best = (-99.0, 0)
    for i in range(len(seq) - w + 1):
        s = sum(KD[a] for a in seq[i:i + w]) / w
        if s > best[0]:
            best = (round(s, 2), i + 1)
    return best


seqs = {}
for acc, name in ACCS.items():
    seq, panther = entry(acc)
    seqs[acc] = seq
    m1 = [m.start() + 1 for m in re.finditer(r"[VI]DD.S", seq)]
    m2 = [m.start() + 1 for m in re.finditer(r"MDAD", seq)]
    kd, pos = max_kd(seq) if len(seq) >= 19 else (None, None)
    print(f"{acc}\t{name}\tlen={len(seq)}\tPANTHER={','.join(panther)}"
          f"\t[VI]DDxS@{m1}\tMDAD@{m2}\tmaxKD19={kd}@{pos}\tC-term={seq[-30:]}")

print("U4PF58 substring of Q9TYJ7:", seqs["U4PF58"] in seqs["Q9TYJ7"])

for pf, label in (("PF07297", "DPM2"), ("PF08285", "DPM3")):
    tsv = get("https://rest.uniprot.org/uniprotkb/search?query=organism_id:6239+AND+xref:pfam-"
              f"{pf}&fields=accession,gene_names,length&format=tsv")
    rows = tsv.strip().splitlines()[1:]
    print(f"worm proteins with {label} Pfam {pf}: {rows if rows else 'none found'}")
