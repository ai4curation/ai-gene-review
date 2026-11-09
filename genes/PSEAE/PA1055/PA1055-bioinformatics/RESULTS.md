# PA1055 (ShaC) bioinformatics: PAINT node PTN002160376

Scripts (run 2026-10-28):

- `panther_node_composition.py PTHR34583 PTN002160376 Q9I4R9 PTHR34583-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR34583-tree.json`;
  output `panther_node_composition_output.txt`)
- `quickgo_node_checks.py GO:0015385 PTN002160376 O05260,Q2FZV3,Q9I4R9` and
  `quickgo_node_checks.py GO:0035725 PTN002160376 Q9I4R9`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN002160376 is the root of the PTHR34583 tree (LUCA speciation node,
  is_family_root: True): 24 leaves in 19 organisms. Its children are a
  duplication node with 6 leaves and a Eubacteria node with 18 leaves.
- GOA holds 24 GO:0015385 IBA rows and 24 GO:0035725 IBA rows with with/from
  PTN002160376; the only seed listed is Q9I4R9 (PA1055).
- Most leaves are Mrp/Mnh/Pha subunit C proteins of Na+/H+ antiporter
  operons (B. subtilis mrpC O05260, S. aureus mnhC1 Q2FZV3 and mnhC2,
  Halobacterium mrpC, Methanosarcina mrpC, Geobacter mrpC, Xanthomonas phaC,
  Thermococcus TK0624 "MnhC subunit").
- The node also contains subunits of archaeal membrane-bound hydrogenase-type
  complexes, Thermococcus kodakaraensis TK2086 "Membrane bound hydrogenase,
  MbhG subunit" and TK1221 "Membrane bound hydrogenase, MbxG subunit", plus
  Chloroflexus Caur_2215 (named "NADH-ubiquinone oxidoreductase chain 4L") and
  several uncharacterised proteins (MJ1310, RB1432, VC_A0156, slr2006, slr2008).
- Neither B. subtilis MrpC (O05260) nor S. aureus MnhC1 (Q2FZV3) has an
  experimental GO annotation in QuickGO; both receive GO:0015385 only by IBA
  from this node. PA1055 (Q9I4R9) carries the PseudoCAP IMP rows for
  GO:0015385 and GO:0035725 (PMID:16030218).

## Interpretation

The node is the whole subunit-C family. A Na+/H+ antiporter subunit role fits
the Mrp operon members, but the activity belongs to the hetero-oligomeric
complex, so `contributes_to` is the right qualifier for a subunit. Leaves
from MBH/MBX-type complexes do not form a stand-alone antiporter. In the
Pyrococcus MBH structure (PMID:29754813) the Mrp-like module translocates Na+,
which is consistent with GO:0035725, but it does so as part of a hydrogenase
complex. The sole seed is a PseudoCAP IMP row, although the cited paper
disrupted only PA1054 (shaA).
