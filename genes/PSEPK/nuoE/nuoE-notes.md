# nuoE notes

- NuoE is the small 2Fe-2S electron-transfer subunit of the peripheral input arm
  [file:PSEPK/nuoE/nuoE-uniprot.txt "Name=[2Fe-2S] cluster"]. It relays
  electrons but does not independently oxidize NADH.

- GO:0051537 is retained as the direct cofactor function; whole-complex
  oxidoreductase terms are not treated as direct NuoE activities.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).
