# AMH (P03971) review notes

## 2026-10-04: PAINT/affinage review

AMH is a TGF-beta family hormone that signals through its dedicated type II receptor.
- **Receptor:** [PMID:34155118 "AMH is a member of the transforming growth factor beta (TGF-β) family, which has evolved to signal through its own dedicated type II receptor, AMH receptor type II (AMHR2)."]
- **Müllerian duct regression:** [PMID:3754790 "Animal cells transfected with the human gene secrete biologically active MIS, which causes regression of the rat Müllerian duct in vitro."]

Decisions:
- **AMHR2 binding rows:** the protein-binding IPIs (x2) and the signaling receptor binding IPI are MODIFYed to GO:0005114 type II TGF-beta receptor binding, which curators already use for AMH-AMHR2 (IDA, PMID:34155118).
- **Sex determination (TAS, NAS): MODIFY to GO:0046546 development of primary male sexual characteristics.** AMH acts after SRY/SOX9 determination (PMID:12834017). Round 1 originally proposed GO:0046661, an ancestor of a term already carried.
- **PMID:14695376** is a mouse Lim1 paper whose abstract does not mention AMH.
  - The Müllerian duct regression IDA is ACCEPTed, deferring to the curator, since it is AMH's defining function.
  - The positive regulation of gene expression IMP is UNDECIDED.
- **Kept as non-core:** gonad development (IBA, IEA), ovarian follicle development, preantral follicle growth, Leydig cell differentiation, and the receptor kinase complex IPI.
- **Over-annotated:** response to xenobiotic stimulus (IEA).

## Round 1 (PR #3993 review)

- **GO:0005160 rows** are accepted at family level, with the specific-term sentence removed. Only the MODIFY rows argue for GO:0005114.
- **GO:0060391** now cites the SMAD-activation quote from PMID:20861221.
- **GO:2000355** is added to core_functions. The directionless follicle rows (GO:0001541, GO:0001546) say why they are non-core.
- **Cell-cell signaling** is now KEEP_AS_NON_CORE.
- **The Lim1 quote** is dropped from supported_by.
