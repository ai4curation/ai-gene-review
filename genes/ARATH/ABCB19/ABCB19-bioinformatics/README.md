# Target-specific inspection of PMID:28887381

`inspect_28887381.py` downloads the seven original XLSX supplements through the
Europe PMC supplementary-files endpoint and searches every worksheet for exact
Arabidopsis loci. `28887381-target-evidence.json` records file SHA256 hashes,
one-based Excel row numbers, all target hits and the relevant summary columns.
Run from the repository root with its Python environment. Raw workbooks are
generated cache, not edited source records.

The original S1 workbook (`supp_RA117.000276_4895_0_supp_4978_88s80d.xlsx`),
worksheet `Mapp`, identifies ABCB19 AT3G28860.1 in rows 2145 and 2804. Both rows
have `True membrane = True`, blank `Dual Localized`, and `SUBAcon localization =
plasma membrane`. S4 sucrose-gradient data also identify the locus. The SUBAcon
column is an imported classification, not a new organelle-localization assay.
The membrane/dual-localization classifications and fractionation methods are
the relevant independent experimental context.

The paper solubilizes a washed microsomal pellet with cholate. Cholate-soluble
material is therefore not synonymous with cytosol. These target rows do not
establish an independently detected soluble cytosolic ABCB19 pool. This is a
source-specific limitation, not an assertion that a multipass protein can never
have an atypical soluble fragment or localization.

For coordinated review, PIN3 AT1G70940.1 appears in S1 row 1879 with the same
membrane/blank-dual/PM summary. ABCB4 occurs in a multigene protein group in S1
row 631, likewise with `True membrane = True` and blank `Dual Localized`.
ABCB1 AT2G36910.1 was found in S4 sucrose-gradient/raw-peptide data, but not in
the S1 `Mapp` summary; this inspection did not verify an ER-specific assignment.
Absence from a summary sheet is not a negative localization experiment.

Original source: McBride et al., 2017, DOI
[10.1074/mcp.RA117.000276](https://doi.org/10.1074/mcp.RA117.000276).
