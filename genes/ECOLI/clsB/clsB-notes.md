# clsB (P0AA84, Escherichia coli K-12) curation notes

Reviewed as an exemplar for the module
`bacterial_phosphatidylglycerol_cardiolipin_biosynthesis`.

- Deep research: no provider API key was available in this session, so no
  `-deep-research-<provider>.md` file was generated. The review rests on the UniProt
  record (curated statements with ECO:0000269 evidence) and the cached publications
  cited in `clsB-ai-review.yaml`. Most cached papers are abstract-only; experimental
  GOA rows whose full text was not visible were accepted only where the cached
  abstract and the curated UniProt statement agree with the claim.
- Broad parent terms (membrane, phospholipid biosynthesis, generic transferase or
  catalytic activity) are refined with MODIFY to the specific terms the gene already
  carries with direct evidence.
- ClsB also converts phosphatidylethanolamine + glycerol to phosphatidylglycerol
  [PMID:27760827 "The reaction of synthesis involves the conversion of phosphatidylethanolamine and glycerol into PG and is catalyzed by ClsB"].
  No specific GO MF term was found for this phosphatidyl transfer; raised as a suggested question.
