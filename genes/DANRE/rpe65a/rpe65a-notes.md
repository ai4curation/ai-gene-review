# rpe65a review notes

- Curated in DANRE batch 04. Rpe65a is a visual-cycle retinoid isomerohydrolase. I accepted the retinyl-ester hydrolase/retinol isomerase and retinoid/retinal metabolism annotations, while marking beta-carotene dioxygenase and broad oxidoreductase terms as not the best representation of the UniProt-described activity.
- Follow-up: plasma membrane is now kept as non-core context to acknowledge the UniProt cytoplasm/peripheral membrane ambiguity.

## Re-review 2026-09-29

Re-reviewed all 17 GOA rows. The previous version cited no primary literature; this pass grounds
the review in five cached papers and UniProt Q6PBW5, and removes three yaml rows no longer in GOA
(GO:0001523 IEA ARBA, GO:0052885 IEA Rhea, GO:0120254 IEA ARBA).

- Paralogs: zebrafish has rpe65a (RPE), rpe65b (extra-ocular) and rpe65c (Muller glia). Only
  rpe65a is the RPE visual-cycle enzyme [PMID:17868371 "In crosssections it became clear that
  retinal RPE65a expression was confined to RPE cells"; PMID:21676174 "zebrafish RPE65c, RPE65a
  and 13cIMH are three homologous proteins encoded by distinct genes"]. The ZFIN donor
  ZDB-GENE-081104-505 in the IBA WITH/FROM is a paralog, not rpe65a.
- Important caveat recorded in every activity row: the zebrafish Rpe65a enzyme has never been
  assayed [PMID:22512451 "It is noteworthy that the enzymatic activity of RPE65a in zebrafish has
  not been studied or characterized."]; the activity rests on orthology plus the morphant
  phenotype [PMID:17868371 "Targeted gene knockdown of RPE65 resulted in morphologically altered
  rod outer segments and overall reduced 11- cis -retinal levels."].
- Core: GO:0052885 (IBA, IEA GO_REF:0000120 [was PENDING], ISS) and GO:0052884 (IEA Rhea, ISS)
  ACCEPT; GO:0042574 IBA, GO:0042572 IEA, GO:0001523 ISS ACCEPT.
- GO:0003834 beta-carotene 15,15'-dioxygenase IBA changed MARK_AS_OVER_ANNOTATED -> REMOVE with
  propagation_review (PROPAGATION_BAD / FUNCTIONAL_DIVERGENCE): the deep family node
  PTN000830314 is seeded by BCO1 oxygenases, and the RPE65 subclade performs a different primary
  chemistry [PMID:38355721 "retinyl ester hydrolysis in the case of RPE65 and carotenoid
  oxygenation in the case of NinaB"]. GO:0016702 IEA (InterPro IPR004294) changed MODIFY -> REMOVE
  for the same reason (no O2 incorporation; no fitting child term).
- GO:0050251 retinol isomerase IBA changed ACCEPT -> MODIFY to GO:0052885 with propagation_review
  (TERM_SCOPING_PROBLEM): the term's substrate is free all-trans-retinol, but RPE65-family enzymes
  (including the rpe65c donor) act on retinyl esters.
- GO:1901827 zeaxanthin biosynthesis IBA KEEP_AS_NON_CORE (single human donor is legitimate; no
  zebrafish evidence either way).
- Localization: cytoplasm IEA/ISS ACCEPT; ER membrane ISS changed KEEP_AS_NON_CORE -> ACCEPT (site
  of the membrane-embedded ester substrate); plasma membrane IEA/ISS KEEP_AS_NON_CORE (loose
  SubCell rendering of the lipid-anchored form).
- Description rewritten; suggested questions/experiments added (direct in vitro assay of Rpe65a;
  stable null allele).
- Validation: zero errors, zero warnings.
