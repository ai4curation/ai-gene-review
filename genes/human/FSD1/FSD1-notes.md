# FSD1 review notes (2026-10-28)

- UniProt Q9BTV5 confirmed (FSD1_HUMAN, GeneID 79187, HGNC:13745). 19 GOA rows.
- Key evidence: PMID:12154070 and PMID:12445389 (abstract only in cache), PMID:30538248
  (full text). See FSD1-deep-research-manual.md for quotes.
- Core picture: brain-enriched centrosome/microtubule-associated protein. SPRY domain binds
  microtubules directly [PMID:30538248 "indicating that FSD1 directly binds to MTs through its SPRY domain"];
  coiled coil targets the centrosome; FSD1 anchors interphase MT asters at mother centrioles
  [PMID:30538248 "FSD1 promotes the anchoring of MT asters at centrosomes by directly binding MTs"].
- Cell-division / mitotic spindle / cytokinesis rows rest on overexpression phenotypes
  (PMID:12445389 "ectopic expression of GLFND inhibits cell division and cytokinesis in CHO cells");
  marked as over-annotations. IBA rows for those terms are seeded from the same human data.
- Localization rows coded IMP (centrosome, microtubule) are localization observations;
  flagged as WRONG_EVIDENCE_CODE CHECK (IDA expected).
- NEW: GO:0034454 microtubule anchoring at centrosome (comparators NIN, CEP19, CCDC68, DCTN1
  carry it in human GOA; FSD1 itself does the anchoring by binding MTs; 3RE MT-binding mutant
  fails to rescue).
- Ciliogenesis not added as NEW: the effect is downstream (Cep290 satellite delocalisation),
  not FSD1 performing a step of cilium assembly.
- PMID:21690310 was supplied as a key paper but is about microRNA miR-1 (alias collision with
  MIR1); no FSD1 content found in PMC full text. Recorded with relevance NONE.
