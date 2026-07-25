# nadE curation notes

## 2026-07-20

- Target identity: PP_4869 / reviewed UniProtKB Q88DF6, a 275-aa
  ammonia-dependent NadE [UniProtKB:Q88DF6, "RecName: Full=NH(3)-dependent NAD(+) synthetase"].
- Reaction: deamido-NAD, ammonium, and ATP yield NAD+, AMP, and diphosphate
  [UniProtKB:Q88DF6, "Reaction=deamido-NAD(+) + NH4(+) + ATP = AMP + diphosphate + NAD(+) + H(+)"]
  [RHEA:21188, ammonia-dependent NAD synthetase reaction].
- Specificity: the target has IPR022926 (NH(3)-dependent NAD synthetase) and no
  glutaminase module [UniProtKB:Q88DF6, "InterPro; IPR022926; NH(3)-dep_NAD(+)_synth."].
- Family grounding: Q88DF6 and the E. coli ammonia-dependent exemplar P18843
  map to PTHR23090:SF7, whereas human glutamine-dependent Q6IA69 maps to
  PTHR23090:SF9 [file:interpro/panther/PTHR23090/PTHR23090-entries.csv].
- Curation: GO:0008795 is core. Electronic GO:0003952 and GO:0004359 were
  removed as broad-family over-propagation contradicted by the reviewed target
  architecture and reaction. PTHR23090 spans both ammonia- and
  glutamine-dependent NAD synthetases and cannot establish donor specificity.
- OpenScientist independently recovered the compact ammonia-dependent
  architecture and explicitly excluded a glutaminase-containing target, which
  supports the two REMOVE decisions. Its residue alignment, oligomeric state,
  and essentiality discussion remain homology-based rather than KT2440
  measurements and were not used to add annotations
  [file:PSEPK/nadE/nadE-deep-research-openscientist.md,
  "no KT2440-specific kinetic study of PP_4869 was located"].
