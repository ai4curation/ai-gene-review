# nuoJ notes

- NuoJ is a small integral-membrane component of the proximal complex I
  coupling interface [file:PSEPK/nuoJ/nuoJ-uniprot.txt "RecName:
  Full=NADH-quinone oxidoreductase subunit J"].

- Whole-complex NADH:quinone activity and proton transport describe its
  contribution to assembled NDH-1 rather than a stand-alone reaction.

## 2026-10-23 re-review

- Deep-research providers unavailable (no API keys); reviewed manually from the
  UniProt record (HAMAP/RuleBase function text, family and TM features) and
  E. coli/Thermus literature by orthology (complete syntenic PP_4119-PP_4131
  nuo operon). See genes/ECOLI/nuoJ/nuoJ-notes.md for the E. coli evidence.
- Replaced RecName quotes with curated HAMAP/RuleBase FUNCTION, SUBUNIT,
  SIMILARITY and TRANSMEM text, or E. coli literature quotes.
- MODIFY rows that proposed the identical GO:0008137 were changed to ACCEPT (the
  contributes_to qualifier is expressed in core_functions instead).
- Broad terms MODIFIED to GO:0008137 / GO:0005886 / GO:0045271; NEW rows added
  for core-function terms not otherwise present (complex I membership,
  respiratory electron transport chain, and for nuoH also contributes_to
  GO:0008137 and proton transmembrane transport).
