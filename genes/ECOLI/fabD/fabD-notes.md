# fabD (Escherichia coli K-12, UniProtKB:P0AAI9) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml`, where E. coli FabD is a
representative of the malonyl-ACP loading step beside P. putida FabD and the
mitochondrial transacylases MCT1/mct1. FabD transfers the malonyl group from
malonyl-CoA to the phosphopantetheine thiol of holo-ACP
[PMID:12842120 "Bacterial malonyl-CoA:acyl carrier protein transacylase catalyzes the transfer of a malonyl moiety from malonyl-CoA to the free thiol group of the phosphopantetheine arm of acyl carrier protein."],
making the building block that every condensation consumes. The gene was cloned by
complementing a thermosensitive mutant and its overexpression raised activity about
a thousandfold
[PMID:1314802 "Expression of the fabD gene in an appropriate E. coli expression vector resulted in an accumulation of the MCT protein of up to 10% of total soluble protein, which was accompanied by an approximately 1,000-fold increase in the MCT activity."].

All rows are accepted except the generic transferase term, which is TOO_GENERAL
because GO:0004314 is asserted on four rows. The IMP row cites PMID:4612036, whose
cached record has no abstract at all; rather than quote nothing, the row cites the
cloning paper that complemented the same fabD89 allele, and the reference review
records that the 1974 paper itself is unquotable.

## Annotation decisions (11 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | IBA | ACCEPT | Phylogenetic assignment of the malonyl-CoA:ACP transacylase activity across the FabD family, bacterial and mitochondrial. |
| GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | IDA | ACCEPT | The core transacylase activity, measured in a continuous coupled assay on malonyl-CoA and holo-ACP. |
| GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | IDA | ACCEPT | Transacylase activity of the cloned gene product: overexpression raised MCAT activity about a thousandfold. |
| GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | IEA | ACCEPT | Electronic assignment of the core transacylase activity from the FabD family signature. |
| GO:0005829 cytosol | IBA | ACCEPT | Phylogenetic assignment of cytosolic activity, with the E. coli protein itself as the node's seed. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from fractionation-based proteomic assignment. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from abundance profiling of the cytosolic fraction. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic assignment of fatty-acid biosynthesis across the transacylase family, the pathway the reaction feeds. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Electronic pathway assignment, consistent with the experimental and phylogenetic rows. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Mutant evidence: temperature-sensitive transacylase mutants are conditionally defective for fatty-acid synthesis. |
| GO:0016740 transferase activity | IEA | TOO_GENERAL | Correct but uninformative parent activity; the exact transacylase term is asserted on four rows of this review. |

**Core function:** enables GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity; in GO:0006633; located in GO:0005829

