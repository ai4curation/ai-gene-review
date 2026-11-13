# dapF (E. coli K-12, P0A6K1) curation notes

## 2026-11-11: review for the lysine_biosynthesis module

- Deep research: not run. No deep-research provider credentials (Perplexity, OpenAI,
  Falcon, Asta) are configured in this environment, so no `-deep-research-*.md` file
  exists; this review rests on the cached publications and the UniProt record.
- Literature checked (cached abstracts; full text available only where the cache says so):
  PMID:15911532, PMID:23426375, PMID:25313159, PMID:2689171, PMID:3031013, PMID:3042781, PMID:6378903.
- Core function: diaminopimelate epimerase activity (GO:0008837),
  [PMID:3042781 "DAP epimerase was assayed by coupling the epimerization of LL-DAP to DL-DAP (Km = 0.26 mM)"].
- Used as the experimentally characterised E. coli exemplar for its step in
  `modules/lysine_biosynthesis.yaml`; the P. putida KT2440 ortholog is the second,
  family-rule-only exemplar.
