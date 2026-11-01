# LOC732803 (K7TR93) bioinformatics results

Script: `compare_tsb.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5).
Raw output: `compare_tsb_output.txt`. Inputs: `../LOC732803-uniprot.txt` (K7TR93),
`P43284-uniprot.txt` (Swiss-Prot TRPB2_MAIZE, TSB2/ORP2, N-terminal fragment),
`P43283-uniprot.txt` (Swiss-Prot TRPB1_MAIZE, TSB1/ORP1), `K7TTR0-uniprot.txt`
(LOC732842, GeneID 732842, chromosome 4, NCBI Gene "orange pericarp 1").

## Identity of the locus

- K7TR93 is the full-length (479 aa) product of NCBI GeneID 732803 (chromosome 10), which
  NCBI Gene names "orange pericarp 2" (aliases TSB2, orp2, GRMZM2G005024).
- K7TR93 vs P43284 (TSB2): 96.6% identity over 443 aligned columns.
- K7TR93 vs P43283 (TSB1): 98.2% identity over 389 aligned columns.
- K7TTR0 (orp1 locus) vs P43283 (TSB1): 99.7% identity; vs P43284 (TSB2): 94.1%.
- Interpretation: the chromosome-4 locus clearly corresponds to Swiss-Prot TSB1. The
  chromosome-10 locus (K7TR93) is assigned to orp2 by genomic position, but its sequence
  is not a near-exact match to the 1992 TSB2 cDNA P43284 (96.6%), and is slightly closer
  to TSB1 over the shorter TSB1 fragment. The two paralogs are about 96% identical, so this
  does not change any functional inference; it is recorded as an open question about the
  P43284 sequence (cultivar or cDNA differences), not as an established error.

## Catalytic residue

- The curated PLP-binding lysine (MOD_RES "N6-(pyridoxal phosphate)lysine", K138 of
  P43284, K84 of P43283) aligns to K174 of K7TR93, inside an H-K-x-N-N motif (173-177).
  The catalytic lysine of the beta-reaction is therefore retained.

## Native-complex peptide

- The peptide QALNVFR, which PMID:18430213 assigned to ZmTSB1 in the native 160 kD
  tryptophan synthase complex, is a tryptic peptide (preceded by R) in K7TR93 (position 229)
  as well as in K7TTR0, P43283 and P43284. It therefore cannot discriminate TSB1 from TSB2;
  the mass-spectrometry identification is equally consistent with TSB2 in the complex.
