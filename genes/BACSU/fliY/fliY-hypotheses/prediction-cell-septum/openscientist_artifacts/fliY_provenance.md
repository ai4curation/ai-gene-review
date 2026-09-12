# fliY (P24073) — Computed Provenance (Iteration 2)

## A. InterPro domain map (EBI InterPro API, live query)

Protein length: 378 aa. No cell-division (FtsZ/FtsA/SepF/DivIVA/SPOR) domains detected.

| Source | Accession | Name | Type | Start | End |
|---|---|---|---|---|---|
| InterPro | IPR051469 | Flagellar motor switch protein FliN/MopA/SpaO | family | 1 | 378 |
| NCBIfam | NF005995 | **flagellar motor switch phosphatase FliY** | family | 3 | 374 |
| InterPro | IPR028976 | CheC-like superfamily | homologous_superfamily | 31 | 228 |
| CDD | cd17907 | flagellar motor switch protein FliY | domain | 33 | 223 |
| Pfam | PF04509 | CheC-like family (active site lobe 1) | domain | 36 | 72 |
| Pfam | PF04509 | CheC-like family (active site lobe 2) | domain | 133 | 169 |
| InterPro | IPR036429 | SpoA-like superfamily (= T3SS SPOA, *not* sporulation) | homologous_superfamily | 287 | 378 |
| InterPro | IPR012826 | Flagellar motor switch FliN | family | 295 | 370 |
| SSF | SSF101801 | Surface presentation of antigens (SPOA) | homologous_superfamily | 295 | 376 |
| Pfam | PF01052 | Type III flagellar switch regulator (C-ring) FliN C-term | domain | 298 | 368 |

**Architecture:** N/central CheC-like phosphatase module (~31–228, two catalytic lobes) + C-terminal FliN C-ring domain (~295–378). Consistent with a CheY-P phosphatase fused to a flagellar C-ring building block.

## B. STRING functional-partner network (STRING v12, species 224308, top 30)

**All 30 highest-confidence partners are flagellar (fli/flg/flh) or chemotaxis (che) genes. Zero cell-division genes (no ftsZ, ftsA, ftsW, sepF, divIVA, divIB, zapA, minCD).**

cheV, ylxF(fliW-region), fliR, fliZ, fliH, fliQ, fliL, flhB, fliP, flhA, fliI, flgE, flgD, fliG, fliK, fliE, flgC, cheD, fliF, cheC, flgB, flgK, fliD, cheY, fliM, fliS, cheA, cheB, cheW, flhO — all score ≥ 0.998.

Key neighbors: **fliM, fliG, fliF (MS-ring), cheY, cheC** — the exact C-ring / switch / CheY-P signaling machinery. This is diagnostic of flagellar-switch localization, not the divisome.

## C. Interpretation for the cell-septum (GO:0030428) prediction

Both independent computed lines (domain content and interaction neighborhood) place fliY squarely in the flagellar switch / C-ring, corroborating the primary literature. **The cell-septum prediction is refuted.** The likely model-error source is the "SpoA-like" superfamily label (SPOA = Surface Presentation Of Antigens, a T3SS export-apparatus fold) being conflated with sporulation/septation, and/or a generic "ring at the membrane" analogy with the FtsZ division ring.
