# PR6193 claim-specific source assessment

PMID12902269 is available in the immutable normal full-text cache. Native UA159/JAM1 experiments use permeabilized-cell PEP-dependent NADH oxidation, with no-PEP reference tubes. Growth phenotypes are not localization assays. Its introductory domain-role statement supports the catalytic-versus-membrane division; it is not direct UA159 localization.

PMID24928869 full primary was independently re-read at https://pmc.ncbi.nlm.nih.gov/articles/PMC4135778/ (Results, amino-sugar transport). The existing normal cache remains abstract-only. Previously acquired text: `.cache/module-audit-logs/mannose-20261107/literature-consultation/2014-mutans.txt`; SHA256 `d18dfe95725c4b17a8f58d2127ecc037b8663c6a1028e6696f3196da68cb1cc2`. Exact whitespace-normalized excerpt:

> Compared to the wild-type strain, cells lacking the manLMN operon displayed almost no detectable PTS-dependent uptake of GlcNAc and only a very low level of transport of GlcN

The assay measures PEP-dependent NADH oxidation after cell permeabilization, not isolated-subunit flux or chemical identification of the phosphorylated product. GO0022880's 6-phosphate specificity is inferred from characterized mannose-family PTS chemistry together with native amino-sugar uptake and the described NagA/NagB pathway; it was not directly resolved by this uptake readout. The intro's explicit E. coli 6-phosphate statement must not be relabeled as a UA159 product assay. This limitation does not negate the supported mechanistic inference. No specific glucosamine term is invented.

ManM topology has five PROSITE-ProRule PRU00429 TM features and its type-4 EIIC channel domain. ManN has five PRU00431 TM features and the EIID channel-domain statement. These support membrane localization by target-specific sequence inference, not native topology mapping. ManL has soluble IIA/IIB domains but no independent native membrane-association result was located. Lack of a TM helix does not disprove peripheral association; both existing membrane assertions remain unresolved. Its cytosolic relay location is a bounded domain/mechanism inference, not growth-derived localization.
