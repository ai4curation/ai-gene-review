# eno102 (S. pombe, UniProt Q8NKC2, SPBPB21E7.01c) notes

Role in module `emp_glycolysis`: enolase step (EC 4.2.1.11), second paralog.

## Evidence
- Only reference in UniProt is the genome sequence; function by similarity to S. cerevisiae ENO1 [UniProt:Q8NKC2 "Evidence={ECO:0000250|UniProtKB:P00924};"].
- Own analysis: global alignment with eno101 gives about 66% identity, and all annotated catalytic (E212 proton donor, K346 proton acceptor), substrate and Mg2+-binding residues are conserved [file:SCHPO/eno102/eno102-bioinformatics/RESULTS.md "All annotated functional residues conserved: True"].
- No GOA PMIDs (fetch-gene-pmids found none); no HDA localisation row, unlike eno101.

## Curation decisions
- All activity rows ACCEPTed on sequence grounds; ISM to obsolete GO:0061621 -> MODIFY to GO:0006096.
- Core location given as cytoplasm (only evidence is by-similarity IEA).

## Naming trap
- UniProt synonym eno1 is shared with eno101.
