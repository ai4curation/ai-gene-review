"""Compare CG8353 (Q9VLR2) with characterised PANTHER PTHR11644:SF2 cytidine deaminases.

Fetches sequences from UniProt REST and NCBI (RefSeq isoforms), performs global
pairwise alignments (BLOSUM62) against human CDA (P32320), and reports identity
and the residues aligned to the human CDA catalytic positions taken from the
curated P32320 UniProt features (Zn ligands C65, C99, C102; proton donor E67;
substrate-binding loop 54-60).

Run: uv run --with biopython --with requests python compare_cda_sf2.py
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCESSIONS = {
    "P32320": "human CDA",
    "P56389": "mouse Cda",
    "Q06549": "yeast CDD1",
    "P0ABF6": "E. coli cdd",
    "Q9VLR2": "fly CG8353 (target)",
    "Q9VLR3": "fly CG8360 (paralog)",
    "Q7KTJ2": "fly CG8349 (paralog)",
}
REFSEQ = ["NP_609196.1", "NP_001260233.1"]
HUMAN_SITES = {54: "loop start", 60: "loop end", 65: "Zn (C)", 67: "proton donor (E)",
               99: "Zn (C)", 102: "Zn (C)"}


def uniprot_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def refseq_seq(acc: str) -> str:
    r = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
        params={"db": "protein", "id": acc, "rettype": "fasta", "retmode": "text"},
        timeout=60,
    )
    r.raise_for_status()
    return "".join(r.text.strip().splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def map_positions(aln, ref_positions):
    """Map 1-based positions in sequence 0 (reference) to sequence 1."""
    out = {}
    for (r0, r1), (q0, q1) in zip(*aln.aligned):
        for p in ref_positions:
            if r0 < p <= r1:
                out[p] = q0 + (p - r0)
    return out


def identity(aln) -> tuple[float, int]:
    s0, s1 = aln[0], aln[1]
    pairs = [(a, b) for a, b in zip(s0, s1) if a != "-" and b != "-"]
    ident = sum(1 for a, b in pairs if a == b)
    return 100.0 * ident / len(pairs), len(pairs)


def main() -> None:
    seqs = {acc: uniprot_seq(acc) for acc in ACCESSIONS}
    print("## Sequence lengths")
    for acc, name in ACCESSIONS.items():
        print(f"{acc}\t{name}\t{len(seqs[acc])} aa")
    print("\n## FlyBase/RefSeq CG8353 protein products vs Q9VLR2")
    for rs in REFSEQ:
        s = refseq_seq(rs)
        print(f"{rs}\t{len(s)} aa\tidentical_to_Q9VLR2={s == seqs['Q9VLR2']}")
    ref = seqs["P32320"]
    al = aligner()
    print("\n## Pairwise global alignment to human CDA P32320")
    print("acc\tname\tpct_identity\taligned_cols\t" + "\t".join(
        f"h{p}:{ref[p-1]}" for p in HUMAN_SITES))
    for acc, name in ACCESSIONS.items():
        if acc == "P32320":
            continue
        aln = al.align(ref, seqs[acc])[0]
        pid, n = identity(aln)
        m = map_positions(aln, HUMAN_SITES)
        cells = []
        for p in HUMAN_SITES:
            q = m.get(p)
            cells.append(f"{seqs[acc][q-1]}{q}" if q else "gap")
        print(f"{acc}\t{name}\t{pid:.1f}\t{n}\t" + "\t".join(cells))
    print("\n## Pairwise identity among fly SF2 paralogs")
    fly = ["Q9VLR2", "Q9VLR3", "Q7KTJ2"]
    for i, a in enumerate(fly):
        for b in fly[i + 1:]:
            pid, n = identity(al.align(seqs[a], seqs[b])[0])
            print(f"{a}\t{b}\t{pid:.1f}\t{n}")


if __name__ == "__main__":
    main()
