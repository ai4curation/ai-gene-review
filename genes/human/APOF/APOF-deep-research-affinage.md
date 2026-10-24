---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APOF
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q13790
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 16
citation_count: 16
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APOF (human)

## Current model (mechanistic narrative)

ApoF (apolipoprotein F) is a liver-secreted regulator of lipoprotein and lipid metabolism that operates primarily as a selective inhibitor of cholesteryl ester transfer protein (CETP) [PMID:9880564]. Purified from LDL and recapitulated with recombinant protein, ApoF is identical to lipid transfer inhibitor protein and preferentially suppresses CETP-mediated cholesteryl ester transfer when LDL is the acceptor while sparing HDL-donor transfers [PMID:9880564]. This selectivity is governed by LDL particle size: larger LDL particles bind more ApoF, and reducing LDL size sharply lowers ApoF binding [PMID:35016907]. In vivo, ApoF knockdown raises CETP-mediated CE transfer from HDL to LDL, increases LDL cholesterol, lowers HDL, and impairs reverse cholesterol transport, confirming its CETP-inhibitory role at the organismal level [PMID:31511396]. ApoF function extends beyond CETP inhibition: gain- and loss-of-function studies show it promotes hepatic VLDL-triglyceride secretion and lipoprotein remnant clearance in concert with increased Ldlr and Lrp1 expression [PMID:35735979], and overexpression accelerates HDL cholesteryl ether clearance and enhances macrophage cholesterol efflux [PMID:19008531]. ApoF deletion is largely dispensable for basal HDL metabolism but produces sex-specific hepatic cholesteryl ester accumulation and reduced lesion area in atherogenic backgrounds [PMID:22363685, PMID:24529150], alongside liver steatosis and dysregulated lipid-metabolic gene programs [PMID:38540406]. ApoF additionally functions downstream of a B7-H4/Stat5 axis to support pancreatic β-cell cholesterol efflux and insulin secretion [PMID:39571901]. Its high liver-specific expression is driven by synergistic ETS-1/C/EBPα transcriptional activation [PMID:25726912] and by FXR [PMID:24211198], and is repressed by agonist-activated LXRα/PPARα/RXR complexes and by retinoic-acid-induced SHP [PMID:31812787, PMID:25014134]. ApoF is proteolytically processed by the proprotein convertase PC7 [PMID:25349778].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008289 lipid binding, GO:0140313 molecular sequestering activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-74160 Gene expression (Transcription)
- **partners:** CETP, PCSK7
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | Apolipoprotein F (ApoF) is identical to lipid transfer inhibitor protein (LTIP): ApoF purified from LDL inhibits cholesteryl ester transfer protein (CETP) activity, preferentially suppressing CETP-mediated transfer events involving LDL as acceptor while having lesser effect on transfers involving HDL as donor. Recombinant ApoF secreted from transfected COS-7 cells reproduced this CETP inhibitor activity with the same LDL specificity, oleate sensitivity, and lipoprotein concentration dependence as native LTIP. | PMID:9880564 | The Journal of biological chemistry |
| 2008 | High | Overexpression of murine or human ApoF in mice significantly reduces total cholesterol (~28%), HDL cholesterol (~27%), and phospholipid levels (~19%) by accelerating plasma clearance of HDL cholesteryl ether. Human ApoF in mice localizes predominantly to HDL3 (>90%), and ApoF overexpression improves macrophage cholesterol efflux on a per HDL-C basis. | PMID:19008531 | Arteriosclerosis, thrombosis, and vascular biology |
| 2012 | High | Deletion of ApoF in mice does not substantially alter plasma lipid concentrations, HDL size, or lipid/protein composition, indicating ApoF is dispensable for basal HDL metabolism in mice. However, sex-specific effects were observed: female ApoF KO mice had increased hepatic cholesteryl ester content, and ApoB-depleted serum from male KO mice was less effective at promoting ABCA1-mediated cholesterol efflux from macrophages. | PMID:22363685 | PloS one |
| 2014 | Medium | ApoF/Ldlr double-knockout mice fed a Western diet show 39% reduction in atherosclerotic lesion area compared to Ldlr KO controls despite no significant differences in plasma lipid parameters. ApoF KO mice also exhibit reduced expression of interferon-alpha (IFNα) responsive genes (Ifi27l2a, Oas2, Oas3) and impaired macrophage activation, attributable to hypomorphic expression of Stat2 located 425 bp downstream of ApoF. | PMID:24529150 | Atherosclerosis |
| 2015 | High | The ApoF promoter is activated by the transcription factors ETS-1/ETS-2 and C/EBPα binding to specific sites in the -198 to -2 nt region. Mutation of EBS-2, EBS-4, and the C/EBP binding site abolished promoter activity. ETS-1 and C/EBPα physically interact and act synergistically to drive ApoF transcription, contributing to its high liver-specific expression. | PMID:25726912 | Biochimie |
| 2013 | Medium | Farnesoid X receptor (FXR) upregulates ApoF expression in liver cells and in C57BL/6 mice: FXR agonists CDCA and GW4064 increase ApoF mRNA, and this regulation depends on FXR binding to an FXR response element (ER1 at -2904 to -2892 bp) in the ApoF gene promoter. | PMID:24211198 | Biochemical and biophysical research communications |
| 2019 | High | APOF mRNA levels are negatively regulated by agonist-activated LXRα and PPARα nuclear receptors. This suppression requires co-incubation with the RXR agonist retinoic acid. ChIP analysis confirmed agonist-dependent binding of LXRα, PPARα, and RXRα to a hormone response element complex (HREc) located approximately -1900 to -2007 bp upstream of the APOF promoter. Mutation of HREc binding sites abolished reporter inhibition. | PMID:31812787 | Biochimica et biophysica acta. Molecular and cell biology of lipids |
| 2019 | High | ApoF knockdown in fat-fed hamsters (siRNA-based model) increases CETP-mediated cholesteryl ester (CE) transfer from HDL to LDL up to 2-fold, raises LDL cholesterol by 40%, reduces HDL by 25%, alters LDL and HDL lipid compositions, decreases hepatic LDLR gene expression, and impairs HDL reverse cholesterol transport. These in vivo data validate in vitro findings that ApoF selectively inhibits CETP activity on LDL. | PMID:31511396 | Journal of lipid research |
| 2022 | High | ApoF overexpression in mice (adenoviral hApoF) increases hepatic VLDL-TG secretion and hepatic lipoprotein remnant clearance (associated with increased Ldlr and Lrp1 expression), resulting in ~25% reduction in plasma TG levels. Conversely, reducing ApoF expression in vivo reduces VLDL secretion and reduces hepatocyte VLDL uptake ~15% in vitro, revealing a role for ApoF in controlling plasma and hepatic TG-rich lipoprotein metabolism beyond CETP inhibition. | PMID:35735979 | Hepatology (Baltimore, Md.) |
| 2022 | High | ApoF binding to LDL is determined by LDL particle size: larger LDL particles bind more ApoF, and this positive correlation was confirmed both in hyperlipidemic plasmas and by in vitro modification of LDL size using CETP ± LCAT. Reduction of enlarged LDL size by LPL treatment reduced ApoF binding by 90%. Plasma ApoF is increased 31% in hypercholesterolemia but decreased 20% in hypertriglyceridemia; combined hyperlipidemia ameliorates the hypercholesterolemia-induced rise. | PMID:35016907 | Journal of lipid research |
| 2014 | Medium | Retinoic acid (RA) suppresses ApoF gene expression in hepatocytes through a mechanism requiring the small heterodimer partner (SHP): RA-induced upregulation of SHP represses ApoF mRNA levels in the hepatic cell line AML-12 in vitro and in SHP null mice in vivo (where this repression is lost), demonstrating SHP-dependent regulation of ApoF transcription. | PMID:25014134 | Gene |
| 2024 | High | B7-H4 deficiency in pancreatic β-cells activates Stat5 signaling, which inhibits Apof expression, leading to reduced cholesterol efflux, accumulated cholesterol in β-cells, and impaired insulin processing and secretion. Overexpression of Apof in β-cells or inhibition of Stat5 reverses this metabolic phenotype, placing ApoF downstream of a B7-H4/Stat5 axis controlling β-cell cholesterol homeostasis. | PMID:39571901 | Molecular metabolism |
| 2017 | Low | ApoF protein concentration in human serum/plasma decreases across stages of non-alcoholic fatty liver disease (NAFLD), as quantified by LC-MS using a universal calibration curve (IGNIS kit). The measured ApoF level in plasma from a healthy volunteer was 445.2 ng/mL. | PMID:28935895 | Scientific reports |
| 2014 | Medium | Proprotein convertase PC7 processes apolipoprotein F in vitro; however, wild-type and R504H-mutant PC7 exhibit similar processing of ApoF, and PC7 KO mice show no change in plasma lipid profiles, indicating that the R504H mutation does not modify PC7's proteolytic activity toward ApoF. | PMID:25349778 | FEBS open bio |
| 2024 | Medium | In ApoF knockout mice, liver histopathology shows vacuolization and steatosis, and serum biochemical assays reveal abnormal lipid content. Transcriptome-wide m6A methylome analysis (MeRIP-seq) in ApoF KO mice shows differentially m6A-methylated mRNAs enriched in cholesterol, triglyceride, and long-chain fatty acid metabolic processes, as well as lipid transport and liver development, demonstrating ApoF's role in maintaining liver health and lipid metabolism. | PMID:38540406 | Genes |
| 2009 | Low | In the lacrimal glands of male NOD mice (a Sjögren's syndrome model), ApoF and ApoE are upregulated and proposed to coordinate lipid efflux from acinar cells, but missorting of ApoF may contribute to cholesteryl ester deposition. Immunofluorescence revealed abnormal subcellular distribution of ApoF protein in NOD mouse lacrimal gland acinar cells compared to controls. | PMID:19345210 | Experimental eye research |

## Citations

- PMID:19008531
- PMID:19345210
- PMID:22363685
- PMID:24211198
- PMID:24529150
- PMID:25014134
- PMID:25349778
- PMID:25726912
- PMID:28935895
- PMID:31511396
- PMID:31812787
- PMID:35016907
- PMID:35735979
- PMID:38540406
- PMID:39571901
- PMID:9880564
