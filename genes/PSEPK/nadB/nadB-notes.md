# nadB curation notes

## 2026-07-20

- Target identity: PP_1426 / UniProtKB Q88MZ2, a 534-aa NadB-family protein
  [UniProtKB:Q88MZ2, "Belongs to the FAD-dependent oxidoreductase 2 family. NadB subfamily."].
- Reaction: L-aspartate oxidation produces iminoaspartate and hydrogen peroxide
  [UniProtKB:Q88MZ2, "Catalyzes the oxidation of L-aspartate to iminoaspartate."]
  [RHEA:25876, "L-aspartate + O2 = iminosuccinate + H2O2"].
- Family grounding: PTHR42716; PAINT node PTN000908494 carries GO:0008734 and
  GO:0034628 with experimentally characterized NadB seed P10902
  [GO_REF:0000033, PTHR42716 PAINT tree].
- Curation: GO:0008734 and GO:0034628 are core. GO:0016491 and GO:0019363 are
  valid but unnecessarily broad and were modified to the specific activity and
  pathway terms.
- OpenScientist independently recovered the NadB family identity, L-aspartate
  oxidase reaction, and de novo NAD+ entry role. Its proposed physical
  NadB-NadA channeling and physiological fumarate acceptor use in KT2440 are
  ortholog-based hypotheses, not target observations, and were not converted
  into annotations [file:PSEPK/nadB/nadB-deep-research-openscientist.md,
  "The functional assignment for Q88MZ2 is a well-supported homology inference, not a direct measurement."].
