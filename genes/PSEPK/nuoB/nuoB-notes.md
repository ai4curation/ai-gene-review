# nuoB notes

- NuoB carries a 4Fe-4S cofactor near the quinone-reduction arm
  [file:PSEPK/nuoB/nuoB-uniprot.txt "Name=[4Fe-4S] cluster"]. GO:0051539 is the
  core cofactor term; broad iron-ion and iron-sulfur binding are retained as
  non-core rather than removed.

- Quinone binding and complex I membership are retained, while whole-complex
  catalytic activity requires a contributes-to interpretation.

## 2026-10-23 rework (bacterial complex I module)

Deep-research providers are unavailable in this environment (no API keys);
literature reviewed manually from cached publications and UniProt. All RecName
quotes replaced with curated UniProt CC FUNCTION/COFACTOR/SUBUNIT/SIMILARITY text
or E. coli ortholog literature (orthology argued in each reason; E. coli
ortholog review genes/ECOLI/nuoB). MODIFY rows that proposed the identical term
(enables -> contributes_to) changed to ACCEPT on the term, with contributes_to
recorded in core_functions. GO:0050136 (non-electrogenic) REMOVEd. NEW GO:0009055
electron transfer activity (ISS from E. coli) as the module leaf function.
Generic terms MODIFY to the specific terms carried. Status COMPLETE at zero
validation warnings.
