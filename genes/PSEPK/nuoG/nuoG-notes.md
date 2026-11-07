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

## 2026-10-23 rework (bacterial complex I module)

Deep-research providers are unavailable in this environment (no API keys);
literature reviewed manually from cached publications and UniProt. All RecName
quotes replaced with curated UniProt CC FUNCTION/COFACTOR/SUBUNIT/SIMILARITY text
or E. coli ortholog literature (orthology argued in each reason; E. coli
ortholog review genes/ECOLI/nuoG). MODIFY rows that proposed the identical term
(enables -> contributes_to) changed to ACCEPT on the term, with contributes_to
recorded in core_functions. GO:0050136 (non-electrogenic) REMOVEd. NEW GO:0009055
electron transfer activity (ISS from E. coli) as the module leaf function.
Generic terms MODIFY to the specific terms carried. Status COMPLETE at zero
validation warnings.
