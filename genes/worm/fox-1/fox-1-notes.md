# fox-1 review notes

- 2026-10-28: Fetched with `just fetch-gene worm fox-1`; accession Q10572 confirmed (WBGene00001484,
  GeneID 180549). 28 GOA rows. No deep-research API keys; manual synthesis in
  `fox-1-deep-research-manual.md`.
- Full text read: PMID:33372658 (Farboud 2020 eLife, key paper), PMID:23468662 (unc-32/UNC-75 paper,
  includes FOX-1 EMSA and NLS mapping), PMID:16139225, PMID:17720939, PMID:23666922.
  Abstract only: PMID:9217163, PMID:9927456, PMID:7821230, PMID:17060915, PMID:17923701, PMID:21471153.
- Key judgement calls:
  - mRNA binding (IBA) -> MODIFY to pre-mRNA intronic binding (GO:0097157); in GO, pre-mRNA binding is
    not a child of mRNA binding (checked with OAK), and every known FOX-1 target is intronic. Same
    call as the paralog review genes/worm/asd-1.
  - mRNA alternative trans-splicing (IDA, PMID:33372658): the trans-spliced xol-1 cDNAs were cloned only
    from high-FOX-1 (transgenic yIs44) embryos [PMID:33372658 "Clones of cDNAs from high FOX-1 conditions revealed both expected and unexpected transcripts (Figure 3C)."];
    FOX-1 is a regulator, not splicing machinery -> MARK_AS_OVER_ANNOTATED.
  - Dosage compensation rows: FOX-1 acts upstream via xol-1 -> sdc-2; the regulation terms
    (GO:1900095 etc.) are obsolete, so the process term is kept as non-core.
  - GO:0007540 "sex determination, establishment of X:A ratio" is arguably the most specific
    description of an X-signal element, but it is not a descendant of primary sex determination and
    no comparator check was done (sex-1, ceh-39 not reviewed here); raised as a question, not NEW.
  - Nervous system development IBA/IEA: seeded from mouse Rbfox only; no worm evidence ->
    MARK_AS_OVER_ANNOTATED (as for asd-1).
