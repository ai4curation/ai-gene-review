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


## 2026-11-06 comparative flagellar audit

The existing COMPLETE review and its three authored NEW proposals were frozen before changes. PMID36409076 maps MotCD to PP_4336/PP_4335 and tests an engineered KT2440 FliC_S267C labeling background reported to retain motility, followed by stator deletions and complementation. MotCD supports spreading and prevents sessile clusters in semisolid agar; MotAB dominates liquid swimming. Being a motor rather than a sensor does not refute participation in chemotaxis. Proton coupling remains inferred: this primary study does not measure ion flux. No inherited NEW payload or action was changed.

Default Falcon was attempted once and returned HTTP403 authentication failure; the genuine command log is retained in the ignored comparative-panel audit directory. No provider report was fabricated.

All original annotation payloads, including any inherited NEW proposals, are preserved. Only reviewer-authored judgments and synthesis were updated. Identity bridges and construct limits are recorded under analysis/module_audits/bacterial_flagellar_assembly_export/comparative-panel/.
