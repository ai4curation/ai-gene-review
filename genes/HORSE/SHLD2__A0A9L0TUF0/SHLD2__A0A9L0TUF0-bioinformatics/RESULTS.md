# Horse SHLD2 canonical model (A0A9L0TUF0) vs human SHLD2 long isoform (Q86V20-2)

Script: `compare_to_human.py` (run with `uv run compare_to_human.py`). Output:
`compare_to_human.out` and `compare_to_human.json`. Global alignment, BLOSUM62,
gap open -10, extend -0.5, free end gaps. Horse sequence from
`SHLD2__A0A9L0TUF0-uniprot.txt`; human long isoform (904 aa, the form used in the
biochemical and rescue studies) from `genes/human/SHLD2/SHLD2-isoform2.fasta`.

## Evolutionary placement

- UniProt places A0A9L0TUF0 in PANTHER PTHR14495:SF2 (SHIELDIN COMPLEX SUBUNIT 2),
  the only subfamily of PTHR14495 and the same subfamily as human SHLD2 Q86V20.
- The PAINT table `interpro/panther/PTHR14495/PTHR14495-paint.tsv` has one annotated node,
  PTN001025652 (taxon 6072, Eumetazoa), seeded only by human Q86V20, with three IBD terms:
  nucleus (GO:0005634), site of double-strand break (GO:0035861) and regulation of
  double-strand break repair via homologous recombination (GO:0010569). The curator did not
  place the signed human terms (negative regulation of HR, positive regulation of NHEJ) or
  isotype switching at this node.
- The other horse GO rows are Ensembl Compara orthology transfers (GO_REF:0000107) from human
  Q86V20 / ENSP00000298786.

## Sequence comparison

| Measure | Value |
|---|---|
| Horse length | 1047 aa |
| Human Q86V20-2 length | 904 aa |
| Identity over aligned pairs | 73.9% (904 aligned pairs) |
| Human coverage | 100% |

| Human region (Q86V20-2 coordinates) | Horse residues | Identity |
|---|---|---|
| 1-60, sufficient for SHLD3 and MAD2L2 binding | 40-100 | 78.3% |
| 6-11, deletion abolishes SHLD3/MAD2L2 binding | 45-50 | 100% |
| 421-904, SHLD2C construct that binds ssDNA | 464-947 | 81.8% |
| 655-723, OB-fold-B exon missing from the short isoform | 698-766 | 85.5% |
| 652-891 (iso-1 652-822), SHLD1-interaction region | 695-934 | 81.2% |

All four cysteines of the OB-fold-C zinc ribbon (human iso-1 C699, C702, C717, C720;
iso-2 C768, C771, C786, C789) are conserved, at horse C811, C814, C829 and C832.

## Horse-specific segments

- An N-terminal extension of 39 residues (MGSMGKREQSERTPGVLACGTGRMELPFAEMSMTFYKET)
  precedes horse M40, which aligns with human M1 (MSGGSQVHIF...).
- A C-terminal extension of 100 residues (horse 948-1047) follows the end of the human
  sequence and has no counterpart in human SHLD2.

Both extensions lie outside the experimentally mapped functional regions. Whether either is
part of the real horse protein or a gene-model artefact (an upstream in-frame start, or
read-through past the conserved stop) was not tested: no transcript or protein evidence was
examined.

## Interpretation

A0A9L0TUF0 is the one-to-one horse ortholog of human SHLD2, in the same PANTHER subfamily,
and it carries every experimentally mapped functional element of the human long isoform:
the SHLD3/MAD2L2-binding N-terminal motif, the OB-fold-B exon whose loss abolishes HR
suppression in human cells, the zinc-ribbon cysteines of OB fold C, and the SHLD1-binding
region. Nothing in the sequence argues against transfer of the human end-protection
functions. These functions are inferred: no experiment on horse SHLD2 is known.
