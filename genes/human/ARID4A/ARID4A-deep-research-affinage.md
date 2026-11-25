---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARID4A
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P29374
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARID4A (human)

## Current model (mechanistic narrative)

ARID4A (RBBP1) is a multidomain chromatin-associated protein that suppresses aberrant histone trimethylation and acts as a transcriptional coregulator within epigenetic and nuclear-receptor pathways [PMID:17043311, PMID:18728284]. In complex with its paralog ARID4B, it binds the Snrpn promoter to maintain genomic imprinting at the Prader-Willi/Angelman domain, controlling H3K9me3, H4K20me3, and DNA methylation at the imprinting center [PMID:17043311]. Loss of ARID4A elevates trimethylation of H3K4, H3K9, and H4K20 and deregulates hematopoietic gene expression, driving a myelodysplastic/myeloproliferative disorder that progresses to AML in mice [PMID:18728284], while combined ARID4A/ARID4B deficiency in Sertoli cells causes spermatogenic arrest by phenocopying loss of the androgen receptor and retinoblastoma protein pathways for which ARID4A serves as a transcriptional coactivator [PMID:23487765]. Structurally, ARID4A engages chromatin through a PWWP-ARID supramodule whose ARID domain binds dsDNA without sequence preference, while an intramolecular acidic loop L12 acts as a DNA mimic that autoinhibits DNA binding and modulates histone-mark engagement by the chromobarrel domain [PMID:34506790, PMID:35365808]; a disease-associated p.His411Asp variant loosens this module, weakens dsDNA binding, and promotes proliferation [PMID:35365808]. Beyond chromatin, ARID4A functions as an RNA-binding protein whose ARID domain recognizes a conserved 3'UTR structural element to stabilize metastasis-suppressor mRNAs including MTSS1, TIMP2, Rb1, and PTEN, thereby restraining breast cancer cell migration and invasion [PMID:40066676].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0003723 RNA binding, GO:0042393 histone binding, GO:0140110 transcription regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-74160 Gene expression (Transcription), R-HSA-8953854 Metabolism of RNA, R-HSA-1643685 Disease
- **partners:** ARID4B, RB1, AR, HERC2
- **complexes:** ARID4A-ARID4B chromatin complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | RBBP1/ARID4A interacts physically with RBBP1L1/ARID4B and with the Snrpn promoter, placing both proteins in a protein complex that regulates genomic imprinting at the PWS/AS domain. Combined homozygous deficiency of Rbbp1/Arid4a and heterozygous deficiency of Rbbp1l1/Arid4b reduced trimethylation of histone H4K20 and H3K9 and reduced DNA methylation at the PWS-IC, shifting the maternal allele toward a paternal epigenotype. Mutations of Rbbp1/Arid4a, Rbbp1l1/Arid4b, or Rb suppressed an Angelman syndrome imprinting defect caused by an AS-IC mutation (genetic epistasis). | PMID:17043311 | Genes & development |
| 2008 | High | Arid4a-deficient mice display increased trimethylation of H3K4, H3K9, and H4K20 in bone marrow, and decreased expression of Hox genes (Hoxb3, Hoxb5, Hoxb6, Hoxb8) and FoxP3, establishing ARID4A as a chromatin remodeling protein that suppresses histone trimethylation and maintains normal hematopoietic gene expression. Loss of Arid4a leads to myelodysplastic/myeloproliferative disorder progressing to AML. | PMID:18728284 | Journal of the National Cancer Institute |
| 2013 | High | ARID4A and ARID4B physically interact with each other. In Sertoli cells, combined deficiency (Arid4a−/−Arid4b+/−) causes spermatogenic arrest and impaired blood-testis barrier, phenocopying Sertoli cell-specific AR and RB knockouts. Molecular analysis identified AR- and RB-responsive genes as downstream targets, indicating ARID4A functions as a transcriptional coactivator for both the androgen receptor (AR) and retinoblastoma protein (RB) pathways. | PMID:23487765 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | Medium | RBBP1 (ARID4A) is transcriptionally regulated by estrogen receptors ERα and ERβ in an isoform-specific manner: ERα drives sustained induction via an Sp1 site in intron 1, while ERβ induction is transient and requires both the Sp1 and estrogen response elements. ChIP showed ERα binding to the intron 1 enhancer is constitutive whereas ERβ binding is transient. RBBP1 induction by both ER isoforms is SRC2-dependent. Deletion of ERα AF1 converted its induction profile to resemble ERβ. | PMID:16873370 | The Journal of biological chemistry |
| 2021 | High | The solution structure of the tandem PWWP-ARID domain of RBBP1 (ARID4A) was determined by NMR. The ARID domain interacts with DNA without GC- or AT-rich sequence preference. A long flexible acidic loop L12 within the ARID domain acts as a DNA mimic, binding to the ARID DNA-binding region and inhibiting DNA binding; L12 also binds weakly to the Tudor and chromobarrel domains and more strongly to the histone H2A-H2B heterodimer. Both L12 and DNA enhance chromobarrel binding to H3K4me3 and H4K20me3. | PMID:34506790 | Journal of molecular biology |
| 2022 | High | The crystal structure of the PWWP-ARID tandem supramodule of ARID4A was determined at 2.05 Å, revealing that PWWP and ARID form a structural and functional supramodule. A disease-associated missense variant p.His411Asp (in the ARID domain) causes a less compact conformation and reduces dsDNA-binding ability. The mutation also decreases G0/G1 arrest and promotes cell proliferation in HEK293T cells. | PMID:35365808 | Molecular psychiatry |
| 2018 | Medium | The crystal structure of the chromo barrel domain of RBBP1 (ARID4A) was determined. ITC assays showed that DNA does not significantly enhance histone H4K20me3 binding by the isolated chromo barrel domain, and surface charge analysis indicated the chromo barrel lacks a typical DNA-binding surface, suggesting this domain alone does not bind DNA. (Negative result: DNA-enhanced H4K20me3 binding requires additional domains beyond the isolated chromo barrel.) | PMID:29408527 | Biochemical and biophysical research communications |
| 2025 | Medium | ARID4A functions as an RNA-binding protein (RBP) that stabilizes mRNAs of metastasis-suppressing genes (MTSS1, TIMP2, Rb1, PTEN) by binding a conserved structural RNA element in their 3'UTRs. The ARID domain of ARID4A is required for mRNA stabilization and metastasis inhibition. Loss of ARID4A promotes breast tumor cell migration and invasion in vitro and in vivo. | PMID:40066676 | Cancer medicine |
| 2018 | Medium | Both ARID4A and ARID4B are direct targets of miR-30d; miR-30d negatively regulates their mRNA levels. Knockout of ARID4A and/or ARID4B promotes prostate cancer cell proliferation, migration, and invasion in vitro. | PMID:29797600 | Journal of cellular biochemistry |
| 2025 | Low | HERC2 binds to ARID4A via a conserved 'DxDKDxD' motif in ARID4A that is recognized by the RLD2 domain of HERC2, placing ARID4A as a binding partner in the HERC2 interaction network relevant to brain development. | PMID:bio_10.1101_2025.09.16.670041 | bioRxiv |

## Citations

- PMID:16873370
- PMID:17043311
- PMID:18728284
- PMID:23487765
- PMID:29408527
- PMID:29797600
- PMID:34506790
- PMID:35365808
- PMID:40066676
- PMID:bio_10.1101_2025.09.16.670041
