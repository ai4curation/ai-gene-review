# NCU07379 (V5IQW8): placement within PTHR40621:SF6 (re-review, 2026-10-21)

Script: `sf6_placement_rereview.py` (run with `uv run --script`); raw output in
`RESULTS-rereview-raw.txt`; alignment in `sf6_placement_rereview.aln.fasta`.
Sequences were fetched live from UniProt; MAFFT L-INS-i alignment; NJ tree on
BLOSUM62 distances; support from 100 column-bootstrap NJ replicates.

## Question

UniProt places NCU07379 in PTHR40621:SF6 (AP-1-LIKE TRANSCRIPTION FACTOR
YAP1-RELATED). SF6 is a broad subfamily: in N. crassa it holds two proteins,
NCU07379 (395 aa) and NCU03905 (577 aa). It also holds the A. nidulans
developmental regulator FlbB (C8VBM8). The question is which clade within SF6
NCU07379 belongs to, because the Yap1 oxidative-stress function and the FlbB
developmental function are clade-specific and should not be transferred across
clades.

## Results

- NCU07379 groups with the FlbB clade. In the NJ tree, the clade
  {V5IQW8, F7VKT3 (Sordaria), G4NCR2 (MGG_00342), G3J390 (CCM_01128), C8VBM8 (FlbB)}
  has 100% bootstrap support.
- NCU03905 is the N. crassa member of the Yap1/NapA clade. The clade
  {F5HEL0 (NCU03905), G4N6V5 (MGG_12814), Q4WMH0 (A. fumigatus Yap1), Q5AW17 (NapA)}
  has 100% bootstrap support, and NCU07379 lies outside it.
- Local Smith-Waterman identity of NCU07379: 47% to FlbB over 314 residues;
  28% to NCU03905; 26% to Pap1. Against the S. cerevisiae Yap proteins the
  local alignments are short (52-123 residues), consistent with similarity
  confined mostly to the bZIP region.
- The comparison is reciprocal. FlbB's best Sordariomycete hits are CCM_01128,
  the Sordaria protein, MGG_00342 and NCU07379, at 42-47% identity each. FlbB is
  31% identical to NCU03905.
- The deeper SF6 branches (Pap1, the S. cerevisiae Yap paralogs, Cap1) have
  bootstrap support below 50%. Only the two terminal clades above are resolved.
- The bZIP region of NCU07379 lies near the N-terminus (about residues 60-120),
  as in FlbB. The C-terminal 150 residues contain 3 cysteines.

## Interpretation

The tree supports NCU07379 as the N. crassa ortholog of FlbB, not of Yap1.
PMID:21423749 lists NCU07379 as the N. crassa FlbB ortholog independently.
Both clades descend from PAINT node PTN008082960, so the general bZIP
DNA-binding transcription activator terms propagated from that node apply.
Yap1/Pap1-specific processes, such as the oxidative-stress response, should not
be transferred to NCU07379.

## Limits

NJ on a small taxon sample. This is not a maximum-likelihood tree, and the
deeper SF6 nodes are unresolved.
