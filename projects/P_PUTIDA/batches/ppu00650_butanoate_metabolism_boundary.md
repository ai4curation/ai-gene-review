---
title: "PSEPK ppu00650 Butanoate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00650: Butanoate metabolism

- Module seed: `butanoate_metabolism_boundary`
- Candidate genes from membership table: 38
- Primary bucket genes: 5
- Existing review files: 38
- Curated review files: 38
- Existing Asta research files: 38

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
| [x] | `scpC` | PP_0154 | Q88RH5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Propionyl-CoA:succinate CoA transferase (EC 2.8.3.-) |
| [x] | `davD` | PP_0213 | Q88RC0 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) |
| [x] | `davT` | PP_0214 | Q88RB9 | kegg:ppu00310 | PRESENT | CURATED | PRESENT | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48) (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase |
| [x] | `bdhA` | PP_0552 | Q88QE2 | kegg:ppu00650 | PRESENT | CURATED | PRESENT | 2,3-butanediol dehydrogenase (EC 1.1.1.4) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `PP_1157` | PP_1157 | Q877U6 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase |
| [x] | `PP_1394` | PP_1394 | Q88N22 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase, large subunit |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `sad-I` | PP_2488 | Q88K05 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `gbd` | PP_2650 | Q88JJ9 | kegg:ppu00650 | PRESENT | CURATED | PRESENT | 4-hydroxybutyrate dehydrogenase (EC 1.1.1.61) |
| [x] | `PP_2799` | PP_2799 | Q88J50 | kegg:ppu00250 | PRESENT | CURATED | PRESENT | Aminotransferase, class III |
| [x] | `aacs` | PP_3071 | Q88IC8 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Acetoacetyl-coenzyme A synthetase (EC 6.2.1.16) |
| [x] | `hbdH` | PP_3073 | Q88IC6 | kegg:ppu00650 | PRESENT | CURATED | PRESENT | 3-hydroxybutyrate dehydrogenase (EC 1.1.1.30) |
| [x] | `atoA` | PP_3122 | Q88I79 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase (EC 2.8.3.6) |
| [x] | `atoB` | PP_3123 | Q88I78 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase (EC 2.8.3.6) |
| [x] | `sad-II` | PP_3151 | Q88I50 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `paaH` | PP_3282 | Q88HS1 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `PP_3394` | PP_3394 | Q88HG4 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | 3-hydroxy-3-methylglutaryl-CoA lyase |
| [x] | `mvaB` | PP_3540 | Q88H25 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | hydroxymethylglutaryl-CoA lyase (EC 4.1.3.4) |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `hbd` | PP_3755 | Q88GG9 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) |
| [x] | `maiA` | PP_3942 | Q88FY4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase) (Nicotinate degradation protein E) |
| [x] | `sdhB` | PP_4190 | Q88FA8 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1) |
| [x] | `sdhA` | PP_4191 | Q88FA7 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1) |
| [x] | `sdhD` | PP_4192 | Q88FA6 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase hydrophobic membrane anchor subunit |
| [x] | `sdhC` | PP_4193 | Q88FA5 | kegg:ppu00020 | PRESENT | CURATED | PRESENT | Succinate dehydrogenase cytochrome b556 subunit |
| [x] | `gabD-II` | PP_4422 | Q88EN2 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) |
| [x] | `fabV` | PP_4635 | Q88E33 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Enoyl-[acyl-carrier-protein] reductase [NADH] (ENR) (EC 1.3.1.9) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `ilvH` | PP_4679 | Q88DY9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) |
| [x] | `ilvI` | PP_4680 | Q88DY8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase (EC 2.2.1.6) |
| [x] | `phaA` | PP_5003 | Q88D25 | kegg:ppu00650 | PRESENT | CURATED | PRESENT | Poly(3-hydroxyalkanoate) polymerase 1 (EC 2.3.1.-) |
| [x] | `phaC-II` | PP_5005 | Q88D23 | kegg:ppu00650 | PRESENT | CURATED | PRESENT | Poly(3-hydroxyalkanoate) polymerase 2 (EC 2.3.1.-) |

## Notes

Generated UTC: 2026-07-08T14:03:31.502167+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon butanoate_metabolism_boundary`
  and `just module-pathway-deep-research-falcon butanoate_metabolism_boundary ppu00650 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/butanoate_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__butanoate_metabolism_boundary__ppu00650-deep-research-falcon.md`.
