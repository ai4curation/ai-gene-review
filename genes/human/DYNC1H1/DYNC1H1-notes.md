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


## 2026-10-18 source-preserving reassessment

The current assessment supersedes earlier blanket interaction removals while preserving the original source assertions and notebook. All 159 imported assertions remain exact: 75 ACCEPT, 54 KEEP_AS_NON_CORE, 28 MODIFY and two UNDECIDED; no NEW rows or source retirement were introduced. The 56 generic-binding sources were individually reassessed: 20 have supported partner-class refinements and 36 retain positive non-core associations. The project-specific generic-binding policy in [CLINGEN_MENDELIAN](../../../projects/CLINGEN_MENDELIAN.md) retains supported GO:0005515 when no informative refinement is established.

Three repeated motor-core entries are consolidated into one minus-end motor mechanism with transport, nuclear movement and mitotic roles. The four process terms were checked for typed ancestor redundancy. Nuclear movement includes mouse dynein-complex perturbation, and checkpoint silencing includes LIC1 perturbation; neither is described as a directly measured human heavy-chain-specific experiment. All 185 inherited annotation quotation occurrences are preserved. The 15 excerpts attached to the replaced redundant core entries are removed with explicit scientific approval; their references and original source caches remain. No new excerpts are introduced.

The two unresolved claims concern a source-specific filopodium observation and granule-lumen attribution. Positive RNA-capture, extracellular-vesicle, membrane-associated, meiotic nuclear-envelope and stress-response observations are retained with assay and organism limits. A validated partner class does not transfer its catalytic activity or physiological role to DYNC1H1. The PSEN2 co-IP band-size discrepancy, recorded interaction fragments and inferred ATP23 class remain explicit.

The official record contains one 4,646-residue Q14204 product and no alternative-product block. Historical experimental inserts, host species and reference-sequence checksums do not independently authenticate a natural product. Current PANTHER data place the exact target in PTHR10676; the older family pointer is preserved as historical input. Literal IBD placement and target descent support all nine inherited assertions.

Existing machine inputs, seven histories, provider artifacts and all preexisting main publication caches remain byte-identical. Genuine normal-fetch variants are retained privately and are not substituted for protected caches. The configured provider attempt and fallback failed; no provider text was fabricated. New publication additions are restricted to genuinely fetched references needed by the reviewed evidence.

See the [source evidence guide](DYNC1H1-source-evidence.md) and [portable source-record package](DYNC1H1-evidence/README.md) for public locators, original-access limits, measurements and reproducible extraction. These authored files organize evidence and are not cited as independent primary experiments.
