---
title: "PSEPK alkanesulfonate uptake and desulfonation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ssuA, ssuB, ssuC, ssuD, ssuE]
autolink_gene_symbols: false
---

# PSEPK alkanesulfonate uptake and desulfonation

- Module: `bacterial_alkanesulfonate_uptake_desulfonation`
- Pathway context: KEGG `ppu00920` (sulfur metabolism)
- Initial curation pull request: [#2590](https://github.com/ai4curation/ai-gene-review/pull/2590)
- Focused genes: 5
- Source GOA rows: 3, all on `ssuD`

## Boundary

This batch covers three linked parts:

1. `ssuA`, `ssuB`, and `ssuC` form the SsuABC alkanesulfonate importer.
2. `ssuE` supplies reduced FMN to the canonical two-component oxygenase system.
3. `ssuD` converts an imported alkanesulfonate to the corresponding aldehyde
   and sulfite.

Sulfite assimilation, sulfur-starvation transcriptional control, aromatic
sulfonate pathways, taurine import/desulfonation, and downstream aldehyde
metabolism are outside the module. Reduced-FMN supply is represented as an
optional canonical SsuE-family part because Pseudomonas putida S-313 genetics
showed that another reductase can support growth on aliphatic sulfonates.

## Status

- [x] Fetch or reuse all five `ssuABCDE` UniProt and GOA inputs.
- [x] Consume every materialized research report. OpenScientist produced a
  complete `ssuB` report; the existing `ssuD` Falcon report was also integrated.
- [x] Record prior missing provider coverage honestly. Completed `ssuA`,
  `ssuC`, `ssuE`, generic-module, and module+pathway+taxon jobs in the initial
  wave did not materialize reports.
- [x] Complete a fresh generic module OpenScientist run in wave122 with the full
  7,200-second allowance; it returned in 968 seconds with HTML/PDF artifacts.
- [x] Use the existing taxon-aware taurine-pathway report as a checked boundary
  source: it identifies `ssuEADCB` as a parallel KT2440 alkanesulfonate system,
  not as part of TauABC/TauD.
- [x] Exclude the nearby `PSEPK__aps_dependent_assimilatory_sulfate_reduction__ppu00920`
  report because it addresses APS-dependent sulfate reduction, not the SsuABC/SsuED
  alkanesulfonate module.
- [x] Reconcile paralog specificity and curate every GOA row.
- [x] Apply annotation-reviewer and module-curation requirements.
- [x] Validate and render all artifacts.
- [x] Merge PR #2590 after two formal review passes and requested corrections.

## Focused Genes

| Gene | Locus | UniProt | GOA rows | Module role | Decision |
|---|---|---:|---:|---|---|
| `ssuA` | PP_0237 | Q88R96 | 0 | periplasmic binding unit | Added inference-supported complex, transport, and location annotations |
| `ssuB` | PP_0240 | Q88R93 | 0 | ATP-coupling unit | Added ATPase, complex-level transporter contribution, process, complex, and location annotations |
| `ssuC` | PP_0239 | Q88R94 | 0 | inner-membrane permease unit | Added complex-level transporter contribution, process, complex, and location annotations |
| `ssuD` | PP_0238 | Q88R95 | 3 | FMNH2-dependent monooxygenase | Accepted exact MF/process; modified the broad oxygenase parent to the existing exact MF |
| `ssuE` | PP_0236 | Q88R97 | 0 | reduced-FMN supplier | Added exact reductase MF and pathway involvement without asserting universal indispensability |

The focused inventory and report coverage are recorded in
[`ppu00920_alkanesulfonate_uptake_desulfonation.tsv`](ppu00920_alkanesulfonate_uptake_desulfonation.tsv).

## Evidence Provenance

- Exact KT2440 accessions and records were checked against current UniProt REST:
  Q88R96, Q88R93, Q88R94, Q88R95, and Q88R97.
- A second complete reviewed exemplar set was verified for Escherichia coli
  K-12: P75853, P0AAI1, P75851, P80645, and P80644.
- PMID:10781557 provides direct P. putida S-313 locus genetics for the SsuABC
  transporter and SsuED reduced-flavin monooxygenase organization.
- PMID:10781534 provides deletion/complementation evidence that SsuABC is a
  dedicated, non-interchangeable alkanesulfonate uptake system in E. coli.
- PMID:10480865 directly characterizes purified E. coli SsuE and SsuD and
  establishes reduced-FMN transfer and broad alkanesulfonate oxygenolysis.
- Local PTHR42847 PAINT data verifies node PTN000768559, seeded by E. coli SsuD
  P80645, for GO:0008726 and GO:0046306. The GOA-provided PTN002450490 was
  retained as row provenance but was not misrepresented as the canonical PAINT
  ancestral node.
- Fresh generic OpenScientist research is retained as
  [`bacterial_alkanesulfonate_uptake_desulfonation-deep-research-openscientist.md`](../../../modules/bacterial_alkanesulfonate_uptake_desulfonation-deep-research-openscientist.md).
  It supports the broad boundary and neighboring-pathway exclusions. Its claim
  that SsuE reduction is universally obligatory conflicts with the direct
  Pseudomonas redundancy result, and its channeling language exceeds the
  unresolved transfer evidence; neither claim was promoted into the module.
- Official QuickGO records were checked directly on 2026-08-13. GO:0042959 is
  correctly labeled `ABC-type alkanesulfonate transporter transporter activity`
  (including the doubled `transporter`), and GO:0055052 is `ATP-binding cassette
  (ABC) transporter complex, substrate-binding subunit-containing`.

## Residual Uncertainty

- The exact substrate range of KT2440 SsuA/SsuC has not been measured directly.
- Q88R93, Q88R94, and Q88R96 roles are strong family/cluster inferences rather
  than target-protein biochemical demonstrations.
- The alternative KT2440 reductase or reductases that can replace SsuE are
  unknown, and their use may depend on substrate and sulfur status.
- KT2440 contains related binding proteins and monooxygenases; their division of
  labor with the syntenic `ssuABCDE` system remains unresolved.

## 2026-09-01 wave122 repair checkpoint

The mandatory annotation-reviewer pass rechecked all three imported `ssuD` GOA
rows and all 16 explicit `NEW` proposals across `ssuA`, `ssuB`, `ssuC`, and
`ssuE`. No row-level action changed. Complex-level transport remains
`contributes_to` for each SsuABC subunit, ATP hydrolysis remains specific to
SsuB, target-record-supported periplasm and membrane locations remain intact,
and neither SsuD nor SsuE receives an inferred cytosol annotation.

The reusable module now has two root parts: the SsuABC uptake complex and a
nested reduced-flavin desulfonation module. The latter decomposes into canonical
SsuE-mediated FMN reduction and SsuD oxygenolysis, while retaining SsuE as an
optional family-specific supplier because another reductase can provide the
chemically required FMNH2 in some bacteria. Sulfite is a product at this
boundary; APS/PAPS-dependent sulfate assimilation and downstream sulfite
reduction remain separate biology.

The fresh generic OpenScientist run completed in 968 seconds. Its useful
boundary and mechanism synthesis was integrated as retrieval evidence, while
overgeneralized essentiality and flavin-transfer claims remain confined to the
generated report.
