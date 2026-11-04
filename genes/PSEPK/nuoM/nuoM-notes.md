# nuoM notes

- NuoM is an antiporter-like integral membrane-arm subunit of complex I
  [file:PSEPK/nuoM/nuoM-uniprot.txt "RecName: Full=NADH-quinone oxidoreductase
  subunit M"].

- GOA provides only generic membrane localization, so the review uses `MODIFY`
  to plasma membrane rather than deleting the only cellular-component row.
  Ubiquinone binding is removed because NuoM is distal to the quinone-reactive
  cavity.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).

## 2026-10-23 rework (Claude Code)

Deep-research providers are unavailable (no API keys); reviewed manually from the
UniProt record, cached E. coli literature and the existing OpenScientist module report.
- Replaced RecName quotes (labels, not evidence) with family cross-references from the
  TrEMBL record (IPR010227, TIGR01972, PTHR43507:SF1, PF00361) and E. coli evidence by
  orthology [PMID:21822288 "Each repeat includes a discontinuous transmembrane helix and
  forms half of a channel across the membrane."; PMID:18590697 "The quinone reductase
  activity was practically lost in K234A, K234R and E144A"]. The record's "Belongs to"
  note is ARBA-derived and was not quoted.
- GO:0003954 KEEP_AS_NON_CORE -> MODIFY to GO:0008137 (correct-but-general rule).
- GO:0008137 MODIFY-to-same-id -> ACCEPT (qualifier change not expressible).
- GO:0048039 REMOVE -> MARK_AS_OVER_ANNOTATED, consistent with E. coli nuoM review
  (quinone site at Nqo4/6/8 [PMID:23417064 "there are no cofactors in the membrane and
  the antiporter-like subunits"]).
- Added NEW part_of GO:0045271 (ISS from E. coli). Core process uses GO:0015990 and
  GO:0042773. `just validate PSEPK nuoM`: zero warnings/errors; status COMPLETE.
