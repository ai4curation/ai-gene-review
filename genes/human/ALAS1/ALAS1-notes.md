# ALAS1 (human, P13196) review notes

UniProtKB P13196 (HEM1_HUMAN). HGNC symbol ALAS1. EC 2.3.1.37. PANTHER PTHR13693:SF50.
Comparator: genes/human/ALAS2 (erythroid paralog).

## Deep research

No `-deep-research-*.md`; deep research unavailable in this session (no provider keys; template
missing). Built from UniProt, Reactome and cached literature.

## Biology

- Housekeeping isozyme. [PMID:32499479 "ALAS1 (gene location 3p21.2) is the housekeeping enzyme providing a basal level of heme in non-erythroid cell types for cytochromes and other hemoproteins."]
- First committed step of heme synthesis. [PMID:2347585 "delta-Aminolevulinate synthase (ALAS) catalyzes the first committed step of heme biosynthesis."]
- Rate-limiting in liver; induced by bile acids via FXR. [PMID:17975826 "Aminolevulinic acid synthase 1 (ALAS1) is the rate-limiting enzyme of heme synthesis in the liver and is highly regulated to adapt to the metabolic demand of the hepatocyte."]
- Matrix enzyme. [Reactome:R-HSA-1592238 "The ALAS1 precursor is imported into the mitochodrial matrix where it catalyzes the synthesis of 5-aminolevulinate from glycine and succinyl-CoA as part of heme biosynthesis."]
- Heme feedback: transcription, mRNA, import, and ClpXP/LONP1 degradation.
  [PMID:21659532 "Heme is known to affect ALAS-1 activity by repressing gene transcription, accelerating mRNA degradation, and impeding pre-ALAS-1 mitochondrial translocation."]
  [PMID:27496948 "We found that ALAS1 forms a complex with ClpXP in a heme-dependent manner"]
- SUCLA2 associates with ALAS2, not ALAS1. [PMID:10727444 "mitochodrially expressed SCS-betaA associates specifically with ALAS-E and not with ALAS-N"]

## Open issue

UniProt attributes Pro-576 hydroxylation/VHL binding and hypoxia-increased activity to ALAS1 via
PMID:16234850, whose abstract reports these for ALAS2 and says the LXXLAP motif is not in ALAS1.
Full text not available; raised as a suggested question rather than a source defect.

## Decisions

- 58 bare protein-binding IPI rows: REMOVE (policy). Identical protein binding (2): MODIFY ->
  protein homodimerization activity.
- hemoglobin biosynthetic process IBA (PTN000343740): MARK_AS_OVER_ANNOTATED (ALAS2-specific role
  propagated above the duplication; family review had this UNRESOLVED).
- porphyrin metabolic / tetrapyrrole biosynthetic process: MODIFY -> heme B biosynthetic process.
- transferase: MODIFY -> ALAS activity (as ALAS2).
- rat-derived response-to rows: MARK_AS_OVER_ANNOTATED except xenobiotic (KEEP_AS_NON_CORE);
  bile acid IDA KEEP_AS_NON_CORE; heme A KEEP_AS_NON_CORE; HPA nucleoplasm MARK_AS_OVER_ANNOTATED.
