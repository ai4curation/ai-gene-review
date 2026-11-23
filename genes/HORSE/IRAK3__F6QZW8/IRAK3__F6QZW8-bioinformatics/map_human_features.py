"""Map experimentally characterised human IRAK3 (Q9Y616) features onto horse IRAK3 F6QZW8.

Horse F6QZW8 and human Q9Y616 sequences are read from the cached UniProt flat files in
this repository; mouse Irak3 Q8K4B2 (knockout donor, PMID:12150927) is fetched from the
UniProt REST API. Global alignment, BLOSUM62, gap open -10, extend -0.5.

Run: uv run --no-project --with biopython --with requests python map_human_features.py
Writes features.json next to this script.
"""
from pathlib import Path
import hashlib
import json

import requests
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

# Human Q9Y616 positions with their sources
FEATURES = [
    ("Death domain (PROSITE)", 41, 106, "UniProt Q9Y616 FT DOMAIN"),
    ("Trp74, death-domain surface 1 (MyD88/IRAK4 binding)", 74, 74, "PMID:38268724"),
    ("Arg97, death-domain surface (IRAK1/TRAF6 interaction)", 97, 97, "PMID:38268724"),
    ("Ser110 (phosphorylated by IRAK1; PIN1 site)", 110, 110, "PMID:29686383"),
    ("Pro111 (PIN1 isomerised; asthma variant P111A)", 111, 111, "PMID:29686383"),
    ("Protein kinase domain (PROSITE)", 165, 452, "UniProt Q9Y616 FT DOMAIN"),
    ("Glycine-rich ATP loop", 171, 179, "UniProt Q9Y616 FT BINDING"),
    ("Lys192 (ATP-binding lysine)", 192, 192, "UniProt Q9Y616 FT BINDING"),
    ("Cys202 (interchain disulfide in dimer)", 202, 202, "PMID:33238146"),
    ("Cys287 (interchain disulfide in dimer)", 287, 287, "PMID:33238146"),
    ("Catalytic loop CGS (HRD in active kinases)", 291, 293, "PMID:33238146"),
    ("Mg-binding loop DFA (DFG in active kinases)", 311, 313, "PMID:33238146"),
    ("Pro478, TRAF6-binding motif region (human 476-482)", 476, 482, "PMID:25481771"),
]


def flatfile_seq(path: Path) -> str:
    text = path.read_text()
    body = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0]
    return "".join(c for c in body if c.isalpha())


def fetch_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def align(a: str, b: str):
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.end_gap_score = 0
    aln = al.align(a, b)[0]
    pairs = {}
    for (s, e), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        for off in range(int(e - s)):
            pairs[int(s) + off + 1] = int(u) + off + 1
    ident = sum(1 for i, j in pairs.items() if a[i - 1] == b[j - 1])
    return pairs, ident


def main() -> None:
    human = flatfile_seq(ROOT / "genes/human/IRAK3/IRAK3-uniprot.txt")
    horse = flatfile_seq(ROOT / "genes/HORSE/IRAK3__F6QZW8/IRAK3__F6QZW8-uniprot.txt")
    mouse = fetch_seq("Q8K4B2")
    out = {
        "method": "Global alignment, BLOSUM62, gap open -10, extend -0.5, free end gaps",
        "sequences": {
            k: {"length": len(s), "sha256": hashlib.sha256(s.encode()).hexdigest()}
            for k, s in [("human_Q9Y616", human), ("horse_F6QZW8", horse), ("mouse_Q8K4B2", mouse)]
        },
        "pairwise": {},
        "features": [],
    }
    maps = {}
    for name, other in [("horse_F6QZW8", horse), ("mouse_Q8K4B2", mouse)]:
        pairs, ident = align(human, other)
        maps[name] = (pairs, other)
        out["pairwise"][f"human_Q9Y616_vs_{name}"] = {
            "paired": len(pairs),
            "identical": ident,
            "identity_over_paired": round(ident / len(pairs), 4),
            "human_coverage": round(len(pairs) / len(human), 4),
        }
    for label, s, e, src in FEATURES:
        row = {"feature": label, "source": src, "human": {"start": s, "end": e, "seq": human[s - 1 : e]}}
        for name, (pairs, other) in maps.items():
            mapped = [pairs.get(i) for i in range(s, e + 1)]
            seq = "".join(other[i - 1] if i else "-" for i in mapped)
            present = [i for i in mapped if i]
            ident = sum(1 for i, j in zip(range(s, e + 1), mapped) if j and human[i - 1] == other[j - 1])
            row[name] = {
                "start": present[0] if present else None,
                "end": present[-1] if present else None,
                "aligned_positions": len(present),
                "identical_positions": ident,
                "seq": seq if e - s < 15 else None,
            }
        out["features"].append(row)
    (HERE / "features.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out["pairwise"], indent=2))
    for row in out["features"]:
        h = row["horse_F6QZW8"]
        m = row["mouse_Q8K4B2"]
        print(
            f"{row['feature']}: human {row['human']['start']}-{row['human']['end']} {row['human']['seq'] if row['human']['end']-row['human']['start']<15 else ''}"
            f" | horse {h['start']}-{h['end']} {h['seq'] or ''} ({h['identical_positions']}/{h['aligned_positions']} id)"
            f" | mouse {m['start']}-{m['end']} {m['seq'] or ''} ({m['identical_positions']}/{m['aligned_positions']} id)"
        )


if __name__ == "__main__":
    main()
