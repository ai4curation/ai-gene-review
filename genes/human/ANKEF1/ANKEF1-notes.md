# ANKEF1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKEF1 (ANKRD5, Q9NU02) is an axonemal protein. Evidence from mouse (PMID:41460250, eLife, full text):
  - It binds the N-DRC subunits DRC4/GAS8 and DRC5/TCTE1, calcium-independently.
  - Ankef1-/- males are infertile, with poor sperm motility.
  - Cryo-ET shows intact but structurally heterogeneous doublet microtubules; ATP, ROS and mitochondrial potential are normal.
  - Zebrafish Ankef1a is in hair-cell kinocilia (PMID:37367482).
- **NEW (ISS from mouse):** GO:0005930 axoneme and GO:0030317 flagellated sperm motility.
  - Participation: ANKEF1 is a structural axonemal component whose loss destabilizes doublets, not just a necessary factor.
  - Comparator: the N-DRC partner TCTE1 carries both terms.
- **Calcium ion binding IEA (EF-hand):** MARK_AS_OVER_ANNOTATED. The motif check (`ANKEF1-bioinformatics/`) finds a non-canonical loop with no Glu12, and UniProt marks no Ca sites.
- **8 protein-binding IPIs** (neurodegeneration interactome, PMID:32814053): removed.
- **Knowledge gap:** MF_DARK; its activity within the N-DRC is unknown.
- Self-check (absence_check.py): the knockout proteomics shows N-DRC levels unchanged; the suggested question is reframed accordingly.

## PAINT / family analysis (added before first review)

- ANKEF1 is on the no-IBA worklist (`projects/paint/human-no-IBA.tsv`, family PTHR24127, subfamily SF1). `just fetch-panther-paint PTHR24127` reports "0 node(s), no node-level annotations".
- Reviewed members (`interpro/panther/PTHR24127/PTHR24127-entries.csv`, now committed): human ANKEF1, mouse Ankef1 (Q9D2J7), and two viral proteins (mimivirus R835, fowlpox FPV012).
  - QuickGO non-IEA annotations: human ANKEF1 has only the interactome IPIs; mouse Ankef1 has MGI ND rows only; the viral proteins have none.
  - So no IBA exists because no family member has experimental donor evidence in GO.
- The 2025 mouse knockout paper (PMID:41460250) has not yet been curated into MGI. Once it is, it would be a natural donor for axoneme and sperm-motility IBAs at a vertebrate node.
