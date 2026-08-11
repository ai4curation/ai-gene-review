---
title: "PSEPK ppu00620 bacterial pyruvate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [aceE, aceF, lpd, pycA, pycB, ppc, ppsA, pyk, pykA]
autolink_gene_symbols: false
---

# PSEPK ppu00620: bacterial pyruvate metabolism

- Reusable module: `modules/bacterial_pyruvate_metabolism.yaml`
- Broad KEGG ppu00620 candidates inspected: 54
- Focused PSEPK proteins: 9
- Module boundary: pyruvate dehydrogenase, anaplerotic carboxylation, and direct PEP/pyruvate interconversion
- Deep-research provider: OpenScientist; six focused gene reports completed,
  while the generic and species/pathway jobs exhausted their full initial
  allowances without producing reports.

## Workflow

- [x] Inspect the ppu00620 worklist, membership records, existing modules, gene reviews, and related PRs.
- [x] Keep the existing human mitochondrial `modules/pyruvate_metabolism.yaml` unchanged.
- [x] Create a species-neutral bacterial module with multiple substantive parts.
- [x] Run module-level OpenScientist research with the full provider timeout; no report was returned before timeout.
- [x] Run module + ppu00620 + PSEPK OpenScientist research with the full provider timeout; no report was returned before timeout.
- [x] Reuse six complete OpenScientist gene reports; attempted missing reports with full timeouts and stopped non-gating retries before publication.
- [x] Audit all nine focused gene reviews as the annotation-reviewer consultant.
- [x] Edit only annotation review sections where action semantics required correction.
- [x] Validate and render the module, project page, and touched gene reviews.
- [x] Open one draft PR for this module/pathway: [PR #2519](https://github.com/ai4curation/ai-gene-review/pull/2519).
- [ ] Shepherd review and CI.

## Satisfiability

| Module part | PSEPK implementation | UniProt | Decision |
|---|---|---|---|
| Pyruvate dehydrogenase E1 | `aceE` / PP_0339 | Q88QZ5 | Covered by GO:0004739, RHEA:19189, and PTHR43825:SF3 |
| Pyruvate dehydrogenase E2 | `aceF` / PP_0338 | Q88QZ6 | Covered by GO:0004742, RHEA:17017, and PTHR43178:SF2 |
| Pyruvate dehydrogenase E3 | `lpd` / PP_5366 | Q88C17 | Covered by GO:0004148, RHEA:15045, and PTHR22912:SF151 |
| Two-subunit pyruvate carboxylase, biotin carboxylase half | `pycA` / PP_5347 | Q88C36 | Covered by GO:0004075, RHEA:13501, and PTHR48095:SF1 |
| Two-subunit pyruvate carboxylase, carrier/carboxyltransferase half | `pycB` / PP_5346 | Q88C37 | Covered by GO:0004736, RHEA:20844, and PTHR43778 |
| PEP carboxylase anaplerosis | `ppc` / PP_1505 | Q88MR4 | Covered by GO:0008964, RHEA:28370, and PTHR30523:SF6 |
| PEP-to-pyruvate conversion | `pykA` / PP_1362; `pyk` / PP_4301 | Q88N54; Q88EZ9 | Two pyruvate-kinase exemplars covered by GO:0004743, RHEA:18157, and PTHR11817 |
| Pyruvate-to-PEP conversion | `ppsA` / PP_2082 | Q88L53 | Covered by GO:0008986, RHEA:11364, and PTHR43030:SF1 |

The KT2440 instance supports both modeled anaplerotic routes: the split
PycA/PycB pyruvate carboxylase and Ppc phosphoenolpyruvate carboxylase. It also
supports both direct PEP/pyruvate directions through two pyruvate kinases and
PpsA. These are reusable bacterial branchpoint roles, not a claim that every
bacterium encodes every leaf.

## Annotation Audit

All existing annotations in the nine focused PSEPK reviews were inspected
against the local UniProt/GOA records, completed gene research, and the
module/pathway synthesis. Exact catalytic terms and appropriate process terms
remain accepted.

- `aceE`, `aceF`, `lpd`, `pycB`, and `ppsA` required no review-section changes.
- `pycA` ATP binding was changed from `ACCEPT` to `KEEP_AS_NON_CORE`; ATP is a substrate of the biotin-carboxylase half-reaction, but GO:0004075 is the core function.
- `ppc` magnesium binding was changed from `ACCEPT` to `KEEP_AS_NON_CORE`; metal dependence is valid supporting chemistry, not the defining activity.
- `pyk` and `pykA` magnesium and potassium binding were changed from `ACCEPT` to `KEEP_AS_NON_CORE`; GO:0004743 remains the accepted core molecular function.
- Existing removal of sodium transport and oxaloacetate decarboxylase from `pycB` remains appropriate because those are over-propagated OadA-family inferences for the carboxylase beta subunit.

## Boundary Decisions

- The root represents direct bacterial pyruvate-node chemistry. It does not duplicate the existing mitochondrial PDC/PC module.
- Lipoylation and cofactor biosynthesis are prerequisites, not pyruvate-metabolism parts.
- Complete Entner-Doudoroff/glycolytic and gluconeogenic trunks remain in their existing modules; only the direct PEP/pyruvate branchpoint reactions are represented here.
- Citrate-cycle, glyoxylate-shunt, malate-dehydrogenase, malate-quinone-oxidoreductase, fumarase, and CoA-transferase rows are downstream or adjacent central-carbon map spillover.
- `maeB` and PP_1389 provide opposing C4-to-pyruvate chemistry, but are not required to define the oxidative and anaplerotic core; their physiological weighting belongs in a dedicated cataplerotic-node treatment.
- `ldhA`, `lldD`, and `dld2` belong to stereospecific lactate production or utilization modules rather than the reusable core defined here.
- `pta`, `acsA1`, and `acsA2` belong to acetate overflow/utilization; acetyl-CoA is shared output/input, not evidence that these enzymes are part of pyruvate dehydrogenation.
- `gloA` and `gloB` are already curated in `methylglyoxal_detoxification`; the shared KEGG accession does not make that detoxification route part of this module.
- Acetoin cleavage, fatty-acid synthesis, thiolases, alcohol/aldehyde oxidation, amino-acid metabolism, and uncharacterized hydrolases are excluded as unrelated map spillover.

## Modeling

The module has three substantive root parts. GO molecular functions are placed
only on terminal annotons. Exact PSEPK UniProt proteins are representative
members on those leaves, not module-level participants. The reusable
description is species-neutral, and no generic cytoplasm/cytosol location is
asserted.

## Research Status

Complete OpenScientist gene reports are present for `aceE`, `aceF`, `lpd`,
`pycA`, `pycB`, and `pykA`. The initial generic module and
module+ppu00620+PSEPK jobs each ran for the full 7200-second provider allowance
and timed out without generating files. Initial `ppc` and `pyk` jobs also timed
out; the first `ppsA` job ended when the provider status endpoint returned HTTP
522. Three-iteration recovery jobs were started according to project policy and
then stopped when provider completion was made non-gating for publication. The
curation therefore relies on verified local UniProt, GOA, Rhea, PANTHER, prior
completed gene research, and existing central-carbon module work rather than
citing nonexistent provider output.

## Validation

The final PR records the exact validation and rendering commands after all
OpenScientist outputs have completed.
