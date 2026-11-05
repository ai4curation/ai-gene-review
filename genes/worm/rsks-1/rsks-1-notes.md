# rsks-1 review notes

## Session 1 (create review)

- fetch-gene resolved Q9NAH6 (KS6B_CAEEL), 18 GOA rows. PMID:23705068 cached and read
  (full text): rsks-1 RNAi, like raga-1/rheb-1 RNAi, reverses the nprl-3 rescue of elo-5 L1
  arrest, placing RSKS-1 as a TORC1 output in postembryonic development
  [PMID:23705068 "We found that elo-5(−) nprl-3(ku540) animals treated with ife-2(RNAi) or rsks-1(RNAi), with or without C17ISO supplement, yielded results similar to those obtained with raga-1(RNAi) and rheb-1(RNAi) (Table 1)"].
- PMID:22560223 was re-fetched with --force to obtain the PMC full text. The paper reports that
  rsks-1 RNAi *reduces* autophagy
  [PMID:22560223 "autophagy was reduced by knockdown of the S6 kinase RSKS-1, which increases translation downstream of TORC1 but also promotes autophagy"],
  which supports the BHF-UCL "positive regulation of autophagosome assembly" row. The UniProt
  entry says the reverse ("Negatively regulates autophagy"); recorded as a UniProt source defect
  (CHECK). Note PMID:18804378 claims no autophagy change in rsks-1 mutants, so the effect is
  modest/context-dependent; kept non-core.
- PMID:17277769 (ife-2 paper, Nature) is abstract-only; the NOT lifespan row cannot be verified
  and conflicts with multiple positive lifespan papers (PMID:17266679, 17266680, 18804378,
  20523893). UNDECIDED. Possibly a specific RNAi condition with no lifespan effect.
- PMID:24431434 abstract-only (publisher restriction); localization (axon, perikaryon) taken from
  UniProt curated subcellular location citing this paper.
- Core function: AGC Ser/Thr kinase acting as a TORC1 effector (T404 hydrophobic motif).
  No NEW process terms proposed: lifespan, germline, autophagy and axon regeneration evidence is
  all mutant phenotype.
- PMID:17266679 (Hansen) vs PMID:17266680 (Pan): adjacent papers in the same Aging Cell issue;
  GOA cites Hansen, UniProt cites Pan. Both report lifespan extension upon S6K loss.
