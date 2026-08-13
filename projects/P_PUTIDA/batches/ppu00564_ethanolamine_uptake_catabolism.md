---
title: "PSEPK ethanolamine uptake and catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_0544, eutB, eutC, aldB-I]
autolink_gene_symbols: false
---

# PSEPK ethanolamine uptake and catabolism

- Module: `bacterial_ethanolamine_uptake_catabolism`
- Selected genes: 4
- KEGG `ppu00564` genes: 2
- Locus-extension genes: 2
- Curated review files: 4
- Completed OpenScientist gene reports: 1

## Workflow

- [x] Fetch all four selected gene-review inputs.
- [x] Integrate the completed EutC OpenScientist report.
- [x] Record missing OpenScientist artifacts for the other genes and module honestly.
- [x] Resolve transporter and aldehyde-dehydrogenase specificity.
- [x] Curate every available QuickGO annotation row with no `PENDING` actions.
- [x] Build and validate a reusable, species-neutral, multi-part module.
- [x] Validate and render the gene, module, and project artifacts.
- [x] Open one draft PR: [PR #2580](https://github.com/ai4curation/ai-gene-review/pull/2580).
- [ ] Shepherd review and CI to merge readiness.

## Selected Genes

| Done | Gene | Locus | UniProt | Selection | GOA rows | Curation | Research | Module role |
|---|---|---|---|---|---:|---|---|---|
| [x] | `eutC` | PP_0542 | Q88QF2 | KEGG `ppu00564` | 7 | CURATED | PRESENT (OpenScientist) | EutBC small subunit |
| [x] | `eutB` | PP_0543 | Q88QF1 | KEGG `ppu00564` | 0 | CURATED | MISSING | EutBC large subunit |
| [x] | `PP_0544` | PP_0544 | Q88QF0 | locus extension | 0 | CURATED | MISSING | APC-family ethanolamine uptake candidate |
| [x] | `aldB-I` | PP_0545 | Q88QE9 | locus extension | 3 | CURATED | PRESENT (existing Asta) | non-acylating acetaldehyde oxidation candidate |

## Boundary

- Uptake, EutBC deamination, and acetaldehyde oxidation are three separate parts.
- The reusable module permits classical EutH or APC-family transport and either
  acetylating EutE or non-acylating ALDH acetaldehyde oxidation.
- Microcompartment assembly, cobalamin synthesis, regulation, and downstream
  acetate or acetyl-CoA assimilation are outside the core boundary.
- KEGG `ppu00564` is glycerophospholipid metabolism, not an ethanolamine
  catabolism pathway definition. It supplies `eutB` and `eutC`; adjacent
  PP_0544 and PP_0545 were added from locus context to make the pathway testable.

## Curation Decisions

- Q88QF0 is an IPR004757/PTHR42770:SF7 APC-family transporter, not a classical
  EutH-family protein. `UniProtKB:P41796` is the verified classical EutH exemplar.
- Q88QE9 is an EC 1.2.1.3/PTHR43111:SF1 non-acylating aldehyde dehydrogenase,
  not acetylating EutE. `UniProtKB:Q9ZAA1` verifies the NAD-dependent
  acetaldehyde-to-acetate activity; `UniProtKB:P41793` verifies classical EutE.
- EutB and EutC are active subunits of one enzyme complex. Molecular function
  and cobalamin-binding assertions therefore use `contributes_to` in gene reviews.
- The two bacterial-microcompartment annotations on EutC were removed because
  no recognizable shell proteins occur in the compact KT2440 locus; shell
  encapsulation remains an optional organism-specific implementation context.
- Q88QF2 GOA cites `PANTHER:PTN002446609` for complex membership. The local
  PTHR39330 PAINT record instead places `GO:0009350` at the verified ancestral
  node `PTN002217404`, seeded by P19636 and P19265; the module uses that canonical node.

## Research Coverage

The completed EutC OpenScientist report and its artifacts were integrated. No
completed OpenScientist files were present for EutB, PP_0544, AldB-I, the generic
module, or the module + pathway + taxon query, so none were invented or restarted.
Those reviews rely on fetched UniProt/GOA records, primary literature, exact
family assignments, verified exemplars, and locus context. AldB-I also retains
its earlier Asta retrieval report as low-weight background.

## Residual Gaps

- Direct transport kinetics are needed to confirm Q88QF0 substrate specificity.
- Direct biochemistry or genetics is needed to establish that AldB-I consumes
  EutBC-derived acetaldehyde in vivo and to quantify its substrate preference.
- Growth and expression tests should establish whether the compact locus supports
  ethanolamine use as carbon, nitrogen, or both under cobalamin-supplied conditions.
- The absence of recognizable shell genes argues against a canonical Eut
  microcompartment but does not exclude an unrecognized encapsulation mechanism.

2026-08-13: Started as module 19 of the current 20-module batch.
