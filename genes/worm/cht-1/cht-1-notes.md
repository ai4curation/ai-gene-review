# worm cht-1 notes

## 2026-11-24 cross-check against BRUMA MF1

- `just fetch-gene worm cht-1` seeded UniProtKB Q11174/CHT-1, 14 GOA rows, and
  two new publication caches: PMID:21731485 as full text and PMID:33691404 as an
  abstract-only record. PMID:16184190 was already cached, and
  `just fetch-gene-pmids worm cht-1` confirmed all three GOA PMIDs were present
  without forcing any existing publication refresh.
- `just mod-description-deep-research worm cht-1` fetched the WormBase curated
  gene description. The Falcon deep-research provider and the Perplexity Lite
  fallback were unavailable, so no generated deep-research file was written.
- `just paint-losses worm cht-1` found no IRD or IKR loss on the Q11174 lineage
  in PTHR11177.
- `interpro/panther/PTHR11177/PTHR11177-paint.tsv` places chitinase activity,
  chitin catabolic process and extracellular region at the PTHR11177
  PTN000126545 root. `interpro/panther/PTHR11177/PTHR11177-entries.csv` places
  C. elegans Q11174/cht-1 and Brugia malayi P29030/MF1 in the same reviewed
  PTHR11177:SF400 endochitinase-related subfamily.
- The molecular-function and chitin-catabolism rows are well supported by the
  GH18 catalytic domain, EC 3.2.1.14, PAINT and the CeCht1 structural paper.
  Chitin binding and extracellular region fit the two C-terminal type-2
  chitin-binding domains and PAINT, but the Q11174 UniProt flat file has no
  `SIGNAL` feature or `SUBCELLULAR LOCATION` comment and the cached literature
  lacks a CHT-1-specific localization assay, so they were kept as non-core.
- PMID:21731485 shows that C. albicans exposure induces cht-1 transcript
  expression, and PMID:16184190 shows that cht-1 is an ATF-6-dependent
  tunicamycin-inducible transcript. The Candida IEP row is a valid peripheral
  expression-based `response to fungus` annotation, but the paper does not show
  a direct antifungal effector role. The ATF-6-dependent tunicamycin row was
  marked over-annotated rather than accepted as direct UPR participation.
- The initial review marked the `response to fungus` row as
  `MARK_AS_OVER_ANNOTATED`; AI review correctly caught that this applied a
  defense-effector bar to a bare `response to` term, whose definition covers
  expression changes after fungal stimulus.
- WormBase's candidate embryogenesis, molting/cuticle-degradation and
  pathogen-chitin roles were not traced to target-specific perturbation data in
  the three cached GOA publications. They remain open questions for the
  physiological extracellular substrate of CHT-1.
