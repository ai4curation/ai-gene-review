# MYCLP1 notes

Automated deep research was attempted for this review with `just deep-research-falcon human MYCLP1 --fallback perplexity-lite`,
but the local Falcon provider was unavailable and the Perplexity fallback was not configured. These notes therefore summarize
the cached primary literature, UniProt record, and PANTHER PAINT data used for the manual review.

## Evidence reviewed

- **Processed MYCL-related locus.** Morton et al. characterized MYCL2, now MYCLP1, as a DNA sequence homologous to
  MYCL1 and reported that "Sequence analysis of MYCL2 revealed an open reading frame of 1194 bp with no intervening
  sequences and strong homology to the recently published DNA sequence of MYCL1" [PMID:2541066].
- **Protein existence is still uncertain.** The reviewed UniProt entry names the product "Putative myc-like protein
  MYCLP1", assigns protein existence level `PE   5: Uncertain;`, and warns that it "Could be the product of a
  pseudogene." This review treats the locus as a pseudogene because neither the cached 1989 locus-characterization
  abstract nor the UniProt record establishes an endogenous protein product.
- **Sequence-only TF predictions.** MYCLP1 still has recognizable Myc-family and bHLH signatures, so the InterPro and
  PAINT propagation rows have a plausible sequence basis. I did not find a cached human MYCLP1 assay showing that an
  endogenous protein is made, enters nuclei, dimerizes with MAX, binds E-box DNA, or regulates Pol II transcription.
  The existing sequence-based rows are therefore marked `UNDECIDED` rather than removed from an abstract-only 1989
  locus characterization paper.
