# lptC (Q88P97) notes

P. putida KT2440 lptC is the orthologue of E. coli K-12 lptC (both in PANTHER PTHR37481:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptC/lptC-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Facilitates the transfer of LPS from the inner membrane to the periplasmic protein LptA.`
- `SUBCELLULAR LOCATION: Cell inner membrane`
- `TIGR04409; LptC_YrbK`

## E. coli literature cited

- PMID:16765569, PMID:20720015, PMID:29449493, PMID:30894744

## Decisions in this review

- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0017089 glycolipid transfer activity (IEA): MODIFY to GO:0140332 lipopolysaccharide transfer activity.
- GO:0030288 outer membrane-bounded periplasmic space (IEA): ACCEPT.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0046836 glycolipid transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- GO:0140332 lipopolysaccharide transfer activity (IEA): ACCEPT.
- Core function: enables GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920, GO:0043165.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
