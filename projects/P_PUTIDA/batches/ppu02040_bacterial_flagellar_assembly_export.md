---
title: "PSEPK bacterial flagellar assembly and export"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fliA, flgM, flhA, fliP, fliI, fliF, fliG, flgG, flgE, fliK, flgK, fliC, fliD, motA, motB]
autolink_gene_symbols: false
---

# PSEPK bacterial flagellar assembly and export

- Module: `bacterial_flagellar_assembly_export`
- Source bucket: KEGG `ppu02040` (flagellar assembly)
- Focused reviews: 15 proteins spanning six architectural parts
- Additional grounded exemplars: 12 export, switch, rod, and junction proteins
- Satisfiability: six-part architecture covered; full 47-protein realization not yet curated
- OpenScientist module/pathway/taxon research: complete

## Boundary

This module covers basal-body and switch assembly, type III export, rod-hook
construction and length control, late transcriptional staging, filament
completion, and stator installation. It is a representative architectural panel
rather than a claim that all 47 KEGG proteins have been curated. Chemotactic
regulation of motor bias is modeled separately.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| MS ring and switch | FliF Q88ET4, FliG Q88ET5, FliM Q88EU5, FliN Q88EU6 | Covered |
| Type III export | FlhA Q88EV8, FlhB Q88EV1, FliP/Q/R Q88EU8/Q88EU9/Q88EV0, FliH/I/J Q88ET6/Q88ET7/Q88ET8 | Covered panel; FliO not modeled |
| Rod-hook and length control | FlgB/C/F/G Q88ER2/Q88ER3/Q88ER7/Q88ER8, FlgD Q88ER4, FlgE Q88ER5, FliK Q88EU2 | Covered panel; rings/caps remain outside focus |
| Late transcription checkpoint | FliA Q88EW1 and FlgM Q88EQ8 | Covered panel; upstream FleQ/FleSR/FleN circuit not modeled |
| Filament completion | FlgK/L Q88ES2/Q88ES3, FliC Q88ES5, FliD Q88ES7 | Covered panel; chaperones not modeled |
| Stator installation | MotA Q88DC2 and MotB Q88DC3 | Covered as a complex |

## Curation Findings

Structural subunits are not assigned whole-complex molecular functions. FliI is
the catalytic export ATPase; en bloc flagellar construction and chemotactic
switching are not conflated. Exact PSEPK proteins are exemplars for reusable
gammaproteobacterial families rather than species-specific module requirements.
The FliA/FlgM checkpoint now follows rod-hook construction, reflecting export
of FlgM after hook-basal-body completion, and the invalid export-gate `PART_OF`
MS-ring edge has been removed.

The OpenScientist report independently finds all six architectural parts
represented. It also identifies the `fliY` cystine-transporter name collision,
the need to distinguish the two Pseudomonas stator systems, and the larger
FleQ/FleSR/FleN regulatory circuit as follow-up work rather than evidence that
the focused panel is a complete 47-protein pathway model.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_flagellar_assembly_export__ppu02040-deep-research-openscientist.md)
- `modules/bacterial_flagellar_assembly_export.yaml`
