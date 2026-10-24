# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Re-review sequence analysis for zebrafish dcxr (Q567K5).

Fetches sequences directly from UniProt REST (independent of any prediction
files), computes pairwise global identities between Q567K5 and characterised
PTHR44252 members from subfamilies SF1, SF2 and SF3, and maps the human DCXR
(Q7Z4W1) catalytic triad and Rossmann glycine motif onto each sequence.

Run: uv run --script compare_sequences_rereview.py > RESULTS-rereview.raw.txt
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

# accession -> (label, PANTHER subfamily as given in PANTHER 19.0 classification files)
MEMBERS = {
    "Q567K5": ("zebrafish dcxr (target)", "SF3"),
    "Q7Z4W1": ("human DCXR", "SF2"),
    "Q91X52": ("mouse Dcxr", "SF2"),
    "Q920P0": ("rat Dcxr", "SF2"),
    "Q8JIS3": ("chicken DER D-erythrulose reductase", "SF3"),
    "Q6P630": ("Xenopus tropicalis dcxr", "SF3"),
    "Q21929": ("C. elegans dhs-21", "SF3"),
    "Q9VWP2": ("Drosophila CG7322", "SF3"),
    "P08074": ("mouse Cbr2", "SF1"),
}
HUMAN_SITES = {136: "S", 149: "Y", 153: "K"}  # UniProt Q7Z4W1 active-site features


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def identity(aln) -> tuple[int, int]:
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    return sum(x == y for x, y in cols), len(cols)


def map_positions(aln, ref_positions):
    """Map 1-based positions in aln target (seq 0) to residues in query (seq 1)."""
    out = {}
    t_idx = q_idx = 0
    for x, y in zip(aln[0], aln[1]):
        if x != "-":
            t_idx += 1
        if y != "-":
            q_idx += 1
        if x != "-" and t_idx in ref_positions:
            out[t_idx] = (y, q_idx if y != "-" else None)
    return out


def main() -> None:
    seqs = {acc: fetch(acc) for acc in MEMBERS}
    al = aligner()
    target = seqs["Q567K5"]
    print("## Q567K5 versus PTHR44252 members (global BLOSUM62, open -10, extend -0.5)\n")
    print("| Accession | Protein | Subfamily | Length | Identical / aligned | % identity |")
    print("|---|---|---|---|---|---|")
    for acc, (label, sf) in MEMBERS.items():
        if acc == "Q567K5":
            continue
        aln = al.align(target, seqs[acc])[0]
        ident, cols = identity(aln)
        print(f"| {acc} | {label} | {sf} | {len(seqs[acc])} | {ident} / {cols} | {100*ident/cols:.1f} |")
    print("\n## Human DCXR catalytic triad mapped onto each sequence\n")
    print("| Accession | S136 | Y149 | K153 |")
    print("|---|---|---|---|")
    for acc in MEMBERS:
        if acc == "Q7Z4W1":
            continue
        aln = al.align(seqs["Q7Z4W1"], seqs[acc])[0]
        m = map_positions(aln, HUMAN_SITES)
        cells = []
        for pos, ref in HUMAN_SITES.items():
            res, qpos = m[pos]
            cells.append(f"{res}{qpos}" + ("" if res == ref else " (changed)"))
        print(f"| {acc} | " + " | ".join(cells) + " |")
    print("\n## Rossmann TGxxxGxG motif (first 25 residues)\n")
    for acc in MEMBERS:
        print(f"- {acc}: {seqs[acc][:25]}")


if __name__ == "__main__":
    main()
