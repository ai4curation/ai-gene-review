# ubiK (PP_5235, Q88CE6) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research (no provider keys); OpenScientist report read.
Unreviewed UniProt entry with HAMAP MF_02216 curated text. No KT2440 experiment.

- E. coli: [PMID:28559279 "we demonstrated that the UbiK protein forms a complex with the
  C-terminal part of UbiJ"]; [PMID:28559279 "both proteins are likely to contribute to global
  UQ biosynthesis rather than to a specific biosynthetic step"].
- No molecular function asserted (unknown), in agreement with the module. Added NEW
  GO:0110142 (part_of) and a BIOLOGY knowledge gap.
- Cytoplasm MODIFY to cytosol; TreeGrafter cytosol ACCEPT (PAINT IBD PTN002211000, seed E. coli
  UbiK Q46868).

Module agreement: `ubik_metabolon_accessory_factor` (GO:0006744, no MF). Consistent.
