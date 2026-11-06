# lptB (Q88P99) notes

P. putida KT2440 lptB is the orthologue of E. coli K-12 lptB (both in PANTHER PTHR45772:SF10).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptB/lptB-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `PF00005; ABC_tran`
- `PS00211; ABC_TRANSPORTER_1`
- `TIGR04406; LPS_export_lptB`

## E. coli literature cited

- PMID:19500581, PMID:24639492, PMID:27795402, PMID:29449493, PMID:30894744

## Decisions in this review

- GO:0000166 nucleotide binding (IEA): MODIFY to GO:0005524 ATP binding.
- GO:0005524 ATP binding (IEA): ACCEPT.
- GO:0005737 cytoplasm (IEA): KEEP_AS_NON_CORE.
- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0016887 ATP hydrolysis activity (IEA): ACCEPT.
- GO:0043190 ATP-binding cassette (ABC) transporter complex (IEA): ACCEPT.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: enables GO:0016887 ATP hydrolysis activity; processes GO:0015920; complex GO:0043190 ATP-binding cassette (ABC) transporter complex.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
