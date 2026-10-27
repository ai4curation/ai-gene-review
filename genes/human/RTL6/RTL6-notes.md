# RTL6 (SIRH3 / Retrotransposon Gag-like 6) — curation notes

RTL6 is the most conserved eutherian *sushi-ichi*/Ty3-gypsy-derived (Gag-like)
domesticated gene. Human review is by orthology to mouse functional studies (ISS).

## Function
- A **pre-made, secreted microglial factor** that accumulates on bacterial
  lipopolysaccharide, forming RTL6-cored complexes that trap LPS
  [PMID:37834332 "there await their targets, such as dsRNA and LPS"].
- Mouse *Rtl6* knockout reduces removal of LPS injected into the brain, with
  dsRNA clearance unaffected
  [PMID:36162816 "indicating that LPS removal was significantly reduced in the Rtl6 KO mice"].
- Strong conservation argues for an important role
  [PMID:36162816 "This indicates that RTL6 has been powerfully conserved in eutherians, suggesting that the role of RTL6 in LPS removal is vitally important, because LPS is an extremely dangerous pathogen."].

## Curation decisions
- RTL6 is the effector trap, so the review uses GO:0050829 defense response to
  Gram-negative bacterium rather than cellular response to lipopolysaccharide.
- Direct LPS binding is inferred from the arginine-rich basic surface, not
  demonstrated; left as a knowledge gap.
- The standalone GO:0045087 innate immune response proposal was dropped.
