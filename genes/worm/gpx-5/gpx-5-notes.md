# gpx-5 notes

## 2026-10-28 initial review

- Fetched Q93204 (gene gpx-5, C11E4.1, WBGene00007516, GeneID 181178); GOA has 10 rows.
- Literature is thin: one experimental paper (PMID:23593298) with an RNAi screen; see
  gpx-5-deep-research-manual.md.
- RNAi phenotype: sensitivity to arsenite, NOT to juglone [PMID:23593298 "knockdown of an
  alpha-class related GST (gst-32), an omega-class GST (gst-44) and an extracellular
  glutathione peroxidase (C11E4.1) less profoundly affected the survival rate under
  arsenite stress"]. WormBase's IMP to GO:0000302 response to reactive oxygen species is
  therefore a lateral mis-term; GO:0046685 response to arsenic-containing substance fits
  the assay. Juglone (the ROS generator in the same screen) had no effect.
- Peroxidatic residue is Cys72 (aligns with GPX1 Sec49). Reducing substrate unknown (GSH
  vs thioredoxin); keep glutathione peroxidase activity UNDECIDED and use peroxidase
  activity as core MF.
- Secreted: SignalP 1-17, no TM, ISS to mouse secreted Cys-GPX5 (P21765) - accept
  extracellular region.
- No NEW terms proposed.
