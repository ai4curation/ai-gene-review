---
title: "PSEPK ppu00790 molybdenum-cofactor biosynthesis subset batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00790: Molybdenum-cofactor biosynthesis subset

- Module: `molybdenum_cofactor_biosynthesis`
- KEGG ppu00790 candidates examined: 32
- Core genes recovered from ppu04122: 2 (`moaD`, `moeB`)
- Selected gene reviews: 13
- Fetched GOA rows reviewed: 59 of 59 (no `PENDING` actions)
- Justified new gene annotations: 1 (`moaD` `part_of` GO:1990140)
- Conserved core roles covered: 6
- Optional MGD/MCD maturation genes covered: 3
- Paralog assignments retained as uncertain: 4
- Broad-map candidates excluded: 21

## Scope

This batch extracts molybdenum-cofactor biosynthesis from the broad KEGG
`ppu00790` "Folate biosynthesis" map. The modeled boundary begins with GTP
cyclization and cPMP formation, includes MoaD carrier activation and
MoaD-MoaE-dependent MPT synthesis, continues through MPT activation and MoeA
molybdate insertion, and includes optional MobA/MocA nucleotide-maturation
branches. It ends at Mo-MPT, MGD, or MCD.

Upstream sulfur supply, molybdate transport, terminal cofactor sulfuration,
cofactor insertion and its chaperones, mature molybdoenzyme subunits and client
reactions, and regulation are outside scope. These downstream operations remain
outside even when a MobA/MocA nucleotide-maturation variant is represented.
Folate, queuosine, riboflavin, and pterin-recycling genes appearing on broad
map00790 are also outside scope.

## Required Workflow

- [x] Fetch missing selected-gene scaffolds.
- [ ] Run OpenScientist research for every selected gene.
- [ ] Run generic module OpenScientist research.
- [ ] Run module + ppu00790 + PSEPK OpenScientist research.
- [x] Curate every GOA row with no `PENDING` actions.
- [ ] Revise and validate the reusable module.
- [ ] Validate and render selected gene reviews and batch artifacts.
- [ ] Open one non-draft PR for this module/pathway.
- [ ] Shepherd the PR through review and CI.

## Selected Genes

| Decision | Gene | Locus | UniProt | Role | Curation conclusion |
|---|---|---|---|---|---|
| COVERED_CORE | `moaA` | PP_4597 | Q88E69 | GTP 3',8'-cyclase | Canonical reviewed MoaA; cPMP synthase annotation removed because that reaction belongs to MoaC. |
| CANDIDATE_UNCERTAIN | `PP_2482` | PP_2482 | Q88K11 | MoaA-family paralog | Radical-SAM/[4Fe-4S] features retained; exact GTP-cyclase activity and redundancy with `moaA` remain undecided. |
| CANDIDATE_UNCERTAIN | `PP_1969` | PP_1969 | Q88LG4 | MoaA-family paralog | Closely related to PP_2482 but divergent from canonical MoaA; exact substrate and pathway role remain undecided. |
| COVERED_CORE | `moaC` | PP_1292 | Q88NC0 | cPMP synthase | Exact GO:0061799 activity retained. |
| RECOVERED_CORE | `moaD` | PP_1293 | Q88NB9 | MPT synthase sulfur carrier | Existing GO:1990133 for the transient MoeB-MoaD activation complex is retained; an ISS `NEW` GO:1990140 row captures the distinct MoaD-MoaE synthase complex used in the core function. |
| COVERED_CORE | `moaE` | PP_1294 | Q88NB8 | MPT synthase catalytic subunit | Exact GO:0030366 activity retained. |
| RECOVERED_CORE | `moeB` | PP_0735 | Q88PW3 | MoaD adenylyltransferase | Exact GO:0061605 retained; GO:0008641 is removed because MoaD acyl-adenylation does not satisfy the live term's E1 thiolester requirement. |
| COVERED_CORE | `moeA` | PP_2123 | Q88L14 | MPT molybdotransferase | Exact GO:0061599 activity retained. |
| CANDIDATE_UNCERTAIN | `moaB-I` | PP_2122 | Q88L15 | possible MogA-equivalent/accessory protein | No standalone MogA was found; UniProt says this MoaB family lacks MPT adenylyltransferase activity, so pathway necessity remains undecided. |
| CANDIDATE_UNCERTAIN | `moaB-II` | PP_4600 | Q88E67 | possible MogA-equivalent/accessory protein | Same unresolved family-level conflict as `moaB-I`; no exact catalytic GO term was added. |
| COVERED_VARIANT | `mobA` | PP_3457 | Q88HA3 | MGD branch | Reviewed Mo-MPT guanylyltransferase GO:0061603 retained as an optional downstream variant. |
| COVERED_VARIANT | `PP_2483` | PP_2483 | Q88K10 | predicted MocA/MCD branch | K07141 plus local subfamily and neighborhood evidence support GO:0061602 as a replacement for broad nucleotidyltransferase; direct CTP assay is absent. |
| COVERED_VARIANT | `PP_4230` | PP_4230 | Q88F68 | predicted MocA/MCD branch | K07141 plus local subfamily and neighborhood evidence support GO:0061602 as a replacement for broad nucleotidyltransferase; client dedication remains inferential. |

