# PA1054 (ShaAB) bioinformatics: PAINT node PTN000511949

Scripts (run 2026-10-28; copied from the PA1055 analysis):

- `panther_node_composition.py PTHR43373 PTN000511949 Q9I4S0 PTHR43373-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR43373-tree.json`;
  output `panther_node_composition_output.txt`). No local PAINT table exists
  for PTHR43373, so the optional IBD cross-check was not run.
- `quickgo_node_checks.py GO:0015385 PTN000511949 Q9I4S0,Q9K2S2` and
  `quickgo_node_checks.py GO:0035725 PTN000511949 Q9I4S0`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN000511949 is the root of the PTHR43373 tree (LUCA speciation node,
  is_family_root: True): 16 leaves in 15 organisms. Its children are an
  Archaea node (2 leaves) and a Eubacteria node (14 leaves).
- GOA holds 16 GO:0015385 IBA rows and 16 GO:0035725 IBA rows with with/from
  PTN000511949, all assigned by GO_Central.
- GO:0015385 has two seeds: Q9I4S0 (PA1054, PseudoCAP IMP, PMID:16030218) and
  Q9K2S2 (B. subtilis MrpA, IMP, PMID:20509166). GO:0035725 has one seed,
  Q9I4S0 (PA1054).
- Leaves are MrpA/MnhA/ShaA proteins (B. subtilis mrpA, S. aureus mnhA1 and
  mnhA2, Geobacter mrpA, Coxiella shaA, Methanosarcina mrpA, Vibrio VC_A0157,
  Xanthomonas ndhF), plus loosely named Mrp-like proteins (Caur_2213,
  SCO6954, DR_0880, THEYE_A1118, blr7320, lmo2378) and Sulfolobus SSO1021,
  named "Formate hydrogenlyase subunit 3 (HycC)".
- No Thermococcus MBH/MBX subunit is in this family (none listed among the
  leaves).

## Interpretation

The node is the MrpA family. Archaeal MBH has no MrpA homologue
(PMID:29754813), consistent with the absence of MBH leaves. The one
hydrogenase-named leaf (SSO1021 HycC) is a caveat for a Na+/H+ antiporter MF.
The antiporter IBD has an independent B. subtilis seed in addition to PA1054;
the Na+ transport IBD rests on PA1054 alone. Both are activity of the Mrp
complex, to which MrpA contributes.
