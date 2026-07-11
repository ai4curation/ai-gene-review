# G6PC3 (Q9BUM1) review notes

## Identity
- Glucose-6-phosphatase 3 / glucose-6-phosphatase-beta (G6Pase-β) / ubiquitous
  glucose-6-phosphatase catalytic subunit-related protein (UGRP). EC 3.1.3.9.
- 346 aa, integral ER membrane protein, 9 transmembrane helices with the active
  site (Arg79, His114, His167) on the lumenal side of the ER membrane
  [UniProt Q9BUM1; PMID:14718531].
- Paralog of the liver/kidney/intestine-restricted G6PC1 (G6Pase-α). ~8x less
  active than G6Pase-α under the same conditions
  [PMID:25492228 "G6Pase-α is eight times more active than G6Pase-β"].

## Molecular function (well supported, experimental)
- Hydrolyzes glucose-6-phosphate (G6P) to glucose + inorganic phosphate in the ER
  [UniProt CATALYTIC ACTIVITY: RHEA:16689, EC 3.1.3.9].
- Forms a covalent phosphohistidine enzyme intermediate at His167 during catalysis;
  active-site mutants R79A, H114A, H167A abolish the intermediate/activity
  [PMID:14718531].
- Disease mutations abolish or reduce phosphohydrolase activity in a sensitive
  rAd/COS-1 assay: 14/16 missense mutants had complete loss; S139I and R189Q
  retained ~49%/45% (and are argued non-pathogenic) [PMID:25492228].
- UniProt CAUTION notes PubMed:12370122 (the original UGRP cloning paper) reported
  no hydrolytic activity, but later studies (PubMed:12965222, 13129915) established
  bona fide G6P hydrolase activity; the catalytic function is now well established.

## Cellular component
- ER membrane, multi-pass; active site in the ER lumen [UniProt SUBCELLULAR
  LOCATION; PMID:14718531; PMID:25492228 "an enzyme embedded in the endoplasmic
  reticulum membrane"]. HPA IDA supports ER localization.
- Membrane (GO:0016020) HDA from an NK-cell membrane-proteome MS survey
  (PMID:19946888) — generic membrane, less informative than ER membrane.

## Biological process
- Directly hydrolyzes G6P → glucose 6-phosphate metabolic process (GO:0051156)
  and intracellular glucose production.
- Works with the ER G6P transporter SLC37A4 (G6PT); the ubiquitous G6Pase-β/G6PT
  complex "maintains energy homeostasis and functionality in neutrophils and
  macrophages" [PMID:25492228].
- Gluconeogenesis (GO:0006094): G6PC3 is ubiquitously expressed and, unlike the
  hepatic G6PC1, is not a classic gluconeogenic/glucose-homeostasis enzyme; its
  clinical phenotype is neutropenia, not fasting hypoglycemia. Gluconeogenesis is
  an IBA/IEA/Reactome pathway-level assignment shared with the family; kept as
  non-core rather than a core function.

## Disease
- Severe congenital neutropenia type 4 (SCN4, MIM 612541), autosomal recessive;
  maturation arrest of granulopoiesis, ER stress and enhanced neutrophil apoptosis
  [UniProt DISEASE; PMID:25492228]. Also Dursun syndrome (DURSS).
- Non-hematological features: prominent superficial venous pattern, congenital
  cardiac anomaly, urogenital malformations [PMID:25492228].

## Curation decisions summary
- Core MF: GO:0004346 glucose-6-phosphatase activity (multiple lines: EXP/IMP/IBA).
- Core CC: GO:0005789 endoplasmic reticulum membrane.
- Core-adjacent process: GO:0051156 glucose 6-phosphate metabolic process.
- Gluconeogenesis annotations kept as non-core.
- GO:0016020 membrane (HDA) marked over-annotated (generic, superseded by ER membrane).
- GO:0005783 endoplasmic reticulum (IBA/IEA/IDA) accepted as correct but non-core
  parent of ER membrane where applicable.
