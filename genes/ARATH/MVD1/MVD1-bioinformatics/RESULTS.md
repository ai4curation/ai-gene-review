# Peroxisomal matrix markers in the Aryal et al. 2014 "cytosol" HDA set

Script: `cytosolic_fraction_markers.py` (queries QuickGO and UniProt at run time; raw
output in `RESULTS-raw.txt`, run 2026-11-18). Run with the project's shared Python:
`python -I cytosolic_fraction_markers.py > RESULTS-raw.txt`.

Question: GOA annotates Arabidopsis MVD1 (O23722) and MK (P46086) to cytosol
(GO:0005829) by HDA from PMID:25293756, a size-exclusion proteomics study of the crude
cytosolic fraction of leaf homogenates. Does that fraction separate cytosol from
peroxisomal matrix?

## Findings

- QuickGO returns 1,256 gene products annotated from PMID:25293756, 706 of them with a
  cytosol HDA row. Positive controls work: MVD1 and MK are both returned with
  GO:0005829 HDA.
- The most abundant leaf-peroxisome matrix enzymes are all in the same cytosol HDA set:
  catalases CAT1 (Q96528), CAT2 (P25819) and CAT3 (Q42547), glycolate oxidase GLO1
  (Q9LRR9) and hydroxypyruvate reductase HPR (Q9C9W5).
- Less abundant leaf peroxisomal proteins (PMDH2, PED1/KAT2) and the seedling
  glyoxysome enzymes (MLS, ICL) were not returned. PMK and MVD2 were not returned.

## Interpretation

The crude cytosolic fraction contains peroxisomal matrix proteins released during
homogenisation, so detection of a soluble enzyme in it cannot distinguish a cytosolic
protein from a peroxisomal-matrix one. The MVD1 cytosol HDA row is therefore
uninformative about cytosol versus peroxisome. For MK the cytosolic location rests on
independent YFP-fusion data (PMID:21655959, PMID:35064110), not on this fraction.
Absence of PMK and MVD2 from the set is not evidence about their location
(low-abundance proteins can be missed).
