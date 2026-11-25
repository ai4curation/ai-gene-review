# hs6st3b notes

## 2026-05-09 review notes

Reviewed GOA, UniProt A0MGZ7, PMID:28103688, and PANTHER family cache. The direct function is heparan sulfate 6-O-sulfotransferase activity using PAPS and oligosaccharide substrates; generic sulfotransferase and ligand-binding annotations were kept subordinate to the specific catalytic term.

## Re-review 2026-09-29
- Full rewrite of all templated review blocks (previously every row read "is reviewed for zebrafish hs6st3b. The annotation is consistent with...").
- Established that the experimental paper PMID:28103688 (Xu et al. 2017) crystallized the zebrafish 6-OST that UniProt assigns to hs6st3b; it shares 81% identity with human HS6ST3 [PMID:28103688 "The zf6-OST shares 71%, 72% and 81% sequence identities with the human 6-OST isoforms 1, 2 and 3"]. Core MF heparan sulfate 6-O-sulfotransferase activity (GO:0017095) ACCEPT, supported directly by structure + activity assays [PMID:28103688 "transfer a sulfo group from ...(PAPS) to the 6-OH of GlcN"].
- GO:0008146 (both IEA and IDA) MODIFY -> GO:0017095. GO:0050656 PAPS binding and GO:0070492 oligosaccharide binding KEEP_AS_NON_CORE as mechanistic components evidenced by the ternary co-crystal structures.
- Kept GO:0000139 Golgi membrane as NEW: supported by the paper's statement that "HS biosynthesis occurs in the Golgi and endoplasm reticulum", type II single-pass topology, and comparator check (human HS6ST1 O60243 and HS6ST2 Q96MM7 both carry GO:0000139, QuickGO TAS). No direct zebrafish imaging, so flagged as family/pathway inference.
- Removed 2 stale rows (GO:0008146 IEA GO_REF:0000120, GO:0017095 IEA GO_REF:0000116) whose GO_REFs no longer match refreshed GOA; resolved the 2 corresponding PENDING rows (GO_REF:0000002 -> MODIFY, GO_REF:0000120 -> ACCEPT).
- Added reference_review (VERIFIED) to PMID:28103688. Validation: 0 errors, 1 soft warning (deep-research not quoted; primary structure paper used instead).
