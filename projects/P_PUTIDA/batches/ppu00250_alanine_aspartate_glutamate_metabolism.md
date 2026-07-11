---
title: "PSEPK ppu00250 Alanine, aspartate and glutamate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00250: Alanine, aspartate and glutamate metabolism

- Module seed: `alanine_aspartate_glutamate_metabolism`
- Candidate genes from membership table: 36
- Primary bucket genes: 8
- Existing review files: 36
- Curated review files: 36
- Existing Asta research files: 36

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `argH` | PP_0184 | P59618 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) |
| [x] | `davD` | PP_0213 | Q88RC0 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) |
| [x] | `davT` | PP_0214 | Q88RB9 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48) (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase |
| [x] | `ansA` | PP_0495 | Q88QJ6 | kegg:ppu00460 | PRESENT | CURATED | PRESENT | Type 1 L-asparaginase (EC 3.5.1.1) |
| [x] | `gdhA` | PP_0675 | Q88Q23 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate dehydrogenase |
| [x] | `PP_0859` | PP_0859 | Q88PJ1 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Omega-amidase YafV (EC 3.5.1.3) |
| [x] | `argG` | PP_1088 | P59604 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase) |
| [x] | `PP_1160` | PP_1160 | Q88NP7 | kegg:ppu00460 | PRESENT | CURATED | PRESENT | Asparaginase family protein |
| [x] | `nadB` | PP_1426 | Q88MZ2 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | L-aspartate oxidase (EC 1.4.3.16) |
| [x] | `asnB` | PP_1750 | Q88M25 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | asparagine synthase (glutamine-hydrolyzing) (EC 6.3.5.4) |
| [x] | `alaA` | PP_1872 | Q88LQ7 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) |
| [x] | `purF` | PP_2000 | Q88LD5 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) |
| [x] | `gdhB` | PP_2080 | Q88L55 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) |
| [x] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `ansB` | PP_2453 | Q88K39 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) |
| [x] | `sad-I` | PP_2488 | Q88K05 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `PP_2799` | PP_2799 | Q88J50 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Aminotransferase, class III |
| [x] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `sad-II` | PP_3151 | Q88I50 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `purB` | PP_4016 | Q88FR7 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) |
| [x] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `gabD-II` | PP_4422 | Q88EN2 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) |
| [x] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `carB` | PP_4723 | Q88DU6 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) |
| [x] | `carA` | PP_4724 | Q88DU5 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) |
| [x] | `purA` | PP_4889 | Q88DD8 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase) |
| [x] | `putA` | PP_4947 | Q88D80 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Bifunctional protein PutA [Includes: Proline dehydrogenase (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxyla |
| [x] | `pyrB` | PP_4998 | Q88D30 | kegg:ppu00240 | PRESENT | CURATED | PRESENT | Aspartate carbamoyltransferase catalytic subunit (EC 2.1.3.2) (Aspartate transcarbamylase) (ATCase) |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase (EC 6.3.1.2) |
| [x] | `gltD` | PP_5075 | Q88CV5 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13) |
| [x] | `gltB` | PP_5076 | Q88CV4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) |
| [x] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `aspA` | PP_5338 | Q88C45 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Aspartate ammonia-lyase (Aspartase) (EC 4.3.1.1) |
| [x] | `glmS` | PP_5409 | Q88BX8 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Glutamine--fructose-6-phosphate aminotransferase [isomerizing] (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) ( |

## Notes

Generated UTC: 2026-07-07T17:08:48.671921+00:00

### Workflow Notes

- Created and validated `modules/alanine_aspartate_glutamate_metabolism.yaml`.
- Registered `kegg:ppu00250` in `projects/P_PUTIDA/build_pathway_worklist.py`
  as a broad alanine/aspartate/glutamate boundary module.
- Fetched 9 missing review folders: `davT`, `ansA`, `PP_0859`, `PP_1160`,
  `asnB`, `PP_2799`, `putA`, `aspA`, and `glmS`.
- Ran Asta for those 9 missing gene-level reports with no provider retries.
- Curated the 9 newly fetched review YAMLs. The final batch has 36/36 review
  folders present, 36/36 Asta reports present, and 36/36 reviews curated.
- Validated the module and all 36 candidate gene reviews. Warnings are limited
  to expected first-pass Asta-context notices.
- Rendered all 36 gene pages.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon alanine_aspartate_glutamate_metabolism` and
  `just module-pathway-deep-research-falcon alanine_aspartate_glutamate_metabolism ppu00250 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/alanine_aspartate_glutamate_metabolism-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__alanine_aspartate_glutamate_metabolism__ppu00250-deep-research-falcon.md`.

### Curation Notes

- The strict alanine/aspartate/glutamate hub is represented by AlaA, GdhA/GdhB,
  GlnA/GS-like paralogs, GltBD, AspA, AsnB, AnsA/PP_1160, and PP_0859.
- KEGG ppu00250 pulls in many real but cross-pathway donor/acceptor side nodes:
  ArgG/ArgH, CarAB/PyrB, PurA/PurB/PurF, NadB, GlmS, PutA, PuuA/Spu ligases,
  DavD/DavT, Sad/GabD enzymes, and PP_2799.
- `davT` is the strongest direct experimental case in this batch: its IDA/IMP
  annotations support 5-aminovalerate aminotransferase activity in lysine
  catabolism, while the GABA aminotransferase transfer was modified to the
  specific DavT activity.
- `PP_2799` was curated as a BioA-like biotin-biosynthesis aminotransferase
  rather than as a committed ppu00250 core enzyme.
- `putA` was curated as bifunctional proline catabolism plus transcriptional
  repression; the electronic L-proline biosynthetic process transfer was
  removed.
- First-pass specificity fixes include PP_0859 broad hydrolase to
  2-oxoglutaramate amidase, AspA broad catalytic/lyase terms to aspartate
  ammonia-lyase, and GlmS broad carbohydrate/glycosylation context to amino
  sugar biosynthesis.
