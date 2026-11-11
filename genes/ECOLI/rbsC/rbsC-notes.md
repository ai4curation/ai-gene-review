# rbsC (Escherichia coli K-12, P0AGI1) curation notes

## 2026-11-11 initial review

- Reviewed as the E. coli exemplar of the RbsC permease subunit of the RbsABC importer in `modules/bacterial_ribose_uptake_and_entry.yaml`.
- Deep research was not run: no deep-research provider credentials were available in this environment,
  and no `-deep-research-<provider>.md` file was created. The review relies on the cached publications
  cited by GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- RbsC is the six-helix integral inner-membrane permease, with cytoplasmic N and C termini
  [PMID:9922273 "the protein traverses the membrane six times and the N and C termini are exposed to the
  cytoplasm"]. It forms the RbsC2 homodimer of the RbsABC2 complex [PMID:25533465].
- The three bare protein-binding rows (RbsB, RbsA, and both together, from the reconstituted complex) were
  removed under the protein-binding policy. Complex membership is captured by GO:0055052.
- Refinements with MODIFY: membrane to plasma membrane, transmembrane transporter activity and D-ribose
  transmembrane transporter activity to ABC-type D-ribose transporter activity, transmembrane transport to
  D-ribose transmembrane transport, and ABC transporter complex to GO:0055052.
- E. coli RbsC is in PANTHER PTHR32196:SF21, whereas KT2440 and B. subtilis RbsC are in SF72. The module
  therefore grounds the permease at family level.
