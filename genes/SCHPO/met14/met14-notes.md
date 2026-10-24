# met14 (SPAC1782.11, UniProt Q9P7G9) notes

Naming: UniProt entry KAPS_SCHPO; PomBase met14 is the ortholog of S. cerevisiae MET14
(APS kinase). Here the pombe and budding-yeast numbers coincide.

## Evidence journal

- Activity: APS kinase, APS + ATP -> PAPS + ADP (EC 2.7.1.25, RHEA:24152)
  [UniProt:Q9P7G9 "FUNCTION: Catalyzes the synthesis of activated sulfate. Required for"];
  APS kinase family, P-loop (Walker A 32..39), active site 103 [UniProt:Q9P7G9].
- Genetics: disruption causes methionine auxotrophy [UniProt:Q9P7G9 "DISRUPTION PHENOTYPE:
  Leads to methionine auxotrophy."], citing PMID:16436428 (abstract-only cache; the abstract
  focuses on met26 but compares "other methionine auxotrophs" [PMID:16436428 "This phenotype
  was not observed in other methionine auxotrophs."]).
- Localization: cytosol and nucleus in the ORFeome YFP screen (PMID:16823372, HDA).
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001382: met14 enables
  GO:0004020, occurs in cytosol, part_of GO:0000103.
- Module: aps_dependent_assimilatory_sulfate_reduction, APS kinase step of the PAPS route.
  S. cerevisiae MET14 core function GO:0004020 in cytoplasm, part of sulfate assimilation;
  consistent.

## Observations
- Nuclear signal (HDA) is from a high-throughput YFP screen; no nuclear role is known. Kept
  non-core.
- PANTHER PTHR11055 is named for the animal bifunctional PAPS synthase; met14 is a
  monofunctional fungal APS kinase (subfamily SF1).
