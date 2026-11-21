# dapA (E. coli K-12, P0A6L2) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:1463470, PMID:15911532, PMID:16858726, PMID:18304323, PMID:24561554, PMID:4910051, PMID:7832769, PMID:8993314.
- Core function: 4-hydroxy-tetrahydrodipicolinate synthase activity (GO:0008840),
  [PMID:8993314 "Dihydrodipicolinate synthase (DHDPS) catalyzes the condensation of pyruvate with L-aspartate beta-semialdehyde."].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
