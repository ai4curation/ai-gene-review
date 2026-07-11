---
title: "PSEPK ppu00740 Riboflavin metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00740: Riboflavin metabolism

- Module seed: `riboflavin_biosynthesis`
- Candidate genes from membership table: 15
- Primary bucket genes: 14
- Existing review files: 15
- Curated review files: 15
- Existing Asta research files: 15

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `ssuE` | PP_0236 | Q88R97 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [x] | `ribD` | PP_0514 | Q88QH9 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) ( |
| [x] | `ribE` | PP_0515 | Q88QH8 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | Riboflavin synthase (EC 2.5.1.9) |
| [x] | `ribAB-I` | PP_0516 | Q88QH7 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [x] | `ribH` | PP_0517 | Q88QH6 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78) |
| [x] | `ribA` | PP_0522 | Q88QH1 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) |
| [x] | `ribB` | PP_0530 | Q88QG4 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [x] | `ribF` | PP_0602 | Q88Q93 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | Riboflavin biosynthesis protein [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2. |
| [x] | `bluB` | PP_1674 | Q88MA0 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79) |
| [x] | `msuE` | PP_2764 | Q88J85 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [x] | `ribC` | PP_2916 | Q88IT3 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | Riboflavin synthase (EC 2.5.1.9) |
| [x] | `ribAB-II` | PP_3813 | Q88GB1 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [x] | `nudF` | PP_4919 | Q88DA8 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphori |
| [x] | `had` | PP_5231 | Q88CF0 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | (S)-2-haloacid dehalogenase (EC 3.8.1.-) |

## Notes

Generated UTC: 2026-07-07T10:16:33.989375+00:00

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 15 KEGG `ppu00740` membership candidates extracted. The worklist primary
  bucket count is 14 because `ubiX` is primarily assigned to the ubiquinone/side
  pathway context; the batch keeps it here as a riboflavin-map boundary gene.
- 15/15 candidate review folders present, Asta retrieval reports present, and
  review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module created and validated:
  `modules/riboflavin_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/riboflavin_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon.md`.
- Gene validation complete for all 15 candidates with `just validate PSEPK
  <gene>`. Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/riboflavin_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/riboflavin_biosynthesis.yaml
```

Main conclusions:

- The strict riboflavin/FMN/FAD biosynthesis module is satisfiable in KT2440.
  The core route is covered by `ribA`, `ribD`, `ribB`, `ribH`, `ribE`, and
  `ribF`; `ribC` remains a duplicate riboflavin synthase candidate.
- Falcon found the main curation lesson: `ribAB-I`/PP_0516 and
  `ribAB-II`/PP_3813 are RibBX/DHBP synthase enzymes, not true bifunctional
  RibBA enzymes. Their GTP cyclohydrolase II annotations were removed from the
  gene reviews and from the module step; the GTP cyclohydrolase II step is
  satisfied only by `ribA`.
- `ssuE` and `msuE` are FMN reductases for organosulfur metabolism, `bluB` is
  cobalamin lower-ligand synthesis, `ubiX` is prenyl-FMN formation for UbiD,
  `nudF` is nucleotide housekeeping, and `had` was excluded from strict
  riboflavin/FMN/FAD biosynthesis.
