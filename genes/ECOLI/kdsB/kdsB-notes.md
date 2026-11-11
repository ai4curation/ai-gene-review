# kdsB (P04951) curation notes

- Reviewed as the Escherichia coli K-12 exemplar for MODULE:kdo_biosynthesis
  (CMP-KDO biosynthesis), alongside the Pseudomonas putida KT2440 members.
- No provider deep-research file was generated in this session (no provider
  API access); the review rests on the cached publications cited in the
  review, the Swiss-Prot record and the PANTHER/PAINT files under
  interpro/panther/.
- Broad InterPro/ARBA parent terms were refined (MODIFY) to the specific
  KDO-pathway terms that the gene carries experimentally.
- The KDO biosynthetic process rows (GO:0019294; PAINT IBA from PTN000486365
  and the EcoCyc IDA from PMID:2989246) were modified to CMP-KDO biosynthetic
  process (GO:0033468): KdsB uses KDO and forms CMP-KDO, and GO:0033468 is not
  a descendant of GO:0019294. Both rows carry source_defects.

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
