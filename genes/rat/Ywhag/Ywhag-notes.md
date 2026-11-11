# Ywhag (rat) review notes

- 2026-10-28: fetched P61983 (RGD:62002, GeneID 56010), 58 GOA rows. Most rows are ISO/IEA/ISS
  from human YWHAG (P61981). Rat experimental rows: MuSK binding (IPI, PMID:15604144), synapse
  (IDA/IEP, PMID:7964746), presynapse (IDA, PMID:16982421), GLUT4 vesicle + insulin response
  (IDA, PMID:21454690, full text read), enzyme regulator (TAS, PMID:8381897), LRRK2 binding (IPI,
  PMID:24351927).
- Checked human source rows in QuickGO (2026-10-28):
  - GO:0022409 positive regulation of cell-cell adhesion and GO:0032880 come from PMID:29678907, whose
    abstract says 14-3-3gamma "destabilized intercellular cohesion of keratinocytes" -> sign inversion;
    should be GO:0022408 negative regulation of cell-cell adhesion. Source defect recorded.
  - GO:0045664 / GO:0048167 come from a human IMP on PMID:11824616, which is a proteomic expression study
    (decreased 14-3-3 gamma in DS brain) with speculation only -> over-annotation; evidence code should
    be checked.
  - GO:0002842 / GO:0050870 from PMID:38377992 (UFL1/PD-1), abstract silent on 14-3-3 -> UNDECIDED.
  - GO:0140031 / GO:0140311 / GO:1904262 / GO:0042149 from PMID:36732624 (WDR24), full text cached and
    supports YWHAG binding phospho-WDR24 [PMID:36732624 "WDR24 specifically bound 14-3-3γ"].
  - GO:0005634 nucleus from FlyBase IDA PMID:31906564 ["14-3-3γ is only localized to the nucleus"].
  - GO:0003779 actin binding ISS uses human YWHAH (P68510, 14-3-3 eta) as With/From: paralog transfer.
  - GO:0019904 / GO:0006605 (mouse MGI IDA, PMID:12446771): 14-3-3 binds MondoA MCR III, retaining it in
    the cytoplasm.
- GO:0045202 synapse IEP row (PMID:7964746) uses an expression-pattern code for a location from a
  fractionation assay -> WRONG_EVIDENCE_CODE CHECK.
- Core: phosphoserine/threonine motif reader (GO:0140031), sequestering (GO:0140311), insulin-regulated
  AS160 binding on GLUT4 vesicles in rat adipocytes.
