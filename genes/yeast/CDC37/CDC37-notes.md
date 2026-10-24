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

## 2026-09-03 Update: completed the verbatim-quote pass (PR review follow-up)

Review feedback on PR #2931 correctly noted that the first pass fixed only the two
quotes that errored, leaving the same paraphrase-by-elision defect elsewhere in the
same `references:` block, and that one of the applied fixes trimmed away the
evidence it was meant to carry. Four further citation-accuracy edits, no changes to
any `action`, term id, `description`, or `core_functions`:

- `references[PMID:17220467].findings[0]` quoted "Levels of the MAPKs Hog1p and
  Slt2p in cells are reduced in a cdc37-S14A mutant, and downstream responses…",
  silently dropping "(Mpk1p)" and "consequently". This only warned rather than
  errored because `full_text_available: false` downgrades abstract-only caches, but
  the abstract *is* cached and the quote was checkably wrong. Replaced with the
  exact text [PMID:17220467 "levels of the MAPKs Hog1p and Slt2p (Mpk1p) in cells
  are reduced in a cdc37-S14A mutant, and consequently downstream responses mediated
  by Hog1p and Slt2p are compromised."] — the same string already used verbatim in
  the `supported_by` block for GO:0000165.
- `references[PMID:17242065].findings[0]` had been trimmed to "in a cdc37 mutant
  strain showed that 51 had decreased abundance compared with levels in the
  wild-type strain." — verbatim, but with the grammatical subject removed, so "51"
  had no denominator and the quote no longer supported the statement "Cdc37 broadly
  stabilizes the yeast kinome". `PMID_17242065.md` has `full_text_available: true`,
  and the Results section states the same finding as a self-contained sentence, so
  used that instead [PMID:17242065 "Of the 65 kinases assayed, 51 displayed reduced
  steady-state levels by at least twofold in the cdc37S14A mutant strain compared
  with the wild type."]. This restores the 51-of-65 (~50% of the kinome) figure and
  avoids the line-break artifact in the abstract's "protein kinases ( \napproximately
  50% of the kinome)".
- Two terminal-period truncations in `supported_by` quotes for PMID:17220467, where
  a period had been substituted for the truncated remainder of the sentence:
  GO:0071474 (`cellular hyperosmotic response`, IMP) now quotes the whole sentence
  [PMID:17220467 "Mutation of the phosphorylation site Ser14 in Cdc37p renders cells
  sensitive to osmotic stress and cell wall perturbation by calcofluor white."], and
  GO:0038066 (`p38MAPK cascade`, IPI) drops the added period [PMID:17220467 "Hog1p
  and Slt2p both interact in a complex with Cdc37p in vivo"], the source continuing
  ", something that has not been reported previously."

`just validate yeast CDC37` now reports ✓ Valid with a single warning, down from two:
the supporting-text warning for PMID:17220467 is gone. The remaining warning
(`existing_annotations[4].review.propagation_review` missing structured metadata on
an IBA/MODIFY annotation) is pre-existing and out of scope for a citation-accuracy
PR.
