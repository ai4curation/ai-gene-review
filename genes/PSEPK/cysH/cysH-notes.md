# cysH curation notes

## First-pass synthesis

- Q88KG2 is assigned EC 1.8.4.10 and the direct reduction of APS to sulfite
  using thioredoxin [UniProtKB:Q88KG2, "Catalyzes the formation of sulfite from
  adenosine 5'-phosphosulfate (APS) using thioredoxin as an electron donor"].
- The record also carries a conflicting electronic PAPS-reductase GO
  annotation. Because the exact reaction and APS-reductase family assignments
  agree, GO:0004604 was removed while GO:0043866 was accepted.
- The [4Fe-4S] cluster is integral but is retained as a non-core supporting
  property rather than duplicated as another core function.

## Boundary decision

CysH is the middle reaction of the direct APS route. An APS-kinase/PAPS-reductase
route is not included in this module instance.


## Comparative sulfate-assimilation audit — 2026-10-26

Re-reviewed all eight rows, preserving the existing NEW sulfate-assimilation proposal. Native P. aeruginosa biochemical discrimination of APS versus PAPS ([PMID:10613872]), cluster evidence ([PMID:11940598]), and KT2440 HAMAP/APS-specific domain evidence support the conserved direct-APS reaction. Cytoplasm and the cluster are core-associated properties. Existing OpenScientist report was consulted as discovery, not substituted for primary evidence. PAPS reductase removal is based on substrate and domain divergence, not the broad family name.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.
