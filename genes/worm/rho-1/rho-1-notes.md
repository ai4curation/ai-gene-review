# rho-1 review notes

- Accession confirmed: Q22038 (RHO1_CAEEL, Swiss-Prot, WormBase WBGene00004357, GeneID 178458).
- No deep-research provider available; manual synthesis in `rho-1-deep-research-manual.md`.
- Full text read: PMID:16391233 (DGK-1 / ACh release), PMID:18801371 (UNC-89 GEF, thick
  filaments), PMID:22363657 (RHGF-2 GEF), PMID:21387015, PMID:28085666. Abstract only:
  PMID:7798239, 15814614, 16580995, 17848508, 23064028, 26578656, 11687661, 16921365, 24016757.

## Curation decisions worth flagging

- GO:0032794 GTPase activating protein binding (IPI PMID:22363657, with rhgf-2/Q22354):
  RHGF-2 is a RhoGEF ["RHGF-2 RhoGEF activity is specific to the C. elegans RhoA homolog
  RHO-1 as determined by direct binding, GDP/GTP exchange" PMID:22363657]. No GO term for
  "guanyl-nucleotide exchange factor binding" exists, and binding to its own GEF is part of
  the G protein cycle (GO:0003925). Row removed as wrong term; source defect recorded
  (WormBase).
- GO:0019901 protein kinase binding (IPI PMID:16391233, with dgk-1): DGK-1 is a
  diacylglycerol (lipid) kinase ["this pathway requires binding of Rho to the DAG kinase
  DGK-1" PMID:16391233]. Modified to GO:0019900 kinase binding; source defect recorded.
  The worm seed for the IBA protein kinase binding row (WB:WBGene00004357) likely derives
  from this mis-termed row, but ortholog seeds (ROCK binding by RhoA) keep the IBA plausible.
- GO:0005829 cytosol is_active_in (IBA): worm RHO-1 is mostly membrane/cytoskeleton
  associated [PMID:7798239]; signalling occurs at the plasma membrane/cortex. Marked as
  over-annotated.
- GO:0007165 signal transduction (IBA) refined to GO:0007266 Rho protein signal transduction.
- No NEW rows: phenotype data (elongation, P-cell migration, polarity) do not on their own
  pass the NEW bar; existing rows already cover the core.
- Update: the IBA GO:0019901 row was also MODIFIED to GO:0019900 kinase binding for claim
  consistency with the IPI row; protein-kinase effector binding (LET-502/ROCK) is plausible
  but not directly shown for worm RHO-1.

## 2026-10-28 PR review fixes

GO:0032794 GTPase activating protein binding (IPI, RHGF-2) changed from REMOVE to MODIFY. GO:0019899 enzyme binding was not used: oaklib shows it is not an ancestor of GO:0032794 (both are direct children of protein binding), and a GEF is not an enzyme in GO. No GEF-binding GO term exists (OLS and oaklib searched), so the replacement is an NTR, guanyl-nucleotide exchange factor binding, with a matching proposed_new_terms entry. The source_defects entry is kept.

## 2026-10-28 PR review fix: GO:0032794 source defect

The source_defects entry on the GO:0032794 GTPase activating protein binding row (IPI, PMID:22363657) now has requested_change CHECK instead of DELETE_ROW, matching the row's MODIFY to the proposed NTR guanyl-nucleotide exchange factor binding. Its explanation now says the binding is real and the row should be repointed once the pending GEF-binding term exists, not deleted.
