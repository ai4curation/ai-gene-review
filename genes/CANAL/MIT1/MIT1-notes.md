# MIT1 notes

## PTHR32385 / IPC mannosyltransferase review, 2026-11-06

- `MIT1` (`CAL0000176496`, UniProt `A0A1D8PIF7`) is the C. albicans PTHR32385
  IPC mannosyltransferase and a direct CGD seed for the `PTN001285482`
  `GO:0000030` IBD node.
- Mille et al. 2004 identified MIT1 as a SUR1 homologue required for IPC
  mannosylation. The abstract reports that disrupting both copies prevented
  MIPC synthesis and blocked downstream phospholipomannan beta-1,2
  mannosylation.
- A manual search found the 2004 MIT1 disruption paper and later papers that
  build on its phospholipomannan biology, but no direct Candida Mit1
  localization study. The 2023 fission-yeast MIPC/cell-wall paper is
  paralog-specific to S. pombe and not used for MIT1.
- The `GO:0000030` IBA from `PANTHER:PTN001285482` is sound but generic now
  that GOA already carries `GO:0103064 inositol phosphorylceramide
  mannosyltransferase activity` by an EC/Rhea IEA. The exact EC/Rhea row is the
  core molecular function.
- The `GO:0051999` IBA from `PANTHER:PTN001285482` is sound. The node is seeded
  by MIT1, A. fumigatus MitA, the three S. pombe Imt proteins, and the S.
  cerevisiae Sur1/Csh1 enzymes.
- The root `GO:0005575 cellular_component` ND row was created by CGD in 2026
  and remains valid: ARBA/UniProt predict a membrane protein, but no literature
  located the C. albicans Mit1 protein more specifically.
