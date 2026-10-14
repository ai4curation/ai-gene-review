"""Compare the zebrafish MAGI3 paralogs magi3b (LOC564220, A0A8M6YYZ5) and
wu:fi36a10 (magi3a in NCBI RefSeq, A0A0R4IGT8) with human MAGI1/2/3, spotted
gar magi3 and the two medaka co-orthologs.

Reports:
  * full-length global identity matrix;
  * per-domain identity of each zebrafish copy (and of gar magi3) to human
    MAGI3, using the UniProt domain boundaries of human MAGI3 (Q5TCQ9):
    PDZ0 (called PDZ 1 in UniProt), guanylate-kinase-like (GK), WW1, WW2,
    PDZ1-PDZ5 (UniProt PDZ 2-6), and the C-terminal disordered tail;
  * the P-loop (Walker A, human 121-128) and the C-terminal four residues.

Sequences: zebrafish from the cached UniProt records in this repository;
the others from the UniProt REST API (accessions are the PANTHER v19 calls
for PTHR10316 used in projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv, plus
human MAGI1 Q96QZ7 and MAGI2 Q86UL8, which appear in the IBA WITH/FROM column).

Run from the repository root:
    uv run python genes/DANRE/wu_fi36a10/wu_fi36a10-bioinformatics/protein_compare.py
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
GENES = ROOT / "genes" / "DANRE"

LOCAL = {
    "zf magi3b / LOC564220 (A0A8M6YYZ5)": GENES / "LOC564220" / "LOC564220-uniprot.txt",
    "zf wu:fi36a10 / magi3a (A0A0R4IGT8)": GENES / "wu_fi36a10" / "wu_fi36a10-uniprot.txt",
}
REMOTE = {
    "human MAGI3 (Q5TCQ9)": "Q5TCQ9",
    "human MAGI1 (Q96QZ7)": "Q96QZ7",
    "human MAGI2 (Q86UL8)": "Q86UL8",
    "gar magi3 (W5MYP7)": "W5MYP7",
    "medaka co-ortholog of LOC564220 (H2LTW6)": "H2LTW6",
    "medaka co-ortholog of wu:fi36a10 (A0A3B3I955)": "A0A3B3I955",
}
REF = "human MAGI3 (Q5TCQ9)"


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def fetch_json(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    return json.loads(urllib.request.urlopen(url, timeout=60).read())


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def columns(aln):
    s1, s2 = aln.sequences
    b1, b2 = aln.aligned
    i = j = 0
    for (a0, a1), (c0, c1) in zip(b1, b2):
        while i < a0:
            yield i, None
            i += 1
        while j < c0:
            yield None, j
            j += 1
        for k in range(a1 - a0):
            yield a0 + k, c0 + k
        i, j = a1, c1
    while i < len(s1):
        yield i, None
        i += 1
    while j < len(s2):
        yield None, j
        j += 1


def identity(a: str, b: str) -> float:
    aln = aligner().align(a, b)[0]
    cols = list(columns(aln))
    ident = sum(1 for i, j in cols if i is not None and j is not None and a[i] == b[j])
    return 100 * ident / len(cols)


def main() -> None:
    seqs = {k: uniprot_txt_seq(p) for k, p in LOCAL.items()}
    ref_json = None
    for k, acc in REMOTE.items():
        d = fetch_json(acc)
        seqs[k] = d["sequence"]["value"]
        if k == REF:
            ref_json = d
    ref = seqs[REF]

    domains = []
    for f in ref_json["features"]:
        if f["type"] == "Domain":
            domains.append((f["description"], f["location"]["start"]["value"], f["location"]["end"]["value"]))
    last_pdz_end = max(e for n, s, e in domains if n.startswith("PDZ"))
    domains.append(("C-terminal tail (after last PDZ)", last_pdz_end + 1, len(ref)))

    names = list(seqs)
    print("## Sequences\n")
    print("| protein | length | C-terminal 4 residues |")
    print("|---|---|---|")
    for n in names:
        print(f"| {n} | {len(seqs[n])} | {seqs[n][-4:]} |")

    print("\n## Full-length global identity (%)\n")
    print("| query | " + " | ".join(names) + " |")
    print("|---|" + "---|" * len(names))
    for n in names:
        print(f"| {n} | " + " | ".join("-" if n == t else f"{identity(seqs[n], seqs[t]):.1f}" for t in names) + " |")

    queries = [
        "zf magi3b / LOC564220 (A0A8M6YYZ5)",
        "zf wu:fi36a10 / magi3a (A0A0R4IGT8)",
        "gar magi3 (W5MYP7)",
    ]
    aligned = {}
    for q in queries:
        aln = aligner().align(ref, seqs[q])[0]
        aligned[q] = list(columns(aln))

    print("\n## Per-domain identity to human MAGI3 (UniProt Q5TCQ9 domain boundaries)\n")
    print("Identity = identical residues / human domain length.\n")
    print("| human MAGI3 domain | residues | " + " | ".join(queries) + " | zf copy A vs copy B |")
    print("|---|---|" + "---|" * len(queries) + "---|")
    za, zb = queries[0], queries[1]
    for dname, s, e in domains:
        cells = []
        segs = {}
        for q in queries:
            ident = 0
            seg = []
            for i, j in aligned[q]:
                if i is not None and s - 1 <= i <= e - 1:
                    if j is not None:
                        seg.append(seqs[q][j])
                        if ref[i] == seqs[q][j]:
                            ident += 1
            segs[q] = "".join(seg)
            cells.append(f"{100 * ident / (e - s + 1):.1f}")
        ab = f"{identity(segs[za], segs[zb]):.1f}" if segs[za] and segs[zb] else "-"
        print(f"| {dname} | {s}-{e} | " + " | ".join(cells) + f" | {ab} |")

    print("\n## Walker A / P-loop (human MAGI3 121-128)\n")
    print(f"- human MAGI3: {ref[120:128]}")
    for q in queries:
        seg = "".join(seqs[q][j] for i, j in aligned[q] if i is not None and 120 <= i <= 127 and j is not None)
        print(f"- {q}: {seg}")


if __name__ == "__main__":
    main()
