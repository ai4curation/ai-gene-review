# nuoH notes

- NuoH is an integral membrane-interface subunit adjacent to the quinone site
  [file:PSEPK/nuoH/nuoH-uniprot.txt "RecName: Full=NADH-quinone oxidoreductase
  subunit H"]. It contributes coupling architecture rather than directly
  oxidizing NADH.

- Generic membrane is removed only because the same GOA set already provides
  the more precise plasma-membrane annotation.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).

## 2026-10-23 re-review

- Deep-research providers unavailable (no API keys); reviewed manually from the
  UniProt record (HAMAP/RuleBase function text, family and TM features) and
  E. coli/Thermus literature by orthology (complete syntenic PP_4119-PP_4131
  nuo operon). See genes/ECOLI/nuoH/nuoH-notes.md for the E. coli evidence.
- Replaced RecName quotes with curated HAMAP/RuleBase FUNCTION, SUBUNIT,
  SIMILARITY and TRANSMEM text, or E. coli literature quotes.
- MODIFY rows that proposed the identical GO:0008137 were changed to ACCEPT (the
  contributes_to qualifier is expressed in core_functions instead).
- Broad terms MODIFIED to GO:0008137 / GO:0005886 / GO:0045271; NEW rows added
  for core-function terms not otherwise present (complex I membership,
  respiratory electron transport chain, and for nuoH also contributes_to
  GO:0008137 and proton transmembrane transport).
