# KNAT1 (BREVIPEDICELLUS) review notes

## Session 1 (create review)

- fetch-gene resolved P46639 (KNAT1_ARATH, Swiss-Prot; TAIR AT4G08150; GeneID 826364). 74 GOA rows,
  54 of them bare GO:0005515.
- No deep-research API; literature synthesis is in `KNAT1-deep-research-manual.md`.
- PMID:23133401 (Gonzalez-Reig 2012, fruit mediolateral patterning) read in full; it is not cited
  in GOA. BP promotes replum development and limits JAG/FIL expression [PMID:23133401
  "Medial factors autonomously constrain lateral factors so that they only express outside the replum"].
  No NEW process term proposed from it: the evidence is mutant/misexpression phenotype plus
  expression, which does not meet the NEW bar.
- Protein-binding policy: rows whose partner is a BELL/BLH TALE protein (BEL1, PNY/BLH9, BLH4, BLH6,
  BLH7, PNF/BLH8, ATH1) -> MODIFY to GO:0046982 protein heterodimerization activity
  [PMID:11701881 "can selectively heterodimerize with specific KNAT homeodomain proteins"].
  Other partners (OFP-independent screen hits, CCT, AGO10/PNH, bZIP30, SWI3B, CAND1 etc.) -> REMOVE
  as uninformative; removal does not dispute the interactions.
- GO:0003700 rows (IBA, 2x ISS) -> MODIFY to GO:0000981, the core MF. GO:0003676/GO:0003677 IEA ->
  MODIFY to GO:0000978 (OAK: GO:0000978 has ancestors GO:0000976, GO:0043565, GO:0003677, GO:0003676).
  GO:0006355 IEA -> MODIFY to GO:0006357.
- Cell fate specification IMP (PMID:7866029) rests on 35S overexpression (lobed leaves); marked
  over-annotated. Cell fate commitment, xylem and phloem pattern formation, xylem development IMP
  rows kept as non-core developmental roles.
- PMID:31806676 eY1H: KNAT1-MP promoter interaction is in supplementary data, not in the cached text;
  accepted (deferring to curator) as KNAT1 is a homeodomain TF.
