# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Align donkey SNAP23 A0A8C4M333 to SNAP-25 family members fetched live from UniProt.

Usage (from this folder):
  uv run --script align_to_orthologs.py ../SNAP23__A0A8C4M333-uniprot.txt

Compares to human SNAP23 (O00161), mouse Snap23 (O09044) and human SNAP25 (P60880),
reporting global-alignment percent identity, and the donkey residues aligned to the human
SNAP23 cysteine-rich palmitoylation cluster and the N-terminal SNARE-motif Gln-48. Nothing is hardcoded
except the accession list and the human residue numbers queried.
"""
import sys
import requests
from Bio import Align
from Bio.Align import substitution_matrices

COMPARATORS = ["O00161", "O09044", "P60880"]
# human O00161 positions: Gln-48 (PMID:12556468) and the cysteine-rich cluster
QUERY_POSITIONS = [48, 79, 80, 83, 85, 87]


def read_uniprot_seq(path):
    seq, in_sq = [], False
    for line in open(path):
        if line.startswith("SQ"):
            in_sq = True
            continue
        if in_sq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", "").strip())
    return "".join(seq)


def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner():
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def main():
    donkey = read_uniprot_seq(sys.argv[1])
    print(f"donkey A0A8C4M333 length={len(donkey)}")
    al = aligner()
    for acc in COMPARATORS:
        other = fetch(acc)
        aln = al.align(donkey, other)[0]
        pairs = {}
        ident = aligned = 0
        for (ds, de), (os_, oe) in zip(*aln.aligned):
            for i, j in zip(range(ds, de), range(os_, oe)):
                pairs[j + 1] = i + 1
                aligned += 1
                ident += donkey[i] == other[j]
        print(f"{acc} length={len(other)} aligned={aligned} identical={ident} "
              f"pct_identity_over_shorter={100*ident/min(len(donkey),len(other)):.1f}")
        if acc == "O00161":
            print("  identical sequence" if donkey == other else "  sequences differ")
            for p in QUERY_POSITIONS:
                d = pairs.get(p)
                print(f"  human {other[p-1]}{p} -> donkey {donkey[d-1]+str(d) if d else 'gap'}")
            diffs = [f"{other[j-1]}{j}{donkey[i-1]}" for j, i in sorted(pairs.items()) if donkey[i-1] != other[j-1]]
            print(f"  substitutions vs human (human-pos-donkey): {' '.join(diffs) or 'none'}")


if __name__ == "__main__":
    main()
