# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare S. pombe asr1 (O94400) with candidate relatives.

Candidates: S. cerevisiae Asr1 (Q06834; PomBase-curated ortholog, PANTHER PTHR45798:SF97),
human PHRF1 (Q9P1Y6; PANTHER PTHR12618:SF20, same subfamily as O94400) and
Komagataella phaffii Atg35 (C4QVX6; PTHR12618:SF20).

For each pair: Smith-Waterman local alignment (BLOSUM62, open -11, extend -1) of the
full-length sequences, identity over the aligned region, and a z-score against 200
shuffled versions of the candidate sequence. Also aligns the pombe N-terminal 1-200
(RING + PHD region) separately. Results printed as JSON; nothing is hardcoded.
"""
import json
import random
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"O94400": "S. pombe asr1", "Q06834": "S. cerevisiae ASR1",
        "Q9P1Y6": "H. sapiens PHRF1", "C4QVX6": "K. phaffii ATG35"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "local"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    return a


def compare(al, q, t, nshuf=200, seed=1):
    best = al.align(q, t)[0]
    score = best.score
    ident = aligned = 0
    for (qs, qe), (ts, te) in zip(*best.aligned):
        for i in range(qe - qs):
            aligned += 1
            ident += q[qs + i] == t[ts + i]
    rng = random.Random(seed)
    shuf = []
    for _ in range(nshuf):
        s = list(t)
        rng.shuffle(s)
        shuf.append(al.score(q, "".join(s)))
    mean = sum(shuf) / nshuf
    sd = (sum((x - mean) ** 2 for x in shuf) / nshuf) ** 0.5
    qcov = (int(best.aligned[0][0][0]) + 1, int(best.aligned[0][-1][1]))
    tcov = (int(best.aligned[1][0][0]) + 1, int(best.aligned[1][-1][1]))
    return {"score": float(score), "aligned_columns": aligned, "identity": round(ident / aligned, 3),
            "query_range": qcov, "target_range": tcov,
            "shuffle_mean": round(mean, 1), "shuffle_sd": round(sd, 1),
            "z": round((score - mean) / sd, 1)}


def main():
    seqs = {a: fetch(a) for a in ACCS}
    al = aligner()
    out = {"lengths": {a: len(s) for a, s in seqs.items()}, "full_length": {}, "pombe_1_200": {}}
    q = seqs["O94400"]
    for t in ["Q06834", "Q9P1Y6", "C4QVX6"]:
        out["full_length"][f"O94400_vs_{t}"] = compare(al, q, seqs[t])
        out["pombe_1_200"][f"O94400[1-200]_vs_{t}"] = compare(al, q[:200], seqs[t])
    out["full_length"]["Q06834_vs_Q9P1Y6"] = compare(al, seqs["Q06834"], seqs["Q9P1Y6"])
    out["full_length"]["Q06834_vs_C4QVX6"] = compare(al, seqs["Q06834"], seqs["C4QVX6"])
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
