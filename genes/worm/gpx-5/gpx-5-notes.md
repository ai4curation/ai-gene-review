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

## 2026-11-24 nematode GP29 cross-check

- Rechecked the existing GPX-5 review after the Brugia malayi GP29 review landed. The
  same conservative boundary still holds for both proteins: Q93204 and P67877 are
  cysteine-type PTHR11592:SF88 GPx-fold proteins with signal peptides, so peroxidase
  activity and extracellular-region annotation are reasonable, but neither has a direct
  glutathione-versus-thioredoxin reductant assay.
- The frozen `PTHR11592-entries.csv` reviewed-member list contains filarial GP29 proteins
  from Wuchereria, Dirofilaria, Brugia malayi and Brugia pahangi plus C. elegans GPX-3, but
  it does not list Q93204/GPX-5. The current Q93204 UniProt record itself supplies the
  PTHR11592:SF88 assignment for GPX-5.
- Falcon and Perplexity Lite deep-research providers were unavailable in this checkout; the
  2026 cross-check used the cached 2026-10 manual notes, the Q93204 UniProt update, the
  Luersen et al. full text, the PTHR11592 family review, and the freshly curated BRUMA GP29
  comparison.
