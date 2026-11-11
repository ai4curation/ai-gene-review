# rbsA (Escherichia coli K-12, P04983) curation notes

## 2026-11-11 initial review

- Reviewed as the E. coli exemplar of the RbsA ATPase subunit of the RbsABC D-ribose importer in `modules/bacterial_ribose_uptake_and_entry.yaml`.
- Deep research was not run: no deep-research provider credentials were available in this environment,
  and no `-deep-research-<provider>.md` file was created. The review relies on the cached publications
  cited by GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- RbsA is the cytoplasmic ATP-binding subunit of the RbsABC2 complex [PMID:25533465 "a cytoplasmic
  ATP-binding cassette protein, RbsA, with fused nucleotide binding domains"].
- The two bare protein-binding rows (PhnG by Y2H; RbsC in the reconstituted complex) were removed under the
  protein-binding policy. The complex membership is captured by GO:0055052, which is accepted.
- General terms were refined with MODIFY: membrane to plasma membrane, monosaccharide transmembrane transport
  to D-ribose transmembrane transport, ABC-type monosaccharide and D-ribose transmembrane transporter
  activity to ABC-type D-ribose transporter activity, and ABC transporter complex to GO:0055052.
- The L-arabinose transporter IBA and its derived arabinose transport IEA are marked over-annotated. The
  PAINT node PTN001953353 is seeded only by AraG, and no evidence shows that RbsABC imports arabinose.
- The UniRule `enables` GO:0015611 row is recorded as a WRONG_QUALIFIER source defect (contributes_to),
  because the activity belongs to the whole complex.
