# CDC37 curation notes

## 2026-09-02 Update: fixed non-verbatim reference quotes

Audited the existing `CDC37-ai-review.yaml` for oversights. The biology/annotation
review itself is sound and well-supported (kinase-directed Hsp90 co-chaperone core
function, ACCEPT/MODIFY/KEEP_AS_NON_CORE calls all consistent with the literature),
but `just validate` / `ai-gene-review validate --verbose --terms` reported two
blocking ERRORs: the `references[].findings[].supporting_text` entries for
PMID:17242065 were not verbatim substrings of the cached publication text.

- The first finding quoted "Analysis of 65 Saccharomyces cerevisiae protein kinases
  showed that 51 had decreased abundance..." but the actual sentence in
  `publications/PMID_17242065.md` is "Analysis of 65 Saccharomyces cerevisiae
  protein kinases (approximately 50% of the kinome) **in a cdc37 mutant strain**
  showed that 51 had decreased abundance compared with levels in the wild-type
  strain." [PMID:17242065 "in a cdc37 mutant strain showed that 51 had decreased
  abundance compared with levels in the wild-type strain."] — trimmed the quote to
  a verbatim substring rather than paraphrasing across the omitted clause.
- The second finding quoted "Results from pulse-labeling studies..." but the actual
  text reads "Results from **our** pulse-labeling studies showed that Cdc37 protects
  nascent kinase chains from rapid degradation shortly after synthesis."
  [PMID:17242065 "Results from our pulse-labeling studies showed that Cdc37 protects
  nascent kinase chains from rapid degradation shortly after synthesis."] — added
  the missing word "our" to restore the exact quote.

No changes were made to any `action`, term id, or the `description`/`core_functions`
content — this is a citation-accuracy fix only. Confirmed `validate --verbose --terms`
now passes (0 errors) and `validate-goa` passes.
