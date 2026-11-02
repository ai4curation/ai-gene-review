"""Global pairwise identity of maize LOC542140 (A0A804M424) to ZmGT1 (FJ573212 CDS)
and to Arabidopsis OPT family members AtOPT3 (O23482) and AtOPT6 (Q9T095).

Fetches sequences from UniProt / NCBI at run time; prints identity as % of query length.
Run: uv run python pairwise_identity.py
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fasta(url: str) -> str:
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if line and not line.startswith(">"))


UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.fasta"
NCBI_CDS = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore"
            "&id={}&rettype=fasta_cds_aa")

query = fasta(UNIPROT.format("A0A804M424"))
targets = {
    "ZmGT1 FJ573212 (ACL82964.1)": fasta(NCBI_CDS.format("FJ573212")),
    "AtOPT3 O23482": fasta(UNIPROT.format("O23482")),
    "AtOPT6 Q9T095": fasta(UNIPROT.format("Q9T095")),
}

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

print(f"query A0A804M424 length {len(query)}")
for name, seq in targets.items():
    aln = aligner.align(query, seq)[0]
    ident = sum(1 for i, j in zip(*aln.indices) if i >= 0 and j >= 0 and query[i] == seq[j])
    print(f"{name}\tlength {len(seq)}\tidentical {ident}\tidentity {100 * ident / len(query):.1f}%")
