# mut-7 (P34607) review notes

## Provenance / process
- Fetched with `just fetch-gene worm P34607 --alias mut-7` (Swiss-Prot P34607, 910 aa; same as module).
- Deep research FAILED (falcon timeout; perplexity fallback not configured). No deep-research file was written.

## Key findings
- RNase D homolog required for transposon silencing and RNAi [PMID:10535732 "We found one of the mutated genes, mut-7, to encode a protein with homology to RNaseD."].
- Biochemistry: recombinant MUT-7 is a 3'-5' exoribonuclease on ssRNA [PMID:39188014 "To test the exoribonuclease activity of MUT-7, we incubated recombinant MUT-7FL with a 5′-6-fluorescein amidite (5′-FAM)-labelled 28-mer ssRNA."], and MUT7-C binds RNA [PMID:39188014 "in C. elegans and human MUT-7, the MUT7-C domain contributes to RNA binding and is thereby crucial for ribonuclease activity"].
- Recruitment: [PMID:39188014 "Mutations disrupting the MUT-7/MUT-8 interaction prevent MUT-7 recruitment to Mutator foci and lead to RNAi resistance."].
- Localization: nucleus and cytosol [PMID:15653635 "Here, we show that the MUT-7 protein resides in complexes of approximately 250 kDa in the nucleus and in the cytosol."]; Mutator foci [PMID:22713602].
- Required for ERGO-1 26G siRNAs [PMID:21245313].

## Curation decisions
- IBAs for DSB repair via HR and mitochondrial matrix were removed, and the ssDNA exonuclease IBA was marked as over-annotated. All three come from the EXD2 lineage.
- The Nibbler-based miRNA 3'-end processing ISS rows were marked as over-annotated.
- The bare protein-binding rows (RDE-2/MUT-8) were removed for lack of functional information. The interaction itself is not disputed.
- The physiological substrate of MUT-7 in Mutator foci is unknown. This is a genuine biological gap.
