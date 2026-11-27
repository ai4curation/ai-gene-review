# BIRC8 manual curation notes

## 2026-11-27 PTHR10044 family review

- Reviewed BIRC8/ILP-2 as the human PTHR10044:SF167 member, with BIRC7/SF163 and the
  prior XIAP curation as family context. `just deep-research-falcon human BIRC8 --fallback
  perplexity-lite` could not run in this environment because those providers were not
  installed; no provider-branded deep-research file was fabricated.
- PMID:11390657 is the key primary source. It describes ILP-2 as an XIAP/ILP-1-related,
  testis-specific retroposed paralog that encodes a single BIR plus a C-terminal RING and
  has a narrower anti-apoptotic profile than XIAP: BIRC8 suppresses Bax and Apaf-1/CASP9
  death, blocks ATP-induced caspase activation in cytosolic extracts, and binds processed
  CASP9, but it did not protect from Fas- or TNF-mediated death.
- The review keeps the caspase-pathway and cytoplasmic annotations and decomposes the
  PAINT `GO:0043027` row to the plain cysteine-type endopeptidase inhibitor activity.
  The cell-cycle, JNK, stress-response, complex and nucleus rows are treated as
  over-annotations from broad BIRC7/XIAP/cIAP biology.
- The current PTHR10044 Wnt row is placed on the XIAP/BIRC8 branch, but its evidence is
  XIAP-based and not part of the SF167 BIRC8 retrogene. The family review therefore
  requests an IRD at the cached SF167 node `PANTHER:PTN002559439`.
