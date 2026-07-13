# pgm notes

## 2026-07-06

First-pass PPP-adjacent review. Important alias issue: UniProt also has GpmI/Q88CX4 with synonym `pgm`, but the KEGG PSEPK pathway metadata for `pgm` in ppu00030 points to PP_3578/Q88GY7. The `pgm` folder was corrected to Q88GY7 before final validation.

UniProt identifies Q88GY7 as phosphoglucomutase EC 5.4.2.2 [file:PSEPK/pgm/pgm-uniprot.txt "DE   RecName: Full=Phosphoglucomutase {ECO:0000256|NCBIfam:TIGR01132};"] and maps the exact activity through UniRule/EC [file:PSEPK/pgm/pgm-uniprot.txt "DR   GO; GO:0004614; F:phosphoglucomutase activity; IEA:UniProtKB-UniRule."]. I accepted phosphoglucomutase activity, kept magnesium binding as non-core, marked broad carbohydrate/phosphotransferase terms as over-annotated, and removed the TreeGrafter phosphopentomutase/purine salvage calls as conflicting with the Q88GY7 enzyme identity.

Asta was regenerated after the accession correction and used only as a target-identity check [file:PSEPK/pgm/pgm-deep-research-asta.md "- **Protein Description:** RecName: Full=Phosphoglucomutase {ECO:0000256|NCBIfam:TIGR01132}; EC=5.4.2.2 {ECO:0000256|NCBIfam:TIGR01132};"].
