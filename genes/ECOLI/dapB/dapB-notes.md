# dapB (E. coli K-12, P04036) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:16858726, PMID:18304323, PMID:20503968, PMID:4151489, PMID:7893644.
- Core function: 4-hydroxy-tetrahydrodipicolinate reductase activity (GO:0008839),
  [file:ECOLI/dapB/dapB-uniprot.txt "FUNCTION: Catalyzes the conversion of 4-hydroxy-tetrahydrodipicolinate"].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
