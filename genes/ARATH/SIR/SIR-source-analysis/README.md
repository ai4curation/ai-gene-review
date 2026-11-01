# SIR in the PMID:28887381 deposited proteomics tables

The publisher-deposited supplement was obtained through Europe PMC's `PMC5672003/supplementaryFiles` endpoint. Run `uv run genes/ARATH/SIR/SIR-source-analysis/extract_membrane_tables.py` from the repository root to download the original ZIP and reproduce the JSON extraction. The script records SHA-256 hashes for each original spreadsheet and all rows containing AT5G04590. Raw spreadsheets remain download artifacts, not edited sources.

Supplemental Table S1 is `supp_RA117.000276_4895_0_supp_4978_88s80d.xlsx`. In its `Mapp` sheet, Excel row 1215 identifies `P1_AT5G04590.1` / `AT5G04590.1` / SIR. The `Subacon localization` field is `plastid`. The `True membrane` and `Dual Localized` fields are both empty. The detected Superdex peak has apparent mass approximately 44.04–46.14 kDa. SIR also appears in the underlying protein and peptide intensity sheets.

No AT5G04590 row was found in the other deposited spreadsheets, including Table S4 (proteins predicted to form an oligomeric membrane-associated complex) or Table S5 (dual-localized proteins). The generated JSON records the complete search of every sheet, including tables with no matches; it does not infer an absence of the protein from every possible membrane.

Interpretation: this experiment detects SIR within a broadly prepared microsomal profiling sample, but does not classify it as a true membrane protein or establish a plasma-membrane localization. The primary paper explicitly includes cytosolic, chloroplast and mitochondrial proteins in this fraction. The specific plasma-membrane GO claim is therefore more precise than this source supports. Peripheral association is possible and does not require a membrane anchor.
