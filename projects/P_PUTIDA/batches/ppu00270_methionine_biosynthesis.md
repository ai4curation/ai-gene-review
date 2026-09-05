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
| [x] | `metE` | PP_2698 | Q88JF1 | kegg:ppu00450 | CURATED | PRESENT | candidate_uncertain: conflicting compact/partial MetE interpretation | Compact MetE catalytic-domain protein |
| [x] | `PP_4637` | PP_4637 | Q88E31 | kegg:ppu00450 | CURATED | PRESENT | candidate_uncertain: partial N-terminal MetE-like domain | MetE-like N-terminal domain protein |

## Notes

OpenScientist's PSEPK pathway report concludes that the methionine-biosynthesis module is satisfiable in KT2440, but not by treating all KEGG ppu00270 members as pathway genes. The supported primary route is `metXS` + `metZ` + `metH`: homoserine is activated to O-succinylhomoserine, sulfur is incorporated by substrate-matched direct sulfhydrylation, and homocysteine is methylated by cobalamin-dependent MetH.

The trans-sulfuration pair `metB` + `PP_4348` is a plausible secondary route. The exact PSEPK cobalamin-independent route remains unresolved because the `metE` and `PP_4637` reviews contain conflicting compact-versus-partial interpretations. `PP_2528`, `PP_4594`, and `PP_4637` are curated conservatively because they are substrate-mismatched, paralog-ambiguous, or partial-domain hits. KT2440 should not be scored as having a complete cobalamin-independent MetE route from either candidate without additional split-enzyme or biochemical evidence.

Generated UTC: 2026-07-12T00:07:59Z

## 2026-09-01 module repair audit

The reusable module was repaired without changing the nine PSEPK gene reviews.
Species-specific satisfiability claims now remain on this batch page rather than
in the module description or notes. The module retains all three bacterial
route-choice axes and now makes the substrate-matched direct routes explicit:
MetA/MetXS supplies O-succinylhomoserine to MetZ, whereas MetX supplies
O-acetylhomoserine to MetY. Trans-sulfuration remains a two-reaction MetB/MetC
alternative, and MetE and MetH remain alternative terminal synthases.

The family audit was conservative. Q88CT3, Q88LD4, and Q88KB5 are used as exact
PSEPK exemplars for the succinyltransferase, O-succinylhomoserine
sulfhydrylase, and cobalamin-dependent methionine synthase leaves. PANTHER IDs
are omitted from the MetA/MetX, MetY, MetZ, and MetE leaves because the local
families do not delimit the claimed substrate specificity or catalytic
completeness. Exact PANTHER subfamilies with official labels and verified member
containment ground canonical MetB, MetC, and MetH leaves. Canonical non-PSEPK
proteins ground the generic MetX, MetB, MetC, MetY, and MetE alternatives. No
PTN is asserted. The broad PTHR30519 identifier is deliberately omitted from the
MetE leaf because it groups complete MetE enzymes with partial MetE-like
proteins in the local evidence.

The selected-gene audit continues to exclude PP_2528, PP_4594, and PP_4637 from
module grounding: their reviews leave the physiological route, reaction
direction, or catalytic completeness unresolved. PSEPK metB and PP_4348 remain
plausible secondary trans-sulfuration candidates, but canonical characterized
MetB and MetC proteins are used to ground the reusable leaves rather than
promoting those KT2440 candidates beyond their gene-review evidence.

The required annotation-reviewer consultation also identified stale conflicts
among the PSEPK metE, metH, and PP_4637 narratives and unsupported specificity
in the PSEPK metB review. Those reviews were not broadened in this module repair;
instead, none is used as an exact exemplar for the disputed MetE or MetB leaves.
