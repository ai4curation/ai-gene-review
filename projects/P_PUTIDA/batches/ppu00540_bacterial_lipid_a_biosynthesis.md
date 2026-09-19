---
title: "PSEPK bacterial lipid A biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [lpxA, lpxC, lpxD, lpxH, lpxB, lpxK, kdsD, kdsA1, kdsA2, kdsC, kdsB, waaA, htrB, PP_0063]
autolink_gene_symbols: false
---

# PSEPK bacterial lipid A biosynthesis

- Module: `bacterial_lipid_a_biosynthesis`
- Source bucket: KEGG `ppu00540` (lipopolysaccharide biosynthesis)
- Focused genes: 14 proteins spanning four biosynthetic parts
- Satisfiability: complete, with two KdsA-family paralogs
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch follows core synthesis from UDP-N-acetylglucosamine through
Kdo-decorated, secondarily acylated lipid A. It excludes downstream LPS core and
O-antigen glycosylation, LPS transport, and post-synthetic lipid A remodeling by
PagL or LpxO-family enzymes. FabZ supplies hydroxyacyl-ACP shared with fatty-acid
synthesis and is treated as an upstream precursor-supply enzyme, not a dedicated
lipid A pathway step.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Early UDP-glucosamine acylation | LpxA Q88MG8, LpxC Q88N71, LpxD Q88MH0 | Covered |
| Lipid-disaccharide formation | LpxH Q88IU7, LpxB Q88MG7, LpxK Q88LM9 | Covered |
| Kdo synthesis and transfer | KdsD Q88P95, KdsA1 Q88MG0/KdsA2 Q88LX0, KdsC Q88P96, KdsB Q88LM7, WaaA Q88D99 | Covered |
| Late secondary acylation | HtrB Q88M40, PP_0063 Q88RR6 | Covered; PP_0063 acceptor specificity unresolved |

## Curation Findings

The module separates four substantive biosynthetic parts and places each
molecular function on the enzyme that catalyzes the corresponding step. KdsA1
and KdsA2 are modeled as alternative exemplars of one conserved family role,
without assuming equal in-vivo contribution. PP_0063 is retained as a late
acyltransferase-family component while its exact KT2440 acceptor specificity
remains open.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-lipid-a-biosynthesis__ppu00540-deep-research-openscientist.md)
- `modules/bacterial_lipid_a_biosynthesis.yaml`
