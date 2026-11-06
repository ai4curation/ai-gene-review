# pleD: c-di-GMP module member review

## 2026-11-05

Primary studies establish direct phosphotransfer and regulated cyclase activity [PMID:16176121; PMID:15075296; PMID:18455986]. PMID:18455986 includes surface-attachment experiments explicitly in CB15 (ATCC19089); PMID:15075296 localization experiments use CB15N. The two strains are not silently equated.

UniProt sequence comparison on 2026-11-05: Q9A5I5 (CB15) and B8GZM2 (NA1000/CB15N) each contain 454 identical residues, SHA-256 `6bc149e43944d296c2209be9fe59adc55f3c6ff763573b7b329d8f0b4ab83101` (hash of the unwrapped amino-acid string). Sources: https://rest.uniprot.org/uniprotkb/Q9A5I5.json and https://rest.uniprot.org/uniprotkb/B8GZM2.json. The new allosteric binding row uses ISS; original evidence codes are unchanged.

The fractionation result states “the PleD response regulator is a soluble cytoplasmic protein” [PMID:15075296]. Polar localization is retained in prose, but the membrane IEA is over-propagated. The family tree used by `just paint-losses CAUVC pleD` lacks Q9A5I5, so lineage losses could not be checked. No claim of absence of PAINT losses is made.

The four generic protein-binding rows are refined to phosphorelay response regulator activity because the kinase interactions transfer regulatory phosphate; they are not evidence that PleD is itself a kinase. Product-binding feedback is separately supported [PMID:17697997, “An allosteric c-di-GMP-binding mode”].

Falcon deep research was attempted with the standard recipe and failed with HTTP 403 authentication. No provider report was authored manually. This review uses primary-source retrieval and cached papers. Original GOA annotation payloads and UniProt/GOA files were preserved.


## PR #6062 review follow-up — 2026-11-06

Replaced the historical-background quotation supporting the NEW allosteric cyclic-di-GMP-binding row with PMID:17697997's own structural result: crosslinking the DGC domains and noncompetitive product inhibition. The sequence-identity transfer and annotation scope are unchanged.
