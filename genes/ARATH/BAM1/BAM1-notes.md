# BAM1 (BARELY ANY MERISTEM 1, At5g65700; UniProt O49545) curation notes

## Identity
- The BAM1 symbol also matches beta-amylase 1 (Q9LIR6, At3g23920), so the gene was fetched by accession O49545 and the AGI locus At5g65700 was verified.

## Key findings
- BAM1 is a CLV1-clade LRR-RK. bam1 bam2 bam3 mutants lose stem cells, and BAM genes also act in leaf vasculature, male gametophyte and ovule development [PMID:16367950].
- BAM1/BAM2 act as receptors in parallel with CLV1. clv1 nulls are weak because of BAM activity, and bam mutants suppress clv3, possibly by sequestering ligand in the meristem flanks [PMID:18780746 "BAM1 and BAM2 act to sequester CLV3-like ligands in the meristem flanks"].
- BAM1 binds CLV3 directly (radioligand Kd 26 nM [PMID:20626648]; photoaffinity labelling [PMID:25754504 "Further analysis showed that the receptor kinase BAM1 directly binds the CLV3 peptide."]). clv1 bam1 has an enlarged SAM with expanded WUS [PMID:25754504].
- BAM ligand specificity is broader than that of CLV1/CLV2 [PMID:20626648].
- In clv1 mutants, BAM genes are expressed ectopically and buffer the meristem [PMID:28355208].
- BAM1 phosphorylates PBL34/35/36, and CLV3-induced MPK3/6 phosphorylation depends on CLV1/BAM1 [PMID:34935965].
- CLE25/26/45-BAM1/3-CIK controls protophloem differentiation [PMID:34651321].
- BAM1/BAM2 are needed for early anther cell layers [PMID:16751349].

## Decisions
- Core MF is GO:0004675 transmembrane receptor protein serine/threonine kinase activity, reached by MODIFYing the GOA IDA GO:0004674 row (PMID:34651321) to it, with support from PMID:25754504 and PMID:20626648 (direct CLV3 binding). The process GO:0007178 is also proposed as NEW.
- The CLE peptide IPI rows are MODIFIED to peptide hormone binding (GO:0017046, as in the CLV1 review). The RLCK IPI rows are MODIFIED to protein kinase binding.
- The CSI-LRR high-throughput ectodomain protein binding rows are REMOVED (bare protein binding, no functional information).
- The IBA hormone-mediated signaling row (a node seeded by BRI1/BRL) is kept as non-core.
- Deep research (falcon) attempted 2026-10-05 and failed with HTTP 402 Payment Required. No deep-research file exists for BAM1.


## PR #4384 review follow-up (2026-10-06)
- Dropped the NEW GO:0004675 row (redundant with its direct parent GO:0004674); instead the GO:0004674 IDA row is MODIFIED to GO:0004675. The IEA GO:0004674 (EC mapping) row and the InterPro IEA GO:0004672 row are also MODIFIED to GO:0004675 so that all kinase rows are consistent. The NEW GO:0007178 row is unchanged.
