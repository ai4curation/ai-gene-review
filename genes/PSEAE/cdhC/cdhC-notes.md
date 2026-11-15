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


## 2026-11-07 — independent PAO1 consultation

CdhC transfers CoA from acetyl-CoA to 3-dehydrocarnitine, yielding acetoacetate and betainyl-CoA. Dataset 2 of PMID24240508 maps this exact PAO1 protein to BKACE_529; neither BKACE529 nor the PA14 BKACE361 appears in the accessible Dataset 4 screen. Table 6 kinetics are from other G5 members. The broad acyltransferase replacement of the KAH-specific mapping follows target-curated physiological chemistry, not a claimed negative KAH assay. PSEPK Q88R31/BKACE511 does have both substrates in that screen, so the clade cannot be declared devoid of KAH activity. Original fourth row (zero-based index 3) NEW GO:0016747 exactly duplicates the third row (zero-based index 2) MODIFY; it remains present with retired:true and its distinct evidence retained on the active replacement/core.

Source scope and access receipts are preserved in [primary-scope](../../../analysis/module_audits/bacterial_l_carnitine_catabolism/pseae-consultation/primary-scope.md). The genuine Falcon attempt failed with HTTP 403 authentication/access rejection; no provider report was invented. The original ordered source payloads and protected caches remain intact. The mapped PANTHER lineage has no reported IRD/IKR loss. All primary source quotations are distinguished from analyst interpretation.
