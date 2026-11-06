# PA1056 (ShaD) bioinformatics: PAINT node PTN001865541

Scripts (run 2026-10-28; copied from the PA1055 analysis):

- `panther_node_composition.py PTHR42703 PTN001865541 Q9I4R8 PTHR42703-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR42703-tree.json`;
  output `panther_node_composition_output.txt`). No local PAINT table exists
  for PTHR42703, so the optional IBD cross-check was not run.
- `quickgo_node_checks.py GO:0015385 PTN001865541 Q9I4R8,O05229` and
  `quickgo_node_checks.py GO:0035725 PTN001865541 Q9I4R8`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN001865541 is not the family root. The PTHR42703 root (PTN000511965,
  LUCA, 28 leaves) splits into an Archaea-Eukaryota node and PTN001865541, a
  Eubacteria speciation node with 16 leaves in 13 organisms.
- GOA holds 16 GO:0015385 and 16 GO:0035725 IBA rows with with/from
  PTN001865541, all assigned by GO_Central.
- GO:0015385 has two seeds: O05229 (B. subtilis MrpD, IMP, PMID:20509166) and
  Q9I4R8 (PA1056, PseudoCAP IMP, PMID:16030218). GO:0035725 has one seed,
  Q9I4R8.
- Leaves under the node: MrpD/MnhD/ShaD/PhaD (B. subtilis mrpD, S. aureus
  mnhD1, mnhD2, Geobacter mrpD, Coxiella shaD, Xanthomonas phaD, Vibrio
  VC_A0155, lmo2381), plus Caur_2216, SCO6956, Thermotoga TM_1105 and TM_1211,
  Rhodopirellula RB1430 and RB1431 and Leptospira LA_4273 ("Formate
  hydrogenase subunit B").
- The archaeal MBH/MBX subunits of this family (Thermococcus TK2087 MbhH,
  TK1220 MbxH, TK1219 MbxH') and archaeal NuoL/M-like proteins sit in the
  Archaea-Eukaryota clade, outside PTN001865541.

## Interpretation

The node is restricted to bacterial MrpD-type subunits, so the MBH
hydrogenase subunits do not receive these IBAs. The Leptospira
formate-hydrogenase-named leaf, the duplicated Thermotoga and Rhodopirellula
pairs are possible non-antiporter members. The activity belongs to the Mrp
complex; MrpD contributes to it.
