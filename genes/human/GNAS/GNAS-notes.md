# GNAS notes

## 2026-06-02

PITA context: The MONDO issue references GNAS for PITA3, but this local review is for UniProt `O95467`, the NESP55 product of the complex GNAS locus. This matters because many GNAS biological phenotypes belong to canonical Gs-alpha products or locus-level imprinting rather than direct NESP55 protein function.

Deep research status: Falcon deep research succeeded for GNAS and produced `GNAS-deep-research-falcon.md` plus an artifact table. The artifact explicitly warned that "NESP55 should not be conflated with canonical Gsalpha signaling protein products" [file:human/GNAS/GNAS-deep-research-falcon_artifacts/artifact-00.md "NESP55 should not be conflated with canonical Gsalpha signaling protein products"].

Functional summary: NESP55 is a chromogranin-like neuroendocrine secretory product. The cloning/processing paper found that the "NESP55 open reading frame encoded a hydrophilic protein" and characterized "posttranslational processing of a maternally expressed protein" [PMID:10729789 "NESP55 open reading frame encoded a hydrophilic protein"; PMID:10729789 "posttranslational processing of a maternally expressed protein"]. Pituitary adenoma IHC describes NESP55 as a "marker of the constitutive secretory pathway" with "brown finely granular cytoplasmic staining" [PMID:21584660 "marker of the constitutive secretory pathway"; PMID:21584660 "brown finely granular cytoplasmic staining"].

Annotation decisions: I kept cytoplasmic/secretory-context annotations, modified generic transport vesicle to secretory granule, and removed or over-annotation-marked Gs-alpha/locus-level phenotypes such as thermogenesis, organism growth, PTH response, and pregnancy. The PTH paper shows a deletion "that removes NESP55" and supports NESP55 as an "additional imprinting control element" [PMID:22378814 "A novel deletion of 18,988 bp that removes NESP55"; PMID:22378814 "NESP55 is an additional imprinting control element"], but that is not direct NESP55 protein activity.

