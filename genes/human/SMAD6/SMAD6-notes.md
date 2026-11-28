# SMAD6 curation notes

Seed review started from the human Swiss-Prot record for SMAD6 (UniProtKB:O43541)
in PANTHER family PTHR13703. Automated deep research was attempted with the
Falcon recipe and `--fallback perplexity-lite`, but the installed
`deep-research-client` in the shared runtime only exposed `claude_code`, so no
provider deep-research file was generated. Because this campaign is constrained
to the main lane without extra sub-workers, the review used the cached GOA,
UniProt, PAINT, Reactome and primary-publication records.

SMAD6 is a BMP-biased inhibitory SMAD. The core cytosolic mechanism is
R-SMAD sequestration: human SMAD6 binds BMP-activated SMAD1 and prevents
formation of SMAD1-SMAD4 signaling complexes. SMAD6 also works as an adaptor
for SMURF-family ubiquitin ligases toward substrates including RUNX2, TBX6 and
MYD88. Those adaptor annotations are direct molecular functions, whereas the
downstream changes in osteoblast, muscle or innate-immune outputs were kept
outside the core.

Rows to bare GO:0005515 protein binding were removed under the project
protein-binding policy. The interactions with SMAD1, SMAD7, PRKX, TSC22D1 and
RUNX2 were retained through more specific terms only when the GOA row carried
one.

The shear-stress row from PMID:9256479 records transcriptional induction of
the SMAD6 and SMAD7 genes by laminar shear in endothelial cells. Expression
induction by flow is not a function performed by the SMAD6 gene product, so the
GO:0034616 row was marked over-annotated while the same paper was still used
for its direct SMAD6-SMAD7 and SMAD6-R-SMAD interaction evidence.

Developmental and clinical phenotypes caused by loss of SMAD6 in mouse or
human cardiovascular development were kept as non-core consequences of faulty
BMP inhibition. Xenopus animal-cap axis patterning after forced expression of
human SMAD6 was not kept as a native human SMAD6 biological process.
