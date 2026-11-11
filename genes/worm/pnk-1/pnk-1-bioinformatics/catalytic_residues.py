"""Map PANK catalytic residues (human PANK3 Glu138, Arg207; Yao et al. 2019) onto
C. elegans PNK-1 (H2KYP7) and PNK-4 (Q18580), and report alignment coverage
against human PANK4 (Q9NVE7, kinase-like domain + C-terminal DUF89 phosphatase domain).

Run from the repository root:  uv run python genes/worm/pnk-1/pnk-1-bioinformatics/catalytic_residues.py
Sequences are downloaded live from the UniProt REST API.
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

ACCS = {
    "H2KYP7": "C. elegans PNK-1",
    "Q18580": "C. elegans PNK-4",
    "Q9H999": "human PANK3",
    "Q8TE04": "human PANK1",
    "Q9BZ23": "human PANK2",
    "Q9NVE7": "human PANK4",
}


def fetch(acc):
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as fh:
        return str(next(SeqIO.parse(io.StringIO(fh.read().decode()), "fasta")).seq)


def aligner():
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "local"
    return al


def map_pos(aln, ref_pos):
    """Return 1-based query position aligned to 1-based ref position (target index 1)."""
    q, t = aln.indices
    for qi, ti in zip(q, t):
        if ti == ref_pos - 1:
            return qi + 1 if qi >= 0 else None
    return None


def main():
    seqs = {a: fetch(a) for a in ACCS}
    al = aligner()
    print("## Lengths")
    for a, n in ACCS.items():
        print(f"{a}\t{n}\t{len(seqs[a])} aa")
    print("\n## PNK-1 (H2KYP7) local alignment identity to human PANKs")
    for ref in ["Q8TE04", "Q9BZ23", "Q9H999", "Q9NVE7"]:
        aln = al.align(seqs["H2KYP7"], seqs[ref])[0]
        s1, s2 = aln[0], aln[1]
        pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
        ident = sum(1 for x, y in pairs if x == y)
        qs, qe = aln.aligned[0][0][0] + 1, aln.aligned[0][-1][1]
        ts, te = aln.aligned[1][0][0] + 1, aln.aligned[1][-1][1]
        print(f"{ACCS[ref]}\tidentity {ident}/{len(pairs)} = {ident/len(pairs):.3f}\t"
              f"PNK-1 {qs}-{qe} vs {ref} {ts}-{te}")
    print("\n## Catalytic residues (human PANK3 numbering)")
    for q in ["H2KYP7", "Q18580", "Q9NVE7", "Q8TE04", "Q9BZ23"]:
        aln = al.align(seqs[q], seqs["Q9H999"])[0]
        out = []
        for ref_pos in (138, 207):
            p = map_pos(aln, ref_pos)
            out.append(f"PANK3 {seqs['Q9H999'][ref_pos-1]}{ref_pos} -> "
                       f"{seqs[q][p-1] + str(p) if p else 'gap'}")
        print(f"{ACCS[q]} ({q}):\t" + "; ".join(out))


if __name__ == "__main__":
    main()
