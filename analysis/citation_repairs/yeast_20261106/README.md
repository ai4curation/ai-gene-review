# Yeast citation repair, 2026-11-06

Full validation for DnaK PR #6125 failed on 17 quotation errors in 16 unrelated yeast reviews. This repair changes only those quotation fields: fifteen paper titles are omitted from optional supporting_text fields, and the two ATG1 quotations are matched to the current extraction's `atg1Δ atg15Δ` typography. The ATG1 sentence is present in the cited PMN paper; it was not misattributed to the paper or a different autophagy process. No experimental annotation is rejected and no gene-specific evidence is invented from general interactome prose.

All publication references, annotation payloads, actions, summaries, reasons and other curated content are preserved. Cached publications, UniProt, GOA and provider outputs are unchanged. The annotation-reviewer consultation checked the primary sources: LEU4/LEU9 retain direct heterodimer evidence from PMID:25841022, and SIS2 retains direct Ppz1-inhibition evidence from PMID:9636153.

The consultation also found a separate substantive issue in HDA1: the rationale for its three identical-protein-binding rows portrays self-association as an alternative to the Hda2/Hda3 complex. PMID:11287668 instead says that self-association contributes to that complex's likely tetramer. This quotation-only repair does not resolve or validate that existing rationale, and does not infer that self-association is dispensable. A distinct evidence review should reassess the three reasons and their core-function classification together.

The current source cache is pinned to main 1970e159b929a11ec02b0bc86e64cebae7cf4c9e. An older worktree cache used spaces before the deletion symbols, explaining why a quotation once matching that extraction no longer matched. No cache was manually repaired to accommodate a quotation.

## Validation result and follow-up scope

The full-corpus run finished successfully on 2e4f3f19b36adf5ff0a2ce5dc0c44c89722cf401: 10,625 reviews validated; zero schema, term, reference or best-practice blocking errors; 279,368 quotation snippets and 108,845 titles checked; 52 reference advisories; all 54 pathway-reference checks passed. All 295 frozen publication files matched the tested commit before recording this result. This closes the 17 observed citation blockers, not the wider citation-quality audit.

Independent review on PR #6134 also reports approximately 80 title-as-quotation entries across 37 yeast reviews, including a top-level HSC82 finding not exercised by the full-corpus recipe. Those figures are the reviewer's report, not a new independent census. The full-run pass does not certify those entries; a separate source review remains needed. The HDA1 rationale issue above remains open.
