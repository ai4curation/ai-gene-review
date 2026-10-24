---
title: "PSEPK bacterial LPS transport"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [lptA, lptB, lptC, lptD, lptE, PP_0982, PP_0983]
autolink_gene_symbols: false
---

# PSEPK bacterial LPS transport

- Module: `bacterial_lps_transport`
- Source bucket: KEGG `ppu00540` (lipopolysaccharide biosynthesis)
- Focused genes: seven proteins spanning three trans-envelope machines
- Satisfiability: complete
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch starts with extraction of completed LPS from the inner membrane and
ends with insertion into the outer leaflet of the outer membrane. Lipid A, core
oligosaccharide, and O-antigen synthesis are upstream. PP_0982 and PP_0983 are
the KT2440 LptF and LptG permease subunits despite lacking standard gene symbols
in the UniProt record.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Inner-membrane LptB2FGC extractor | LptB Q88P99, LptC Q88P97, PP_0982/LptF Q88P71, PP_0983/LptG Q88P70 | Covered |
| Periplasmic bridge | LptA Q88P98 | Covered |
| Outer-membrane translocon | LptD A0A140FVZ0, LptE Q88DN0 | Covered |

## Curation Findings

The module keeps ATP hydrolysis as a direct LptB molecular function and treats
LPS transport as a process performed by the assembled trans-envelope system.
LptF/LptG are represented as the membrane cavity, LptC/LptA as the bridge, and
LptD/LptE as the outer-membrane endpoint. This avoids assigning the entire
transport operation as an independently enabled function of every structural
subunit.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-lps-transport-and-outer-membrane-assembly__ppu00540-deep-research-openscientist.md)
- `modules/bacterial_lps_transport.yaml`
