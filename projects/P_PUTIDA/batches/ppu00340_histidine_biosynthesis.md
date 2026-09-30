---
title: "PSEPK ppu00340 Histidine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00340: L-histidine biosynthesis

- Reusable module: `modules/histidine_biosynthesis.yaml`
- KEGG ppu00340 candidates inspected: 20
- Biosynthetic candidates: 12 proteins covering 9 ordered reactions
- Histidinol-phosphate phosphatase implementations: 2 unrelated families
- KEGG-map spillover excluded from this module: 8
- Gene-level provider: OpenScientist
- Module and PSEPK satisfiability provider: OpenScientist

## Workflow

- [x] Define a multi-step, species-neutral module boundary.
- [x] Separate biosynthesis from Hut histidine catabolism and unrelated map spillover.
- [x] Fetch the selected PSEPK genes.
- [x] Review every GOA annotation for the selected genes.
- [x] Complete the OpenScientist evidence pass, recording provider timeouts and cross-report support.
- [x] Validate module and gene reviews.
- [x] Render module, gene, and project pages.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Satisfiability

| Order | Reaction or role | PSEPK gene(s) | UniProt | Decision |
|---|---|---|---|---|
| 1 | ATP phosphoribosyltransferase, short-form catalytic and regulatory subunits | `hisG`, `hisZ` | Q88P87, Q88DD7 | Covered by the short-form architecture variant; reusable module also models long-form HisG |
| 2 | Phosphoribosyl-ATP diphosphatase | `hisE` | Q88D14 | Covered; activity was mislabeled as HisI in the old module |
| 3 | Phosphoribosyl-AMP cyclohydrolase | `hisI` | Q88D15 | Covered; ARBA diphosphatase co-annotation removed |
| 4 | ProFAR isomerase | `hisA` | Q88R42 | Covered; TreeGrafter tryptophan-process annotation removed because KT2440 has separate TrpF |
| 5 | Imidazole-glycerol-phosphate synthase | `hisF`, `hisH` | Q88R41, Q88R44 | Covered as a two-subunit coupled activity |
| 6 | Imidazoleglycerol-phosphate dehydratase | `hisB` | Q88R45 | Covered by monofunctional IGPD |
| 7 | Histidinol-phosphate aminotransferase | `hisC` | Q88P86 | Covered |
| 8 | Histidinol-phosphate phosphatase | `PP_3157`, `PP_5147` | Q88I44, Q88CN3 | Two unrelated candidates; neither exact KT2440 activity is established, so both gene-level decisions are `UNDECIDED` |
| 9 | Histidinol dehydrogenase | `hisD` | P59400 | Covered; performs both terminal oxidations |

The pathway is candidate-level satisfiable in KT2440, but the exact protein or
proteins carrying step 8 remain unresolved. PRPP production is shared upstream
metabolism and is not modeled as a required histidine-specific part.

## Phosphatase Redundancy

`PP_3157` (Q88I44) is an exact member of the experimentally defined IMPase-like
HisN family, while `PP_5147` (Q88CN3) is a HAD-family candidate related to the
experimentally validated Pseudomonas aeruginosa enzyme PA0335. The module
therefore models the reaction as an enzyme-family variant set with `ONE_OR_MORE`
selection, but treats both PSEPK proteins as candidates rather than active
exemplars. `TIGR01490` is omitted because its official `HAD-SF-IB-hyp1` scope
does not establish histidinol-phosphate specificity. Direct KT2440 genetics and
substrate-specific assays are needed to identify the physiological enzyme or
enzymes.

## Excluded Candidates

| Gene | Reason outside the module boundary |
|---|---|
| `gshA` | Glutathione biosynthesis; broad KEGG histidine-metabolism map overlap |
| `PP_1721` | Predicted phosphoserine phosphatase without histidine-specific support |
| `PP_4983` / `iaaM` | Tryptophan 2-monooxygenase in auxin/tryptophan metabolism |
| `hutH`, `hutU`, `hutI`, `hutG`, `hutF` | Histidine utilization/catabolism, to be curated as a separate Hut module |

## Module Decisions

- The reusable module starts at the first committed HisG reaction and contains
  nine ordered reaction parts; it is not a wrapper around a single enzyme.
- Molecular functions are attached to leaf annotons, not to the biological-
  process module node.
- The generic module uses activity-based names for reactions whose HisE/HisI
  symbols vary across taxa.
- The first reaction uses an `EXACTLY_ONE` architecture variant set: short-form
  HisG plus HisZ, exemplified by PSEPK, or a long-form single-chain HisG.
- Every PSEPK-selected leaf has a concrete PSEPK UniProt candidate. HisZ is
  confined to the short-form architecture and is not required by long-form
  ATPPRT enzymes.
- The phosphatase leaf is an explicit enzyme-family variant set. It also uses
  reviewed Pseudomonas aeruginosa PA0335 (UniProtKB:Q9I6F6) as the direct
  experimental exemplar for the HAD-family implementation.
- No redundant cytoplasm/cytosol pair is asserted at module level.

## Research Status

The module/pathway/taxon OpenScientist report supports the pathway boundary and
ordered activities. PA0335 is genetically and biochemically validated as a
monofunctional HAD-family histidinol-phosphate phosphatase, but the cached
primary evidence does not establish Q88CN3 orthology or substrate specificity.
The PSEPK phosphatase step therefore remains a documented satisfiability gap
between two credible candidates rather than a resolved assignment.

The first gene-level OpenScientist submissions inherited the wrapper's
600-second default and timed out before the provider's normal completion
window. Full runs use `--timeout 7200`; failures are recorded as provider
status rather than replaced by hand-written provider files. The retried
target-specific `hisE` job reached OpenScientist's own 3,600-second ceiling;
the exact HisE identity and reaction are instead cross-supported by the
completed adjacent HisI/HisE report and UniProt/HAMAP evidence. The
target-specific `hisF` job reached the same provider ceiling; HisF's exact
cyclase-partner identity and coupled PRFAR reaction are cross-supported by the
completed HisH/HisF complex report and its exact UniProt record.

## Validation

All 12 selected gene reviews pass `just validate`; the two unresolved
phosphatase reviews carry the expected warning that no core function is
asserted. The module passes LinkML `ModuleReview` validation and the dedicated
module validator. Its only messages are expected namespace-label warnings for
InterPro, Pfam, and NCBIfam selectors, plus confirmation that the uncertain HAD
family ID was omitted. The changed module, gene-review, and project pages render
successfully.
