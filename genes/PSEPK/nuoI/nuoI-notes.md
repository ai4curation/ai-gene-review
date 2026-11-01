# nuoI notes

- NuoI carries a 4Fe-4S cofactor in the distal peripheral-arm electron relay
  [file:PSEPK/nuoI/nuoI-uniprot.txt "Name=[4Fe-4S] cluster"]. Specific cluster
  binding is core; broad iron binding is valid but non-core.

- Generic membrane is removed because GOA also supplies plasma membrane, not
  because NuoI is an integral membrane-arm protein.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).

## 2026-10-23 re-review (complex I module promotion)

- Replaced RecName and sidecar quotes with HAMAP MF_01351 text (cofactor,
  function, location, family) and the E. coli NuoI study PMID:22474289, cited
  by orthology.
- Added NEW (ISS) rows: GO:0009055 electron transfer activity (core MF and
  module leaf), GO:0022904 respiratory electron transport chain, and
  GO:0045271 respiratory chain complex I.
- Iron ion binding is MODIFY -> GO:0051539. Membrane is MODIFY ->
  plasma membrane. GO:0016651 is MODIFY -> GO:0008137. Aerobic respiration is
  kept as non-core.
- Validation: 0 warnings and 0 errors (with UV_NATIVE_TLS unset).
