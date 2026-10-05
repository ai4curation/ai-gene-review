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
