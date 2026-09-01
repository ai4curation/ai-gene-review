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
| 6 | `ispG` | PP_0853 | Q88PJ7 | GO:0141197 flavodoxin-coupled HMBPP synthase | OpenScientist complete and assessed |
| 7 | `ispH` | PP_0606 | Q88Q89 | GO:0051745 HMBPP reductase | OpenScientist complete and assessed |

## Wave117 Repair

This repair preserves the reusable seven-reaction route while tightening family,
reaction, and evolutionary grounding. The module now uses exact PANTHER
subfamilies for DXS, Dxr, IspD, IspE, IspF, and IspH. Several official PANTHER
labels are chloroplast-biased even though their verified member sets contain the
reviewed bacterial exemplars; those labels are retained verbatim and accompanied
by explicit scope caveats rather than rewritten.

IspG remains represented by separate flavodoxin- and ferredoxin-coupled leaves.
Both use the parent PANTHER family because the indexed SF0 label conflates the
ferredoxin/chloroplast implementation with reviewed flavodoxin-coupled bacterial
members. Carrier specificity is instead grounded by each leaf's exact GO
molecular function, Rhea reaction, and reviewed UniProt exemplar. No IspG PTN is
asserted because the available PAINT node supports the ferredoxin term but does
not cleanly distinguish the two carrier-specific implementations. The other six
steps retain only locally verified PAINT IBD nodes.

The existing completed OpenScientist reports were reused: generic module research
completed in 1,643 seconds, and PSEPK pathway/taxon research completed in 1,187
seconds. No replacement run was needed. A required annotation-reviewer pass
examined all existing annotations, evidence, core functions, and proposed terms
for `dxs`, `dxr`, `ispD`, `ispE`, `ispF`, `ispG`, and `ispH`; it found no blocking
biological, GO, or evidence issue and recommended no gene-review edit.

For PSEPK specifically, the seven reviewed UniProt entries cover every reaction.
DXS remains a shared route entry and Dxr the commitment step. Q88PJ7 supports the
flavodoxin-coupled IspG reaction, but its physiological flavodoxin/reductase
partners have not been established directly in KT2440. Q88Q89 IspH directly
supports alternative IPP- and DMAPP-forming branches, so a separate native IDI is
not required to complete the route. Direct KT2440 biochemical assays were not
located for every enzyme, and those target-specific evidence gaps are not promoted
to generic module claims.

## Curation Findings

- The seven PSEPK Swiss-Prot entries satisfy every required reaction; no pathway
  hole is apparent in the first pass.
- DXS is a route-entry enzyme rather than a committed MEP step because DXP is a
  branch-point metabolite.
- For PSEPK IspG, Rhea 43604 and the reviewed UniProt record support the
  flavodoxin-specific GO:0141197 term. The unsupported ferredoxin-specific IEA
  is removed rather than modified because the exact flavodoxin annotation is
  already independently present. The reusable module separately models the
  ferredoxin-coupled implementation with GO:0046429, Rhea 26119, and the
  reviewed cyanobacterial exemplar UniProtKB:Q3AK30.
- IspH directly supports both GO:0019288 and GO:0050992 because its terminal
  reaction produces both IPP and DMAPP.
- Species-aware OpenScientist research independently recovered the seven core
  genes and the same ten out-of-scope bucket members. Its "seven committed
  steps" wording was not adopted: DXS remains a shared branch-point entry.
- No native IDI is present in the current KT2440 proteome, but this is not a
  pathway hole because IspH directly forms both IPP and DMAPP. The `idi` used
  in PMID:31500633 was cloned from *E. coli*, as stated in the paper's Methods.
  KEGG M00096 includes a separate K01823 IDI step, so this curated module is
  intentionally not treated as a literal M00096 transcription.
- The report's proposed PP_0142/PP_0959 "reannotation" was not propagated:
  local metadata already assigns these proteins to the ABC-transporter bucket,
  outside the ppu00900 candidate set.
- The PSEPK implementation of every required step has paired PSEPK and E. coli
  UniProt exemplars, and the alternate ferredoxin-coupled IspG leaf has a
  reviewed cyanobacterial exemplar. Canonical PAINT IBD nodes were added for
  DXS (`PTN000179250`), Dxr (`PTN000776155`), IspD
  (`PTN000781812`), IspE (`PTN000466527`), IspF (`PTN000781796`), and IspH
  (`PTN000764789`). The IspG PAINT node supports the ferredoxin sibling term,
  but does not cleanly separate the carrier-specific subfamilies, so it was
  deliberately not asserted.
- Generic OpenScientist module research supported the seven-reaction order,
  the DXS/Dxr boundary, direct dual output by IspH, and electron-carrier
  variation at IspG. Its claims that MEP and MVA are universally mutually
  exclusive, that DXS is universally rate-limiting, and that all seven steps
  are obligatory in every biological context were not adopted. MEP-intermediate
  signaling, detailed Fe-S mechanism, and downstream metabolism remain outside
  this module's core.
- IspG OpenScientist research supports the family-level ME-CPP-to-HMBPP
  reaction and conserved [4Fe-4S] architecture but found no direct biochemical,
  structural, or knockout study of Q88PJ7. Ortholog mechanism, claimed
  essentiality, and inferred cytoplasmic localization were not promoted as
  target-specific evidence; the native KT2440 flavodoxin/reductase partners
  remain unresolved.

## Workflow Status

### Wave117 Repair

- [x] Re-audit the seven-reaction boundary and all seven PSEPK gene reviews.
- [x] Verify exact PANTHER labels, member containment, reviewed exemplars, and PAINT nodes.
- [x] Separate flavodoxin- and ferredoxin-coupled IspG implementations conservatively.
- [x] Reuse and assess completed generic and PSEPK OpenScientist research.
- [x] Complete the required annotation-reviewer consult for all seven genes.

### Initial Pass

- [x] Partition the 17 KEGG candidates into the seven-step route and out-of-scope entries.
- [x] Fetch all seven selected genes with current UniProt and GOA records.
- [x] Complete an initial manual review of every GOA row.
- [x] Build and validate a species-neutral seven-part module.
- [x] Add exact Rhea reactions, paired UniProt exemplars, and locally verified PAINT nodes.
- [x] Complete and assess the remaining gene-level OpenScientist reports.
- [x] Complete and assess generic OpenScientist module research.
- [x] Complete and assess PSEPK module + pathway + taxon research.
- [x] Reconcile gene reviews, pathway boundary, and module against completed research.
- [x] Validate and render all affected artifacts.
- [x] Open draft pull request #2182 for this module.
- [x] Shepherd the pull request through review and CI to merge readiness.

## Files

- Module: `modules/mep_isoprenoid_precursor_biosynthesis.yaml`
- Generic research: `modules/mep_isoprenoid_precursor_biosynthesis-deep-research-openscientist.md`
- PSEPK pathway research: `projects/P_PUTIDA/deep-research/PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist.md`
- Membership table: `projects/P_PUTIDA/batches/ppu00900_mep_isoprenoid_precursor_biosynthesis.tsv`
