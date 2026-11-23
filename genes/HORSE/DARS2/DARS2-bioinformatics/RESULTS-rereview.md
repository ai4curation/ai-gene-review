# DARS2 (horse) re-review: gene-model identity and phylogenetic placement

Date: 2026-10-20. Independent of any ProtNLM2 output.

## Inputs and scripts

- `dars2_models-rereview.fasta`: UniProt sequences for all horse DARS2 products
  (A0A3Q2HM61, A0A3Q2L7S0, F6STJ2, A0A9L0SB67) and human Q6PI48, downloaded from
  rest.uniprot.org on 2026-10-20.
- `compare_models_rereview.py` -> `results-rereview.json`: global BLOSUM62 alignment of
  each horse product against human Q6PI48 and mapping of the human UniProt binding-site
  features (`uv run --with biopython python compare_models_rereview.py`).
- `ensembl_gene-rereview.json`: Ensembl REST lookup of ENSECAG00000004044 (expand=1).
- `panther_fullpath_rereview.py` -> `panther_fullpath_rereview.out`: ancestral path of
  the horse and human DARS2 leaves in the unpruned PANTHER 19 PTHR22594 tree.

## 1. The benchmark accession is an exon-skipping alternative isoform

All four horse UniProt DARS2 entries are products of one Ensembl gene,
ENSECAG00000004044 (chromosome 5), which has seven protein-coding transcripts
(593 to 668 aa). A0A9L0SB67 (616 aa) is the product of ENSECAT00000125808 (16 exons).

Exon comparison with ENSECAT00000043786 (A0A3Q2HM61, 652 aa, 17 exons): the only
difference is that ENSECAT00000125808 lacks one 108-nt exon (chr5:9524240-9524347).
The exon is a multiple of three, so its omission is an in-frame deletion of 36 residues.

A0A3Q2HM61 is the entry chosen as the gene-centric canonical product for DARS2 in the
UniProt horse reference proteome (UP000002281 one-protein-per-gene FASTA); none of the
four is a reviewed Swiss-Prot entry. The Ensembl canonical transcript ENSECAT00000005413
(F6STJ2, 668 aa) adds one further 48-nt exon that has no counterpart in human Q6PI48.

| Accession | Length | Paired with human | Identity | Human residues absent |
|---|---|---|---|---|
| A0A3Q2HM61 | 652 | 643 | 89.9% | 3-4 |
| F6STJ2 | 668 | 643 | 89.9% | 3-4 (plus 16 extra horse residues) |
| A0A3Q2L7S0 | 632 | 623 | 89.6% | 2, 9-14, 25-39 (altered N-terminus) |
| A0A9L0SB67 | 616 | 607 | 90.3% | 3-4, 341-376 |

All four horse products share the same C-terminal 20 residues (WPADSEAEKSSLDHPHHPES),
which differ from the human C-terminus (LKPYHIRVSKPTDSKAERAH). This is a horse-wide
feature, not specific to A0A9L0SB67.

## 2. What the 36-residue deletion removes

The missing human segment 341-376 (IIDISDVFRNTEIGFLQDALSKPHGTVKAICIPEGA) lies at
the start of the bacterial-type insertion domain, which the human DARS2 crystal-structure
paper places at residues 337-470 (PMID:23275545). The human N6-acetyllysine K368 (UniProt Q6PI48 notes that acetylation protects DARS2
from ubiquitin-mediated degradation) falls in the deleted segment.

All human UniProt substrate-binding features map onto identical residues in A0A9L0SB67:

| Human feature | Human | A0A9L0SB67 |
|---|---|---|
| Aspartate region 244-247 | QQFK | QQFK |
| ATP/Asp binding 266-268 | RDE | RDE |
| ATP binding 535 | E | E |
| Asp binding 542 | R | R |
| ATP binding 584-587 | GLDR | GLDR |

The N-terminal mitochondrial transit region (human 1-47) is retained, with 2 residues
absent and conservative changes (it remains Arg-rich). The anticodon-binding OB fold
(InterPro IPR004365) and the class II catalytic domain (PROSITE PS50862, 185-567) are
present.

Interpretation: the catalytic core and binding residues are intact, but a part of the
insertion domain that, in the human enzyme, reorients to open the active-site groove for
the tRNA acceptor arm is missing. Whether this isoform folds, dimerises or aminoacylates
tRNA(Asp) cannot be decided from sequence; no expression or activity data for it exist.

## 3. Phylogenetic placement (PANTHER 19, PTHR22594)

Horse DARS2 (Ensembl:ENSECAG00000004044.4) and human DARS2 (HGNC:25538) leaves share
an identical path from the family root to PTN000502607:

PTN000502375 (duplication) > PTN000502597 (PTHR22594:SF5 root) > PTN000502598 >
PTN000502599 > PTN000502600 > ... > PTN000502607, then human
PTN000502608 > PTN000502609 > PTN002731624 > PTN000502610 > PTN002503203 and horse
PTN000502617 > PTN001475965 > PTN001475968.

So the horse gene sits inside both PAINT IBD nodes used for human DARS2:
PTN000502597 (aspartate-tRNA ligase activity; aspartyl-tRNA aminoacylation) and
PTN000502598 (mitochondrion). It is the one-to-one ortholog of human DARS2 within SF5.
PANTHER places one leaf per gene, so this placement is for the gene, not for the
specific alternative transcript.
