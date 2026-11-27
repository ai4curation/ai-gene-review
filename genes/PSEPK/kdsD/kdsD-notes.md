# kdsD curation notes

- Q88P95 carries the exact EC 5.3.1.13/Rhea 23104 API reaction and a KDO
  biosynthesis pathway comment [file:PSEPK/kdsD/kdsD-uniprot.txt,
  "3-deoxy-D-manno-octulosonate biosynthesis"].
- The consecutive kdsC/PP_0956 and kdsD/PP_0957 locus tags support the
  housekeeping KDO interpretation, but no direct KT2440 enzyme assay was found.
- The explicit UniProt lipopolysaccharide-biosynthesis pathway line supports a
  new GO:0009103 row; E. coli genetics provides comparative, not target-strain,
  evidence for API redundancy [PMID:16765569, "indicating genetic redundancy
  for these two functions"].
- Broad carbohydrate, isomerase, and binding annotations are not treated as
  equivalent to the exact API molecular function.

## 2026-11-10 completion pass

- Generic parent rows that the evidence refines were changed to MODIFY with the
  specific KDO-pathway term (rather than MARK_AS_OVER_ANNOTATED), matching the
  E. coli exemplar reviews; substrate-binding rows stay KEEP_AS_NON_CORE.
- Every row now carries a vetted quote (UniProt curated rule/family lines,
  PANTHER PAINT rows, or E. coli ortholog papers clearly marked as such).
- No provider deep research was generated (no provider access in this session).
