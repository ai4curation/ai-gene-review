# Ser (Serrate) — curation notes (DROME, P18168)

## Session 2026-09-30 (Notch signaling module)

Deep research: falcon run launched; first attempt failed (falcon timeout, perplexity fallback not
configured), relaunched. Review written from UniProt, cached publications and GOA.

### Key findings
- Serrate binds the same Notch EGF repeats (11-12) as Delta [PMID:1657403].
- Ser-Notch affinity is similar to Dl-Notch [PMID:10504334 "the interactions between Serrate and
  Notch are similar in affinity to those between Delta and Notch"].
- Fringe inhibits responsiveness to Serrate and potentiates Delta [PMID:9202123], restricting
  Ser-Notch signaling to the wing D/V boundary.
- Conserved intracellular motifs: one Mib1/Neur-interaction motif needed for trans-activation and
  endocytosis but not for cis-inhibition; cis-inhibition occurs at the cell surface
  [PMID:17006545].
- Ser ectodomain binds glycosphingolipids via a conserved GSL-binding motif [PMID:20176925].
- Serrate (not Delta) is the ligand for crystal cell specification in the lymph gland
  [PMID:12445385; PMID:12569125].
- A third, DSL-less Notch ligand, Weary (CG31665), acts in the adult heart [PMID:20203305] — relevant
  to pathway variants.

### Decisions
- Core MF: GO:0005112 Notch binding and GO:0048018 receptor ligand activity; process Notch
  signaling pathway; location plasma membrane / apical PM.
- REMOVE: GO:0005515 protein binding (Mib1). MODIFY: GO:0007166 -> GO:0007219.
- Axon/axolemma/neuron projection, endosomal compartments, apical cortex kept as non-core.

### PANTHER
UniProt DR PANTHER: PTHR12916 ("CYTOCHROME C OXIDASE POLYPEPTIDE VIC-2") and PTHR12916:SF11
("MUCIN-4") — official PANTHER names, evidently not descriptive of Serrate. Note that Ser is not in
PTHR24049 with Dl/N. IBA GO:0005112 <- PANTHER:PTN002371879 (same node as Dl).
