# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare horse BICDL1 (F6SAQ3) with characterised SF12 orthologs.

Fetches sequences from UniProt REST, does global alignments (BLOSUM62),
reports identity/coverage, and maps functionally characterised residues
(mouse BICDR-1 K512, Rab6-binding; W166 coiled-coil registry marker in
Chaaban & Carter 2022, which used mouse BICDR1) onto the horse sequence.
Writes results.json beside this script.
"""
import json
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "horse_F6SAQ3": "F6SAQ3",
    "human_Q6ZP65": "Q6ZP65",
    "human_Q6ZP65-2": "Q6ZP65-2",
    "mouse_A0JNT9": "A0JNT9",
    "zebrafish_P0CF95": "P0CF95",
    "human_BICDL2_A1A5D9": "A1A5D9",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def align(a: str, b: str):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al.align(a, b)[0]


def stats(aln, la: int, lb: int) -> dict:
    ident = paired = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            paired += 1
            ident += aln.target[i] == aln.query[j]
    return {
        "len_horse": la,
        "len_other": lb,
        "paired": paired,
        "identical": ident,
        "pct_identity_over_paired": round(100 * ident / paired, 2),
        "pct_horse_covered": round(100 * paired / la, 2),
        "pct_other_covered": round(100 * paired / lb, 2),
    }


def map_pos(aln, other_pos1: int):
    """Map a 1-based position in the other sequence to horse (1-based)."""
    j0 = other_pos1 - 1
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        if s2 <= j0 < e2:
            return int(s1 + (j0 - s2) + 1)
    return None


def unpaired_segments(aln, which: str, min_len: int = 5):
    """Segments in horse (target) or other (query) with no aligned partner."""
    blocks = aln.aligned[0] if which == "horse" else aln.aligned[1]
    seqlen = len(aln.target) if which == "horse" else len(aln.query)
    segs, prev = [], 0
    for s, e in blocks:
        if s - prev >= min_len:
            segs.append([int(prev) + 1, int(s)])
        prev = e
    if seqlen - prev >= min_len:
        segs.append([int(prev) + 1, int(seqlen)])
    return segs


def main():
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    horse = seqs["horse_F6SAQ3"]
    out = {"lengths": {k: len(v) for k, v in seqs.items()}, "pairs": {}}
    for k, s in seqs.items():
        if k == "horse_F6SAQ3":
            continue
        aln = align(horse, s)
        d = stats(aln, len(horse), len(s))
        d["horse_unpaired_segments"] = unpaired_segments(aln, "horse")
        d["other_unpaired_segments"] = unpaired_segments(aln, "other")
        out["pairs"][k] = d
        if k == "mouse_A0JNT9":
            res = {}
            for label, pos in {"K512_Rab6_binding": 512, "W166_coiled_coil": 166}.items():
                hp = map_pos(aln, pos)
                res[label] = {
                    "mouse_residue": s[pos - 1],
                    "horse_position": hp,
                    "horse_residue": horse[hp - 1] if hp else None,
                }
            out["mouse_residue_mapping"] = res
            (Path(__file__).parent / "alignment_horse_mouse.txt").write_text(str(aln))
        if k == "human_Q6ZP65":
            (Path(__file__).parent / "alignment_horse_human.txt").write_text(str(aln))
    (Path(__file__).parent / "results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
