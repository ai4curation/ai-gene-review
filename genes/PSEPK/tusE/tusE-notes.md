# tusE curation notes

## Functional assignment

PP_3996/Q88FT6 is the TusE-family terminal sulfur carrier in the contiguous
PP_3993-PP_3996 `tusD-tusC-tusB-tusE` locus. The target retains the terminal
cysteine noted by the OpenScientist sequence analysis and has the local
IPR007453 DsrC/TusE family assignment.
[file:PSEPK/tusE/tusE-uniprot.txt "DR   InterPro; IPR007453; DsrC/TusE."]

The mechanistic assignment comes from the reconstituted *E. coli* relay: TusE
promotes TusA-to-TusD sulfur transfer and interacts with MnmA-tRNA.
[PMID:16387657 "TusE also interacts with an MnmA-tRNA complex."] No direct
KT2440 sulfur-transfer experiment was identified, so the species assignment is
based on family, conserved residue, and operon context.

## Completion pass (module bacterial_mnma_trna_thiolation)

- Every existing row now carries verbatim support: KT2440 UniProt family
  signatures (InterPro, NCBIfam, HAMAP, PIRSF, PANTHER) and active-site features,
  the cached E. coli primary papers (PMID:16387657, PMID:16472754,
  PMID:12549933, PMID:16871210, abstract-only), and the OpenScientist locus and
  identity analysis (quoted, not treated as experimental evidence).
- Broad terms (tRNA processing, tRNA modification, transferase,
  sulfurtransferase) are MODIFIED to the specific terms the gene already
  carries, matching the treatment of the E. coli orthologs in
  genes/ECOLI/*. GOA and module files are no longer listed as references.
- No KT2440-specific experiment on the Tus relay or MnmA was found; all
  functional assignments are ortholog- and locus-based.
