# PP_1256 curation notes

- Q88NF5 is an EC 1.2.1.26 alpha-ketoglutaric-semialdehyde dehydrogenase-family
  protein predicted to use NAD+ or NADP+
  [file:PSEPK/PP_1256/PP_1256-uniprot.txt, "RecName: Full=2,5-dioxovalerate dehydrogenase"].
- Its physical linkage to PP_1255, PP_1257, and proR makes this paralog the
  leading terminal-step candidate, but PP_2585 and PP_3602 carry the same EC
  assignment and no target-specific experiment has resolved pathway flux.
- 2026-11-11 revision: the substrate-specific GO:0047533 annotation is
  accepted, and the two broad oxidoreductase IEA rows are changed (MODIFY) to
  it. Two relatives support NADP+ use: the same-subfamily (PTHR43353:SF3)
  A. baylyi KgsD (Q6FFQ0), whose NADP+ reaction UniProt curates from
  PMID:18364348, and the hydroxyproline-inducible A. brasilense KGSADH-III
  [PMID:17202142, "NAD(+)-dependent KGSADH-II and NADP(+)-dependent
  KGSADH-III"]. The earlier NEW GO:0004030 row was dropped because it is an
  ancestor of the accepted GO:0047533. The cofactor-neutral proposed term is
  kept in case PP_1256 turns out to prefer NAD+.
- No BP row is added: synteny alone does not show that PP_1256, rather than
  PP_2585 or PP_3602, carries the hydroxyproline flux.
- Deep research: not available for this gene (the Edison/Falcon API returned
  403 on 2026-11-11).
