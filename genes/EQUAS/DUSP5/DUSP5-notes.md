# DUSP5 (donkey, A0A8C4MED2) - review notes

DONKEY40 cohort. All 11 GOA rows are IEA (TreeGrafter, EC mapping, InterPro2GO, UniRule, Ensembl Compara, combined). No PMIDs were cited by GOA; evidence comes from the human ortholog record, a cached paper, and a sequence comparison.

## Sequence
- Donkey 384 aa vs human Q16690 384 aa: [file:EQUAS/DUSP5/DUSP5-bioinformatics/RESULTS.md "94.79% identity over 384 paired residues"]. Catalytic Cys conserved: ["ACT_SITE Phosphocysteine intermediate: human [263] C -> donkey [263] C"]. NLS fully conserved: ["22 of 22 human residues in this span are identical"].
- Script: `DUSP5-bioinformatics/compare.py` (Biopython global alignment); human GOA download in `human-Q16690-quickgo-annotations.tsv`.

## Function
- Human UniProt: [file:EQUAS/DUSP5/DUSP5-bioinformatics/human-Q16690-uniprot.txt "Dual specificity protein phosphatase; active with phosphotyrosine, phosphoserine and phosphothreonine residues. The highest relative activity is toward ERK1."]
- [PMID:15713638 "We conclude that DUSP5 is an inducible nuclear ERK-specific MAP kinase phosphatase that functions as both an inactivator of and a nuclear anchor for ERK2 in mammalian cells."]
- Specificity: [PMID:15713638 "it inactivates ERK2 but not Jun N-terminal protein kinase or p38 MAP kinase"].

## Decisions
- Core: GO:0017017 MAPK Tyr/Ser/Thr phosphatase activity; GO:0043409 negative regulation of MAPK cascade; nucleus.
- TreeGrafter rows: endoderm formation (over-annotated; zebrafish developmental phenotype), cytoplasm (over-annotated; DUSP5 is nuclear), phosphoprotein phosphatase activity (too general), negative regulation of MAPK cascade (accept).
- ProtNLM2 GO:0017018 myosin phosphatase activity: wrong (myosin phosphatase is the PP1c/MYPT1 holoenzyme, a different phosphatase family).
