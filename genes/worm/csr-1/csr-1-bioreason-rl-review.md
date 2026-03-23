# BioReason-Pro RL Review: csr-1 (C. elegans)

Source: csr-1-deep-research-bioreason-rl.md

- **Correctness**: 1/5
- **Completeness**: 1/5

## Critical failure: wrong gene

BioReason analyzed the sequence for **nhr-47** (Q17370, a nuclear hormone receptor) rather than the actual CSR-1 protein (Q21992, an Argonaute). This is the same gene identity error documented extensively in the curated review, where the GOA file incorrectly mapped csr-1 to nhr-47 because csr-1 was listed as an old synonym for nhr-47 in some databases.

BioReason's analysis describes:
- Nuclear hormone receptor with NR2 subfamily membership
- Paired zinc-finger DNA-binding domain (HNF4-like)
- Ligand-binding domain with co-regulator switching
- Nuclear transcriptional regulator

## What CSR-1 actually is

CSR-1 is the only singly essential Argonaute protein in C. elegans (out of 24 Argonaute family members). Its actual biology:

| Feature | BioReason (wrong gene) | Actual CSR-1 |
|---------|----------------------|--------------|
| Protein type | Nuclear hormone receptor | Argonaute protein |
| Domains | Zinc fingers + ligand-binding domain | PAZ + PIWI domains |
| MF | DNA-binding TF activity | siRNA binding (22G-RNAs) |
| BP | Regulation of transcription | Chromosome segregation, gene silencing regulation |
| CC | Nucleus | P granules, chromosomes |
| Key function | Ligand-responsive transcription | Epigenetic gene activation (RNAa), germline protection from piRNA silencing |

## Failure mode analysis

**Garbage in, garbage out.** BioReason analyzed the wrong protein sequence entirely. The system has no mechanism to detect that the input sequence does not match the gene name. The NHR-47 analysis itself is technically competent domain-to-function reasoning for a nuclear receptor, but it describes the wrong protein. This is a database curation error that BioReason propagated uncritically.

This case demonstrates that sequence-only analysis without cross-referencing gene identity databases can lead to completely wrong conclusions. The curated review caught this error and marked all nhr-47-derived annotations for REMOVAL, replacing them with literature-derived CSR-1 Argonaute annotations.
