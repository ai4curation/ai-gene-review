# phzS bioinformatics: PAINT node PTN002492679 (GO:0004497 monooxygenase activity)

Scripts (run 2026-10-28):

- `panther_node_composition.py PTHR13789 PTN002492679 Q9HWG9 <tree.json> interpro/panther/PTHR13789/PTHR13789-paint.tsv`
  (PANTHER v19 `treeinfo` tree; output `panther_node_composition_output.txt`)
- `quickgo_node_checks.py GO:0004497 PTN002492679 Q9HWG9,Q55087`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN002492679 is the root of the PTHR13789 tree (LUCA speciation node,
  is_family_root: True), 104 reference-genome leaves in 19 organisms.
  It is the only IBD in the local PTHR13789 PAINT table, and its only seed is
  Q9HWG9 (PhzS).
- Root children: a Eukaryota clade (88 leaves; mostly fungal "salicylate
  hydroxylase, putative", FAD-binding monooxygenases such as fmqB and mdpD,
  diatom, Chlamydomonas, kinetoplastid and Klebsormidium "zeaxanthin
  epoxidase" proteins) and a bacterial duplication node (16 leaves).
- Path to PhzS: root > PTN002674159 (duplication) > PTN000350393 (Eubacteria,
  SF318) > PTN002301285 (duplication) > PTN002301286 (Proteobacteria, SF268)
  > phzS. The SF268 clade otherwise holds only uncharacterised
  Bradyrhizobium and Phaeosphaeria proteins.
- GOA (QuickGO, exact term, with/from PTN002492679) holds 3507 GO:0004497 IBA
  rows from this node across UniProt.
- Synechocystis chlP (Q55087, geranylgeranyl diphosphate reductase) is a leaf
  under PTN000350393 and receives the GO:0004497 IBA from this node, although
  its own InterPro/EC-based annotations are geranylgeranyl reductase activity
  (GO:0102067) and UniProt's current PANTHER cross-reference places it in
  PTHR42685, not PTHR13789.

## Interpretation

The node term is the generic class A flavoprotein monooxygenase activity, the
right level for a LUCA-rooted family of FAD_binding_3 aromatic hydroxylases
with diverse substrates. A PhzS-specific term (GO:0102169) would be wrong for
the clade. The seed claim (PhzS is an NAD(P)H/FAD monooxygenase) is true on
independent evidence (PMID:17253782 activity assays; PMID:18416536 structure),
although the PseudoCAP row cites a crystallization note with no activity
assay. The chlP leaf is a likely exception: a reductase of the same
FAD-binding fold, which should not inherit monooxygenase activity. This is a
point about one leaf's placement (or a NOT annotation for it), not about the
node.

Limitations: no MSA or active-site residue analysis was done; reference
genome leaves only; QuickGO counts change with each GOA release.
