# nuoL notes

- NuoL is an antiporter-like membrane-arm subunit required for complex I proton
  translocation [file:PSEPK/nuoL/nuoL-uniprot.txt "RecName:
  Full=NADH-quinone oxidoreductase subunit L"]. It does not directly oxidize
  NADH.

- Generic membrane is removed as redundant because plasma membrane is already
  present in GOA.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).
