# Csn2 (mouse beta-casein, P10598) - review notes

- UniProt FUNCTION: "Important role in determination of the surface properties of the casein micelles." Calcium-sensitive casein; single phosphate centre in mouse [PMID:21789179 "In mouse milk, 3 of the phosphate centres are in present α-casein and only one in β-casein."]
- Knockout (Kumar et al. 1994): [PMID:8016126 "Homozygous beta-casein mutant mice are viable and fertile; females can lactate and successfully rear young."]; [PMID:8016126 "Despite the deficiency of beta-casein, casein micelles were assembled in heterozygous and homozygous mutants, albeit with reduced diameters."]; [PMID:8016126 "The growth of pups feeding on the milk of homozygous mutants was reduced relative to those feeding on the milk of wild-type mice."]; [PMID:8016126 "The results presented here demonstrate that beta-casein has no essential function and that the casein micelle is remarkably tolerant of changes in composition."]
  - Note: the PMID suggested in the task brief (9671715) is a plasmid DNA segregation paper; the correct Csn2 KO PMID is 8016126.
- In alpha-casein KO milk, beta-casein drops >=50% [PMID:21789179 "indicating at least a 50% reduction in β-casein protein concentration in milk"].
- cysteine-type endopeptidase inhibitor activity: IBA/ISO from human beta-casein IDA [PMID:12788072 "beta-Casein and the active domain, synthesized L(133)-Q(151), peptide inhibited cysteine proteases."] -- reverse zymography in vitro, peptide-centred; in vivo physiological role unproven; beta-casein is itself a major protease substrate in milk. Mark over-annotated.
- Lactation: accept as a broad process (micelle component secreted in milk; KO reduces micelle size and pup growth), not essential.

## Deep research
- OpenScientist deep research not available at time of review.

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ and the points used were
checked against the abstracts.

- No contradictions with the review. The report's primary function (calcium phosphate
  sequestration, micelle building, nutrient supply, lactation) matches the core
  functions; it also treats beta-casomorphins as digestion products.
- Added to GO:0140314 (NEW): PMID:42439892 (mouse Ergic2/3 knockout: less phosphorylated
  beta-casein in milk and poorer offspring growth; correlative, since the whole secretome
  is affected), PMID:31928725, and a quote from the report.
- Checked but not adopted: the report presents the self-association data of PMID:3401012
  as beta-casein biophysics generally; that paper studies nonphosphorylated human
  beta-casein. Golgi-vesicle micelle assembly (PMID:6581043, 6586179) is rat work on caseins
  in general; a Golgi lumen location for mouse beta-casein was not proposed from it.
  Expression control (PMID:37591874, 27129249), Fam20C, SPCA calcium pumping
  (PMID:16025219, 6302145; properties of other proteins) and microtubule transport
  (PMID:1400631) were not used for annotation.
- No action changes.
