# motA (PP_4905, Q88DC2) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK motA --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/motA/motA-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Removed DE-name ("Flagellar motor rotation protein", imported ECO:0000313), DR GO and ARBA subcellular-location quotes.
- Added KT2440 genetics: PMID:36409076 [PMID:36409076 "In homogeneous fluids, the MotAB stator is crucial to promote swimming motility, so the movement of ΔmotAB mutant cells in aqueous fluids is strongly impaired."] [PMID:36409076 "the MotAB (PP4905 and PP4904)"]. NEW GO:0071973 changed from IC to IMP on this paper.
- GO:0071978 swarming: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0071973. Chemotaxis kept MARK_AS_OVER_ANNOTATED with a rewritten reason (stator supplies torque; switching is done by the C ring/che proteins). NEW GO:1902600 changed from IEA (citing the UniProt file) to IC on PMID:18310339. GO:0015078 contributes_to (module MF, complex level) and GO:0120101 kept. Removed the GOA-file reference. Status COMPLETE.


## Taxon/module audit, 2026-11-06

PP_4905/Q88DC2 is MotA of MotAB, distinct from PP_4336/MotC. Pair deletion and complementation establish MotAB-dependent swimming in KT2440. The contribution to proton transport is inferred from homologous Pseudomonas stators and conserved architecture; the KT2440 study does not directly compare proton versus sodium coupling. A MotA/TolQ/ExbB domain alone would not establish either ion specificity or a flagellar role. Retain existing NEW rows and stator contributions.

Source anchor: [PMID:36409076 "Additionally, the genome encodes a second copy of a stator outside this gene cluster, the MotAB (PP4905 and PP4904) (15)."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
