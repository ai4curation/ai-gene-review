# SMAD7 curation notes

Seed review started from the human Swiss-Prot record for SMAD7 (UniProtKB:O15105)
in PANTHER family PTHR13703. Automated deep research was attempted with the
Falcon recipe and `--fallback perplexity-lite`, but the installed
`deep-research-client` in the shared runtime only exposed `claude_code`, so no
provider deep-research file was generated. Because this campaign is constrained
to the main lane without extra sub-workers, the review used the cached GOA,
UniProt, PAINT, Reactome and primary-publication records.

SMAD7 is the broadly acting inhibitory SMAD. Its core functions are to inhibit
TGF-beta superfamily receptor signaling by binding type I receptors, to recruit
SMURF ubiquitin ligases to receptors, and to repress SMAD transcriptional
complexes in the nucleus. The receptor-level and nuclear mechanisms together
explain rows to negative regulation of TGF-beta, activin, BMP and SMAD signaling.

Rows to bare GO:0005515 protein binding were removed under the project
protein-binding policy. The repeated IPI rows describe real interactions with
SMAD signaling regulators, ubiquitin ligases, WW-domain proteins and
beta-catenin machinery, but GO:0005515 itself does not capture a mechanistic
SMAD7 activity.

The beta-catenin and adherens-junction rows from PMID:18593713 were kept as a
non-core SMAD7 output because the paper supports direct SMAD7-Axin and
beta-catenin effects that stabilize the beta-catenin-E-cadherin complex. The
obsolete GO:2000049 rows were replaced with the retained adherens junction
assembly term.

The shear-stress row from PMID:9256479 records transcriptional induction of
the SMAD6 and SMAD7 genes by laminar shear in endothelial cells. Expression
induction by flow is not a function performed by the SMAD7 gene product, so the
GO:0034616 row was marked over-annotated while the same paper was still used
for its direct SMAD6-SMAD7 interaction and transcription-inhibition evidence.
