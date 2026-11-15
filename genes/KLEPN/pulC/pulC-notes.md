# pulC (Klebsiella pneumoniae, P15643) curation notes

## 2026-11-13 initial review

- Reviewed as the Klebsiella Pul exemplar of the GspC envelope connector for
  `modules/bacterial_type_ii_secretion.yaml`. The Pul system is the type II secretion system in which
  the GspC role was first defined, and it is the system whose assembled core was solved by cryo-EM.
- Deep research was not run (no provider credentials in this environment); no
  `-deep-research-<provider>.md` file was created. Sources are the cached publications and the curated
  UniProt record. PMID:2677007, the entry's only reference, was fetched for this review; PMID:10383968,
  PMID:10735856 and PMID:31780649 were located by PubMed search on PulC and fetched.
- All three GOA rows are electronic (one Swiss-Prot subcellular-location mapping, two InterPro2GO), yet
  the primary evidence for PulC is strong: inner-membrane fractionation of a PulC-PhoA hybrid and a
  requirement for pullulanase secretion [PMID:2677007], signal-anchor-mediated inner-membrane
  association [PMID:10383968], co-immunoprecipitation with PulM, PulL and PulE [PMID:10735856], and
  resolution of PulC in the assembled machine at 2:1:1:1:1 stoichiometry with its HR domain on the
  secretin base [PMID:31780649]. All three rows are therefore accepted on that evidence, and the
  absence of experimental annotations is raised as a suggested question (a curation gap, not a
  knowledge gap).
- PMID:10383968 also finds PulC with the outer membrane and reads it as a periplasm-spanning bridge
  disrupted by cell lysis; the cryo-EM structure shows the HR domain reaching only the secretin base, so
  no outer-membrane location is asserted.
- The pul genes of this entry come from the strain now classified as Klebsiella oxytoca while UniProt
  records Klebsiella pneumoniae (NCBITaxon:573). The review keeps the UniProt taxon and raises the
  discrepancy as a question rather than asserting a source defect.