GO:1990140 is an existing live GO cellular-component term, so the proposal is an
`action: NEW` row in `existing_annotations`, supported by the PTHR33359:SF1
ortholog and the conserved MoaD-MoaE heterotetramer. `proposed_new_terms` remains
empty because no new ontology class is being requested.

## MogA Search

No standalone KT2440 protein mapped to the locally fetched MogA family
PTHR43764 or to KEGG K03831. The only small MoaB/Mog-fold candidates are
`moaB-I` and `moaB-II` (both K03638/PTHR43232), while `moeA` carries the
separate molybdotransferase architecture. Because MoaB catalytic competence is
lineage-dependent and the two target entries explicitly carry a transferred
"no MPT adenylyltransferase activity" statement, neither paralog is asserted as
the missing MogA-equivalent. Direct MPT-AMP and MoeA-coupled assays are needed.

## Excluded Broad-Map Genes

| Category | Genes | Reason |
|---|---|---|
| Folate and pterin synthesis | `folB`, `PP_0393`, `folE1`, `folE2__Q88JY1`, `folE2__Q88HM9`, `pabB`, `pabC`, `folC`, `folK`, `folP`, `folA`, `folM` | Build or reduce folate/monapterin intermediates, not Mo-MPT. |
| Queuosine synthesis | `queC`, `queD`, `queE`, `queF` | Make preQ0/preQ1 for tRNA queuosine. |
| Riboflavin synthesis | `ribA`, `ribAB-I`, `ribAB-II` | Make riboflavin precursors. |
| Pterin-dependent phenylalanine hydroxylation | `phhA`, `phhB` | Mature enzyme and pterin-recycling functions, not MoCo construction. |
| Sulfur and molybdate inputs | IscS/TusA-like sulfur relay proteins; molybdate transporters | External inputs to the bounded module. |
| Molybdoenzyme maturation and use | `PP_2480`, `PP_4231`, neighboring oxidoreductase subunits, and other mature Mo enzymes | Client-specific cofactor insertion or catalysis downstream of MGD/MCD formation. |

## Evidence Assessment

Final-module generic and PSEPK pathway OpenScientist runs are still in progress.
Only reports with completed provider files and artifacts will be cited as
complete. The stale report generated from the earlier human-oriented seed is not
accepted as evidence and will be replaced before publication.

The local sequence analysis shows that PP_2482 and PP_1969 retain radical-SAM
motifs but are only 36-38% identical to canonical Q88E69 and lack its two
MoaA-specific InterPro records. Pairwise identity alone also fails to distinguish
MobA from MocA; PP_2483 and PP_4230 are therefore assigned as predicted MocA
proteins from concordant K07141, PTHR43777:SF1, and neighborhood evidence, not
from global sequence identity alone.

The reusable module uses family or ortholog selectors according to the local
resolution of each role and exposes the curated KT2440 UniProt proteins as
concrete representatives. Q88K11, Q88LG4, Q88L15, and Q88E67 are recorded in
knowledge gaps rather than forced into canonical MoaA or catalytic MoaB roles;
Q88K10 and Q88F68 are shown as predicted, not experimentally demonstrated,
MocA representatives.

The MPT-synthesis leaf represents the required GO:1990140 MoaD2-MoaE2
heterotetramer as a protein complex with two visible MoaE catalytic units and
two visible MoaD sulfur-carrier units. MoeB-dependent MoaD activation remains a
separate preceding reaction rather than being folded into the synthase complex.

## Formal Expansion QA

The order-4 nucleotide-maturation part is explicitly `optional: true`; the
module compiler does not infer an empty branch from a nested `ZERO_OR_MORE`
variant set alone. A module-specific `compile_module_file` + `enumerate_routes`
assertion passes with six routes: two MGD routes, two MCD routes, and two routes
with neither `mobA_mgd_synthesis` nor `mocA_mcd_synthesis`. Both no-dinucleotide
routes retain the complete upstream sequence through
`moeA_molybdotransferase`, demonstrating a valid Mo-MPT-only realization.

## Artifacts

- Generic research: `modules/molybdenum_cofactor_biosynthesis-deep-research-openscientist.md`
- PSEPK pathway research: `projects/P_PUTIDA/deep-research/PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist.md`
- Sequence analysis: `genes/PSEPK/moaA/moaA-bioinformatics/RESULTS.md`
- PANTHER evidence: `PTHR22960`, `PTHR33359`, `PTHR23404`, `PTHR10953`, `PTHR10192`, `PTHR43232`, `PTHR43764`, `PTHR19136`, and `PTHR43777`

Generated UTC: 2026-07-20
