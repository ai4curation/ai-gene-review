# NUMB (donkey, Equus asinus) - A0A9L0IQ95

DONKEY40 cohort review. Unreviewed TrEMBL entry, 506 aa, "Protein numb homolog".

## Sources
- Donkey UniProt record `NUMB-uniprot.txt` (PIRNR017607 function/location; PTB domain 37-173).
- Donkey GOA `NUMB-goa.tsv`: 5 IEA rows (3 TreeGrafter GO_REF:0000118, 1 SubCell GO_REF:0000044, 1 combined GO_REF:0000120). No experimental rows.
- Human ortholog P49757 UniProt record fetched to `NUMB-bioinformatics/human-P49757-uniprot.txt`. No human or mouse NUMB review exists in the repository.
- Cached publication PMID:18657069 (AAK1 regulates Numb in clathrin-mediated endocytosis; human cells).

## Sequence
- 97.03% identity to human NUMB over 505 aligned residues; exon structure matches human isoform 5 (P49757-5): retains PTB insert (human 68-78), lacks human 219-316 and 366-413 [file:EQUAS/NUMB/NUMB-bioinformatics/RESULTS.md "Its exon structure matches human isoform 5 (P49757-5, 505 aa)"].

## Biology (from human/mouse)
- Endocytic protein regulating clathrin-mediated receptor endocytosis [human UniProt "Regulates clathrin-mediated receptor endocytosis"; PMID:18657069 "Numb is an endocytic protein that is proposed to influence clathrin-coated pit assembly"].
- T102A mutant disrupts transferrin and LDL internalization [PMID:18657069 "potently disrupts transferrin and low-density lipoprotein internalization"].
- Localizes to plasma membrane (peripheral, cytoplasmic side) and endosome membrane [human UniProt SUBCELLULAR LOCATION].
- Neurogenesis: maintains radial glial progenitors (mouse genetics) [human UniProt "Plays a role in the process of neurogenesis"].
- Notch antagonism is classical literature for Numb, but neither human nor mouse GOA carries a Notch-pathway term; not proposed as NEW (comparator/convention check).

## Decisions
- cytoplasm, plasma membrane, basolateral PM, cytoplasmic vesicle: ACCEPT (consistent with human/mouse localization data and the PAINT node).
- positive regulation of neurogenesis: KEEP_AS_NON_CORE (developmental outcome; mouse genetics).
- NEW: regulation of clathrin-dependent endocytosis (GO:2000369), from the human endocytosis data.
