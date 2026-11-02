# lptA (Q88P98) notes

P. putida KT2440 lptA is the orthologue of E. coli K-12 lptA (both in PANTHER PTHR36504:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptA/lptA-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `May form a bridge between the inner membrane and the outer membrane, via interactions with LptC and LptD, thereby facilitating LPS transfer across the periplasm.`
- `Required for the translocation of LPS from the inner membrane to the outer membrane.`
- `SUBCELLULAR LOCATION: Periplasm`
- `TIGR03002; outer_YhbN_LptA`

## E. coli literature cited

- PMID:17056748, PMID:18424520, PMID:18480051, PMID:20446753, PMID:20720015, PMID:22668317, PMID:29449493

## Decisions in this review

- GO:0001530 lipopolysaccharide binding (IEA): ACCEPT.
- GO:0009279 cell outer membrane (IEA): KEEP_AS_NON_CORE.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0017089 glycolipid transfer activity (IEA): MODIFY to GO:0140332 lipopolysaccharide transfer activity.
- GO:0030288 outer membrane-bounded periplasmic space (IEA): ACCEPT.
- GO:0042597 periplasmic space (IEA): MODIFY to GO:0030288 outer membrane-bounded periplasmic space.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0046836 glycolipid transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: enables GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920, GO:0043165.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
