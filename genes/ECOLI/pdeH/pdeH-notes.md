# pdeH: c-di-GMP module member review

## 2026-11-05

The purified YhjH assay and E48A catalytic control support c-di-GMP cleavage [PMID:18765794, “Purified YhjH was active as a c-di-GMP-cleaving phosphodiesterase”]. Global-pool measurements establish why its depletion affects multiple outputs [PMID:29018125]. This does not mean every DGC/PDE acts on one uniform cellular pool.

The full PMC text of PMID:26553851 was inspected online (https://pmc.ncbi.nlm.nih.gov/articles/PMC4719445/): PdeH is described as a soluble PDE without a signal-input domain. The standard cache refresh still returned abstract-only material, so no full-text quotation is asserted against that cache. The membrane IBA is marked over-annotated based on target-specific architecture and published localization description. No IRD/IKR loss was found by `paint-losses`.

The UniProt disruption text says “80% reduced concentrations of c-di-GMP” for a pdeH deletion. This conflicts with the primary measurements of elevated c-di-GMP in the deletion and is not used as support. The curated review follows the primary papers.

Falcon deep research was attempted with the standard recipe and failed with HTTP 403 authentication. No provider report was authored manually. This review uses primary-source retrieval and cached papers. Original GOA annotation payloads and UniProt/GOA files were preserved.


## PR #6062 second follow-up — 2026-11-06

Follow-up review corrected the unsupported attribution of soluble/cytoplasmic localization to the abstract-only PMID:26553851 cache. The membrane IBA concern is now explicitly based on the curated EAL-domain architecture, with a verbatim UniProt domain quote, and does not claim direct localization evidence or assert a substitute compartment.
