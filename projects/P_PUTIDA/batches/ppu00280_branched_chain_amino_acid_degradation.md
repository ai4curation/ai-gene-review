---
title: "PSEPK ppu00280 Valine, leucine and isoleucine degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00280: Valine, leucine and isoleucine degradation

- Module seed: `branched_chain_amino_acid_degradation`
- Candidate genes from membership table: 35
- Primary bucket genes: 8
- Existing review files: 35
- Curated review files: 35
- Existing Asta research files: 35

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
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `PP_0596` | PP_0596 | Q88Q98 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18) |
| [x] | `mmsA-I` | PP_0597 | Q88Q97 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `PP_2437` | PP_2437 | Q88K54 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) |
| [x] | `PP_2793` | PP_2793 | Q88J56 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) |
| [x] | `aacs` | PP_3071 | Q88IC8 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Acetoacetyl-coenzyme A synthetase (EC 6.2.1.16) |
| [x] | `atoA` | PP_3122 | Q88I79 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase (EC 2.8.3.6) |
| [x] | `atoB` | PP_3123 | Q88I78 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase (EC 2.8.3.6) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `PP_3394` | PP_3394 | Q88HG4 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | 3-hydroxy-3-methylglutaryl-CoA lyase |
| [x] | `ilvE` | PP_3511 | Q88H54 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) |
| [x] | `mvaB` | PP_3540 | Q88H25 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | hydroxymethylglutaryl-CoA lyase (EC 4.1.3.4) |
| [x] | `PP_3725` | PP_3725 | Q88GJ7 | kegg:ppu00071 | PRESENT | CURATED | PRESENT | Acyl-CoA dehydrogenase |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `ivd` | PP_4064 | Q88FM5 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Isovaleryl-CoA dehydrogenase, mitochondrial (EC 1.3.8.4) |
| [x] | `mccB` | PP_4065 | Q88FM4 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Methylcrotonyl-CoA carboxylase biotin-containing subunit beta (EC 6.4.1.4) |
| [x] | `liuC` | PP_4066 | Q88FM3 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Methylglutaconyl-CoA hydratase (EC 4.2.1.18) |
| [x] | `mccA` | PP_4067 | Q88FM2 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `lpdG` | PP_4187 | Q88FB1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `bkdAA` | PP_4401 | Q88EQ2 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component alp |
| [x] | `bkdAB` | PP_4402 | Q88EQ1 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component beta |
| [x] | `bkdB` | PP_4403 | Q88EQ0 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.-) |
| [x] | `lpdV` | PP_4404 | Q88EP9 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |
| [x] | `ldh` | PP_4617 | Q88E51 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Leucine dehydrogenase (EC 1.4.1.9) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `mmsB` | PP_4666 | Q88E02 | kegg:ppu00280 | PRESENT | CURATED | PRESENT | 3-hydroxyisobutyrate dehydrogenase (HIBADH) (EC 1.1.1.31) |
| [x] | `mmsA-II` | PP_4667 | Q88E01 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `lpd` | PP_5366 | Q88C17 | kegg:ppu00785 | PRESENT | CURATED | PRESENT | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) |

## Notes

Generated UTC: 2026-07-07T18:48:33.336396+00:00

## Workflow Notes

- Completed first-pass curation for all 35 KEGG ppu00280 membership candidates.
- Created and validated the species-neutral module:
  `modules/branched_chain_amino_acid_degradation.yaml`.
- Fetched the 17 previously missing review folders and ran Asta gene-level
  retrieval for each.
- Validated all 35 candidate gene reviews. Existing side-pathway reviews still
  have some non-blocking "Asta file not cited in annotation decisions" warnings;
  the 17 newly curated ppu00280 reviews validate cleanly.
- Rendered gene review pages for all 35 candidates.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon branched_chain_amino_acid_degradation` and
  `just module-pathway-deep-research-falcon branched_chain_amino_acid_degradation ppu00280 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/branched_chain_amino_acid_degradation-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__branched_chain_amino_acid_degradation__ppu00280-deep-research-falcon.md`.

## Curation Notes

- Treat the strict BCAA degradation core as the `ivd`/`mccA`/`mccB`/`liuC`
  L-leucine branch, `mmsB`/`mmsA-I`/`mmsA-II` L-valine branch, and
  `bkdAA`/`bkdAB`/`bkdB` BCKDH complex context.
- Added conservative `NEW` rows where GOA lacked strong synthesized terms:
  `liuC` and `mccA` for L-leucine catabolism, `mccA` for the
  methylcrotonyl-CoA carboxylase complex, and `bkdAA`/`bkdAB`/`bkdB` for the
  branched-chain alpha-ketoacid dehydrogenase complex/process context.
- `ldh` was corrected from a fetched glutamate dehydrogenase GOA activity to
  L-leucine dehydrogenase activity based on the UniProt EC 1.4.1.9 identity.
- `PP_0596`, `aacs`, `atoA`, and `atoB` are boundary/endpoint chemistry, not
  strict upstream BCAA degradation: beta-alanine/amine transamination,
  acetoacetate ligase, and beta-ketoadipate CoA-transferase context,
  respectively.
- Fatty-acid beta-oxidation paralogs, thiolases, lipoamide E3 paralogs, and
  beta-ketoadipate CoA-transferases remain boundary spillovers unless
  gene-level evidence supports a committed BCAA role.
