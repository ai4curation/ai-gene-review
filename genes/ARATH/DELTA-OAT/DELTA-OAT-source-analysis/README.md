# Arabidopsis localization source audit

The accompanying script downloads the publisher-deposited supplementary archive for PMID:28887381 from Europe PMC, records each workbook SHA256, and extracts the four exact AGI target identifiers from the summary tables. The JSON output preserves spreadsheet row numbers and column headers. Raw spreadsheets remain build artifacts, not rewritten publication caches.

The S1 Mapp sheet lists all four target proteins as mitochondrion.

Specifically, the Superdex entries are ARGAH2 (At4g08870; row 970), ARGAH1 (At4g08900; row 971), DELTA-OAT (At5g46180; row 1416), and ALDH12A1 (At5g62530; row 1524). ARGAH1 has a True membrane flag in that sheet, but the Dual localized field is empty. The other three lack either flag in those entries. ARGAH2 also has a Superose entry in the void. These observations establish detection in the experiment, not organelle-specific import or stable cytosolic residence.

The study begins with mixed leaf microsomes, uses cholate solubilization and size-exclusion profiles, and compares sucrose-gradient penetration with crude soluble fractions. Its method can identify real membrane association, including soluble proteins that associate with membranes; absence of a transmembrane helix is not a reason to reject association. However, a broad fraction or inherited location label does not independently demonstrate plastid localization of OAT/ALDH12A1 or a native cytosolic pool of either arginase. Those annotation claims remain unresolved rather than being rejected from a different organelle's positive evidence.

Separate primary experiments establish OAT mitochondrial targeting (PMID:18419821), ALDH12A1 targeting by its first 40 residues (PMID:11532180), and ARGAH1/2 matrix targeting using myc fusions, a matrix marker and differential permeabilization (PMID:18567826). The ARGAH chloroplast report (PMID:28716421) uses a different transient leaf-expression system; the two experiments should not be collapsed into one universal targeting result.

PMID:20018591 full text was obtained by normal cache fetching. Its metal-loaded IMAC assay uses solubilized mitochondrial extracts and subsequent protein identification from gel bands. Attempts to retrieve its supplementary Word document returned an HTML challenge page; no fabricated document extraction was retained. Target-specific S3/S4 metal-binding rows therefore remain unverified. Lack of a physiological metal-cofactor requirement is not evidence that incidental metal binding is absent.
