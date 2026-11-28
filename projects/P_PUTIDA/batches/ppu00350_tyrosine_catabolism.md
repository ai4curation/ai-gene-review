---
title: "PSEPK ppu00350 L-tyrosine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [tyrB, amaC, hpd, hmgA, hmgC, hmgB]
autolink_gene_symbols: false
---

# PSEPK ppu00350: L-tyrosine catabolism

- Module: `tyrosine_catabolism`
- Pathway context: KEGG `ppu00350` (tyrosine metabolism)
- Focused genes: 6
- Broad membership-table candidates: 16

## Boundary

This batch covers the five reactions from L-tyrosine to fumarate and
acetoacetate:

1. `tyrB`/`amaC`: paralog-supported L-tyrosine transamination to
   4-hydroxyphenylpyruvate
2. `hpd`: oxidative formation of homogentisate
3. `hmgA`: aromatic-ring cleavage to maleylacetoacetate
4. `hmgC`: isomerization to fumarylacetoacetate
5. `hmgB`: terminal hydrolysis to fumarate and acetoacetate

The lower HmgA/HmgC/HmgB route can also receive homogentisate from
phenylalanine and aromatic-compound pathways. Those separate entry reactions,
DOPA metabolism, and unrelated aldehyde/semialdehyde dehydrogenases in the
broad KEGG bucket are outside this module.

## Status

- [x] Confirm that all six focused gene reviews are already curated.
- [x] Revise the reusable module from human hepatic framing to cross-species biochemistry.
- [x] Add exact PSEPK exemplars to every reaction leaf.
- [x] Remove module-level cytosol and disease/drug-specific role descriptions.
- [x] Complete generic module-level OpenScientist research.
- [x] Complete module + `ppu00350` + PSEPK OpenScientist research.
- [x] Validate and render the revised module.
- [x] Revalidate and render the six focused gene reviews.
- [x] Render the batch page and refresh its inventory.
- [x] Open one PR for this module.
- [ ] Shepherd the revised PR through review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | Existing review evidence |
|---|---|---|---|---|
| `tyrB` | PP_1972 | Q88LG1 | tyrosine aminotransferase | Falcon and Asta reports; curated exact MF and PLP context |
| `amaC` | PP_3590 | Q88GX7 | paralogous tyrosine aminotransferase | Curated KT2440 RB-TnSeq/validation evidence plus exact PTHR11879:SF37 assignment |
| `hpd` | PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase | Falcon report and organism-specific growth evidence |
| `hmgA` | PP_4621 | Q88E47 | homogentisate 1,2-dioxygenase | Reviewed UniProt plus Falcon and OpenScientist reports |
| `hmgC` | PP_4619 | Q88E49 | maleylacetoacetate isomerase | OpenScientist report and exact GST-zeta family assignment |
| `hmgB` | PP_4620 | Q88E48 | fumarylacetoacetase | OpenScientist report and exact terminal-pathway assignment |

## Excluded Bucket Members

The broad KEGG list includes DavD, succinate-semialdehyde dehydrogenases,
phenylacetaldehyde dehydrogenase, DOPA decarboxylase, tryptophan
2-monooxygenase, and generic aminotransferase/dehydrogenase candidates. Their
membership reflects other branches of the tyrosine map, not missing reactions
in the five-step route curated here. PP_1709 is a shorter FAH-superfamily
protein with no exact EC assignment; it is not substituted for the
pathway-linked, EC 3.7.1.2 HmgB without substrate-specific evidence.

The species-aware report classifies steps 2-5 as covered and identifies the
entry reaction as paralog-supported. Its claim that the entry assignment is
only rule-based is superseded here by the existing AmaC review's direct KT2440
RB-TnSeq/validation evidence. The report is retained for its pathway-wide
satisfiability and excluded-candidate analysis:
[`PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist.md`](../deep-research/PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist.md).

The complete candidate inventory is retained in
[`ppu00350_tyrosine_catabolism.tsv`](ppu00350_tyrosine_catabolism.tsv).
