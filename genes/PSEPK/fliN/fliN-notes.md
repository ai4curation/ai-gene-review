# fliN notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK fliN --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK fliN` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL entry Q88EU6 (PP_4357), FliN/MopA/SpaO family (TIGR02480). No KT2440 fliN experiments cached.
- [PMID:31452860 "CheY-P binds to FliNC in a FliM-dependent manner"]
- [PMID:31452860 "A continuous spiral density at the bottom edge of the C ring is made of the C-terminal domains of FliM (FliMC) and FliN."]
- [PMID:31452860 "FliN also provides binding sites for FliH"]

Decisions: GO:0003774 MODIFY -> GO:0005198 (same reasoning as FliM); plasma membrane KEEP_AS_NON_CORE; membrane MODIFY -> GO:0005886; chemotaxis ACCEPT; flagellum and basal body MODIFY -> GO:0009433; cell motility ACCEPT. Core MF GO:0005198 (module C-ring complex-level MF).


## Taxon/module audit, 2026-11-06

PMID:20439729 reports E. coli CheY-P/FliN binding; PMID:39179739 instead finds no such contact in its Salmonella active-CheY-mutant structure. These need not imply that the earlier experiment was false, but prohibit an unqualified universal docking claim. Retain structural switch participation and chemotaxis; describe the KT2440 direct binding interface as unresolved. Primary PMID:38632342 supports the lower C-ring organization. FliH docking remains comparative-family evidence.

Source anchor: [PMID:39179739 "CheY** has no interactions with FliN and the bottom subring in the structure."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
