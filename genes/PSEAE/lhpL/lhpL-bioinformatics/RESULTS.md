# lhpL (PA1255) bioinformatics: PAINT node PTN002433936

Scripts (run 2026-10-28; copied from the PA1054 analysis):

- `panther_node_composition.py PTHR33442 PTN002433936 Q9I489 PTHR33442-tree.json ../../../../interpro/panther/PTHR33442/PTHR33442-paint.tsv`
  (PANTHER v19 `treeinfo` tree saved as `PTHR33442-tree.json`; output
  `panther_node_composition_output.txt`).
- `quickgo_node_checks.py GO:0047580 PTN002433936 Q9I489` (live QuickGO; output
  `quickgo_node_checks_output.txt`).

## Findings (from the outputs)

- PTN002433936 is an internal DUPLICATION node of PTHR33442. The family root is
  PTN002530875 (Eubacteria speciation, 48 leaves); the path runs root ->
  PTN008001402 (HORIZ_TRANSFER, 45 leaves) -> PTN002433936 (9 leaves, 7
  organisms).
- The only IBD of PTHR33442 relative to this node is the node's own
  GO:0047580 IBD, with one seed (`UniProtKB:Q9I489`, snapshot 20180110).
- Leaves under the node: *Korarchaeum cryptofilum* Kcr_0803, *Chloroflexus
  aurantiacus* Caur_2964, *Bacillus cereus* BC_2834, BC_0905 and BC_2835,
  *Nematostella vectensis* NEMVEDRAFT_v1g67963 (annotated
  "trans-L-3-hydroxyproline dehydratase (Fragment)"), *Streptomyces coelicolor*
  SCO6293, *Clostridium botulinum* prdF, and *P. aeruginosa* lhpL. Most are
  named "Proline racemase"; BC_0905 is named "Trans-3-hydroxy-L-proline
  dehydratase".
- GOA holds 35 GO:0047580 annotations with PTN002433936 in with/from: 9 from
  GO_Central (the reference leaves), 24 from TreeGrafter and 2 from UniProt.
- The target's own annotations: GO:0047580 by IBA (from this node), IEA
  (ARBA00044834) and IMP (PMID:27145750); GO:0050346 by EXP (PMID:27929065) and
  IEA (RHEA:10320 / EC 4.2.1.77).

## Interpretation

The node is a coherent proline-racemase-family clade, and two of its nine leaves
(lhpL itself and the *Nematostella* fragment, plus *B. cereus* BC_0905 by name)
are already associated with trans-3-hydroxy-L-proline dehydratase activity. The
problem is the term, not the clade: GO:0047580 is the *4*-hydroxyproline
reaction, which UniProt records as experimentally absent for Q9I489, while
GO:0050346 (the 3-hydroxy dehydratase) is the activity the seed gene actually
has. The IBD should be re-pointed to GO:0050346; the 35 propagated rows include
TreeGrafter transfers outside the reference set.
