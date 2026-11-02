# LIPA (lysosomal acid lipase) review notes

UniProt P38571 (LICH_HUMAN), HGNC:6617. Falcon deep research was launched for this gene but failed;
the synthesis below was done manually from the cached publications, the Reactome entries
and the UniProt record.

## Core biology

- LIPA encodes lysosomal acid lipase / cholesteryl ester hydrolase (LAL, EC 3.1.1.13), the
  only lysosomal enzyme hydrolyzing cholesteryl esters and triacylglycerols delivered to
  lysosomes by endocytosis of LDL
  [PMID:1718995 "The lysosomal enzyme catalyzes the deacylation of triacylglyceryl and cholesteryl ester core lipids of endocytosed low density lipoproteins; this activity is deficient in patients with Wolman disease and cholesteryl ester storage disease."].
- Purified human liver LAL hydrolyzes trioleoylglycerol, cholesteryl oleate and 1,2-/1,3-
  dioleoylglycerols; TAG and CE hydrolytic activities co-purify
  [PMID:7204383 "Trioleoylglycerol, cholesterol oleate, and 1,2- and 1,3-dioleoylglycerols were substrates for the purified enzyme"].
- Acid pH optimum, consistent with lysosomal action
  [PMID:8112342 "The purified enzyme was most active at low pH (4.5-5.0)"].
- LAL is synthesized as a preproprotein; the pro-region is required for folding and activity
  [PMID:15269241 "LAL is indeed a preproprotein, in which the pro-region is essential for its folding and stability, secretion, and enzyme activity"].

## Disease

- Biallelic LIPA variants cause lysosomal acid lipase deficiency: infantile-onset (Wolman
  disease) and childhood/adult-onset (CESD)
  [PMID:26225414 "The phenotypic spectrum of lysosomal acid lipase deficiency (LAL-D) ranges from an infantile-onset form (previously known as Wolman disease)"].
- Residual activity tracks severity
  [PMID:9633819 "WD is caused by genetic defects of LAL that leave no residual enzymatic activity, while in CESD patients a residual LAL activity can be identified."].
- dismech `Wolman_Disease` marks GO:0004771 sterol ester esterase activity and GO:0004806
  triacylglycerol lipase activity DECREASED in the lysosomal lumen, with GO:0046461 and
  GO:0019433 DECREASED: consistent with the core functions below.

## Annotation decisions (summary)

- Core: sterol ester esterase activity (GO:0004771), triacylglycerol lipase activity
  (GO:0004806), lysosome/lysosomal lumen.
- General IEA parent MF terms (lipase activity, hydrolase acting on ester bonds, carboxylic
  ester hydrolase) modified to the specific activities.
- Core BP in core_functions: GO:0046461 neutral lipid catabolic process and GO:0090122
  cholesterol ester hydrolysis involved in cholesterol transport (defined as lysosomal
  cholesterol ester hydrolysis that feeds intracellular cholesterol transport; currently
  annotated in GOA only to CES1 by TAS). Not entered as NEW existing_annotations.
