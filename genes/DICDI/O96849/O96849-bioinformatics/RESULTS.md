# O96849 (DIRS-1 ORF2) catalytic-motif check

Script: `motif_check.py` (run with `uv run python motif_check.py`; requires HMMER on PATH).
Raw output: `motif_check_output.txt`. Pfam HMMs (PF05869, PF00078, PF17917) are downloaded
from the InterPro API at run time; sequences from UniProt REST.

## Copies

O96849 and Q23898 are both 608 aa and differ at 9 positions (38, 276, 284, 286, 298, 308,
385, 496, 505), all outside the catalytic positions listed below. They are two cloned copies
of the same DIRS-1 ORF2 and the conclusions apply to both.

## Reverse transcriptase (PF00078 RVT_1, residues 51-215, 99.3 bits)

Residues at the three Mg-coordinating aspartates: D99 (in VKLDIKK), D165 and D166 (in the
YLDD motif, positions 163-166). All three catalytic aspartates are retained.

## RNase H (PF17917 RT_RNaseH, residues 323-403, 37.7 bits; CDD cd09275 327-449)

Acidic residues at candidate active-site positions: D331 and E334 (TDASE), E368 (REMLA),
D393 (QTDN), D443 (KADH; assignment of this fourth position is tentative, it lies outside the
Pfam envelope). The DEDD-type acidic cluster appears retained, but positions were assigned
from the Pfam/CDD alignment, not from a structure.

## C-terminal Dam-like methyltransferase region (PF05869, residues 455-561, 43.1 bits)

The region is a genuine but distant match to the phage Dam N6-adenine methyltransferase
family (E = 7.8e-15 against the full Pfam HMM). However the catalytic motif IV, which is NPPY
in the reviewed phage Dam enzymes used as positive controls (P51715 NPPY at 69, Q38156 NPPY
at 113), aligns to FPPP (519-522) in O96849: both the N (catalytic, binds the target adenine
N6) and the Y (stacks with the flipped base) are substituted. No [DNSH]PP[YFW] motif occurs
anywhere in O96849 or Q23898.

Interpretation: the C-terminal region is a degenerate Dam-like domain. Its catalytic
methyltransferase activity is doubtful on sequence grounds; it may be non-catalytic or have
divergent function. No experiment has tested it.

## Limitations

Motif positions were read from HMM alignments to Pfam models, not from structures; no
biochemical data exist for any of these domains in DIRS-1.
