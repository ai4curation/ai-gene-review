---
title: "PSEPK ppu00900 MEP isoprenoid precursor biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [dxs, dxr, ispD, ispE, ispF, ispG, ispH]
autolink_gene_symbols: false
---

# PSEPK ppu00900: MEP isoprenoid precursor biosynthesis

This batch extracts the complete seven-reaction MEP/DOXP precursor route from
the broader 17-gene KEGG `ppu00900` membership bucket. The reusable module is
`modules/mep_isoprenoid_precursor_biosynthesis.yaml`.

## Boundary

The core route is `dxs` -> `dxr` -> `ispD` -> `ispE` -> `ispF` -> `ispG` ->
`ispH`. DXS is included because it forms DXP at the route entry, but DXP also
feeds vitamin biosynthesis; Dxr is the first committed MEP reaction. IspH forms
both IPP and DMAPP.

The following KEGG members are outside this module:

| Gene(s) | Reason excluded |
|---|---|
| `ispA` | Downstream farnesyl diphosphate synthesis from IPP/DMAPP. |
| `ispB` | Downstream octaprenyl diphosphate synthesis. |
| `uppS` | Downstream undecaprenyl diphosphate synthesis. |
| `ubiX` | Prenylated-FMN cofactor synthesis, not MEP precursor formation. |
| `PP_0582`, `fadA__Q88L84`, `PP_2215`, `PP_3355`, `bktB`, `yqeF` | Thiolase/acetyl-CoA chemistry included in the broad KEGG backbone map but not in the MEP route. |

## Selected Genes

| Step | Gene | Locus | UniProt | Core activity | Gene research |
|---:|---|---|---|---|---|
| 1 | `dxs` | PP_0527 | Q88QG7 | GO:0008661 DXP synthase | OpenScientist complete and assessed |
| 2 | `dxr` | PP_1597 | Q88MH4 | GO:0030604 DXP reductoisomerase | OpenScientist complete and assessed |
| 3 | `ispD` | PP_1614 | Q88MF7 | GO:0050518 MEP cytidylyltransferase | Existing Falcon report assessed |
| 4 | `ispE` | PP_0723 | Q88PX5 | GO:0050515 CDP-ME kinase | OpenScientist complete and assessed |
| 5 | `ispF` | PP_1618 | Q88MF3 | GO:0008685 ME-CPP synthase | OpenScientist complete and assessed |
| 6 | `ispG` | PP_0853 | Q88PJ7 | GO:0141197 flavodoxin-coupled HMBPP synthase | OpenScientist running |
| 7 | `ispH` | PP_0606 | Q88Q89 | GO:0051745 HMBPP reductase | OpenScientist complete and assessed |

## Curation Findings

- The seven PSEPK Swiss-Prot entries satisfy every required reaction; no pathway
  hole is apparent in the first pass.
- DXS is a route-entry enzyme rather than a committed MEP step because DXP is a
  branch-point metabolite.
- For IspG, Rhea 43604 and the reviewed UniProt record support the
  flavodoxin-specific GO:0141197 term. The ferredoxin-specific GO:0046429 IEA is
  marked for modification rather than treated as a second core activity.
- IspH directly supports both GO:0019288 and GO:0050992 because its terminal
  reaction produces both IPP and DMAPP.
- Every module leaf has PSEPK and E. coli UniProt exemplars. Canonical PAINT IBD
  nodes were added for DXS (`PTN000179250`), Dxr (`PTN000776155`), IspD
  (`PTN000781812`), IspE (`PTN000466527`), IspF (`PTN000781796`), and IspH
  (`PTN000764789`). The IspG PAINT node supports the ferredoxin sibling term,
  not the flavodoxin term used here, so it was deliberately not asserted.

## Workflow Status

- [x] Partition the 17 KEGG candidates into the seven-step route and out-of-scope entries.
- [x] Fetch all seven selected genes with current UniProt and GOA records.
- [x] Complete an initial manual review of every GOA row.
- [x] Build and validate a species-neutral seven-part module.
- [x] Add exact Rhea reactions, paired UniProt exemplars, and locally verified PAINT nodes.
- [ ] Complete and assess the remaining gene-level OpenScientist reports.
- [ ] Complete and assess generic OpenScientist module research.
- [ ] Complete and assess PSEPK module + pathway + taxon research.
- [ ] Reconcile gene reviews, pathway boundary, and module against completed research.
- [ ] Validate and render all affected artifacts.
- [x] Open draft pull request #2182 for this module.
- [ ] Shepherd the pull request through review and CI to merge readiness.

## Files

- Module: `modules/mep_isoprenoid_precursor_biosynthesis.yaml`
- Generic research: `modules/mep_isoprenoid_precursor_biosynthesis-deep-research-openscientist.md`
- PSEPK pathway research: `projects/P_PUTIDA/deep-research/PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist.md`
- Membership table: `projects/P_PUTIDA/batches/ppu00900_mep_isoprenoid_precursor_biosynthesis.tsv`
