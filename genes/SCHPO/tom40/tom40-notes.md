# tom40 notes

## 2026-11-24

- Ran `just fetch-gene SCHPO tom40` to create the UniProt, GOA, and review stub
  files for O13656 / SPBC27B12.13.
- Checked open pull requests and `origin/main` before editing; no current PR or
  main-branch gene review targeted `tom40` or SPBC27B12.13.
- Deep-research provider commands were unavailable in this checkout
  (`deep-research-falcon` had no usable provider and `deep-research-claude-code`
  was not logged in), so I recorded a manual TOM-focused literature summary in
  `tom40-deep-research-manual.md`.
- Reviewed all 15 fetched GOA rows. I accepted `GO:0008320 protein
  transmembrane transporter activity`, TOM complex, and mitochondrial outer
  membrane annotations; kept matrix/IMS/TIM22/TIM23-SORT/beta-barrel TOM routes
  as non-core; and marked generic `GO:0055085 transmembrane transport` plus the
  ARBA mitochondrial membrane organization row as over-annotated.
- 69729a3800007453 consistency: no disagreement for tom40. The GO-CAM already
  models PomBase:SPBC27B12.13 with `GO:0008320`, TOM-complex membership,
  mitochondrial outer membrane occurrence, and `GO:0030150`.
