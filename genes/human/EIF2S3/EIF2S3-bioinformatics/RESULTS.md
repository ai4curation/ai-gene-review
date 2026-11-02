# EIF2S3 reconstructed database results

The saved PTHR42854 tree and alignment each contain 345 entries. Human P41091 is unique, and its ungapped 472-residue sequence exactly matches the official sequence. All four imported IBA contexts join a positive IBD at an ancestor on the literal target path; the associated donor fields are retained rather than reduced to a donor count.

All 41 imported generic-binding contexts have literal matching records in the 197-row IntAct export. The retained fields distinguish methods, experimental species, features, record IDs and source publications. This establishes the provenance of the source-pair assertions, not uniform physical directness or native-context confidence.

| Dataset | Complete input rows | EIF2S3 incident rows | Selected rows |
|---|---:|---:|---:|
| OpenCell | 29,922 | 136 | 3 |
| BioPlex2 | 59,584 | 1 | 1 |
| BioPlex3 | 129,687 | 2 | 2 |

OpenCell selection asks for EIF2S3 as the tagged target and CDC123, EIF2S1 or EIF2S2 as the literal interactor label. All incident BioPlex rows are retained. The saved AP-MS graph contains one EIF2S3 incident edge, the CDC123 pair, with its original attributes. These selections do not collapse mixed protein groups or equate an affinity-purification result with purified binding.

All 15 Reactome source events have a selected forward input/output/component path to R-HSA-72514, human EIF2S3/P41091 in cytosol. The entity records initiator methionine 1 and chain 2–472; this is processing, not a natural alternative product. Database component paths are distinguished from primary-paper assays and from another component's kinase or nucleotide-exchange function.

The offline replay authenticates 22 archived input members, reproduces all three result objects and rejects changed input bytes. The parser adds no annotation, biological verdict or publication quotation. Source-specific experimental and access limits remain in the source guide and review reasons.
