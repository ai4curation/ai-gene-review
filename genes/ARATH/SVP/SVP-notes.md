# SVP (Q9FVC1) curation notes

## 2026-10-06 resolution of UNDECIDED rows

- PMID:11439126 (AP1/CAL Y2H screen, abstract only) protein binding -> MODIFY to protein heterodimerization activity; deferring to the curator that SVP was among the AP1-interacting MADS proteins [PMID:11439126 "Among the five MADS-box genes identified in this screen"]; AP1-SVP dimer independently supported by PMID:16679456.
- PMID:15805477 (MADS interactome, abstract only) protein binding -> MODIFY to protein heterodimerization activity [PMID:15805477 "revealed a collection of specific heterodimers and a few homodimers"].
- PMID:28650476 (CrY2H-seq; SVP pairs only in supplement) protein binding -> REMOVE per bare protein-binding policy (interaction not doubted).
- PMID:21709243 (GI-SVP) protein binding: changed MARK_AS_OVER_ANNOTATED -> REMOVE, as the validator policy excludes MARK_AS_OVER_ANNOTATED for GO:0005515.
- PMID:25132385 (EFM) sequence-specific DNA binding (IPI) -> ACCEPT, deferring to the curator; abstract states EFM "is directly promoted by another major FT repressor, SHORT VEGETATIVE PHASE".
- Core MF GO:0000981 is consistent with the module `vernalization_flc_silencing` annoton for SVP.
