# tom22 notes

## 2026-11-24

- Ran `just fetch-gene SCHPO tom22` to create the UniProt, GOA, and review stub
  files for O13813 / SPAC17H9.16.
- Checked open pull requests and `origin/main` before editing; no current PR or
  main-branch gene review targeted `tom22` or SPAC17H9.16.
- Deep-research provider commands were unavailable in this checkout
  (`deep-research-falcon` had no usable provider and `deep-research-claude-code`
  was not logged in), so I recorded a manual TOM-focused literature summary in
  `tom22-deep-research-manual.md`.
- Reviewed all 12 fetched GOA rows. I accepted the outer membrane, TOM-complex,
  `GO:0140436`, `contributes_to GO:0008320`, and matrix-import rows; kept
  IMS/TIM22/TIM23-SORT TOM routes as non-core; and marked generic
  `GO:0006886 intracellular protein transport` as over-annotated.
- 69729a3800007453 consistency for the final GO-CAM PR: the Tom22 activities
  with root molecular_function `GO:0003674` should be refined against
  `GO:0140436 mitochondrial signal sequence receptor activity` or
  `contributes_to GO:0008320 protein transmembrane transporter activity`, as
  appropriate for each modeled step.
