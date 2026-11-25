# Pcx notes

## 2026-11-24

Initialized the mouse `Pcx` review with `just fetch-gene mouse Pcx`.
Provider-backed deep research could not run in this checkout: Falcon reported only
`claude_code` as available, and the Perplexity fallback was also unavailable. I
therefore made these manual notes from cached primary literature, the UniProt
record, the reviewed human `PC` gene review, the reviewed PANTHER
`PTHR43778` family and the two gluconeogenesis GO-CAM reviews.

- `Pcx` in GO-CAMs `61e0e55600001225` and `62d0afa500000298` is
  `GO:0004736` pyruvate carboxylase activity in `GO:0005759` mitochondrial
  matrix and `GO:0006094` gluconeogenesis. This agrees with the mouse review.
- PMID:31006591 directly knocked out mouse hepatic `Pcx`: "LPCKO mice have
  impaired hepatic anaplerosis, diminution of TCA cycle intermediates,
  suppressed gluconeogenesis, reduced TCA cycle flux". This is the strongest
  mouse support for hepatic gluconeogenesis and oxaloacetate anaplerosis.
- PMID:23423574 used antisense oligonucleotides in rodents and frames pyruvate
  carboxylase as the first committed step of gluconeogenesis and a regulator of
  hepatic glucose production. The mouse contribution is part of a broader
  rat/mouse study, so the full liver-specific knockout paper is the cleaner
  support for core mouse function.
- The mouse UniProt E9QPD7 record is TrEMBL, but it has a coherent conserved
  domain architecture: biotin carboxylation, ATP-grasp,
  pyruvate-carboxyltransferase and a C-terminal biotinyl carrier domain with
  predicted N6-biotinyllysine.
- PMID:34547241 supports human cytosolic PC in the MDH1-ME1-PC hydride-transfer
  complex. I kept the mouse Ensembl transfers for cytoplasm and NAD/NADP
  metabolism as non-core because PC is conserved and the paper reports mouse and
  human prostate cancer models, but the core function remains mitochondrial
  oxaloacetate production.
- PMID:23861867 is a human HCV/Huh7 paper. Its viral-process annotations are not
  appropriate for mouse `Pcx`: PC is a host metabolic dependency for infectious
  particle production, not viral RNA-packaging or release machinery, and PC is
  the target of NS5A/NS4B transcriptional down-regulation rather than the
  regulator.
