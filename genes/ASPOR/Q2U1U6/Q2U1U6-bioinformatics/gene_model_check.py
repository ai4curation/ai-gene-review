# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Gene-model check for Q2U1U6 (AO090138000091, A. oryzae RIB40).

1. Aligns Q2U1U6 to full-length section-Flavi orthologs (UniProt) to locate it.
2. Fetches the RIB40 genomic neighbourhood of the CDS (AP007170.1:187060..187464),
   translates all six frames and maps exact 8-mer peptides of the A. flavus
   ortholog (A0A7U2MCM8) onto the genome, to ask whether the N-terminal ~280 aa
   are encoded upstream (gene-model truncation) or absent.

Run: uv run gene_model_check.py
"""
import io
import requests
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner, substitution_matrices

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CDS_START, CDS_END = 187060, 187464
WIN = 12000
ORTHOLOGS = ["A0A7U2MCM8", "A0A5N6JAE3", "A0ABQ6LHX9", "Q4WKU8"]


def uniprot(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return next(SeqIO.parse(io.StringIO(r.text), "fasta"))


def main():
    q = uniprot("Q2U1U6")
    aligner = PairwiseAligner(mode="local")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -11, -1
    print("## Q2U1U6 vs full-length orthologs")
    print(f"Q2U1U6 length: {len(q.seq)}")
    for acc in ORTHOLOGS:
        s = uniprot(acc)
        aln = aligner.align(str(q.seq), str(s.seq))[0]
        qb, sb = aln.aligned
        ident = sum(
            1
            for (a0, a1), (b0, b1) in zip(qb, sb)
            for i, j in zip(range(a0, a1), range(b0, b1))
            if q.seq[i] == s.seq[j]
        )
        alen = sum(a1 - a0 for a0, a1 in qb)
        print(
            f"{acc} len={len(s.seq)} query {qb[0][0]+1}-{qb[-1][1]} "
            f"subject {sb[0][0]+1}-{sb[-1][1]} identity {ident}/{alen} "
            f"| {s.description[:90]}"
        )

    start, stop = CDS_START - WIN, CDS_END + 2000
    r = requests.get(
        EUTILS,
        params=dict(db="nuccore", id="AP007170.1", rettype="fasta",
                    retmode="text", seq_start=start, seq_stop=stop),
        timeout=60,
    )
    r.raise_for_status()
    g = next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq
    print(f"\n## Genomic window AP007170.1:{start}-{stop} ({len(g)} nt)")
    fl = str(uniprot("A0A7U2MCM8").seq)
    k = 8
    frames = []
    for strand, nuc in (("+", g), ("-", g.reverse_complement())):
        for f in range(3):
            sub = nuc[f:]
            sub = sub[: len(sub) - len(sub) % 3]
            frames.append((strand, f, str(Seq(sub).translate())))
    hits = []
    for pos in range(0, len(fl) - k + 1):
        pep = fl[pos : pos + k]
        for strand, f, prot in frames:
            idx = prot.find(pep)
            if idx >= 0:
                if strand == "+":
                    nt = start + f + idx * 3
                else:
                    nt = stop - (f + idx * 3)
                hits.append((pos + 1, strand, f, nt))
                break
    covered = sorted({h[0] for h in hits})
    print(f"A0A7U2MCM8 8-mers with exact genomic match: {len(covered)} of {len(fl)-k+1}")
    # summarise contiguous blocks of ortholog positions
    blocks = []
    for h in hits:
        if blocks and h[0] - blocks[-1][1] <= k and h[1:3] == blocks[-1][2]:
            blocks[-1][1] = h[0]
            blocks[-1][4] = h[3]
        else:
            blocks.append([h[0], h[0], h[1:3], h[3], h[3]])
    for b0, b1, (strand, f), n0, n1 in blocks:
        print(f"  ortholog aa {b0}-{b1+k-1}  strand {strand} frame {f}  genome ~{n0}-{n1}")
    print(
        "N-terminal region (ortholog aa 1-279) matched: "
        f"{sum(1 for p in covered if p < 280)} 8-mers"
    )
    junction_check(str(g), start)


def junction_check(gs, start):
    """Find a GT..AG intron joining exon 1 (ends ...EAGRDQ + G1 of Gly279) to the
    codon-phase-2 remainder of Gly279 followed by His280 (CAC ACC ATG TCG = HTMS)."""
    exon1_end_motif = "GAAGCGGGGCGTGATCAAG"  # E A G R D Q + first nt of G
    i = gs.find(exon1_end_motif)
    donor = i + len(exon1_end_motif)  # 0-based index of intron's first nt
    h = gs.find("CACACCATGTCG", donor)  # H T M S (exon 2)
    # the two nt before CAC complete the Gly codon; intron ends just before them
    acceptor_end = h - 2  # exclusive
    intron = gs[donor:acceptor_end]
    print("\n## Exon1/exon2 junction (RIB40 genome)")
    print(f"exon1 ends at genomic {start + donor - 1}; intron {start + donor}-{start + acceptor_end - 1}"
          f" length {len(intron)}; starts {intron[:2]} ends {intron[-2:]}")
    print(f"intron sequence: {intron}")
    print(f"reconstituted Gly codon: {gs[donor-1]}{gs[acceptor_end:acceptor_end+2]}"
          f" -> {Seq(gs[donor-1] + gs[acceptor_end:acceptor_end+2]).translate()}")
    print(f"annotated CDS start (ATG at {CDS_START}) lies inside this intron: "
          f"{start + donor <= CDS_START <= start + acceptor_end - 1}")


if __name__ == "__main__":
    main()
