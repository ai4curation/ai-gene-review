# squD (Saro_2443, Q2G5J4) notes

## Deep research
- 2026-11-10: perplexity deep research fails in this environment (no provider credentials;
  "All providers failed", tried on AGRFC smoA). Review built from UniProt and cached literature.

## Sources
- Primary paper: Liu et al. 2021 ACS Catal. 11:14740 (DOI 10.1021/acscatal.1c04321), no PMID,
  not cached. UniProt curates FUNCTION/CATALYTIC ACTIVITY from it as Ref.2 (ECO:0000269).
  [file:NOVAD/squD/squD-uniprot.txt "Catalyzes the oxidative desulfurization of sulfoquinovose to sulfite and 6-dehydro-D-glucose (Ref.2)."]
- Review PMID:41676062 (full text cached)
  [PMID:41676062 "In the sulfo-ASMO pathway, the degradation of SQ is initiated by the flavin-dependent alkane sulfonate monooxygenase SquD, which converts SQ to 6-dehydro-D-glucose and sulfite by an oxidative C-S bond cleavage."]
  and SquD pairs with an SsuE-type reductase.
- Adjacent gene squF (Saro_2444) = 6-dehydroglucose reductase.

## Decisions
- Same treatment as SmoC: GO:0008726 ACCEPT; GO:0016705 MODIFY -> GO:0008726; GO:0046306
  MODIFY -> GO:1902777; proposed NTR sulfoquinovose monooxygenase activity.
- TreeGrafter graft node PTN008675999 is not an IBD node in PTHR42847 PAINT.
- PANTHER PTHR42847:SF4.
