---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADTRP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q96IZ2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADTRP (human)

## Current model (mechanistic narrative)

ADTRP is an atypical multipass transmembrane hydrolase that uses conserved threonine and histidine residues to selectively hydrolyze bioactive fatty acid esters of hydroxy fatty acids (FAHFAs), and which functions in endothelial, adipose, and macrophage contexts to control vascular integrity, anticoagulation, and thermogenesis [PMID:27018888, PMID:32152231]. Active-site mutagenesis, cell-active covalent inhibitors, and Adtrp-knockout mice establish it as one of the principal endogenous FAHFA hydrolases in vivo, with loss of function elevating tissue FAHFA levels without altering other lipid classes [PMID:27018888, PMID:32152231]; this hydrolase role is tissue-dependent, as hepatic overexpression alone does not alter FAHFA pools or metabolic homeostasis [PMID:34288722]. In endothelial cells ADTRP regulates tissue factor pathway inhibitor (TFPI) expression and anticoagulant activity, co-localizing with TFPI and caveolin-1 in lipid rafts and driving TFPI transcription through the transcription factor POU1F1 [PMID:21868574, PMID:32445923]. ADTRP also supports vascular development and vessel integrity by negatively regulating canonical Wnt/β-catenin signaling downstream of LRP6 and upstream of GSK3β, with its deficiency causing vascular malformations and MMP-9 upregulation in zebrafish and mice [PMID:30571485], and it suppresses monocyte adhesion and transendothelial migration via a PIK3R3–AKT–MIA3/TANGO1 axis [PMID:28645652, PMID:28341552]. Its expression is directly induced by androgen through an androgen receptor half-ARE [PMID:28645652]. In brown/beige adipose tissue ADTRP promotes thermogenesis by binding S100b and facilitating its secretion to support β3-adrenergic signaling, with knockout mice showing cold intolerance rescuable by direct β3-AR stimulation [PMID:35804197].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-109582 Hemostasis, R-HSA-162582 Signal Transduction
- **partners:** S100B, TFPI, CAV1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | ADTRP is an atypical transmembrane hydrolytic enzyme that depends on conserved threonine and histidine residues for catalysis, and specifically hydrolyzes bioactive fatty acid esters of hydroxy fatty acids (FAHFAs) but not other major lipid classes. | PMID:27018888 | Nature chemical biology |
| 2020 | High | ADTRP (and AIG1) are the first endogenous FAHFA hydrolases identified in vivo; tissues from Adtrp-KO and double-KO mice showed elevated FAHFA levels (particularly 9-carbon ester isomers) with decreased FAHFA hydrolysis activity, while other lipid classes were unaltered. A dual AIG1/ADTRP inhibitor (ABD-110207) acutely elevated FAHFA levels in wild-type mice. | PMID:32152231 | The Journal of biological chemistry |
| 2011 | Medium | ADTRP regulates both native and androgen-enhanced TFPI expression and activity in endothelial cells; ADTRP knockdown reduces TFPI mRNA and activity, while ADTRP overexpression enhances them. ADTRP colocalizes with TFPI and caveolin-1 in lipid rafts/caveolae, and dihydrotestosterone upregulates TFPI and ADTRP expression with increased FXa inhibition by TFPI in an ADTRP- and caveolin-1-dependent manner. | PMID:21868574 | Blood |
| 2017 | Medium | Androgen directly activates ADTRP transcription via the androgen receptor binding to a half androgen response element (ARE, TGTTCT) located at +324 bp from the ADTRP transcription start site, as confirmed by chromatin immunoprecipitation. ADTRP mediates androgen's inhibitory effects on monocyte adhesion to endothelial cells and transendothelial migration through downstream genes PIK3R3 and MIA3. | PMID:28645652 | Biochimica et biophysica acta. Molecular basis of disease |
| 2017 | Medium | ADTRP positively regulates PIK3R3 (PI3K regulatory subunit 3) expression, which leads to activation of AKT and subsequent upregulation of MIA3/TANGO1, forming a gene-gene regulatory network. ADTRP knockdown promotes monocyte adhesion and transendothelial migration, inhibits EC proliferation and migration, and increases apoptosis; these effects are reversed by constitutively active AKT1 or MIA3/TANGO1 overexpression. | PMID:28341552 | Biochimica et biophysica acta. Molecular basis of disease |
| 2018 | Medium | ADTRP plays a critical role in vascular development and vessel integrity in vivo; genetic inhibition of Adtrp causes vascular malformations in zebrafish and newborn mice including dilation, tortuosity, perivascular inflammation, increased permeability, and microhemorrhages. ADTRP negatively regulates canonical Wnt signaling downstream of LRP6 and upstream of GSK3β, and ADTRP deficiency upregulates MMP-9 via this Wnt pathway in endothelial and mast cells. | PMID:30571485 | Journal of the American Heart Association |
| 2020 | Medium | ADTRP regulates TFPI transcription through transcription factor POU1F1; the ADTRP-response element was localized to a 50 bp region between -806 bp and -756 bp upstream of the TFPI transcription start site containing a POU1F1 binding site. Deletion of the POU1F1-binding site or knockdown of POU1F1 abolished ADTRP-mediated TFPI transcription. ChIP and EMSA confirmed POU1F1 binding to this element. | PMID:32445923 | Gene |
| 2015 | Low | C6ORF105/ADTRP expression in human macrophages is positively regulated by the transcription factor PPARγ; PPARγ activation increases C6ORF105 expression in human macrophages and atherosclerotic lesions in a PPARγ-dependent manner. | PMID:25595457 | FEBS letters |
| 2021 | Low | SNP rs6903956 in the ADTRP gene exhibits allele-specific differences in transcriptional activity; GATA2 binds preferentially to the G allele and the A (risk) allele has lower transcriptional activity and reduced GATA2 binding. | PMID:33856550 | Molecular genetics and genomics : MGG |
| 2021 | Low | ADTRP and LDL receptors LDLR, CD36, and LOX-1 positively regulate each other through NF-κB and AKT pathways: LDL receptor knockdown downregulates ADTRP, while LDL receptor overexpression increases ADTRP via NF-κB; reciprocally, ADTRP overexpression upregulates LDLR/CD36/LOX-1 and knockdown downregulates them. | PMID:33746034 | Biochimica et biophysica acta. Molecular basis of disease |
| 2022 | Medium | Adtrp promotes thermogenesis in brown/beige adipose tissue by binding to S100b and mediating its secretion, which in turn promotes β3-adrenergic receptor-mediated thermogenesis via sympathetic innervation. Adtrp KO mice display cold intolerance and excess lipid accumulation in brown adipose tissue, and thermogenesis can be rescued by direct β3-AR stimulation with CL316,243. | PMID:35804197 | Cellular and molecular life sciences : CMLS |
| 2021 | Medium | Hepatic overexpression of Adtrp in diet-induced obese mice did not influence FAHFA levels in plasma or liver, and had no significant effect on lipid profiles, glucose metabolism, or liver transcriptome, indicating that hepatic Adtrp alone is not a major regulator of FAHFA levels or metabolic homeostasis in this context. | PMID:34288722 | American journal of physiology. Cell physiology |

## Citations

- PMID:21868574
- PMID:25595457
- PMID:27018888
- PMID:28341552
- PMID:28645652
- PMID:30571485
- PMID:32152231
- PMID:32445923
- PMID:33746034
- PMID:33856550
- PMID:34288722
- PMID:35804197
