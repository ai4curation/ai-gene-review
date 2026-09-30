# SHLD2: human–horse sequence comparison

The downloaded human Q86V20 sequence (835 residues) and selected horse A0A9L0RGD6 sequence (883 residues) share 70.2% identity among 792 paired residues. Paired coverage is 94.9% of human and 89.7% of horse.

Full alignments, sequence hashes and calculation details: [SHLD2.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/SHLD2.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Human isoforms and horse C-terminus

The human canonical sequence Q86V20-1 has 835 residues; Q86V20-2 has 904 residues, containing the 69-residue insertion annotated by UniProt at position 654. The selected horse sequence retains the inserted OB-fold segment, with strong alignment through human isoform-2 residue 798. Beyond that point the horse C-terminus is substantially divergent and gapped. This is not a complete match to either human isoform. See [the long-isoform alignment](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/SHLD2-isoform2.json) and downloaded [human isoform 2](../../../../genes/human/SHLD2/SHLD2-isoform2.fasta). The sequence supports shieldin recruitment-module identity, but not an intact DNA-end-protection module without further model/structure checking.

Noordermeer et al. (PMID:30022168) show that their short splice form and an OB-fold mutant retain DSB recruitment and complex association while failing to suppress homologous recombination. Therefore, conserved localization cannot by itself establish repair-pathway regulation in this selected horse protein.
