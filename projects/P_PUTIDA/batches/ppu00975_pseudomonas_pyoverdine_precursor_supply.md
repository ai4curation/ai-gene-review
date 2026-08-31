---
title: "PSEPK pyoverdine precursor supply"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK pyoverdine precursor supply

- Module seed: `pseudomonas_pyoverdine_precursor_supply`
- Source bucket: `ppu00975` (biosynthesis of various siderophores)
- KEGG seed genes: 3
- Additional pathway gene recovered by hole filling: 1 (`pvdA`)

## Boundary

This batch tests a reusable precursor-supply submodule for pyoverdine rather
than treating the broad KEGG siderophore map as a complete pathway. The
candidate module contains parallel reactions that make or tailor unusual amino
acid building blocks before NRPS assembly. Ferribactin NRPS assembly,
cytoplasm-to-periplasm transport, periplasmic chromophore maturation,
pyoverdine secretion, ferripyoverdine uptake, and iron release are separate
modules.

KEGG seeds `pvdH`, `pvdY`, and PP_2800, but omits the established ornithine
N5-monooxygenase PvdA. PP_2800 is a distant locus paralog of the dedicated
cluster enzyme PvdH and is not accepted as a pyoverdine component from its EC
mapping alone. PvdY is included as an ortholog-supported hydroxyornithine
acetylation enzyme: PMID:16585778 characterizes the type II Pseudomonas
aeruginosa PvdYII enzyme, but leaves the free-versus-NRPS-bound acceptor state
open, while the precise PP_4245 reaction remains untested in KT2440. It is
curated as an adjacent tailoring gene, outside the strict two-reaction
precursor-supply module.

## Status

- [x] Fetch PvdY and PP_2800; existing PvdA and PvdH inputs were already present.
- [x] Complete and adjudicate four OpenScientist gene reports.
- [x] Define and research the reusable two-reaction module after paralog and boundary adjudication.
- [x] Curate or revise all four focused gene reviews.
- [x] Validate and render all artifacts.
- [x] Open one module PR: [#2808](https://github.com/ai4curation/ai-gene-review/pull/2808).
- [ ] Complete `/review` follow-up.

## Focused Genes

| Gene | Locus | UniProt | Provisional role | Current boundary |
|---|---|---|---|---|
| `pvdA` | PP_3796 | Q88GC8 | ornithine N5-hydroxylation | expected module component; absent from KEGG seed |
| `pvdH` | PP_4223 | Q88F75 | L-2,4-diaminobutyrate supply | expected module component |
| `pvdY` | PP_4245 | Q88F54 | hydroxyornithine acetylation | adjacent tailoring; direct KT2440 assay absent |
| `PP_2800` | PP_2800 | Q88J49 | class III PLP aminotransferase | likely KEGG paralog spillover |

The original three-gene KEGG inventory remains in
[`ppu00975_pseudomonas_pyoverdine_precursor_supply.tsv`](ppu00975_pseudomonas_pyoverdine_precursor_supply.tsv).

## Initial Paralog Evidence

- PvdH is `PANTHER:PTHR43552:SF1` and lies in the pyoverdine locus.
- PP_2800 is the distinct `PANTHER:PTHR43552:SF2` subfamily and lies in a
  separate catabolic locus adjacent to multiple aminotransferase and redox
  genes. These identifiers are used for paralog discrimination, not as a basis
  for assigning PP_2800 to pyoverdine biosynthesis.

## Satisfiability Result

| Module part | KT2440 implementation | Assessment |
|---|---|---|
| N5-hydroxy-L-ornithine supply | `pvdA` / PP_3796 / Q88GC8 | covered; omitted from the KEGG seed |
| L-2,4-diaminobutyrate supply | `pvdH` / PP_4223 / Q88F75 | covered; dedicated pyoverdine-locus paralog |

The reusable module is therefore satisfiable in KT2440 without invoking either
extra KEGG candidate. `PP_2800` retains only a broad class III transaminase
assignment pending physiological substrate evidence. `pvdY` is retained as a
pyoverdine-associated hydroxyornithine-tailoring enzyme by orthology to the
experimentally characterized type II *P. aeruginosa* PvdYII, but tailoring is
outside this precursor-forming boundary.

This result is supported by both the generic module report and the independent
target-specific KEGG bucket satisfiability report:

- [`pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist.md`](../../../modules/pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist.md)
- [`PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist.md`](../deep-research/PSEPK__pseudomonas_pyoverdine_precursor_supply__ppu00975-deep-research-openscientist.md)
