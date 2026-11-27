# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Align horse RBM41 (A0A3Q2GZN1) to human RBM41 canonical (Q96IZ5-1) and to the
human isoform 3 exon insertion, and map the human RRM onto horse.

Run from repo root:
    uv run --script genes/HORSE/RBM41/RBM41-bioinformatics/compare_horse_human.py
Writes RESULTS.md next to this script. Nothing is hardcoded except the human
isoform-3 inserted peptide, which is read from the human VAR_SEQ VSP_021346 note.
"""
from pathlib import Path
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
horse = SeqIO.read(here.parent / "RBM41-uniprot.txt", "swiss")
human = SeqIO.read(here / "human-Q96IZ5-uniprot.txt", "swiss")
hs, qs = str(human.seq), str(horse.seq)

al = Align.PairwiseAligner(mode="global")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -10, -0.5
aln = al.align(hs, qs)[0]
h2q = {}
for (s, e), (t, u) in zip(*aln.aligned):
    for i, j in zip(range(s, e), range(t, u)):
        h2q[i] = j
ident = sum(hs[i] == qs[j] for i, j in h2q.items())


def runs(pos):
    out = []
    for p in sorted(pos):
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


mapped = set(h2q.values())
q_unpaired = [r for r in runs(j + 1 for j in range(len(qs)) if j not in mapped) if r[1] - r[0] >= 4]
h_unpaired = [r for r in runs(i + 1 for i in range(len(hs)) if i not in h2q) if r[1] - r[0] >= 4]

# human isoform-3 insertion from VSP_021346 ("Q -> QAYHK...")
ins = None
for f in human.features:
    if f.type == "VAR_SEQ" and f.id == "VSP_021346":
        note = f.qualifiers["note"].replace(" ", "")
        ins = note.split("->")[1].split("(")[0][1:]
ins_pos = qs.find(ins) + 1 if ins else 0

lines = [
    "# RBM41 horse (A0A3Q2GZN1) vs human (Q96IZ5) comparison",
    "",
    f"Horse length {len(qs)} aa; human canonical isoform 1 length {len(hs)} aa.",
    f"Global alignment: {ident}/{len(h2q)} identical paired residues "
    f"({100*ident/len(h2q):.2f}% identity); paired coverage {100*len(h2q)/len(hs):.2f}% of human, "
    f"{100*len(h2q)/len(qs):.2f}% of horse.",
    f"Horse ranges (>=5 aa) without a human partner: {q_unpaired}.",
    f"Human ranges (>=5 aa) without a horse partner: {h_unpaired}.",
    "",
    f"Human isoform-3 inserted peptide (VSP_021346, after human Q174): {ins}",
    f"Found in horse sequence at position: {ins_pos if ins_pos > 0 else 'not found'}",
    "",
    "## Human features mapped to horse",
]
for f in human.features:
    if f.type != "DOMAIN":
        continue
    s, e = int(f.location.start), int(f.location.end)
    npair = sum(1 for p in range(s, e) if p in h2q)
    nid = sum(1 for p in range(s, e) if p in h2q and hs[p] == qs[h2q[p]])
    qs_, qe_ = h2q.get(s), h2q.get(e - 1)
    lines.append(
        f"- {f.type} {f.qualifiers.get('note', '')}: human [{s+1}, {e}] -> horse "
        f"[{qs_+1 if qs_ is not None else '-'}, {qe_+1 if qe_ is not None else '-'}]; "
        f"{nid} of {e-s} human residues identical ({npair} paired)"
    )
# EMSA construct used by Norppa et al. 2024: human residues 267-413
s, e = 266, 413
nid = sum(1 for p in range(s, e) if p in h2q and hs[p] == qs[h2q[p]])
lines.append(
    f"- Human RRM construct 267-413 used for EMSA (PMID:38499487): {nid} of {e-s} residues identical in horse"
)
lines += ["", "Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5.",
          "Pairwise identity is not by itself evidence of orthology; orthology rests on shared PANTHER subfamily PTHR16105:SF2."]
(here / "RESULTS.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
