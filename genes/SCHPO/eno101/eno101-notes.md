# eno101 (S. pombe, UniProt P40370, SPBC1815.01) notes

Role in module `emp_glycolysis`: enolase step (EC 4.2.1.11); S. cerevisiae counterparts ENO1/ENO2.

## Evidence
- Reaction [UniProt:P40370 "Reaction=(2R)-2-phosphoglycerate = phosphoenolpyruvate + H2O;"]; Mg2+ cofactor and homodimer by similarity [UniProt:P40370 "Note=Mg(2+) is required for catalysis and for stabilizing the dimer."].
- No S. pombe-specific enzymology in GOA references; cytosol and nucleus in ORFeome screen [PMID:16823372 "we determined the localization of 4,431 proteins"].
- Paralog eno102 (Q8NKC2) about 66% identical, full active site retained [file:SCHPO/eno102/eno102-bioinformatics/RESULTS.md "All annotated functional residues conserved: True"].

## Curation decisions
- ISM to obsolete GO:0061621 -> MODIFY to GO:0006096.
- Mg binding kept non-core (S. cerevisiae ENO1/ENO2 reviews used ACCEPT; difference is only in emphasis).
- No gluconeogenesis annotation exists in GOA for either S. pombe enolase (S. cerevisiae ENO1/ENO2 core functions include gluconeogenesis); not proposed as NEW here.

## Naming trap
- UniProt gives synonym eno1 to BOTH eno101 and eno102; key on accession.
