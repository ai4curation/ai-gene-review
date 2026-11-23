# APAF1 notes

## 2026-09-30 APOPTOSIS review

- Seeded human APAF1 and reviewed all 70 GOA rows against cached GOA,
  UniProt, Reactome, PANTHER-family, and primary-publication evidence.
- Treated APAF1 as the cytochrome-c- and nucleotide-activated apoptosome
  scaffold for intrinsic apoptotic signaling, with core functions covering
  apoptotic cysteine-endopeptidase activator activity, CASP9 CARD-domain
  binding, and ADP-dependent NB-ARC switching.
- Tightened broad apoptosis rows (`GO:0006915`,
  `GO:0042981`, `GO:0043065`, and `GO:0097190`) to
  `GO:0097193 intrinsic apoptotic signaling pathway` where the source supported
  the canonical apoptosome role.
- Replaced the CASP9 `GO:0005515 protein binding` rows from the apoptosome
  structural/biochemical literature with `GO:0050700 CARD domain binding`;
  removed the cytochrome-c, AVEN, NAIP, PPP1CA, and YWHAE generic
  protein-binding rows rather than preserving uninformative flat interactions.
- Marked stimulus, tissue, and phenotype terms transferred from mouse or rat
  (`response to hypoxia`, `response to nutrient`, kidney/cardiac/system
  development, ER-stress-specific intrinsic apoptosis, TGF-beta response, and
  related anatomy terms) as over-annotations of APAF1's core apoptosome
  activity.
- Left cached abstract-only rows as `UNDECIDED` when the abstract did not expose
  the curator-visible APAF1 assay: CARD8/CASP9/complex rows from PMID:11821383,
  TRIAP1/p53CSV from PMID:15735003, and the UniProt TAS rows backed only by the
  broad PMID:18309324 review abstract.
- Flagged PMID:10383829 as a wrong supporting PMID for the broad nucleotide
  binding row; the paper is about soluble receptor-like PTP-kappa, while
  APAF1's nucleotide switch is supported by the 1999 Hu et al. and Saleh et al.
  biochemical papers.
