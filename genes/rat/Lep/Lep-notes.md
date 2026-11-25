# Lep (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Lep` resolved P50596 (LEP_RAT, RGD:3000, GeneID 25608); 228 GOA rows.
  First two attempts timed out on rest.uniprot.org; third succeeded.
- No deep research provider available; literature synthesis in `Lep-deep-research-manual.md`.
- Template: the human LEP review (`genes/human/LEP/`) was used for consistency of
  judgements on shared ISO-transferred terms.

### Key decisions

- Core: hormone activity, leptin receptor binding, leptin-mediated signaling pathway,
  negative regulation of appetite by leptin-mediated signaling, energy homeostasis,
  extracellular region. [PMID:9618284 "enhanced levels of tyrosine phosphorylation of STAT3
  and MAPK were detected in CHO-OBRb cells"]
- GO:0005615 extracellular space is obsolete (QuickGO, checked this session), so
  extracellular region rows are accepted rather than refined.
- DNA binding (ISO/IEA) traces to mouse MGI IDA from PMID:29519872, a paper on the
  Lnc-leptin enhancer locus contacting the Lep locus (DNA-DNA chromatin contact); the
  leptin protein does not bind DNA. Removed and recorded as a source defect against MGI.
  [PMID:29519872 "Direct interaction was detected between DNA loci of Lnc-leptin and Lep in
  mature adipocytes"]
- Megalin IPI rows (PMID:15131016, PMID:17324488): leptin is endocytic cargo of megalin
  (LRP2), not a signalling ligand of it; signaling receptor binding marked over-annotated,
  bare protein binding removed per policy.
- Phagocytosis, fatty acid catabolism, appetite/feeding behavior, ovulation, angiogenesis and
  prostaglandin secretion rows were refined to regulation terms (MODIFY) because leptin
  regulates rather than performs these processes.
- IEP "response to X" rows describe regulation of Lep expression; marked over-annotated.
- GO:0060587 regulation of lipoprotein lipid oxidation (IDA, PMID:21068181): abstract is about
  lipolysis/glyceroneogenesis in WAT and NEFA oxidation, not lipoprotein oxidation; marked
  over-annotated with a SUSPECTED wrong-term defect for RGD.
- PMID:17760865 (TRH/histamine anorexia) read in full; it is not a GOA source for Lep, and
  only discusses leptin as upstream of TRH neurons. Cited as background (LOW relevance).
