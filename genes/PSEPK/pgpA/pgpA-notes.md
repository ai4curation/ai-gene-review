# pgpA curation notes

Q88QH3 is a membrane phosphatidylglycerophosphatase A. Current UniProt states
that it dephosphorylates phosphatidylglycerol phosphate and assigns RHEA:33751
[UniProtKB:Q88QH3, "Lipid phosphatase which dephosphorylates"].

The KT2440 pathway reconstruction explicitly places `pgpA` after `pgsA` in
phosphatidylglycerol formation [PMID:21895997, "pgpA– phosphatidylglycerophosphatase A"].
The exact activity and phosphatidylglycerol biosynthetic process are therefore
the informative annotations; generic lipid metabolism is less useful.

Whether another phosphatidylglycerol-phosphate phosphatase compensates for
PgpA in KT2440 remains an experimental question.

## 2026-11 update

Re-reviewed to completion alongside the E. coli exemplar in `genes/ECOLI/` used by the
module `bacterial_phosphatidylglycerol_cardiolipin_biosynthesis`. Broad parent terms
(membrane, phospholipid or lipid biosynthesis, generic transferase or catalytic activity)
that were previously kept as non-core are now refined with MODIFY to the specific terms
the gene carries, so that same-term rows are treated the same way across the PSEPK and
E. coli orthologues. Every row now cites vetted family-level or curated evidence. No
deep-research provider key was available.
