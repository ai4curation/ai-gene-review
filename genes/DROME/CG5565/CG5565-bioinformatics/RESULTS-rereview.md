# CG5565 PANTHER tree placement (re-review, 2026-10-20)

Script: `panther_tree_rereview.py` (run with `just panther-tree-rereview`). It downloads the PANTHER 19 PTHR18901 tree from the pantherdb.org treeinfo service (saved as `panther_tree_rereview/PTHR18901-tree.json`), walks root-to-leaf paths for the requested genes, and intersects each path with the PAINT IBD rows in `interpro/panther/PTHR18901/PTHR18901-paint.tsv`. Raw stdout is in `panther_tree_rereview/output.txt`; structured output in `panther_tree_rereview/results.json`.

## Findings

CG5565 (FlyBase:FBgn0031335) descends from PTN000431252 (Unikonts), the node carrying the PAINT IBD for GO:1990738 pseudouridine 5'-phosphatase activity seeded by human PUDP and yeast YKL033W-A.

The CG5565 leaf path runs through a Diptera duplication node, PTN000431298, that also gives rise to the fly paralogs CG5561, CG5556, CG5564 and Gs1l; all five fly genes inherit both the GO:0016791 IBD at PTN000431251 and the GO:1990738 IBD at PTN000431252.

Human PUDP (HGNC:16818) descends from the same PTN000431252 node; its leaf subfamily SF43 arises only after a Catarrhini duplication (PTN004500568), while mouse Pudp remains SF38. The SF38 (CG5565) versus SF43 (human PUDP) label difference therefore reflects a recent primate-lineage split, not a deep divergence separating the fly gene from the characterised mammalian enzyme.

The plant glycerol-3-phosphatase IBD (GO:0043136) and mitochondrion IBD (GO:0005739) sit at PTN008360158 in the bikont/plant lineage and are not inherited by CG5565.

## Limitations

The GOA snapshot for CG5565 (and for human PUDP itself) carries only the GO:0016791 IBA from PTN000431251; the GO:1990738 IBD at PTN000431252 is dated 20260729 and has not yet propagated to GOA. The tree establishes descent from the annotated node; it cannot show whether one or more of the five post-duplication fly paralogs has diverged in substrate preference. No fly paralog has been assayed biochemically.
