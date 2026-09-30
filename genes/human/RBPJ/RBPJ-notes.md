# RBPJ (human, Q06330) review notes

## Identity
- CSL / CBF1 / Su(H) ortholog. PANTHER PTHR10665 (RECOMBINING BINDING PROTEIN SUPPRESSOR OF HAIRLESS).
- IBA nodes: DNA-binding TF activity, cis-regulatory DNA binding, nucleus PTN000071433; Notch signaling pathway and MAML1-RBP-Jkappa-ICN1 complex PTN002580211.

## Key findings
- Repressor by default: binds CIR [PMID:9874765], SMRT/NCOR2 [PMID:10713164], SHARP/SPEN -> CtIP/CtBP [PMID:16287852], L3MBTL3-KDM1A [PMID:29030483 "In the absence of NOTCH ICD, RBPJ recruits L3MBTL3 and the histone demethylase KDM1A..."].
- Activator with NICD and MAML: crystal structure of CSL-ANK-MAML1 on DNA [PMID:16530044]; cooperative dimers on paired sites [PMID:17284587].
- RITA1 exports RBPJ from nucleus [PMID:21102556].
- Pharmacological disruption of the complex (SAHM1 [PMID:19907488], CB-103 [PMID:32601208]).
- COX4I2 oxygen responsive element activation [PMID:23303788].
- EBV EBNA2/EBNA3 target RBPJ [PMID:8627785].

## Decisions
- Core: GO:0000981 DNA-binding TF activity RNAPII-specific; GO:0000978; complexes GO:1990433/GO:0002193; processes GO:0000122, GO:0007221, GO:0007219.
- protein binding: NICD/MAML1/SNW1 -> transcription coactivator binding (GO:0001223); corepressors -> transcription corepressor binding (GO:0001222); viral, p53, KCTD1, RITA1, AP-MS hits -> REMOVE.
- GO:0061629 with SPEN -> MODIFY to corepressor binding.
- Mouse cardiac/vascular development terms non-core; BMP/ERBB/ephrin positive regulation and "regulation of generation of precursor metabolites" over-annotated.

## Variant-relevant biology
- CSL is the single DNA-binding effector; "default repression" mode; repressor partners differ by lineage (SPEN/SHARP in mammals vs Hairless in Drosophila).
