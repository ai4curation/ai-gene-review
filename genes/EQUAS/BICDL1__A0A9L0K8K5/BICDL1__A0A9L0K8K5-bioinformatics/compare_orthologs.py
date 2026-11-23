# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Align donkey BICDL1 A0A9L0K8K5 to mouse A0JNT9 and human Q6ZP65.

Reports global-alignment identity, the position of the CC1 box (AARLG) and
the donkey residue aligned to mouse Lys512 (the K512M mutation abolishes Rab6
binding in mouse BICDR-1, PMID:20360680). Sequences are fetched live from UniProt.
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"donkey": "A0A9L0K8K5", "mouse": "A0JNT9", "human": "Q6ZP65"}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def pairs(aln):
    """Map positions (1-based) of seq A to seq B over aligned blocks."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(int(a1) - int(a0)):
            m[int(a0) + i + 1] = int(b0) + i + 1
    return m


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    out = {"lengths": {k: len(s) for k, s in seqs.items()}}
    out["cc1_box_AARLG"] = {k: (s.find("AARLG") + 1 or None) for k, s in seqs.items()}
    al = aligner()
    for other in ("mouse", "human"):
        aln = al.align(seqs["donkey"], seqs[other])[0]
        mp = pairs(aln)
        ident = sum(1 for d, o in mp.items() if seqs["donkey"][d - 1] == seqs[other][o - 1])
        out[f"donkey_vs_{other}"] = {
            "aligned_pairs": len(mp),
            "identical": ident,
            "pct_identity_over_aligned": round(100 * ident / len(mp), 2),
            "donkey_residues_unaligned": len(seqs["donkey"]) - len(mp),
        }
        if other == "mouse":
            rev = {o: d for d, o in mp.items()}
            k512 = rev.get(512)
            out["mouse_K512"] = {
                "mouse_residue": seqs["mouse"][511],
                "donkey_position": k512,
                "donkey_residue": seqs["donkey"][k512 - 1] if k512 else None,
                "donkey_context": seqs["donkey"][k512 - 6 : k512 + 5] if k512 else None,
                "mouse_context": seqs["mouse"][506:517],
            }
            # Donkey segments with no mouse counterpart (runs >= 10)
            runs, start = [], None
            for i in range(1, len(seqs["donkey"]) + 2):
                if i <= len(seqs["donkey"]) and i not in mp:
                    start = start or i
                elif start:
                    if i - start >= 10:
                        runs.append([start, i - 1, seqs["donkey"][start - 1 : i - 1]])
                    start = None
            out["donkey_insertions_vs_mouse"] = runs
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
