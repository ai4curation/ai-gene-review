# PLD4 notes

## 2026-11-22 ORGANELLES lysosome batch 2

- One GO:0005764 row (IEA, GO_REF:0000044, SL-0158). The UniProt "Lysosome" item is tagged
  ECO:0000269 to PMID:39423811 (Singh et al. 2024, Cell; full text cached and read); every other
  UniProt location item is by similarity to mouse Q8BG07.
- PMID:39423811: human PLD4 "localized to lysosomes when expressed in HMC3 cells"; affinity-isolated
  lysosomes from PLD4-expressing cells gain S,S-BMP synthase activity; catalytic-triad mutants lose
  activity but still reach lysosomes; HMC3 and HEK293T do not express PLD4 endogenously; Pld4 KO mice
  lose ~80% of spleen BMP. PMID:30111894 (full text cached): PLD3/PLD4 "most active at acidic pH
  (5–5.5) and are localized to endolysosomes" (localization cited to refs 15-17, not shown there).
- Verdict: resident enzyme with activity measured in the organelle; row stays ACCEPT (core);
  lysosome stays in core_functions.locations.
- No sub-compartment row: type II signal-anchor (TM 31-51, ECO:0000255) is one line; the lysosomal
  pool is shown only for overexpressed PLD4 in a non-expressing cell line, with no marker-controlled
  assay on endogenous PLD4 resolving membrane from lumen (MFF precedent).
