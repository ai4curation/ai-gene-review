# lptD (A0A140FVZ0) notes

P. putida KT2440 lptD is the orthologue of E. coli K-12 lptD (both in PANTHER PTHR30189:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptD/lptD-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Interacts with LptE and LptA.`
- `PF04453; LptD`
- `SUBCELLULAR LOCATION: Cell outer membrane`
- `Together with LptE, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane.`

## E. coli literature cited

- PMID:12207697, PMID:16861298, PMID:20203010, PMID:24990744, PMID:26370939, PMID:29449493

## Decisions in this review

- GO:0009279 cell outer membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0019867 outer membrane (IEA): MODIFY to GO:0009279 cell outer membrane.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0061024 membrane organization (IEA): MODIFY to GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly.
- GO:1990351 transporter complex (IEA): MODIFY to GO:0062051 lipopolysaccharide transport system.
- GO:0015221 lipopolysaccharide transmembrane transporter activity (ISO): NEW, contributes_to (by orthology to E. coli lptD).
- Core function: contributes_to GO:0015221 lipopolysaccharide transmembrane transporter activity; processes GO:0015920, GO:0043165; complex GO:0062051 lipopolysaccharide transport system.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).
