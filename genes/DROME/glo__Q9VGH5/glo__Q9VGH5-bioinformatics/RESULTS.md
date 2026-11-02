# glo (Q9VGH5) evolutionary placement and isoform check

Script: `panther_and_isoform_check.py` (stdlib only; output in `panther_and_isoform_check.out.txt`).
Inputs: release-pinned PANTHER 19.0 classification files (`.cache/panther/PTHR19.0_*`),
the PAINT IBD table for PTHR13976 (`interpro/panther/PTHR13976/PTHR13976-paint.tsv`), and the
UniProt flat files for Q9VGH5 and Q8INJ6.

## Findings

- Q9VGH5 is classified in PANTHER subfamily PTHR13976:SF76. Every IBA donor protein sits in a
  different subfamily: HNRNPH1 SF60, HNRNPF SF32, HNRNPH2 SF33, HNRNPH3 SF36, GRSF1 SF42,
  ESRP1 SF37, ESRP2 SF30 and Drosophila fus SF25. Glo therefore does not share a subfamily
  with any experimentally characterised hnRNP F/H protein, and subfamily-specific functions
  of the mammalian proteins should not be transferred to it.
- The IBA rows come from two deep PAINT nodes. PTN000360053 spans the hnRNP F/H, GRSF1 and
  ESRP clades and carries only RNA binding (GO:0003723), nucleoplasm (GO:0005654) and
  regulation of RNA splicing (GO:0043484). PTN000359854 (taxon:2759) carries ribonucleoprotein
  complex (GO:1990904). No more specific splicing, G-quadruplex or alternative-splicing term
  was placed at these nodes. PAINT left those out, so this review does not add them by transfer.
- Q8INJ6 (isoform C, 179 aa) is identical to Q9VGH5 over residues 1-168. Only the first RRM
  domain (49-129) lies inside the shared region. The second PROSITE RRM (146-225) and the third
  qRRM (crystallised as residues 475-562, PDB 5UZN) occur only in the full-length product.
  Q8INJ6 is not listed in the PANTHER 19.0 fly classification file.

## Limitations

No new alignment or phylogeny was built. The placement relies on PANTHER's HMM
classification and the PAINT node assignments.
