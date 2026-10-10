# SUR2 (SYR2; YDR297W, P38992) notes

## Identity and activity
- Sterol desaturase / fatty acid hydroxylase (His-box diiron) family; sphingolipid C4-hydroxylase converting sphinganine and dihydroceramide to phytosphingosine/phytoceramide, cyt b5-dependent [UniProt:P38992].
- Genetic and biochemical evidence [PMID:9556590 "yeast strains carrying a disrupted SYR2 allele produced sphingoid long chain bases lacking the 4-hydroxyl group present in wild type strains"; "4-hydroxylase activity was increased in microsomes prepared from a SYR2 overexpression strain"].
- Not essential [PMID:9556590 "that this hydroxylation is not essential for growth"].
- ER localization [PMID:8868422 "shown to encode a 349 amino acid protein located in the endoplasmic reticulum"].

## Curation decisions
- IBA sphingolipid delta-4 desaturase activity (PTN000933245, donor S. pombe SPBC887.15c) REMOVED: Sur2 hydroxylates C4; delta-4 desaturation is the DEGS family, absent from S. cerevisiae. PAINT node worth checking.
- YeastPathways RCA cytosol -> MODIFY to ER membrane.
- Core MF GO:0102772 sphingolipid C4-monooxygenase activity (EC 1.14.18.5). Note the GO definition is written for dihydroceramide; free sphinganine (RHEA:33519) is not among its Rhea xrefs, although YeastPathways uses the free-base reaction.
