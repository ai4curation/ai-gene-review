# TreeGrafter (method): suppress graft-node terms whose PAINT taxon excludes the query organism

**Destination:** PANTHER/TreeGrafter developers (pantherdb.org feedback, or
the TreeGrafter repository).

**Summary.** TreeGrafter copies a graft node's GO terms to the query protein
without checking the node's PAINT taxon. Ticket 2 shows choanoflagellate
cadherins inheriting 30 junction and catenin rows from a node PAINT records
at Bilateria (`taxon:33213`).

**Proposed QC rule.** If the PAINT taxon of the IBD node does not include the
query's organism, drop the term or flag it for curator review. The query and
taxon IDs are already in the pipeline, so the check is cheap. It would also
catch the general case of terms reaching proteins from organisms outside
the clade a node was curated for. Our corpus now has three such cases, in
tickets 2, 11 and 12.

**Repo references.** `projects/TREEGRAFTER/holozoan-hippo-case-study.md`;
`projects/ORIGINS_OF_MULTICELLULARITY/propagation-audit.md` (Case 6).
