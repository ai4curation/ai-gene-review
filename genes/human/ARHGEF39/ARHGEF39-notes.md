# ARHGEF39 notes

- ARHGEF39 is a minimal DH-PH Dbl-family GEF (C9orf100); it promotes HCC proliferation and migration [PMID:22327280].
- **Substrate:**
  - FRET biosensors in HEK293FT: activates RhoA, not Rac1 or Cdc42 [PMID:35959104].
  - Lung adenocarcinoma: called a Rac-GEF needed for EGF/HGF-driven migration, but ARHGEF39 knockdown did not significantly lower global Rac1-GTP [PMID:34731623].
  - Core function therefore lists RhoA as the substrate.
- Location: plasma membrane and focal adhesions (Müller et al. 2020, cited in PMID:35959104).
- **GOA calls:**
  - GEF activity (IEA), plasma membrane (IBA/IEA/IDA) and positive regulation of cell migration (IBA/IDA) → ACCEPT.
  - IBA node PTN002931692 is seeded by ARHGEF39 itself.
  - Y2H/AP-MS protein binding (CALCOCO2, TIFA, Q2T9J0) → REMOVE.
- Review round (PR #4169), substrate evidence balanced:
  - For RhoA: overexpression activates the RhoA biosensor [PMID:35959104]. Caveats:
    - The effect appears only at the highest transfection ratio.
    - The Müller 2020 family screen [PMID:32203420] saw no RHOA/RAC1/CDC42 activation.
    - Zhou 2018 pulled down RAC1, not RHOA.
  - For Rac1: knockdown abolishes EGF-induced Rac1 activation by FRET [PMID:34731623].
  - RhoA is kept as the core substrate because overexpression activation is closer to direct exchange.
- Plasma membrane rows now cite PMID:34731623 first-hand: cytosolic at rest, moving to the PM and ruffles on EGF/HGF.
