# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Characterise the horse WDPCP Ensembl canonical product A0A9L0T876.

Steps (all fetched live; nothing hard-coded except accessions/stable ids):
1. Download protein sequences of A0A9L0T876 (ENSECAT00000134648), A0A9L0R7M2
   (ENSECAT00000123939, the model colinear with human/mouse at both ends),
   human O95876 and mouse Q8C456 from UniProt REST; save to sequences.fasta.
2. Identical prefix with A0A9L0R7M2, and global BLOSUM62 alignment against
   human and mouse; report where the colinear region ends.
3. Map the human S708 residue (inside the PIP-binding C-terminal tail of
   PMID:35427153) and the human last-60-residue window onto A0A9L0T876.
4. Fetch Ensembl exon structures of both horse transcripts and report which
   exons are shared, and the genomic location of the A0A9L0T876 terminal exon
   relative to the A0A9L0R7M2 exons.
Output: printed report, captured in output.txt.
"""
from io import StringIO

import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

ACCS = ["A0A9L0T876", "A0A9L0R7M2", "O95876", "Q8C456"]
TX = {"A0A9L0T876": "ENSECAT00000134648", "A0A9L0R7M2": "ENSECAT00000123939"}

fasta = "".join(
    requests.get(f"https://rest.uniprot.org/uniprotkb/{a}.fasta", timeout=60).text for a in ACCS
)
open("sequences.fasta", "w").write(fasta)
seqs = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse(StringIO(fasta), "fasta")}

aligner = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5, end_gap_score=0)
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")


def main_block_end(q: str, r: str) -> tuple[int, int, int]:
    """End (1-based query, reference) of the longest aligned block, and its length.

    Short scattered blocks after it are free-end-gap noise in an unrelated tail.
    """
    aln = aligner.align(seqs[q], seqs[r])[0]
    blocks = list(zip(*aln.aligned))
    (qs, qe), (rs, re_) = max(blocks, key=lambda b: b[0][1] - b[0][0])
    return int(qe), int(re_), int(qe - qs)


q = "A0A9L0T876"
print(f"{q} length {len(seqs[q])}")
t, r7 = seqs[q], seqs["A0A9L0R7M2"]
prefix = next(i for i in range(min(len(t), len(r7))) if t[i] != r7[i])
print(f"identical prefix with A0A9L0R7M2: residues 1-{prefix}; then {q} has {len(t) - prefix} novel residues "
      f"and A0A9L0R7M2 has {len(r7) - prefix} residues not present in {q}")
print(f"  {q} {prefix + 1}-{len(t)}: {t[prefix:]}")
print(f"  A0A9L0R7M2 {prefix + 1}-{len(r7)}: {r7[prefix:]}")
for ref in ["O95876", "Q8C456"]:
    qe, re_, ln = main_block_end(q, ref)
    print(f"vs {ref} ({len(seqs[ref])} aa): longest aligned block ({ln} residues) ends at {q} {qe} = {ref} {re_}; "
          f"{ref} residues after it: {len(seqs[ref]) - re_}")
    if ref == "O95876":
        tail_start = len(seqs[ref]) - 59
        print(f"  human last-60 PIP-binding window = O95876 {tail_start}-{len(seqs[ref])}; residues of it within "
              f"the colinear block: {max(0, re_ - tail_start + 1)}; S708 (residue {seqs[ref][707]}) inside block: "
              f"{708 <= re_}")

# Ensembl exon structures
exons = {}
for acc, tx in TX.items():
    d = requests.get(
        f"https://rest.ensembl.org/lookup/id/{tx}?expand=1",
        headers={"Content-Type": "application/json"},
        timeout=60,
    ).json()
    exons[acc] = [(e["start"], e["end"]) for e in sorted(d["Exon"], key=lambda e: e["start"])]
    print(f"{acc} {tx}: {len(exons[acc])} exons, span {exons[acc][0][0]}-{exons[acc][-1][1]} (strand {d['strand']})")
shared = set(exons["A0A9L0T876"]) & set(exons["A0A9L0R7M2"])
print(f"exons with identical coordinates in both: {len(shared)}")
only_t = [e for e in exons["A0A9L0T876"] if e not in shared]
print(f"A0A9L0T876-specific exons (start,end): {only_t}")
r_ex = exons["A0A9L0R7M2"]
for s, e in only_t:
    up = [x for x in r_ex if x[1] < s]
    dn = [x for x in r_ex if x[0] > e]
    overl = [x for x in r_ex if x[0] <= e and x[1] >= s]
    where = (f"overlaps A0A9L0R7M2 exon(s) {overl}" if overl else
             f"lies in the A0A9L0R7M2 intron between exon ending {up[-1][1] if up else None} "
             f"and exon starting {dn[0][0] if dn else None}")
    print(f"  exon {s}-{e}: {where}; A0A9L0R7M2 exons downstream of it: {len(dn)}")
