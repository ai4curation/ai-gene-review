---
title: "PSEPK choline-O-sulfate uptake and desulfation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_0075, PP_0076, betC]
autolink_gene_symbols: false
---

# PSEPK choline-O-sulfate uptake and desulfation

- Module: `bacterial_choline_o_sulfate_uptake_and_desulfation`
- Pathway context: choline-O-sulfate utilization
- Focused genes: 3
- Source GOA rows: 11

## Boundary

This batch covers two linked parts:

1. A provisional BetD/BetE-style choline-O-sulfate uptake step, represented by
   periplasmic binding candidate PP_0076 and SLC26A/SulP-STAS membrane candidate
   PP_0075.
2. BetC hydrolysis of choline-O-sulfate to choline, sulfate, and a proton.

Downstream BetA/BetB oxidation of choline to glycine betaine, transcriptional
regulation, and alternative sulfur-starvation pathways are outside scope. The
transport part is explicitly provisional: the KT2440 study did not assay
PP_0075 or PP_0076 individually, and choline-O-sulfate accumulation persisted
in the tested mutant background.

## Status

- [x] Fetch UniProt and GOA inputs for all three genes.
- [x] Define a reusable two-part module and validate its structure.
- [x] Check current target architectures and an experimentally characterized
  BetC exemplar.
- [x] Integrate and adjudicate all five completed OpenScientist reports.
- [x] Curate every GOA row and synthesize core functions.
- [x] Validate and render all artifacts.
- [x] Open single module PR [#2804](https://github.com/ai4curation/ai-gene-review/pull/2804).
- [ ] Complete `/review` follow-up.

## Focused Genes

| Gene | Locus | UniProt | GOA rows | Module role | Current evidence boundary |
|---|---|---:|---:|---|---|
| `PP_0075` | PP_0075 | Q88RQ4 | 2 | membrane transport candidate | SulP/SLC26-STAS architecture; exact cargo untested |
| `PP_0076` | PP_0076 | Q88RQ3 | 6 | periplasmic binding candidate | choline-family binding protein; no individual KT2440 assay |
| `betC` | PP_0077 | Q88RQ2 | 3 | choline sulfatase | exact family/EC plus KT2440 genetics and ortholog biochemistry |

The focused inventory and report coverage are recorded in
[`choline_o_sulfate_uptake_desulfation.tsv`](choline_o_sulfate_uptake_desulfation.tsv).

## Evidence Provenance

- PMID:17116241 provides direct KT2440 genetics for the `betC` region and shows
  that choline-O-sulfate uptake is not abolished by the tested mutation.
- PMID:9736747 provides direct genetics and enzyme evidence for the reviewed
  Sinorhizobium BetC exemplar O69787.
- PMID:29458126 provides purified-enzyme kinetics and crystal structures for
  the Sinorhizobium BetC exemplar.
- PMID:21369825 establishes that the BetC/BetD/BetE neighborhood recurs in
  another Pseudomonas strain, while only predicting BetD/BetE transport roles.
- Current UniProt records establish PP_0075 as an SLC26A/SulP-STAS multi-pass
  protein, PP_0076 as a signal-peptide-bearing choline-family binding protein,
  and Q88RQ2 as an IPR017785 choline-sulfatase-family protein.
- No PANTHER or PTN selector is asserted for exact BetC identity because the
  available PTHR45953:SF1 grouping is functionally broad and misleadingly named.
- The PP_0075 and PP_0076 OpenScientist reports were adjudicated rather than
  accepted wholesale. The PP_0075 report speculates about sulfate cargo and an
  ABC uptake route. The PP_0076 report additionally misidentifies
  PP_0074/Q88RQ5 (AroE shikimate dehydrogenase) as an ABC ATPase. Only
  independently checkable architecture and explicit knowledge-gap statements
  were retained.
- The generic module report's useful primary references were checked locally.
  Its claim that PMID:21369825 characterizes BetDE transport was narrowed: the
  paper clones the locus and characterizes BetC/BetR, but calls BetD/BetE
  potential transport proteins and reports no direct transport assay.
- The species-aware report correctly marks KT2440 uptake as
  `candidate_uncertain` and identifies PP_0076 as an orphan binding-protein
  candidate without a neighboring ABC ATPase. Its statement that no direct
  KT2440 phenotype exists is rejected because PMID:17116241 directly studies a
  KT2440 `betC` mutant and reports intact COS accumulation plus loss of C/N use.
- The BetC gene report correctly recovers the target motif and direct KT2440
  phenotype but repeats the unsupported adjacent-ABC-importer claim; that
  transport conclusion was not imported into the review or module.

Completed module-level reports:

- `modules/bacterial_choline_o_sulfate_uptake_and_desulfation-deep-research-openscientist.md`
- [`PSEPK module+pathway+taxon report`](../deep-research/PSEPK__bacterial-choline-o-sulfate-uptake-and-desulfation__choline-o-sulfate-utilization-deep-research-openscientist.md)

## Residual Uncertainty

- The physiological cargo range and coupling mechanism of PP_0075 are unknown.
- Direct binding specificity for PP_0076 has not been measured.
- The physical and functional coupling of PP_0075 and PP_0076 is not established.
- Direct enzyme kinetics have not been reported for KT2440 Q88RQ2 in isolation.
