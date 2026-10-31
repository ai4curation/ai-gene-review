# gst-32 notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm gst-32`; UniProt accession confirmed as Q9NA96
  (TrEMBL, gene gst-32, ORF Y53F4B.37, WormBase WBGene00001780, GeneID 190230).
- 5 GOA rows: GST activity (IBA, IEA/ARBA), glutathione metabolic process (IBA),
  cytoplasm (IEA/ARBA), response to ROS (IMP, WB, PMID:23593298).
- No deep-research provider available; manual research in gst-32-deep-research-manual.md.
- PubMed has no paper naming gst-32 in title/abstract. The only experimental data is the
  RNAi screen in PMID:23593298 (full text cached): gst-32(RNAi) worms are sensitive to 3 mM
  arsenite (24.0% vs 90.0% survival) but not to 0.15 mM juglone (87.8% vs 90.8%)
  [PMID:23593298 "knockdown of an alpha-class related GST (gst-32), an omega-class GST
  (gst-44) and an extracellular glutathione peroxidase (C11E4.1) less profoundly affected the
  survival rate under arsenite stress"].
- Decision: MODIFY the IMP from response to ROS (GO:0000302) to response to
  arsenic-containing substance (GO:0046685) and log a WRONG_TERM source defect for WB
  (PROBABLE: the juglone column argues against the ROS claim; arsenite-induced oxidative stress
  is the authors' interpretation, not a measurement).
- MF/glutathione metabolism IBA and the ARBA rows accepted on family grounds (GST N/C
  domains, sigma-like CDD hits, YxLxYF catalytic-Tyr motif at the N-terminus); no biochemistry
  for GST-32 exists, flagged as a suggested experiment.
- No NEW process terms: the only phenotype is an RNAi survival phenotype, already captured by
  the modified row.
