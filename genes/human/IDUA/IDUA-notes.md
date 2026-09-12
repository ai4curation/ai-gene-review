# IDUA (alpha-L-iduronidase) review notes

UniProt: P35475 (IDUA_HUMAN), EC 3.2.1.76, 653 aa precursor (signal 1-27, chain 28-653).
Family: glycosyl hydrolase family 39 (GH39; CAZy GH39). GO term for MF in GOA: **GO:0003940 L-iduronidase activity**.

## Core biology
IDUA is a lysosomal exo-glycosidase that hydrolyses terminal non-reducing alpha-L-iduronic
acid residues in the glycosaminoglycans heparan sulfate and dermatan sulfate, one of the
sequential steps of lysosomal GAG catabolism.

- FUNCTION (UniProt): "Lysosomal hydrolase responsible for the degradation of the glycosaminoglycans heparan sulfate and dermatan sulfate." [ECO:0000269|PubMed:7998955]
- CATALYTIC ACTIVITY (UniProt): "Hydrolysis of unsulfated alpha-L-iduronosidic linkages in dermatan sulfate.; EC=3.2.1.76"
- [PMID:24036510 "IDUA participates in the stepwise degradation of the glycosaminoglycans (GAGs) heparan sulphate and dermatan sulphate, by removing a single α-L-iduronyl residue from the non-reducing ends of these complex polysaccharides."]
- [PMID:24036510 "IDUA is an α-retaining glycoside hydrolase with strict substrate specificity for L-IdoA"] — retaining double-displacement mechanism, nucleophile Glu299, general acid/base Glu182.
- Structure: three domains (TIM barrel with active site, beta-sandwich, fibronectin type III). N-glycan at Asn372 forms part of the substrate-binding pocket and is required for full activity [PMID:23959878, PMID:24036510].
- Subcellular location: Lysosome (UniProt SUBCELLULAR LOCATION: Lysosome; lysosomal lumen GO:0043202). Trafficked via M6P pathway. Monomer.

## Disease
Deficiency causes mucopolysaccharidosis type I (MPS I): MPS1H (Hurler, MIM:607014, severe),
MPS1H/S (Hurler-Scheie, MIM:607015, intermediate), MPS1S (Scheie, MIM:607016, attenuated).
Urinary excretion of dermatan sulfate and heparan sulfate. Many missense variants curated in UniProt.
Mouse Idua-/- accumulates HS with a terminal iduronic-acid-capped disaccharide
[PMID:21873421 "representing the terminal iduronic acid residue capping the non-reducing end
of the HS chain, where no further degradation can occur in the absence of Idua"].

## Annotation review summary
- MF GO:0003940 L-iduronidase activity: core. Supported by IDA (PMID:24036510), EXP (PMID:23959878),
  TAS (PMID:2470345, Reactome), IBA. ACCEPT.
- GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds (IEA/InterPro): correct parent of
  GH39 activity but less informative than GO:0003940. KEEP_AS_NON_CORE.
- BP: heparan sulfate proteoglycan catabolic process (GO:0030200), dermatan sulfate proteoglycan
  catabolic process (GO:0030209), glycosaminoglycan catabolic process (GO:0006027): core, accept.
  IDA support for DS (PMID:24036510), IMP for HS/heparin (PMID:21873421, mouse Idua-/-).
- GO:0030211 heparin proteoglycan catabolic process (IEA/ARBA, IMP mouse): heparin is a highly
  sulfated variant of heparan sulfate; IDUA acts on the same alpha-L-iduronosidic linkages. Keep but
  non-core (heparin is a specialized subset; the physiological substrates are HS + DS).
- GO:0005975 carbohydrate metabolic process (IEA/InterPro): correct but very high-level parent;
  KEEP_AS_NON_CORE (subsumed by GAG catabolism).
- GO:0005984 disaccharide metabolic process (TAS PMID:2470345): the assay used HS/DS-derived
  disaccharide substrates; the physiological substrate is the polymer, not free disaccharides.
  MARK_AS_OVER_ANNOTATED (assay artifact / not the in vivo process).
- CC lysosome (GO:0005764), lysosomal lumen (GO:0043202): core, accept.
- GO:0070062 extracellular exosome (HDA PMID:23533145): mass-spec detection in prostatic-secretion
  urinary exosomes; typical for secretory/lysosomal proteins. KEEP_AS_NON_CORE (not the primary site).
- GO:0005102 signaling receptor binding (IEA/Ensembl, from rat ortholog D3ZE16): no evidence IDUA
  is a signaling receptor ligand; bare/uninformative binding term propagated electronically.
  MARK_AS_OVER_ANNOTATED.

## Core MF term used in core_functions
GO:0003940 L-iduronidase activity (exact GOA term; confirmed current label via OLS).
</content>
</invoke>
