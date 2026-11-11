# phnB (PA1002) bioinformatics: PAINT node PTN000230115

Scripts (run 2026-10-28; copied from the PA1054 analysis):

- `panther_node_composition.py PTHR43418 PTN000230115 P09786 PTHR43418-tree.json ../../../../interpro/panther/PTHR43418/PTHR43418-paint.tsv`
  (PANTHER v19 `treeinfo` tree saved as `PTHR43418-tree.json`; output
  `panther_node_composition_output.txt`).
- `quickgo_node_checks.py GO:0002047 PTN000230115 P09786` and
  `quickgo_node_checks.py GO:0004048 PTN000230115 P09786` (live QuickGO; output
  `quickgo_node_checks_output.txt`).

## Findings (from the outputs)

- PTHR43418 has 154 leaves. The path to the node runs root PTN002880935 ->
  PTN000230074 (LUCA, 149 leaves, subfamily PTHR43418:SF4) -> PTN000230100
  (Eubacteria, 45) -> PTN000230112 (Proteobacteria, 20) -> PTN000230119 ->
  PTN000230115 (Gammaproteobacteria, 7 leaves in 7 organisms, PTHR43418:SF2).
- Leaves under PTN000230115: trpG of *Haemophilus influenzae* (HI_1388),
  *Shewanella oneidensis* (SO_3020), *Vibrio cholerae* (VC_1173) and
  *Yersinia pestis* (YP_2005); the bifunctional TrpGD of *Salmonella*
  Typhimurium (STM1724) and *Escherichia coli*; and *P. aeruginosa* phnB
  (PA1002).
- IBDs relative to the node (from the local PAINT table):
  - ANCESTOR PTN000230074 GO:0004049 (2 seeds: SGD:S000001694, UniProtKB:P00904)
  - ANCESTOR PTN000230074 GO:0000162 (8 seeds)
  - SELF PTN000230115 GO:0004048 (1 seed: UniProtKB:P00904)
  - SELF PTN000230115 GO:0002047 (1 seed: UniProtKB:P09786, this gene)
- GOA holds 267 rows for GO:0002047 and 267 for GO:0004048 with PTN000230115 in
  with/from: 7 from GO_Central and 260 from TreeGrafter in each case.
- Target annotations: GO:0004049 by IMP (PMID:2153661) and IEA (ARBA, RHEA:21732,
  EC 4.1.3.27); GO:0002047 by IMP and IBA; GO:0004048 by IBA; GO:0000162 by IBA
  from the ancestor node.

## Interpretation

Two independent problems at this node.

1. **Phenazine biosynthesis on non-phenazine producers.** The GO:0002047 IBD is
   sole-seeded by phnB and reaches the TrpG/TrpGD proteins of *E. coli*,
   *Salmonella*, *Haemophilus*, *Yersinia*, *Vibrio* and *Shewanella*, none of
   which make phenazines. Even for phnB the term is indirect: PhnAB supplies
   anthranilate for PQS, and PQS induces the phz genes, while the phenazine core
   is built from chorismate by PhzE without an anthranilate intermediate.
2. **A fusion-protein artefact.** The GO:0004048 IBD is sole-seeded by
   *E. coli* P00904, a 531-residue bifunctional TrpGD in which the
   phosphoribosyltransferase activity comes from the fused TrpD region. phnB is
   200 residues and consists of a single glutamine amidotransferase domain
   (PROSITE PS51273, residues 2-195), so it cannot have that activity; the same
   applies to the other standalone TrpG leaves.

The ancestral node's GO:0004049 anthranilate synthase and GO:0000162 tryptophan
biosynthesis IBDs are better founded (2 and 8 seeds) and are not challenged here.
