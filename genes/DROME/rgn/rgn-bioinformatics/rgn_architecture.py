# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Architecture checks for Drosophila Rgn (M9PFV8) against PANTHER PTHR23211 seeds
(TGN38/TGOLN2) and against PTHR22803 C-type lectins (REG1A, REG3A, fly lectin-galC1).

Checks: (1) hydrophobic transmembrane-like segments (Kyte-Doolittle, window 19, >=1.6);
(2) C-terminal tyrosine sorting motif YxxL/YxxI/YxxV/YxxF/YxxM in the last 40 residues;
(3) CTLD sugar/Ca2+ motifs (EPN/QPD and WND) in the CTLD; (4) global pairwise identity.
Sequences are fetched live from UniProt REST; nothing is hard-coded except accessions.
"""
import json
import random
import re
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "M9PFV8": "rgn isoform B/C (fly, PTHR23211:SF0)",
    "Q9Y102": "rgn isoform A/D (fly, PTHR23211:SF0)",
    "O43493": "TGOLN2 (human, PTHR23211:SF0, PAINT seed)",
    "P19814": "Ttgn1/TGN38 (rat, PTHR23211:SF0, PAINT seed)",
    "P05451": "REG1A (human, PTHR22803)",
    "Q06141": "REG3A (human, PTHR22803)",
    "Q9VIX1": "lectin-galC1/DL1 (fly, PTHR22803; ISS donor FBgn0016675)",
}
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def tm_segments(seq: str, window: int = 19, cutoff: float = 1.6, skip_n: int = 30):
    hits = []
    for i in range(skip_n, len(seq) - window + 1):
        score = sum(KD[a] for a in seq[i:i + window]) / window
        if score >= cutoff:
            hits.append((i + 1, round(score, 2)))
    # collapse to segments
    segs = []
    for pos, sc in hits:
        if segs and pos <= segs[-1][1] + 1:
            segs[-1] = (segs[-1][0], pos, max(segs[-1][2], sc))
        else:
            segs.append((pos, pos, sc))
    return [{"start": s, "end": e + window - 1, "max_kd": m} for s, e, m in segs]


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "local"
    out = {}
    rgn = seqs["M9PFV8"]
    for acc, desc in ACCS.items():
        s = seqs[acc]
        tail = s[-40:]
        rec = {
            "description": desc,
            "length": len(s),
            "tm_like_segments_after_res30": tm_segments(s),
            "c_terminal_YxxPhi_motifs": [m.group() for m in re.finditer(r"(?=(Y..[LIVFM]))", tail)]
            and [m.group(1) for m in re.finditer(r"(?=(Y..[LIVFM]))", tail)],
        }
        if acc != "M9PFV8":
            aln = aligner.align(rgn, s)[0]
            ident = sum(1 for (a, b) in zip(*aln) if a == b and a != "-")
            alen = sum(1 for (a, b) in zip(*aln) if a != "-" and b != "-")
            rec["local_alignment_vs_M9PFV8"] = {
                "score": aln.score,
                "aligned_pairs": alen,
                "identities": ident,
                "percent_identity": round(100 * ident / alen, 1) if alen else 0.0,
                "rgn_span": [int(aln.aligned[0][0][0]) + 1, int(aln.aligned[0][-1][1])],
            }
        out[acc] = rec
    # composition-preserving shuffle control for each comparator (seeded, 200 shuffles)
    rng = random.Random(7227)
    for acc in ACCS:
        if acc in ("M9PFV8", "Q9Y102"):
            continue
        s = list(seqs[acc])
        scores = []
        for _ in range(200):
            rng.shuffle(s)
            scores.append(aligner.score(rgn, "".join(s)))
        scores.sort()
        real = out[acc]["local_alignment_vs_M9PFV8"]["score"]
        out[acc]["shuffle_control"] = {
            "n": len(scores),
            "max_shuffled_score": scores[-1],
            "median_shuffled_score": scores[len(scores) // 2],
            "fraction_shuffled_ge_real": sum(1 for x in scores if x >= real) / len(scores),
        }
    ctld = rgn[69:199]
    out["M9PFV8_CTLD_70_199"] = {
        "sequence": ctld,
        "cysteine_positions": [i + 70 for i, a in enumerate(ctld) if a == "C"],
        "EPN_present": "EPN" in ctld,
        "QPD_present": "QPD" in ctld,
        "WND_present": "WND" in ctld,
    }
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
