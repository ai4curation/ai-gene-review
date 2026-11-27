# flgM (PA3351, Q9HYP5) review notes

## Both annotations trace to one paper, and it is the right one

PMID:11872701 is titled "Identification and functional characterization of flgM, a gene encoding
the anti-sigma 28 factor in Pseudomonas aeruginosa", and it establishes the activity by two
independent routes:

- **Genetics.** [PMID:11872701 "The beta-galactosidase activity of a transcriptional fusion of the
  fliC promoter to lacZ was upregulated in the flgM mutant, suggesting that the activity of FliA,
  the sigma factor that regulates fliC, was increased."] An increase in a sigma-28-dependent
  promoter's output when *flgM* is gone is the signature of an anti-sigma factor, and the
  authors confirmed the consequence at the protein level: [PMID:11872701 "an increased amount of
  flagellin was demonstrated in the flgM mutant of P. aeruginosa strain PAK by Western blot"].
- **Direct binding.** [PMID:11872701 "Direct interaction of the P. aeruginosa FlgM with the
  alternative sigma factor sigma(28) was demonstrated by utilizing the yeast two-hybrid system."]

The sigma factor in question is FliA, which in PAO1 is **PA1455** (UniProt P29248, "RNA polymerase
sigma factor FliA"). The paper also localises the binding determinant:
[PMID:11872701 "A conserved region is present in the C-terminal half of the FlgM of P. aeruginosa
and in FlgM homologues of other organisms that includes the sigma(28) binding domain."] That is
consistent with the record, which matches `IPR031316 FlgM_C` alongside the family entries.

Note the strain caveat: the Western blot was done in strain **PAK**, not PAO1, while the *fliC*
fusion work is not strain-qualified in the abstract. The gene is the same in both, and the
annotation is on the PAO1 locus, so this is worth recording rather than acting on.

## Why the process row is kept general

`GO:0045892` negative regulation of DNA-templated transcription arrives by InterPro2GO from
`IPR007412 FlgM`. It is true, and it is kept rather than refined.

The temptation is to deepen it to `GO:2000143` negative regulation of DNA-templated transcription
initiation, as the sibling review of PA2895 (SbrR) carries — both proteins are anti-sigma factors
and both work by withholding a sigma factor, so the mechanism is the same shape. Two reasons not
to:

1. **This row's own evidence does not reach it.** The supporting entity is the FlgM family
   signature, which identifies the family and its sigma-28 binding domain but says nothing about
   which step of transcription is blocked. Under the 2026-11-14 ruling the test for MODIFY is the
   row's own evidence, and a family signature stops at the general term.
2. **The specific term is not asserted elsewhere in this review**, so `TOO_GENERAL` does not apply
   either — that action is for a term already entailed by a more specific one on the same gene.
   Here `GO:0045892` is the gene's only process claim, which is precisely the case the enum says
   to keep.

What PA2895 has and this gene does not is a paper reporting that the antagonised sigma factor
associates with RNA polymerase in vivo, which is what licenses the initiation term there. The
two reviews therefore differ, and that difference is evidential rather than inconsistent. A
cross-gene consistency argument would be the wrong basis for deepening a term here.
