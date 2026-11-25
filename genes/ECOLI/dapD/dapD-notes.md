# dapD (E. coli K-12, P0A9D8) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:15911532, PMID:18304323, PMID:6365916.
- Core function: 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase activity (GO:0008666),
  [PMID:6365916 "The enzyme catalyzes the formation of CoA and N-succinyl-2-amino-6-keto-L-pimelate from succinyl-CoA and tetrahydrodipicolinate."].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
