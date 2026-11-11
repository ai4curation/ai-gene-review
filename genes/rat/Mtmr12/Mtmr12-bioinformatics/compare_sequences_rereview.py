# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review comparison of rat Mtmr12 TrEMBL product A0A8I5ZMD5 against the
Swiss-Prot canonical rat Q5FVM6 and the human/mouse orthologs (same PANTHER
subfamily PTHR10807:SF37). Sequences are fetched live from UniProt REST.

Reports: lengths, global-alignment identity blocks, the N-terminal segment
that differs, its Kyte-Doolittle hydropathy, and conservation of the
myotubularin catalytic-motif region (CX5R in active members) across products.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "A0A8I5ZMD5": "rat TrEMBL product (benchmark)",
    "Q5FVM6": "rat Swiss-Prot canonical",
    "Q80TA6": "mouse Swiss-Prot",
    "Q9C0I1": "human Swiss-Prot",
    "Q13496": "human MTM1 (active paralog, comparator)",
}

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def max_kd_window(seq: str, w: int = 11) -> tuple[float, int]:
    best = (-99.0, 0)
    for i in range(len(seq) - w + 1):
        v = sum(KD.get(a, 0) for a in seq[i:i + w]) / w
        if v > best[0]:
            best = (round(v, 2), i + 1)
    return best


def blocks(aln):
    out = []
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        ident = sum(1 for a, b in zip(aln.target[s1:e1], aln.query[s2:e2]) if a == b)
        out.append({"target": [int(s1) + 1, int(e1)], "query": [int(s2) + 1, int(e2)], "identical": ident})
    return out


def main():
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    res = {"lengths": {a: len(s) for a, s in seqs.items()}, "pairs": {}}
    sel = seqs["A0A8I5ZMD5"]
    for ref in ["Q5FVM6", "Q80TA6", "Q9C0I1"]:
        aln = aligner.align(seqs[ref], sel)[0]
        b = blocks(aln)
        res["pairs"][f"{ref}_vs_A0A8I5ZMD5"] = b
    res["n_terminus"] = {a: seqs[a][:60] for a in ["A0A8I5ZMD5", "Q5FVM6", "Q80TA6", "Q9C0I1"]}
    res["max_kd_11_first40"] = {a: max_kd_window(seqs[a][:40]) for a in
                                ["A0A8I5ZMD5", "Q5FVM6", "Q80TA6", "Q9C0I1"]}
    # catalytic motif region: locate MTM1 CX5R (CSDGWDR) and the aligned segment in each MTMR12
    mtm1 = seqs["Q13496"]
    cpos = mtm1.find("CSDGWDR")
    res["mtm1_cx5r_pos"] = cpos + 1
    motif = {}
    for a in ["A0A8I5ZMD5", "Q5FVM6", "Q9C0I1"]:
        aln = aligner.align(mtm1, seqs[a])[0]
        # map MTM1 cpos..cpos+7 to target
        seg = []
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for k in range(s1, e1):
                if cpos <= k < cpos + 7:
                    seg.append(seqs[a][s2 + (k - s1)])
        motif[a] = "".join(seg)
    res["aligned_to_MTM1_CSDGWDR"] = motif
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
