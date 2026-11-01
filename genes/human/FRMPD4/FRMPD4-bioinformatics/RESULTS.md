# FRMPD4 quantitative fragment interaction audit

This analysis replays the 53 FRMPD4 protein-binding contexts citing [PMID:36115835](https://doi.org/10.1038/s41467-022-33018-0). The original workbook contains 713 rows in which FRMPD4 supplies a PDZ domain or terminal peptide. Of these, 191 measurement rows join the 53 original annotated partners: 31 contexts have a positive original fragment measurement and 22 have unresolved quantitative support. These results describe the inspected assays; they do not establish full-length endogenous complexes, tissue roles, infection processes or absence of interaction.

## Reproduction

The script uses Python 3's standard library and does not access the network or alter any source. Obtain the original [Supplementary Data 1 workbook](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-33018-0/MediaObjects/41467_2022_33018_MOESM4_ESM.xlsx) separately. Its 12,233,560 bytes must have SHA-256 `ada912921164f0a79630c6a714b9ff264a7217ad3e646153ef498eb456206795`; the script stops on a different checksum. The large workbook is not duplicated here.

From this directory, with a downloaded or previously retained workbook:

```sh
python3 audit_36115835.py --workbook /path/to/41467_2022_33018_MOESM4_ESM.xlsx \
  --goa ../FRMPD4-goa.tsv --output /tmp/frmpd4-audit-replay
```

Use a new output directory. Compare the four generated files with `results/`. The script reads the XLSX XML directly, retains original cell values and joins each annotated accession to the exact source data. `inputs/contexts.tsv` binds original context indices to physical lines in the immutable native GOA export. `inputs/intact-36115835.jsonl` contains 189 complete, unmodified 42-field IntAct records from the 2026-11-01 query snapshot, including source line, interaction identifiers, exact isoform suffixes, features, taxon, negative flag and literal affinity parameter. Input hashes, the public query and original page hash are recorded in `inputs/provenance.json`. Base accessions are used only to locate the original records; their declared molecular identities are never rewritten. Partner gene names and synonyms supply an explicit, case-insensitive join to the workbook's domain names, including INADL/PatJ aliases.

## Measurements and thresholds

The original Methods sections **Interaction measurements with holdup experiments** and **Conversion of holdup binding intensities to dissociation constants** explain the relevant conventions. The first supplies BI detection cutoffs of 0.05 for DAPF and 0.1 for SAPF and LYSC/CALIP. The latter explains why sensitivity in affinity units varies with the peptide concentration and assay. There is no single pKd cutoff of 4 for all rows.

[Matched measurements](results/matched-measurements.tsv) records each original worksheet row, direction, composite pKd, selected method, FP affinity, actual BI, applicable method BI cutoff and conversion concentration. Its `calculated_pKd_limit_assuming_4uM_PDZ` column is a calculation from original Eq. 2 using the paper's usual 4 µM PDZ concentration. It is explicitly not an author-reported per-domain limit and is not used to assign a curation action or override the reported measurements. The original worksheet does not separately provide a literal per-domain pKd cutoff. The calculation is `Kd_limit = (PBM_uM - 4 * BI_cutoff) * (1 - BI_cutoff) / BI_cutoff`, followed by conversion from micromolar to molar and `-log10`.

Composite zero is not interpreted as an affinity of 1 M. For every selected zero-composite row, the script independently verifies that its underlying BI is below the applicable method cutoff. It also records whether any literal `<` expression was present; a reported censored value is not silently replaced by a measured number. The unresolved IntAct string `kd:1.0x10(molar)` and `negative=false` are retained verbatim and are not sufficient to verify positive measured binding. Missing curated parameters remain missing. No quantitative claim is inferred from the negative flag alone.

[Context summary](results/context-summary.tsv) distinguishes positive original measurements from finite curated parameters. The four original contexts numbered 22, 47, 51 and 59 have additional positive author rows even though their exact curated records contain no finite affinity parameter. All 27 contexts with a finite curated parameter have a numeric original affinity match. For example, TJP3's positive original row 11802 has composite pKd 3.83; its original BI and method are exposed alongside that value. Its orientation is FRMPD4's PDZ binding the TJP3 peptide, which does not support annotating FRMPD4 as binding a partner PDZ domain.

The 31 positive contexts comprise 27 with positive FRMPD4 C-terminal peptide binding to partner PDZ domains and four supported only in the reverse direction. For the other 22, the inspected source does not resolve a positive quantified interaction. This is uncertainty about the imported assertion, not evidence that binding never occurs and not a basis for removing an experimental annotation solely from incomplete support.

[All target rows](results/all-target-rows.tsv) preserves the complete 713-row FRMPD4 slice, including additional measurements outside the 53 annotated partner joins. Column letters refer to the original worksheet, whose first row supplies the column names. [Summary](results/summary.json) reports the computed counts. The outputs contain source data and measurement interpretations, not copies of the gene's biological synthesis or automatically generated GO review decisions.
