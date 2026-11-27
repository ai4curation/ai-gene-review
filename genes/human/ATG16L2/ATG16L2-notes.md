# ATG16L2 notes

## 2026-10-05 review (PAINT, affinage)

- Complex but no canonical role [PMID:22082872 "Based on these results, we concluded that Atg16L2 is not required for canonical autophagy, despite forming an ~800-kDa complex with Atg12–5 and having E3-like activity."].
- Location [PMID:22082872 "A subcellular distribution analysis indicated that, despite forming the Atg12–5-16L2 complex, Atg16L2 is not recruited to phagophores and is mostly present in the cytosol."].
- NOT rows (ISS from mouse): I accepted NOT autophagosome assembly and NOT autophagosome. NOT autophagy is UNDECIDED, because later mouse knockouts report that ATG16L2 positively regulates LPS-induced autophagy flux [PMID:35426127, abstract-only] and has lineage-specific autophagy roles [PMID:31451676].
- Nucleoplasm (HPA IDA) is UNDECIDED: the mouse study judged nuclear EGFP signal a tagging artifact.
- IPI complex row (PMID:23202584): the cached structural paper does not mention ATG16L2. Accepted anyway, deferring to the curator, since the complex is independently established.
- Inflammasome roles (NLRP3, NLRC4/NAIP) come from single abstract-only mouse studies. No NEW terms are proposed; they are recorded in the knowledge gap.

## 2026-10-05 revision (reviewer round 1)

- NOT autophagy is now ACCEPTed. The later mouse data (PMID:35426127) describe action on the ATG5-12-16L1 complex, which is regulation of autophagy and so compatible with a NOT involved_in row. This matches the NOT autophagosome assembly reasoning.
- core_functions now carries contributes_to_molecular_function GO:0019776 Atg8-family ligase activity, as in the ATG16L1 review [PMID:22082872 "S5 ), indicating that the Atg12–5-16L2-N complex has the ability to function as an E3-like enzyme, the same as the Atg12–5-16L1-N complex does."]. Caveat: shown only with a membrane-targeted N-terminal fragment (Kras-CAAX fusion).
- PMID:23202584 now has a reference_review, with correctness left unset because support cannot be judged from the cache. The Crohn/SLE description claim now traces to PMID:31451676. The HPA reliability score was not checked.
