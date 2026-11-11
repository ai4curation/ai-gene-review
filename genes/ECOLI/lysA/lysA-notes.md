# lysA (E. coli K-12, P00861) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:10625645, PMID:11856852, PMID:14343156, PMID:15690043, PMID:18508763, PMID:19402753, PMID:24561554, PMID:26921318.
- Core function: diaminopimelate decarboxylase activity (GO:0008836),
  [PMID:11856852 "The final step in lysine biosynthesis in bacteria, the conversion of meso-diaminopimelate to L-lysine, is catalyzed by the only known D-amino-acid decarboxylase, diaminopimelate decarboxylase (DDC)."].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
