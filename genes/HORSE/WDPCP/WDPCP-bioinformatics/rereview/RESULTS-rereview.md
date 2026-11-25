# WDPCP horse gene-model comparison (re-review, 2026-10-20)

Reproduce: `uv run compare_gene_models_rereview.py` in this folder (input `wdpcp_models.fasta`,
downloaded from the UniProt REST API on 2026-10-20; raw output in `output_rereview.txt`).
Alignments are global BLOSUM62 alignments with free end gaps (Biopython PairwiseAligner); all
numbers below are computed by the script, not entered by hand.

## Gene models

Ensembl gene ENSECAG00000019956 (horse chromosome 15) has eight protein-coding transcripts, each with
its own UniProtKB/TrEMBL entry. Ensembl REST (`lookup/id/ENSECAG00000019956?expand=1`) marks
ENSECAT00000134648 (protein ENSECAP00000083348, UniProt A0A9L0T876, 756 aa) as the canonical transcript.
The benchmark accession A0A3Q2KRK8 is the product of the non-canonical transcript ENSECAT00000034053
(ENSECAP00000026115, 705 aa). No horse WDPCP entry is Swiss-Prot reviewed.

## Results

| query | reference | identity | reference residues unaligned | query residues unaligned |
|---|---|---|---|---|
| A0A9L0T876 (756) | O95876 (746) | 605/667 = 0.907 | 1-33, 693-735, 739-741 | 668-756 |
| A0A3Q2KRK8 (705) | O95876 (746) | 619/693 = 0.893 | 1-33, 723-742 | 694-705 |
| A0A3Q2KRK8 (705) | Q8C456 (722) | 548/693 = 0.791 | 38-39, 669-676, 695-699, 704-717 | 694-705 |
| A0A9L0R7M2 (713) | O95876 (746) | 636/713 = 0.892 | 1-33 | none |
| Q8C456 (722) | O95876 (746) | 568/712 = 0.798 | 1-33, 720-720 | 36-37, 669-676 |

C-terminal 30 residues:

- human O95876: NAEDGELREDGREQEIRDGGSLKMIHFGLV
- mouse Q8C456: WNAEGELKEDQRKQDIGDVGSLRMVHFGLV
- horse A0A9L0R7M2: NEEEGEIREDCTGQEIRDGGSLRMVHFRLV
- horse A0A3Q2KRK8: GSLMPKTCNEEDQSFDVASYWKHQQWTMYA
- horse A0A9L0T876 (Ensembl canonical): ELERSCTGIWVFFDFIYNYFEVQTFSVFKS

## Interpretation

- The N-terminal difference is not a truncation: mouse Q8C456 also lacks human residues 1-33, and all
  horse models except A0A3Q2HIY6 start with the mouse-like MSFCLTELHLWSL motif.
- A0A3Q2KRK8 is colinear with human WDPCP through human residue 722 (WD40 propeller and alpha-solenoid
  retained), then ends in a 12-residue segment (horse 694-705) that aligns to neither human nor mouse.
  It therefore lacks the last ~24 human residues, including the conserved terminal motif
  (GSLxMxHFxLV) present in human, mouse and the horse A0A9L0R7M2 model. This is consistent with use of
  an alternative final exon.
- The C-terminal ~60 residues of mouse Wdpcp carry its phosphoinositide binding (PMID:35427153). The
  A0A3Q2KRK8 product keeps the first part of this segment but lacks its conserved end, so lipid-binding
  properties cannot be transferred to this isoform without testing.
- A0A9L0R7M2 (713 aa) is the horse model colinear with the full human and mouse proteins at both ends.
  The Ensembl canonical A0A9L0T876 diverges from horse residue 668 onward and also lacks the conserved
  C-terminal motif.

## PAINT context (from interpro/panther/PTHR13667/PTHR13667-paint.tsv)

The PAINT ancestral node PTN001007408 (taxon 6072, Eumetazoa) in PTHR13667 carries IBD assertions for
axonemal basal plate (GO:0097541), cilium organization (GO:0044782), nervous system development
(GO:0007399) and establishment of protein localization (GO:0045184). UniProt places A0A3Q2KRK8 in
PTHR13667:SF5, the same subfamily as human O95876, mouse Q8C456 and Xenopus Q32NR9, so horse WDPCP
descends from this node. The node does not carry plasma membrane, axoneme, phosphatidylinositol
binding or septin cytoskeleton terms.
