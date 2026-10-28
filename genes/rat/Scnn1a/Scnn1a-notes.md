# Scnn1a (rat) review notes

## Session 1 (initial review)

- fetch-gene resolved P37089 (SCNNA_RAT, RGD:3639, GeneID 25122); 101 GOA rows, all keyed to P37089.
- No deep-research provider available; literature summary in `Scnn1a-deep-research-manual.md`.
- Most cached papers are abstract-only; full text for PMID:17562820, PMID:22045317, PMID:24419567,
  PMID:26394093, PMID:27413634, PMID:18308722.

### Decisions

- Core: sodium channel activity (GO:0005272), apical plasma membrane, sodium channel complex,
  sodium ion import across plasma membrane, sodium ion homeostasis.
- GO:0015280 ligand-gated sodium channel activity (IBA/IEA) -> MODIFY to GO:0005272: ENaC is
  constitutively open, regulated by proteolysis and trafficking, not by a gating ligand
  [file:rat/Scnn1a/Scnn1a-uniprot.txt "Furin cleaves the SCNN1A subunit, which results in a stepwise
  increase in the open probability of the channel due to the release of an inhibitory tract"].
- General transport terms (GO:0006814, GO:0035725, GO:0015081, GO:0016020, GO:0005929) -> MODIFY to
  the specific terms the gene already carries.
- GO:0006883 intracellular sodium ion homeostasis -> MARK_AS_OVER_ANNOTATED (ENaC sets organismal
  Na+ balance, not intracellular Na+).
- Expression-only IEP response terms (hypoxia, salt stress, dexamethasone, testosterone, candesartan,
  angiotensin, mechanical stimulus, vasopressin IEP) -> MARK_AS_OVER_ANNOTATED. Aldosterone rows kept
  as non-core because aldosterone induction of alpha-ENaC is the canonical physiological regulation
  and ENaC executes aldosterone-stimulated Na+ absorption [PMID:16426574 "aldosterone increased
  alpha-ENaC mRNA expression in DS rat similar to DR rat"].
- Salty taste (NAS) kept non-core, supported by PMID:20107438; sour taste over-annotated.
- GO:0050878 regulation of body fluid levels (IMP, lung siRNA) -> MODIFY to GO:0042045 epithelial
  fluid transport [PMID:16258001 "pSi-4 pretreatment reduced baseline lung fluid absorption by
  approximately 30%"].
- NEW GO:0070294 renal sodium ion absorption (IC). Comparator check via QuickGO (2026-10-28):
  NKCC2 (Slc12a1), NCC (SLC12A3/Slc12a3), Kcnj1, Clcnkb carry GO:0070294; no ENaC subunit in
  human/mouse/rat does. ENaC itself performs the apical Na+ entry step, so it passes the
  "does the gene product do the work" test.
- Consistent with sibling reviews of rat Scnn1b/Scnn1g where the same terms recur.
