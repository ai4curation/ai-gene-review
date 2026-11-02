"""Sequence checks for RBMP2 (A0A2K3DG19), standard library only.

Run: python3 analyze_sequence.py  (from this folder)

Reports:
  1. Cysteine positions in the whole protein and within the PROSITE PS50206
     rhodanese domain (775-920, from the UniProt FT line).
     Also scans the domain for [C/D]xxGxx, a crude pointer to the residue in
     the position of the catalytic Cys of active rhodanese domains.
  2. Occurrences of the Rubisco-binding motif consensus [D/N]W[R/K]XX[L/I/V/A]
     defined by Meyer et al. 2020 (PMID:33177094).
  3. Kyte-Doolittle hydropathy windows (19 aa) with mean >= 1.6, the classic
     threshold for candidate transmembrane helices. This is a crude screen,
     not a topology prediction.
"""
import re
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "RBMP2-uniprot.txt"
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2,
          I=4.5, L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9,
          Y=-1.3, V=4.2)


def read_seq(path):
    text = path.read_text()
    sq = text.split("\nSQ   ")[1].split("\n", 1)[1]
    return "".join(sq.replace("//", "").split())


def domain_bounds(path, name="Rhodanese"):
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", line)
        if m and name in lines[i + 1]:
            return int(m.group(1)), int(m.group(2))
    return None


def main():
    seq = read_seq(UNIPROT)
    print(f"length: {len(seq)}")
    cys = [i + 1 for i, c in enumerate(seq) if c == "C"]
    print(f"cysteines (whole protein): {cys}")
    bounds = domain_bounds(UNIPROT)
    if bounds:
        s, e = bounds
        dom = seq[s - 1:e]
        print(f"rhodanese domain {s}-{e}: {dom}")
        print(f"cysteines in rhodanese domain: "
              f"{[p for p in cys if s <= p <= e]}")
        # Rhodanese active-site loops start with the catalytic Cys followed by
        # a short loop containing Gly (e.g. CRxGx[R/T] in CDC25, CxxGxx in
        # sulfurtransferases). Scan for any [C/D]xxGxx in the domain as a crude
        # pointer to the residue occupying the Cys position.
        for m in re.finditer(r"[CD]..G..", dom):
            print(f"  [C/D]xxGxx loop candidate at {s + m.start()}: {m.group()}")
    print("Rubisco-binding motif matches [DN]W[RK]..[LIVA]:")
    for m in re.finditer(r"(?=([DN]W[RK]..[LIVA]))", seq):
        print(f"  {m.start() + 1}-{m.start() + 6} {m.group(1)}")
    print(f"C-terminal 10 residues: {seq[-10:]}")
    w = 19
    hits = []
    for i in range(len(seq) - w + 1):
        score = sum(KD[a] for a in seq[i:i + w]) / w
        if score >= 1.6:
            hits.append((i + 1, score))
    # merge overlapping windows into segments
    segs = []
    for start, score in hits:
        if segs and start <= segs[-1][1] + 1:
            segs[-1][1] = start + w - 1
            segs[-1][2] = max(segs[-1][2], score)
        else:
            segs.append([start, start + w - 1, score])
    print("Kyte-Doolittle segments (19-aa window mean >= 1.6):")
    for s, e, sc in segs:
        print(f"  {s}-{e} max={sc:.2f} {seq[s - 1:e]}")


if __name__ == "__main__":
    main()
