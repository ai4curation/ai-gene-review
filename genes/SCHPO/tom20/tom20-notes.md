# tom20 notes

## 2026-11-24

- Ran `just fetch-gene SCHPO tom20` to create the UniProt, GOA, and review stub
  files for O14225 / SPAC6F12.07.
- Checked open pull requests and `origin/main` before editing; no current PR or
  main-branch gene review targeted `tom20` or SPAC6F12.07.
- Deep-research provider commands were unavailable in this checkout
  (`deep-research-falcon` had no usable provider and `deep-research-claude-code`
  was not logged in), so I recorded a manual TOM-focused literature summary in
  `tom20-deep-research-manual.md`.
- Reviewed all 15 fetched GOA rows. I accepted TOM complex, mitochondrial outer
  membrane, and matrix-import annotations, kept other TOM routes as non-core,
  added missing `GO:0140436 mitochondrial signal sequence receptor activity`,
  and marked generic `intracellular protein transport`, generic ARBA
  mitochondrial membrane organization, and the PAINT tRNA-import transfer as
  over-annotated.
- 69729a3800007453 consistency: no disagreement for tom20. The GO-CAM already
  models PomBase:SPAC6F12.07 with `GO:0140436`, TOM-complex membership,
  mitochondrial outer membrane occurrence, and `GO:0030150`.
