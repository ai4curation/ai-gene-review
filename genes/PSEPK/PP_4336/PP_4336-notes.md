# PP_4336 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK PP_4336 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK PP_4336` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL Q88EW6; MotC (MotA-like, PANTHER PTHR30433:SF3). KT2440 paper PMID:36409076 (full text):
- [PMID:36409076 "P. putida has a large gene cluster for flagellar motility comprising the genes for the stator MotCD (PP4336 and PP4335)."]
- [PMID:36409076 "MotC shares 83% identity, and MotD shares 70% identity."]
- [PMID:36409076 "For both agar concentrations, the ΔmotAB culture spreads almost as quickly as the wild type, whereas the ΔmotCD culture spreads considerably more slowly."]
- [PMID:36409076 "The double mutant ΔmotAB ΔmotCD is nonmotile."]
- [PMID:36409076 "In Pseudomonas aeruginosa, the two stators, MotAB and MotCD, use proton motive force"]

Decisions: plasma membrane ACCEPT; membrane MODIFY -> GO:0005886; chemotaxis MARK_AS_OVER_ANNOTATED (stator, not signaling; consistent with motA); swarming MARK_AS_OVER_ANNOTATED (P. putida does not swarm with flagella).
NEW: GO:0071977 swimming motility IMP (motCD double-gene deletion + complementation); GO:0120101 stator complex IC; GO:0015078 contributes_to IC (module MF; proton conduction not directly measured in KT2440).
Note: the project synthesis says MotCD loci were "not resolved"; PMID:36409076 resolves them as PP4336/PP4335.
