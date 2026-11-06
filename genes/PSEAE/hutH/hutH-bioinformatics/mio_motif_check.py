"""Check the MIO-forming Ala-Ser-Gly motif and pairwise identity of PAO1 HutH (PA5098),
the HutH-like paralog PA5093, and the structurally characterised P. putida HutH (P21310).

Usage: uv run python mio_motif_check.py
Fetches sequences from the UniProt REST API; prints results (nothing is hardcoded).
"""
import urllib.request

from Bio.Align import PairwiseAligner, substitution_matrices

ACCS = {"PA5098_hutH": "Q9HU85", "PA5093_HutH-like": "Q9HU90", "Pputida_hutH": "P21310"}


def fetch(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as fh:
        lines = fh.read().decode().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def identity(a: str, b: str) -> float:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
    aln = al.align(a, b)[0]
    same = sum(
        1
        for (s1, e1), (s2, e2) in zip(*aln.aligned)
        for i in range(e1 - s1)
        if a[s1 + i] == b[s2 + i]
    )
    return same / min(len(a), len(b))


def window_at(query: str, ref: str, ref_start: int, ref_end: int) -> str:
    """Residues of query aligned to ref[ref_start:ref_end] (0-based)."""
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
    aln = al.align(ref, query)[0]
    out = []
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i in range(e1 - s1):
            if ref_start <= s1 + i < ref_end:
                out.append(f"{query[s2 + i]}{s2 + i + 1}")
    return " ".join(out) or "(gap)"


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    for k, s in seqs.items():
        pos = s.find("ASG")
        print(f"{k} ({ACCS[k]}): length {len(s)}; first 'ASG' at {pos + 1 if pos >= 0 else 'absent'}")
    ref = seqs["Pputida_hutH"]
    rpos = ref.find("ASG")
    print(f"P. putida MIO motif positions: {rpos + 1}-{rpos + 3}")
    for k in ("PA5098_hutH", "PA5093_HutH-like"):
        print(f"{k} residues aligned to P. putida MIO motif: {window_at(seqs[k], ref, rpos, rpos + 3)}")
    names = list(seqs)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            print(f"identity {names[i]} vs {names[j]}: {identity(seqs[names[i]], seqs[names[j]]):.3f}")


if __name__ == "__main__":
    main()
