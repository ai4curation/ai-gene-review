# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Independent re-review comparison of Vmn2r73 A0A3B2WCZ5 vs canonical D3Z7M3.

Fetches both sequences and TRANSMEM features directly from UniProt REST (no
prediction-output files are read), aligns them globally, maps exact-identity
blocks, and scans Kyte-Doolittle hydropathy (window 19) for candidate
transmembrane segments in the target.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET, CANON = "A0A3B2WCZ5", "D3Z7M3"
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def fetch(acc):
    j = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()
    tms = [(f["location"]["start"]["value"], f["location"]["end"]["value"])
           for f in j.get("features", []) if f["type"] == "Transmembrane"]
    return j["sequence"]["value"], tms


def blocks(aln):
    """Return contiguous identical blocks as (canon_start, canon_end, tgt_start, tgt_end)."""
    out = []
    for (cs, ce), (ts, te) in zip(*aln.aligned):
        run = None
        for k in range(ce - cs):
            same = aln.target[cs + k] == aln.query[ts + k]
            if same and run is None:
                run = k
            if (not same or k == ce - cs - 1) and run is not None:
                end = k if same else k - 1
                if end - run + 1 >= 10:
                    out.append((cs + run + 1, cs + end + 1, ts + run + 1, ts + end + 1))
                run = None
    return out


def hydropathy_peaks(seq, w=19, thr=1.6):
    peaks = []
    for i in range(len(seq) - w + 1):
        s = sum(KD.get(a, 0) for a in seq[i:i + w]) / w
        if s >= thr:
            peaks.append((i + 1, i + w, round(s, 2)))
    return peaks


def main():
    tseq, ttm = fetch(TARGET)
    cseq, ctm = fetch(CANON)
    print(f"{TARGET} length {len(tseq)}; UniProt TRANSMEM features: {ttm or 'none'}")
    print(f"{CANON} length {len(cseq)}; UniProt TRANSMEM features: {ctm}")
    al = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                               open_gap_score=-10, extend_gap_score=-0.5)
    aln = al.align(cseq, tseq)[0]
    print("Identical blocks >=10 aa (canonical start-end -> target start-end):")
    for b in blocks(aln):
        print(f"  {b[0]}-{b[1]} -> {b[2]}-{b[3]} ({b[1]-b[0]+1} aa)")
    print(f"Target C-terminal 30 aa: {tseq[-30:]}")
    pk = hydropathy_peaks(tseq)
    print("Target KD windows (w=19) >= 1.6:", "none" if not pk else f"{len(pk)} windows; first {pk[0]}, last {pk[-1]}")
    pkc = hydropathy_peaks(cseq[560:], thr=1.6)
    print(f"Canonical KD windows >=1.6 in residues 561-{len(cseq)} (positive control): {len(pkc)}")


if __name__ == "__main__":
    main()
