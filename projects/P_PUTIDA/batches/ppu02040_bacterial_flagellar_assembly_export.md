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
- Focused genes: 15 proteins spanning six architectural parts
- Satisfiability: complete at the representative-part level
- OpenScientist module and gene research: running

## Boundary

This module covers transcriptional staging, type III export, basal-body and
switch assembly, rod-hook construction and length control, filament completion,
and stator installation. It uses representative essential components rather
than duplicating all members of the 47-gene KEGG locus. Chemotactic regulation
of motor bias is modeled separately.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Late transcription checkpoint | FliA Q88EW1 and FlgM Q88EQ8 | Covered |
| Type III export | FlhA Q88EV8, FliP Q88EU8, FliI Q88ET7 | Covered |
| MS ring and switch | FliF Q88ET4 and FliG Q88ET5 | Covered |
| Rod-hook and length control | FlgG Q88ER8, FlgE Q88ER5, FliK Q88EU2 | Covered |
| Filament completion | FlgK Q88ES2, FliC Q88ES5, FliD Q88ES7 | Covered |
| Stator installation | MotA Q88DC2 and MotB Q88DC3 | Covered as a complex |

## Curation Findings

Structural subunits are not assigned whole-complex molecular functions. FliI is
the catalytic export ATPase; en bloc flagellar construction and chemotactic
switching are not conflated. Exact PSEPK proteins are exemplars for reusable
bacterial families rather than species-specific module requirements.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-flagellar-assembly-export__ppu02040-deep-research-openscientist.md)
- `modules/bacterial_flagellar_assembly_export.yaml`
