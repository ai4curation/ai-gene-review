# cdhB (Q9HTH9) curation notes

## 2026-11-04 — review for the bacterial L-carnitine catabolism module

- Scaffolded with `just fetch-gene PSEAE cdhB` while generalizing
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

CdhB hydrolyzes betainyl-CoA after CdhC-dependent CoA transfer. The broad fatty-acyl-CoA hydrolase mapping is refined to the existing acyl-CoA hydrolase replacement. Original fourth row (zero-based index 3) proposes exactly the same GO:0016289 as the third row (zero-based index 2) already supplies by MODIFY. This author-created duplicate proposal is retained with its original NEW action and payload, marked retired at annotation level, and all of its distinct support is copied into the active replacement and core. No activity or evidence is withdrawn.

Source scope and access receipts are preserved in [primary-scope](../../../analysis/module_audits/bacterial_l_carnitine_catabolism/pseae-consultation/primary-scope.md). The genuine Falcon attempt failed with HTTP 403 authentication/access rejection; no provider report was invented. The original ordered source payloads and protected caches remain intact. The mapped PANTHER lineage has no reported IRD/IKR loss. All primary source quotations are distinguished from analyst interpretation.

## 2026-11-07 — family consistency follow-up

The previous categorical SF2 fatty-acyl exclusion and proposed FadM-only pruning are withdrawn. Betainyl-CoA chemistry does not establish absence of secondary fatty-acyl-CoA hydrolysis. The supported acyl-CoA MODIFY replacement, all annotation actions, source payloads, proposal lifecycle flags and core functions are unchanged. Propagation is now explicitly unresolved and the upstream request is a suspected scope CHECK, not a directed pruning correction. PAO1 CdhB is demonstrably inside PTN001273712; this is substrate-range uncertainty, not topology uncertainty. The positive FadM seed is retained. A full substrate panel would resolve the remaining activity question. Original frozen receipts remain historical; this correction has an additive before/after handoff.
