# PGRPLB evidence notes

## 2026-09-20 full-gene IBA re-review

Restored broad immune functions and retained the inherited Gram-positive context. Receptor signaling and extracellular-space localization remain unresolved; corrected systemic-versus-local immune wording and removed a redundant old NEW proposal.

The former Gram-negative-only replacement conflated peptidoglycan chemotype with Gram stain. Predicted transmembrane segments do not exclude every extracellular pool. GO:0016019 requires signal initiation, which the knockdown readout does not directly establish. The existing negative-signaling proposal is retained with real primary ortholog support; its old IBA metadata is not evidence that the proposed term occurs at the PAINT node.

- PMID:28494453: Anopheles coluzzii, formerly A. gambiae M form, has two predicted PGRPLB membrane isoforms. Knockdown increased systemic fat-body CEC1 without affecting the measured local midgut response. This is direct ortholog perturbation evidence, not target-specific biochemical kinetics.
- file:ANOGA/PGRPLB/PGRPLB-deep-research-falcon.md: Read mechanistic account and limitations. Much discussion comes from PGRP-LD/PGRPLC or family literature; primary PGRPLB experiments now distinguish the actual role.

PAINT: {'family': 'PTHR11022', 'node': 'PTN002475783', 'finding': 'Current ancestral amidase/receptor/immune/Gram-positive assertions persist. Current extracellular-region IBD differs in scope from the older extracellular-space row; no demonstrated loss follows from this drift.'}

All 13 rows were assessed, including experimental, electronic, negated and old proposed entries. All actual GOA rows and source fields remain unchanged. One redundant old reviewer-authored NEW proposal was deleted; the original reviewed-row count includes that proposal. Remaining questions are recorded in `projects/IBA_REVIEW/rereview-2026-09-20/receptor-and-lipid-claims.yaml`; coordinated reports will be assessed critically when available.

Corrected the source metadata of the remaining old reviewer-authored NEW proposal to ISS/PMID:28494453. Actual GOA rows are unaffected.


## Evidence-presentation correction (2026-09-23)

Corrected local-file quotations or matched supporting text to its claim where applicable. Missing-assay caveats remain in reasons rather than serving as positive support. Annotation actions are unchanged.


## OpenScientist immune-receptor follow-up (2026-09-27)

Assessed `PGRPLB-hypotheses/immune-receptor-defense-and-secretion/openscientist.md`.
The focused paralog check resolves GO:0016019 away from `UNDECIDED`: PGRP-LB is the
catalytic amidase that depletes peptidoglycan ligands, whereas PGRP-LC is the
signal-initiating Anopheles peptidoglycan receptor. Updated the PAINT receptor row
to `MARK_AS_OVER_ANNOTATED` as a wrong-ortholog-or-paralog propagation. Kept the Gram-positive
defense row as non-core for now because DAP-type specificity and negative immune
regulation weaken the exact term, but the broad inherited bacterial-defense context
still lacks a target-specific loss experiment.
