# ctdspl2b notes

## Provenance and setup

- Record: A4QNX6 (Swiss-Prot CTL2B_DANRE, 460 aa), ZFIN ZDB-GENE-030131-1809, Ensembl ENSDARG00000060586 (chr7).
- Paralog: ctdspl2a (Q08BB5). DANRE_DUPLICATION batch 4 random pair (PANTHER `TGD_tree`; Ensembl
  Compara duplication node Osteoglossocephalai).
- Deep research was not available (Edison 402 Payment Required; OpenAI key invalid). Literature
  searched by hand in Europe PMC; see ctdspl2a-notes.md for queries and the mammalian literature.
  No zebrafish study of ctdspl2b exists.

## Key mammalian evidence (see ctdspl2a-notes.md)

- [PMID:26920047 "SCP4 exhibited Ser5-preferential CTD phosphatase activity in vitro, while small interfering RNA-mediated SCP4 knockdown in HeLa cells increased phosphorylation levels of Pol II at Ser5 and Ser7, but not at Ser2."]
- [PMID:28851713 "In this study, we discovered a nuclear phosphatase, SCP4/CTDSPL2 (SCP4), that dephosphorylated FoxO1/3a and promoted FoxO1/3a transcription activity."]

## My analysis (file:DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md)

- DxDx(T/V) motif DLDET at 287-291, aligned to human D293-T297; FCP1-homology domain 96.2% identical
  to human CTDSPL2; 70.9% identical to ctdspl2a overall.
- Maternal and ubiquitous, same profile as ctdspl2a at two- to three-fold lower TPM. Medaka keeps a
  one-to-one orthologue of each copy.

## Annotation decisions

- Same calls as ctdspl2a for the shared rows (MF accepted, nucleus accepted, gluconeogenesis kept
  as non-core). ctdspl2b has no root ND cellular_component row; that asymmetry is bookkeeping.
