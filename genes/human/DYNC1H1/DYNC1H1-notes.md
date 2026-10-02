# DYNC1H1 review notes

## 2026-09-27 (claude-code)

- Core function: catalytic heavy chain of cytoplasmic dynein 1; minus-end-directed microtubule motor
  [PMID:21723285 "In an in vitro MT gliding assay, both dynein-1 and dynein-2 showed minus-end-directed motor activities."].
  Processive motility needs dynactin plus an activating adaptor [PMID:24986880 "addition of dynactin together with the N-terminal region of the cargo adaptor BICD2 (BICD2N) gives rise to unidirectional dynein movement over remarkably long distances."].
- Nucleokinesis: dynein pulls the nucleus toward the centrosome [PMID:17618279 "The nucleus is transported along the trailing microtubules by dynein assisted by myosin II."];
  [PMID:15173193 "Dynein inhibition resulted in similar defects in both nucleus-centrosome (N-C) coupling and neuronal migration."].
  Human MCD variants [PMID:22368300]. Consistent with module assignment of GO:0008569.
- Decisions: all 56 GO:0005515 rows REMOVE (uninformative; LIS1, HTT, DISC1, CRACR2A etc.).
  "Positive regulation of intracellular transport" rows MODIFY to direct transport terms (dynein is the motor, not a regulator).
  "Positive regulation of mitotic SAC" (NAS, PMID:19229290) MODIFY to GO:1902426 deactivation of mitotic SAC
  [PMID:19229290 "Cytoplasmic dynein functions in the checkpoint, apparently by moving critical checkpoint components off kinetochores."].
  "Regulation of mitotic spindle organization" (PMID:23027904) MODIFY to GO:0040001 establishment of mitotic spindle localization (the assay is spindle positioning).
  Azurophil granule lumen / extracellular region (Reactome) REMOVE; exosome HDA, RNA-binding HDA, cold-induced thermogenesis, male germ cell nucleus MARK_AS_OVER_ANNOTATED.
- Falcon deep research (arrived mid-review) agrees; cited for retrograde axonal transport and nuclear positioning.
- New cached PMIDs: 12730604, 21820100, 22368300, 29420470.
