# CSN2 (Bos taurus, beta-casein, P02666) - curation notes

## Identity and family
- Secreted milk phosphoprotein, signal peptide 1-15, mature chain 16-224; phosphoserine cluster
  Ser30/32/33/34 (+Ser50) [file:BOVIN/CSN2/CSN2-uniprot.txt "Phosphoserine"].
- Calcium-sensitive casein of the SCPP family. Caseins arose from tooth/SCPP genes;
  Ca-sensitive caseins (alpha-s and beta) descend from a CSN1/2 ancestor [PMID:21245413
  "Ca-sensitive caseins (α(s)- and β-caseins) bind Ca but precipitate at high Ca concentrations,
  whereas Ca-insensitive casein (κ-casein) does not usually interact with Ca but instead stabilizes the micelle"].
- SCPP cluster: [PMID:12646701 "Casein makes milk supersaturated with Ca-phosphate, which
  was critical to the successive mammalian divergence."]

## Core biology
- Calcium phosphate sequestration: [PMID:25632319 "In milk, a stable fluid is formed in which sequestered
  nanoclusters of calcium phosphate are substructures in casein micelles."]
- Intrinsically disordered, partially folds on Ca binding [PMID:24918971 "We show that CAS partially folds and
  stiffens upon calcium binding"].
- Chaperone-like / anti-amyloid: [PMID:23958008 "As a result of forming micelles, nutritious milk can be secreted
  and stored without causing either pathological calcification or amyloidosis of the mother's mammary tissue."]
- Phosphorylated in the Golgi by FAM20C [PMID:26091039 "We demonstrated that one of these kinases, Fam20C, is the bona fide “Golgi casein kinase”"].
- Mouse knockout: [PMID:8016126 "Despite the deficiency of beta-casein,
  casein micelles were assembled in heterozygous and homozygous mutants, albeit
  with reduced diameters."; "The growth of pups feeding on the milk of homozygous mutants was reduced"].
  => beta-casein contributes to milk protein supply but is not essential for micelle formation or lactation.
  (Mouse Csn2 knockout: PMID:8016126, Kumar et al. 1994 PNAS.)

## Annotation themes
- 17 IPI "protein binding" rows: beta-casein used as model substrate for proteases HtrA2/3/4, DegP, LONP1 and
  kinase FAM20C (e.g. [PMID:24520911 "Both ATPase and peptidase activities can be stimulated by the binding of a larger protein
  substrate, such as β-casein."]). Substrate interactions; uninformative -> REMOVE.
- Cysteine protease inhibition (PMID:12788072): reverse zymography + synthetic L133-Q151 peptide in vitro; no in vivo
  evidence; beta-casein is itself a protease substrate -> MARK_AS_OVER_ANNOTATED (IDA and IBA).
- beta-CN(1-28) plasmin fragment blocks apical K+ channels and is proposed as a milk-borne negative-feedback signal
  (PMID:11045601, PMID:19563620). Fragment is generated in milk by endogenous plasmin; injection into udder lumen
  reduces milk yield -> KEEP_AS_NON_CORE for K+ channel inhibitor and negative regulation of lactation.
- NF-kB / TNF / inflammation (PMID:25038658): tryptic hydrolysate peptides in HEK reporter cells -> MARK_AS_OVER_ANNOTATED.
- Steroid "response to" terms (PMID:3585228): total casein synthesis/mRNA in explants inhibited by high-dose steroids;
  expression-level effect -> MARK_AS_OVER_ANNOTATED.
- Golgi (PMID:5168866): micelles form in Golgi vesicles -> Golgi lumen KEEP_AS_NON_CORE, Golgi apparatus TOO_GENERAL.

## Deep research
- OpenScientist deep research was not yet available when this review was completed; review based on primary literature, UniProt and cached publications.
