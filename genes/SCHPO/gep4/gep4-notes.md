# gep4 (Q9Y7U3, SPCC645.02) notes

Role: mitochondrial PGP phosphatase (EC 3.1.3.27); module `cdp_dag_phospholipid_synthesis` part 7.
Fetch: correct accession Q9Y7U3.

## Evidence
- No S. pombe biochemistry or genetics; function is by orthology to S. cerevisiae Gep4 [PMID:20485265 "we identify a novel phosphatase in the mitochondrial matrix space, Gep4, and demonstrate that it dephosphorylates phosphatidylglycerolphosphate to generate phosphatidylglycerol, an essential step during CL biosynthesis"]
- S. pombe localisation: mitochondrion in ORFeome screen [PMID:16823372]. UniProt cites the same paper for "inner membrane; peripheral; matrix side" [UniProt:Q9Y7U3 "{ECO:0000269|PubMed:16823372}; Matrix side"], which a YFP screen cannot resolve — the sub-mitochondrial detail is effectively by similarity.
- GEP4 family, HAD IIIA [UniProt:Q9Y7U3 "Belongs to the GEP4 family."]

## Decisions
- MODIFY cytoplasm IBA (deep HAD node PTN002711682 with bacterial PgpA) -> mitochondrial matrix, as in the S. cerevisiae GEP4 review.
- `mitochondrial membrane organization` IC -> non-core.
- Core: GO:0008962 / GO:0006655, GO:0032049 / GO:0005759, consistent with S. cerevisiae GEP4 and with PomBase GO-CAM 67086be200000363.
