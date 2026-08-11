---
title: "PSEPK ppu03070 bacterial type II secretion batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pilD, xcpP, xcpQ, gspE, gspF, gspG, xcpU, xcpV, xcpW, xcpX, xcpY, xcpZ]
autolink_gene_symbols: false
---

# PSEPK ppu03070: bacterial type II secretion

- Reusable module: `modules/bacterial_type_ii_secretion.yaml`
- Target branch: Xcp/Gsp type II secretion within KEGG `ppu03070`
- Correct boundary: inner-membrane platform, GspE ATPase, pseudopilus, and
  outer-membrane GspD/XcpQ secretin
- Focused PSEPK proteins reviewed: 12
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate the Xcp/Gsp type II branch from the broad KEGG secretion map.
- [x] Keep Sec and Tat substrate delivery outside the T2SS module.
- [x] Exclude type IV pilus and unrelated fimbrial proteins despite shared folds.
- [x] Exclude type I, type V/TPS, and type VI secretion machinery.
- [x] Model the inner-membrane platform, ATPase, pseudopilus, and secretin as
  substantive root parts.
- [x] Assign ATP hydrolysis only to the GspE leaf.
- [x] Ground every leaf with an exact UniProt exemplar and focused review.
- [x] Complete an annotation-reviewer pass for every focused review.
- [x] Run generic and PSEPK ppu03070 OpenScientist research requests with normal timeouts.
- [x] Validate and render the module, reviews, and project page.
- [x] Open one dedicated draft PR.
- [ ] Shepherd review and CI.

## Satisfiability

| Part | Conserved role | PSEPK implementation | UniProt | Decision |
|---|---|---|---|---|
| Inner-membrane platform | GspC connector | `xcpP` | Q88P08 | Core |
| Inner-membrane platform | GspF platform core | `gspF` | Q88P05 | Core |
| Inner-membrane platform | GspL ATPase-facing subunit | `xcpY` | Q88P00 | Core |
| Inner-membrane platform | GspM stabilizer | `xcpZ` | Q88NZ9 | Core |
| Secretion ATPase | GspE motor | `gspE` | Q88P06 | Core catalytic motor |
| Pseudopilus | shared prepilin leader peptidase/N-methyltransferase | `pilD` | Q88Q64 | Required maturation enzyme |
| Pseudopilus | GspG major pseudopilin | `gspG` | Q88P04 | Core structural subunit |
| Pseudopilus | GspH minor pseudopilin | `xcpU` | Q88P03 | Core tip/initiation subunit |
| Pseudopilus | GspI minor pseudopilin | `xcpV` | Q88P02 | Core tip/initiation subunit |
| Pseudopilus | GspJ minor pseudopilin | `xcpW` | Q88P01 | Core tip/initiation subunit |
| Pseudopilus | GspK minor pseudopilin | `xcpX` | Q88P11 | Core tip/initiation subunit |
| Outer-membrane secretin | GspD channel | `xcpQ` | Q88P07 | Core outer-membrane exit |

The PP_1042 and PP_1045-PP_1054 Xcp/Gsp region supplies the platform, motor,
pseudopilins, and secretin. PilD/PP_0632 supplies the shared prepilin-processing
activity required to mature the pseudopilins. `gspN`/PP_1055 is adjacent but
remains a lineage-variable accessory candidate, not a required part of the
conserved module.

## Annotation Decisions

- GspE alone retains `GO:0016887` ATP hydrolysis activity. Platform,
  pseudopilus, and secretin subunits receive no inferred catalytic MF.
- XcpQ receives `GO:0008320` protein transmembrane transporter activity for the
  secretin channel, and GspG receives `GO:0005198` structural molecule activity
  for the major pseudopilus subunit.
- PilD retains leader-peptidase activity and gains the specific
  `GO:0071885` N-terminal protein N-methyltransferase activity; both MFs are
  attached to PilD leaves under the pseudopilus-maturation part.
- Existing `GO:0015627` T2SS-complex and `GO:0015628` T2SS-process annotations
  are accepted when the exact Gsp/Xcp family assignment is diagnostic.
- Broad `protein secretion`, `membrane`, and duplicate generic outer-membrane
  terms are marked over-annotated where a more specific existing term is
  available.
- XcpX broad protein secretion is refined to the T2SS-specific process.
- Missing T2SS complex/process and plasma-membrane assertions are proposed as
  NEW for XcpP, XcpW, XcpY, and XcpZ based on exact family identity, topology,
  and locus context.
- The existing PilA review is not folded into this batch: it correctly removes
  T2SS annotations caused by a shared pilin-domain mapping and retains type IV
  pilus biology.

## Boundary Decisions

- SecYEG/SecA/SecDF and TatABC deliver substrates across the inner membrane.
  They are upstream routes and are not components of the T2SS machine.
- Type IV pilus proteins and generic fimbrial proteins are excluded. Homology
  between T4P and T2SS components does not establish membership in both systems.
- TPS/type V proteins, type I ABC exporters, and type VI secretion proteins on
  the broad KEGG map are separate modules.
- Signal-peptide cleavage, periplasmic folding, and substrate-specific
  extracellular functions remain outside the machine boundary.
- GspN is recorded as an accessory candidate because it is not a uniformly
  conserved required component of the canonical four-part architecture.
- The reusable module contains no generic cytoplasm or cytosol assertion.
- Molecular functions are present only on leaf annotons.

## Research Status

The module/pathway/taxon report is stored under
`projects/P_PUTIDA/deep-research/` with its completed HTML and PDF artifacts.
The generic module request remained queue-bound and was stopped when publication
was prioritized; it produced no report and is not cited as evidence. Local
UniProt, GOA, InterPro, PANTHER, and focused gene reviews provide the
identifier-level grounding.

## Validation

All twelve focused reviews, the `ModuleReview`, the module validator, and the
rendered module and batch pages are checked before publication.
