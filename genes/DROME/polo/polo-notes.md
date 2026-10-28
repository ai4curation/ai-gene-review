# polo review notes

## Session 1 (create review)

- fetch-gene resolved P52304 (POLO_DROME, FlyBase FBgn0003124, GeneID 40232); 64 GOA rows.
- No deep-research provider available; literature summary in `polo-deep-research-manual.md`.
- Additional PMIDs cached: 9813088 (full text, key cytokinesis paper), 1660828 and 24829288
  (UniProt FUNCTION sources).
- Abstract-only papers: 10954431, 11283617, 15572022, 16412419, 17046997, 18463163,
  22389397, 23136393, 24954048, 3417791, 8510757, 8890161, 9914376, 1660828. Experimental
  annotations from these were not removed; where the abstract did not show the claim
  (15572022 spindle pole; 17046997 kinetochore microtubule) I deferred to the curator or used UNDECIDED.

## Key decisions

- `protein kinase activity` (GO:0004672) rows -> MODIFY to `protein serine/threonine kinase
  activity` (GO:0004674), which the gene already carries (IBA, IDA PMID:8890161).
- `mitotic cell cycle` (GO:0000278) rows -> MODIFY to `mitotic spindle organization`
  (GO:0007052); spindle-pole/branched spindle phenotypes are the specific supported outcome
  [PMID:3417791 "Embryos from homozygous polo females have aberrant mitotic spindles that are highly branched and have broad poles"].
- `spindle` -> MODIFY to `spindle midzone` + `spindle pole` (both shown).
- `intracellular protein localization` (PMID:9813088, Pav-KLP fails to reach midzone in
  polo1 spermatocytes) -> MODIFY to `protein localization to meiotic spindle midzone` (GO:1903096).
- `male germline ring canal formation` and `pronuclear fusion` marked over-annotated:
  both are downstream consequences (fewer cytokinesis events; failed pronuclear migration).
- Developmental terms (heart, larval muscle, neuroblast proliferation, oocyte fate) kept as non-core.
- Protein binding rows (Mtrm, Gwl) removed per protein-binding policy; the interactions are real
  [PMID:18052611 "Mtrm binds to Polo with an approximate stoichiometry of 1:1"].
- No NEW annotations proposed. Cytokinesis (GO:0000281 mitotic cytokinesis) is well
  supported for fly cells (PMID:16412419 myosin recruitment) but the existing actomyosin
  ring assembly and male meiosis cytokinesis rows already capture Polo's cytokinesis role.
