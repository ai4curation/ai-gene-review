# CYP51A1 (Q16850) review notes

## Identity and core function
CYP51A1 = lanosterol 14-alpha-demethylase (LDM; sterol 14alpha-demethylase; P450 51A1; EC 1.14.14.154).
Cytochrome P450 monooxygenase (heme-thiolate, axial Cys binding residue at position 455, ligand Fe;
[file:human/CYP51A1/CYP51A1-uniprot.txt "axial binding residue"]). It is the only P450 species conserved
across phyla (animals, fungi, plants) [PMID:8619637 "which is the only P450 described so far to be expressed in different phyla"].

Catalyses the first post-lanosterol step of cholesterol biosynthesis: the three-step oxidative removal of the
14alpha-methyl group (C-32) of lanosterol and 24,25-dihydrolanosterol, released as formate, producing
4,4-dimethyl-cholesta-dienols (FF-MAS type intermediates) [file:human/CYP51A1/CYP51A1-uniprot.txt "the three-step oxidative removal of the"].
In mammals CYP51 also produces meiosis-activating sterols [PMID:20149798 "important intermediates, meiosis-activating sterols, are produced by CYP51"].

## Evidence highlights
- Purified human liver P450 catalysing lanosterol 14alpha-demethylation; demethylated 24,25-dihydrolanosterol
  and its oxygenated intermediates (32-OH, 32-oxo) to 4,4-dimethylcholesta-8,14-dien-3beta-ol
  [PMID:8399332 "catalyzing lanosterol 14 alpha-demethylation was \npurified from human liver"].
- cDNA cloned; E. coli expression confers lanosterol 14alpha-demethylase activity; expression regulated by
  oxysterols (SREBP-type sterol feedback) [PMID:8619637 "the cDNA encodes an enzyme having lanosterol 14 alpha-demethylase \nactivity"].
- Crystal structures (ligand-free + ketoconazole/econazole) confirm heme cofactor and monooxygenase mechanism;
  target of azole antifungals [PMID:20149798 "Three crystal structures of \nhuman CYP51"].
- ER membrane, single-pass membrane protein (TM 30-50) [file:human/CYP51A1/CYP51A1-uniprot.txt "Endoplasmic reticulum membrane"].
- Post-translationally regulated by MARCHF6 E3 ligase ubiquitination -> proteasomal degradation
  (PubMed:31904814; abstract not cached).

## Localization
ER membrane (GO:0005789) is well supported (Reactome TAS; UniProt SubCell; GO-CAM 6796b94c00001560).
GO:0016020 "membrane" (HDA, PMID:19946888, NK-cell membrane proteome) is a generic proteomics-detection
localization; less informative than ER membrane but not wrong -> keep as non-core.

## BP annotations to scrutinize
The Ensembl-Compara (IEA GO_REF:0000107) and ARUK-UCL (ISS GO_REF:0000024) annotations transferred from mouse
Cyp51 ortholog (UniProtKB:Q8K0C4):
- GO:0042177 negative regulation of protein catabolic process
- GO:0050709 negative regulation of protein secretion
- GO:1900222 negative regulation of amyloid-beta clearance
These are indirect/downstream phenotypic effects (likely from a specific mouse study linking cholesterol-synthesis
enzymes to APP/amyloid handling), not the core enzymatic function. Marked non-core / over-annotated; the ISS pair
is a curator sequence-similarity transfer so retained (not removed).

## GO-CAM
Model gomodel:6796b94c00001560 "Cholesterol biosynthesis from lanosterol (Human)": CYP51A1 activity =
GO:0008398 sterol 14-demethylase activity, part_of GO:0006695 cholesterol biosynthetic process,
occurs_in GO:0005789 endoplasmic reticulum membrane. Confirms the core-function triple used here.

## Core function summary
MF: GO:0008398 sterol 14-demethylase activity (heme/iron-dependent P450 monooxygenase).
BP: GO:0006695 cholesterol biosynthetic process (first post-lanosterol step).
CC: GO:0005789 endoplasmic reticulum membrane.
No common Mendelian disease (rare recessive CYP51A1 deficiency described as a cataract-hepatopathy syndrome per
Orphanet 521432, but not a common disorder).
