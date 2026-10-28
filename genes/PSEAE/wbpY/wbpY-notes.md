# wbpY (PA5448, Q9HTB9) notes

No deep-research provider was available; literature research done manually (PubMed MCP + cached
publications).

## Identity

- UniProt Q9HTB9 (TrEMBL, unreviewed; PE 4), 375 aa, *P. aeruginosa* PAO1, locus PA5448, in the
  A-band (common polysaccharide antigen, CPA) cluster next to wbpX (PA5449, G3XCU3) and wbpZ.
- GT4 (CAZy) GT-B fold glycosyltransferase: Pfam PF13439 Glyco_transf_4 and PF00534
  Glycos_transf_1; PANTHER PTHR46401 (GLYCOSYLTRANSFERASE WBBK-RELATED) SF2.

## Function

- CPA is a D-rhamnan homopolymer of trisaccharide repeats [D-Rha a1-2 D-Rha a1-3 D-Rha a1-3]n
  [PMID:35166992 "composed of a homopolymer of D-rhamnose (D-Rha) in trisaccharide repeating units"].
- 1998 genetics: wbpX, wbpY and wbpZ mutants lack A-band LPS while B-band is unaffected; WbpY was
  proposed to add alpha1-3 Rha [PMID:9680202 "Chromosomal wbpX, wbpY and wbpZ mutants were
  generated, and Western immunoblot analysis demonstrates that these mutants are unable to
  synthesize A-band LPS, while B-band synthesis is unaffected"]. Abstract only; the assignment of
  activities in that paper was by sequence and phenotype.
- WbpZ (the first D-RhaT) adds D-Rha a1-3 to GlcNAc/GalNAc-PP-lipid [PMID:25845842].
- 2022 biochemistry: recombinant WbpY transfers one D-Rha from GDP-D-Rha in alpha1-3 linkage onto
  the WbpZ product D-Rha a1-3 D-GlcNAc a-PP-lipid (NMR); WbpX adds a1-2 and a1-3 Rha; WbpX+WbpY
  together make D-Rha oligomers non-processively [PMID:35166992 "NMR spectroscopic analysis of the
  WbpY reaction product showed that WbpY transferred one D-Rha residue in α1-3 linkage to synthetic
  D-Rhaα1-3-D-GlcNAcα-O-PO3-PO3-(CH2)11-O-phenyl acceptor"].
- So WbpY is a GDP-D-rhamnose:D-Rha-a1,3-D-GlcNAc-PP-lipid a1,3-D-rhamnosyltransferase. GO has no
  D-rhamnosyltransferase term; rhamnosyltransferase terms sit under GO:0016758 hexosyltransferase
  activity, which is the most specific existing MF.

## GO structure

- GO:0009243 O antigen biosynthetic process is part_of GO:0009103 lipopolysaccharide biosynthetic
  process (OAK, sqlite:obo:go), so the LPS rows are correct but general for WbpY.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN005302544 | GO:0016757 glycosyltransferase activity | 2 (WbpY, WbpX) | 60 (22 taxa) | GO:0016757 glycosyltransferase activity, IMP, PMID:9680202 | INDIRECT-PHENOTYPE (term correct) | The 1998 MF assignment rests on mutant LPS phenotype plus sequence similarity, not an activity assay. The term is nevertheless true: WbpY (and WbpX) were shown in vitro to be GDP-D-Rha rhamnosyltransferases (PMID:35166992). Node conclusion sound for a GT4 clade; re-seed with IDA from PMID:35166992. |
| PTN000749272 | GO:0009103 lipopolysaccharide biosynthetic process | 1 (sole seed) | 51 (19 taxa) | GO:0009103 LPS biosynthetic process, IMP, PMID:9680202 | SOUND | Mutants lack A-band (CPA) LPS and WbpY itself catalyses a chain-extension step of the CPA O antigen, so participation in LPS biosynthesis is direct. LPS biosynthesis is a reasonable breadth for a WbbK-related GT4 subclade from O-antigen clusters; members in other species could instead make capsule or exopolysaccharide, which was not checked. |
