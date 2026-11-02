---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKIP1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9NQ31
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 19
citation_count: 19
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKIP1 (human)

## Current model (mechanistic narrative)

AKIP1 (BCA3) is a context-dependent signaling adaptor that converts protein kinase A (PKA) activity into transcriptional and metabolic outputs across NF-κB, Wnt/β-catenin, and mitochondrial pathways [PMID:20562110, PMID:23319652, PMID:30936461]. In its best-characterized role, AKIP1 expression determines whether PKA acts as an NF-κB activator: in cells with high AKIP1, PKA-activating agents enhance p65–PKAc interaction, p65 Ser-276 phosphorylation, and NF-κB-dependent transcription, effects reversed by AKIP1 knockdown [PMID:20562110], and AKIP1 likewise drives cAMP/PKA-dependent p65 nuclear translocation in myometrial cells [PMID:34166397]. Through this NF-κB axis and cooperation with SP1/AP2, AKIP1 transactivates VEGF-C and the CXC chemokines CXCL1/2/8 to drive angiogenesis and tumor growth [PMID:24413079, PMID:29520695], and it transactivates ZEB1 to promote EMT [PMID:29218247]. In the Wnt pathway AKIP1 binds β-catenin, retains it in the nucleus by blocking the β-catenin–APC interaction, and enhances PKAc-mediated β-catenin phosphorylation to recruit CBP and activate downstream transcription, promoting HCC invasion and metastasis [PMID:30936461]. AKIP1 also activates AKT signaling, feeding both NF-κB nuclear translocation via mTOR in tumor cells [PMID:29133128] and rpS6/eEF2-dependent cardiomyocyte hypertrophy [PMID:24169435, PMID:36899057]. Independently of transcription, AKIP1 localizes to interfibrillary mitochondria, interacts with apoptosis-inducing factor (AIF), enhances electron transport chain coupling, reduces ROS, and protects against oxidant- and ischemia-induced cell death [PMID:23319652, PMID:24236204, PMID:40869079]. Additional partners place AKIP1 at the interface of cytoskeletal and viral processes: it binds GTP-loaded Rac1 to modulate actin-dependent cell spreading [PMID:17227220], cooperates with YY1 to transactivate HSP90AA1 and thereby stabilize EGFR [PMID:37596322], and is co-opted by Ebola virus VP35 to activate PKA–CREB1 signaling required for viral replication [PMID:35474062]. AKIP1 protein stability is controlled by a UBE2S/USP15 module that removes K11-linked ubiquitination, augmenting NF-κB output [PMID:39098687].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus, GO:0005739 mitochondrion, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-74160 Gene expression (Transcription), R-HSA-1430728 Metabolism, R-HSA-1643685 Disease
- **partners:** PRKACA, RELA, CTNNB1, AIFM1, RAC1, YY1, SP1, USP15
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | AKIP1 acts as a molecular determinant of PKA signaling in NF-κB activation: in cells with high endogenous AKIP1 (MDA-MB231, MCF7), PKA-activating agents enhanced NF-κB-dependent transcriptional activity, the interaction between p65 and PKAc, and phosphorylation of p65 on Ser-276; RNAi knockdown of AKIP1 reversed these effects, showing AKIP1 switches PKA from an NF-κB inhibitor to an activator. | PMID:20562110 | The Journal of biological chemistry |
| 2007 | High | AKIP1 (BCA3) is a direct Rac1-interacting protein: it binds specifically to GTP-loaded Rac1 but not GDP-Rac1 in vivo; amino acids 76–125 of BCA3 are required for Rac1 binding; BCA3 and Rac1 co-localize perinuclearly in CSF-1-treated osteoclasts; BCA3 overexpression markedly attenuates CSF-1-induced cell spreading, implicating BCA3 in Rac1-dependent actin remodeling. | PMID:17227220 | Journal of bone and mineral research |
| 2013 | High | AKIP1 is preferentially localized to interfibrillary mitochondria in cardiac myocytes and interacts with the mitochondrial protein apoptosis-inducing factor (AIF) under normal and oxidant stress conditions; cardiac gene transfer of AKIP1 increased mitochondrial AKIP1, decreased ROS generation, enhanced calcium tolerance, decreased cytochrome C release, and enhanced phosphorylation of mitochondrial PKA substrates upon ischemic stress. | PMID:23319652 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | High | AKIP1 overexpression in neonatal cardiomyocytes increases mitochondrial oxygen consumption rate (OCR) and ATP-linked OCR, reduces mitochondrial superoxide production, and enhances electron transport chain coupling efficiency without inducing mitochondrial biogenesis or changes in ETC density; AKIP1 silencing attenuates phenylephrine-stimulated OCR increases. | PMID:24236204 | PloS one |
| 2013 | Medium | AKIP1 overexpression in neonatal rat cardiomyocytes stimulates hypertrophic growth (increased cell size, cytoskeletal organization, protein synthesis) specifically through Akt phosphorylation, which activates ribosomal rpS6 and translation elongation factor eEF2; Akt inhibition fully blocks AKIP1-induced hypertrophy. | PMID:24169435 | International journal of molecular sciences |
| 2014 | Medium | AKIP1 transcriptionally upregulates VEGF-C by interacting with the VEGF-C promoter in cooperation with transcription factors SP1, AP2, and NF-κB, thereby driving angiogenesis and lymphangiogenesis in esophageal squamous cell carcinoma. | PMID:24413079 | Oncogene |
| 2019 | High | AKIP1 binds to β-catenin and retains it in the nucleus by blocking its interaction with APC; AKIP1 also enhances PKAc-mediated phosphorylation of β-catenin, leading to recruitment of CBP and activation of Wnt/β-catenin downstream transcription, promoting HCC invasion and metastasis. | PMID:30936461 | Oncogene |
| 2017 | Medium | AKIP1 promotes EMT in non-small-cell lung cancer by directly binding to the ZEB1 promoter and transactivating ZEB1 expression; this binding depends on an interaction between AKIP1 and the transcription factor SP1. | PMID:29218247 | American journal of cancer research |
| 2018 | Medium | AKIP1 elevates expression of CXC chemokines CXCL1, CXCL2, and CXCL8 in cervical cancer cells via NF-κB; an IKKβ inhibitor reduces AKIP1-induced chemokine expression, and these chemokines mediate AKIP1-driven angiogenesis (endothelial tube formation via CXCR2) and cancer cell proliferation. | PMID:29520695 | Molecular and cellular biochemistry |
| 2018 | Medium | miR-320 directly targets the AKIP1 3′UTR (confirmed by luciferase reporter assay) and suppresses AKIP1 expression; AKIP1 knockdown promotes cardiomyocyte apoptosis and loss of mitochondrial membrane potential upon hypoxia/reoxygenation, mirroring the effect of miR-320 overexpression, placing AKIP1 downstream of miR-320 in the mitochondrial apoptotic pathway. | PMID:30181740 | Cellular & molecular biology letters |
| 2022 | High | EBOV VP35 binds AKIP1, which consequently activates PKA and the downstream transcription factor CREB1; CREB1 is recruited into EBOV ribonucleoprotein complexes in viral inclusion bodies and is used for viral replication; AKIP1 depletion or PKA-CREB1 inhibition dramatically impairs EBOV replication. | PMID:35474062 | Nature communications |
| 2021 | Medium | AKIP1 mediates cAMP/PKA-driven enhancement of NF-κB (p65) nuclear translocation and COX-2 expression in myometrial cells; AKIP1 knockdown reverses forskolin-induced enhancement of IL-1β-driven COX-2 mRNA and reduces nuclear p65 and c-jun levels. | PMID:34166397 | PloS one |
| 2017 | Medium | AKIP1 (BCA3) promotes HCC tumor growth, metastasis, and angiogenesis through AKT activation, which in turn activates mTOR signaling and induces cytoplasm-to-nuclear translocation of NF-κB p65; blockage of AKT with LY294002 impairs these AKIP1-mediated phenotypes. | PMID:29133128 | Experimental cell research |
| 2023 | Medium | AKIP1 cooperates with transcription factor YY1 to drive transcriptional activation of HSP90AA1 (HSP90α), which stabilizes EGFR protein; YY1 directly interacts with AKIP1, and HSP90α overexpression rescues EGFR instability caused by AKIP1 depletion. | PMID:37596322 | Oncogene |
| 2024 | Medium | UBE2S recruits deubiquitinase USP15 to remove K11-linked ubiquitination from AKIP1, thereby stabilizing AKIP1 protein; increased AKIP1 stability then augments NF-κB transcriptional activity and promotes GBM progression. | PMID:39098687 | International journal of biological macromolecules |
| 2023 | Medium | In cardiomyocyte-specific AKIP1 transgenic mice, AKIP1 overexpression promotes exercise-induced cardiomyocyte elongation (physiological hypertrophy) via Akt activation, C/EBPβ downregulation, and CITED4 de-repression, as well as RSK3 reduction, PP2Ac increase, and SRF dephosphorylation; AKIP1 protein clusters were detected in the cardiomyocyte nucleus by electron microscopy. | PMID:36899057 | Scientific reports |
| 2018 | Low | AKIP1 is incorporated into HIV-1 particles via its C-terminus, which is the same region that binds the catalytic subunit of PKA (PKAc); because PKAc is known to be packaged into HIV-1 particles, AKIP1 incorporation is likely mediated through its interaction with PKAc. However, incorporated AKIP1 had no detected effect on HIV-1 infectivity. | PMID:29677171 | Viruses |
| 2014 | Low | Exon 3 and exon 5 of BCA3 (AKIP1) are required for nuclear localization; a splice variant lacking exon 3 and exon 5 shows altered subcellular localization and reduced NF-κB-dependent reporter activity compared to full-length BCA3, suggesting these exons encode a nuclear localization signal and an NF-κB regulatory domain. | PMID:25526186 | Genetics and molecular research |
| 2025 | Medium | AKIP1 overexpression in porcine cells reduces apoptosis (caspase-3/7 activity), suppresses MPTP-mediated necrosis, decreases lipid peroxidation (ferroptosis marker), lowers mitochondrial superoxide production, and enhances mitochondrial respiration and recovery following H2O2-induced oxidative challenge. | PMID:40869079 | International journal of molecular sciences |

## Citations

- PMID:17227220
- PMID:20562110
- PMID:23319652
- PMID:24169435
- PMID:24236204
- PMID:24413079
- PMID:25526186
- PMID:29133128
- PMID:29218247
- PMID:29520695
- PMID:29677171
- PMID:30181740
- PMID:30936461
- PMID:34166397
- PMID:35474062
- PMID:36899057
- PMID:37596322
- PMID:39098687
- PMID:40869079
