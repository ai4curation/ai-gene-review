# Q9HTH6 (Q9HTH6) curation notes

## 2026-11-04 — review for the bacterial L-carnitine catabolism module

- Scaffolded with `just fetch-gene PSEAE Q9HTH6` while generalizing
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

CaiX is a periplasmic carnitine-recognition subunit working with CbcWV. The full PMID19406895 study distinguishes PA5388 uptake from the downstream enzyme pathway; the catabolism IMP row is therefore refined to the already supported carnitine transport process. PAO1 transposon mutants are explicitly included, while targeted deletion/complementation mainly uses PA14. PMID19919675 Table 5 combines B728a CaiX with PAO1 CbcWV in E. coli; uptake Km is not a purified PAO1 CaiX binding Kd. No PANTHER family was recoverable from this raw record, so a lineage-loss check remains unresolved rather than negative.

Source scope and access receipts are preserved in [primary-scope](../../../analysis/module_audits/bacterial_l_carnitine_catabolism/pseae-consultation/primary-scope.md). The genuine Falcon attempt failed with HTTP 403 authentication/access rejection; no provider report was invented. The original ordered source payloads and protected caches remain intact. All primary source quotations are distinguished from analyst interpretation.
