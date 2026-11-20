---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SUCLG2
affinage_run_date: 2026-06-10T10:51:54
uniprot_accession: Q96I99
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for SUCLG2 (human)

## Current model (mechanistic narrative)

SUCLG2 is the GTP-forming beta subunit of mitochondrial succinyl-CoA ligase, whose proper localization and stability depend on heterodimerization with the alpha subunit SUCLG1; loss of SUCLG1 mislocalizes SUCLG2 and reduces its protein level, fragmenting mitochondria and impairing substrate-level phosphorylation [PMID:30470562]. SUCLG2 resides in the mitochondrial network and, in human cerebral cortex, is selectively expressed in microvascular cells rather than neuronal or glial populations [PMID:25370487]. Functionally, SUCLG2 is required for mitochondrial DNA maintenance, an activity linked to its support of mitochondrial nucleoside diphosphate kinase (NDPK) and cytochrome c oxidase activity [PMID:21295139]. Beyond its core metabolic role, SUCLG2 governs the global succinylation state of mitochondrial proteins, and its loss raises succinylation of metabolic enzymes to dampen mitochondrial function; SUCLG2 is itself succinylated at Lys93, which stabilizes it, while SIRT5 desuccinylates Lys93 to license TRIM21-mediated K63-ubiquitination and lysosomal degradation [PMID:37904651]. Germline variants in the GTP-binding domain abolish SUCLG2 protein, destabilize the SDHB subunit, prevent assembly of complex II (succinate dehydrogenase), and cause succinate accumulation in pheochromocytoma/paraganglioma [PMID:34415331]. In cancer, SUCLG2 acquires non-canonical roles: upon EGF stimulation it translocates to the nucleus, complexes with phosphorylated EGFR, co-occupies the VEGFA promoter to drive VEGFA transcription and neuroendocrine differentiation, and confers EGFR-TKI (erlotinib) resistance [PMID:42252434], with EGFR–LIFR signaling upstream upregulating its expression to promote neuroendocrine differentiation and glycolysis [PMID:32963351]. SUCLG2 also restrains succinylation-dependent NF-κB signaling in tolerogenic dendritic cells by suppressing Lactb succinylation at Lys288 [PMID:37216870].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0140110 transcription regulator activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005739 mitochondrion, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-1643685 Disease, R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction
- **partners:** SUCLG1, SIRT5, TRIM21, EGFR, LMNA, DLAT
- **complexes:** succinyl-CoA ligase (SUCLG1-SUCLG2 heterodimer), mitochondrial complex II / succinate dehydrogenase (assembly dependency)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2023 | High | SUCLG2 controls overall succinylation levels of mitochondrial proteins in lung adenocarcinoma cells; its deletion upregulates succinylation of mitochondrial proteins, reducing enzymatic activity or protein stability of key metabolic enzymes and dampening mitochondrial function. SUCLG2 itself is succinylated on Lys93, which enhances its protein stability. SIRT5 desuccinylates SUCLG2 on Lys93, and TRIM21 then ubiquitinates SUCLG2 via K63-linkage leading to lysosomal degradation. | PMID:37904651 | Advanced science |
| 2011 | High | SUCLG2 knockdown in human fibroblasts (patient and control) caused significant decrease in mitochondrial DNA (mtDNA) content, decreased mitochondrial nucleoside diphosphate kinase (NDPK) and cytochrome c oxidase activities, and marked growth impairment, establishing SUCLG2 as crucial for mtDNA maintenance. The association with mitochondrial NDPK activity suggests SUCLG2 supports mtDNA maintenance via NDPK. | PMID:21295139 | Biochimica et biophysica acta |
| 2020 | Medium | EGFR-LIFR signaling upregulates SUCLG2 expression in prostate cancer cells; nuclear EGFR acts as a transcriptional regulator by directly binding the LIFR promoter. SUCLG2 upregulation increases succinate synthesis and enzymatic activities of mitochondrial NDPK, and promotes neuroendocrine differentiation and glycolysis in prostate cancer. Knockdown of SUCLG2 suppressed neuroendocrine differentiation in vitro and reduced xenograft tumor growth. | PMID:32963351 | Oncogene |
| 2022 | High | Germline variants in the GTP-binding domain of SUCLG2 cause absence of SUCLG2 protein, decrease in SDHB subunit levels, faulty assembly of mitochondrial complex II (succinate dehydrogenase), aberrant mitochondrial respiration, and elevated succinate accumulation in pheochromocytoma/paraganglioma tumors and SUCLG2-deficient hPheo1 cells. | PMID:34415331 | Journal of the National Cancer Institute |
| 2018 | Medium | Mutations in SUCLG1 (the alpha subunit) lead to strongly reduced SUCLG1 protein, which causes mislocalization of SUCLG2 protein (partial co-localization with mitochondrial network by confocal imaging), morphological fragmentation of mitochondria, impaired mitochondrial substrate-level phosphorylation (mSLP), and reduction of SUCLA2 and SUCLG2 protein levels. This establishes that SUCLG2 localization and stability depend on its heterodimeric partner SUCLG1. | PMID:30470562 | Molecular genetics and metabolism |
| 2014 | Medium | In human cerebral cortex, SUCLG2 protein is localized to cells forming the microvasculature (not neurons, astroglia, microglia, or oligodendroglia), as determined by double immunofluorescence. Co-localization with mitotracker in fibroblasts confirmed SUCLG2 resides in the mitochondrial network. This establishes cell-type-specific mitochondrial localization of SUCLG2 in the brain. | PMID:25370487 | Journal of bioenergetics and biomembranes |
| 2023 | Medium | Suclg2 maintains the tolerogenic phenotype of regulatory dendritic cells (diffDCs) by suppressing succinylation of Lactb at lysine 288. In diffDCs, Suclg2 prevents NF-κB signaling activation; Suclg2 knockdown enhanced NF-κB signaling and expression of inflammatory genes (CD40, Ccl5, Il12b) and impaired T cell apoptosis induction. Lactb succinylation at K288 was identified as a positive regulator of NF-κB signaling that Suclg2 suppresses. | PMID:37216870 | Journal of autoimmunity |
| 2026 | High | EGF stimulation induces SUCLG2 nuclear translocation in prostate cancer cells, where SUCLG2 forms a complex with phosphorylated EGFR and co-occupies the VEGFA promoter to co-activate VEGFA transcription, driving neuroendocrine gene programs. SUCLG2 overexpression conferred erlotinib (EGFR-TKI) resistance in vitro, and SUCLG2 depletion restored TKI sensitivity; VEGFA reconstitution rescued the effect of SUCLG2 depletion. | PMID:42252434 | Cell communication and signaling |
| 2025 | Medium | SUCLG2 interacts with LMNA in glioblastoma cells, leading to acetylation of LMNA at K470, which affects oxidative phosphorylation levels and mitochondrial damage. SUCLG2 also interacts with DLAT, reducing binding of H4K16la (lactylation mark) to promoter regions, thereby suppressing expression of BEST1, GRAMD4, and MBD6 and affecting GBM cell proliferation and apoptosis. | PMID:41249152 | Cell death discovery |

## Citations

- PMID:21295139
- PMID:25370487
- PMID:30470562
- PMID:32963351
- PMID:34415331
- PMID:37216870
- PMID:37904651
- PMID:41249152
- PMID:42252434
