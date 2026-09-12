# PCYT2 (Q99447) review notes

Human gene: **PCYT2** = ethanolamine-phosphate cytidylyltransferase (ET);
CTP:phosphoethanolamine cytidylyltransferase. HGNC:8756. UniProt Q99447 (PCY2_HUMAN),
389 aa, EC 2.7.7.14.

## Core function (well established)

PCYT2/ET catalyzes the **second and rate-limiting step of the CDP-ethanolamine
(Kennedy) pathway of phosphatidylethanolamine (PE) biosynthesis**:
phosphoethanolamine + CTP + H(+) -> CDP-ethanolamine + diphosphate.

- UniProt: "Ethanolamine-phosphate cytidylyltransferase that catalyzes the second step
  in the synthesis of phosphatidylethanolamine (PE) from ethanolamine via the
  CDP-ethanolamine pathway" [file:human/PCYT2/PCYT2-uniprot.txt "the second step in the synthesis of phosphatidylethanolamine (PE) from"].
- UniProt CATALYTIC ACTIVITY: Rhea:RHEA:24592; EC=2.7.7.14; reaction "phosphoethanolamine
  + CTP + H(+) = CDP-ethanolamine + diphosphate"
  [file:human/PCYT2/PCYT2-uniprot.txt "Reaction=phosphoethanolamine + CTP + H(+) = CDP-ethanolamine +"].
- UniProt PATHWAY: "Phospholipid metabolism; phosphatidylethanolamine biosynthesis;
  phosphatidylethanolamine from ethanolamine: step 2/3"
  [file:human/PCYT2/PCYT2-uniprot.txt "phosphatidylethanolamine from ethanolamine: step 2/3"].
- Vaz et al. 2019: "CTP:phosphoethanolamine cytidylyltransferase (ET), encoded by the
  PCYT2 gene, is the ubiquitously expressed rate-limiting enzyme for PE synthesis via the
  CDP-ethanolamine pathway"
  [PMID:31637422 "is the ubiquitously expressed rate-limiting enzyme for PE synthesis via the CDP-ethanolamine pathway"].
- Vaz et al. 2019: "ET catalyses the conversion of CTP and phosphoethanolamine into the
  activated nucleotide intermediate CDP-ethanolamine and pyrophosphate"
  [PMID:31637422 "ET catalyses the conversion of CTP and phosphoethanolamine into the activated nucleotide intermediate CDP-ethanolamine and pyrophosphate"].
- Original cloning (Nakashima et al. 1997): "CTP-phosphoethanolamine cytidylyltransferase
  (ET) is the enzyme that catalyzes the formation of CDP-ethanolamine in the
  phosphatidylethanolamine biosynthetic pathway from ethanolamine"
  [PMID:9083101 "the enzyme that catalyzes the formation of CDP-ethanolamine in the"];
  cDNA rescued a yeast ect1 mutant, and the GST fusion "shown to have ET activity"
  [PMID:9083101 "shown to have ET activity"]. Abstract-only cache (full_text_available: false).

## Structure / localization

- 389 aa, single polypeptide with **two tandem cytidylyltransferase (CTP_transf_like)
  domains**: UniProt lists Pfam PF01467 (x2), CDD cd02174 (CCT) and cd02173 (ECT),
  and InterPro IPR044608 (Ect1/PCYT2). Vaz et al. describe patient-1 missense variants
  "both within the second cytidylyltransferase (CTP) catalytic domain"
  [PMID:31637422 "both within the second cytidylyltransferase (CTP) catalytic domain"].
- Mammalian ET/PCYT2 is a **soluble cytosolic** enzyme (unlike the membrane-associated
  choline counterpart PCYT1A). GOA IBA localizes it to cytoplasm (GO:0005737,
  GO_REF:0000033). Cytosol (GO:0005829) is the more precise anatomical location.
- NOTE: Reactome (R-HSA-1483190, TAS) models the reaction at the **ER membrane** with a
  "membrane-bound ... PCY2 dimer" [reactome/R-HSA-1483190.md]. This conflicts with the
  cytosolic characterization; the ER-membrane C annotation (GO:0005789) is treated as an
  over-annotation of a soluble enzyme (kept, not removed, as TAS/Reactome).

## Disease

- Biallelic hypomorphic PCYT2 variants cause **autosomal-recessive complex hereditary
  spastic paraplegia (SPG82; MIM:618770)**: "global developmental delay with regression,
  spastic para- or tetraparesis, epilepsy and progressive cerebral and cerebellar atrophy"
  [PMID:31637422 "global developmental delay with regression, spastic para- or tetraparesis, epilepsy and\nprogressive cerebral and cerebellar atrophy"].
- Patient variants are hypomorphic with "reduced enzyme activity"
  [PMID:31637422 "reduced enzyme activity"]; complete loss is likely lethal in vertebrates
  (Pcyt2-null mice embryonically lethal).

## Annotation notes

- Three redundant MF annotations to GO:0004306 (IBA/GO_REF:0000033, IEA/GO_REF:0000120,
  IMP/PMID:31637422, TAS/PMID:9083101). All correct core MF; keep the experimental IMP
  and the two direct-literature ones as ACCEPT, phylogenetic IBA as ACCEPT.
- GO:0003824 (catalytic activity, IEA/InterPro) is a correct but uninformative parent of
  the specific MF -> MARK_AS_OVER_ANNOTATED.
- Four `protein binding` (GO:0005515) IPI annotations, all from large-scale interactome
  screens (BioPlex/HuRI-type: PMID:28514442, 32296183, 32814053, 33961781). Bare
  protein-binding, no specific partner-based function -> MARK_AS_OVER_ANNOTATED (per
  policy, never REMOVE a bare protein-binding IPI). Interactors (e.g. INPPL1, PSMA1,
  CASP6, LAMP2, REL) are not part of a coherent PE-synthesis complex.
- GO:0008654 (phospholipid biosynthetic process, TAS/PMID:9083101) is a correct but
  general parent of GO:0006646 -> KEEP_AS_NON_CORE.

## Core MF/BP/CC term ids (verified via OLS)

- MF: GO:0004306 ethanolamine-phosphate cytidylyltransferase activity
- BP: GO:0006646 phosphatidylethanolamine biosynthetic process
- CC: GO:0005829 cytosol (and IBA parent GO:0005737 cytoplasm)
