# dapE (E. coli K-12, P0AED7) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:1644752, PMID:18304323, PMID:28470834, PMID:3276674.
- Core function: succinyl-diaminopimelate desuccinylase activity (GO:0009014),
  [PMID:3276674 "catalyzes the hydrolysis of N-succinyl-L-diaminopimelic acid to produce L-diaminopimelic acid and succinate"].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
