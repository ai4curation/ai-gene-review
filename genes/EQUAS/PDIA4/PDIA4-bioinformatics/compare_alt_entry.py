"""Compare the selected donkey PDIA4 entry (A0A8C4LTV9) with a second donkey
PDIA4 UniProt entry (A0A8C4PKQ4) and with human P13667.

Run from the repository root:
    uv run python genes/EQUAS/PDIA4/PDIA4-bioinformatics/compare_alt_entry.py
Writes ALT_ENTRY.md. Local (Smith-Waterman-style) alignment, BLOSUM62,
gap open -10, extend -0.5. Results are computed, not hardcoded.
"""
from pathlib import Path
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

here = Path(__file__).resolve().parent
sel = SeqIO.read(here.parent / "PDIA4-uniprot.txt", "swiss")
alt = SeqIO.read(here / "donkey-A0A8C4PKQ4-uniprot.txt", "swiss")
hum = SeqIO.read(here / "human-P13667-uniprot.txt", "swiss")
al = Align.PairwiseAligner(mode="local")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -10, -0.5

def summ(a, b):
    best = al.align(a.seq, b.seq)[0]
    pairs = [(i, j) for (s, e), (t, u) in zip(*best.aligned) for i, j in zip(range(s, e), range(t, u))]
    ident = sum(a.seq[i] == b.seq[j] for i, j in pairs)
    return dict(a_start=pairs[0][0] + 1, a_end=pairs[-1][0] + 1, b_start=pairs[0][1] + 1, b_end=pairs[-1][1] + 1,
                paired=len(pairs), ident=ident, pct=round(100 * ident / len(pairs), 2))

lines = ["# PDIA4: the two donkey PDIA4 UniProt entries", ""]
for (a, b) in [(sel, alt), (alt, hum), (sel, hum)]:
    r = summ(a, b)
    lines.append(f"- {a.id} ({len(a.seq)} aa) residues {r['a_start']}-{r['a_end']} align locally to {b.id} ({len(b.seq)} aa) residues {r['b_start']}-{r['b_end']}: {r['pct']}% identity over {r['paired']} paired residues.")
lines += ["", f"- First 30 residues of {alt.id}: {str(alt.seq[:30])}", f"- First 30 residues of {hum.id}: {str(hum.seq[:30])}",
          f"- {sel.id} residues 541-560: {str(sel.seq[540:560])}", "",
          "Regenerate with `uv run python genes/EQUAS/PDIA4/PDIA4-bioinformatics/compare_alt_entry.py`."]
(here / "ALT_ENTRY.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
