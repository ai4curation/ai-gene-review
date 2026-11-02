"""Pairwise alignment of Drosophila BNIP3 (Q9VPD6) against family members,
mapping the human BNIP3 annotated regions (UniProt Q12983 features) onto the
fly sequence. Sequences are parsed from the cached UniProt flat files in the repo.

Run from repo root:  uv run python genes/DROME/BNIP3/BNIP3-bioinformatics/align_motifs.py
"""
import sys
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "fly_BNIP3_Q9VPD6": ROOT / "genes/DROME/BNIP3/BNIP3-uniprot.txt",
    "human_BNIP3_Q12983": ROOT / "genes/human/BNIP3/BNIP3-uniprot.txt",
    "human_BNIP3L_O60238": ROOT / "genes/human/BNIP3L/BNIP3L-uniprot.txt",
    "worm_dct1": ROOT / "genes/worm/dct-1/dct-1-uniprot.txt",
}

# Regions of human BNIP3 (1-based, inclusive). BH3 and TM are from the Q12983
# UniProt FT lines; the LIR (W18/L21 core "WVEL") is the canonical LIR reported
# for BNIP3 (Hanna et al. 2012, PMID:22505714).
HUMAN_REGIONS = {"LIR_core": (18, 21), "BH3_motif": (100, 125), "TM": (164, 184)}
# Fly regions as experimentally defined by Taoka et al. 2025 (PMID:40801807):
# LIR mutated at W16A/L19A (fly WIEL, residues 16-19 of Q9VPD6),
# MER deleted G42-Q53.
FLY_REGIONS = {"MER(Taoka)": (42, 53)}


def read_seq(p):
    seq, on = [], False
    for line in p.read_text().splitlines():
        if line.startswith("SQ "):
            on = True
            continue
        if on:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", ""))
    return "".join(seq)


def mapping(aln):
    """Return dict target_pos(1-based) -> query_pos(1-based) for aligned columns."""
    m = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[ts + i + 1] = qs + i + 1
    return m


def main():
    seqs = {k: read_seq(v) for k, v in FILES.items() if v.exists()}
    fly = seqs["fly_BNIP3_Q9VPD6"]
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    print(f"fly BNIP3 length {len(fly)}")
    for name, s in seqs.items():
        if name.startswith("fly"):
            continue
        aln = al.align(s, fly)[0]
        ident = sum(1 for (ts, te), (qs, qe) in zip(*aln.aligned)
                    for i in range(te - ts) if s[ts + i] == fly[qs + i])
        print(f"\n=== {name} (len {len(s)}) vs fly: identities {ident}, "
              f"identity over fly length {ident/len(fly):.1%}")
        print(aln)
        if name == "human_BNIP3_Q12983":
            m = mapping(aln)
            for reg, (a, b) in HUMAN_REGIONS.items():
                hs = s[a - 1:b]
                fpos = [m[i] for i in range(a, b + 1) if i in m]
                fs = fly[min(fpos) - 1:max(fpos)] if fpos else ""
                cov = len(fpos) / (b - a + 1)
                print(f"  human {reg} {a}-{b}: {hs}")
                print(f"    -> fly aligned {min(fpos) if fpos else '-'}-"
                      f"{max(fpos) if fpos else '-'} ({cov:.0%} of columns aligned): {fs}")
    for reg, (a, b) in FLY_REGIONS.items():
        print(f"\nfly {reg} {a}-{b}: {fly[a-1:b]}")
    # simple LIR (W/F/Y-x-x-L/I/V) scan of fly N-terminus
    import re
    print("\nCanonical LIR-like [WFY]xx[LIV] matches in fly residues 1-60:")
    for mm in re.finditer(r"(?=([WFY]..[LIV]))", fly[:60]):
        print(f"  {mm.start()+1}: {mm.group(1)}")


if __name__ == "__main__":
    sys.exit(main())
