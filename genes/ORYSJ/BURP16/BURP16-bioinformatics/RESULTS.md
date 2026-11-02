# OsBURP16 (Q7XES5) family placement and motif analysis (2026-10-21)

Script: `burp16_family_analysis.py` (run with
`uv run --no-project --with biopython python burp16_family_analysis.py`); raw output
in `burp16_family_analysis.out`. Data are fetched live from the PANTHER treeinfo API
(PANTHER 19, PTHR31458) and UniProt REST. Independent of any ProtNLM2 output.

## 1. PANTHER tree placement

Q7XES5 is a PANTHER 19 reference leaf in PTHR31458:SF2. Its ancestor path is
Tracheophyta PTN007882607 > Magnoliophyta PTN000779096 > Mesangiosperma PTN004827825 >
Liliopsida PTN004827826 > commelinids PTN004827828 > duplication PTN002050022 >
Poaceae PTN002050027 > BEP clade PTN002050028 > duplication PTN000779097 > leaf
PTN000779098.

Only two leaves lie below the grass duplication node PTN000779097: OsBURP16
(Q7XES5, Os10g0409400) and OsBURP12 (Q6ZA27, Os08g0380100). OsBURP12 is therefore
the in-paralog of OsBURP16 created by a grass-lineage duplication. No eudicot member
(tomato GP1 Q40161, Arabidopsis PGL1/PGL2/PGL3) shares a node with OsBURP16 below the
Mesangiosperma speciation node PTN004827825, so none is a one-to-one ortholog.

Q7XES5 does not descend from PTN004827911 (under_PTN004827911=False), the only node in
PTHR31458 that carries PAINT IBD annotations (GO:0009505 plant-type cell wall,
GO:0009827 plant-type cell wall modification, GO:0042547 cell wall modification
involved in multidimensional cell growth; seed AT1G70370). PAINT curators therefore
did not propagate these terms to the grass PG1beta-like lineage, and GOA holds no
IBA rows for Q7XES5.

## 2. Motifs

| acc | protein | length | F[TS]xYG | FxxY | CH dipeptides |
|---|---|---|---|---|---|
| Q7XES5 | OsBURP16 | 344 | 0 | 0 | 260, 272, 301, 328 |
| Q6ZA27 | OsBURP12 | 627 | 4 | 22 | 545, 557, 586, 613 |
| Q6K2M1 | OsBURP14 | 690 | 2 | 22 | 19, 608, 620, 649, 676 |
| Q40161 | tomato GP1 (PG1 beta) | 630 | 6 | 21 | 548, 560, 589, 616 |
| O80760 | AtPGL2 | 624 | 5 | 21 | 542, 554, 583, 610 |
| P92990 | AtPGL3 | 626 | 7 | 21 | 544, 556, 585, 612 |
| P92982 | AtPGL1 | 622 | 5 | 21 | 540, 552, 581, 608 |

OsBURP16 keeps the four CH dipeptides of the C-terminal BURP domain at the spacing
seen in all comparators (CH-x10-CH-x27-CH-x25-CH), but it lacks the entire
repeat-rich variable region (the FTNYG / FxxY units that make up most of the mature
tomato PG1 beta subunit). The OsBURP16 protein is a signal peptide (1-25), a ~100-residue
N-terminal segment and the BURP domain (UniProt 128-341).

## 3. Global identity to Q7XES5

| acc | protein | identity over aligned pairs | identity over Q7XES5 length |
|---|---|---|---|
| Q6ZA27 | OsBURP12 | 0.532 | 0.526 |
| Q6K2M1 | OsBURP14 | 0.526 | 0.520 |
| Q40161 | tomato GP1 | 0.501 | 0.491 |
| O80760 | AtPGL2 | 0.485 | 0.471 |
| P92990 | AtPGL3 | 0.491 | 0.483 |
| P92982 | AtPGL1 | 0.478 | 0.465 |

Global identities are inflated by gaps over the absent repeat region and are roughly
similar for all comparators; they do not resolve orthology, which is read from the
tree above.

## 4. Interpretation

- OsBURP16 is a PG1beta-like BURP protein by PANTHER subfamily (SF2) and BURP-domain
  architecture, with a predicted signal peptide, consistent with secretion.
- It lacks the FTNYG repeat region that is the defining structural feature of the
  tomato PG1 beta subunit, so a PG1 beta-like mechanism (repeat-mediated anchoring of
  PG2 to the wall) cannot be assumed to be conserved.
- Its only close relative is the grass in-paralog OsBURP12; eudicot PG1beta-like
  proteins diverged at the monocot-eudicot split.
