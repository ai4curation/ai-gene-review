# tusc2b notes

## Setup and provenance

- Fetched with `just fetch-gene` on Q6DH03 (TrEMBL, zgc:92701, 111 aa); 4 GOA rows (ND root MF,
  3 IBA from mouse Tusc2). ZFIN ZDB-GENE-040718-99, Ensembl ENSDARG00000025340, chromosome 22.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` was generated. Literature searched by hand via Europe PMC
  (same queries as tusc2a). No zebrafish study of either copy exists.
- Part of DANRE_DUPLICATION batch 4 (random sample, seed 20260928); paralog tusc2a. The shared
  analysis is in `genes/DANRE/tusc2a/tusc2a-bioinformatics/`.

## Background

Mammalian TUSC2 is a myristoylated mitochondrial regulator of calcium uptake
[PMID:24328503 "Our results establish Fus1 as one of the few identified regulators of mitochondrial calcium handling."]
(see tusc2a notes for the full background and quotes).

## Own analysis

See [tusc2a-bioinformatics/RESULTS.md](../tusc2a/tusc2a-bioinformatics/RESULTS.md). tusc2b keeps
Gly2 and the DEDGDLAHEFYEE motif; it is 65.8% identical to human TUSC2 and 77.7% to gar. It is the
main zygotic copy (26-51 TPM from blastula to larva) and has higher Bgee scores than tusc2a in most
adult tissues (top: muscle, somite, liver). ZFIN has one whole-organism in situ row (zygote to
pec-fin; ZDB-PUB-040907-1) with no restricted domain.

## Curation decisions

Same as tusc2a: ND MF accepted; mitochondrion and regulation of mitochondrial membrane potential
accepted; inflammatory response marked as over-annotated.
