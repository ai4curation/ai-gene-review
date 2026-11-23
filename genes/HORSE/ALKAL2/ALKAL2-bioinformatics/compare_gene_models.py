# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Compare horse ALKAL2 gene models (F6XWZ3 and siblings) with human ALKAL2/ALKAL1.

Reads the UniProt flat files in this folder (and the gene folder's F6XWZ3 record),
locates the human-like start, aligns, and checks the conserved cysteines of the
augmentor domain (human ALKAL2 disulfides C111-C147, C125-C134; interchain C66).
"""
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
FILES = {
    "F6XWZ3": HERE.parent / "ALKAL2-uniprot.txt",
    "A0A3Q2I4Q6": HERE / "horse-A0A3Q2I4Q6-uniprot.txt",
    "A0A9L0SHF3": HERE / "horse-A0A9L0SHF3-uniprot.txt",
    "A0A3Q2L2L8": HERE / "horse-A0A3Q2L2L8-uniprot.txt",
    "human_ALKAL2_Q6UX46": HERE / "ALKAL2-human-Q6UX46-uniprot.txt",
    "human_ALKAL1_Q6UXT8": HERE / "ALKAL1-human-Q6UXT8-uniprot.txt",
}
seqs = {k: str(next(SeqIO.parse(str(v), "swiss")).seq) for k, v in FILES.items()}
for k, s in seqs.items():
    print(f"{k}\tlength={len(s)}")

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "local"

human = seqs["human_ALKAL2_Q6UX46"]
HUMAN_CYS = {66: "interchain", 111: "C111-C147", 125: "C125-C134", 134: "C125-C134", 147: "C111-C147"}


def report(name: str, ref_name: str, ref: str) -> None:
    q = seqs[name]
    aln = aligner.align(q, ref)[0]
    ident = aligned = 0
    mapping = {}
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(rs, re_)):
            aligned += 1
            ident += q[i] == ref[j]
            mapping[j + 1] = i + 1
    qblocks = aln.aligned[0]
    print(f"\n{name} vs {ref_name}: query {qblocks[0][0]+1}-{qblocks[-1][1]}, "
          f"ref {aln.aligned[1][0][0]+1}-{aln.aligned[1][-1][1]}, "
          f"identity {ident}/{aligned} = {100*ident/aligned:.1f}%")
    if ref_name.startswith("human_ALKAL2"):
        for pos, role in HUMAN_CYS.items():
            qp = mapping.get(pos)
            aa = q[qp - 1] if qp else "-"
            print(f"  human C{pos} ({role}) -> {name} {aa}{qp if qp else ''}")


for name in ["F6XWZ3", "A0A3Q2I4Q6", "A0A9L0SHF3", "A0A3Q2L2L8"]:
    report(name, "human_ALKAL2_Q6UX46", human)
report("F6XWZ3", "human_ALKAL1_Q6UXT8", seqs["human_ALKAL1_Q6UXT8"])

# Is the 152-aa model an exact suffix of F6XWZ3?
f6, short = seqs["F6XWZ3"], seqs["A0A3Q2I4Q6"]
idx = f6.find(short)
print(f"\nA0A3Q2I4Q6 found in F6XWZ3 at residue {idx+1 if idx >= 0 else 'not found'}"
      f" (F6XWZ3 N-terminal extension = {idx} residues)")
ext = f6[:idx]
comp = {aa: ext.count(aa) for aa in "RGAPSD"}
print(f"extension composition (R,G,A,P,S,D counts): {comp}; "
      f"fraction RGAP = {sum(ext.count(a) for a in 'RGAP')/len(ext):.2f}")
