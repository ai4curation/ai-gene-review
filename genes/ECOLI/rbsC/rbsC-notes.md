# rbsC (Escherichia coli K-12) curation notes

## 2026-11-11 initial review

- Reviewed as an exemplar for `modules/bacterial_ribose_uptake_and_entry.yaml` (RbsABC import, RbsD pyranase, RbsK ribokinase).
- Deep research was not run: no deep-research provider credentials were available in this environment. No
  `-deep-research-<provider>.md` file was created. The review relies on the cached publications cited by
  GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- Bare protein-binding rows were removed under the protein-binding policy; the RbsABC2 complex membership is
  captured by GO:0055052 [PMID:25533465 "The ribose transporter in Escherichia coli is a tripartite complex"].
- General terms (membrane, transmembrane transport, kinase activity, etc.) were refined with MODIFY to the
  specific terms the gene already carries, consistent with the KT2440 sibling reviews.
