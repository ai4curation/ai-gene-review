# LOC732842 (K7TTR0) bioinformatics results

Script: `compare_tsb1.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5).
Raw output: `compare_tsb1_output.txt`. Inputs: `../LOC732842-uniprot.txt` (K7TTR0),
`P43283-uniprot.txt` (Swiss-Prot TRPB1_MAIZE, TSB1/ORP1, N-terminal fragment, copied from the
LOC732803 review folder), `K7TR93-uniprot.txt` (LOC732803, the chromosome-10 orp2 paralog).

## Identity of the locus

- K7TTR0 is the 474 aa product of NCBI GeneID 732842 (chromosome 4), which NCBI Gene names
  "orange pericarp 1" (aliases TSB1, orp1, GRMZM2G169593, Zm00001d049610).
- K7TTR0 vs P43283 (Swiss-Prot TSB1): 388/389 identical aligned columns (99.7%), so K7TTR0 is
  the full-length TSB1 protein.
- K7TTR0 vs K7TR93 (orp2/TSB2): 96.8% identity over 468 aligned columns.

## Catalytic residue

- The curated PLP-binding lysine of P43283 (MOD_RES 84, "N6-(pyridoxal phosphate)lysine")
  aligns to K169 of K7TTR0, in the context AHKINN (H-K-x-N-N motif). The catalytic lysine of
  the beta-reaction is retained.

## Peptides and constructs from PMID:18430213

- The three native-complex tryptic peptides ADGTGPLIYLK (148), DATSEAIR (250) and QALNVFR (224)
  all occur in K7TTR0, each preceded by K/R. All three also occur in K7TR93, so the MS data do
  not by themselves discriminate TSB1 from TSB2.
- The ZmTSB1 forward expression primer encodes (after the NdeI-derived His-Met) AASPAA, found at
  position 58 of K7TTR0 (and at 64 of K7TR93). The recombinant "mature" ZmTSB1 therefore
  started near residue 57, i.e. the authors treated roughly the first 56 residues as the
  plastid-targeting sequence. The paper names the protein ZmTSB1 and equates Zmtsb1 with orp1,
  which is the locus encoding K7TTR0.
