# kdsC curation notes

- Q88P96 carries the exact EC 3.1.3.45/Rhea 11500 KDO-8-phosphate phosphatase
  reaction [file:PSEPK/kdsC/kdsC-uniprot.txt,
  "Full=3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC"].
- The TreeGrafter N-acylneuraminate cytidylyltransferase annotation is removed
  as a paralog transfer in the mixed CMAS/KdsC PANTHER family.
- No direct KT2440 biochemical assay was found; the exact call is based on EC,
  KdsC-specific family evidence, and pathway continuity.

## 2026-11-10 completion pass

- Generic parent rows that the evidence refines were changed to MODIFY with the
  specific KDO-pathway term (rather than MARK_AS_OVER_ANNOTATED), matching the
  E. coli exemplar reviews; substrate-binding rows stay KEEP_AS_NON_CORE.
- Every row now carries a vetted quote (UniProt curated rule/family lines,
  PANTHER PAINT rows, or E. coli ortholog papers clearly marked as such).
- No provider deep research was generated (no provider access in this session).
- The removed TreeGrafter GO:0008781 row now records a PANTHER source defect:
  the PTHR21485 PAINT tree contains no KdsC leaf (see
  interpro/panther/PTHR21485/PTHR21485-tree-check.txt), so the IBD at
  PTN000486303 reaches KdsC proteins only through HMM family assignment.
