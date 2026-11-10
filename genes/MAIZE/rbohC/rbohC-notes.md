# rbohC notes

## 2026-10-28 session

- fetch-gene resolved A5H238 as expected (GeneID 100101532, PeroxiBase 5489); GOA has
  6 IEA rows (InterPro2GO, UniProt combined IEA, GO_REF:0000108).
- No deep-research key; wrote rbohC-deep-research-manual.md by hand.
- Key papers: PMID:19592501 (cloning, 948 aa, ABA induction), PMID:20693409 (BR induction,
  expression only), PMID:36045577 (Gao 2022, abstract only: ZmRBOHC stomatal ROS, drought),
  PMID:41792868 (Fu 2026: Zmrbohc mutant, attenuated chitin ROS burst, GSR susceptibility).
- Identity of the ZmRBOHC in Gao/Fu with A5H238: probable (OsRBOHC ortholog; NCBI
  "respiratory burst oxidase3", web database ZmRBOHC/ZmRBOH9/rboh3), but neither cached text
  gives a gene id, so they are cited as MEDIUM relevance and not used to create new rows.
- Decisions: peroxidase activity REMOVE (wrong InterPro2GO mapping, source_defect),
  cellular oxidant detoxification REMOVE (derived from that), oxidoreductase / NAD(P)H-O2
  oxidoreductase / membrane MODIFY to GO:0106292 / GO:0005886, calcium ion binding
  KEEP_AS_NON_CORE. No NEW process rows: the genetic data (stomatal closure, defense to
  Fusarium) are phenotypes from papers whose gene identity is not fully confirmed;
  raised as suggested questions instead.
- Followed the ZmrbohB review (genes/MAIZE/LOC100037794) for consistency.
