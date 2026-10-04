# ARMC7 review notes

## Sources
- Affinage: trust gates clear; a single finding from the activated minor spliceosome structure (PMID:33509932, abstract only in the cache).
- PubMed recall (ARMC7, 2026-10-04): the only functional papers are PMID:33509932 and PMID:30760564 (maize RBM48, which reports the conserved RBM48-ARMC7 interaction).
- 83 of 86 GOA rows are generic protein binding from proteome-scale screens. Partners were resolved by UniProt batch query (66 accessions).

## Decisions
- U12-type catalytic step 2 spliceosome (IPI) and mRNA splicing via spliceosome (NAS) → ACCEPT; these are the core role.
- Cytosol (HPA IDA) → KEEP_AS_NON_CORE.
- All protein-binding rows → REMOVE (policy), including RBM48: complex membership is captured by the spliceosome row.
- No NEW cap-binding MF: the abstract assigns cap binding to the RBM48-ARMC7 complex, not to ARMC7 itself.
