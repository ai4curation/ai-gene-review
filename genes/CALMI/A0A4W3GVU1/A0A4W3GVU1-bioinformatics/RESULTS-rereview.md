# A0A4W3GVU1 (Callorhinchus milii esrp1): phylogenetic placement (re-review, 2026-10-21)

Script: `esrp_phylogeny_rereview.py` (raw output in `esrp_phylogeny_rereview.out`; alignment
`esrp_members_rereview.aln.fasta`; tree `esrp_members_rereview.nwk`).

Method: UniProt sequences of the target and 12 PTHR13976 members (ESRP1 and ESRP2 from
human, mouse, zebrafish, Xenopus; Drosophila fusilli; human HNRNPF, HNRNPH1, GRSF1, RBM12)
were aligned with MAFFT (--auto). Identity was computed over columns where both sequences
are ungapped; a neighbour-joining tree was built from identity distances and rooted on RBM12.
This is a quick distance tree, not a maximum-likelihood phylogeny.

## Results

- Target length 684 aa; human ESRP1 (Q6NXG1) is 681 aa, mouse Esrp1 (Q3US41) 680 aa. The
  target aligns over 679 columns of human ESRP1, so it is a full-length product, not a fragment.
- Identity of the target: mouse Esrp1 78.3%, human ESRP1 77.9%, Xenopus esrp1 75.8%;
  human ESRP2 59.5%, mouse Esrp2 58.7%; Drosophila fusilli 44.1%; HNRNPF/HNRNPH1 31.4%
  (over only ~340-370 columns), GRSF1 27.3%, RBM12 22.1%.
- In the NJ tree the target groups with tetrapod ESRP1 (Xenopus, mouse, human), inside the
  ESRP clade (ESRP1 + ESRP2, sister to fusilli) and outside the hnRNP H/F + GRSF1 clade.
  The two zebrafish sequences branch at the base of the vertebrate ESRP group, so the tree does
  not resolve teleost esrp1/esrp2 orthology; this does not affect the target's placement.
- UniProt's PANTHER cross-reference gives only the family (PTHR13976) for the target, not a
  subfamily. Its placement with tetrapod ESRP1 is consistent with PTHR13976:SF37 (EPITHELIAL
  SPLICING REGULATORY PROTEIN 1, which contains human ESRP1 and mouse Esrp1 in the PANTHER 19.0
  classifications), and it falls under the PAINT nodes PTN001018050 (mRNA binding, IBD,
  seeds fusilli/ESRP1/ESRP2) and PTN000360053 (RNA binding, regulation of RNA splicing,
  nucleoplasm).

## Interpretation

The target is the elephant shark ESRP1 ortholog, not an ESRP2 or hnRNP H/F relative.
Functions established experimentally for mammalian ESRP1 and propagated by PAINT at the ESRP
clade node (mRNA binding; regulation of RNA splicing; nuclear localisation) can be transferred.
Subfamily-specific downstream phenotypes (e.g. craniofacial development in mouse knockouts)
are not annotated here.
