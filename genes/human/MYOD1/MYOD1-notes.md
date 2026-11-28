# MYOD1 curation notes

Deep-research provider status: all API-backed providers were unavailable in this
workspace, and the installed `claude_code` provider failed with `Not logged in`.
The review therefore uses cached GOA PMIDs, Reactome summaries, UniProt, and
manual reading recorded here rather than a generated
`MYOD1-deep-research-<provider>.md` file.

MYOD1 is the human `PTHR11534:SF2` member of the PANTHER myogenic-factor family.
The fetched PAINT slice has no IRD/IKR loss on the human MYOD1 lineage. Its main
gains sit at `PTN000164853` for nucleus, Pol II cis-regulatory-region binding,
Pol II DNA-binding transcription-factor activity, regulation of Pol II
transcription, and positive regulation of myoblast differentiation, plus
`PTN000164854` for RNA polymerase II transcription regulator complex, skeletal
muscle cell differentiation, and positive regulation of skeletal muscle fiber
development.

The direct molecular core is nuclear bHLH dimerization and E-box/cis-regulatory
DNA binding coupled to Pol II transcriptional activation of skeletal-muscle
genes. UniProt's reviewed MYOD1 entry summarizes the activator role, promoter
co-occupancy with MYF5 and MYOG, and the need for bHLH dimerization.
PMID:11076940 adds direct promoter evidence at the human ACCbeta promoter, where
MyoD acts on two E-boxes and an additional GCCTGTCA element.

Two ComplexPortal rows on `GO:0043335` protein unfolding and `GO:1904949`
ATPase complex cite PMID:19818707, but that full-text paper is explicitly about
YOD1, also called OTUD2 or DUBA8, as a p97-associated otubain deubiquitinase in
ER dislocation. Those rows are treated as confirmed wrong-gene-product source
defects against ComplexPortal.

The PMID:10672515 rows are narrowed to what the abstract can support. MyoD
transduction was used to create myogenic converted fibroblasts for an annexin
VII isoform study; the abstract is enough for a broad positive
muscle-differentiation effect, but not for direct MYOD1 regulation of RNA
splicing, myotube development, or myoblast fusion.
