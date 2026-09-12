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

## Falcon integration (2026-06-21)

Integrated the FutureHouse Falcon deep-research report (`B3GALNT2-deep-research-falcon.md`) into the review. The report's conclusions broadly agree with the existing review (core M3 / matriglycan biology, ER-primary localization, avoidance of apoptosis/inflammation/pyroptosis/synaptic over-annotations). Changes made:

- **Added 1 reference: PMID:30898876** (Nakane et al. 2019, J Biol Chem 294:7433-7444, "Identification of mammalian glycoproteins with type-I LacdiNAc structures synthesized by the glycosyltransferase B3GALNT2"). Resolved from DOI 10.1074/jbc.ra118.006892 in the Falcon report; PMID confirmed via PubMed eutils; full text fetched into cache. `reference_review`: relevance MEDIUM, correctness VERIFIED. This is the one genuinely new primary paper in the report.
  - Adds: B3GALNT2-dependent type-I LacdiNAc (GalNAc-beta1,3-GlcNAc) on **N-glycans** of mainly intracellular/ER glycoproteins (LRP1, nicastrin) beyond the alpha-DG O-mannosyl glycan. [PMID:30898876 "Our results further revealed that LDN presence on low-density lipoprotein receptor-related protein 1 and nicastrin depends on B3GALNT2, indicating the occurrence of type-I LDN in vivo in mammalian cells."]
  - Provides independent localization evidence reconciling ER (core) vs Golgi (non-core): [PMID:30898876 "B3GALNT2 mainly localizes in the ER and partly in the Golgi apparatus"]. Used this verbatim quote as `supported_by` on the IBA Golgi-membrane annotation to back the KEEP_AS_NON_CORE call.
- **Enriched the IBA Golgi-membrane annotation summary** with the Nakane corroboration (no action change; KEEP_AS_NON_CORE retained, now better supported).
- **Refined the top-level `description`** to note the N-glycan/intracellular type-I LacdiNAc activity (kept project-independent, flagged its significance as not yet established) and to state ER-mainly/Golgi-partly localization.
- **Updated the third `suggested_question`** to reflect that the N-glycan substrate question is now partly addressed by PMID:30898876.

Falcon claims NOT acted on (with reasons):
- All other report citations are review/contextual papers (Praissman & Wells 2014, Sheikh 2017, Willer 2014, Endo 2015, Bouchet-Séraphin 2015, Bigotti & Brancaccio 2021, Sharaf-Eldin 2025, Togayachi 2026). They restate known core M3 / matriglycan pathway and disease biology already captured by the existing references and primary citations (PMID:23929950, PMID:23453667, PMID:14724282, Reactome). Adding them as citations would not strengthen any specific annotation; not added.
- Falcon repeatedly frames B3GALNT2 localization as "ER, not primarily Golgi" and at one point implies the Golgi annotation should be downweighted further. The existing review already keeps Golgi as non-core; the Nakane primary data ("mainly ER, partly Golgi") actually justifies *retaining* the Golgi annotation rather than removing it, so no REMOVE was applied (consistent with not overruling on partial evidence).
- Falcon's muscle/brain/ECM "biological process" discussion describes downstream disease consequences (cobblestone lissencephaly, sarcolemmal integrity, laminin binding). These are organism-level phenotypes of the glycosylation defect, not direct B3GALNT2 GO process functions; no new BP annotations proposed (the review already centers on GO:0035269 O-mannosylation). Consistent with Falcon's own annotation-risk assessment.
- No PMID was added for any claim that could not be resolved/fetched; the only resolvable new primary paper was Nakane 2019.
