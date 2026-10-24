# Source-record defects for CACAO

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P41067 enables GO:0016887 ATP hydrolysis activity (IDA, PMID:20172994)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:P41067 → UniProtKB:Q46698 (TraB of plasmid pKM101, VirB4-family ATPase (866 aa))
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/ECOLI/traB/traB-ai-review.yaml`

This CACAO IDA row (2015-03-20) gives ATP hydrolysis activity to P41067, the 475 aa TraB of plasmid F (VirB10/TraB family, no Walker-A motif). The cited paper (PMID:20172994) assays the VirB4 homologue of plasmid pKM101, which is also named TraB and has its own UniProt entry, Q46698 (866 aa, plasmid pKM101). On F the VirB4-family ATPase is TraC (P18004). The row should be moved to Q46698.
