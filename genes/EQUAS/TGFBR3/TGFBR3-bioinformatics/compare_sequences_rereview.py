# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Re-review analysis for donkey TGFBR3 (A0A8C4M6Z6).

Maps human Q03167 functional sites not covered by compare.py (GAG attachment
serines, N-glycans, TGF-beta interaction region, Thr-840 phosphosite, the
cytoplasmic tail) onto the donkey sequence, and checks whether the human
segment 763-776 that has no donkey partner is also absent from other
mammalian TGFBR3 sequences (rereview-orthologs.fasta, downloaded from UniProt
REST). Writes RESULTS-rereview.md. Nothing is hardcoded except site positions
read from the human UniProt flat file.

Run from the repository root:
    uv run --script genes/EQUAS/TGFBR3/TGFBR3-bioinformatics/compare_sequences_rereview.py
"""
from pathlib import Path

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
human = SeqIO.read(here / "human-Q03167-uniprot.txt", "swiss")
donkey = SeqIO.read(here.parent / "TGFBR3-uniprot.txt", "swiss")
others = list(SeqIO.parse(here / "rereview-orthologs.fasta", "fasta"))

al = Align.PairwiseAligner(mode="global")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -10, -0.5


def h2x(seq):
    best = al.align(human.seq, seq)[0]
    m = {}
    for (s, e), (t, u) in zip(*best.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            m[i] = j
    return m


hs = str(human.seq)
ds = str(donkey.seq)
hd = h2x(donkey.seq)
lines = ["# TGFBR3 re-review: site mapping and juxtamembrane segment check", ""]
lines.append(
    f"Human Q03167 ({len(hs)} aa) vs donkey A0A8C4M6Z6 ({len(ds)} aa); global alignment, "
    "BLOSUM62, gap open -10, extend -0.5."
)
lines += ["", "## Human point/region features mapped to donkey", ""]
for f in human.features:
    if f.type not in {"CARBOHYD", "MOD_RES", "REGION", "TOPO_DOM"}:
        continue
    note = f.qualifiers.get("note", "")
    note = note[0] if isinstance(note, list) else note
    if "Disordered" in note:
        continue
    s, e = int(f.location.start), int(f.location.end)
    pos = range(s, e)
    paired = [p for p in pos if p in hd]
    ident = sum(hs[p] == ds[hd[p]] for p in paired)
    if e - s == 1:
        d = hd.get(s)
        dres = f"{ds[d]}{d + 1}" if d is not None else "gap"
        lines.append(f"- {f.type} {note}: human {hs[s]}{s + 1} -> donkey {dres}")
    else:
        dspan = f"[{hd[paired[0]] + 1}, {hd[paired[-1]] + 1}]" if paired else "none"
        lines.append(
            f"- {f.type} {note}: human [{s + 1}, {e}] -> donkey {dspan}; "
            f"{ident}/{len(pos)} identical, {len(paired)} paired"
        )

lines += ["", "## Human 755-790 window in each sequence (aligned to human)", ""]
win = range(754, 790)
lines.append(f"- human Q03167: {hs[754:790]}")
for rec in [donkey] + others:
    m = hd if rec is donkey else h2x(rec.seq)
    sq = str(rec.seq)
    s = "".join(sq[m[p]] if p in m else "-" for p in win)
    gaps = [p + 1 for p in range(len(hs)) if p not in m]
    name = rec.id if rec is not donkey else "donkey A0A8C4M6Z6"
    lines.append(
        f"- {name} ({len(sq)} aa): {s}; human residues without partner: {len(gaps)}"
        + (f" (first {gaps[0]}, last {gaps[-1]})" if gaps else "")
    )

lines += ["", "## C-terminal cytoplasmic tail (last 15 residues)", ""]
lines.append(f"- human: {hs[-15:]}")
lines.append(f"- donkey: {ds[-15:]}")
for rec in others:
    lines.append(f"- {rec.id}: {str(rec.seq)[-15:]}")
lines += [
    "",
    "Interpretation is left to the review; pairwise alignment does not by itself establish orthology",
    "(orthology here rests on PANTHER subfamily PTHR14002:SF7 membership).",
]
(here / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
