# HOG1 Curation Notes

## 2026-10-10

- Started from `just fetch-gene CANAL HOG1`, which seeded 67 GOA rows for
  *Candida albicans* HOG1/Q92207 and cached the 17 GOA PMIDs.
- `just deep-research-falcon CANAL HOG1 --fallback perplexity-lite` could not
  run because no deep-research provider was configured, so this review used
  manual curation of the cached publications and a live search for newer
  HOG1-specific literature.
- Live searching found the December 2024 PLOS Pathogens paper PMID:39715274,
  "Stress contingent changes in Hog1 pathway architecture and regulation in
  Candida albicans", which was not in the GOA seed. I cached it and used it as
  the current mechanistic reference for the Ssk1/Ssk2/Pbs2/Hog1 split between
  high-salt activation and oxidative-stress activation.
- The fungal PAINT node `PANTHER:PTN001172058` in PTHR24055 is the fungal
  HOG1/stress-MAPK node rather than the full MAPK family. Its three propagated
  process terms, `osmosensory signaling pathway`, `cellular response to
  oxidative stress`, and `stress-activated MAPK cascade`, all match the
  experimentally characterized *C. albicans* HOG1 pathway.
- The broad `PANTHER:PTN000622075` localization and serine/threonine kinase
  IBAs are also acceptable for Q92207: they transfer only shared MAPK activity
  and cytoplasm/nucleus locations, not an ERK/JNK/p38-specific animal pathway.
- The main curation correction is polarity. The positive `filamentous growth`
  rows are backed by experiments showing derepressed hyphal growth in `hog1`
  mutants, so they should be replaced with negative-regulation filamentation
  terms.
- PMID:39432552 directly found that `hog1`, `pbs2`, and `ssk2` mutants are
  sensitive to oxidized linolenic acid. That supports a lipid-peroxidation
  survival phenotype, but it does not show that Hog1 itself participates in
  the chemistry of lipid oxidation.
- PMID:38949302, the 2024 systematic *C. albicans* kinome library paper, was
  also cached during the live search. It is useful background for future
  kinase screens but was not direct enough for a HOG1 `supported_by` quote.
- Follow-up after PR review: the `GO:0005737 cytoplasm` rows were left as
  `ACCEPT`, but their evidence was tightened. The PMID:15817773 IDA row now
  cites the paper's own Hog1-GFP "localized throughout the cell" statement,
  while the broad PAINT, PMID:15229284, and UniProt-SubCell cytoplasm rows now
  cite UniProt's explicit cytoplasm/nucleus location block instead of reusing a
  nuclear-accumulation-only quote.
