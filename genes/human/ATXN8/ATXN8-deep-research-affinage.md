---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATXN8
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q156A1
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATXN8 (human)

## Current model (mechanistic narrative)

ATXN8 encodes a nearly pure polyglutamine protein transcribed from the antiparallel CAG strand of the SCA8 CTG·CAG repeat locus, and its expansion drives cerebellar and brainstem neurodegeneration through a toxic protein gain-of-function: expanded ATXN8 forms 1C2-positive intranuclear polyglutamine inclusions in Purkinje and brainstem neurons of both SCA8 transgenic mice and human autopsy tissue [PMID:16804541]. The same locus is transcribed bidirectionally, producing the noncoding CUG-expansion antisense transcript ATXN8OS, which accumulates as ribonuclear foci that sequester MBNL1 and dysregulate MBNL1/CELF-controlled splicing—upregulating the CNS target GAT4/Gabt4 and reducing GABAergic inhibition in the cerebellar granular cell layer; loss of Mbnl1 worsens motor deficits, placing ATXN8OS expansion upstream of the MBNL/CELF splicing pathway [PMID:19680539]. In cell models, ATXN8 polyglutamine protein contributes to caspase-dependent apoptotic death [PMID:19229559]. ATXN8 transcription is controlled at its proximal promoter by C/EBPα binding, which upregulates expression [PMID:22577844], and by a functional -62 G/A promoter polymorphism in which the -62G allele drives higher reporter activity [PMID:19229559]; expanded ATXN8OS RNA additionally shows increased stability and is associated with repressive H3-K9 dimethylation and reduced H3-K14 acetylation at the locus [PMID:19203395].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-5357801 Programmed Cell Death
- **partners:** MBNL1, CEBPA
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | ATXN8 is a previously unidentified gene expressed from the antiparallel (CAG) strand of the SCA8 CTG·CAG repeat expansion locus. It encodes a nearly pure polyglutamine expansion protein, and 1C2-positive intranuclear polyglutamine inclusions were detected in cerebellar Purkinje cells and brainstem neurons of SCA8 transgenic mice (CTG116 expansion) and human SCA8 autopsy tissue, demonstrating protein-level toxic gain-of-function. | PMID:16804541 | Nature genetics |
| 2009 | High | ATXN8 CAG-expansion transcripts (encoding polyglutamine) are expressed bidirectionally from the same SCA8 locus as the noncoding CUG-expansion ATXN8OS transcripts. CUG-expansion RNA accumulates as ribonuclear inclusions co-localizing with MBNL1 in selected neurons, and loss of Mbnl1 enhances motor deficits in SCA8 mice, placing ATXN8OS upstream of MBNL1/CELF regulated splicing. The CUG-expansion transcripts trigger splicing changes and upregulate the CUGBP1-MBNL1-regulated CNS target GAT4/Gabt4, leading to reduced GABAergic inhibition in the cerebellar granular cell layer. | PMID:19680539 | PLoS genetics |
| 2009 | Medium | In cell lines carrying large SCA8 alleles, ATXN8 expression is significantly higher than in control cells, and treatment with MG-132 or staurosporine increases cell death or caspase-3 activity, indicating that ATXN8 polyglutamine protein contributes to apoptotic cell death. A novel ATXN8 promoter SNP at position -62 (G/A) modulates transcriptional activity: the -62G allele drives significantly higher luciferase reporter activity than -62A in neuroblastoma and embryonic kidney cells. | PMID:19229559 | Human genetics |
| 2009 | Medium | Expanded CUG-repeat ATXN8OS transcripts (88 and 157 CR) form ribonuclear foci in stable cell lines. Larger repeat expansions (157 CR) cause increased H3-K9 dimethylation and reduced H3-K14 acetylation around the ATXN8OS gene locus (detected by ChIP-PCR), indicating epigenetic silencing. The expanded RNA also shows increased stability (slower decay after actinomycin D treatment) compared to shorter repeat alleles. | PMID:19203395 | BMC molecular biology |
| 2012 | Medium | CCAAT/enhancer-binding protein alpha (C/EBPα) binds to the ATXN8 proximal promoter and upregulates ATXN8 expression in neuroblastoma SK-N-SH cells, as demonstrated by ChIP-PCR and cDNA co-transfection with luciferase reporter assay. | PMID:22577844 | European journal of neurology |

## Citations

- PMID:16804541
- PMID:19203395
- PMID:19229559
- PMID:19680539
- PMID:22577844
