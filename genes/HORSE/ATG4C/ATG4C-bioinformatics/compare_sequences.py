# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Compare horse ATG4C gene model A0A3Q2H6C4 with human ATG4C (Q96DT6) and donkey A0A9L0IIU3.

Reads sequences from UniProt flat files in the repository; prints identity, coverage,
unpaired segments, and mapping of human catalytic residues (C111, D345, H347) and
the human C-terminal LIR region.
"""
import json
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "horse": ROOT / "genes/HORSE/ATG4C/ATG4C-uniprot.txt",
    "human": ROOT / "genes/EQUAS/ATG4C/ATG4C-bioinformatics/human_Q96DT6-uniprot.txt",
    "donkey": ROOT / "genes/EQUAS/ATG4C/ATG4C-uniprot.txt",
}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("SQ "))
    seq = []
    for l in lines[start + 1 :]:
        if l.startswith("//"):
            break
        seq.append(l.replace(" ", ""))
    return "".join(seq)


def align(a: str, b: str):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al.align(a, b)[0]


def pairs(aln):
    """Map query index -> target index for aligned positions."""
    m = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned.tolist()):
        for k in range(qe - qs):
            m[int(qs) + k] = int(ts) + k
    return m


def unpaired(n, paired_idx, minlen=5):
    segs, run = [], []
    for i in range(n):
        if i not in paired_idx:
            run.append(i)
        else:
            if len(run) >= minlen:
                segs.append((run[0] + 1, run[-1] + 1))
            run = []
    if len(run) >= minlen:
        segs.append((run[0] + 1, run[-1] + 1))
    return segs


seqs = {k: read_seq(v) for k, v in FILES.items()}
out = {"lengths": {k: len(v) for k, v in seqs.items()}, "comparisons": {}}
human = seqs["human"]
for other in ("horse", "donkey"):
    aln = align(human, seqs[other])
    m = pairs(aln)
    ident = sum(1 for h, o in m.items() if human[h] == seqs[other][o])
    rev = set(m.values())
    sites = {}
    for label, pos in (("C111 nucleophile", 111), ("D345", 345), ("H347", 347)):
        o = m.get(pos - 1)
        sites[label] = f"{human[pos-1]}{pos} -> " + (f"{seqs[other][o]}{o+1}" if o is not None else "gap")
    out["comparisons"][other] = {
        "paired": len(m),
        "identity_over_paired_pct": round(100 * ident / len(m), 2),
        "human_coverage_pct": round(100 * len(m) / len(human), 2),
        "other_coverage_pct": round(100 * len(m) / len(seqs[other]), 2),
        "human_unpaired_segments": unpaired(len(human), set(m)),
        "other_unpaired_segments": unpaired(len(seqs[other]), rev),
        "catalytic_sites": sites,
        "human_last_paired": max(m) + 1,
        "other_pos_aligned_to_human_last_paired": m[max(m)] + 1,
    }
# identity of horse vs donkey over the first 458 / whole
aln = align(seqs["donkey"], seqs["horse"])
m = pairs(aln)
ident = sum(1 for d, h in m.items() if seqs["donkey"][d] == seqs["horse"][h])
out["comparisons"]["donkey_vs_horse"] = {
    "paired": len(m),
    "identity_over_paired_pct": round(100 * ident / len(m), 2),
    "horse_unpaired_segments": unpaired(len(seqs["horse"]), set(m.values())),
    "donkey_unpaired_segments": unpaired(len(seqs["donkey"]), set(m)),
}
out["human_Cterm_30"] = human[-30:]
out["horse_region_430_470"] = seqs["horse"][429:470]


def windowed_identity(a: str, b: str, start: int, end: int, win: int = 50):
    """Ungapped per-window identity of a[start:end] vs b[start:end] (1-based report)."""
    rows = []
    for s in range(start, end, win):
        e = min(s + win, end)
        same = sum(1 for i in range(s, e) if a[i] == b[i])
        rows.append({"window": f"{s+1}-{e}", "identity_pct": round(100 * same / (e - s), 1)})
    return rows


def local_hit(query: str, target: str):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "local"
    aln = al.align(query, target)[0]
    return {"score": float(aln.score), "query_span": [int(aln.aligned[0][0][0]) + 1, int(aln.aligned[0][-1][1])],
            "target_span": [int(aln.aligned[1][0][0]) + 1, int(aln.aligned[1][-1][1])]}


extra = {
    "ungapped_horse_vs_human_1_458": windowed_identity(seqs["horse"], human, 0, 458),
    "human_tail_404_458": human[403:],
    "horse_tail_404_666": seqs["horse"][403:],
    "local_hit_human_tail_404_458_in_horse_404_666": local_hit(human[403:], seqs["horse"][403:]),
}
out.update(extra)
print(json.dumps(out, indent=2))
