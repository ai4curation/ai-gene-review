# met16 (SPAC13G7.06, UniProt Q10270) notes

Naming: UniProt MET16_SCHPO; ortholog of S. cerevisiae MET16 (PAPS reductase, E. coli CysH).

## Evidence journal

- Activity: thioredoxin-dependent PAPS reductase, PAPS + [thioredoxin]-dithiol -> sulfite +
  adenosine 3',5'-bisphosphate + [thioredoxin]-disulfide (EC 1.8.4.8, RHEA:11724)
  [UniProt:Q10270 "FUNCTION: The NADP dependent reduction of PAPS into sulfite involves"];
  PAPS reductase family, CysH subfamily [UniProt:Q10270].
- Genetics: deletion causes methionine auxotrophy [UniProt:Q10270 "DISRUPTION PHENOTYPE:
  Leads to methionine auxotrophy."] (UniProt cites PMID:16436428).
- Electron donor: the cytosolic thioredoxin trx1 is the primary donor; trx1 deletion causes
  cysteine auxotrophy rescued by sulfite [PMID:18758731 "This suggests that Trxl serves as a
  primary electron donor for 3'-phosphoadenosine-5'-phosphosulfate (PAPS) reductase"].
  Met16 is listed among thioredoxin-recycled enzymes [PMID:28640807 "These two cascades have
  to recycle enzymes which suffer disulfide formation as part of their catalytic functions,
  such as the essential Cdc22 and the non-essential Tpx1, Mxr1 or Met16 (Fig 1A)."].
- Localization: cytosol and nucleus (ORFeome YFP, PMID:16823372).
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001388: met16 enables GO:0004604
  in cytosol, part_of GO:0000103; trx1 (GO:0009055) provides input for met16.
- Module: aps_dependent_assimilatory_sulfate_reduction, PAPS-reduction step. S. cerevisiae
  MET16 core function GO:0004604, cytosol, sulfate assimilation; consistent.

## Observations
- No experimental GOA row exists for met16 itself (all IBA/IEA/HDA); the pombe-specific
  evidence is the deletion phenotype cited by UniProt and the trx1 genetics.
- GOA has no GO:0000103 sulfate assimilation row for met16 (only GO:0006790 and GO:0070814);
  core_functions uses GO:0000103, matching the GO-CAM part_of and the S. cerevisiae review.
