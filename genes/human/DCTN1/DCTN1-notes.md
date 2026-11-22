# DCTN1 (p150Glued) review notes

## Session 2026-09-27 (claude-code)

Sources: UniProt Q14203, cached GOA-cited publications, plus PMID:25035494, PMID:25814576,
PMID:19874786, PMID:15173193, PMID:39115447 (all cached).

Key biology (with provenance):
- p150Glued is the dynein- and microtubule-binding shoulder projection of dynactin
  [PMID:25814576 "On top sits the shoulder domain (7) from which emerges a long projection, corresponding to dynactin’s largest subunit p150Glued (DCTN1) (8)."].
- Dynactin plus a cargo adaptor activates processive mammalian dynein
  [PMID:25035494 "The addition of BicD2 to purified brain dynein did not stimulate processive motility, indicating a requirement for dynactin"].
- Neuron-specific anti-catastrophe / nucleation activity of the CAP-Gly+basic N-terminus
  [PMID:23874158 "p150(Glued) is a potent anti-catastrophe factor for microtubules."].
- Nuclear envelope pool at prophase (Plk1 pS179) [PMID:20679239].
- Nucleokinesis: p150 co-precipitates with Syne-1/Syne-2 in embryonic brain [PMID:19874786];
  nesprin-2 SR48-56 binds p150Glued [PMID:39115447].
- Subdistal appendage pool recruited by KIF3A; MT anchoring and centriole cohesion [PMID:23386061].

Decisions of note:
- No GOA annotation to dynactin complex (GO:0005869) or to a dynein-activating MF; proposed
  MODIFY of microtubule associated complex / protein-containing complex rows to GO:0005869, and a
  NEW contributes_to GO:0140660 cytoskeletal motor activator activity (PMID:25035494).
- Sterol sensor activity (contributes_to) REMOVED: ORP1L is the sensor, p150Glued the effector
  (PMID:19564404 full text).
- NOT axonal transport (PMID:18364389) REMOVED: a negative result for one dominant allele does
  not establish non-involvement; the G59S paper itself (PMID:16505168) proposes impaired
  retrograde axonal transport.
- Organism-level phenotypes from transgenic mutant-p150 mice (motor behavior, neuromuscular
  process, ventral spinal cord development, NMJ development) marked over-annotated.
- 43 of 44 protein binding rows REMOVED as uninformative; tau row MODIFIED to tau protein binding.

Deep research: DCTN1-deep-research-falcon.md arrived after the first pass; it agrees with the review (non-enzymatic dynein activator arm; retrograde axonal transport initiation; caution against assigning complex-level cargo functions to p150 alone). Its pointer to Singh 2024 LIS1-p150 was checked in PMID:38547289 and cited.
