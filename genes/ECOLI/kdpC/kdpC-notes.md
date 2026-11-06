# kdpC (E. coli K-12) curation notes

## 2026-11-01 review pass

- No provider deep-research file exists for this gene; provider deep research was
  not run for this pass. Evidence came from cached publications (full text:
  PMID:28636601, PMID:30478378, PMID:34272288; abstract-only: PMID:7896809,
  PMID:9789555, PMID:356049, PMID:2849541, PMID:8499455, PMID:21711450) and the
  curated UniProt entry.
- GO:1903103 potassium:proton antiporter complex (IBA and ComplexPortal IPI on
  PMID:28636601) is defined by K+/H+ antiporter activity (GO:0015386). KdpFABC is an
  ATP-driven P-type K+ uptake pump [PMID:28636601, "Mutagenesis has been used to
  establish that K+ is transported through KdpA5,6 and that the energy of ATP is
  harnessed by KdpB7."]. Both rows set to MODIFY -> GO:0031004 with source_defects.
- Bare protein binding rows removed per policy; complex membership captured by GO:0031004.
- KdpC "catalytic chaperone"/ATP-binding model [PMID:21711450, "both ATP binding to
  KdpC and ATP hydrolysis activity of KdpFABC were sensitive to the"] conflicts with
  structures placing the KdpC soluble domain in the periplasm [PMID:28636601, "This
  topology puts the soluble domain, which appears to have a novel fold, on the
  periplasmic side of the membrane."]. ATP binding set to MARK_AS_OVER_ANNOTATED;
  GO:0008556 "enables" rows marked over-annotated (KdpC contributes_to only).
