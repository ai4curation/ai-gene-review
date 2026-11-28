# PADI1 notes

## 2026-11-28 manual review

`just deep-research-falcon human PADI2 --fallback perplexity-lite` could not run because the Falcon/agentapi launcher was unavailable in this checkout, so this family was reviewed manually from the seeded GOA rows, UniProt records, cached GOA publications, Reactome records, and PANTHER metadata.

Human PADI1 is an active, calcium-dependent peptidyl/protein arginine deiminase. The primary cloning paper produced recombinant human PAD type I and found it enzymically active [PMID:12416996, "A recombinant PAD type I was produced in Escherichia coli and shown to be enzymically active."]. Saijo et al. crystallized the active calcium-bound protein and found a unique monomeric solution state [PMID:27393304, "size-exclusion chromatography revealed PAD1 to be a monomer in solution"]. A later NNMT study directly used both PAD1 and PAD2 as NNMT-citrullinating enzymes, but this substrate context is not specific enough to add a new NNMT-related biological-process term [PMID:30044909].

PADI1 has no row-specific evidence for a PADI4-like nuclear histone role in the cached sources; the PANTHER nucleus row is therefore treated as over-propagation from PADI4. Generic `protein binding` rows are uninformative interaction-capture rows and are removed under the repository's protein-binding policy.

The PADI1 HPA GO_REF:0000052 annotation is an IDA Human Protein Atlas immunofluorescence curation to GO:0005829 cytosol; this supports resolving diffuse cytoplasmic localization to the cytosol child term.
