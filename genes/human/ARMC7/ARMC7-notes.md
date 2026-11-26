# ARMC7 review notes

## Sources
- Affinage: trust gates clear; a single finding from the activated minor spliceosome structure (PMID:33509932, abstract only in the cache).
- PubMed recall (ARMC7, 2026-10-04): the only functional papers are PMID:33509932 and PMID:30760564 (maize RBM48, which reports the conserved RBM48-ARMC7 interaction).
- 83 of 86 GOA rows are generic protein binding from proteome-scale screens. Partners were resolved by UniProt batch query (66 accessions).

## Decisions
- U12-type catalytic step 2 spliceosome (IPI) and mRNA splicing via spliceosome (NAS) → ACCEPT; these are the core role.
- Cytosol (HPA IDA) → KEEP_AS_NON_CORE.
- All protein-binding rows → REMOVE (policy), including RBM48: complex membership is captured by the spliceosome row.
- NEW U6atac snRNA binding (GO:0030624), contributes_to (round 1, below).

## Review round 1 (PR #4190)
- NEW GO:0030624 U6atac snRNA binding, qualifier contributes_to (IDA, PMID:33509932), because cap binding belongs to the RBM48-ARMC7 heterodimer. It is also the core function's contributes_to_molecular_function. GO:0000339 RNA cap binding was not used: its definition is restricted to 7-methylguanosine caps, and U6atac carries a gamma-monomethyl phosphate cap.
- The RBM48 row stays REMOVE: the activity is now captured by the contributes_to MF and the complex row.
- ZMAT5 (U11/U12-20K), ESS2 and SYF2 rows get specific sentences; the ZMAT5 hit corroborates minor-spliceosome membership.
- The cytosol row notes that UniProt has no subcellular location for ARMC7.
