# ggt2 (SPAC56E4.06c, UniProt O14194) – notes

Gamma-glutamyl transpeptidase II; paralog of ggt1. Module: vacuolar GGT variant. S. cerevisiae ortholog ECM38.

## Evidence
- Activity: [PMID:15920625 "The Schizosaccharomyces pombe cells harboring plasmid pPHJ02 showed about 4-fold higher GGT activity in the exponential phase than the cells harboring the vector only, indicating that the cloned GGTII gene is functional."]
- Overexpression increases GSH and uptake, stress tolerance [PMID:15920625 "The S. pombe cells containing the cloned GGTII gene were found to contain higher levels of both intracellular glutathione (GSH) content and GSH uptake."].
- Induction: [PMID:16202243 "The synthesis of beta-galactosidase from the GGTII-lacZ fusion gene was significantly enhanced by NO-generating SNP and hydrogen peroxide in the wildtype yeast cells."]
- Location: ORFeome HDA vacuole [PMID:16823372]; UniProt vacuole membrane, type II [UniProt:O14194].

## Decisions
- Plasma membrane IBA removed (as for ECM38/ggt1). Cellular detoxification NAS kept non-core (GS-conjugate degradation; overexpression protects against Cd/Hg/DEM).
- GO-CAM: ggt2 enables GO:0036374, no occurs_in; module correctly puts fungal GGT at vacuolar membrane.
