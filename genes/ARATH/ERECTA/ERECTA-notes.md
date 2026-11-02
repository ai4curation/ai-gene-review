# ERECTA (At2g26330, Q42371) curation notes

Session 2026-10-06 (stomatal_lineage_development module). Folder named ERECTA (UniProt primary name ERECTA; synonym ER). Initial `just fetch-gene ARATH ERECTA` was replaced by an accession-based fetch (`Q42371 --alias ERECTA`). Falcon deep research failed (HTTP 402).

## Key findings
- LRR-RLK: cytoplasmic kinase, TM, extracellular LRRs [PMID:8624444].
- Primary receptor for EPF2; direct, saturable binding [PMID:22241782]; ER-family triple mutants have clustered stomata [PMID:16002616 "Loss-of-function mutations in all three ER-family genes cause stomatal clustering."].
- EPF ligands induce ER-SERK heteromerization; mutual transphosphorylation; SERKs act upstream of the MAPK cascade [PMID:26320950].
- Plasma membrane localization of functional ERECTA-YFP [PMID:26203655].
- Inflorescence architecture via YDA-MKK4/5-MPK3/6 [PMID:23263767 "YODA (YDA), a MAPKK kinase, was shown to be upstream of MKK4/MKK5 and downstream of ER in regulating inflorescence architecture"].
- Pleiotropic secondary roles: transpiration efficiency [PMID:16007076], thermotolerance [PMID:26280413], vascular patterning with PXY [PMID:23578929], ovule MMC fate [PMID:37606225], resistance to Ralstonia [PMID:14617092] and Plectosphaerella [PMID:15998304; PMID:19589071].

## Curation decisions
- Core MF: transmembrane receptor protein serine/threonine kinase activity GO:0004675 (NEW; existing ISS GO:0019199 accepted as parent).
- Core BPs: negative regulation of stomatal complex development (GO:2000122, NEW; stomatal complex morphogenesis rows MODIFIED to it) and inflorescence morphogenesis (GO:0048281, accepted).
- 13 high-throughput ectodomain-network protein binding rows (PMID:29320478) REMOVED as uninformative; stomagen protein binding MODIFIED to peptide binding.
- Mitochondrion HDA (PMID:14671022) MARK_AS_OVER_ANNOTATED (likely membrane contamination; ERECTA-YFP at plasma membrane).
- Lease et al. 2001 New Phytologist IDA (DOI:10.1046/j.1469-8137.2001.00150.x) title verified via Crossref; not cached; accepted.
- No GO-CAM models contain ERECTA.
