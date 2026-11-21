# PA1057 (ShaE) bioinformatics: PAINT node PTN002160407

Scripts (run 2026-10-28):

- `panther_node_composition.py PTHR34584 PTN002160407 Q9I4R7 PTHR34584-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR34584-tree.json`;
  output `panther_node_composition_output.txt`)
- `quickgo_node_checks.py GO:0015385 PTN002160407 Q7WY60,Q2G2H8,Q9I4R7` and
  `quickgo_node_checks.py GO:0035725 PTN002160407 Q9I4R7`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN002160407 is the root of the PTHR34584 tree (LUCA speciation node,
  is_family_root: True): 20 leaves in 17 organisms. Its children are a
  Euryarchaeota node with 5 leaves and a Eubacteria node with 15 leaves.
- GOA holds 20 GO:0015385 IBA rows and 20 GO:0035725 IBA rows with with/from
  PTN002160407; the only seed listed is Q9I4R7 (PA1057).
- Most leaves are Mrp/Mnh/Pha subunit E proteins of Na+/H+ antiporter
  operons (B. subtilis mrpE Q7WY60, S. aureus mnhE1 Q2G2H8 and mnhE2,
  Halobacterium and Methanosarcina mrpE, Geobacter mrpE, Coxiella shaE,
  Xanthomonas phaE, Thermococcus TK0618 "MnhE subunit").
- The node also contains Thermococcus kodakaraensis TK2080 "Membrane bound
  hydrogenase, MbhA subunit" and TK1226 "Membrane bound hydrogenase, MbxA
  subunit", subunits of hydrogenase-type complexes.
- Neither B. subtilis MrpE (Q7WY60) nor S. aureus MnhE1 (Q2G2H8) has an
  experimental GO annotation in QuickGO; both receive GO:0015385 only by IBA
  from this node. PA1057 (Q9I4R7) carries the PseudoCAP IMP rows for
  GO:0015385 and GO:0035725 (PMID:16030218).

## Interpretation

As for subunit C (PA1055), the Na+/H+ antiport activity is a property of the
Mrp complex; MrpE is a small subunit that is needed for complex assembly and
full activity in B. pseudofirmus but reported dispensable for transport in
B. subtilis. `contributes_to` is the right qualifier for this family. The
MBH/MBX subunit A leaves are part of hydrogenase complexes rather than
stand-alone antiporters. The sole seed is a PseudoCAP IMP row, although the
cited paper disrupted only PA1054 (shaA).
