# cdhC (Q9HTH7) curation notes

## 2026-11-04 — review for the bacterial L-carnitine catabolism module

- Scaffolded with `just fetch-gene PSEAE cdhC` while generalizing
  `modules/bacterial_l_carnitine_catabolism.yaml` beyond P. putida KT2440.
- No provider deep research was generated for this gene in this session (no
  provider run was available); no `-deep-research-*.md` file exists. The review
  rests on the curated UniProt entry, GOA, and the cached publications.
- Literature checked: PMID:19406895 (Wargo and Hogan 2009, P. aeruginosa
  carnitine locus; abstract only), PMID:24240508 (Bastard et al. 2014, BKACE
  screen; abstract only), PMID:19919675 (Chen et al. 2010, Cbc/CaiX; full text),
  PMID:30670548 (Bazire et al. 2019, S. meliloti carnitine metabolism; abstract
  only, PMC6416908 full text could not be retrieved), PMID:4302217 (Aurich et al.
  1968, P. aeruginosa carnitine dehydrogenase; no abstract cached).
- Where the cached paper is abstract-only, experimental detail (kinetics,
  disruption phenotypes, EC assignment) is quoted from the UniProt statements
  that carry ECO:0000269 evidence for that paper.
- GO has no exact terms for EC 2.3.1.317 (CdhC/BcoG) or EC 3.1.2.33
  (CdhB/BcoE-BcoF C-terminal region); these are recorded as proposed_new_terms
  and annotated at the parents GO:0016747 and GO:0016289.
