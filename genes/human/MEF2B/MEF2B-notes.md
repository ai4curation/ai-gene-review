# MEF2B curation notes

Automated Falcon deep research, with the `perplexity-lite` fallback, was unavailable in this worktree. This note records the manual evidence synthesis used for the MEF2B review.

MEF2B is the human RSRFR2/MEF2 family member. Human RSRF proteins recognize CTA(A/T)4TAG DNA, bind as dimers, and include RSRFR2/MEF2B, which differs from the MEF2A isoforms by seven conservative substitutions in the MADS/MEF2 core [PMID:1748287]. The MEF2 family cloning and mapping papers support MEF2B as one of four human MADS-box transcription-factor genes [PMID:1516833; PMID:8575763].

MEF2B is especially well represented in structural corepressor studies. A crystal structure of the human MEF2B MADS/MEF2S domain bound to DNA and a Cabin1 peptide showed how Cabin1 is recruited by the DNA-bound MEF2 dimer [PMID:12700764]. A subsequent HDAC9/MEF2/DNA structure showed that class II HDAC-binding motifs also occupy the same MEF2S hydrophobic groove and explained how class II histone deacetylases are recruited by MEF2 [PMID:15567413]. These structures support MEF2B DNA binding, dimerization, transcription-regulator-complex membership and HDAC binding.

The high-throughput HT-SELEX row from PMID:28473536 directly supports sequence-specific double-stranded DNA binding, but not the extra cis-regulatory context of RNA polymerase II promoter/enhancer binding. Several `GO:0005515` rows come from Cabin1/HDAC or large human interactome screens; Cabin1 and HDAC interactions are useful mechanistic evidence, but the bare protein-binding term is removed under the project protein-binding policy rather than used as a standalone molecular function.

The PANTHER family projects a heart-development row to MEF2B from PAINT node
`PTN002632019` with two ZFIN donors. This review did not verify the donor
symbols or the placement of that node in the PTHR11945 tree, and the available
human evidence only shows MEF2B transcript detection in developing heart
[PMID:10458488]. The `GO:0007507` row is therefore left `UNDECIDED` pending a
direct node-level check. The old `muscle organ development` TAS row from the
original human MEF2 cloning literature is kept as a broad, non-core family
context.
