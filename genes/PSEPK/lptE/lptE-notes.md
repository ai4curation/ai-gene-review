# lptE (Q88DN0) notes

P. putida KT2440 lptE is the orthologue of E. coli K-12 lptE (both in PANTHER PTHR38098:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptE/lptE-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Binds LPS and may serve as the LPS recognition site at the outer membrane.`
- `Interacts with LptD.`
- `PF04390; LptE`
- `Required for the proper assembly of LptD.`
- `SUBCELLULAR LOCATION: Cell outer membrane`

## E. coli literature cited

- PMID:16861298, PMID:20203010, PMID:21257904, PMID:21257909, PMID:24938785, PMID:29449493

## Decisions in this review

- GO:0001530 lipopolysaccharide binding (IEA): ACCEPT.
- GO:0009279 cell outer membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0019867 outer membrane (IEA): MODIFY to GO:0009279 cell outer membrane.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:1990351 transporter complex (IEA): MODIFY to GO:0062051 lipopolysaccharide transport system.
- GO:0015221 lipopolysaccharide transmembrane transporter activity (ISO): NEW, contributes_to (by orthology to E. coli lptE).
- Core function: enables GO:0001530 lipopolysaccharide binding and contributes_to GO:0015221 lipopolysaccharide transmembrane transporter activity; processes GO:0015920, GO:0043165; complex GO:0062051 lipopolysaccharide transport system.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
