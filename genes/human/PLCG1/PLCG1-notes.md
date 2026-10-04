# PLCG1 (human, P19174) review notes

## 2026-09-30 initial review

Context: reviewed as the PLC-gamma output branch of the FGFR signaling module
(`modules/fgfr_signaling.yaml`, annoton `plcg1_phospholipase`, GO:0004435). Review kept
gene-centric; PLCG1 is a general RTK / immune-receptor effector.

### Core biology (with provenance)

- Catalytic activity: PIP2 -> IP3 + DAG.
  [PMID:37422272 "PLCG1 encodes phospholipase C (PLC) γ1, an enzyme activated by receptor and non-receptor tyrosine kinases and hydrolyzes phosphatidylinositol 4,5-bisphosphate (PIP2) to produce critical second messengers, including diacylglycerol (DAG) and inositol-1,4,5-trisphosphate (IP3)"]
- Human GoF variant S1021F raises IP3 and Ca2+ flux in T cells.
  [PMID:37422272 "The PLCγ1 S1021F mutant showed increased production of intracellular IP3 after anti-CD3 stimulation, as measured by IP-one ELISA"]
- FGFR docking at pY766.
  [PMID:1379697 "a fibroblast growth factor (FGF) receptor with a single point mutation at residue 766 replacing tyrosine with phenylalanine fails to associate with PLC gamma in response to FGF"]
  [PMID:23063561 "the requirement of a single phosphorylated tyrosine (pY766 for FGFR1) in the unstructured receptor C-terminal tail has been shown to be necessary and sufficient for the recruitment of PLCγ isoforms"]
  [PMID:1656221 "A tyrosine-phosphorylated carboxy-terminal peptide of the fibroblast growth factor receptor (Flg) is a binding site for the SH2 domain of phospholipase C-gamma 1."]
- SH2-dependent membrane translocation, colocalisation with EGFR and PIP2 in ruffles.
  [PMID:11331309 "The translocation of PLC gamma to the plasma membrane required the functional Src homology 2 domains"]
- T cells: SH2 binding to phosphorylated LAT.
  [PMID:10811803 "Upon T cell activation, LAT becomes highly phosphorylated on tyrosine residues, and Grb2, Gads, and phospholipase C (PLC)-gamma1 bind LAT via Src homology-2 domains."]
- Lipase-independent functions reported (mitogenesis).
  [PMID:20510673 "These data suggest that PLC-gamma1 is required for EGFR-induced SCC cell mitogenesis and the mitogenic function of PLC-gamma1 is independent of its lipase activity."]

### Decisions

- 73 `protein binding` IPIs: MODIFY -> GO:0001784 phosphotyrosine residue binding where the
  cited abstract shows pTyr/SH2-dependent binding (PMIDs 1656221, 1396585, 7993895, 8657103,
  10811803, 8384556, 24728074, 15641795, 8321198); all others REMOVE as uninformative
  (not disputing the interactions).
- GO:0004629 (C-type glycerophospholipase) -> MODIFY to GO:0004435 (assays measure IP3 from PIP2).
- GO:0008180 COP9 signalosome (IDA, PMID:22561606): REMOVE. The Tespa1 abstract speaks of the
  "TCR signalosome"; PLCG1 is not a CSN subunit. Looks like a lexical mis-mapping.
  [PMID:22561606 "Tespa1 associated with the TCR signaling components PLC-γ1 and Grb2"]
- GO:0140324 lysophospholipase C (ISS from rat): MARK_AS_OVER_ANNOTATED, no human evidence.
- GO:2000353 positive regulation of endothelial apoptosis (miRNA study, abstract-only):
  MARK_AS_OVER_ANNOTATED. GO:0002862 (Reactome FCGR3A-IL10): MARK_AS_OVER_ANNOTATED.
- GO:0005085 GEF (dynamin, rat ISS): KEEP_AS_NON_CORE; flagged as question.
- PMID:2550068 (platelet PLC purification, abstract-only) supports PLC activity / cytosol /
  PM; "PLC-II" is a recorded synonym of PLCG1. Deferred to curator (ACCEPT).
- PMID:15702972 (PLC-eta cloning) cytoplasm IDA: ACCEPT, full text not available; location
  consistent with all other evidence.
- NEW: GO:0008543 FGFR signaling pathway. Participation: PLCG1 performs the PIP2 hydrolysis
  step. Comparator: PLCG1 carries GO:0007173 (EGFR) for the same role; FRS2 carries
  GO:0008543 (QuickGO: IGI PMID:9660748, IBA); GRB2 does not. No PLCG1 ortholog (human
  P19174, mouse Q62077, rat P10686) carries GO:0008543 (QuickGO query 2026-09-30).

### Module relevance

- GO:0004435 is well supported (IBA from PTN007434641, IDA, IMP-derived via MODIFY).
- FGFR pY766 recruitment directly supported by cached PMID:1379697, PMID:1656221,
  PMID:8321198, PMID:23063561. FGFR-driven mitogenesis does not require the branch
  (title of PMID:1379697), consistent with the module marking it optional.
