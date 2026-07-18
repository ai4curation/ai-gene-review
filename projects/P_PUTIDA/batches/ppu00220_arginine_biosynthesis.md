---
title: "PSEPK ppu00220 arginine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [argA, argB, argC1, argC2, aruC, argD, argE, argF, argG, argH, argJ, PP_3571]
autolink_gene_symbols: false
---

# PSEPK ppu00220: arginine biosynthesis

This batch curates the acetylated-ornithine route from L-glutamate to
L-arginine. The reusable model is `modules/arginine_biosynthesis.yaml`; the
raw KEGG-derived membership table is
[`ppu00220_arginine_biosynthesis.tsv`](ppu00220_arginine_biosynthesis.tsv).

## Scope and status

- Eight ordered reaction parts are modeled.
- Ten PSEPK genes provide the preferred implementations of those parts.
- `argD/PP_4481` and `PP_3571` are boundary/conflict reviews and are not counted
  as preferred module exemplars.
- `argD/PP_4481` was absent from the KEGG-derived candidate set. Gene-level
  review shows why: despite its UniProt ArgD name, it is embedded in the AST
  catabolic operon and belongs to the AstC-like PANTHER SF113 branch.
- Carbamoyl-phosphate production is treated as shared substrate supply rather
  than a core part of this pathway module.

## Reaction-to-gene assignment

| Part | Reaction role | PSEPK implementation | UniProt | Curation status |
|---|---|---|---|---|
| 1 | L-glutamate acetylation | `argA/PP_5185` | `P0A0Z9` | Curated; dedicated ArgA route |
| 1 | L-glutamate acetylation | `argJ/PP_1346` | `P59612` | Curated; bifunctional ArgJ alternative |
| 2 | Acetylglutamate kinase | `argB/PP_5289` | `P59300` | Curated |
| 3 | Acetylglutamyl-phosphate reductase | `argC1/PP_0432` | `Q88QQ6` | Curated; type 1 family |
| 3 | Acetylglutamyl-phosphate reductase | `argC2/PP_3633` | `P59308` | Curated; type 2 family |
| 4 | Acetylornithine aminotransferase | `aruC/PP_0372` | `Q88QW2` | Curated; inferred anabolic ArgD-like SF79/K00821 candidate |
| 5 | Ornithine release by transacetylation | `argJ/PP_1346` | `P59612` | Curated; cyclic implementation |
| 5 | Ornithine release by deacetylation | `argE/PP_5186` | `Q88CJ5` | Curated; linear implementation, individual mutant prototrophic |
| 6 | Ornithine carbamoyltransferase | `argF/PP_1079` | `Q88NX4` | Curated; anabolic family |
| 7 | Argininosuccinate synthase | `argG/PP_1088` | `P59604` | Curated and updated |
| 8 | Argininosuccinate lyase | `argH/PP_0184` | `P59618` | Curated |

The module uses `ONE_OR_MORE` variant sets for parts 1, 3, and 5. The presence
of multiple valid genes does not establish condition-specific flux or genetic
redundancy. In particular, current evidence does not justify claiming that
KT2440 uses ArgJ rather than ArgA/ArgE as its dominant route.

## Boundary and uncertain candidates

`argD/PP_4481` is a high-confidence acyl-ornithine aminotransferase but not the
preferred biosynthetic exemplar. It lies directly beside `astA-I`, `astA-II`,
`astB`, and `astD`, and PANTHER places it with characterized AstC/AruC
succinylornithine transaminases. Its review therefore proposes
succinylornithine:2-oxoglutarate transaminase activity and L-arginine catabolism
as the core function/process while retaining acetylornithine transamination as
a plausible non-core activity. Direct KT2440 genetics identifies the tested
insertion as `argD (= astC [PP_4481])`; the mutant remains arginine prototrophic,
which the authors attribute to a compensating transaminase (PMID:31451546).

