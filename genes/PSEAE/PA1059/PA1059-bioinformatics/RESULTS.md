# PA1059 (ShaG) bioinformatics: PAINT node PTN002162936

Scripts (run 2026-10-28; copied from the PA1055 analysis):

- `panther_node_composition.py PTHR34703 PTN002162936 Q9I4R5 PTHR34703-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR34703-tree.json`;
  output `panther_node_composition_output.txt`). No local PAINT table exists
  for PTHR34703, so the optional IBD cross-check was not run.
- `quickgo_node_checks.py GO:0015385 PTN002162936 Q9I4R5,O05227` and
  `quickgo_node_checks.py GO:0035725 PTN002162936 Q9I4R5`
  (live QuickGO; output `quickgo_node_checks_output.txt`; the script also
  counts the node's rows by assigning group)

## Findings (from the outputs)

- PTN002162936 is the root of the PTHR34703 tree (LUCA speciation node, is_family_root: True):
  19 leaves in 16 organisms, split into a Euryarchaeota node (4 leaves) and a
  Eubacteria node (15 leaves).
- GOA holds GO:0015385 IBA rows with with/from PTN002162936: 19 assigned by GO_Central
  (the reference-tree leaves) plus several hundred assigned by TreeGrafter
  (exact counts in the output file). The only seed listed is Q9I4R5 (PA1059).
- There is no GO:0035725 IBA from this node (0 rows); the PA1059 GO:0035725 IMP
  row seeds no IBD.
- B. subtilis MrpG (O05227) has no experimental GO:0015385 annotation; it gets
  the term only by IBA from this node.
- Most leaves are MrpG/MnhG/PhaG/ShaG proteins of Mrp operons. The node also
  contains the Thermococcus kodakaraensis membrane-bound hydrogenase subunits
  TK2082 "Membrane bound hydrogenase, MbhC subunit" and TK1224 "Membrane bound hydrogenase, MbxC subunit".

## Interpretation

The node is the whole subunit-G family. A contribution to Na+/H+ antiport
fits the Mrp operon members, but the activity belongs to the hetero-oligomeric
complex. MBH/MBX complexes are redox-driven hydrogenases with an Mrp-like
Na+-translocating module (PMID:29754813), not stand-alone Na+/H+ antiporters.
The sole seed is a PseudoCAP IMP row, although the cited paper disrupted only
PA1054.
