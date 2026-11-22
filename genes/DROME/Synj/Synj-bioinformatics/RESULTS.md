# Synj (Q5U0V7) catalytic motif conservation

Script: `catalytic_motifs.py` (run with `uv run --with biopython python catalytic_motifs.py`);
raw output in `RESULTS-raw.txt`. Sequences fetched live from UniProt (Q5U0V7 fly Synj,
O43426 human SYNJ1 canonical isoform, G5ECL2 worm UNC-26); global BLOSUM62 pairwise
alignments of fly and worm against human.

## Results

- Lengths: fly Synj Q5U0V7 1218 aa; human SYNJ1 O43426 1573 aa; worm UNC-26 G5ECL2 1119 aa.
- SAC domain catalytic CX5R(T/S) motif: human CLDCLDRT (from residue 383) aligns to fly
  CLDCLDRT starting at fly residue 396, identical; worm UNC-26 is also identical (CLDCLDRT at 378).
- 5-phosphatase signature motifs: human WCGDFNYR (727) aligns to fly WCGDFNYR (737), identical;
  human PAWTDRV (802) aligns to fly PAWTDRV (812), identical.
- Fly residue 228 is R (context TRFNVRGTNDE) and aligns to human canonical O43426 R219
  (context TRFNVRGTNDD). PMID:28331029 describes the fly R228Q knock-in as the equivalent of the
  human Parkinsonism R258Q, which is numbered on a different SYNJ1 isoform; the conserved
  arginine is present in the fly protein.
- Other regex hits for C.{5}R[TS] in human SYNJ1 (residues 184, 374) are incidental matches,
  not the catalytic motif; they are reported in the raw output only for completeness.

## Interpretation

The full-length fly product retains the catalytic signature residues of both phosphatase
modules (SAC CX5R(T/S) and the 5-phosphatase WxGDxNxR / PxxxDR motifs), so there is no
sequence evidence of catalytic loss in either domain. This supports transfer of the
dual phosphatase chemistry demonstrated for synaptojanin family members, and is consistent
with the direct fly 5-phosphatase assays (PMID:24977345, PMID:27559170).
