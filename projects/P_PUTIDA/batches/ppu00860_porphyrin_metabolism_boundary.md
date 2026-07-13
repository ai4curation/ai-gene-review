---
title: "PSEPK ppu00860 Porphyrin metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00860: Porphyrin metabolism

- Module seed: `porphyrin_metabolism_boundary`
- Candidate genes from membership table: 46
- Primary bucket genes: 45
- Existing review files: 46
- Curated review files: 46
- Existing Asta research files: 46

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `hemF` | PP_0073 | Q88RQ6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Oxygen-dependent coproporphyrinogen-III oxidase (CPO) (Coprogen oxidase) (Coproporphyrinogenase) (EC 1.3.3.3) |
| [x] | `PP_0109` | PP_0109 | Q88RM0 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cytochrome B |
| [x] | `cyoE1` | PP_0110 | Q88RL9 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141) (Heme B farnesyltransferase 1) (Heme O synthase 1) |
| [x] | `hemC` | PP_0186 | Q88RE5 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Porphobilinogen deaminase (PBG) (EC 2.5.1.61) (Hydroxymethylbilane synthase) (HMBS) (Pre-uroporphyrinogen synthase) |
| [x] | `hemD` | PP_0187 | Q88RE4 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Uroporphyrinogen-III synthase (EC 4.2.1.75) |
| [x] | `PP_0188` | PP_0188 | Q88RE3 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Uroporphyrin-III C-methyltransferase |
| [x] | `PP_0431` | PP_0431 | Q88QQ7 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Protoporphyrinogen IX oxidase (PPO) (EC 1.3.99.-) |
| [x] | `bfr-I` | PP_0482 | Q88QK8 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Bacterioferritin (EC 1.16.3.1) |
| [x] | `hemA` | PP_0732 | Q88PW6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Glutamyl-tRNA reductase (GluTR) (EC 1.2.1.70) |
| [x] | `hemH` | PP_0744 | Q88PV4 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Ferrochelatase (EC 4.98.1.1) (Heme synthase) (Protoheme ferro-lyase) |
| [x] | `cyoE2` | PP_0816 | Q88PN3 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141) (Heme B farnesyltransferase 2) (Heme O synthase 2) |
| [x] | `hemO` | PP_1005 | Q88P48 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Heme oxygenase |
| [x] | `bfr-II` | PP_1082 | Q88NX1 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Bacterioferritin (EC 1.16.3.1) |
| [x] | `pduO` | PP_1349 | Q88N66 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyl |
| [x] | `PP_1358` | PP_1358 | Q88N58 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Heme iron utilization protein |
| [x] | `cobO` | PP_1672 | Q88MA2 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyl |
| [x] | `cobB__Q88MA1` | PP_1673 | Q88MA1 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Hydrogenobyrinate a,c-diamide synthase (EC 6.3.5.9) (Hydrogenobyrinic acid a,c-diamide synthase) |
| [x] | `cobD` | PP_1675 | Q88M99 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cobalamin biosynthesis protein CobD |
| [x] | `cobC` | PP_1676 | Q88M98 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | threonine-phosphate decarboxylase (EC 4.1.1.81) (L-threonine-O-3-phosphate decarboxylase) |
| [x] | `cobQ` | PP_1677 | Q88M97 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cobyric acid synthase |
| [x] | `cobP` | PP_1678 | Q88M96 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Bifunctional adenosylcobalamin biosynthesis protein (EC 2.7.1.156) (EC 2.7.7.62) |
| [x] | `cobT` | PP_1679 | Q88M95 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase (NN:DBI PRT) (EC 2.4.2.21) (N(1)-alpha-phosphorib |
| [x] | `PP_1680` | PP_1680 | Q88M94 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Alpha-ribazole-5'-phosphate phosphatase (EC 3.1.3.73) |
| [x] | `cobS` | PP_1681 | Q88M93 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Adenosylcobinamide-GDP ribazoletransferase (EC 2.7.8.26) (Cobalamin synthase) (Cobalamin-5'-phosphate synthase) |
| [x] | `gltX` | PP_1977 | Q88LF6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS) |
| [x] | `cobA` | PP_2090 | Q88L45 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | uroporphyrinogen-III C-methyltransferase (EC 2.1.1.107) |
| [x] | `PP_2582` | PP_2582 | Q88JR7 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Heme oxygenase |
| [x] | `hemB` | PP_2913 | Q88IT6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24) |
| [x] | `hemBB` | PP_3322 | Q88HN1 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24) |
| [x] | `PP_3409` | PP_3409 | Q88HF1 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cobalamin biosynthesis protein cobE |
| [x] | `cobM` | PP_3410 | Q88HF0 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-4 C(11)-methyltransferase (EC 2.1.1.133) |
| [x] | `PP_3506` | PP_3506 | Q88H59 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Magnesium chelatase, subunit ChII |
| [x] | `cobN` | PP_3507 | Q88H58 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cobaltochelatase subunit CobN (EC 6.6.1.2) |
| [x] | `PP_3763` | PP_3763 | Q88GG1 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | CobF protein |
| [x] | `cysG` | PP_3999 | Q88FT3 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Siroheme synthase [Includes: Uroporphyrinogen-III C-methyltransferase (Urogen III methylase) (EC 2.1.1.107) (SUMT) (Urop |
| [x] | `hemN` | PP_4264 | Q88F35 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Coproporphyrinogen-III oxidase (EC 1.3.98.3) |
| [x] | `hemL` | PP_4784 | Q88DP0 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Glutamate-1-semialdehyde 2,1-aminomutase (GSA) (EC 5.4.3.8) (Glutamate-1-semialdehyde aminotransferase) (GSA-AT) |
| [x] | `cobJ` | PP_4826 | Q88DJ9 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-3B C17-methyltransferase |
| [x] | `cobI` | PP_4827 | Q88DJ8 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-2 C(20)-methyltransferase (EC 2.1.1.130) |
| [x] | `cobH` | PP_4828 | Q88DJ7 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-8X methylmutase (EC 5.4.99.61) |
| [x] | `cobG` | PP_4829 | Q88DJ6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-3B synthase (EC 1.14.13.83) |
| [x] | `cobL` | PP_4830 | Q88DJ5 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-6Y C(5,15)-methyltransferase (EC 2.1.1.132) |
| [x] | `cbiD` | PP_4831 | Q88DJ4 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Cobalt-precorrin-5B C(1)-methyltransferase (EC 2.1.1.195) (Cobalt-precorrin-6A synthase) |
| [x] | `cobK` | PP_4832 | Q88DJ3 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Precorrin-6x reductase |
| [x] | `PP_4856` | PP_4856 | Q88DG9 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | ferroxidase (EC 1.16.3.1) |
| [x] | `hemE` | PP_5074 | Q88CV6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Uroporphyrinogen decarboxylase (UPD) (URO-D) (EC 4.1.1.37) |

## Notes

Generated UTC: 2026-07-08T16:05:26.316190+00:00

2026-07-11 PDT status sync: `modules/porphyrin_metabolism_boundary.yaml` is
curated and validates with both module validators. The module intentionally
spans the KEGG `ppu00860` candidate set plus the UniPathway UPA00252 support
view: `PP_0188` remains a no-GOA HemX-family boundary candidate from KEGG
`ppu00860`, while `PP_0189` is tracked as the adjacent HemY_N/TPR late
protoheme-biosynthesis support factor from UPA00252. The module should be read
as a tetrapyrrole/heme/corrinoid/siroheme boundary, not as one linear pathway.

Real Falcon commands were run:

```bash
just module-deep-research-falcon porphyrin_metabolism_boundary
just module-pathway-deep-research-falcon porphyrin_metabolism_boundary ppu00860 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. Expected output paths remain:

- `modules/porphyrin_metabolism_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__ppu00860-deep-research-falcon.md`
