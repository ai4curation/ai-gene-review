---
title: "PSEPK ppu00770 Pantothenate and CoA biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00770: Pantothenate and CoA biosynthesis

This batch tests pantothenate formation and the five-reaction conversion of
pantothenate to coenzyme A in *Pseudomonas putida* KT2440. The reusable module
is [Pantothenate and coenzyme A biosynthesis](../../../modules/coenzyme_a_biosynthesis.html).

The generated membership table contains 24 candidates because KEGG ppu00770
overlaps branched-chain-amino-acid synthesis, beta-alanine production,
phosphopantetheinylation, and nucleotide metabolism. Seven KT2440 genes satisfy
the eight reactions in the curated module; one fused `dfp/coaBC` protein
performs two consecutive reactions. Five additional genes were promoted to
review to resolve false-positive or peripheral pathway assignments.

## Workflow Status

- [x] Fetch all 12 selected genes and their GOA annotations.
- [x] Complete species-aware module + pathway + taxon OpenScientist research.
- [x] Rewrite the reusable module as a species-neutral eight-reaction pathway.
- [x] Ground family variants with exact UniProt exemplars and verified PAINT nodes.
- [ ] Complete generic module OpenScientist research.
- [x] Complete all 12 gene-level OpenScientist reports.
- [x] Curate and validate all 12 selected gene reviews.
- [ ] Render the module, genes, and project pages.
- [ ] Open and shepherd one pull request for this module.

## Pathway Satisfiability

| Order | Reaction | KT2440 implementation | Review status | Decision |
|---|---|---|---|---|
| 1 | 3-methyl-2-oxobutanoate to 2-dehydropantoate | `panB` / PP_4699 / Q88DW9 | Curated | covered |
| 2 | 2-dehydropantoate to (R)-pantoate | `panE` / PP_1351 / Q88N64 | Curated | covered by canonical PanE |
| 3 | Pantoate + beta-alanine to pantothenate | `panC` / PP_4700 / Q88DW8 | Curated | covered |
| 4 | Pantothenate to 4'-phosphopantothenate | `coaX` / PP_0438 / Q88QQ0 | Curated | covered by type III PanK |
| 5 | Phosphopantothenate + cysteine to PPC | `dfp` / PP_5285 / Q88C96, CoaB region | Curated | covered by fused CoaBC |
| 6 | PPC to 4'-phosphopantetheine | `dfp` / PP_5285 / Q88C96, CoaC region | Curated | covered by fused CoaBC |
| 7 | 4'-phosphopantetheine to dephospho-CoA | `coaD` / PP_5123 / Q88CQ7 | Curated | covered by standalone PPAT |
| 8 | Dephospho-CoA to CoA | `coaE` / PP_0631 / Q88Q65 | Curated | covered by standalone DPCK |

**Module result: `covered`.** KT2440 uses the bacterial CoaX + fused CoaBC +
standalone CoaD/CoaE architecture. A human-only PANK/PPCS/PPCDC/COASY model
would create artificial gaps.

Beta-alanine is an input to reaction 3 rather than an invariant module step.
No canonical PanD aspartate decarboxylase was found in KT2440. The encoded
reductive pyrimidine-degradation route (`pydA`, `pydX`, `pydB`, `hyuC`, and
PP_0614) is the leading alternative source, but direct flux attribution remains
a species-level question outside this reusable module.

## Selected Reviews

| Gene | Locus / UniProt | Selection reason | Curation status |
|---|---|---|---|
| `panB` | PP_4699 / Q88DW9 | Core pantoate-arm reaction 1 | Curated and validated |
| `panE` | PP_1351 / Q88N64 | Canonical pantoate-arm reductase | Curated and validated |
| `panC` | PP_4700 / Q88DW8 | Pantothenate-forming reaction | Curated and validated |
| `coaX` | PP_0438 / Q88QQ0 | Type III pantothenate kinase | Curated and validated |
| `dfp` | PP_5285 / Q88C96 | Fused CoaB + CoaC reactions | Curated and validated |
| `coaD` | PP_5123 / Q88CQ7 | Standalone PPAT | Curated and validated |
| `coaE` | PP_0631 / Q88Q65 | Standalone DPCK | Curated and validated |
| `PP_2325` | PP_2325 / Q88KG5 | KPR-related paralog and false-positive pathway call | Curated and validated |
| `PP_2998` | PP_2998 / Q88IK1 | KPR-related paralog with unresolved specificity | Curated and validated |
| `PP_4452` | PP_4452 / Q88EL0 | Extra UniPathway KPR false positive; opine-DH family | Curated and validated |
| `PP_0922` | PP_0922 / Q88PC8 | ACP phosphodiesterase pulled into ppu00770 | Curated and validated |
| `mazG` | PP_1657 / Q88MB7 | Nucleotide pyrophosphohydrolase pulled into ppu00770 | Curated and validated |

