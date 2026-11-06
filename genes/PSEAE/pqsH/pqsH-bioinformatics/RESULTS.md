# pqsH bioinformatics: composition of PAINT node PTN008173107

Script: `panther_node_composition.py` (downloads the PANTHER v19 tree for
PTHR45934 from the pantherdb.org `treeinfo` service, or reads a cached copy).
Raw output: `panther_node_composition_output.txt` (run on 2026-10-28).

## Findings (from the script output)

- PTN008173107, the node carrying the GO:0004497 monooxygenase activity IBD
  seeded only by PqsH, is the root of the PTHR45934 tree (is_family_root: True),
  with 297 leaves in 41 genera.
- Root children: one Emericella nidulans leaf (ANIA_08131) and a
  HORIZ_TRANSFER node (PTN005262028, 296 leaves).
- The horizontal-transfer node has three children: P. aeruginosa pqsH
  (PTN002301282), Streptomyces coelicolor SCO1338 (putative monooxygenase), and a
  Viridiplantae clade of 294 leaves (PTN000350346).
- So 294 of the 297 leaves are green-plant proteins (Eucalyptus 30, Triticum 26,
  Helianthus 21, ... Arabidopsis MO1, MO2, MO3, CTF2A, CTF2B). PqsH is the only
  bacterial protein with experimental data, and the only seed.

## Interpretation

The IBD stays at the generic "monooxygenase activity" level, which is the
activity shared by FAD-dependent class A aromatic hydroxylases (Pfam
FAD_binding_3, InterPro IPR044560 MOase). That is the right level for a node at
the family root. A PqsH-specific term (GO:0102164, HHQ 3-monooxygenase) would be
wrong here, because the plant clade has no reason to hydroxylate
2-alkylquinolones. The node placement is plausible on structural grounds, but no
experimental annotation for any plant member was used. The ~294 plant IBAs
therefore rest on one horizontally transferred bacterial lineage. That is a
statement about where the evidence comes from, not a demonstration that the
node is wrong.

Limitations: the script does not inspect MSAs or catalytic-residue
conservation in the plant clade, and it does not check whether plant members
have their own experimental GO annotations in current GOA.
