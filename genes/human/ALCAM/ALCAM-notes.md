# ALCAM (Q13740) review notes

## 2026-10-04: PAINT/affinage review

ALCAM/CD166 is the ligand of CD6 on T cells.
- **CD6 ligand:** [PMID:7760007 "We prepared an ALCAM-Rg fusion protein and showed that it binds to COS cell transfectants expressing CD6, demonstrating that ALCAM is a CD6 ligand."]
- **Weak homophilic binding:** [PMID:15048703 "CD166 also interacts in a homophilic manner but with around 100-fold lower affinity"]
- **Role at the synapse:** it stabilizes T cell-DC contacts [PMID:16352806 "ALCAM-blocking antibodies interfere with DC-T-cell conjugate formation, demonstrating that CD6-ALCAM binding is essential for stable T-cell-APC contact."]

Decisions:
- **NEW GO:0098632 cell-cell adhesion mediator activity (IMP, PMID:16352806).**
  - Participation: ALCAM's own N-terminal Ig domain makes the trans contact.
  - Comparator check is positive: in human, CNTN1, NRCAM, NFASC, DSCAM, CD47 and CD200 carry it (QuickGO, 64 human annotations).
  - Before this, ALCAM had no adhesion MF.
- **CD6 interaction rows: MODIFY to GO:0005102 signaling receptor binding.**
- **Galectin interaction rows: REMOVE.** The binding is carbohydrate-dependent lectin activity of the galectin, and there is no galectin-ligand term.
- **Signal transduction (TAS): MODIFY to GO:0042102 positive regulation of T cell proliferation** (changed in round 1 of PR #3969).
  - Originally marked over-annotated on the grounds that it was "CD6's work, not the ligand's". That was wrong: GO's T cell costimulation definition includes the surface-bound ligand.
  - Costimulatory ligands do carry descendants of positive regulation of T cell proliferation or activation (ICOSLG, CD70, CD47).
  - Evidence: [PMID:16352806 "the presence of CD6-blocking antibodies or recombinant ALCAM-Fc proteins results in a strong and sustained inhibition of T-cell proliferation"]
- **Neural rows: kept as non-core.** They are ISS from chicken BEN/DM-GRASP (P42292), IEA, or IBA.
- **Also kept as non-core:** exosome and focal adhesion HDA rows, the secreted-isoform extracellular region rows, and TCR complex colocalization.
