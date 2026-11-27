# MYCL notes

Automated deep research was attempted for this review with `just deep-research-falcon human MYCL --fallback perplexity-lite`,
but the local Falcon provider was unavailable and the Perplexity fallback was not configured. These notes therefore summarize
the cached primary literature, UniProt record, and PANTHER PAINT data used for the manual review.

## Evidence reviewed

- **MYCL is a functional Myc-family paralog.** DePinho et al. described the human L-myc gene and an L-myc pseudogene.
  The cached abstract reports that the "L-myc gene contains three exons with coding regions and splice junctions located
  at positions analogous to those found in the c- and N-myc genes" and that an expression vector carrying L-myc could
  contribute to transformation in rat embryo fibroblasts [PMID:3322939].
- **Conserved bHLH-LZ function.** MYCL carries the Myc N-terminal and bHLH InterPro signatures and sits on
  `PTHR45851` node `PTN001691821` for the Myc family nuclear transcription-factor activity rows. UniProt summarizes
  the same inferred molecular core: "Binds DNA as a heterodimer with MAX."
- **Nuclear localization.** The UniProt record cites Ikegaki et al. for direct L-Myc protein detection and states
  nuclear localization from both a PROSITE-ProRule prediction and experimental evidence. GOA also has Human Protein
  Atlas HTP rows for nucleoplasm and chromosome; these are retained as compatible high-throughput localization calls.
- **Scope.** None of the MYCL papers reviewed here identifies MYCL-specific direct target genes. The review therefore retains the
  family-level molecular function and localization rows but does not manufacture MYCL process annotations beyond the
  existing PAINT/InterPro terms.
