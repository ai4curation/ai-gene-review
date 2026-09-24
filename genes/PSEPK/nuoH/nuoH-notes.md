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
