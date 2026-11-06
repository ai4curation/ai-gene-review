# Yeast citation repair, 2026-11-06

Full validation for DnaK PR #6125 failed on 17 quotation errors in 16 unrelated yeast reviews. This repair changes only those quotation fields: fifteen paper titles are omitted from optional supporting_text fields, and the two ATG1 quotations are matched to the current extraction's `atg1Δ atg15Δ` typography. The ATG1 sentence is present in the cited PMN paper; it was not misattributed to the paper or a different autophagy process. No experimental annotation is rejected and no gene-specific evidence is invented from general interactome prose.

All publication references, annotation payloads, actions, summaries, reasons and other curated content are preserved. Cached publications, UniProt, GOA and provider outputs are unchanged. The annotation-reviewer consultation checked the primary sources: LEU4/LEU9 retain direct heterodimer evidence from PMID:25841022, and SIS2 retains direct Ppz1-inhibition evidence from PMID:9636153.

The consultation also found a separate substantive issue in HDA1: the rationale for its three identical-protein-binding rows portrays self-association as an alternative to the Hda2/Hda3 complex. PMID:11287668 instead says that self-association contributes to that complex's likely tetramer. This quotation-only repair does not resolve or validate that existing rationale, and does not infer that self-association is dispensable. A distinct evidence review should reassess the three reasons and their core-function classification together.

The current source cache is pinned to main 1970e159b929a11ec02b0bc86e64cebae7cf4c9e. An older worktree cache used spaces before the deletion symbols, explaining why a quotation once matching that extraction no longer matched. No cache was manually repaired to accommodate a quotation.
