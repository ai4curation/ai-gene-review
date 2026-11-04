# PP_0983 (Q88P70) notes

P. putida KT2440 PP_0983 is the orthologue of E. coli K-12 lptG (both in PANTHER PTHR33529:SF2).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptG/lptG-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `IPR030923; LptG`
- `PF03739; LptF_LptG`
- `TIGR04408; LptG_lptG`

## E. coli literature cited

- PMID:15919996, PMID:18375759, PMID:19500581, PMID:30894744

## Decisions in this review

- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0016020 membrane (IEA): MODIFY to GO:0005886 plasma membrane.
- GO:0043190 ATP-binding cassette (ABC) transporter complex (IEA): ACCEPT.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: contributes_to GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920; complex GO:0043190 ATP-binding cassette (ABC) transporter complex.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
