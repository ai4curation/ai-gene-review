# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global/local alignment of A0A8C9H4D2 (Piliocolobus OLFML2A gene model) against
human OLFML2A Q68BL7, reading sequences from the cached UniProt flat files.

Run from the repository root:
    uv run genes/9PRIM/A0A8C9H4D2/A0A8C9H4D2-bioinformatics/compare_to_human.py
"""
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    i = next(n for n, line in enumerate(lines) if line.startswith("SQ   "))
    seq = []
    for line in lines[i + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


query = read_seq(ROOT / "genes/9PRIM/A0A8C9H4D2/A0A8C9H4D2-uniprot.txt")
human = read_seq(ROOT / "genes/human/OLFML2A/OLFML2A-uniprot.txt")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "local"
aln = aligner.align(query, human)[0]

qblocks, hblocks = aln.aligned
q_start, q_end = qblocks[0][0], qblocks[-1][1]
h_start, h_end = hblocks[0][0], hblocks[-1][1]
ident = sum(
    1
    for (qs, qe), (hs, he) in zip(qblocks, hblocks)
    for a, b in zip(query[qs:qe], human[hs:he])
    if a == b
)
aligned_len = sum(qe - qs for qs, qe in qblocks)

print(f"query length: {len(query)}")
print(f"human Q68BL7 length: {len(human)}")
print(f"local alignment query {q_start + 1}-{q_end}, human {h_start + 1}-{h_end}")
print(f"identical positions: {ident} / {aligned_len} aligned query residues "
      f"({100 * ident / aligned_len:.1f}%)")
print(f"human residues before alignment start (absent from query): {h_start}")
print(f"human residues after alignment end (absent from query): {len(human) - h_end}")
print(f"query residues before alignment start (no human counterpart): {q_start}")
print(f"query N-terminal 30 aa: {query[:30]}")
print(f"human N-terminal 30 aa: {human[:30]}")
cys_human = [i + 1 for i, c in enumerate(human[: h_start]) if c == "C"]
print(f"cysteines in the human region missing from query: {len(cys_human)} {cys_human}")
print(aln)

# Same-gene full-length product (Ensembl ENSPTEG00000015637, isoform X1),
# downloaded with: curl -s https://rest.uniprot.org/uniprotkb/A0A8C9H9A8.txt
full = read_seq(Path(__file__).resolve().parent / "A0A8C9H9A8-uniprot.txt")
aln2 = aligner.align(query, full)[0]
qb2, fb2 = aln2.aligned
id2 = sum(1 for (qs, qe), (fs, fe) in zip(qb2, fb2)
          for a, b in zip(query[qs:qe], full[fs:fe]) if a == b)
al2 = sum(qe - qs for qs, qe in qb2)
print(f"A0A8C9H9A8 length: {len(full)}")
print(f"local alignment vs A0A8C9H9A8: query {qb2[0][0] + 1}-{qb2[-1][1]}, "
      f"A0A8C9H9A8 {fb2[0][0] + 1}-{fb2[-1][1]}; identical {id2}/{al2} "
      f"({100 * id2 / al2:.1f}%)")
print(f"A0A8C9H9A8 residues before alignment start (absent from query): {fb2[0][0]}")
print(f"A0A8C9H9A8 N-terminal 30 aa: {full[:30]}")
# Human isoform 3 (Q68BL7-3): residues 1-214 missing, 215-223 ATGTGSKAQ -> MSKRDKAGK
iso3 = "MSKRDKAGK" + human[223:]
aln3 = aligner.align(query, iso3)[0]
qb3, ib3 = aln3.aligned
id3 = sum(1 for (qs, qe), (s_, e_) in zip(qb3, ib3)
          for a, b in zip(query[qs:qe], iso3[s_:e_]) if a == b)
al3 = sum(qe - qs for qs, qe in qb3)
print(f"human isoform 3 (reconstructed from VSP_029565/VSP_029567) length: {len(iso3)}")
print(f"local alignment vs human isoform 3: query {qb3[0][0] + 1}-{qb3[-1][1]}, "
      f"iso3 {ib3[0][0] + 1}-{ib3[-1][1]}; identical {id3}/{al3} ({100 * id3 / al3:.1f}%)")
