# ZNF788P KRAB and zinc-finger sequence audit

Script: `znf788p_check.py` (run with `uv run --script znf788p_check.py`; raw output in
`results.txt`). All inputs are fetched live from Ensembl REST, UniProt REST/UniSave and
ENA. The script uses a BLOSUM62 local alignment (gap open -10, extend -0.5) against the
KRAB domain of ZNF10/KOX1 (P21506, residues 14-85), and a regex for C2H2 zinc-finger
motifs (C-x2/4-C-x12-H-x3/4-H).

## Results

- Ensembl ENSG00000214189 is a `transcribed_unprocessed_pseudogene`. Its only
  transcript (ENST00000430298) has no annotated translation.
- UniProt Q6ZQV5 has had three sequence versions. Versions 1 (2004-2007) and 2
  (2007-2018) were a 615-aa protein with 14 C2H2 zinc-finger motifs and no KRAB domain.
  Since March 2018, version 3 has been an 82-aa product (PE5) with **0 C2H2 motifs**.
- The 82-aa product aligns to the ZNF10 KRAB domain over 54 residues (26 identical,
  48.1%), but only up to ZNF10 residue 68 of 14-85. It covers the KRAB-A box and stops
  there. Nothing corresponds to the end of the A box or to a KRAB-B box.
- Classical KRAB-A motifs: ZNF10 D18-V19 maps to ZNF788P D28-V29 (retained). ZNF10
  M43-L44-E45 maps to ZNF788P M53-Q54-E55, so the central leucine is replaced by
  glutamine.
- cDNA AK128700 (FLJ cDNA): in frame 2, the KRAB peptide begins at nt 209 and reaches a
  stop codon after 61 codons (nt 392). The zinc-finger ORF (the historical 615-aa
  sequence) begins in the same frame at nt 638 and runs 615 codons (stop at nt 2483).
  The KRAB exon and the zinc-finger array are therefore in frame with each other but
  separated by a stop codon. Frame 2 of AK128700 contains 17 C2H2 motifs, and frame 1
  of AK128282 contains 16.

## Interpretation

The locus has the layout of a KRAB-zinc-finger gene: a KRAB-A exon and a downstream
zinc-finger array exon. In the transcripts, however, the two are not joined into one
open reading frame. The current UniProt product is only the truncated KRAB-A part. That
segment has no zinc fingers, no DNA-binding domain of any kind, no B box, and a
substitution in the MLE motif. The zinc-finger ORF can be translated on its own from an
internal ATG, which is why the entry described it before 2018. Which product, if either,
is made in cells cannot be decided from sequence alone.
