# ANAPC10 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC10/DOC1 is a constitutive core APC/C subunit [PMID:10318877 "APC10 is a genuine APC subunit whose cellular levels or association with the APC are not cell cycle-regulated"].
- **Mechanism:** with CDH1 it forms the D-box co-receptor [PMID:21107322 "Cdh1 and Apc10, identified from difference maps, create a co-receptor for the D-box following repositioning of Cdh1 towards Apc10."]. Loss of Apc10 inactivates the APC/C without disassembling it (PMID:10318877).
- **In vivo:** the mouse Os allele disrupts Apc10 and blocks the metaphase-to-anaphase transition (PMID:11247669).
- **GOA rows (58):**
  - 36 Reactome TAS cytosol/nucleoplasm rows are accepted, following the CDC27 precedent.
  - All APC/C complex, APC/C-dependent catabolism and chain-type (K11, K48, branched) rows are accepted.
  - The IBA contributes_to ubiquitin protein ligase activity row is accepted. It is the right MF for a non-catalytic substrate-recognition subunit.
- **Protein binding IPI (PMID:34595750, FBXO43/EMI2):** removed. It describes an inhibitor binding the APC/C, and the WITH/FROM field oddly lists ANAPC10 itself.
- **Regulation of meiotic cell cycle (NAS):** kept as non-core; there is no APC10-specific meiotic evidence.
- **Not added:** affinage also reports SMAD3/HEF1 (PMID:15144564), NLRP3 (PMID:34407203) and centrosome/kinetochore localization (PMID:10498862). These are single studies, so no NEW terms were proposed.

## 2026-10-04 round 2 (reviewer comments on #4055)

- **GO:0000278 mitotic cell cycle (IBA):** MODIFY to GO:0007091 metaphase/anaphase transition of mitotic cell cycle.
  - Verified with OLS that GO:0007091 is_a GO:0000278.
  - Follows the ANAPC11 precedent; ANAPC2, CDC20 and CDC27 also carry GO:0007091.
  - propagation_review: TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH.
  - GO:0007091 added to core_functions.
- **K11 row from PMID:29033132:** now quotes its own paper.
- **Other fixes:** a label typo; the cytoplasm row now points to the Reactome cytosol rows; the description mentions CDC20 as the other coactivator.
- **Meiosis:** the reason now notes that APC10 binds FBXO43 in testis extracts (PMID:34595750). Still KEEP_AS_NON_CORE.
