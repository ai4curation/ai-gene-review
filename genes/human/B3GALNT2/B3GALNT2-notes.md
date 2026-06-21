# B3GALNT2 (Q8NCR0) — Research Notes

## Identity
- UDP-GalNAc:beta-1,3-N-acetylgalactosaminyltransferase 2 (Beta-1,3-GalNAc-T2). EC 2.4.1.313.
- GT31 family (CAZy), glycosyltransferase 31 / beta-1,3-glycosyltransferase motif family (Pfam Galactosyl_T, InterPro IPR002659). Type II single-pass membrane protein (cytoplasmic 1-6, TM 7-23, lumenal 24-500). [UniProt Q8NCR0]
- HGNC:28596, GeneID 148789, chromosome 1. MANE-Select NM_152490.5 / NP_689703.1 (isoform 1, 500 aa). Two isoforms.

## Core molecular function
- Beta-1,3-N-acetylgalactosaminyltransferase: transfers GalNAc from UDP-GalNAc in a beta-1,3 linkage onto a terminal beta-GlcNAc, forming the GalNAc-beta1-3-GlcNAc disaccharide. [PMID:14724282 abstract "Its N-acetylgalactosaminyltransferase activity was observed when N-acetylglucosamine (GlcNAc) beta1-O-benzyl was used as an acceptor substrate. The enzyme product was determined to have a beta1,3-linkage by NMR spectroscopic analysis, and was therefore named beta1,3-N-acetylgalactosaminyltransferase-II (beta3GalNAc-T2)."]
- Originally characterized in vitro (Narimatsu lab) as making "a unique carbohydrate structure, GalNAcbeta1-3GlcNAc" on N- and O-glycans, with no activity toward glycolipids; KM 5.4 uM for UDP-GalNAc. [PMID:14724282]. UniProt: "Has no galactose nor galactosaminyl transferase activity toward any acceptor substrate" — i.e. strict beta-1,3-GalNAc specificity (distinguishing it from B3GALT galactosyltransferases in the same GT31 family).

## Biological role — alpha-dystroglycan core M3 (matriglycan) pathway
- Acts coordinately with POMGNT2 (GTDC2) on protein O-mannose of alpha-dystroglycan (DAG1): POMGNT2 adds beta-1,4-GlcNAc to O-Man, then B3GALNT2 adds beta-1,3-GalNAc, forming the GalNAc-beta3-GlcNAc-beta4-Man trisaccharide (the "core M3" O-mannosyl trisaccharide). [PMID:23929950 "we prepared a secreted form of B3GALNT2 (B3GALNT2dTM) ... and incubated this protein with UDPGalNAc and the GlcNAc-beta4-Man-O-peptide produced by the GTDC2dTM reaction. MALDI-TOF/MS analysis confirmed that B3GALNT2 could transfer a GalNAc residue to the acceptor ... suggesting that B3GALNT2 and GTDC2 can synthesize GalNAc-beta3-GlcNAc-beta4-Man."]
- This trisaccharide is then phosphorylated at the 6-position of mannose by POMK (SGK196); phosphorylation requires the prior GalNAc-beta3-GlcNAc-beta terminus. Loss of B3GALNT2 blocks downstream phosphorylation. [PMID:23929950 "the cells from the CMD patients did not produce [32P]-phosphorylated DGFc340, indicating that phosphorylation of the alpha-DG O-mannose is inhibited by lack of the GalNAc-beta3-GlcNAc-beta-terminus from the mannose."]
- The phospho-trisaccharide (core M3) is subsequently extended (FKTN, FKRP, TMEM5/RXYLT1, B4GAT1, LARGE) into "matriglycan" [-3GlcA-beta3-Xyl-]n, which is the actual laminin-G ligand-binding moiety. B3GALNT2 itself does NOT bind laminin; it builds an internal linker. [PMID:23929950]

## Subcellular location
- Localizes to the endoplasmic reticulum in cells; missense disease variants (G247E, V268M) perturb ER localization. [PMID:23453667 "B3GALNT2 localized to the endoplasmic reticulum, and this localization was perturbed by some of the missense mutations identified." and "we transfected mutated V5-tagged constructs into C2C12 cells and observed that two of them (c.740G>A [p.Gly247Glu] and c.802G>A [p.Val268Met]) altered the ER localization"]
- UniProt also annotates Golgi apparatus membrane (by similarity, type II membrane protein) — typical for GT31 family. Note PMID:23453667 discusses that O-mannosylation occurs in the ER and that some GalNAc transferases can be ER-located, "which appears to be the case for B3GALNT2." So ER is the experimentally supported compartment for the alpha-DG function; Golgi membrane is the family-default/IBA location.

## Disease
- Biallelic loss-of-function/missense mutations cause muscular dystrophy-dystroglycanopathy congenital with brain and eye anomalies, type A11 (MDDGA11; MIM:615181), spectrum from severe Walker-Warburg syndrome to milder MEB/FCMD-like. A secondary congenital disorder of glycosylation (CDG) / dystroglycanopathy. [PMID:23453667 "mutations in B3GALNT2 can cause dystroglycanopathy with muscle and brain involvement."]
- Mechanism: hypoglycosylation of alpha-DG -> reduced laminin/ECM binding. Zebrafish b3galnt2 knockdown recapitulates muscle + brain phenotype and reduced functional alpha-DG glycosylation. [PMID:23453667]

## Interactions
- High-throughput binary interactome (HuRI/Y2H) reports interaction with TMBIM1 (Q969X1). [PMID:32296183; UniProt INTERACTION "Q8NCR0; Q969X1: TMBIM1; NbExp=3"]. This is a generic "protein binding" (GO:0005515) IPI — not informative of catalytic function; no evidence it is functionally relevant to the alpha-DG pathway.

## Tissue expression
- Expressed broadly; highest in testis, adipose tissue, skeletal muscle, ovary. [PMID:14724282]

## GO annotation observations (for review)
1. Over-annotation of downstream/process onto single-sugar enzyme: B3GALNT2 adds ONE GalNAc to one position; broad process terms "glycoprotein biosynthetic process" (GO:0009101) and generic "protein O-linked glycosylation" (GO:0006493) are not wrong but are unspecific. The more precise BP term is GO:0035269 "protein O-linked glycosylation via mannose" (the alpha-DG O-mannosyl glycan it actually elongates).
2. MF terms span a generality ladder: GO:0016758 hexosyltransferase activity (IEA, broad) < GO:0008194 UDP-glycosyltransferase activity (IBA, broad) < GO:0008376 acetylgalactosaminyltransferase activity (IDA/TAS, specific & experimentally supported). The IDA GO:0008376 is the best-supported MF; the broader IEA/IBA terms are over-general parents.
3. GO-gap (RHEA project): there is NO GO MF term specific to EC 2.4.1.313 ("protein O-mannose beta-1,3-N-acetylgalactosaminyltransferase" / the core-M3 GalNAc transfer). GO:0008376 is defined as transfer "to an oligosaccharide", which is broader than the protein-O-mannose-glycan acceptor B3GALNT2 actually uses in vivo. A new child term is warranted.
4. "protein binding" GO:0005515 (IPI, TMBIM1) is uninformative per curation guidelines; MODIFY/over-annotation.
5. Do NOT remove experimental annotations (IDA/IMP) on the basis of cached abstracts; all are consistent with the gene's verified function.
