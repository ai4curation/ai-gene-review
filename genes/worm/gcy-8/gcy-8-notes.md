# gcy-8 notes

## Session 2026-10-08 (claude-code)

Deep research: `just deep-research-falcon worm gcy-8 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout; perplexity provider not available in this environment).
No deep-research file was created. Review based on cached publications in `publications/`,
the UniProt record, and GOA.

Annotation actions: {'MARK_AS_OVER_ANNOTATED': 1, 'ACCEPT': 20, 'REMOVE': 1, 'KEEP_AS_NON_CORE': 10}

Key evidence:
- AFD-specific GCY-8/18/23 subfamily, sensory-ending localization [PMID:16415369 "GFP-tagged GCY-8, 18, and 23 were localized exclusively to the sensory endings of AFD"]
- Direct cyclase activity and Cl- inhibition [PMID:27062922 "First, while hNPR1 has essentially no basal activity, as previously reported, GCY-8-expressing cells show significant activity, as predicted by our genetic data."]
- GCY-8 alone needed for execution of isothermal tracking and AFD responses to oscillating temperature [PMID:21315599 "Thus, while all three rGC genes play roles in regulating the temperature range in which IT behavior can be exhibited, only gcy-8 regulates the ability of the AFD neurons to execute IT behavior."]
- Microvilli shape control via cGMP/WSP-1 [PMID:27062922 "GCY-8, along with PDE-1 and PDE-5, modulate neuron cGMP levels, and cGMP antagonizes WSP-1, which promotes NRE elongation, presumably through actin nucleation."]
- Protein kinase activity (IEA) REMOVED: kinase-homology domain predicted catalytically inactive (UniProt).
- Peptide receptor activity IBA marked over-annotated (no peptide ligand; only known ECD regulator is inhibitory Cl-).
