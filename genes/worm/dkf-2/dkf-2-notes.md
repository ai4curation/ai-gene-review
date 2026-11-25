# dkf-2 review notes

## GO-CAM 568b0f9600000284 consistency notes

- The DKF-2 activity in `gomodel:568b0f9600000284` is consistent as a gene-level statement: `GO:0004674` protein serine/threonine kinase activity, `GO:0009898` cytoplasmic side of plasma membrane, and `part_of` `GO:0140367` antibacterial innate immune response match the reviewed DKF-2 core function.
- The model's `DKF-2 -> PMK-1` edge should be weakened from a direct positive regulation edge. Ren et al. showed that elevated DKF-2 increases PMK-1 dual phosphorylation and that PMK-1 is required for most DKF-2-induced immune-effector mRNAs, but also stated that the direct DKF-2 target connecting PKD to the PMK-1 pathway was unknown.
- The existing `GO:0004697` DAG-dependent kinase EC row over-specifies DKF-2 as a PKC-like kinase and was removed in the gene review. The GO-CAM already avoids this problem by typing DKF-2 with the generic but correct `GO:0004674`.

## Deep research

- 2026-11-24: Automated deep-research provider attempts were unavailable in this checkout. `deep-research-falcon` reported no usable Falcon or Perplexity provider, and `deep-research-claude-code` could not run because the provider was not logged in. The review used the fetched GOA, UniProt, WormBase MOD description, PAINT-loss check, GO-CAM review context, and local cached PMID files instead.
