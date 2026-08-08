---
title: "PSEPK ppu00730 Thiamine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00730: Thiamine metabolism

- Module seed: `thiamine_diphosphate_biosynthesis`
- Candidate genes from membership table: 13
- Additional curation follow-ups from OpenScientist: 2 (`PP_5105`/ThiS, `moeB`/PP_0735)
- Primary bucket genes: 13
- Existing review files: 2
- Curated review files: 2
- Existing gene-level deep-research files: 0

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [ ] Fetch selected high-priority genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes selected for full review.
- [ ] Curate selected gene reviews.
- [x] Validate module and touched gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `thiL` | PP_0519 | Q88QH4 | kegg:ppu00730 | MISSING | MISSING | MISSING | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) |
| [ ] | `dxs` | PP_0527 | Q88QG7 | kegg:ppu00730 | MISSING | MISSING | MISSING | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) |
| [ ] | `thiO` | PP_0612 | Q88Q83 | kegg:ppu00730 | PRESENT | CURATED | MISSING | Glycine oxidase (GO) (EC 1.4.3.19) |
| [ ] | `iscS` | PP_0842 | Q88PK8 | kegg:ppu00730 | MISSING | MISSING | MISSING | Cysteine desulfurase IscS (EC 2.8.1.7) |
| [ ] | `adk` | PP_1506 | P0A136 | kegg:ppu00730 | MISSING | MISSING | MISSING | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate ki |
| [ ] | `iscS-II` | PP_2435 | Q88K56 | kegg:ppu00730 | MISSING | MISSING | MISSING | cysteine desulfurase (EC 2.8.1.7) |
| [ ] | `PP_3186` | PP_3186 | Q88I16 | kegg:ppu00730 | MISSING | MISSING | MISSING | Aminopyrimidine aminohydrolase (EC 3.5.99.2) |
| [ ] | `thiD` | PP_4782 | Q88DP2 | kegg:ppu00730 | MISSING | MISSING | MISSING | hydroxymethylpyrimidine kinase (EC 2.7.1.49) |
| [ ] | `thiE` | PP_4783 | Q88DP1 | kegg:ppu00730 | MISSING | MISSING | MISSING | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphoryla |
| [ ] | `rsgA` | PP_4903 | Q88DC4 | kegg:ppu00730 | MISSING | MISSING | MISSING | Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-) |
| [ ] | `thiC` | PP_4922 | Q88DA5 | kegg:ppu00730 | MISSING | MISSING | MISSING | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosp |
| [ ] | `thiI` | PP_5045 | Q88CY4 | kegg:ppu00730 | PRESENT | CURATED | MISSING | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) |
| [ ] | `thiG` | PP_5104 | Q88CS6 | kegg:ppu00730 | MISSING | MISSING | MISSING | Thiazole synthase (EC 2.8.1.10) |

## Additional Curation Follow-Ups

| Priority | Gene | Locus | UniProt | Bucket | OpenScientist action | Rationale |
|---|---|---|---|---|---|---|
| High | `PP_5105` / ThiS | PP_5105 | Q88CS5 | kegg:ppu04122 | Add to module gene list | ThiS sulfur carrier is required for thiazole synthesis and sits next to `thiG`, but the local partition assigns it to sulfur relay rather than ppu00730. |
| High | `moeB` | PP_0735 | Q88PW3 | kegg:ppu04122 | Review as candidate_uncertain | KT2440 lacks a dedicated ThiF; MoeB is the only plausible E1-like adenylyltransferase candidate for the ThiS activation step but is not confirmed. |

## Notes

First-pass boundary:

- Core de novo ThDP biosynthesis is the HMP branch (`thiC`, `thiD`), thiazole branch (`dxs`, `thiO`, ThiF/ThiI/ThiS sulfur relay, `thiG`), coupling by `thiE`, and final phosphorylation by `thiL`.
- `PP_5105` encodes ThiS, the sulfur carrier needed by the thiazole branch. It is not in the ppu00730 candidate list because the local partition assigns it to KEGG sulfur-relay map ppu04122, but it should be treated as a likely pathway hole for this module.
- OpenScientist resolves the cysteine-desulfurase candidate toward housekeeping `iscS`/PP_0842 by operon context and down-weights `iscS-II`/PP_2435, but this is still inferential and should be checked in full gene review.
- KEGG map spillover / neighboring processes: `adk` is adenylate kinase, `rsgA` is ribosome biogenesis GTPase, and `PP_3186` is an aminopyrimidine aminohydrolase/salvage candidate rather than an obligatory de novo ThDP step.

OpenScientist findings:

- Module-level report: `modules/thiamine_diphosphate_biosynthesis-deep-research-openscientist.md`.
- PSEPK pathway report: `projects/P_PUTIDA/deep-research/PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist.md`.
- The de novo ThDP pathway is satisfiable in KT2440. Direct target-strain support is strongest for ThiO biochemistry and the `thiC` TPP riboswitch; the rest is mainly homology, EC, synteny, and prototrophy evidence.
- The single serious curation gap is ThiF-type ThiS C-terminal adenylylation (EC 2.7.7.73). KT2440 has no dedicated `thiF`; `moeB`/PP_0735 is the sole plausible but unconfirmed substitute.
- Move TenA/PP_3185/PP_3186 and PP_1762 to a future thiamine-salvage module; do not model them as required de novo ThDP biosynthesis steps.

This PR is a module-first pass with module and species/pathway OpenScientist grounding. It does not create PENDING gene-review stubs for all 13 KEGG members. Full gene reviews should prioritize `moeB`, `PP_5105`, `thiL`, `thiC`, `thiD`, `thiE`, `thiG`, and the `iscS`/`iscS-II` sulfur-donor question.

PR: https://github.com/ai4curation/ai-gene-review/pull/2139

Generated UTC: 2026-07-15T12:21:56.455521+00:00
