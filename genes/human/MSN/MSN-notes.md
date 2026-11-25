# MSN PTHR23281 review notes

## 2026-11-22

- Reviewed the seeded MSN GOA rows against the existing UniProt, GOA, PANTHER
  PAINT, Reactome, and cached PMID sources without fetching new publications.
- Kept the central ERM biology as core: regulated F-actin/plasma-membrane
  linking, apical and microvillus membrane localization, filopodia, cell-shape
  control, and adhesion-molecule binding. The PTHR23281 IBA rows for plasma
  membrane, microvillus, filopodium, actin binding, cell adhesion molecule
  binding, and cell-shape regulation are consistent with the MSN branch and the
  family review.
- Kept the HOPS/Vps11 endosome maturation rows for MSN because the cached
  publication supports moesin/radixin/ezrin interaction with Vps11 and
  ERM-dependent EGFR trafficking through early and late endosomes. The remaining
  PANTHER problem is node scope: PTN001150648 also reaches Merlin/NF2 for these
  terms and should be pruned family-wide, but that is not an MSN-specific
  rejection.
- Kept T cell proliferation, T cell migration, immunological synapse formation,
  and endothelial leukocyte docking rows where the human studies directly
  support them. Marked MYADM/ICAM1 endothelial barrier and NHERF1 3D-gland
  morphogenesis calls as true but context-specific rather than core MSN
  biology.
- Removed every seeded bare GO:0005515 protein binding row under the repository
  policy: most of those interactions may be real, but bare protein binding is
  not an informative retained molecular-function annotation here.
- Left four rows unresolved from the available cache:
  GO:0003725 double-stranded RNA binding from the Raftlin/TLR3 record,
  GO:0009986 cell surface and GO:0019899 enzyme binding from the streptococcal
  GAPDH/uPAR record, and the PTHR23281 GO:0005912 adherens-junction IBA. The
  family review also leaves the adherens-junction node unresolved pending the
  broader EZR/MSN/RDX split.
- Marked the HDA nucleus hit, MYADM-derived positive regulation of gene expression, and broad protein
  catabolic process rows as over-annotations. They reflect proteomic outliers or
  downstream consequences of better-described MSN activities rather than core
  functions.
- Treated the extracellular-region colostrum hit as too general relative to the
  kept extracellular-exosome rows.
