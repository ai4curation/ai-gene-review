# nuoG notes

- NuoG is a large peripheral-arm electron-relay subunit with both 2Fe-2S and
  4Fe-4S cofactors [file:PSEPK/nuoG/nuoG-uniprot.txt "Name=[2Fe-2S] cluster";
  "Name=[4Fe-4S] cluster"].

- Its only GOA localization is generic membrane. The review uses `MODIFY` to
  plasma membrane because deleting that row would strand the complex-associated
  subunit without any cellular-component annotation.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).
