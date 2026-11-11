# Sec71 (Q9VJW1): ComplexPortal SEC62-SEC63 complex membership check

Script: `check_complexportal.py` (live queries to the ComplexPortal web service and
the UniProt REST API); raw output in `output.txt`.

## Question

GOA carries three NAS rows for Q9VJW1 (rough endoplasmic reticulum membrane,
Sec62/Sec63 complex, post-translational protein targeting to membrane,
translocation), all from ComplexPortal record CPX-26617 citing PMID:15901661.
Is Drosophila Sec71 plausibly a subunit of the ER Sec62/Sec63 translocon complex?

## Results

- ComplexPortal CPX-26617 "SEC62-SEC63 complex" (Drosophila melanogaster) lists
  three participants: Q9VJW1 Sec71, Q9VS57 Sec63 and Q9VL49 Trp1 (Translocation
  protein SEC62).
- Drosophila Sec71 (Q9VJW1) is 1653 residues, has no predicted transmembrane
  segment, and carries the BIG/Sec7-family ARF-GEF architecture: Pfam DCB,
  Sec7-like_HUS, Sec7, Sec7-like_HDS and BIG2_C.
- The UniProt gene_exact:SEC71 query for S. cerevisiae returns P33754, gene SEC66
  (Translocation protein SEC66), 206 residues, one transmembrane segment, Pfam Sec66.
  SEC71 is a synonym of yeast SEC66, the Sec63-complex subunit.

## Interpretation

The yeast Sec63-complex subunit called Sec71 is Sec66, a small single-pass membrane
protein with a Sec66 domain. The fly gene named Sec71 is a large, soluble
BIG1/BIG2-type Sec7-domain ARF guanine-nucleotide exchange factor with none of those
features. The two proteins share a name, not a family. Including Q9VJW1 in a
Drosophila Sec62/Sec63 complex therefore looks like a symbol collision with yeast
SEC71/SEC66, and the three NAS rows derived from CPX-26617 do not describe the fly
protein.
