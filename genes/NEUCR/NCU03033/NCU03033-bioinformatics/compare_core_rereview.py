# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare the NF-YA/Hap2 essential core of Q7SGY4 (NCU03033) with characterized
PTHR12632 members: S. cerevisiae HAP2 (P06774), human NFYA (P23511) and
S. pombe php2 (P24488). Sequences are fetched live from UniProt REST.

The core is located in each sequence by a local alignment against the Q7SGY4
region spanning the UniProt-annotated subunit-association motif (194-217) and
NFYA/HAP2-type DNA-binding region (225-250), i.e. Q7SGY4 residues 190-255.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q7SGY4": "NCU03033", "P06774": "HAP2_YEAST", "P23511": "NFYA_HUMAN", "P24488": "php2_SCHPO"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
query = seqs["Q7SGY4"]
core = query[189:255]  # 1-based 190..255
print(f"Q7SGY4 length {len(query)}; core 190-255: {core}")

aligner = Align.PairwiseAligner()
aligner.mode = "local"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5

for acc, name in ACCS.items():
    if acc == "Q7SGY4":
        continue
    aln = aligner.align(core, seqs[acc])[0]
    ident = sum(1 for (qs, qe), (ts, te) in zip(*aln.aligned) for i in range(qe - qs) if core[qs + i] == seqs[acc][ts + i])
    alnlen = sum(qe - qs for qs, qe in aln.aligned[0])
    tstart = aln.aligned[1][0][0] + 1
    tend = aln.aligned[1][-1][1]
    print(f"\n{name} ({acc}, length {len(seqs[acc])}): core aligns to {tstart}-{tend}; "
          f"identity {ident}/{alnlen} = {100*ident/alnlen:.1f}%")
    print(aln)
