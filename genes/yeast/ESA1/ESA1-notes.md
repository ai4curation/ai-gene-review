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

## Update 2026-10-10

Refreshed the review against current GOA as the first MYST-family entry in the
fungal PAINT family project.

- Re-fetched `yeast/ESA1` and reconciled the old 63-line review against the
  current 76 GOA rows, dropping stale rows that are no longer exported by GOA
  and reviewing every newly seeded row.
- Accepted the current `PTHR10615` IBA rows: broad eukaryotic MYST node
  `PANTHER:PTN004172926` for chromatin, nucleus, histone acetyltransferase,
  transcription, and chromatin-binding assertions, and fungal ESA1 node
  `PANTHER:PTN000834946` for `histone H4 acetyltransferase activity`.
- Updated all current `GO:0005515 protein binding` rows to `REMOVE`; the
  IntAct and ComplexPortal curation remains useful as interaction evidence, but
  the generic GO molecular-function assertion does not add an ESA1 activity.
- Modified the current `GO:0000786 nucleosome` annotation to the molecular
  function term `GO:0031491 nucleosome binding`, which better describes the
  NuA4/Piccolo NuA4 nucleosome contact assay.
- Read newer ESA1/NuA4 papers, including the 2024 nuclear-shape and lipid
  metabolism study and the 2025 cryo-EM study of piccolo NuA4 acetylation, and
  kept them as additional literature support rather than introducing a new GO
  process assertion.
