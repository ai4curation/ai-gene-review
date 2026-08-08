---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AFF3
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P51826
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AFF3 (human)

## Current model (mechanistic narrative)

AFF3 (LAF4) is a nuclear transcriptional activator that controls allele-specific gene expression and developmental gene programs as the central component of the Super Elongation Complex-like 3 (SEC-L3) [PMID:8555498, PMID:28180295]. It binds double-stranded DNA and carries a domain that strongly activates transcription, localizing to nuclear speckles where it redistributes the elongation factors CDK9 and cyclin T1, linking it to transcription elongation and RNA splicing [PMID:8555498, PMID:26214578]. AFF3 is recruited to defined genomic loci by sequence-specific zinc finger proteins: ZFP281 brings AFF3 to enhancers including the Meg3 enhancer of the imprinted Dlk1-Dio3 locus, whereas ZFP57 directs it to the IG-DMR, and AFF3 binds the methylated DMR downstream of XIST to maintain mono-allelic XIST expression [PMID:28180295, PMID:30535390]. Through its C-terminal domain, AFF3 binds immunoglobulin switch regions and promotes recruitment of AID to drive isotype-specific class switch recombination [PMID:36001653]. In the developing cerebral cortex AFF3 is required for neuronal migration, acting in part through its transcriptional target Mdga2 [PMID:25162227]. AFF3 protein level is controlled by a nine-amino-acid degron recognized for ubiquitin-mediated degradation; de novo degron variants stabilize AFF3 and cause KINSSHIP syndrome via a dominant-negative/gain-of-function mechanism, while promoter CGG/GCC repeat expansions trigger methylation-induced silencing and functional haploinsufficiency associated with neurodevelopmental disorders [PMID:24763282, PMID:33961779, PMID:39313615]. AFF3 is also recurrently disrupted by leukemic fusions to MLL/KMT2A and to RUNX1/AML1 [PMID:12203795, PMID:12743608, PMID:17968322].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-168256 Immune System, R-HSA-1266738 Developmental Biology
- **partners:** ZFP281, ZFP57, CDK9, CCNT1
- **complexes:** Super Elongation Complex-like 3 (SEC-L3)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1996 | Medium | AFF3 (LAF4) encodes a nuclear protein that binds double-stranded DNA cellulose in vitro and contains a domain that strongly activates transcription when fused to the GAL4 DNA-binding domain, establishing it as a transcriptional activator. | PMID:8555498 | Blood |
| 1996 | Medium | AFF3 (LAF4) localizes to the nucleus with an uneven, granular immunofluorescence pattern in lymphoid cells. | PMID:8555498 | Blood |
| 2002 | Medium | LAF4/AFF3 is fused to MLL (KMT2A) as a result of t(2;11)(q11;q23) translocation in infant pro-B ALL, with the fusion breakpoint located within the region homologous to the AF4 transactivation domain, implicating AFF3 transactivation function in leukemogenesis. | PMID:12203795, PMID:12743608 | Genes, chromosomes & cancer |
| 2007 | Medium | AFF3 (LAF4) is fused to AML1 (RUNX1) as a result of t(2;21)(q11;q22) in pediatric T-ALL, making LAF4 the first gene fused to both MLL and AML1 in acute leukemia; the fusion joins exon 7 of AML1 to exon 8 of LAF4 in-frame. | PMID:17968322 | Oncogene |
| 2014 | High | FRA2A cytogenetic fragile site at 2q11 is caused by CGG repeat expansion in a conserved, brain-active alternative promoter of AFF3; expanded repeats are associated with CpG hypermethylation of the AFF3 promoter, monoallelic AFF3 expression (functional haploinsufficiency) in carriers, and neurodevelopmental phenotypes. | PMID:24763282 | PLoS genetics |
| 2017 | High | AFF3, as the central component of the Super Elongation Complex-like 3 (SEC-L3), associates with the zinc finger protein ZFP281; ZFP281 recruits AFF3 to the Meg3 enhancer within the imprinted Dlk1-Dio3 locus to regulate allele-specific expression of the Meg3 polycistron. Genome-wide analyses confirm ZFP281 generally co-localizes with AFF3 at enhancers, while localization of AFF3 to the IG-DMR at the same locus requires the distinct zinc finger protein ZFP57. | PMID:28180295 | Nucleic acids research |
| 2015 | Medium | AFF3 is a transcriptional target of the Wnt/β-catenin signaling pathway; a Wnt response element at position -1408 of the AFF3 TSS mediates its regulation. AFF3 localizes to nuclear speckles, and its overexpression alters nuclear speckle organization and redistributes CDK9 and cyclin T1 to AFF3/speckle sites, implicating AFF3 in both transcription elongation and RNA splicing. | PMID:26214578 | Oncogenesis |
| 2019 | Medium | AFF3 binds to the differentially methylated region (DMR) downstream of the XIST promoter in a DNA-methylation-dependent manner, and AFF3 knockdown causes de-repression of the inactive XIST allele in terminally differentiated cells, establishing a role for AFF3 in maintaining mono-allelic XIST expression. This mechanism is distinct from the KAP1-H3K9 methylation pathway that controls imprinted loci. | PMID:30535390 | Journal of molecular cell biology |
| 2018 | Medium | AFF3 overexpression activates the estrogen receptor (ER) signaling pathway and transcriptionally upregulates a subset of ER-regulated genes, conferring tamoxifen resistance and enabling estrogen-independent growth in breast cancer cells. | PMID:30326937 | Journal of experimental & clinical cancer research |
| 2022 | High | AFF3 directly facilitates immunoglobulin class switch recombination (CSR) with isotype preference: AFF3-deficient mice show reduced IgG2c, IgG1, and IgG3 but not IgM. Mechanistically, the AFF3 protein binds to IgM and IgG1 switch regions via its C-terminal domain, and Aff3 deficiency reduces recruitment of AID (activation-induced cytidine deaminase) to the switch regions. | PMID:36001653 | Science advances |
| 2021 | High | De novo missense variants or deletions in the degron of AFF3 (a nine-amino-acid sequence recognized by E3 ubiquitin ligase for protein degradation) cause KINSSHIP syndrome. Mouse knockin models and zebrafish overexpression experiments indicate a dominant-negative/gain-of-function mechanism whereby increased AFF3 level is pathological, consistent with the degron disrupting ubiquitin-mediated degradation of AFF3. | PMID:33961779 | American journal of human genetics |
| 2014 | Medium | Laf4/Aff3 is required for normal cellular migration in the developing mouse cerebral cortex; loss of Laf4 in organotypic slices impairs cortical cell migration. Mdga2 was identified as a transcriptional target of Laf4, and Mdga2 overexpression partially rescues the migration deficit caused by Laf4 loss. | PMID:25162227 | PloS one |
| 2024 | Medium | AFF3 LoF and degron (KINSSHIP) variants modulate transcriptomes through variant-specific mechanisms: both affect the same pathways but only ~one-third of differentially expressed genes overlap between homozygous LoF/LoF and KINSSHIP/KINSSHIP lines; the DNA repair pathway shows opposite modulation in the two genotypes. More than one-third of AFF3-bound loci change expression in either homozygous context. | PMID:38811945 | Genome medicine |
| 2024 | Medium | A GCC repeat expansion in the promoter of AFF3 is associated with DNA methylation-induced gene silencing and with a ~2.4-fold reduced probability of completing secondary education; AFF3 expansions are significantly enriched in neurodevelopmental disorder cohorts compared to controls, establishing promoter GCC expansion as a major mechanism of AFF3 loss-of-function in the population. | PMID:39313615 | Nature genetics |
| 2024 | Low | AFF3 regulates ACSL4 protein expression, thereby modulating fatty acid metabolism and ferroptosis sensitivity in castration-resistant prostate cancer cells; AFF3 overexpression increases sensitivity to the ferroptosis inducer RSL3, while AFF3 knockdown decreases it. | PMID:38478171 | Apoptosis |

## Citations

- PMID:12203795
- PMID:12743608
- PMID:17968322
- PMID:24763282
- PMID:25162227
- PMID:26214578
- PMID:28180295
- PMID:30326937
- PMID:30535390
- PMID:33961779
- PMID:36001653
- PMID:38478171
- PMID:38811945
- PMID:39313615
- PMID:8555498
