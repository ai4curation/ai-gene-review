# cheB1 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK cheB1 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK cheB1` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

Swiss-Prot entry Q88EW5 is HAMAP-annotated (MF_00099, PE 3). No KT2440 cheB1 experimental paper found in cache.
- Operon: [PMID:23766109 "this cluster is comprised of four independent transcriptional units: flhAF, fleNfliA, cheYZA and cheBmotAB"] - the "motAB" here are PP_4336/PP_4335, later called MotCD [PMID:36409076 "comprising the genes for the stator MotCD (PP4336 and PP4335)"].
- E. coli anchors: [PMID:358191 "This enzyme catalyzes the hydrolysis of gamma-glutamyl methyl ester residues"], [PMID:6304723 "enzymatic deamidation of glutamine to methyl-accepting glutamic acid"], [PMID:7578071 "donates a phosphoryl group to either of two regulator proteins, CheY or the receptor methylesterase (CheB)"].

Decisions: GO:0008984 ACCEPT (core, module MF); GO:0050568 ACCEPT (genuine family second activity; caveat: KT2440 receptor glutamines at adaptation sites untested); GO:0000156 ACCEPT; GO:0000160 ACCEPT; GO:0006935 ACCEPT; GO:0005737 ACCEPT (no finer KT2440 data, consistent with cheY/cheZ); GO:0007165 MODIFY -> GO:0000160.
Open: role of second CheB paralog PP_3759.


## Taxon/module audit, 2026-11-06

The operon called cheBmotAB in the older work contains the later-named MotCD pair, not PP_4905/PP_4904. CheB1 is PP_4337. All accepted methylesterase/deamidase and receiver claims remain conserved-family inferences; no new KT2440 biochemical result or direct CheA-to-CheB1 assay is asserted. Core descriptions now state this limit explicitly.

Source anchor: [PMID:23766109 "this cluster is comprised of four independent transcriptional units: flhAF, fleNfliA, cheYZA and cheBmotAB"]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
