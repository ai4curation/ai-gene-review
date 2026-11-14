# PP_4335 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK PP_4335 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK PP_4335` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL Q88EW7; MotD (MotB-like, PANTHER PTHR30329; MotB_plug + OmpA-like domains; one TM helix). Same KT2440 paper as PP_4336 (PMID:36409076); the deletion removed both PP_4336 and PP_4335.
- [PMID:31452860 "The MotA4/MotB2 complex is anchored to the peptidoglycan (PG) layer through direct interactions of the C-terminal periplasmic domain of MotB with the PG layer"]

Decisions: plasma membrane ACCEPT; membrane MODIFY -> GO:0005886. NEW: GO:0071977 IMP, GO:0120101 IC, GO:0015078 contributes_to IC (module stator MF). Not added: GO:0042834 peptidoglycan binding (MotB family inference only; no cached direct evidence for MotD) - left as a suggested question/experiment.
Note: PANTHER subfamily PTHR30329:SF20 is labelled "EXPORTED PROTEIN" and holds Q88EW7. Family-level PTHR30329 is HETEROGENEOUS (OmpA-like peptidoglycan-binding domain proteins: OmpA, Pal, OprF and others as well as MotB/PomB/LafU/MotD stator anchors), so it is not itself a stator family; the module grounds MotD at SF20.


## Taxon/module audit, 2026-11-06

PP_4335 is the MotD B-type stator subunit based on exact pair genetics and MotB_plug/OmpA architecture. PANTHER PTHR30329 is heterogeneous and is not itself a stator family; update review reasons accordingly. Proton specificity remains inferred, not measured for KT2440. The older 4:2 quotation above is historical and superseded by PMID:32929189; it is not an asserted native KT2440 stoichiometry. Retain all inherited NEW rows.

Source anchor: [PMID:36409076 "P. putida has a large gene cluster for flagellar motility comprising the genes for the stator MotCD (PP4336 and PP4335)."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.



## 2026-11-06 comparative flagellar audit

The existing COMPLETE review and its three authored NEW proposals were frozen before changes. PMID36409076 maps MotCD to PP_4336/PP_4335 and tests an engineered KT2440 FliC_S267C labeling background reported to retain motility, followed by stator deletions and complementation. MotCD supports spreading and prevents sessile clusters in semisolid agar; MotAB dominates liquid swimming. Proton coupling remains inferred: this primary study does not measure ion flux. No inherited NEW payload or action was changed.

Default Falcon was attempted once and returned HTTP403 authentication failure; the genuine command log is retained in the ignored comparative-panel audit directory. No provider report was fabricated.

All original annotation payloads, including any inherited NEW proposals, are preserved. Only reviewer-authored judgments and synthesis were updated. Identity bridges and construct limits are recorded under analysis/module_audits/bacterial_flagellar_assembly_export/comparative-panel/.


## 2026-11-11 — reconcile chemotaxis and merged flagellar audits

Retain merged flagellar evidence and decisions, including gradient-guided stator mechanics and FliG switching; retain branch primary structural references, target-specific caveats, and broad-family limits. FliN direct CheY-contact uncertainty is preserved.
