# Csn1s1 (mouse alpha-S1-casein, "alpha-casein", P19228) - review notes

## Identity / family
- Calcium-sensitive casein of the SCPP-derived casein locus (mouse chr 5). UniProt: "Important role in the capacity of milk to transport calcium phosphate." Belongs to the alpha-casein family; 15 x 6-aa tandem repeats.
- Casein genes descend from SCPP genes [PMID:21245413 "Ca-sensitive caseins (α(s)- and β-caseins) bind Ca but precipitate at high Ca concentrations, whereas Ca-insensitive casein (κ-casein) does not usually interact with Ca but instead stabilizes the micelle."]
- Mouse naming: alpha-casein = Csn1s1; beta = Csn2; gamma-casein = Csn1s2a; epsilon = Csn1s2b; kappa = Csn3.

## Knockout (Kolb et al. 2011, PLoS One, full text cached)
- [PMID:21789179 "Absence of α-casein protein significantly curtails secretion of other milk proteins and calcium-phosphate, suggesting a role for α-casein in the establishment of casein micelles."]
- Milk Ca and phosphate down ~90%: [PMID:21789179 "the lower casein protein levels in α-casein deficient mice are accompanied by a significantly lower concentration of calcium and phosphate in milk"]
- Phosphate centres: [PMID:21789179 "In mouse milk, 3 of the phosphate centres are in present α-casein and only one in β-casein."]
- Pup growth: [PMID:21789179 "α-Casein deficiency severely delays pup growth during lactation and results in a life-long body size reduction compared to control animals"]
- Secondary effects: reduced transcription of other casein genes, ER stress markers (BiP, grp94, PDIA6) in milk -> indirect.
- Authors' interpretation: [PMID:21789179 "The data support a critical role for α-casein in casein micelle assembly."]

## Family-level biology
- [PMID:23958008 "As a result of forming micelles, nutritious milk can be secreted and stored without causing either pathological calcification or amyloidosis of the mother's mammary tissue."]
- Calcium phosphate sequestration through phosphorylated residues (bovine model) [PMID:30128695].

## Annotation judgements
- Extracellular region (all codes): accept; secreted milk protein.
- lactation IMP: accept (KO severely impairs milk protein/Ca-P secretion).
- nutrient reservoir activity IDA, molecular sequestering activity IMP: accept; core.
- response to estradiol/progesterone/DHEA/11-deoxycorticosterone (IBA): propagated from a bovine explant study (PMID:3585228) of steroid inhibition of casein synthesis at supraphysiological doses [PMID:3585228 "inhibition was only achieved by using concentrations of progesterone exceeding by 1000-fold those required for similar effects in tissue from non-lactating animals"]. The casein protein is an expression readout, not a participant in hormone response -> REMOVE.

## Deep research
- OpenScientist deep research not available at time of review (see final report).

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ and the points used were
checked against the abstracts (full text where cached).

- No contradictions with the review. The report's central claims (micelle scaffold,
  calcium phosphate sequestration, knockout curtails milk protein and calcium phosphate
  secretion and pup growth) match the review's core functions and its ACCEPT of lactation
  (IMP) and MODIFY of molecular sequestering activity to GO:0140314.
- Added to GO:0007595 lactation (IMP, PMID:21789179): PMID:10504344 (goat alpha-s1 null:
  ER export of the other caseins depends on alpha-s1-casein) and PMID:25549363 (rat: the
  membrane-associated form sits in cholesterol-rich ER microdomains; alpha-s1-casein "takes
  center stage" in micelle building and transport). These show the protein does part of
  the work of milk secretion, not only being its cargo.
- Added to GO:0140313 (MODIFY -> GO:0140314): PMID:25714333 (micelles sequester and
  transport amorphous calcium phosphate) and a quote from the report.
- Not used: casein-cluster super-enhancer regulation (PMID:37591874), CSN1S1-promoter
  transgenics (PMID:21881921), FAM20C, peptide activities (PMID:27765241, 25580741).
- No action changes.
