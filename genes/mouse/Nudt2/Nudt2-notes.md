# Nudt2 (mouse, P56380) review notes

## Summary of evidence

- Mouse Nudt2 (Apah1) is the PTHR21340:SF0 asymmetrical Ap4A hydrolase, 147 aa, Nudix box
  at 43-64, Tetra_PHTase signature (IPR003565). Orthologue of human NUDT2 and worm ndx-4.
- No direct Ap4A assay on the mouse protein; the activity is transferred from pig P50584
  and worm Q9U2M7. Worm ndx-4 kinetics:
  [PMID:11738085 "It hydrolyses Ap4A with a K(m) of 7 microM and k(cat) of 27 s(-1) producing AMP and ATP as products."]
- In cells, the mammalian Nudt2 product turns over Ap4A in activated mast cells, affecting
  MITF/USF2 target genes (abstract does not state species/cell lines):
  [PMID:18644867 "The knockdown of Ap(4)A hydrolase modulated Ap(4)A accumulation, resulting in changes in the expression of MITF and USF2 target genes."]
- Recombinant mouse Nudt2 decaps dpCoA- and FAD-capped RNA in vitro (catalytic EE-QQ
  mutant inactive), no deNADding; loss of Nudt2 in cells did not alter FAD-capped RNA:
  [PMID:32432673 "Additionally, we identify seven Nudix proteins (Nudt2, Nudt7, Nudt8, Nudt15, Nudt16 and Nudt19) that possess dpCoA cap decapping (deCoAping) activity in vitro, and two Nudix proteins (Nudt2 and Nudt16) possessing FAD cap decapping (deFADding) activity."]
  [PMID:32432673 "while a similar function cannot be attributed to Nudt2 at least under the growth conditions and the cells employed"]
  (Note the abstract lists six names for "seven" proteins; Figure 3C text adds Nudt12.)
- Mitochondrion HDA from MitoCarta proteomics; Nudt2 not discussed in the text
  [PMID:18614015 "we performed mass spectrometry, GFP tagging, and machine learning to create a mitochondrial compendium of 1098 genes and their protein expression across 14 mouse tissues."]
- Family-wide in vitro PRPP pyrophosphatase activity, minor for Ap4A hydrolases (human
  enzyme kcat 0.057 s-1) [PMID:12370170]; mouse has no PRPP annotation, so not used.

## Curation decisions (consistent with genes/worm/ndx-4)

- GO:0004081 (IBA, IEA, 2x ISS): ACCEPT.
- GO:0008796 IEA: ACCEPT (broader parent).
- GO:0016787 hydrolase IEA: MODIFY -> GO:0004081.
- GO:0006167 AMP / GO:0006754 ATP biosynthetic process (IBA from PTN000482012):
  MARK_AS_OVER_ANNOTATED; product-based, node seeded solely by worm ndx-4 IDA rows that
  were themselves marked over-annotated.
- GO:0006915 apoptotic process ISS (from worm, citing the structure paper PMID:11937063):
  REMOVE; transfer of a speculative statement whose worm TAS source was removed.
- GO:0005739 mitochondrion HDA: KEEP_AS_NON_CORE (experimental, cannot check supplement;
  human NUDT2 independently has a mitochondrial matrix annotation).
- NEW GO:0015967 diadenosine tetraphosphate catabolic process (ISS, PMID:18644867):
  the enzyme performs the hydrolytic step; comparator ndx-4 carries it by IDA.
- RNA cap decapping: no GO terms exist for FAD-cap/dpCoA-cap decapping (GO:0110155 is
  NAD-cap only, and Nudt2 lacks deNADding). In vitro only and without a cellular effect,
  so no NEW term proposed; raised as a suggested question.

## PAINT notes

PTN000482012 IBDs for GO:0006167 and GO:0006754 cite only WB:WBGene00003581 (ndx-4).
These product-based process terms propagate to all SF0 members (mouse, human, ...); the
appropriate node-level process would be GO:0015967.

## Additional literature (found via deep research, verified against cached abstracts)

- Mouse Nudt2 decaps m7G- and G-capped RNA in vitro, producing m7GMP and m7GDP:
  [PMID:23353937 "Here we demonstrate that six additional mouse Nudix proteins--Nudt2, Nudt3, Nudt12, Nudt15, Nudt17, and Nudt19--have varying degrees of decapping activity in vitro on both monomethylated and unmethylated capped RNAs."]
- Human NUDT2 knockout raises Ap4A 175-fold:
  [PMID:27144453 "KBM-7 cells in which the NUDT2 Ap4A hydrolase gene had been disrupted (NuKO cells), causing a 175-fold increase in intracellular Ap4A"]
- Ap4A is a 5' RNA cap; NUDT2 and DXO cleave Ap4A-RNA in vitro:
  [PMID:37934413 "A decapping enzyme screen identifies two enzymes cleaving Ap4 A-RNA,NUDT2 and DXO, both of which also cleave other substrate RNAs in vitro."]
- Human biallelic NUDT2 variants cause a neurodevelopmental disorder; decapping implicated:
  [PMID:38141063 "Importantly, add-back experiments using an Ap4A hydrolase defective in mRNA decapping highlighted loss of NUDT2 decapping as the activity implicated in altered mRNA homeostasis."]
  The deep research report reads this as a NUDT2 separation-of-function variant; the
  abstract does not say which Ap4A hydrolase was used, so that interpretation is not adopted.

Decapping GO terms considered and not proposed: GO:0140933 (m7GDP-releasing) and
GO:0140932 (m7GMP-releasing) each capture only one of Nudt2's two products; the evidence
for mouse is in vitro, and the physiological cap substrate (m7G vs Ap4A) is unresolved.
Raised as a suggested question.

## Deep research status

OpenScientist completed 2026-10-08 (~14 min): `Nudt2-deep-research-openscientist.md`.
Most claims are orthologue-based (Drosophila Apf nuclear localization [PMID:17344088],
human structure [PMID:23384440], LysRS-Ap4A-HINT1-MITF axis [PMID:14975237]); none
change the curation decisions. It confirms no Nudt2 knockout mouse phenotype was found.
