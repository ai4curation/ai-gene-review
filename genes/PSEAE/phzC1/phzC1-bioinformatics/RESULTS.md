# phzC1 (PA4212 / PA1901) bioinformatics: PAINT node PTN000481936

Scripts (run 2026-10-28; copied from the PA1054 analysis):

- `panther_node_composition.py PTHR21337 PTN000481936 Q7DC82 PTHR21337-tree.json ../../../../interpro/panther/PTHR21337/PTHR21337-paint.tsv`
  (PANTHER v19 `treeinfo` tree saved as `PTHR21337-tree.json`; output
  `panther_node_composition_output.txt`).
- `quickgo_node_checks.py GO:0002047 PTN000481936 Q7DC82` (live QuickGO; output
  `quickgo_node_checks_output.txt`).

## Findings (from the outputs)

- PTHR21337 has 186 leaves. The path runs root PTN000481914 (LUCA,
  PTHR21337:SF0) -> PTN002724389 (Eubacteria, 173) -> PTN004539259
  (HORIZ_TRANSFER, 170) -> PTN000481936 (Proteobacteria, 5 leaves in 4
  organisms).
- Leaves under PTN000481936: *Helicobacter pylori* HP_0134,
  *Bradyrhizobium diazoefficiens* blr3778, *Xanthomonas campestris* dhs1,
  *P. aeruginosa* phzC1 (PA1901) and *P. aeruginosa* PA2843. All are named
  "Phospho-2-dehydro-3-deoxyheptonate aldolase".
- IBDs relative to the node (local PAINT table): ANCESTOR PTN000481914
  GO:0003849 with two seeds (AGI_LocusCode:AT4G39980, UniProtKB:O53512); SELF
  PTN000481936 GO:0002047 with one seed (UniProtKB:Q7DC82, this gene), PAINT
  snapshot 20250225.
- GOA holds 5 GO:0002047 rows with PTN000481936 in with/from, all from
  GO_Central; there is no TreeGrafter propagation for this term at this node.
- A QuickGO check of the paralogue PA2843 (Q9I000) shows it carrying
  `involved_in GO:0002047` by IBA with with/from
  `PANTHER:PTN000481936|UniProtKB:Q7DC82`, alongside GO:0003849 and GO:0009073.

## Interpretation

The seeded claim is sound for phzC1 itself (the phz-operon DAH7PS), but the node
is a generic Proteobacteria DAHP synthase clade. Its other members are
housekeeping shikimate-pathway enzymes: *H. pylori*, *Xanthomonas* and
*Bradyrhizobium* make no phenazines, and PA2843 is *P. aeruginosa*'s own
primary-metabolism DAH7PS, which structural work distinguishes from the
phz-cluster enzyme by the presence of the alpha2a/alpha2b helices and by
allosteric regulation (PMID:30242059). The phenazine IBD therefore transfers a
pathway-specific role onto four enzymes that do not have it. The clade's correct
shared assertion, DAHP synthase activity, is already made at the family root.
