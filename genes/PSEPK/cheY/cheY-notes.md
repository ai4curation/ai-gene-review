# cheY (PP_4340, Q88EW2) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK cheY --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/cheY/cheY-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Earlier version had paraphrased supporting_text attributed to abstract-only PMIDs 36287825 and 25100612, and a non-verbatim falcon quote; all replaced.
- Evidence: P. putida CheA transfers phosphate to CheY in vitro [PMID:40197389 "The addition of CheY to phosphorylated CheA led to a labeling of CheY and a reduction in the phospholabeling of CheA"]; CheY co-purifies with CheA [PMID:40197389 "the response regulator CheY and the phosphatase CheZ (two proteins known to be associated with CheA) also showed high Log2(fold change) values"]. PROSITE REC domain 2-119 and 4-aspartylphosphate Asp52 (PROSITE-ProRule).
- Added NEW GO:0000156 phosphorelay response regulator activity (IC, PMID:40197389; locus tag of the assayed CheY not stated in the text, so not IDA) and NEW GO:0006935 chemotaxis (IC; cluster with cheA2, whose mutant is non-chemotactic [PMID:30761113 "mutation of cheA2 abolished chemotaxis"]). No KT2440 cheY mutant exists (knowledge gap; see suggested experiments).
- GO:0000160 ACCEPT; GO:0005737 ACCEPT (no cytosol row; UniProt location is ARBA-only so support is falcon synthesis plus the He 2025 description). Status COMPLETE.


## Taxon/module audit, 2026-11-06

The target remains PP_4340/Q88EW2, supported by REC architecture and cheYZA neighborhood. Official supplement names CheY as a pull-down hit but gives no accession or CheY expression construct/primers. Keep inherited IC rows; do not upgrade this exact target to IDA. Motor-switch participation is well grounded by family mechanism, while direct docking to KT2440 FliN is unmeasured and the 2024 Salmonella structure cautions against assuming universal FliN contact.

Source anchor: [PMID:40197389 "The addition of CheY to phosphorylated CheA led to a labeling of CheY and a reduction in the phospholabeling of CheA"]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
