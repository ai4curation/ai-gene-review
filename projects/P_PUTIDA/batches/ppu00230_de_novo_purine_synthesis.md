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
- [x] Attempt full OpenScientist research for every selected gene. Reports completed
  for `purF`, `purD`, `purN`, and `purC`; the remaining requests exhausted their
  configured provider windows without reports.
- [x] Curate every GOA row in the selected gene reviews.
- [x] Revise and validate the species-neutral `de_novo_purine_synthesis` module.
- [x] Run full OpenScientist module research.
- [x] Attempt full OpenScientist module + `ppu00230` + PSEPK research; the
  corrected request exhausted the 7,200-second provider timeout without a
  report.
- [x] Render the module and project page.
- [x] Open one non-draft PR for this module:
  [#2239](https://github.com/ai4curation/ai-gene-review/pull/2239).
- [ ] Shepherd the PR through review and CI.

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
- `purK` retains its specific N5-CAIR synthetase term; the direct
  AIR-carboxylase annotation is modified to that specific activity because
  bacterial PurK supplies N5-CAIR for the separate PurE reaction.
- Both GAR transformylases remain in the pathway because they implement
  distinct one-carbon donor chemistries at the same reaction position.
- Generic catalytic parents and valid broad purine-nucleotide process
  annotations are modified to enzyme-specific activities and `GO:0006189`.
  Purine nucleobase-process annotations are marked over-annotated because IMP
  is a nucleotide, while valid ATP, nucleotide, magnesium, and metal-binding
  annotations are retained as non-core. PurF's L-glutamine metabolic-process
  annotation is also retained as non-core because it describes a consumed
  substrate rather than the enzyme's de novo purine-pathway role.
- Human PPAT, GART, PFAS, PAICS, ADSL, and ATIC reviews and exact UniProt
  exemplars ground the eukaryotic fusion architectures alongside the bacterial
  proteins. Primary studies ground the PurN/PurT and PurK/PurE alternative
  routes.
- Cytosolic localization remains in the target gene reviews rather than the
  reusable module. Localization is not a defining reaction requirement, and a
  module-level location would conflate bacterial cytoplasm/cytosol conventions
  with lineage-specific eukaryotic organization.

## Excluded Candidate Groups

The remaining KEGG hits belong to IMP branch synthesis, purine salvage,
nucleotide interconversion, purine catabolism, alarmone metabolism,
phosphoribosyl-pyrophosphate supply, DNA precursor synthesis, urease, or broad
adenylate-dependent metabolism. They remain in the immutable 65-gene source
snapshot `ppu00230_de_novo_purine_synthesis.tsv` but are outside the
PRPP-to-IMP module boundary.

The species-aware OpenScientist request was allowed the full configured 7,200
seconds with three iterations and returned no report. The module therefore
cites the completed generic report and inspectable gene, exact-record, and
ontology evidence, not a nonexistent taxon-specific source.

Gene-level OpenScientist reports completed for `purF`, `purD`, `purN`, and
`purC`. The corrected `purL`, `purT`, `purB`, and `purH` requests each exhausted
the full 7,200-second provider timeout; the `purM`, `purK`, and `purE` attempts
also returned no report. These retrieval outcomes do not create pathway holes:
all eleven target assignments were adjudicated against exact UniProt records,
domain/family evidence, the completed generic module research, and the
available primary literature.

## 2026-09-01 Fusion and family repair

Repair PR: [#2865](https://github.com/ai4curation/ai-gene-review/pull/2865).

The human GART fusion P22102 is classified as
PANTHER:PTHR10520:SF12 at the whole-protein level. The PurD and PurN leaves
retain GART as an exact fusion exemplar, while the reviewed record's N-terminal
ATP-grasp and C-terminal transformylase domain assignments establish those leaf
activities without using the whole-protein subfamily as their selector. The
PurM leaf now uses PTHR10520:SF12 because it contains both standalone bacterial
PurM proteins and the GART fusion; the exact leaf function constrains the
selector to their shared cyclo-ligase role. Human ADSL P30566 is now
represented by its exact eukaryotic PTHR43172:SF1 family alongside the distinct
bacterial PTHR43411 PurB family. These repairs preserve ten ordered reaction
positions and do not treat a fusion as a one-step module.
The same audit moved purely electronic cytosol or cytoplasm annotations to
non-core in `purN`, `purT`, `purL`, `purM`, `purK`, `purC`, `purB`, and `purH`,
and removed those locations from synthesized core functions. The coexisting
broad cytoplasm and narrower cytosol rows in `purN` and `purM` are both retained
as plausible electronic localizations, but neither is treated as core.
