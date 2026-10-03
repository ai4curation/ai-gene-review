# CTNNA1 bioinformatics: PANTHER node placement of alpha-catenin IBAs

Script: `panther_nodes.py` (queries the public PANTHER v19 tree API; raw output in
`panther_nodes.out`, generated 2026-10-01).

## Question

Human CTNNA1 IBA rows (beta-catenin binding, actin filament binding, catenin complex,
adherens junction, cell-cell adhesion, cell migration) all cite PANTHER node
PTN001052343. Where is that node, and does it include the Dictyostelium
alpha-catenin (ctnnA, Q54MH2, dictyBase DDB_G0285939) or any unicellular holozoan?

## Results (from panther_nodes.out)

- PTHR18914 (ALPHA CATENIN) root is PTN001052343, taxon range Eumetazoa, 85 leaves.
  Leaf organisms include Nematostella vectensis and bilaterians only; no sponge,
  choanoflagellate, filasterean or amoebozoan sequence is in this family tree.
- Human CTNNA1 (P35221) descends from PTN001052343 (Eumetazoa) > PTN000431715
  (Bilateria) > ... > Homo-Pan.
- PTHR46180 (VINCULIN) root is PTN005285701, taxon range Unikonts, 49 leaves,
  including Dictyostelium discoideum, D. purpureum, Entamoeba histolytica,
  Batrachochytrium dendrobatidis and Monosiga brevicollis.
- Dictyostelium ctnnA (Q54MH2, "Ddalpha-catenin") is classified in PTHR46180, not in
  PTHR18914: PTN005285701 (Unikonts) > PTN005285703 (Amoebozoa) > PTN005285707
  (Dictyostelium). Human VCL descends from the same root via the
  Metazoa-Choanoflagellida node PTN001052341.

## Interpretation

The CTNNA1 IBAs are placed at a eumetazoan node, so they assert inheritance only
within animals, which is compatible with all the experimental donors. The
Dictyostelium alpha-catenin-like protein, which binds the beta-catenin-related
protein Aardvark and F-actin, sits in the PANTHER vinculin family. Its
beta-catenin-type binding therefore reaches human VCL (beta-catenin binding IBA at
PTN005285701), not CTNNA1. PANTHER does not put the animal alpha-catenin clade and
the amoebozoan protein in one family. Whether Dd ctnnA is orthologous to animal
alpha-catenin or to the vinculin/alpha-catenin ancestor is not settled by this
classification.
