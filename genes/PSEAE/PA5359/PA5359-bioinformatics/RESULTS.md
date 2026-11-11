# PA5359 bioinformatics: PAINT node PTN002217427

Scripts (run 2026-10-28; copied from the PA1054 analysis):

- `panther_node_composition.py PTHR39335 PTN002217427 Q9HTJ9 PTHR39335-tree.json`
  (PANTHER v19 `treeinfo` tree saved as `PTHR39335-tree.json`; output
  `panther_node_composition_output.txt`). No local PAINT table exists for
  PTHR39335, so the optional IBD cross-check was not run.
- `quickgo_node_checks.py GO:0043448 PTN002217427 Q9HTJ9` (live QuickGO; output
  `quickgo_node_checks_output.txt`).

## Findings (from the outputs)

- PTN002217427 is the root of PTHR39335 (`is_family_root: True`), a Eubacteria
  speciation node with 7 leaves in 5 organisms, subfamily PTHR39335:SF1. The
  whole family is this node.
- Leaves: *Streptomyces coelicolor* SCO0930 and SCO7673 ("Lipoprotein"),
  *Gloeobacter violaceus* glr0303, *Bradyrhizobium diazoefficiens* bll4220 and
  bll5559, *Solanum lycopersicum* Solyc00g055940.1 ("Lipoprotein with
  Yx(FWY)xxD motif"), and *P. aeruginosa* PA5359 ("Lipoprotein"). None carries a
  name or definition related to alkane oxidation.
- GOA holds 764 GO:0043448 annotations with PTN002217427 in with/from: 7 from
  GO_Central (the reference leaves) and 757 from TreeGrafter.
- PA5359's own annotations are exactly two: GO:0043448 by IMP (PMID:14574114,
  PseudoCAP) and GO:0043448 by IBA from this node, with PA5359 itself as the
  with/from gene.
- A QuickGO query by reference shows PMID:14574114 is the source of one
  annotation in the whole database, the PseudoCAP IMP on Q9HTJ9. The five genes
  the paper's abstract describes - alkB1 PA2574, alkB2 PA1525, rubA1 PA5351,
  rubA2 PA5350, rubB/alkT PA5349 - carry GO:0043448 from UniProt keyword
  mapping (GO_REF:0000041), not from this paper.

## Interpretation

The node is a small, uncharacterised lipoprotein-repeat family (Pfam PF03640
Lipoprotein_15, PIRSF029720) whose members span actinobacteria, a
cyanobacterium, an alphaproteobacterium and a plant. Alkane catabolism needs an
alkane hydroxylase, rubredoxin and rubredoxin reductase; nothing in this family
supplies any of them, and a tomato protein cannot be performing bacterial alkane
degradation. The IBD rests on a single PseudoCAP row whose supporting paper is
not accessible here, and whose gene is absent from that paper's abstract while
sitting one digit away from the locus of the rubredoxin reductase the paper does
describe. The propagation is unsafe irrespective of how the seed is resolved.