## Candidate Partition

| Bucket | Genes | Treatment |
|---|---|---|
| Core module | `panB`, `panE`, `panC`, `coaX`, `dfp`, `coaD`, `coaE` | Included as exact KT2440 implementations of the eight reusable reactions |
| KPR annotation diagnostics | `PP_2325`, `PP_2998`, plus extra `PP_4452` | Reviewed separately; not interchangeable module copies of canonical PanE |
| Beta-alanine supply | `PP_0614`, `hyuC`, `pydB`, `pydX`, `pydA` | Upstream alternative route; not a fixed module part |
| Branched-chain precursor metabolism | `PP_1157`, `PP_1394`, `ilvC`, `ilvD`, `ilvE`, `ilvH`, `ilvI` | Shared precursor context, not pantothenate/CoA module members |
| CoA utilization | `PP_1183` / EntD | Uses CoA-derived phosphopantetheine downstream; not a biosynthetic step |
| Map spillover reviewed here | `PP_0922`, `mazG` | Curate their actual functions and exclude them from the module |

The machine-generated source table is retained at
[`ppu00770_coenzyme_a_biosynthesis.tsv`](ppu00770_coenzyme_a_biosynthesis.tsv).

## Curation Decisions

- `panE` Q88N64 is the canonical KT2440 ketopantoate reductase and is the only
  PSEPK PanE exemplar in the reusable module.
- `PP_2325` is the reciprocal-best Pseudomonas ortholog of experimentally
  characterized PaKPR2, which is inactive toward ketopantoate. Its electronic
  KPR and pantothenate annotations are removed; a broad oxidoreductase
  annotation is proposed.
- `PP_2998` belongs to the same broad KPR-related family, but current evidence
  does not resolve its substrate. It must not be treated as a second required
  module step.
- The gene-level OpenScientist reports for `PP_2325` and `PP_2998` repeated the
  electronic PanE assignment from distant family similarity and did not
  resolve the closer PaKPR2 evidence. Those hypotheses were evaluated rather
  than imported: `PP_2325` is removed from the pathway, while the less closely
  resolved `PP_2998` annotations remain undecided.
- `PP_4452` is assigned to the opine/lysopine-dehydrogenase family and KEGG
  K04940 in an opine-utilization neighborhood. Its EC 1.1.1.169 and
  pantothenate annotations are removed.
- The InterPro-derived `pantothenate catabolic process` annotation on `dfp` is
  directionally wrong and is removed. Both CoaBC catalytic functions and its
  oligomeric decarboxylase-complex annotation are retained.
- `PP_0922` and `mazG` are peripheral map hits, not missing or optional CoA
  biosynthesis reactions.
- `PP_0922` is a predicted AcpH-family ACP phosphodiesterase. Its molecular
  function is retained, but the generic fatty-acid-biosynthesis process transfer
  is marked over-annotated because ACP prosthetic-group turnover is not itself a
  biosynthetic step and its KT2440 physiology is unresolved.
- `mazG` is a tandem-domain NTP pyrophosphohydrolase in nucleotide-pool
  turnover. The canonical NTP activity is retained, the broad stress-response
  transfer remains undecided, and the ribothymidine `TTP` process is removed as
  a conflation with the separately represented canonical `dTTP` substrate.

## Research

- [Species-aware OpenScientist report](../deep-research/PSEPK__coenzyme_a_biosynthesis__ppu00770-deep-research-openscientist.md)
- Generic module report: `modules/coenzyme_a_biosynthesis-deep-research-openscientist.md`
- Gene-level reports: `genes/PSEPK/<gene>/<gene>-deep-research-openscientist.md`

## Validation

Final validation and rendering results will be recorded here before the pull
request is marked ready for review.
