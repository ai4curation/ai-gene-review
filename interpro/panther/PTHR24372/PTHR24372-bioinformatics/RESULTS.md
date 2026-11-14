# PTHR24372 members on the PANTHER 19 trees, and the PAINT nodes that reach them

## Question

The PAINT slice for PTHR24372 (`PTHR24372-paint.tsv`) holds 28 node rows on 11 nodes.
Several of those nodes carry Slit-family or other leucine-rich-repeat-family seeds
(SLIT1/2/3, TLR3, GP1BA, CD180, LINGO1 and others), which is unexpected for the
glycoprotein hormone receptor family. The slice is built from the leaf IBA file, so a
node enters it when any member listed in `PTHR24372-entries.csv` carries an IBA from
it. This analysis asks three things: which subfamilies lie below each annotated node
of the PTHR24372 tree; which reviewed members are actually leaves of that tree; and,
for each reviewed member, which PANTHER nodes its IBA annotations come from.

## Method

`lgr_tree_placement.py` loads the PTHR24372 and PTHR45836 (SLIT HOMOLOG) trees from
the PANTHER treeinfo API through `ai_gene_review.etl.panther_trees`, reads the
family's PAINT slice and member table, and queries QuickGO for the IBA annotations
(ECO:0000318) of the 56 reviewed members. Run from the repository root:

```
uv run python interpro/panther/PTHR24372/PTHR24372-bioinformatics/lgr_tree_placement.py
```

Raw output is in `output.txt` (run 2026-11-14, PANTHER 19.0 trees).

## Results

### Tree structure

The root PTN000689980 (398 leaves) has three main branches, matching the three LGR
types described in the literature:

- PTN001224575 (90 leaves): SF0 TSHR, SF1 LHCGR and SF5 FSHR, which together form the
  vertebrate node PTN001556595, plus SF74 (invertebrate glycoprotein hormone
  receptors: Drosophila Lgr1, C. elegans fshr-1, Nematostella, Trichoplax and others).
- PTN008402522 (59 leaves): the vertebrate LGR4/5/6 node PTN002542418 (SF67 LGR4,
  SF71 LGR5, SF73 LGR6) plus SF82 (Drosophila rickets and its invertebrate orthologs).
- PTN001224607 (249 leaves): the relaxin-family receptor node PTN001970551 (SF68
  RXFP1, SF72 RXFP2, SF70 and the arthropod/deuterostome SF80, including Drosophila
  Lgr3 and Lgr4) plus SF77, 185 invertebrate orphan receptors from Trichoplax, sea
  urchin, Nematostella, Ciona and amphioxus.

The LGR6 clade is PTN002809239 (14 leaves, SF73 only).

### Annotated nodes outside the PTHR24372 tree

Five of the 11 annotated nodes in the slice are not internal nodes of the PTHR24372
tree: PTN001224703, PTN001556510, PTN002809265, PTN002911625 and PTN002911633. Their
rows entered the slice because six reviewed LGR4 or LGR6 entries carry IBAs from them.

### Tree membership of reviewed members

36 of the 56 reviewed members are leaves of the PTHR24372 tree. Of the other 20, 14 are
from species with no leaf in the tree (sheep, marmoset, crab-eating macaque, hamster,
guinea pig, donkey, wallaby, Muscovy duck, channel catfish, orangutan, the sea anemone
Anthopleura and the snail Lymnaea) and carry no IBA in QuickGO. The remaining six are
LGR4 or LGR6 entries of species that do have leaves in the tree; InterPro and UniProt
classify them in PTHR24372:SF67 or SF73, but they sit elsewhere in the PANTHER 19 trees:

- Human LGR6 (Q9HBX8), mouse Lgr4 (A2ARI4) and rat Lgr4 (Q9Z2H4) are leaves of the
  PTHR45836 tree, as PTHR45836:SF19 and PTHR45836:SF10.
- Bovine LGR4 (F1MLX5), zebrafish lgr4 (E7FE13) and mouse Lgr6 (Q3UVD5) are leaves of
  neither tree.

Their orthologs human LGR4 (Q9BXB1), Xenopus lgr4 (B0BLW3) and zebrafish lgr6 (P0DM44)
are leaves of the PTHR24372 tree.

### Where each member's IBAs come from

- Human LGR6, mouse Lgr4 and rat Lgr4 receive IBAs only from three PTHR45836 nodes:
  negative chemotaxis (PTN001556510), axon guidance (PTN002911625), and heparin binding
  and Roundabout binding (PTN002911633).
- Bovine LGR4, zebrafish lgr4 and mouse Lgr6 receive IBAs only from two nodes outside
  the PTHR24372 tree: plasma membrane (PTN001224703) and signaling receptor activity
  (PTN002809265).
- The in-tree LGR4 and LGR5 orthologs receive plasma membrane from the root and positive
  regulation of canonical Wnt signaling from their clade nodes, and nothing else: the
  IRDs at PTN002809225 and PTN002809236 stop the three root receptor and signaling terms.
- Zebrafish lgr6 (P0DM44) receives GO:0008528, GO:0007189 and GO:0009755 from the root,
  because no IRD sits on the LGR6 clade PTN002809239, and receives no Wnt term.
- Every in-tree TSHR, LHCGR, FSHR, RXFP1 and RXFP2 ortholog receives the four root terms;
  the glycoprotein hormone receptors also receive their clade-specific receptor activity
  and pathway terms.

## Interpretation

Orthologs of one gene receive different IBA sets depending on which PANTHER tree their
sequence landed in: mouse and rat Lgr4 inherit Slit functions that human and Xenopus
LGR4 do not. That is a tree-membership problem in PANTHER rather than a node-placement
judgement by a PAINT curator, so it is not fixable by moving or pruning nodes in the
PTHR24372 tree alone.
