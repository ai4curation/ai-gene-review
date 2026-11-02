# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Compare horse WDPCP gene models (all UniProt entries for Ensembl gene
ENSECAG00000019956) against human O95876 and mouse Q8C456.

Input: wdpcp_models.fasta, downloaded with
  curl "https://rest.uniprot.org/uniprotkb/stream?query=(gene:WDPCP+AND+organism_id:9796)+OR+accession:O95876+OR+accession:Q8C456&format=fasta"
Output: printed table (captured in RESULTS-rereview.md).
"""
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
recs = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse(HERE / "wdpcp_models.fasta", "fasta")}

aligner = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5, end_gap_score=0)
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")


def compare(query: str, ref: str) -> str:
    aln = aligner.align(recs[query], recs[ref])[0]
    pairs = ident = 0
    for (s1, e1), (s2, _e2) in zip(*aln.aligned):
        for k in range(e1 - s1):
            pairs += 1
            ident += recs[query][s1 + k] == recs[ref][s2 + k]
    ref_gaps, prev = [], 0
    for (_s1, _e1), (s2, e2) in zip(*aln.aligned):
        if s2 > prev:
            ref_gaps.append(f"{prev + 1}-{int(s2)}")
        prev = int(e2)
    if prev < len(recs[ref]):
        ref_gaps.append(f"{prev + 1}-{len(recs[ref])}")
    q_gaps, prev = [], 0
    for (s1, e1), (_s2, _e2) in zip(*aln.aligned):
        if s1 > prev:
            q_gaps.append(f"{prev + 1}-{int(s1)}")
        prev = int(e1)
    if prev < len(recs[query]):
        q_gaps.append(f"{prev + 1}-{len(recs[query])}")
    return (f"| {query} ({len(recs[query])}) | {ref} ({len(recs[ref])}) | {ident}/{pairs} = {ident / pairs:.3f} "
            f"| {', '.join(ref_gaps) or 'none'} | {', '.join(q_gaps) or 'none'} |")


print("| query | reference | identity | reference residues unaligned | query residues unaligned |")
print("|---|---|---|---|---|")
for acc in recs:
    if acc in ("O95876", "Q8C456"):
        continue
    for ref in ("O95876", "Q8C456"):
        print(compare(acc, ref))
print(compare("Q8C456", "O95876"))
print()
for acc in ("O95876", "Q8C456", "A0A3Q2KRK8", "A0A9L0R7M2", "A0A9L0T876"):
    print(f"{acc} last 30 residues: {recs[acc][-30:]}")
