# Identity and assay provenance

This is a manual source audit, not a sequence-identity prediction. All functional claims cite the normally cached primary papers. No source cache was edited.

| Link | Evidence | Limit |
|---|---|---|
| Q97R12 → TIGR4/SP_1029 | Normal `rlmCD-uniprot.txt`: accession, GN locus, OS strain, taxon 170187; sequence length 543 | UniProt currently lacks a primary symbol; its uncharacterized name does not negate later experiments |
| SP_1029 → native RlmCD | PMID26365244 Methods and Figures 2–3 explicitly disrupt SP_1029 in TIGR4 and identify both methylated sites | pTKY1196 donor strain differs between Methods and Results; native knockout chemistry is independent |
| SP_1029 → recombinant structures | PMID30388185 Methods explicitly names the cloned sp_1029 ORF and full-length 1–543/short 1–454 constructs | BL21-Gold is the expression host, not the source species |
| Structures → Q97R12 | Normal UniProt DR:PDB lists 5XJ1/5XJ2/5ZQ0/5ZQ1/5ZQ8/5ZTH; primary papers report corresponding structures | Construct truncation and E443Q mutation are explicit; not an assertion that all structures represent unmodified full-length protein |
| Dual specificity | Native TIGR4 LC/MS plus distinct recombinant U747 and U1939 RNA assays (26365244,28949991,30388185) | Shared pocket and family membership alone are insufficient; the earlier 18-nt packing pose is excluded |

The companion JSON records source hashes and exact accession/locus/PDB fields as read on 2026-10-26. The review symbol `rlmCD` is justified by the primary experiments, and the original seeded top-level fallback `Q97R12` is recorded in the audit baseline. All six annotation payloads remain unchanged.
