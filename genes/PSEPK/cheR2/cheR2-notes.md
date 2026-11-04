# cheR2 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK cheR2 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK cheR2` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

Literature: PMID:23677992 (abstract-only cache; Swiss-Prot entry Q88ER1 carries ECO:0000269 lines from it).
- [PMID:23677992 "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors."]
- [PMID:23677992 "The mutant in CheR2 was deficient in chemotaxis, whereas mutation of CheR1 and CheR3 had either no or little effect on chemotaxis."]
- [PMID:23677992 "Analytical ultracentrifugation experiments demonstrate that CheR2 is monomeric"]

Decisions:
- GO:0008983 (IEA): ACCEPT, core MF (module MF supported by KT2440 data).
- GO:0008757 SAM-dependent MTase (InterPro2GO): MODIFY -> GO:0008983 (correct but general).
- NEW GO:0006935 chemotaxis, IMP, PMID:23677992 (no BP in GOA; CheR2 performs the adaptation methylation step).
- The project synthesis lists CheR2 as "homology + operon context" and treats paralog assignment as unresolved; PMID:23677992 resolves it experimentally (CheR2 = flagellar chemotaxis; CheR1 = biofilm route).
- Not added: GO:0000160 phosphorelay (CheR is not a phosphorelay participant); cytoplasm (no direct data, not in GOA).
