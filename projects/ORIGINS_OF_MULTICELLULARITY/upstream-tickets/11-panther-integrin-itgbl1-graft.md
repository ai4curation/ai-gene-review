# PANTHER / TreeGrafter, PTHR10082: unicellular integrin betas grafted onto the vertebrate ITGBL1 node

**Destination:** PANTHER team (pantherdb.org feedback).

**Summary.** In the PANTHER tree API (2026-10-01), node PTN002560695 in
PTHR10082 is subfamily SF3, "INTEGRIN BETA-LIKE PROTEIN 1", with species
Euteleostomi. All of its leaves are vertebrate ITGBL1. TreeGrafter grafts
unicellular holozoan integrin betas onto it. In QuickGO, the node's 9 terms
(including focal adhesion, cell-cell adhesion and cell-matrix adhesion)
reach:
- six *Capsaspora* integrin-beta entries, 54 rows in all: A0A0D2U6H2,
  A0A0D2VIQ2 and A0A0D2WRB3, plus the cDNA entries D7PE18, D7PE19 and D7PE20;
- one ichthyosporean protein (A0A0L0G967), 9 rows.

**Evidence.**
- *Capsaspora* integrin beta 2 (A0A0D2WRB3 = D7PE19, CAOG_05058) is a full
  transmembrane integrin beta with a MIDAS-type motif and NPxY-type tail
  motifs.
- An antibody against its beta-I domain reduces adhesion to
  fibronectin-coated surfaces (DOI:10.1101/2020.02.27.967653, preprint of
  PMID:32857975).
- *Capsaspora* has no fibronectin ortholog and no known matrix ligand.

**Requested change.** Graft unicellular holozoan integrin betas onto a
pre-metazoan integrin-beta node, not the vertebrate ITGBL1 subfamily. The
general fix is the taxon QC rule in [ticket 10](10-treegrafter-qc-rule.md).

**Repo references.** `genes/CAPO3/coITGB2/coITGB2-ai-review.yaml`.
