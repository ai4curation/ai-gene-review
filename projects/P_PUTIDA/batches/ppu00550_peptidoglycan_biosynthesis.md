---
title: "PSEPK peptidoglycan precursor biosynthesis and export"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK peptidoglycan precursor biosynthesis and export

This batch models the conserved pathway from UDP-N-acetylglucosamine through
UDP-MurNAc-pentapeptide, lipid I, and lipid II to translocation of lipid II
across the cytoplasmic membrane. It stops before glycan polymerization and
peptide cross-linking, which form a distinct multi-complex module.

## Workflow

- [x] Fetch the nine gene records not already present.
- [ ] Run full OpenScientist research for all ten selected genes.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral
  `peptidoglycan_precursor_biosynthesis` module.
- [x] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00550` + PSEPK research.
- [x] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `murA` | PP_0964 | Q88P88 | UDP-GlcNAc enolpyruvyl transfer |
| [ ] | `murB` | PP_1904 | Q88LM5 | UDP-MurNAc formation |
| [ ] | `murC` | PP_1338 | Q88N75 | L-alanine addition |
| [ ] | `murD` | PP_1335 | Q88N78 | D-glutamate addition |
| [ ] | `murE` | PP_1332 | Q88N81 | meso-diaminopimelate addition |
| [ ] | `ddlB` | PP_1339 | Q88N74 | D-Ala-D-Ala dipeptide synthesis |
| [ ] | `murF` | PP_1333 | Q88N80 | D-Ala-D-Ala addition to UDP-MurNAc-tripeptide |
| [ ] | `mraY` | PP_1334 | Q88N79 | Lipid I synthesis |
| [ ] | `murG` | PP_1337 | Q88N76 | Lipid II synthesis |
| [ ] | `murJ` | PP_0601 | Q88Q94 | Lipid II translocation |

## Boundary Decisions

- `murJ` is added despite its absence from the broad KEGG `ppu00550` extract
  because lipid II translocation is required to connect cytoplasmic precursor
  synthesis to periplasmic assembly.
- `ftsW`/`ftsI`, `mrdB`/`mrdA`, class A PBPs, PbpC, and MtgA belong to the
  downstream polymerization and cross-linking module.
- `uppS` and `uppP` supply and recycle the undecaprenyl carrier but are not
  direct lipid II synthesis steps.
- D-Ala-D-Ala carboxypeptidases `dacA` and `dacB` are remodeling enzymes.
- `ddlA` and the third Ddl paralog are alternative D-Ala-D-Ala ligases in
  KT2440; the division-cluster `ddlB` copy is used as the concrete exemplar
  while paralog use is tested by the pathway-level research.

The complete 23-gene KEGG source snapshot remains in
`ppu00550_peptidoglycan_biosynthesis.tsv`.
