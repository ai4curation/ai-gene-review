# daf-11 notes

## Session 2026-10-08 (claude-code)

Deep research: `just deep-research-falcon worm daf-11 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout; perplexity provider not available in this environment).
No deep-research file was created. Review based on cached publications in `publications/`,
the UniProt record, and GOA.

Annotation actions: {'MARK_AS_OVER_ANNOTATED': 5, 'ACCEPT': 19, 'KEEP_AS_NON_CORE': 29, 'MODIFY': 5, 'REMOVE': 9}

Key evidence:
- DAF-11 is a receptor-type guanylyl cyclase [PMID:10790386 "We report that daf-11 encodes one of a large family of C. elegans transmembrane guanylyl cyclases (TM-GCs)."]
- Ciliary localization in ASI, ASJ, ASK, AWB, AWC, dependent on DAF-25 [PMID:21124868 "In wild-type animals, the DAF-11::GFP protein localized to the sensory cilia of the olfactory neuron pairs ASI, ASJ, ASK, AWB and AWC"]
- Required for LITE-1 phototransduction in ASJ [PMID:20436480 "Two independent daf-11 mutant alleles, ks67 and m47, both lacked photocurrents in ASJ"]
- Required for NO-evoked ASJ calcium responses [PMID:30014846 "The daf-11(m47) mutation abolished the NO-evoked calcium transients in the ASJ neurons"]
- Dauer: daf-11 Daf-c is suppressed by cilium-structure mutants [PMID:1732156 "Dauer-constitutive mutations in one gene, daf-11, were strongly suppressed for dauer formation by mutations in the nine cilium-structure genes."]; daf-11 mutants have normal dye filling [PMID:21124868 "By contrast, daf-11 and daf-21 mutants show wild-type dye filling"]. Hence the 9 IGI "cilium assembly" rows (PMID:1732156) were REMOVED as an over-reading of epistasis.
- "dauer larval development" rows MODIFIED to GO:0061067 negative regulation of dauer larval development (Daf-c loss-of-function).
- "response to temperature stimulus" marked over-annotated: temperature dependence is of the dauer decision, not DAF-11 thermosensation (AFD uses GCY-8/18/23).
- Module note: consistent with modules/c_elegans_cgmp_sensory_transduction.yaml (DAF-11 as AWC/ASJ cGMP source).
