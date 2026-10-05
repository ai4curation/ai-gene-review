# EGD2 notes

## 2026-10-01 re-review

Forced a current GOA and UniProt refresh for yeast EGD2/NAC-alpha.

- Current GOA has 19 active rows. Six older source assertions in the pinned review
  are now absent from live GOA and were retained as `retired: true`: the PAINT
  `GO:0051082` IBA, the UniProt keyword `GO:0015031` IEA, the PMID:9482879
  `GO:0051082` IMP, and generic IntAct `GO:0005515` rows from PMID:16429126,
  PMID:16554755 and PMID:27107014.
- Current PTHR21713 has one alpha-NAC node, `PTN000496516`, with two IBD
  assertions: `GO:0005737` cytoplasm and `GO:0006612` protein targeting to
  membrane. GO:0051082 is now formally obsolete, explaining why the historical
  `GO:0051082` IBA is no longer in the current PAINT extract; the propagation
  review is stale-source in the literal sense that the obsolete IBD is no longer
  emitted, not a donor-count or self-donor issue.
- PMID:10518932 is abstract-only in the cache but directly supports the SGD
  `GO:0006613` cotranslational membrane-targeting rows: yeast NAC prevents
  signal-less ribosome nascent chains from binding ER membranes.
- PMID:11683391 and PMID:11959135 are abstract-only in the cache and expand
  the context around EGD2-containing NAC. PMID:11683391 supports active nuclear
  import of single NAC subunits as a transient non-core localization. PMID:11959135
  supports the mitochondrial targeting arm by showing that NAC mutants have fewer
  mitochondrial-surface ribosomes and lower levels of proteins normally targeted
  cotranslationally to mitochondria.
- PMID:26618777 is full text in the cache and supports alpha-beta NAC as a
  ribosome-associated nascent-chain chaperone system. It also supports the
  ComplexPortal NAC membership row newly seeded by the refresh.
- PMID:16926149 is abstract-only in the cache and supports Ccr4-Not/Not4/Ubc4
  regulation of Egd1p/Egd2p ubiquitination. The newly active
  `UniProtKB:Q02642`/Egd1 interaction row remains a generic `protein binding`
  assertion and was removed rather than converted into a narrower molecular
  function.
- A PubMed/web search for 2024-2026 EGD2, Cne1p-independent NAC-alpha, and
  YHR193C papers found no newer direct yeast EGD2 functional paper beyond
  PMID:39426497 already cached here.
