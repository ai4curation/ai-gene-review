# arg5 (SPBC56F2.09c, cpa1, UniProt O60060) notes

## Naming trap
- S. pombe arg5 = CPSase A small (glutaminase) subunit = S. cerevisiae CPA1. S. cerevisiae ARG5,6 = S. pombe arg11.

## Evidence
- [UniProt:O60060 "FUNCTION: Small subunit of the arginine-specific carbamoyl phosphate"]; transit peptide 1..17.
- Location conflict in UniProt: [UniProt:O60060 "SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:200419}."] vs [UniProt:O60060 "Cytoplasm {ECO:0000269|PubMed:16823372}."]. Partner arg4 is mitochondrial in the same HTP screen.
- Separate pyrimidine CPSase: [UniProt:O60060 "one, CPSase P, is part of a multifunctional protein (ura1) encoding 3"]; [UniProt:O60060 "synthase is channeled to its respective pathway, in contrast to"].

## Decisions
- HDA cytoplasm UNDECIDED; IBA/IEA cytoplasm MODIFY -> matrix.
- de novo pyrimidine nucleobase biosynthesis (InterPro2GO) REMOVE: compartmentalised, channelled CPSase A; pyrimidine CPSase is ura1. (S. cerevisiae CPA1 review only marked it over-annotated because the budding-yeast pools are shared.)
- Core: MF GO:0004359, contributes_to GO:0004088, complex GO:0005951, matrix.
