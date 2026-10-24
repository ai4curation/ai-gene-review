---
title: Forty horse genes for ProtNLM evaluation
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Forty horse genes for ProtNLM evaluation

**40 selected horse genes with 89 GO predictions and 17 function descriptions.**
The paired reviews evaluate these horse predictions using exact sequence evidence
and characterized mammalian counterparts. The selection is based
on informative functional claims and biological diversity. Every gene has GO or
function-text output; protein-name predictions were not a selection criterion.

[Download the 40-gene list](mammal-benchmark/horse40.csv) ·
[All 106 GO/function outputs](mammal-benchmark/horse40-predictions.csv) ·
[Current protein sequences](mammal-benchmark/horse40-sequences.fasta) ·
[Selection manifest](mammal-benchmark/horse40-manifest.json)

27 genes have GO predictions, 17 have function descriptions, and four have both.
The list includes catalytic/regulatory distinctions, substrate and pathway
specificity, taxonomic context, localization and developmental claims. The focus
column records the review question, not a correctness verdict. Each target is paired
with a human review and evaluated against primary evidence and its exact current
horse sequence. See the [review findings and evidence gaps](horse40-review-findings.md).

| # | Horse review | Human review | Accession | GO | Function text | Review focus |
|---|---|---|---|---:|---:|---|
| 1 | <gene species="HORSE" symbol="VAPA">VAPA</gene> | <gene species="human" symbol="VAPA">VAPA</gene> | [A0A3Q2H1L9](https://rest.uniprot.org/uniprotkb/protnlm/A0A3Q2H1L9) | 0 | 1 | Test sperm-crawling narrative and taxonomic context |
| 2 | <gene species="HORSE" symbol="CAPSL">CAPSL</gene> | <gene species="human" symbol="CAPSL">CAPSL</gene> | [A0A3Q2I3U9](https://rest.uniprot.org/uniprotkb/protnlm/A0A3Q2I3U9) | 0 | 1 | Test venom-secretion narrative |
| 3 | <gene species="HORSE" symbol="MYL10">MYL10</gene> | <gene species="human" symbol="MYL10">MYL10</gene> | [A0A9L0TJE1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0TJE1) | 0 | 1 | Test venom-secretion narrative on a different protein family |
| 4 | <gene species="HORSE" symbol="KRIT1">KRIT1</gene> | <gene species="human" symbol="KRIT1">KRIT1</gene> | [A0A9L0SR44](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SR44) | 0 | 1 | Test piRNA and germline narrative against target identity |
| 5 | <gene species="HORSE" symbol="CTDSP2">CTDSP2</gene> | <gene species="human" symbol="CTDSP2">CTDSP2</gene> | [F7A4N8](https://rest.uniprot.org/uniprotkb/protnlm/F7A4N8) | 1 | 0 | Resolve predicted kinase activity versus target catalytic class |
| 6 | <gene species="HORSE" symbol="PEA15">PEA15</gene> | <gene species="human" symbol="PEA15">PEA15</gene> | [A0A9L0RWM8](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0RWM8) | 1 | 0 | Test carbohydrate-transport process assignment |
| 7 | <gene species="HORSE" symbol="ALDH7A1">ALDH7A1</gene> | <gene species="human" symbol="ALDH7A1">ALDH7A1</gene> | [A0A9L0RRL6](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0RRL6) | 1 | 0 | Resolve precise aldehyde-dehydrogenase substrate specificity |
| 8 | <gene species="HORSE" symbol="GHSR">GHSR</gene> | <gene species="human" symbol="GHSR">GHSR</gene> | [F6QF00](https://rest.uniprot.org/uniprotkb/protnlm/F6QF00) | 0 | 1 | Test oxytocin-receptor narrative and ligand specificity |
| 9 | <gene species="HORSE" symbol="ALG5">ALG5</gene> | <gene species="human" symbol="ALG5">ALG5</gene> | [A0A5F5PM72](https://rest.uniprot.org/uniprotkb/protnlm/A0A5F5PM72) | 0 | 1 | Resolve sugar donor and dolichol-glycosylation reaction |
| 10 | <gene species="HORSE" symbol="HSPD1">HSPD1</gene> | <gene species="human" symbol="HSPD1">HSPD1</gene> | [F6Z587](https://rest.uniprot.org/uniprotkb/protnlm/F6Z587) | 0 | 1 | Distinguish chaperonin complexes and transferred client biology |
| 11 | <gene species="HORSE" symbol="CXCR3">CXCR3</gene> | <gene species="human" symbol="CXCR3">CXCR3</gene> | [A0A9L0T1D1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T1D1) | 0 | 1 | Resolve chemokine ligand class and specificity |
| 12 | <gene species="HORSE" symbol="DARS2">DARS2</gene> | <gene species="human" symbol="DARS2">DARS2</gene> | [A0A9L0SB67](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SB67) | 0 | 1 | Test tRNA-Asn charging and organellar substrate specificity |
| 13 | <gene species="HORSE" symbol="GPAM">GPAM</gene> | <gene species="human" symbol="GPAM">GPAM</gene> | [A0A9L0TTC1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0TTC1) | 0 | 1 | Distinguish acyl-ACP from acyl-CoA donor chemistry |
| 14 | <gene species="HORSE" symbol="HSPA4">HSPA4</gene> | <gene species="human" symbol="HSPA4">HSPA4</gene> | [A0A9L0S5Z5](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0S5Z5) | 0 | 1 | Resolve ribosome-associated chaperone-family and complex transfer |
| 15 | <gene species="HORSE" symbol="DUOX1">DUOX1</gene> | <gene species="human" symbol="DUOX1">DUOX1</gene> | [A0A9L0SQG9](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SQG9) | 4 | 1 | Separate hydrogen peroxide production, catabolism and thyroid context |
| 16 | <gene species="HORSE" symbol="MTMR9">MTMR9</gene> | <gene species="human" symbol="MTMR9">MTMR9</gene> | [A0A9L0T3C1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T3C1) | 7 | 0 | Separate phosphatase regulation and binding from intrinsic catalysis |
| 17 | <gene species="HORSE" symbol="PTPRN2">PTPRN2</gene> | <gene species="human" symbol="PTPRN2">PTPRN2</gene> | [A0A9L0T4W6](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T4W6) | 1 | 0 | Assess dephosphorylation process for a phosphatase-like protein |
| 18 | <gene species="HORSE" symbol="DNMT3L">DNMT3L</gene> | <gene species="human" symbol="DNMT3L">DNMT3L</gene> | [A0A9L0T837](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T837) | 2 | 0 | Compare regulatory function with active DNA methyltransferase |
| 19 | <gene species="HORSE" symbol="IRAK3">IRAK3</gene> | <gene species="human" symbol="IRAK3">IRAK3</gene> | [A0A3Q2HDT6](https://rest.uniprot.org/uniprotkb/protnlm/A0A3Q2HDT6) | 0 | 1 | Assess receptor-signaling narrative and inactive-kinase context |
| 20 | <gene species="HORSE" symbol="PPP4R4">PPP4R4</gene> | <gene species="human" symbol="PPP4R4">PPP4R4</gene> | [A0A9L0S961](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0S961) | 3 | 0 | Separate phosphatase-regulator function from developmental transfer |
| 21 | <gene species="HORSE" symbol="CDK7">CDK7</gene> | <gene species="human" symbol="CDK7">CDK7</gene> | [A0A9L0R074](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0R074) | 2 | 0 | Evaluate specific kinase activity and phosphorylation process |
| 22 | <gene species="HORSE" symbol="MAP2K2">MAP2K2</gene> | <gene species="human" symbol="MAP2K2">MAP2K2</gene> | [A0A9L0SHX8](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SHX8) | 1 | 0 | Evaluate conserved kinase process and specificity |
| 23 | <gene species="HORSE" symbol="ZDHHC23">ZDHHC23</gene> | <gene species="human" symbol="ZDHHC23">ZDHHC23</gene> | [A0A9L0T4E4](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T4E4) | 1 | 0 | Evaluate specific protein S-palmitoyltransferase activity |
| 24 | <gene species="HORSE" symbol="CH25H">CH25H</gene> | <gene species="human" symbol="CH25H">CH25H</gene> | [F6T000](https://rest.uniprot.org/uniprotkb/protnlm/F6T000) | 3 | 0 | Evaluate oxidoreductase and lipid-biosynthesis specificity |
| 25 | <gene species="HORSE" symbol="BCAT2">BCAT2</gene> | <gene species="human" symbol="BCAT2">BCAT2</gene> | [A0A9L0TSN4](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0TSN4) | 0 | 1 | Evaluate branched-chain amino-acid catabolic narrative |
| 26 | <gene species="HORSE" symbol="SIRT5">SIRT5</gene> | <gene species="human" symbol="SIRT5">SIRT5</gene> | [F6S899](https://rest.uniprot.org/uniprotkb/protnlm/F6S899) | 1 | 1 | Evaluate deacylation substrate classes and weak in-vitro activity caveat |
| 27 | <gene species="HORSE" symbol="USP8">USP8</gene> | <gene species="human" symbol="USP8">USP8</gene> | [A0A9L0T7K6](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0T7K6) | 1 | 1 | Separate deubiquitination function from protein-catabolism process |
| 28 | <gene species="HORSE" symbol="OMA1">OMA1</gene> | <gene species="human" symbol="OMA1">OMA1</gene> | [A0A9L0R9P8](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0R9P8) | 1 | 0 | Evaluate proteolysis prediction and more specific mitochondrial role |
| 29 | <gene species="HORSE" symbol="EFR3A">EFR3A</gene> | <gene species="human" symbol="EFR3A">EFR3A</gene> | [A0A9L0S4L8](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0S4L8) | 1 | 0 | Evaluate protein recruitment to plasma membrane |
| 30 | <gene species="HORSE" symbol="CACNB3">CACNB3</gene> | <gene species="human" symbol="CACNB3">CACNB3</gene> | [A0A5F5PZM5](https://rest.uniprot.org/uniprotkb/protnlm/A0A5F5PZM5) | 1 | 0 | Distinguish ion-channel regulation from ion transport catalysis |
| 31 | <gene species="HORSE" symbol="SHLD2">SHLD2</gene> | <gene species="human" symbol="SHLD2">SHLD2</gene> | [A0A9L0RGD6](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0RGD6) | 6 | 1 | Evaluate DNA-repair directionality, class switching and localization |
| 32 | <gene species="HORSE" symbol="GEMIN5">GEMIN5</gene> | <gene species="human" symbol="GEMIN5">GEMIN5</gene> | [A0A9L0R5P7](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0R5P7) | 6 | 0 | Compare RNA-binding and translation claims with ubiquitination |
| 33 | <gene species="HORSE" symbol="AFAP1L2">AFAP1L2</gene> | <gene species="human" symbol="AFAP1L2">AFAP1L2</gene> | [A0A9L0RQI4](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0RQI4) | 9 | 0 | Evaluate adaptor binding, kinase activation and cytokine processes |
| 34 | <gene species="HORSE" symbol="OLFML2A">OLFML2A</gene> | <gene species="human" symbol="OLFML2A">OLFML2A</gene> | [A0A9L0SKW1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SKW1) | 4 | 0 | Separate extracellular-matrix location, binding and organization |
| 35 | <gene species="HORSE" symbol="CC2D2A">CC2D2A</gene> | <gene species="human" symbol="CC2D2A">CC2D2A</gene> | [A0A5F5PJ44](https://rest.uniprot.org/uniprotkb/protnlm/A0A5F5PJ44) | 4 | 0 | Evaluate developmental-process transfer and ciliary mechanism |
| 36 | <gene species="HORSE" symbol="WDPCP">WDPCP</gene> | <gene species="human" symbol="WDPCP">WDPCP</gene> | [A0A3Q2KRK8](https://rest.uniprot.org/uniprotkb/protnlm/A0A3Q2KRK8) | 4 | 0 | Evaluate cilium and cytoskeleton localization with projection organization |
| 37 | <gene species="HORSE" symbol="TRAF2">TRAF2</gene> | <gene species="human" symbol="TRAF2">TRAF2</gene> | [F7BIV4](https://rest.uniprot.org/uniprotkb/protnlm/F7BIV4) | 5 | 0 | Evaluate receptor binding, complex membership and immune context |
| 38 | <gene species="HORSE" symbol="WEE1">WEE1</gene> | <gene species="human" symbol="WEE1">WEE1</gene> | [F6TY09](https://rest.uniprot.org/uniprotkb/protnlm/F6TY09) | 7 | 0 | Separate kinase-related processes from oocyte-specific context |
| 39 | <gene species="HORSE" symbol="DYNLT2B">DYNLT2B</gene> | <gene species="human" symbol="DYNLT2B">DYNLT2B</gene> | [A0A9L0SWY1](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0SWY1) | 10 | 0 | Evaluate ciliary transport, dynein binding and localization claims |
| 40 | <gene species="HORSE" symbol="DNMT3A">DNMT3A</gene> | <gene species="human" symbol="DNMT3A">DNMT3A</gene> | [A0A9L0TK01](https://rest.uniprot.org/uniprotkb/protnlm/A0A9L0TK01) | 2 | 0 | Compare gene-expression regulation with DNMT3L on the same output terms |

## Identity and evidence

There is one accession per selected gene label and no duplicate current protein
sequences. SHLD2 uses A0A9L0RGD6; the additional release record A0A3Q2HUD4 is not a
second benchmark gene. Symbols come from the frozen official accession list.
Some current UniProt records omit their gene-name field; that absence is retained
in the CSV rather than filled from the model's predicted name.

The [ordinary UniProt record snapshot](mammal-benchmark/horse40-uniprot.jsonl.gz)
provides species, sequence versions, lengths and sequence checksums. All 40 are
horse records and all current lengths match the release list. This does not prove
that every record is a complete protein or that the prediction-time sequence is
unchanged; examine gene models and domain completeness during review.

The CSV identifies existing human, mouse and rat review files with matching gene
symbols as evidence-search leads. These are not verified orthology assignments or
independent biological validation. Establish the counterpart and trace its
experimental/analytical evidence before transferring a claim to horse.

This is a targeted, retrospective cohort, not a random horse sample or an estimate
of whole-proteome accuracy. A later mammalian benchmark can grow from these
horse-anchored cases after orthology and evidence are established. The original
ARGO-ProtNLM-50 is unchanged.

[Benchmark design and census](mammal-benchmark-design.md) ·
[ProtNLM evaluation project](../PROTNLM_EVALUATION.md)
