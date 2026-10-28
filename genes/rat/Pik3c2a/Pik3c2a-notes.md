# Pik3c2a (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Pik3c2a` resolved D3ZTF6 (TrEMBL, GN Pik3c2a, RGD:1310389,
  GeneID 361632) with 46 GOA rows, as expected. First attempt timed out against
  rest.uniprot.org; the retry succeeded.
- GOA contains no rat-specific experimental rows: everything is IBA, IEA, ISS
  (from human O00443) or ISO (from human O00443 or mouse MGI:1203729), plus an ND row.
- Donor experimental annotations checked in QuickGO (2026-10-28):
  - human O00443: GO:0016303/GO:0035005/GO:0046934 IDA (PMID:9337861, PMID:11239472,
    PMID:10805725); clathrin binding IDA (PMID:11239472); endocytosis IMP
    (PMID:21081650); positive regulation of autophagy IMP (PMID:28910396);
    positive regulation of cell migration involved in sprouting angiogenesis IMP
    (PMID:26175229); locations IDA/EXP (PMID:10766823, PMID:11239472,
    PMID:11606566, PMID:21081650, HPA).
  - mouse Q61194: autophagy/starvation/PI3P synthesis IGI (PMID:24098492),
    negative regulation of zinc ion transmembrane transport IMP (PMID:23823722).
- The zinc row is puzzling: PMID:23823722 (Posor et al. 2013) is about PI(3,4)P2 in
  clathrin-mediated endocytosis, and its abstract does not mention zinc. Full text not
  cached; left UNDECIDED with a SUSPECTED source defect (CHECK) to MGI.
- PMID:24098492 used combined PI3K-C2alpha + beta siRNA in MEFs, so the mouse IGI rows
  cannot attribute the starvation phenotype to C2alpha alone; PMID:32102612 indicates
  PIK3C2A is the shear-stress (ciliary) source of PI3P, with VPS34 serving starvation.
- Key rat paper PMID:21127054 (INS1 cells, full text read): knockdown impairs insulin
  granule exocytosis at fusion (SNAP25 proteolysis), not calcium influx or Akt. This
  is phenotype evidence. Under the NEW-term bar I did not add a NEW process row
  (e.g. positive regulation of insulin secretion); instead it is recorded in the
  description, core_functions narrative and suggested experiments. A curator may want
  an RGD IMP row to GO:0032024 from this paper; raised as a suggested question.
- Sequence check from the UniProt record: catalytic loop DRHNDN at 1251 and DFG at 1269
  present; the UniProt CAUTION about missing residues for PRU00269 feature propagation
  is a feature-propagation note, not evidence of a pseudokinase.
- PX domain binds PI(4,5)P2 (PMID:17038310), so the InterPro phosphatidylinositol
  binding row is refined to GO:0005546.
- Added NEW clathrin-coated pit (ISS from PMID:11239472 / PMID:23823722) beside the
  plasma membrane rows.

## 2026-10-28: PI(4,5)P2 3-kinase activity rows (PR #5679 CI)

The two GO:0046934 rows (EC-mapped IEA, ISO from human IDA) were first KEEP_AS_NON_CORE. CI's family cross-check flagged them, because the PANTHER PTHR10048 family review scopes this activity to the class I catalytic subunits only. That matches this review's own evidence: the recombinant enzyme phosphorylates PtdIns(4,5)P2 only with a phosphatidylserine carrier, and in cells the products are PI3P and PI(3,4)P2. Both rows are now MARK_AS_OVER_ANNOTATED, and the ISO row has a propagation_review.
