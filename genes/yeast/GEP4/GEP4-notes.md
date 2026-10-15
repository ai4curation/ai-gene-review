# GEP4 (YHR100C, UniProt P38812) notes

## Function
- Mitochondrial PGP phosphatase (EC 3.1.3.27), HAD superfamily, PGPP1/Gep4 family [UniProt:P38812].
- "we identify a novel phosphatase in the mitochondrial matrix space, Gep4, and demonstrate that it dephosphorylates phosphatidylglycerolphosphate to generate phosphatidylglycerol, an essential step during CL biosynthesis" [PMID:20485265].
- Functional conservation with bacterial PgpA: "Expression of a mitochondrially targeted variant of Escherichia coli phosphatase PgpA restores CL levels in Gep4-deficient cells" [PMID:20485265].
- Location: inner membrane, peripheral, matrix side [UniProt:P38812, citing PMID:16823961, PMID:20485265].

## Pathway context (module cdp_dag_phospholipid_synthesis)
- Step 7 of the module: PGP -> PG, between Pgs1 (PGP synthase) and Crd1 (CL synthase).
- YeastCyc reaction list does not attach GEP4 to a reaction, but GOA still carries RCA rows from SGD_PWY:PHOS-PWY: `cytosol` (wrong; default compartment) and `phospholipid biosynthetic process` (too general).
- Not present in the gocams/index.tsv YeastPathways models.

## Review decisions
- Accept PGPase MF (IBA/IEA/IDA/IMP/IGI), CL and PG biosynthesis, mitochondrion / inner membrane / matrix / extrinsic component of MIM.
- REMOVE RCA cytosol (PHOS-PWY default compartment).
- MODIFY RCA phospholipid biosynthetic process -> GO:0006655; MODIFY deep-node IBA cytoplasm -> mitochondrial matrix.
