# argD (E. coli K-12, P18335) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:10074354, PMID:25243376.
- Core function: succinyldiaminopimelate:2-oxoglutarate transaminase activity (GO:0009016),
  [PMID:10074354 "This enzyme exhibits both NAcOATase and DapATase activity, with similar specificity constants for N-acetylornithine and N-succinyl-L,L-DAP, suggesting that it can function in both lysine and arginine biosynthesis."].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
