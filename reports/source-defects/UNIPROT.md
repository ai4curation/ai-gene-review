# Source-record defects for UNIPROT

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9LD83 involved_in GO:0090333 regulation of stomatal closure (IMP, PMID:29463779)
- **Field:** GO_ID
- **Change:** GO:0090333 → GO:0090332 (stomatal closure)
- **Recorded in:** `genes/ARATH/SLAC1/SLAC1-ai-review.yaml`

This IMP row annotates SLAC1 (Q9LD83, AT1G12480) to regulation of stomatal closure from the loss of light-stress-induced stomatal closure in slac1 mutants (PMID:29463779). SLAC1 is the guard-cell S-type anion channel whose anion efflux carries out the closing movement, so the phenotype supports participation in stomatal closure (GO:0090332) rather than regulation of it.

> Furthermore, this response depended on the function of genes encoding the ROS-generating NADPH oxidase RBOHD and various stomatal regulators, such as the anion channel SLAC1
> — PMID:29463779
