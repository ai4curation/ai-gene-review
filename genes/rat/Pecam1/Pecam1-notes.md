# Pecam1 (rat) review notes

## 2026-10-28 session

- fetch-gene resolved Q3SWT0 (PECA1_RAT, RGD:61927, GeneID 29583); GOA 69 rows all keyed to Q3SWT0.
- No deep-research provider; wrote `Pecam1-deep-research-manual.md` from cached papers.
- Full text available: PMID:17662049 (RBE4, PECAM-1 counteracts ICAM-1 signaling), PMID:18466611
  (IFN-gamma/TGF-beta regulation of expression). Abstract only: PMID:8248808, PMID:10861081,
  PMID:9148965, PMID:9388260, PMID:22592748, plus added background PMID:8340753, PMID:16163360,
  PMID:9252369.
- Human PECAM1 (P16284) donor annotations were checked in QuickGO (2026-10-28) to see what the ISO
  rows rest on. Notable: GO:0072011 glomerular endothelium development ISO is from a human IEP row
  (PMID:17464107), i.e. expression propagated as involvement; GO:0048018 receptor ligand activity
  from human IDA PMID:9551996 (CD31 as CD38 ligand; not read).
- Key decisions:
  - Core: homophilic cell-cell adhesion at endothelial junctions; diapedesis/neutrophil and monocyte
    extravasation; ITIM/SHP-2 inhibitory signaling (protein phosphatase binding, counteracting
    ICAM-1/RhoA); mechanosensing.
  - cell adhesion / cell-cell adhesion rows -> MODIFY to homophilic and leukocyte cell-cell adhesion.
  - regulation/positive regulation of cell migration -> MODIFY to positive regulation of leukocyte
    migration (and endothelial cell migration for human-sourced row).
  - IEP response-to-cytokine rows -> MARK_AS_OVER_ANNOTATED (expression change only).
  - immune response IBA -> MARK_AS_OVER_ANNOTATED (Fc-receptor-family node; PECAM1 role is trafficking).
  - cytoplasm and smooth muscle contractile fiber (mouse ISO) -> MARK_AS_OVER_ANNOTATED.
  - T cell activation, bicellular tight junction assembly -> UNDECIDED (donor papers not read).
