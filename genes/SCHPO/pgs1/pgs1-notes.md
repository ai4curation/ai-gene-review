# pgs1 (Q9HDW1, SPBP18G5.02) notes

Role: PGP synthase (EC 2.7.8.5), committed step of PG/CL branch; module `cdp_dag_phospholipid_synthesis` part 6.
Fetch: `just fetch-gene SCHPO pgs1` retrieved the correct accession Q9HDW1.

## Evidence
- Purified to homogeneity from S. pombe mitochondrial membranes [PMID:9468529 "In this work, we report the purification to homogeneity of PGPS from S. pombe."]
- Inner-membrane location, committed step of CL synthesis [PMID:9468529 "is located in the mitochondrial inner membrane and catalyzes the committed step in the cardiolipin branch of phospholipid synthesis"]; membrane-associated [PMID:9468529 "The enzyme was solubilized from the mitochondrial membrane of S. pombe with Triton X-100."]
- Activity in extracts regulated by growth phase and inositol [PMID:1324908 "Starvation for inositol resulted in a twofold derepression of PGP synthase and PS synthase expression"]
- Reaction and family [UniProt:Q9HDW1 "Belongs to the CDP-alcohol phosphatidyltransferase class-II"]

## Decisions
- REMOVE `GO:0016024 CDP-diacylglycerol biosynthetic process` (EXP, PMID:1324908): pgs1 consumes CDP-DAG; the paper assayed CDP-DG synthase as a separate enzyme.
- MODIFY IC `mitochondrial matrix` -> `mitochondrial inner membrane` (abstract of the cited paper states inner membrane). PomBase GO-CAM 67086be200000363 places pgs1 in the matrix.
- `mitochondrial membrane organization` IC kept as non-core.
- Core: GO:0008444 / GO:0032049 + GO:0006655 / GO:0005743 — same as the S. cerevisiae PGS1 review.
