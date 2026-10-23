# hmgA (Q88E47, PP_4621) notes

## 2026-10-23 re-review (homogentisate catabolism module, step 1)

- Replaced UniProt quotes that restated labels (DE RecName, DR GO cytoplasm IEA:TreeGrafter)
  with curated evidence: UniProt FUNCTION text (ECO:0000269, PMID:15262943/PMID:23858455),
  the HAMAP-backed "Belongs to the homogentisate dioxygenase family." line, and the
  PMID:23858455 abstract [PMID:23858455 "producing maleylacetoacetate from homogentisate"].
- Iron ion binding kept non-core; supported directly by the Q88E47 crystal structures
  [PMID:23858455 "uses a mononuclear nonheme Fe(2+) to"].
- The four CollecTF rows from PMID:15262943 (GO:0000976, GO:0001217, GO:0032993, GO:0045892)
  stay REMOVE. The cached abstract explicitly names HmgR as the repressor that binds the Phmg
  promoter [PMID:15262943 "HmgR protects a region in the Phmg promoter"]. Each row now carries
  a source_defects entry (WRONG_GENE_PRODUCT, REPOINT to UniProtKB:Q88E46 hmgR/PP_4622,
  PROBABLE). Q88E46 was looked up via the UniProt REST API (gene hmgR, taxon 160488). A
  QuickGO query (2026-10-23) showed Q88E46 has no CollecTF annotation, which is consistent
  with mis-attachment. The resource enum has no CollecTF value, so the resource is OTHER.
- hmgA has no IBA rows (its PANTHER-derived IEAs come via PTN002252947/TreeGrafter). The
  family review (interpro/panther/PTHR11056/PTHR11056-review.yaml) lists Q88E47 as an SF0
  representative.
- Status set to COMPLETE.
