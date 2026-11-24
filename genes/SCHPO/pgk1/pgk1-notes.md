# pgk1 (S. pombe, UniProt O60101, SPBC14F5.04c) notes

Role in module `emp_glycolysis`: phosphoglycerate kinase step (EC 2.7.2.3); S. cerevisiae counterpart PGK1.

## Evidence
- No S. pombe-specific biochemistry in cache; function by similarity [UniProt:O60101 "Catalyzes one of the two ATP producing reactions in the"], reaction [UniProt:O60101 "Reaction=(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl"].
- Single PGK gene in S. pombe (PANTHER PTHR11406 member; UniProt entry).
- Cytosol and nucleus in ORFeome screen [PMID:16823372 "we determined the localization of 4,431 proteins"].
- Mitochondrion annotations (ISS, IEA) derive from S. cerevisiae Pgk1 proteomics [UniProt:O60101 "Mitochondrion {ECO:0000250|UniProtKB:P00560}."]; kept non-core.

## Curation decisions
- ISO to obsolete GO:0061621 -> MODIFY to GO:0006096.
- ATP binding / ADP binding kept non-core.
