# pgsA curation notes

Q88FJ8 is the KT2440 PgsA candidate. Current UniProt assigns the exact
CDP-diacylglycerol--glycerol-3-phosphate phosphatidyltransferase reaction
(RHEA:12593) and a multi-pass membrane topology
[UniProtKB:Q88FJ8, "Full=CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase"].

The KT2440 lipidomics/pathway study explicitly places `pgsA` upstream of
`pgpA` in phosphatidylglycerol biosynthesis and detects phosphatidylglycerol
and cardiolipin in this strain [PMID:21895997, "pgsA– CDP‐diacylglycerol‐glycerol‐3‐phosphate‐3‐phosphatidyltransferase; pgpA– phosphatidylglycerophosphatase A"].

The exact molecular function is well supported by current deterministic
resources. The physiological contribution should be tested with targeted
lipidomics because the literature establishes pathway context rather than a
PgsA-specific knockout phenotype in KT2440.

## 2026-11 update

Re-reviewed to completion alongside the E. coli exemplar in `genes/ECOLI/` used by the
module `bacterial_phosphatidylglycerol_cardiolipin_biosynthesis`. Broad parent terms
(membrane, phospholipid or lipid biosynthesis, generic transferase or catalytic activity)
that were previously kept as non-core are now refined with MODIFY to the specific terms
the gene carries, so that same-term rows are treated the same way across the PSEPK and
E. coli orthologues. Every row now cites vetted family-level or curated evidence. No
deep-research provider key was available.
