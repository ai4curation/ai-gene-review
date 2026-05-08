# catA (catA-I, PP_3713) - Catechol 1,2-dioxygenase - Pseudomonas putida KT2440

## Gene Identity
- UniProt: Q88GK8 (TrEMBL, unreviewed)
- Locus tag: PP_3713
- EC: 1.13.11.1
- Gene name: catA-I (there is a paralog catA-II at PP_3166, Q88I35)
- Related reviewed entry: Q51960 (catA from P. putida strain arvilla/C1)
- PANTHER family: PTHR33711 (Intradiol Ring-Cleavage Dioxygenase)
- InterPro: IPR012801 (catechol dioxygenase, probable)

## Core Enzymatic Function
Catechol 1,2-dioxygenase catalyzes the intradiol (ortho) ring cleavage of catechol to cis,cis-muconate:
  catechol + O2 -> cis,cis-muconate + 2H+
This is step 1/3 in the beta-ketoadipate pathway converting catechol to 5-oxo-4,5-dihydro-2-furylacetate [PMID:12534463 "Complete genome sequence... Pseudomonas putida KT2440"].

## Cofactor
- Non-heme Fe(III) is the catalytic metal [PMID:14599591 "EPR study confirmed non-heme iron properties in organic solvents"]
- Conserved iron-coordinating residues: Tyr, His (by homology to characterized intradiol dioxygenases)

## Pathway Context - Beta-ketoadipate pathway
The beta-ketoadipate pathway (ortho-cleavage pathway) degrades aromatic compounds (benzoate, p-hydroxybenzoate) through catechol or protocatechuate as central intermediates. In P. putida KT2440:
- Benzoate -> catechol (via benABCD)
- Catechol -> cis,cis-muconate (catA, this gene)
- cis,cis-muconate -> muconolactone (catB, muconate cycloisomerase)
- muconolactone -> beta-ketoadipate enol-lactone (catC, muconolactone isomerase)

## Genetic Organization
- catA is part of the cat regulon in P. putida, though not in the same operon as catBC
- The catBCA operon is regulated by CatR (a LysR-type transcriptional regulator) with cis,cis-muconate as the inducer [PMID:9079907 "CatR and cis,cis-muconate required for catBCA transcription activation"]
- CatR binds at multiple sites: recognition binding site (RBS), activation binding site (ABS), and an internal binding site (IBS) within catB for repression [PMID:9573187 "Internal binding site for CatR within catB structural gene mediates repression"]
- Growth medium composition affects regulation - amino acids cause exponential silencing [PMID:11495992 "CatR-mediated transcription silenced on rich medium until stationary phase"]

## Paralog catA-II (PP_3166)
P. putida KT2440 has a second catechol 1,2-dioxygenase (catA-II, Q88I35, 304 aa). catA-I (PP_3713) is considered the primary enzyme in the beta-ketoadipate/cat pathway context.

## Substrate Specificity
- QSAR studies on catechol 1,2-dioxygenase from P. putida arvilla C1 show substituents at C4/C5 decrease activity - rate depends on nucleophilic reactivity (HOMO energy) of the catecholate [PMID:9799107 "Clear quantitative relationship between ln kcat and E(HOMO)"]
- The enzyme from P. putida is inhibited by C4-substituted catechols in a reversible manner

## Bioremediation Relevance
- catA from P. putida has been cloned and expressed in E. coli for enhanced biodegradation of the herbicide isoproturon [PMID:37751014]
- Catechol 1,2-dioxygenase enzymes are important for bioremediation of aromatic pollutants

## Structural Biology
- No crystal structure for P. putida catA-I specifically, but the intradiol dioxygenase family is well characterized structurally
- Crystal structure of related hydroxyquinol 1,2-dioxygenase PnpC from P. putida DLL-E4 shows conserved Fe(III) pentacoordination by Tyr160, Tyr194, His218, His220 [PMID:30446218]
- The intradiol mechanism involves Fe(III)-mediated activation of the substrate for O2 attack
