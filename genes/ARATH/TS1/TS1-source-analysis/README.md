# Source-table extraction

Run `uv run extract_localization_tables.py` to retrieve the publisher-deposited supplements through Europe PMC and reproduce `localization-table-extraction.json`. The report records URLs, HTTP status, table filenames, SHA256 checksums, headers and exact locus-matching rows. It does not modify publication caches or infer absence from a missing row.

PMID18431481 provides direct chloroplast/stromal observations for all five panel loci. S1 rows73/143/343/827/882 correspond to At1g14810, AKHSDH1, HSK, AKHSDH2 and TS1, respectively. S2 supplies stromal-enrichment abundance, and S3 independent stromal-preparation detections. AKHSDH2 was detected as gene model At4g19710.2; that historical model assignment should not be treated as proof of a present-day splice-isoform-specific localization.

PMID28887381 S1 Mapp row1113 labels At4g29840.1 (TS1) plastid. It does not substantiate the precise plasma-membrane location under review. This does not prove that peripheral or conditional membrane association is impossible.

PMID25293756 and PMID20061580 endpoints did not yield usable ZIP archives in this run. Their missing extraction is an access limitation, not evidence that a protein was absent. No GO annotation rows are used as independent support.
