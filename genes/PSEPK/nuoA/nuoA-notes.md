# nuoA notes

- NuoA is a small membrane-interface subunit of proton-translocating complex I
  [file:PSEPK/nuoA/nuoA-uniprot.txt "RecName: Full=NADH-quinone oxidoreductase
  subunit A"]. Whole-complex catalytic terms describe a contribution of NuoA,
  not an independently catalyzed reaction.

- GO:0050136 is removed because its non-electrogenic definition conflicts with
  the proton-translocating NDH-1 system.

## 2026-10-23 re-review

- Deep-research providers unavailable (no API keys); reviewed manually from the
  UniProt record (HAMAP/RuleBase function text, family and TM features) and
  E. coli/Thermus literature by orthology (complete syntenic PP_4119-PP_4131
  nuo operon). See genes/ECOLI/nuoA/nuoA-notes.md for the E. coli evidence.
- Replaced RecName quotes with curated HAMAP/RuleBase FUNCTION, SUBUNIT,
  SIMILARITY and TRANSMEM text, or E. coli literature quotes.
- MODIFY rows that proposed the identical GO:0008137 were changed to ACCEPT (the
  contributes_to qualifier is expressed in core_functions instead).
- Broad terms MODIFIED to GO:0008137 / GO:0005886 / GO:0045271; NEW rows added
  for core-function terms not otherwise present (complex I membership,
  respiratory electron transport chain, and for nuoH also contributes_to
  GO:0008137 and proton transmembrane transport).
