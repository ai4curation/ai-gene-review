# PpSQ1_00400 (P0DOV7) 6-deoxy-6-sulfo-D-gluconate dehydratase, Pseudomonas putida SQ1 — notes

## Provenance and access

- Deep research with perplexity failed in this environment (2026-11-10; "All providers failed").
  Sources: UniProt P0DOV7, PMID:26195800 (abstract only), PMID:41676062 (review, full text).

## Function

- UniProt (ECO:0000269 PubMed:26195800): "Catalyzes the dehydration of 6-deoxy-6-sulfo-D-gluconate
  to 2-dehydro-3,6-dideoxy-6-sulfo-D-gluconate." RHEA:47912, EC 4.2.1.162; induced on SQ.
- [PMID:41676062 "SG undergoes dehydration catalyzed by 6-deoxy-6-sulfogluconate dehydratase
  (SG-DH) to form 2-keto-3,6-dideoxy-6-sulfogluconate (KDSG)"].
- IlvD/Edd family (PF00920, PF24877, PROSITE PS00886); [4Fe-4S] cluster and homodimer inferred
  only by similarity to A. brasilense L-arabonate dehydratase AraC (Q1JUQ1; ECO:0000250); no
  cluster or kinetics data for P0DOV7 accessible here, so no cofactor row is added.
- GO has no SG dehydratase term (OLS, 2026-11-10). Parent GO:0016836 hydro-lyase activity is the
  module's term and as precise as GO allows.

## GOA rows

- GO:0003824 catalytic activity (IEA InterPro2GO IPR020558) -> MODIFY to GO:0016836.
- GO:0016836 hydro-lyase activity (IEA ARBA:ARBA00026984) -> ACCEPT, supported by the curated
  FUNCTION text rather than the ARBA rule.
- PTHR43183: no PAINT node-level annotations (fetch-panther-paint 2026-11-10: 18 nodes, none
  annotated), so no IBA/TreeGrafter rows.
