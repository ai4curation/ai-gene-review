# Hgf (rat) review notes

- Fetched with `just fetch-gene rat Hgf`; UniProt P17945 (HGF_RAT), 46 GOA rows.
- No deep-research provider available; manual synthesis in `Hgf-deep-research-manual.md`.
- PMID:20097747 (Lionetti et al. 2010, HBR in infarcted rat heart) read in full text: HGF is
  only a readout there (mRNA up, secretion into medium up after HBR) [PMID:20097747 "The HBR treatment enhanced the secretion of VEGF and HGF in the culture medium from both RCm and Stro-1 cells."].
  It supports secretion (extracellular space) for rat HGF but not any process involvement of HGF.
- Core: MET ligand (receptor ligand activity / growth factor activity), extracellular.
  [PMID:1846706 "directly established the c-met product as the cell-surface receptor for HGF"]
- Pseudoprotease: NOT endopeptidase IBA accepted; IEA proteolysis removed (HGF is the
  substrate of HGFAC/TMPRSS13 processing, it does not cleave anything)
  [file:rat/Hgf/Hgf-uniprot.txt "Has lost two of the three essential catalytic residues"].
- `cellular response to hepatocyte growth factor stimulus` on the ligand itself is an
  over-annotation: the responding cell carries MET.
- Abstract-only experimental rows: 1826679 (protein-containing complex binding) and
  17549731 (positive regulation of myelination) cannot be checked against full text; set UNDECIDED.
- No NEW terms proposed (strict NEW bar). receptor ligand activity would be redundant with growth factor activity (its descendant), which the gene already carries.
