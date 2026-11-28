# MYF6 curation notes

Deep-research provider status: all API-backed providers were unavailable in this
workspace, and the installed `claude_code` provider failed with `Not logged in`.
The review therefore uses cached GOA PMIDs, Reactome summaries, UniProt, and
manual reading recorded here rather than a generated
`MYF6-deep-research-<provider>.md` file.

MYF6 is the human `PTHR11534:SF4` member of the PANTHER myogenic-factor family.
The fetched PAINT slice has no IRD/IKR loss on the human MYF6 lineage. MYF6
inherits the family-level PAINT gains for nucleus, Pol II cis-regulatory-region
binding, RNA polymerase II-specific DNA-binding transcription-factor activity,
skeletal-muscle differentiation, and positive regulation of myoblast or skeletal
muscle fiber differentiation.

The human reviewed UniProt entry states the main direct function at the current
level of accessible evidence: MYF6 is a myogenic factor involved in muscle
differentiation, induces fibroblasts to differentiate into myoblasts, is a
probable sequence-specific DNA-binding protein, and needs another bHLH protein
for efficient DNA binding. The two existing TCF12 interaction rows are the only
MYF6 protein-binding rows; both are refined from bare `GO:0005515` to bHLH
transcription factor binding because the UniProt interaction table records the
MYF6-TCF12 pair.
