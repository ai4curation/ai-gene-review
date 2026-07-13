---
title: "PSEPK ppu00270 methionine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [metXS, metZ, PP_2528, metB, PP_4594, PP_4348, metH, metE, PP_4637]
autolink_gene_symbols: false
---

# PSEPK ppu00270: methionine biosynthesis

- Module seed: `methionine_biosynthesis`
- KEGG candidate genes from membership table: 46
- Selected module genes reviewed here: 9
- Curated review files in this batch: 9
- Module/pathway OpenScientist reports: 2
- Gene-level OpenScientist reports currently present: 9 of 9

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Curation | OpenScientist research | Module interpretation | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `metXS` | PP_5097 | Q88CT3 | kegg:ppu00270 | CURATED | PRESENT | covered: homoserine O-succinyltransferase | Homoserine O-succinyltransferase |
| [x] | `metZ` | PP_2001 | Q88LD4 | kegg:ppu00270 | CURATED | PRESENT | covered: substrate-matched direct sulfhydrylation | O-succinylhomoserine sulfhydrylase |
| [x] | `PP_2528` | PP_2528 | Q88JW9 | kegg:ppu00270 | CURATED | PRESENT | candidate_uncertain: O-acetylhomoserine substrate mismatch | O-acetylhomoserine thiol-lyase |
| [x] | `metB` | PP_0659 | Q88Q39 | kegg:ppu00450 | CURATED | PRESENT | covered: first trans-sulfuration enzyme | Cystathionine gamma-synthase |
| [x] | `PP_4348` | PP_4348 | Q88EV4 | kegg:ppu00450 | CURATED | PRESENT | covered: second trans-sulfuration enzyme | Cystathionine beta-lyase |
| [x] | `PP_4594` | PP_4594 | Q88E72 | kegg:ppu00450 | CURATED | PRESENT | candidate_uncertain: paralog/accessory gamma-lyase risk | Cystathionine gamma-synthase-family protein |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | CURATED | PRESENT | covered: cobalamin-dependent terminal methylation | Methionine synthase |
| [x] | `metE` | PP_2698 | Q88JF1 | kegg:ppu00450 | CURATED | PRESENT | covered/candidate: predicted compact cobalamin-independent MetE | Compact MetE catalytic-domain protein |
| [x] | `PP_4637` | PP_4637 | Q88E31 | kegg:ppu00450 | CURATED | PRESENT | candidate_uncertain: partial N-terminal MetE-like domain | MetE-like N-terminal domain protein |

## Notes

OpenScientist's PSEPK pathway report concludes that the methionine-biosynthesis module is satisfiable in KT2440, but not by treating all KEGG ppu00270 members as pathway genes. The supported primary route is `metXS` + `metZ` + `metH`: homoserine is activated to O-succinylhomoserine, sulfur is incorporated by substrate-matched direct sulfhydrylation, and homocysteine is methylated by cobalamin-dependent MetH.

The trans-sulfuration pair `metB` + `PP_4348` is a plausible secondary route. `metE` is curated as a predicted compact cobalamin-independent MetE, but direct KT2440 activity still needs testing. `PP_2528`, `PP_4594`, and `PP_4637` are curated conservatively because they are substrate-mismatched, paralog-ambiguous, or partial-domain hits. In particular, KT2440 should not be scored as having a complete cobalamin-independent MetE route from `PP_4637` alone without additional split-enzyme or biochemical evidence.

Generated UTC: 2026-07-12T00:07:59Z
