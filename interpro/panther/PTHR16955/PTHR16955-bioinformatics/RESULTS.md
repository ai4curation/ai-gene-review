# PTHR16955 members on the PANTHER tree, and the PAINT nodes that reach them

## Question

The PAINT slice for PTHR16955 (`PTHR16955-paint.tsv`) holds four IBD rows, all on one
node, PTN002704209, with taxon 117571 (Euteleostomi). This analysis asks which proteins
sit below that node, which internal node separates the mammalian KISS1 orthologs from the
single non-mammalian leaf, and from which PANTHER node the reviewed members and zebrafish
kiss1 receive their IBA annotations.

## Method

`kiss1_tree_placement.py` loads the PTHR16955 tree from the PANTHER treeinfo API through
`ai_gene_review.etl.panther_trees`, reads the family's PAINT slice and member table, and
queries QuickGO for the IBA annotations (ECO:0000318) of the four reviewed members plus
zebrafish kiss1 (A8C5J1). Run from the repository root:

```
uv run python interpro/panther/PTHR16955/PTHR16955-bioinformatics/kiss1_tree_placement.py
```

Raw output is in `output.txt` (run 2026-11-14).

## Results

### Tree structure

The tree has 15 leaves and 14 internal nodes, and every leaf is in subfamily SF6
(METASTASIS-SUPPRESSOR KISS-1). The root is PTN002704209, the node that carries all four
PAINT rows, so the IBDs cover the whole family.

The leaves are KISS1 orthologs of 14 mammals (human, chimpanzee, gorilla, two rhesus
macaque entries, mouse, rat, dog, cat, horse, cow, two opossum entries and platypus) and
one fish, zebrafish kiss1 (A8C5J1, leaf PTN001048170). No zebrafish kiss2 sequence is a
leaf of this tree.

PTN000424419 (14 leaves) holds every leaf except zebrafish kiss1, so it is the mammalian
KISS1 node. Its child PTN000424420 (13 leaves) leaves out platypus as well.

### PAINT rows

All four rows sit at the root PTN002704209 and reach all 15 leaves:

| GO term | Seeds |
|---|---|
| GO:0005576 extracellular region | rat Kiss1 (RGD:727850), human KISS1 (Q15726) |
| GO:0031773 kisspeptin receptor binding | rat Kiss1, zebrafish kiss1 (ZFIN:ZDB-GENE-080128-1) |
| GO:0007186 G protein-coupled receptor signaling pathway | mouse Kiss1 (MGI:2663985), rat Kiss1, human KISS1 |
| GO:0033686 positive regulation of luteinizing hormone secretion | rat Kiss1 |

The slice has no IRD or IKR rows.

### IBA provenance

Human KISS1 (Q15726), rhesus KISS1 (Q5PXH1), mouse Kiss1 (Q6Y4S4), rat Kiss1 (Q7TSB7) and
zebrafish kiss1 (A8C5J1) each carry the same four IBA rows in QuickGO, and every row cites
PTN002704209. No member receives an IBA from any other node of this tree.

## Limitations

The tree and the QuickGO rows are the current public releases at the run date. The
analysis says where the PAINT rows are placed and what they reach. It says nothing about
whether the functions are right, which is judged from the literature in
`PTHR16955-review.yaml`.
