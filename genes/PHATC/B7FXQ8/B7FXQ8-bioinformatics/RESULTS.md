# B7FXQ8 (HSP20A) phylogenetic placement among small heat shock proteins

Script: `shsp_tree.py` (run with `uv run --with biopython python shsp_tree.py`);
raw output in `shsp_tree.out`; alignment `shsp_panel.aln.fasta`, ACD-trimmed
alignment `shsp_panel.acd.aln.fasta`, tree `shsp_panel.nj.nwk`.

## Method

Twenty sHSP sequences were fetched from UniProt: the target, six other
P. tricornutum sHSPs, two Thalassiosira pseudonana sHSPs that are in the
PANTHER tree (PTHR11527:SF175), eight experimentally characterised PTHR11527 or
archaeal sHSPs (yeast HSP26, S. pombe hsp16, Arabidopsis HSP17.6A and HSP17.7,
rice Hsp16.9A, wheat Hsp16.9B, M. tuberculosis HspX, M. jannaschii Hsp16.5), and
three sHSPs from other PANTHER families (human HSPB1 and CRYAB, PTHR45640;
E. coli IbpA, PTHR47062). They were aligned with MAFFT L-INS-i, trimmed to the
alignment columns of the target's alpha-crystallin domain (residues 47-155),
and a neighbour-joining tree was built from BLOSUM62 distances, rooted on IbpA.

## PANTHER context (checked by API, not computed here)

- InterPro assigns B7FXQ8 to PTHR11527 at family level only (no subfamily).
- PANTHER 19 does not include Phaeodactylum tricornutum as a genome, so B7FXQ8
  is not a leaf of the PTHR11527 tree and receives no IBA annotations.
- The PTHR11527 tree root is PTN000163021 (species LUCA). Its PAINT IBDs are
  protein folding (GO:0006457), response to heat (GO:0009408), response to salt
  stress (GO:0009651), response to hydrogen peroxide (GO:0042542) and protein
  complex oligomerization (GO:0051259). No molecular function is asserted at
  the root.
- The T. pseudonana sHSPs B8CD87 and B8BTA8 sit in PTHR11527:SF175 and carry all
  five root IBA terms in GOA.

## Results

ACD identity to B7FXQ8 (aligned positions):

| accession | protein | ACD identity |
|---|---|---|
| B8CD87 | T. pseudonana sHSP, PTHR11527:SF175 | 0.525 |
| B8BTA8 | T. pseudonana sHSP, PTHR11527:SF175 | 0.442 |
| B7G195 | P. tricornutum sHSP | 0.376 |
| O81822 | Arabidopsis HSP17.7 | 0.340 |
| P27777 | rice Hsp16.9A | 0.330 |
| O14368 | S. pombe hsp16 | 0.327 |
| Q9XIE3 | Arabidopsis HSP17.6A | 0.324 |
| P15992 | yeast HSP26 | 0.276 |
| P9WMK1 | M. tuberculosis HspX | 0.219 |
| P04792 | human HSPB1 (PTHR45640) | 0.196 |

In the NJ tree, B7FXQ8 groups with the T. pseudonana SF175 protein B8CD87.
Both fall in a cluster of diatom sHSPs, separate from the plant cytosolic
class I/II sHSPs and from the fungal/actinobacterial branch (HSP26, hsp16,
HspX). The tree has no bootstrap support and the deep branching among sHSP
lineages is poorly resolved. It therefore places B7FXQ8 with a diatom SF175
lineage, and no experimentally characterised protein falls inside that lineage.

The C-terminal I-X-I motif, which sHSPs use for oligomer assembly, is present
in the target as IAI at residues 150-152.

## Interpretation

- B7FXQ8 is a full-length sHSP (163 aa). It has a complete ACD (47-155), an
  N-terminal region rich in aromatic residues and a C-terminal extension that
  carries the IXI motif. Nothing suggests it is a fragment.
- Its closest placed relative is a T. pseudonana PTHR11527:SF175 protein, which
  is a descendant of PAINT root PTN000163021. The only experimentally
  characterised relatives are family-level relatives that share that root node,
  such as the plant cytosolic sHSPs and yeast HSP26. None of them is an
  ortholog.
- Functions that can be transferred are therefore limited to the family-root
  IBD set: client holdase behaviour of sHSPs, oligomerization and response to
  heat. Subfamily-specific properties of any characterised member cannot be
  transferred, such as compartment, stress-granule partitioning or
  osmotolerance phenotypes.
