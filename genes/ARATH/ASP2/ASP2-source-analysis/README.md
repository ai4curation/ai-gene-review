# Primary supplemental-table inspection

The extraction scripts download publisher-deposited supplements through Europe PMC, preserve source URLs and SHA256 checksums, and extract exact target rows. They do not modify publication caches. Run from the repository root with `uv run <script>`.

PMID28887381 Supplement1 Mapp: ASP2/ASP4 group row1303 is classified cytosol; ALAAT1/ALAAT2 row103 is classified mitochondrion; ASP5 isoform group row2334 is classified plastid and has a membrane-protein flag. These are protein-group assignments. They do not independently prove the GOA plastid/nucleus/plasma-membrane assignments, respectively, and do not establish absence from those compartments.

PMID21533090 SupplementS3: ASP2 row5055 has a detected peptide; ASN2 isoforms row5793 have a detected peptide. SupplementS4 rows1127/1308/1309 classify these proteins NSnoTM. Detection in the plasmodesmal preparation, which the authors report contains putative cytoplasmic contaminants, does not by itself resolve stable plasmodesmal localization. Lack of a transmembrane helix is not a reason to exclude peripheral association. SupplementS5 contains preexisting GO assertions, not independent evidence, and is not used to justify annotations.

Some requested Europe PMC supplementary endpoints returned non-ZIP responses; the extraction report records those failures without inventing missing tables. Primary study abstracts and full text were assessed separately. No absence of a matching row is treated as proof of absence of function.
