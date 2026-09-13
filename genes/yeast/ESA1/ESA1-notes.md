# ESA1 curation notes

## Update 2026-09-02

Batch audit of the existing `ESA1-ai-review.yaml`. The review is otherwise thorough
(63 GOA lines all reviewed, sound REMOVE/KEEP_AS_NON_CORE calls), but one citation in
`core_functions[0].supported_by` was wrong:

- The entry cited `PMID:11742990` ("The Saccharomyces cerevisiae Set1 complex includes
  an Ash2 homologue and methylates histone 3 lysine 4", Roguev et al. 2001 EMBO J) with
  `supporting_text` equal to that paper's own title, offered as support for ESA1's core
  histone-acetyltransferase molecular function (GO:0004402) plus its involvement in
  transcription regulation (GO:0006357) and DNA repair (GO:0006281).
- `publications/PMID_11742990.md` (cached abstract) is about the **Set1/COMPASS**
  H3K4-methyltransferase complex and does not mention ESA1/Esa1 anywhere
  [PMID:11742990 "The Saccharomyces cerevisiae Set1 complex includes an Ash2 homologue
  and methylates histone 3 lysine 4"] — an unrelated methyltransferase complex, not the
  NuA4/Esa1 acetyltransferase this review is about. This is a genuine miscitation (right
  format, wrong paper), not merely a weak citation.
- Fixed by replacing it with `PMID:9520405` ("ESA1 is a histone acetyltransferase that
  is essential for growth in yeast", Smith et al. 1998 PNAS), which is already used
  elsewhere in this review's `existing_annotations` (GO:0004402 IMP evidence line) and
  directly supports the claim: [PMID:9520405 "we express a yeast ORF with homology to
  MYST family members and show it possesses histone acetyltransferase activity"].
- No other content, actions, or GO terms were changed. `PMID:31699900` (crotonylation)
  remains as the second `supported_by` entry, unchanged.

Everything else reviewed (all `existing_annotations`, the `description`, and the rest of
`core_functions`) was judged sound and evidence-backed; no further changes made in this
pass. Note: this gene directory also carries several non-standard files
(`ESA1-CURATION-ANALYSIS.md`, `ESA1-CURATION-SUMMARY.md`, `ESA1-ai-review-CURATED.yaml`,
`ESA1-ANNOTATION-TRIAGE.tsv`, `README-CURATION.md`, `FILES-INDEX.md`,
`ESA1-DECISIONS-OVERVIEW.txt`, `ESA1-CURATION-COMPLETE.md`) left over from an earlier
curation pass; left untouched here since removing/consolidating them is outside the
scope of this citation fix.
