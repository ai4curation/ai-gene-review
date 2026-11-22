# NFYA2 review notes

## Session 1 (2026-10-26)

- Fetched with `just fetch-gene ARATH NFYA2`; UniProt Q9M9X4 confirmed (NFYA2_ARATH, 295 aa).
- Note: UniProt cross-reference is `GeneID; 819738` (At3g05690); the workflow task text gave
  NCBI Gene 839525, which does not match the UniProt record. The UniProt accession was used.
- No deep research API; literature synthesis in `NFYA2-deep-research-manual.md`.
- 13 GOA rows. Key decisions:
  - GO:0003700 (IEA, ISS) -> MODIFY to GO:0000981 (the gene already carries it by IBA; plant
    NF-Y targets are protein-coding Pol II genes such as FT, YUC2, HsfA3)
    [PMID:27977687 "In the presence of NF-YB2/NF-YC3 dimers, NF-YA2 and NF-YA6 bound the CCAAT probe in a concentration-specific manner"].
  - GO:0006355 (IEA, ISS) -> MODIFY to GO:0006357 (already carried by IBA).
  - Nucleus, CCAAT-binding factor complex, GO:0006357, GO:0000981 -> ACCEPT.
  - GO:0045893 positive regulation (IDA, PMID:25490919) -> ACCEPT but note NF-YA2 also
    represses targets (YUC2, ARGOS) [PMID:28469131 "Overexpression of NF-YA2 and NF-YA10 decreased contents of endogenous IAA through repressing yuc2 expression."].
  - Response to heat (IDA) -> KEEP_AS_NON_CORE: context role; conflicting direction
    between PMID:23118940 (OE tolerant) and PMID:36050841 (OE sensitive).
  - Double fertilization (IMP, PMID:15634699, abstract only) -> KEEP_AS_NON_CORE, defer to curator;
    lethality of nf-ya2 noted in PMID:27977687.
- NEW: GO:0048510 regulation of timing of transition from vegetative to reproductive phase.
  NF-YA2 itself, as the DNA-binding subunit of NF-Y, binds the FT CCAAT element in vitro
  [PMID:27977687] and SOC1 [PMID:25105952]; NF-YA2-EDLL fusion shows FT-dependent early flowering.
  This is direct participation as a transcription regulator, not substrate/necessity evidence.
  Direction neutral term chosen because PMID:24336445 reports late flowering upon OE.
