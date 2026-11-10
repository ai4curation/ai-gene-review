# kdsB curation notes

- The reviewed Q88LM7 record carries the exact EC 2.7.7.38/Rhea 23448 CMP-KDO
  synthetase reaction [file:PSEPK/kdsB/kdsB-uniprot.txt,
  "Reaction=3-deoxy-alpha-D-manno-oct-2-ulosonate + CTP"].
- Cytoplasm and cytosol are redundant localization rows. Cytoplasm is retained
  as non-core, and the TreeGrafter cytosol row is kept as compatible non-core
  evidence; neither redundant location is promoted into the core function.
- No direct KT2440 assay was found, so the evidence remains homology/rule based.

## 2026-11-10 completion pass

- Generic parent rows that the evidence refines were changed to MODIFY with the
  specific KDO-pathway term (rather than MARK_AS_OVER_ANNOTATED), matching the
  E. coli exemplar reviews; substrate-binding rows stay KEEP_AS_NON_CORE.
- Every row now carries a vetted quote (UniProt curated rule/family lines,
  PANTHER PAINT rows, or E. coli ortholog papers clearly marked as such).
- No provider deep research was generated (no provider access in this session).
