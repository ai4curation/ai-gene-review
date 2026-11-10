# phzM bioinformatics: PAINT node PTN002463933 (GO:0008757 SAM-dependent methyltransferase activity)

Scripts (run 2026-10-28):

- `panther_node_composition.py PTHR43712 PTN002463933 Q9HWH2 <tree.json> interpro/panther/PTHR43712/PTHR43712-paint.tsv`
  (PANTHER v19 `treeinfo` tree; output `panther_node_composition_output.txt`)
- `quickgo_node_checks.py GO:0008757 PTN002463933 Q9HWH2,Q4WQZ4,C8VQ72`
  (live QuickGO; output `quickgo_node_checks_output.txt`)

## Findings (from the outputs)

- PTN002463933 is the root of the PTHR43712 tree (LUCA speciation node,
  is_family_root: True), 80 reference-genome leaves in 16 organisms.
- Root children: a Eukaryota clade (75 leaves) and a Eubacteria clade
  (5 leaves: phzM, Shewanella SO_2905, Streptomyces SCO7452, Gloeobacter
  gll0305 and one more).
- The eukaryotic leaves are nearly all "O-methyltransferase" proteins: fungal
  secondary-metabolite O-methyltransferases (gliM, ftmMT, xanE, tpcA, asqD,
  asqN, cicE, sterigmatocystin 8-O-methyltransferase), horse ASMT
  (acetylserotonin O-methyltransferase), amphioxus ASMT-like, Klebsormidium
  O-methyltransferase family proteins.
- The only other IBD in the v19 tree relative to the node is a descendant,
  PTN000922397 GO:0044550 secondary metabolite biosynthetic process (5 seeds,
  Aspergillus).
- The local PAINT table also lists PTN000202149 IBDs (GO:0008171, GO:0008757,
  GO:0009058, GO:0032259) seeded by plant and mammalian O-methyltransferases,
  but PTN000202149 does not occur in the v19 PTHR43712 tree; these rows look
  stale or belong to another family version.
- GOA holds 64 GO:0008757 IBA rows with with/from PTN002463933.
- Two leaves that inherit the IBA are described in UniProt as cluster
  transcriptional coactivators, not methyltransferases: Aspergillus fumigatus
  tpcD (Q4WQZ4) and A. nidulans mdpA (C8VQ72). Both receive GO:0008757 IBA
  from PTN002463933 (QuickGO output).

## Interpretation

GO:0008757 is the right level for this node. The clade contains O-methylating
enzymes (most members) and at least one N-methylating enzyme (PhzM, which
methylates N5 of PCA), so GO:0008171 O-methyltransferase activity would be
wrong at the root, and a PhzM-specific term would be wrong for the clade. The
seed claim is directly supported for PhzM (PMID:17253782). The tpcD and mdpA
coactivators may be non-catalytic members; whether they lost catalytic
residues was not checked here (no MSA), so this is only a flag.

Limitations: reference-genome leaves only; no MSA or SAM-motif conservation
analysis; QuickGO counts change with GOA releases.