`PP_3571/Q88GZ4` belongs to the same broad M20/ArgE-like space as
acetylornithine deacetylases, but its family signals conflict: NCBIfam
`TIGR01892` supports an ArgE-like enzyme. PANTHER
`PTHR43808:SF31` displays an N-acetyl-L-citrulline-deacetylase label, but the
same branch contains many reviewed DapE succinyldiaminopimelate
desuccinylases, so that label is not substrate-discriminating. Its genomic
neighborhood is not an arginine-biosynthesis cluster. Until substrate
specificity is resolved, it is not an exemplar for part 5 and does not satisfy
a pathway requirement.

## Boundary decisions

| Bucket | Genes or activities | Decision |
|---|---|---|
| Shared substrate supply | `carA/PP_4724`, `carB/PP_4723` | Outside core; carbamoyl phosphate also supplies pyrimidine synthesis |
| Arginine deiminase catabolism | `arcA`, `arcB`, `arcC` | Excluded; ArcB is not the anabolic ArgF implementation |
| Arginine succinyltransferase catabolism | `astA-I`, `astA-II`, `astB`, `astD`, `argD/PP_4481` | Excluded from core; PP_4481 is the AstC-like transaminase despite its UniProt gene name |
| Urea utilization | `ureA`, `ureB`, `ureC` | Excluded |
| General nitrogen/glutamate metabolism | `glnA`, `gdhA`, `gdhB`, PP_3148, PP_4399, PP_4547 | Excluded |
| Polyamine and other map spillover | `puuA-I`, `puuA-II`, `spuB`, `spuI`, `alaA`, `ansB` | Excluded |

## Research interpretation

The OpenScientist module/pathway/taxon retrieval correctly distinguished
anabolic ArgF from catabolic ArcB, identified the KEGG overview-map spillover,
and recovered the eight-step pathway outline. It nevertheless promoted
`argD/PP_4481` as a biosynthetic step-4 contributor and described several
coexisting enzymes as redundant without incorporating the direct KT2440 mutant
study. Gene-level review plus local operon and PANTHER evidence instead retain
PP_4481 as the AstC-like catabolic enzyme with plausible non-core ACOAT activity
and use `aruC/PP_0372` as the preferred SF79 biosynthetic candidate.

Claims that the cyclic ArgJ route is dominant or that ArgE is merely a backup
are likewise not encoded as requirements. The KT2440 study found that
individual `argE` and `argJ` mutants remain arginine prototrophs, whereas an
`argA` mutant is auxotrophic. This supports alternative ornithine-release
implementations but does not establish interchangeable pathway initiation or
condition-specific flux (PMID:31451546).

## Validation

- All 12 selected gene reviews pass `just validate PSEPK <gene>`. `PP_3571`
  has the expected advisory warning that no core function is asserted while
  its physiological substrate remains unresolved.
- The module passes LinkML validation. The module validator reports only the
  expected unresolved-prefix warnings for `NCBIfam` and `InterPro`; PAINT
  ancestry and all GO term labels validate.
- Ten focused tests for provider-aware extraction and OpenScientist timeout
  propagation pass, and all touched Python files pass Ruff.
- Repository-wide validation reports 3,694/3,694 gene reviews valid with zero
  errors, and all 53 pathway files containing PMID references pass.
- The module, all selected gene reviews, this batch page, and the parent project
  page render successfully.

## Workflow

- [x] Partition the KEGG-derived candidates into core, shared, catabolic, and uncertain buckets.
- [x] Fetch the selected PSEPK UniProt and GOA records.
- [x] Create the reusable eight-part module with leaf-level molecular functions.
- [x] Run module/pathway/taxon OpenScientist research.
- [x] Complete gene-level OpenScientist retrieval for all selected genes.
- [x] Finish `aruC` research integration and final annotation review.
- [x] Integrate research evidence and render all gene reviews.
- [x] Run scoped and repository-wide validation.
- [ ] Commit, push, and open one draft PR for this module.
