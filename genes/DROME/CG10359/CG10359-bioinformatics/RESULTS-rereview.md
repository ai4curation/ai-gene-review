# CG10359 (B7Z0B2) re-review: isoform identity and FReD phylogenetic placement

Analysis date: 2026-10-20. Scripts: `isoform_compare_rereview.py` (section 1) and `fred_tree_rereview.py` (section 2), each run with `uv run --script <name>`.
Outputs: `fred_rereview.fa`, `fred_rereview.aln.fa`, `fred_rereview_nj.nwk`, `fred_rereview_results.tsv`.

## 1. Isoform identity

UniProt holds four unreviewed entries for FlyBase FBgn0035452 (CG10359); there is no reviewed (Swiss-Prot) entry.
B7Z0B2 (485 aa) is the longest product. Compared with B7Z0B2 by sequence alignment (difflib opcodes, 0-based):

| Entry | Length | Difference from B7Z0B2 |
|---|---|---|
| B7Z0B3 | 459 | lacks B7Z0B2 residues 144-169 (26 aa internal segment) |
| Q9VZN7 | 460 | one extra N-terminal residue; lacks the same 26 aa segment |
| Q95S38 | 460 | as Q9VZN7 plus two single-residue substitutions (cDNA clone) |

All four carry a predicted signal peptide and one Fibrinogen C-terminal domain (PROSITE PS51406; B7Z0B2 263..477).
None carries a predicted transmembrane segment. B7Z0B2 is therefore a full-length isoform of the gene, not a fragment;
the alternative segment lies in the N-terminal region upstream of the FReD and removes no annotated domain.

## 2. Phylogenetic placement of the FReD

PANTHER 19.0 places B7Z0B2 in PTHR19143:SF327 ("FI21813P1-RELATED"), a subfamily whose PANTHER members are eight
D. melanogaster proteins and one C. elegans protein (Q5ZR75); no vertebrate protein and no experimentally
characterised protein is in SF327. Human FIBCD1 (Q8N539) is in PTHR19143:SF45 (vertebrate members only), and human
FCN1 (O00602) is in PTHR19143:SF377.

FReD-only MAFFT (L-INS-i) alignment of 26 sequences, BLOSUM62 distances, neighbour-joining, midpoint-rooted.
The CG10359 FReD groups with its SF327 fly paralogs Q8IRM2 and Q9W302 inside a cluster of insect FReDs
(SF327 + SF458), separate from the clade containing FIBCD1, MFAP4 and the ficolins. This is a single-domain
distance tree without bootstrap support, so deep branching order is not resolved; it is consistent with, and adds
nothing beyond, the PANTHER subfamily split.

Pairwise identity of the CG10359 FReD (aligned columns only), top values from `fred_rereview_results.tsv`:

| Sequence | Identity |
|---|---|
| AAF46535 (Q9W302, SF327) | 0.456 |
| AAF52372 (Q9VME7, SF458) | 0.451 |
| AAF59068 (A1Z7G6, SF327) | 0.442 |
| FIBCD1_HUMAN (Q8N539, SF45) | 0.413 |
| MFAP4_HUMAN (P55083) | 0.404 |
| FGL1_HUMAN (Q08830) | 0.404 |
| FCN1_HUMAN (O00602, SF377) | 0.382 |
| ANGPT1_HUMAN (Q15389) | 0.389 |

FIBCD1 is no closer to CG10359 than MFAP4 or FGL1, and the ficolin FCN1 is about as distant as angiopoietin-1.
The FReD identity profile gives no ortholog-level signal linking CG10359 specifically to FIBCD1 or to ficolins.

## Interpretation (limits)

- CG10359 belongs to an insect/nematode FReD subfamily without characterised members.
- Functions specific to the FIBCD1 subfamily (type II transmembrane anchoring, acetyl-group/chitin receptor) or to
  ficolins (collagen-like domain lectins, GPR43 docking) cannot be transferred on phylogenetic grounds.
- The analysis does not test whether CG10359 binds acetylated ligands; binding-pocket residues were not examined.
