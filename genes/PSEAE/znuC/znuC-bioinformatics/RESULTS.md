# znuC (PA5500) bioinformatics: PAINT node PTN001952271

Scripts (run 2026-10-28; copied from the PA1054 analysis):

- `panther_node_composition.py PTHR42734 PTN001952271 Q9HT73 PTHR42734-tree.json`
  (PANTHER v19 `treeinfo` tree saved as `PTHR42734-tree.json`; output
  `panther_node_composition_output.txt`). No local PAINT table exists for
  PTHR42734, so the optional IBD cross-check was not run.
- `quickgo_node_checks.py GO:0010043 PTN001952271 Q9HT73` (live QuickGO; output
  `quickgo_node_checks_output.txt`).

## Findings (from the outputs)

- PTHR42734 has 90 leaves. The path to the node runs root PTN002448841 ->
  PTN009164625 (LUCA, 32 leaves) -> PTN009164626 -> PTN001953439 (Eubacteria,
  29) -> PTN009164628 (Proteobacteria, 10) -> PTN002533586 -> PTN001952271
  (Gammaproteobacteria, 7 leaves in 7 organisms, subfamily PTHR42734:SF9).
- Leaves under PTN001952271: znuC of *Haemophilus influenzae* (HI_0408),
  *Vibrio cholerae* (VC_2082), *Salmonella* Typhimurium (STM1892),
  *Yersinia pestis* (YP_1903), *Escherichia coli*, *P. aeruginosa* (PA5500),
  and one *Nematostella vectensis* "ABC transporter domain-containing protein
  (Fragment)".
- GOA holds 1455 GO:0010043 annotations with PTN001952271 in with/from: 7 from
  GO_Central (the reference leaves) and 1448 from TreeGrafter.
- The target's own annotations include GO:0010043 by IBA (this node, with
  Q9HT73 itself) and by IMP (PMID:24086521); GO:0042626 and GO:0043190 by IBA
  from the family root PTN002448841 with donor P06611 (*E. coli* BtuD, the
  vitamin B12 importer ATPase); GO:0015633 by IEA from EC 7.2.2.20 /
  RHEA:29795; GO:0071577 and GO:0055085 by IEA (GO_REF:0000108).

## Interpretation

The node is a clean ZnuC clade, so propagation is not the problem; the term is.
The node's IBD term, GO:0010043 response to zinc ion, comes from a single
seed - this gene's PseudoCAP IMP row, which rests on a growth defect in
EDTA-chelated medium. For an importer's ATPase subunit the supported process is
zinc import across the plasma membrane (GO:0071578). The family-root IBA for
GO:0042626 has an unrelated donor (BtuD), which is why that row is generic; the
specific ABC-type zinc transporter activity (GO:0015633) is already present from
the curated EC number.
