"""Compare A0A6I8TLE4 with PTHR10194 members and check the RasGAP arginine finger.

Fetches sequences from UniProt REST, aligns them with MAFFT (L-INS-i), and reports
(1) pairwise identity of the target to each comparator over aligned columns, and
(2) the residue in each sequence at the column of the p120GAP (RASA1, P20936)
arginine finger R789, plus the neighbouring finger-loop residues.

Run: uv run --with requests python compare_rasgap_rereview.py
"""
import subprocess
import sys
from pathlib import Path

import requests

HERE = Path(__file__).parent
TARGET = "A0A6I8TLE4"
COMPARATORS = {
    "Q8T498": "raskol DROME (SF60)",
    "Q8MLZ5": "gap-2 CAEEL (SF60)",
    "P33314": "BUD2 YEAST (SF60)",
    "Q54Y08": "ngap DICDI (SF60)",
    "Q5VWQ8": "DAB2IP HUMAN (SF26)",
    "Q9UJF2": "RASAL2 HUMAN (SF52)",
    "Q96PV0": "SYNGAP1 HUMAN (SF25)",
    "P20936": "RASA1 HUMAN (SF146)",
    "P21359": "NF1 HUMAN (SF142)",
}
FINGER_REF = ("P20936", 789)  # p120GAP arginine finger


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def read_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    name = None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        elif name:
            seqs[name] += line.strip()
    return seqs


def main() -> None:
    accs = [TARGET, *COMPARATORS]
    raw = {a: fetch(a) for a in accs}
    fa = HERE / "rasgap_rereview_input.fasta"
    fa.write_text("".join(f">{a}\n{s}\n" for a, s in raw.items()))
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)],
        capture_output=True, text=True, check=True,
    ).stdout
    (HERE / "rasgap_rereview_aln.fasta").write_text(out)
    aln = read_fasta(out)
    t = aln[TARGET]
    print(f"{'accession':10} {'label':24} {'len':>5} {'aligned':>8} {'%id':>6}")
    for a, label in COMPARATORS.items():
        s = aln[a]
        cols = [(x, y) for x, y in zip(t, s) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in cols)
        pct = 100 * ident / len(cols) if cols else 0.0
        print(f"{a:10} {label:24} {len(raw[a]):5d} {len(cols):8d} {pct:6.1f}")
    ref, pos = FINGER_REF
    col, n = None, 0
    for i, c in enumerate(aln[ref]):
        if c != "-":
            n += 1
            if n == pos:
                col = i
                break
    assert col is not None
    print(f"\nArginine-finger column (from {ref} R{pos}); window -3..+3:")
    for a in accs:
        s = aln[a]
        res_pos = sum(1 for c in s[: col + 1] if c != "-")
        print(f"{a:10} {s[col - 3: col + 4]}  residue={s[col]} pos={res_pos if s[col] != '-' else 'gap'}")


if __name__ == "__main__":
    sys.exit(main())
