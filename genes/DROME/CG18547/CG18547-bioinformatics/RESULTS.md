# CG18547 (Q9VGF3) bioinformatics: PANTHER tree placement and AKR tetrad

Scripts (run with `uv run <script>`): `panther_tree_placement.py` (output
`panther_tree_placement.out`) and `tetrad_check.py` (output `tetrad_check.out`).
Both fetch live data (PANTHER treeinfo API, UniProt REST); nothing is hard-coded
except the reference positions in O81884, which come from its UniProt record.

## Tree placement (PANTHER 19, PTHR42686)

- CG18547 path: PTN002448388 (LUCA, SF1 root) > PTN005126602 > PTN000199432 (Eukaryota)
  > PTN000199433 (Opisthokonts) > PTN000920361 (Metazoa-Choanoflagellida) > PTN000920362 (Eumetazoa)
  > PTN000199434 (Bilateria) > PTN000199440 (Ecdysozoa) > PTN002869781 (Endopterygota)
  > PTN000199444 (Diptera) > PTN000199437 (DUPLICATION) > Q9VGF3.
- The Drosophila duplication node PTN000199437 contains three paralogs: CG18547 (Q9VGF3),
  CG3397 (Q9VGF1) and CG12224 (Q9VGF2). Mosquito AGAP011125 and Tribolium TC014368 are outgroups.
- LCA with C. elegans mec-14 (Q20127) is PTN000199440 (Ecdysozoa, speciation): mec-14 is a
  co-ortholog of the three fly paralogs.
- LCA with yeast ARA2 (Q04212) is PTN000199433 (Opisthokonts); ARA2 sits in the fungal clade
  PTN000920371 (Dikarya).
- LCA with Arabidopsis LGALDH (O81884) is PTN000199432 (Eukaryota); LGALDH sits in the
  land-plant clade PTN000920391 (Embryophyta).
- No vertebrate leaf occurs in the Bilateria clade (tunicate, amphioxus, sea urchin,
  nematodes, insects only): the gene is absent from human/mouse.

PAINT context (QuickGO, checked 2026-10-21): GO:0010349 L-galactose dehydrogenase activity
is propagated to O81884 from PTN000920391 (plant node), and ARA2's D-arabinose
dehydrogenase / dehydro-D-arabinono-1,4-lactone biosynthesis IBAs come from PTN000920371
(fungal node). CG18547 receives only GO:0016491 oxidoreductase activity from the SF1 root
PTN002448388. Neither specific function was placed at a node ancestral to CG18547.

## AKR catalytic tetrad (global pairwise alignment, BLOSUM62)

| O81884 (LGALDH) | CG18547 (Q9VGF3) | ARA2 (Q04212) |
|---|---|---|
| Asp54 | Asp71 | Asp53 |
| Tyr59 (proton donor, UniProt ACT_SITE) | Tyr76 | Tyr58 |
| Lys87 | Lys102 | Lys86 |
| His124 (substrate binding, UniProt BINDING) | His143 | His124 |

Identity over aligned positions: CG18547 vs LGALDH 42.6% (133/312);
ARA2 vs LGALDH 34.3% (104/303). CG18547 retains the complete Asp-Tyr-Lys-His tetrad,
so it is expected to be a catalytically competent AKR. Retention of the tetrad says
nothing about substrate: L-galactose, D-arabinose, D-threo-aldose and pyridoxal
dehydrogenases in the same subfamily all carry it.
