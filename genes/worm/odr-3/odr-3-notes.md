# odr-3 notes

## Session 2026-10-08 (claude-code)

Deep research: `just deep-research-falcon worm odr-3 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout; perplexity provider not available in this environment).
No deep-research file was created. Review based on cached publications in `publications/`,
the UniProt record, and GOA.

Annotation actions: {'ACCEPT': 15, 'KEEP_AS_NON_CORE': 9, 'MARK_AS_OVER_ANNOTATED': 3}

Key evidence:
- Gi/Go-like G-alpha in olfactory and nociceptive neurons [PMID:9459442 "The Gi/Go-like G alpha protein ODR-3 is strongly and selectively implicated in the function of C. elegans olfactory and nociceptive neurons."]
- Ciliary localization; main stimulatory olfactory G-alpha [PMID:15342507 "ODR-3 constitutes the main stimulatory signal and is sufficient for the detection of odorants."]
- Controls AWC cilia shape [PMID:9459442 "In odr-3 null mutants, the fan-like AWC cilia take on a filamentous morphology like normal AWA cilia"]
- Interacts with ODR-10 in yeast split-ubiquitin assay [PMID:25415379 "suggesting strong interactions between ODR-10 and the nematode Gα subunits and the chimaeras derived from them"]
- adenylate cyclase-modulating GPCR pathway (IBA/IEA) marked over-annotated: ODR-3 effectors are guanylyl cyclase/cGMP in AWC and TRPV OSM-9 in ASH.
- Not a NEW candidate here but noted: ASH nociception (chemical/mechanical avoidance) role [PMID:9459442 "odr-3 function is essential in the ASH neurons that sense noxious chemical and mechanical stimuli"] has no specific GO annotation in GOA; a curator could consider it.
- Module note: odr-3 (Q18434) is not in modules/c_elegans_cgmp_sensory_transduction.yaml; it would be the upstream G-alpha of the AWC ODR-1/DAF-11 step.
