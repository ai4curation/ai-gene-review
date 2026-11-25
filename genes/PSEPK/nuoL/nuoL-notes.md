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

## 2026-11-01 rework

All CC text in the PP_4129 UniProt record is ARBA-derived, so it is not quoted. Support now
comes from family/domain signatures (NCBIfam TIGR01974 NDH_I_L, InterPro IPR001750 ND/Mrp_TM),
Phobius TM helices (16), and E. coli NuoL literature by orthology (PMID:21417432, PMID:36104567,
PMID:23864658). The earlier MODIFY that proposed the identical GO:0008137 was changed to ACCEPT,
with contributes_to noted in the reason. GO:0003954 MODIFY to GO:0008137; GO:0016020 MODIFY to
GO:0005886; NEW part_of GO:0045271 (ISS) added because complex membership was missing from GOA.
The earlier note saying "generic membrane is removed" is superseded: the row is now MODIFY, not REMOVE.
Deep-research providers are unavailable here (no API keys).
