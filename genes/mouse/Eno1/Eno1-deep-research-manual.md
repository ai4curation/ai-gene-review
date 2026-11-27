# Manual deep research for mouse Eno1

External deep-research providers were not run for this branch so the review could keep to a
single lightweight worker and the shared retained runtime. I manually checked the seeded mouse
GOA, the mouse P17182 UniProt record, the PTHR11902 enolase family review and PAINT cache, the
61e0e55600001225 and 62d0afa500000298 GO-CAM reviews, the cached publication records cited by
mouse GOA, and the cached papers behind the main human ENO1 transfers.

## Core reaction and GO-CAM context

Mouse Eno1 is the alpha-enolase isozyme. UniProt records the EC 4.2.1.11
2-phospho-D-glycerate/phosphoenolpyruvate dehydration reaction, and the PTHR11902 family review
places phosphopyruvate hydratase activity, the phosphopyruvate hydratase complex, and glycolysis
at the root PAINT node for the enolase family. This makes the cytosolic lower-glycolysis reaction
the core function.

The gluconeogenesis GO-CAMs 61e0e55600001225 and 62d0afa500000298 use Eno1 for the
phosphoenolpyruvate to 2-phosphoglycerate step. That chemistry is correct, and it chains Pck1
to Pgam1 through the expected metabolite. The cited PMID:30679508 evidence is not a direct
demonstration of this cytosolic step, though: Cho et al. study ENOblock-induced nuclear
translocation of enolase and repression of lipid and gluconeogenic transcriptional programs.
The GO-CAM inconsistency is therefore evidential rather than mechanistic.

## Moonlighting functions

Human ENO1 produces MBP-1, a short isoform that binds the human c-myc P2 promoter and represses
transcription (PMID:2005901). The follow-up domain paper maps MBP-1 repressor regions in the
N- and C-terminal parts of the protein and links those domains to cell-growth suppression
(PMID:10082554). A second follow-up identifies MIP-2A as an MBP-1 binding protein that relieves
MBP-1-mediated c-myc repression and colocalizes with MBP-1 primarily in the perinuclear membrane
(PMID:11134351). These annotations are plausible for mouse by orthology, but they are secondary
to the glycolytic enzyme function.

Cell-surface alpha-enolase is a plasminogen receptor. Anti-alpha-enolase antibody blocked most
cell-dependent plasminogen activation by human leukocytic cell lines, neutrophils, and monocytes
(PMID:12666133), and alpha-enolase was detected with H2B, annexin 2, and p11 at the surface of
mouse macrophage lines and induced mouse peritoneal macrophages (PMID:17690254). The human
positive-regulation-of-plasminogen-activation transfer and mouse cell-surface rows are therefore
kept as non-core.

## Rows left unresolved

The Six3OS RNA-binding paper (PMID:21936910) is full text in the local cache, but the visible
article text describes Six3OS binding to Ezh2 and Eya family members and does not identify Eno1.
The Eno1 RNA-binding row likely depends on a supplemental proteomic table, so I left it
UNDECIDED.

RGD rat Eno1 was the seed for several fine-grained location and binding rows. The current RGD
lookup failed for RGD:2553 and the cached mouse input does not expose those rat source
publications, so the cell-cortex, growth-cone, heat-shock-protein-binding,
protein-complex-binding, membrane-raft, and synaptic-membrane transfers are UNDECIDED. The
generic enzyme-binding row was supportable from the mouse beta-enolase paper that also reports
shared alpha-alpha isoenolase binding properties (PMID:9169614).

The IL-7 phosphoproteomics paper (PMID:29581031) names several induced tyrosine-phosphorylated
targets in the abstract but not Eno1, so the IL-7 response row is UNDECIDED until the hit can be
verified from the full dataset. The myelin proteome paper (PMID:17634366) verifies the purified
mouse myelin experiment but not the exact Eno1 peptide or protein hit in visible cached text, so
the myelin sheath row is also UNDECIDED.
