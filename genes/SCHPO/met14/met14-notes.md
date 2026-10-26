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


## 2026-10-26 complete fungal-member reassessment

Reassessed all 11 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

The conserved APS-kinase reaction and nucleotide-binding architecture support ATP binding as core, not peripheral. PMID:1654509 is budding-yeast structural-gene evidence and is explicitly used as ortholog support. Native methionine-pathway phenotype evidence (PMID:16436428) is retained with curator deference: its abstract foregrounds met26 and does not establish that met14 was absent from the full experimental comparisons. No wrong-gene claim or REMOVE is inferred from the title. Complete cellular-component and broader pathway rows were assessed, not only the module step.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids SCHPO met14` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-SCHPO-met14-*.log`.
