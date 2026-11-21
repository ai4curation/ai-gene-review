# HMGB1 notes

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

Rows: GO:0005783 IEA (GO_REF:0000044, SL-0095) and IDA (PMID:35239449); no qualifier recorded in the review; no ER sub-compartment rows.

- UniProt: "Endoplasmic reticulum {ECO:0000269|PubMed:35239449}. Note=(Microbial infection) SARS-COV-2 ORF3A promotes HMGB1 translocation from the nucleus to the cytoplasm where it is recruited by and colocalizes with ORF3A at the endoplasmic reticulum." (file:human/HMGB1/HMGB1-uniprot.txt)
- PMID:35239449 (abstract only; PMC9629087 returned no full text): [PMID:35239449 "ORF3a localizes to the ER and induces RETREG1/FAM134B-related reticulophagy through the HMGB1-BECN1 (beclin 1) pathway"].
- HMGB1 has no signal peptide, TM segment or retention motif; it is nuclear and secreted by a leaderless route, so the earlier IEA reason ("ER localization is part of HMGB1's secretory pathway") was wrong.
- Outcome: both rows changed ACCEPT -> KEEP_AS_NON_CORE (recruited cytosolic pool, infection-specific; ER batch 1 rule for A1CF/AMBRA1/BRSK2); stays at root; IDA's title-only quote replaced by UniProt and abstract quotes. Close call with MARK_AS_OVER_ANNOTATED (pool seen only with infection/ORF3a), stated in the reasons. core_functions not touched (no ER location there).
