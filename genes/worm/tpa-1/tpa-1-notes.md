# tpa-1 review notes

## GO-CAM 568b0f9600000284 consistency notes

- The TPA-1 molecular function in `gomodel:568b0f9600000284` should be `GO:0004697` diacylglycerol-dependent serine/threonine kinase activity rather than the generic parent `GO:0004674` protein serine/threonine kinase activity.
- The GO-CAM's intestinal antibacterial context should cite PMID:19371715 for TPA-1 acting upstream of DKF-2. PMID:22470487 supports TPA-1 in epidermal `nlp` antimicrobial peptide induction after fungal infection and wounding, not intestinal antibacterial immunity.
- The GO-CAM is missing an `occurs_in` value for TPA-1. `GO:0009898` cytoplasmic side of plasma membrane is plausible by DAG/C1-domain mechanism and because TPA-1 activates membrane-recruited DKF-2, but the gene review should not assert this as a direct TPA-1 localization without a TPA-1 localization assay.
- The direct TPA-1-to-DKF-2 edge is more defensible than the direct DKF-2-to-PMK-1 edge. Ren et al. show the in vivo TPA-1/DKF-2 relationship in intestinal cells, and PKC-mediated phosphorylation of the PKD activation loop is the established mechanism.

## Deep research

- 2026-11-24: Automated deep-research provider attempts were unavailable in this checkout. `deep-research-falcon` reported no usable Falcon or Perplexity provider, and `deep-research-claude-code` could not run because the provider was not logged in. The review used the fetched GOA, UniProt, WormBase MOD description, PAINT-loss check, GO-CAM review context, and local cached PMID files instead.
