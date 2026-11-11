# Horse TNFRSF1A gene models vs human TNFR1 (P19438)

Scripts: `compare_sequences.py` (feature coverage, cysteine conservation; output
`results.json`) and `nterm_alignment.py` (full pairwise alignments; output
`alignments.txt`). Both are PEP 723 scripts run with `uv run --script`; sequences
and human features are fetched live from the UniProt REST API. Alignments are
global, BLOSUM62, gap open -10, extend -0.5. In `alignments.txt` Biopython labels the
first sequence (the horse model) "target" and human P19438 "query".

## Gene models

All three horse UniProt entries for TNFRSF1A are unreviewed products of the same
Ensembl gene ENSECAG00000016330 (VGNC:24369), and all three map to PANTHER
PTHR46861:SF1, the same subfamily as human P19438 and mouse P25118.

| Accession | Length | Identity to human (aligned) | Human ECD Cys conserved (of 24) | Notes |
|-----------|--------|-----------------------------|----------------------------------|-------|
| A0A5F5Q204 (benchmark) | 475 | 0.75 | 24 | complete CRD1-4, TM, death domain; 22-residue N-terminal insertion in the signal-peptide region |
| F6YIE3 | 413 | 0.73 | 20 | lacks the signal peptide and half of CRD1 |
| A0A5F5PQM0 | 410 | 0.75 | 18 | human-like N-terminus and signal peptide; lacks part of CRD1 and CRD2 |
| P25118 (mouse) | 454 | 0.67 | 24 | control |

## Feature coverage for A0A5F5Q204 (human coordinates)

- Signal peptide 1-29: covered, but only 59% identical; horse residues 8-29
  (`KVLDMLPRRETPTPSPDRVCDL` region) have no human counterpart. The hydrophobic core
  `ALLALLVEIYPSG` that follows is conserved, and is identical to the start of A0A5F5PQM0
  (`MGLPAVPGLLPPLALLALLVEIYPSG...`). A0A5F5Q204 therefore has a different, longer
  N-terminal segment from the human-like model; whether it is cleaved as a normal signal
  peptide was not tested here.
- CRD1 43-82 (contains the PLAD): 100% covered, 88% identical.
- CRD2 83-125: 91% identical. CRD3 126-166: 81% identical (one 3-residue insertion,
  `ETS`). CRD4 167-196: 73% identical.
- Transmembrane helix 212-232: 86% identical.
- N-SMase activation domain 338-348: 73% identical.
- Death domain 356-441: 87% identical.

## Interpretation

A0A5F5Q204 encodes a complete TNFR1 receptor: all 24 extracellular cysteines of the
four human CRDs, the transmembrane helix and the death domain are present. Its only
substantive difference from the human receptor is the N-terminal segment that precedes
the mature chain, so the mature receptor would be the same as that of the human-like model.
Of the three horse models it is the only one with an intact ectodomain. The two sibling
models are truncated in CRD1/CRD2 and would not be expected to bind TNF normally.
No analysis here tests whether the horse protein binds TNF or signals; those
conclusions rest on 1:1 orthology (PANTHER PTHR46861:SF1; PAINT node PTN002930098 at
Euteleostomi) and on the conservation reported above.
