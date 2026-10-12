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
- Module research: not run for this batch
- Gene-level OpenScientist research: complete for lpxA only

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
| Late secondary acylation | HtrB Q88M40, PP_0063 Q88RR6 | Covered; both positions experimentally assigned |

## Curation Findings

The module separates four substantive biosynthetic parts and places each
molecular function on the enzyme that catalyzes the corresponding step. KdsA1
and KdsA2 are modeled as alternative exemplars of one conserved family role,
without assuming equal in-vivo contribution. Both late acyltransferases are
position-specific: PP_0063 installs 2-OH-C12:0 at the 2-position and PP_1735
(HtrB/LpxL, Q88M40) installs C12:0 at the 2'-position, established by deletion
plus reciprocal overexpression and ESI/MS of the isolated lipid A
(PMID:28557109). That work used strain KT2442 rather than KT2440, the strain of
these accessions. No GO molecular-function child yet describes 2-position
2-OH-lauroyl transfer, so PP_0063 keeps the generic acyltransferase parent while
HtrB carries GO:0008913.

## Evidence

- [PMID:28557109](https://pubmed.ncbi.nlm.nih.gov/28557109/) — Identification of
  two secondary acyltransferases of lipid A in *Pseudomonas putida* KT2442
- OpenScientist report for lpxA: `genes/PSEPK/lpxA/lpxA-deep-research-openscientist.md`
  (gene-folder deep research is not rendered into `pages/`, so this is a path
  rather than a link)
- `modules/bacterial_lipid_a_biosynthesis.yaml`
