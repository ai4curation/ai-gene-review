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
- Existing review files: 0
- Curated review files: 0
- Existing gene-level deep-research files: 0

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [ ] Fetch selected high-priority genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes selected for full review.
- [ ] Curate selected gene reviews.
- [x] Validate module and touched gene reviews.
- [x] Open one PR for this module/pathway: [#2136](https://github.com/ai4curation/ai-gene-review/pull/2136).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Gene research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `ssuE` | PP_0236 | Q88R97 | kegg:ppu00740 | MISSING | MISSING | MISSING | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [ ] | `ribD` | PP_0514 | Q88QH9 | kegg:ppu00740 | MISSING | MISSING | MISSING | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) ( |
| [ ] | `ribE` | PP_0515 | Q88QH8 | kegg:ppu00740 | MISSING | MISSING | MISSING | Riboflavin synthase (EC 2.5.1.9) |
| [ ] | `ribAB-I` | PP_0516 | Q88QH7 | kegg:ppu00740 | MISSING | MISSING | MISSING | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [ ] | `ribH` | PP_0517 | Q88QH6 | kegg:ppu00740 | MISSING | MISSING | MISSING | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78) |
| [ ] | `ribA` | PP_0522 | Q88QH1 | kegg:ppu00740 | MISSING | MISSING | MISSING | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) |
| [ ] | `ribB` | PP_0530 | Q88QG4 | kegg:ppu00740 | MISSING | MISSING | MISSING | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [ ] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | MISSING | MISSING | MISSING | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [ ] | `ribF` | PP_0602 | Q88Q93 | kegg:ppu00740 | MISSING | MISSING | MISSING | Riboflavin biosynthesis protein [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2. |
| [ ] | `bluB` | PP_1674 | Q88MA0 | kegg:ppu00740 | MISSING | MISSING | MISSING | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79) |
| [ ] | `msuE` | PP_2764 | Q88J85 | kegg:ppu00740 | MISSING | MISSING | MISSING | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) |
| [ ] | `ribC` | PP_2916 | Q88IT3 | kegg:ppu00740 | MISSING | MISSING | MISSING | Riboflavin synthase (EC 2.5.1.9) |
| [ ] | `ribAB-II` | PP_3813 | Q88GB1 | kegg:ppu00740 | MISSING | MISSING | MISSING | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [ ] | `nudF` | PP_4919 | Q88DA8 | kegg:ppu00740 | MISSING | MISSING | MISSING | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphori |
| [ ] | `had` | PP_5231 | Q88CF0 | kegg:ppu00740 | MISSING | MISSING | MISSING | (S)-2-haloacid dehalogenase (EC 3.8.1.-) |

## Notes

First-pass boundary:

- Core GTP-derived pyrimidine branch: `ribA` covers GTP cyclohydrolase II, followed by the two RibD activities in `ribD`.
- Core ribulose-5-phosphate donor branch: `ribB`, `ribAB-I`, and `ribAB-II` are DHBP synthase/RibBX-side candidates. The OpenScientist PSEPK report flags `ribAB-I` and `ribAB-II` as likely RibBX-like proteins whose C-terminal GTP-CHII-fold domains are degenerate, so they should not be used to satisfy GTP cyclohydrolase II without targeted gene review.
- Lumazine and riboflavin formation: `ribH` carries lumazine synthase; `ribE` and the redundant paralog `ribC` carry riboflavin synthase.
- Downstream flavin-cofactor activation: `ribF`, which converts riboflavin to FMN and FAD and is included as a connected downstream part of the reusable module.
- KEGG map spillover / neighboring processes: `ssuE` and `msuE` are FMN reductases, `ubiX` makes prenylated FMN for UbiD-family decarboxylases, `bluB` consumes flavin chemistry in cobalamin lower-ligand biosynthesis, `nudF` is nucleotide/ADP-ribose metabolism, and `had` is a broad HAD-family hit with only weak riboflavin-map context.

OpenScientist conclusions:

- The de novo riboflavin + FMN/FAD activation module is fully satisfiable in KT2440 on homology and architecture grounds, with no direct KT2440 biochemical/genetic evidence found in the first pass.
- The most important immediate gene-review follow-ups are `ribAB-I` and `ribAB-II` for the RibBX/dead-C-domain question, then `ribC` and `ribF`; `ribD` and `ribE` are lower priority unless review exposes annotation problems.
- No new GO terms are needed from this pass; existing MF/BP terms are sufficient if assigned to the correct step and gene.

This PR is a module-first light pass. It does not create PENDING gene-review stubs for all 15 KEGG members. Full gene reviews should prioritize the core `rib` genes and any non-core entries whose current GO/pathway mappings look misleading after module-level review.

Generated UTC: 2026-07-15T11:02:48.876044+00:00
