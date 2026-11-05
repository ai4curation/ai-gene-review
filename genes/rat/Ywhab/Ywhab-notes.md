# Ywhab (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Ywhab` resolved P35213 (1433B_RAT, Swiss-Prot, RGD:61998, GeneID 56011);
  51 GOA rows. No deep research API keys; manual synthesis in `Ywhab-deep-research-manual.md`.
- Rat experimental rows: HCV core IPI (PMID:10644344, full text: rat 14-3-3 beta used
  directly, "bind directly to several species of 14-3-3 protein (human 14-3-3ɛ, rat 14-3-3β, and S. cerevisiae Bmh1)");
  ASK1/PP5 complex in rat hippocampus (PMID:12786973, abstract only); FBI1 repressor complex
  (PMID:18460465, abstract only).
- PMID:21454690 (full text): beta binds phospho-AS160 in rat adipocyte lysates, weaker than gamma
  [PMID:21454690 "Both 14-3-3β and 14-3-3γ precipitated AS160, but the γ isoform was much more effective and precipitated higher amounts"].
  No beta-specific vesicle enrichment; no NEW annotation proposed (binding to a specific client
  is already covered by the phosphorylation-dependent binding core MF).
- Human source checks via QuickGO (P31946):
  - GO:0004864 phosphatase inhibitor <- PMID:17255105 (PDE3B shielding from dephosphorylation) - substrate protection, not phosphatase inhibition; flagged WRONG_TERM.
  - GO:0005774 vacuolar membrane <- PMID:11260479 EXP (Chlamydia inclusion membrane) - pathogen vacuole context; flagged.
  - GO:0045944 <- PMID:10869435 (HDAC4/5 sequestration) - indirect.
  - GO:0045744 <- PMID:21224381 (AKAP-Lbc, abstract silent on 14-3-3).
  - GO:0042308, GO:0140311 <- PMID:10869435, PMID:17974916 (HDAC4, YAP).
  - GO:0048471 <- PMID:12963375 (hD53 cytoplasm colocalization).
  - GO:0019899 <- PMID:17255105 (PDE3B, IPI); GO:0019904 <- PMID:11984006 (LYST).
- Ontology checks (OAK): GO:0050815 phosphoserine residue binding is_a GO:0045309 is_a GO:0051219
  phosphoprotein binding; GO:0140031 sits under GO:0140030 modification-dependent protein binding.
