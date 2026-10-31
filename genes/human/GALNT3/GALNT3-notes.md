# GALNT3 review notes (2026-10-10)

Deep research: `just deep-research-falcon human GALNT3` failed (falcon timeout); literature work was done manually from
the GOA-cited papers cached in `publications/`.

## Function
- Initiating GalNAc-transferase of mucin-type O-glycosylation; recombinant enzyme active with distinct
  specificity [PMID:8663203]; "GalNAc-T1 and -T3 showed strict donor substrate specificities for UDP-GalNAc"
  [PMID:9295285].
- Key physiological substrate FGF23: "GalNAc-T3 selectively directs O-glycosylation in a subtilisin-like
  proprotein convertase recognition sequence motif, which blocks processing of FGF23" [PMID:16638743];
  "GalNAc-T3 specifically glycosylates FGF23 at Thr178 in its subtilisin-like proprotein convertase (PC) site"
  [PMID:31932717].
- Type II Golgi membrane enzyme with "Golgi lumen located catalytic, GT-A fold domain" [PMID:31932717].

## Disease (HFTC1 / HHS)
- "Both patients had low levels of the full-length FGF23 with markedly augmented amounts of the inactive
  fragments" [PMID:17129170].

## Curation decisions
- All activity rows ACCEPT; core MF GO:0004653, BP GO:0016266, location Golgi membrane.
- FGFR signaling (Reactome TAS) -> MARK_AS_OVER_ANNOTATED: GALNT3 makes the ligand, it does not signal.
- Cytoplasm (is_active_in, IEA) -> MARK_AS_OVER_ANNOTATED.
- Calcium ion binding IDA -> UNDECIDED (abstract only; cofactor is Mn2+).
- Alignment with dismech `Hyperphosphatemic_Familial_Tumoral_Calcinosis`: the GALNT3 node uses GO:0004653
  (LOSS_OF_FUNCTION) and the downstream node protein O-linked glycosylation DECREASED - consistent.
