# GALNS (human) — review notes

UniProtKB:P34059 · HGNC:4122 · N-acetylgalactosamine-6-sulfatase (galactose-6-sulfate sulfatase; GalN6S) · EC 3.1.6.4

Deep research: falcon provider was out of credits (HTTP 402) at the time of this review, so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record
(`GALNS-uniprot.txt`), the seeded GOA (`GALNS-goa.tsv`), cached publications, and cached Reactome entries.

## Core biology (verified)

- **Molecular function.** GALNS is a lysosomal sulfatase that hydrolytically removes the 6-O-sulfate
  group from two terminal sugars: N-acetyl-D-galactosamine-6-sulfate (in chondroitin-6-sulfate) and
  D-galactose-6-sulfate (in keratan sulfate). EC 3.1.6.4.
  [PMID:22940367 "removes sulfate groups from a terminal N-acetylgalactosamine-6-sulfate (or galactose-6-sulfate) in mucopolysaccharides such as keratan sulfate and chondroitin-6-sulfate"]
  UniProt CATALYTIC ACTIVITY: "Hydrolysis of the 6-sulfate groups of the N-acetyl-D-galactosamine 6-sulfate
  units of chondroitin sulfate and of the D-galactose 6-sulfate units of keratan sulfate."
  The GO term GO:0043890 "N-acetylgalactosamine-6-sulfatase activity" has a definition that matches
  this exactly and is the correct core MF term (present in GOA as IEA, TAS, EXP, and IDA).

- **Formylglycine dependence.** Like all sulfatases, GALNS requires post-translational conversion of an
  active-site cysteine (Cys79, in a CXPXR motif) to Cα-formylglycine (3-oxoalanine), catalysed by the
  formylglycine-generating enzyme SUMF1/FGE; this modified residue is the catalytic nucleophile.
  [PMID:22940367 "FGE recognizes this motif and converts Cys 79 into a formylglycine aldehyde"]
  SUMF1 is the master regulator of all 17 human sulfatases; loss of SUMF1 causes multiple sulfatase
  deficiency. SUMF2 modulates (dampens) SUMF1 enhancement of sulfatase activity [PMID:15962010].

- **Cofactor / structure.** Homodimeric glycoprotein; each monomer binds one Ca2+ ion coordinating the
  formylglycine nucleophile [PMID:22940367]. Two N-glycosylation sites (Asn204, Asn423); three disulfide bonds.

- **Localisation.** Lysosome / lysosomal lumen. Immunostaining in cultured lung fibroblasts confirms
  lysosomal localisation [PMID:30760748 "GALNS indeed showed a lysosomal localization in both ever smokers and COPD patients"].
  As a secreted lysosomal hydrolase it is also detected extracellularly (extracellular exosome HDA
  PMID:23533145; extracellular region / azurophil granule lumen via neutrophil degranulation Reactome).

- **Biological process.** Catabolism of the glycosaminoglycans keratan sulfate and chondroitin-6-sulfate.
  GOA carries GO:0030207 chondroitin sulfate proteoglycan catabolic process (IDA, PMID:18285341 — modulating
  GALNS/ASB expression changes cellular chondroitin sulfate content). The keratan-sulfate side of the core
  BP is not yet in GOA; GO:0042340 (current label "keratan sulfate proteoglycan catabolic process") is the
  correct term and is added as a NEW annotation.

- **Disease.** Deficiency causes mucopolysaccharidosis type IVA (MPS IVA / Morquio A syndrome; MIM 253000),
  an autosomal recessive lysosomal storage disease with intracellular accumulation of keratan sulfate and
  chondroitin-6-sulfate; short stature, skeletal dysplasia, corneal clouding, normal intelligence.
  Extensive allelic heterogeneity; most missense mutations destabilise the fold rather than hit the active
  site [PMID:22940367].

## Annotation-by-annotation decisions (summary)

- GO:0004065 arylsulfatase activity (IBA) — ACCEPT. Family-level MF, correct but broad; PAN-GO/IBA term
  for the sulfatase family. Not the most specific term but not wrong.
- GO:0005764 lysosome (IEA, GO_REF:0000120) — ACCEPT. Consistent with IDA + UniProt SUBCELL.
- GO:0043890 N-acetylgalactosamine-6-sulfatase activity (IEA) — ACCEPT. This is the correct core MF.
- GO:0043890 (TAS, Reactome:R-HSA-2263490) — ACCEPT. Same correct MF, Reactome-sourced.
- GO:0005764 lysosome (IDA, PMID:30760748) — ACCEPT. Direct immunolocalisation.
- GO:0043890 (EXP, PMID:22940367) — ACCEPT. Structure/enzymology paper; correct core MF.
- GO:0030207 chondroitin sulfate proteoglycan catabolic process (IDA, PMID:18285341) — ACCEPT (non-core
  vs KS but a genuine core catabolic role). Core BP.
- GO:0043890 (IDA, PMID:18285341) — ACCEPT. Correct core MF, IDA.
- GO:0005576 extracellular region (TAS, Reactome R-HSA-6798751 neutrophil degranulation) — KEEP_AS_NON_CORE.
  Secreted-fraction / degranulation localisation, not the primary site of action.
- GO:0035578 azurophil granule lumen (TAS, Reactome) — KEEP_AS_NON_CORE. Neutrophil degranulation context.
- GO:0043202 lysosomal lumen (TAS, Reactome R-HSA-2263490) — ACCEPT. Precise site of action.
- GO:0070062 extracellular exosome (HDA, PMID:23533145) — KEEP_AS_NON_CORE. High-throughput proteomics of
  prostatic-secretion exosomes; localisation byproduct, not core.
- GO:0043202 lysosomal lumen (TAS, Reactome R-HSA-1630304) — ACCEPT. Precise site of action.
- GO:0008484 sulfuric ester hydrolase activity (IDA, PMID:15962010) — MARK_AS_OVER_ANNOTATED. Parent MF
  (sulfuric ester hydrolase); GALNS's specific activity GO:0043890 is the informative child. The SUMF1/SUMF2
  paper measured GALNS activity as one of several sulfatases; the general term is subsumed by the specific one.
- GO:0003943 N-acetylgalactosamine-4-sulfatase activity (TAS, PMID:8325655) — MODIFY → GO:0043890. This is
  the wrong specificity: GALNS is a 6-sulfatase; the 4-sulfatase is ARSB. The cited paper (PMID:8325655) is a
  chromosome-mapping abstract that does not assay 4-sulfatase activity. TAS (not experimental), so replacing
  the mistaken 4-sulfatase term with the correct 6-sulfatase term is appropriate.

## NEW
- GO:0042340 keratan sulfate proteoglycan catabolic process — the KS-degradation half of the core BP,
  supported by UniProt FUNCTION and the structure paper; Reactome models "Keratan sulfate degradation"
  (R-HSA-2022857) with GALNS.
