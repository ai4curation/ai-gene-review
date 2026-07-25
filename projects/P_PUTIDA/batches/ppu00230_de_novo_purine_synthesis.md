---
title: "PSEPK de novo inosine monophosphate biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [purF, purD, purN, purT, purL, purM, purK, purE, purC, purB, purH]
autolink_gene_symbols: false
---

# PSEPK de novo inosine monophosphate biosynthesis

This batch narrows the 65-member KEGG `ppu00230` purine-metabolism map to the
eleven proteins that satisfy the ten ordered reactions from PRPP to IMP.
The reusable module models reaction roles independently of protein fusion
architecture, includes the PurN and PurT alternatives for GAR formylation, and
distinguishes the bacterial PurK/PurE N5-CAIR route from direct AIR
carboxylation.

## Workflow

- [x] Fetch the eleven selected gene records.
- [ ] Run full OpenScientist research for every selected gene.
- [x] Curate every GOA row in the selected gene reviews.
- [x] Revise and validate the species-neutral `de_novo_purine_synthesis` module.
- [ ] Run full OpenScientist module research.
- [ ] Run full OpenScientist module + `ppu00230` + PSEPK research.
- [ ] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `purF` | PP_2000 | Q88LD5 | Committed phosphoribosylamine formation |
| [x] | `purD` | PP_4823 | Q88DK2 | GAR synthetase |
| [x] | `purN` | PP_1664 | Q88MB0 | Folate-dependent GAR transformylase variant |
| [x] | `purT` | PP_1457 | Q88MW1 | ATP/formate-dependent GAR transformylase variant |
| [x] | `purL` | PP_1037 | Q88P16 | Large-type FGAM synthase |
| [x] | `purM` | PP_1665 | Q88MA9 | AIR synthetase |
| [x] | `purK` | PP_5335 | Q88C48 | N5-CAIR synthetase |
| [x] | `purE` | PP_5336 | Q88C47 | N5-CAIR mutase |
| [x] | `purC` | PP_1240 | Q88NG9 | SAICAR synthetase |
| [x] | `purB` | PP_4016 | Q88FR7 | SAICAR lyase; also acts in the AMP branch |
| [x] | `purH` | PP_4822 | Q88DK3 | AICAR transformylase and IMP cyclohydrolase |

## Curation Decisions

- `purM` loses the incorrect PurD ligase annotation transferred from a
  eukaryotic trifunctional PANTHER context; its AIR synthetase activity is
  retained.
- `purC` loses an unsupported cobalamin-process annotation propagated from a
  broad family mapping.
- `purK` retains its specific N5-CAIR synthetase term; the broad direct
  AIR-carboxylase term is treated as redundant for this half of the bacterial
  two-enzyme route.
- Both GAR transformylases remain in the pathway because they implement
  distinct one-carbon donor chemistries at the same reaction position.
- Parent catalytic, binding, and broad purine-process terms are not duplicated
  in core functions when an enzyme-specific activity and
  `GO:0006189` are available.

## Excluded Candidate Groups

The remaining KEGG hits belong to IMP branch synthesis, purine salvage,
nucleotide interconversion, purine catabolism, alarmone metabolism,
phosphoribosyl-pyrophosphate supply, DNA precursor synthesis, urease, or broad
adenylate-dependent metabolism. They remain in the immutable 65-gene source
snapshot `ppu00230_de_novo_purine_synthesis.tsv` but are outside the
PRPP-to-IMP module boundary.
