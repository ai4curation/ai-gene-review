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

## Ontology check behind GO:0019294 -> GO:0033468 (2026-11-11)

- Command: `uv run runoak -i sqlite:obo:go ancestors GO:0033468 -p i,p`
  (GO release cached by OAK, 2026-11). The is_a/part_of ancestors of
  GO:0033468 CMP-keto-3-deoxy-D-manno-octulosonic acid biosynthetic process are
  nucleotide-sugar biosynthetic process (GO:0009226), carbohydrate derivative
  biosynthetic process (GO:1901137), nucleoside phosphate and organophosphate
  biosynthesis and their parents. GO:0019294 is not among them, and
  `runoak ... descendants GO:0019294 -p i,p` returns no terms.
- GO:0019294 is defined as "The chemical reactions and pathways resulting in
  the formation of keto-3-deoxy-D-manno-octulosonic acid"; KdsB consumes KDO.
  UniProt splits the same pathways (UniPathway UPA00030 lipopolysaccharide
  biosynthesis vs UPA00358 CMP-KDO biosynthesis).
