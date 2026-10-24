---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AFP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P02771
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 17
citation_count: 17
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AFP (human)

## Current model (mechanistic narrative)

AFP (alpha-fetoprotein) is an oncofetal glycoprotein whose cis-regulatory elements drive lineage-restricted expression in visceral and yolk-sac endoderm, fetal liver hepatocytes, and gut/pancreas epithelium during development [PMID:16708394], and whose intracellular pool in HCC cells functions as a pro-tumorigenic, anti-apoptotic signaling hub [PMID:33009373]. Mechanistically, intracellular AFP binds the RNA-binding protein HuR and drives its cytoplasmic accumulation, suppressing Fas mRNA translation and blocking Fas/FADD-mediated extrinsic apoptosis; AFP-deficient mice show reduced DEN-induced tumor progression with increased apoptosis [PMID:33009373]. AFP also acts as an HSP90 co-chaperone, binding HSP90 to stabilize the client oncoproteins c-MYC and c-MET against ubiquitin-mediated degradation [PMID:39135041], and directly binds PTEN to engage PI3K/AKT signaling that promotes proliferation [PMID:26078940, PMID:37217071]. AFP transcription is positively regulated by FOXM1 [PMID:35955438] and is directly repressed by HBP1 binding the AFP promoter, a repression that the HBV protein HBx relieves by binding HBP1 [PMID:33794968]; AFP levels are further supported post-translationally by gp96, which stabilizes the transcription factor NR5A2 by blocking its SUMOylation and degradation [PMID:37204028]. A G→A substitution at position -119 of the AFP promoter, within an HNF1 binding site, increases HNF1α binding and elevates AFP expression, causing hereditary persistence of alpha-fetoprotein in adults [PMID:7684942]. Beyond hepatocellular cancer, secreted AFP signals through its receptor (AFPR) to promote proliferation and invasion and engages Wnt/β-catenin signaling in AFP-producing gastric cancer [PMID:34650031, PMID:30809100].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0044183 protein folding chaperone, GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005829 cytosol, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5357801 Programmed Cell Death, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease, R-HSA-392499 Metabolism of proteins
- **partners:** HUR, HSP90, PTEN, GP73, HBP1, C-MYC, C-MET
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1993 | High | A G→A substitution at position -119 in the AFP gene promoter (within an HNF1 binding site) causes hereditary persistence of alpha-fetoprotein (HPAFP) in adults. The mutant sequence binds HNF1α more tightly than wild-type in gel retardation assays, and AFP promoter constructs containing this substitution drive higher CAT reporter expression in transfected human hepatoma cells, establishing that enhanced HNF1α binding at this site paradoxically increases rather than represses AFP expression. | PMID:7684942 | Human molecular genetics |
| 1992 | Medium | AFP mRNA is expressed in baboon fetal liver, gastrointestinal tract, and kidney but not in brain, skin, spleen, pancreas, muscle, heart, thymus, placenta, or amnion. After injection of radiolabeled AFP into pregnant baboons, AFP protein was taken up by all fetal tissues (highest in adipose, kidney, intestine, lung, liver, cerebral cortex), demonstrating that intracellular AFP in non-hepatic fetal tissues is predominantly of plasma origin rather than locally synthesized. | PMID:1379224 | Journal of biochemistry |
| 1994 | Medium | AFP inhibits apoptosis (activation-induced cell death) in HL-60 cells via binding to AFP receptors (AFPr). Using monoclonal antibodies 167H.1 and 167H.4 that are agonists for distinct AFPr isoforms, both AFP and the 167H.1 MAb (but not 167H.4 MAb) blocked apoptosis, indicating AFP's growth-enhancing effect is due to suppression of cell death rather than mitogenic activity. Loss of AFPr expression correlated with increased susceptibility to apoptosis during cellular senescence. | PMID:7532927 | Anticancer research |
| 2006 | Medium | AFP regulatory elements (promoter/enhancer) direct expression specifically in visceral endoderm, yolk sac endoderm, fetal liver hepatocytes, and gut/pancreas epithelium in transgenic mice. GFP reporter driven by AFP cis-regulatory elements allowed real-time visualization and flow cytometric isolation of these endodermal lineage cells, establishing the sufficiency of these elements for tissue-specific expression. | PMID:16708394 | Developmental dynamics |
| 2011 | Medium | AFP immunosuppressive activity maps to its domain 2 (D2) and domain 3 (D3), but not domain 1 (D1). Recombinant D2-AFP and D3-AFP, like full-length AFP, significantly inhibited HLA-DR high/CD11c high and CD80+/CD86 high expression on monocyte-derived dendritic cells and impaired IL-12(p70) secretion, whereas D1-AFP did not suppress these markers. Full-length AFP additionally suppressed CD40 expression, which was not replicated by any individual domain. | PMID:21235824 | BMC immunology |
| 2014 | Low | AFP activates the PI3K/Akt signaling pathway in hepatoma cells to promote proliferation. AFP intervention in HepG2 cells increased PI3K and Akt protein levels, and this effect was blocked by AFP monoclonal antibody or the PI3K inhibitor LY294002, establishing a direct link between AFP and PI3K/Akt activation. | PMID:24425104 | Tumour biology |
| 2015 | Low | AFP protein directly binds to PTEN (phosphatase and tensin homolog), whereas human serum albumin (HSA) does not. Co-localization and co-immunoprecipitation showed strong AFP-PTEN interaction in cells. Molecular docking identified AFP domains I and III as the PTEN contact regions, and in silico substitution of AFP residues 490M and 105L (corresponding to steric clash-causing K490 and R105 in HSA) explained the absence of HSA-PTEN binding. | PMID:26078940 | BioMed research international |
| 2015 | Low | HBx (hepatitis B virus X protein) preferentially upregulates expression of both AFP and AFP receptor (AFPR) in normal liver cells (L-02) and hepatoma cells. AFPR signaling then stimulates Src expression via the PI3K pathway, as PI3K inhibitors Ly294002 and GDC0941 suppressed AFPR-mediated Src upregulation in AFPR-positive HCC lines. Laser confocal microscopy confirmed co-localization of AFP, AFPR, and Src. | PMID:25943101 | BMC cancer |
| 2020 | High | Intracellular AFP promotes HCC progression by binding to the RNA-binding protein HuR, causing HuR to accumulate in the cytoplasm, which inhibits Fas mRNA translation and thereby suppresses the Fas/FADD-mediated extrinsic apoptotic pathway. AFP-deficient mice showed reduced DEN-induced liver tumor progression with increased apoptosis, and AFP knockdown in human HCC cells inhibited proliferation and induced apoptosis via Fas/FADD activation. | PMID:33009373 | Cell death & disease |
| 2021 | Medium | GP73 (Golgi protein 73) directly binds to AFP and increases AFP secretion from HCC cells. Extracellular AFP then promotes proliferation and metastasis of HCC cells expressing AFP receptor (AFPR). Extracellular GP73 independently also promotes HCC cell malignancy, and AFP and GP73 synergize extracellularly to enhance the malignant phenotype and drug resistance to sorafenib. | PMID:34650031 | Oncogenesis |
| 2021 | High | Transcription factor HBP1 directly represses AFP gene expression by binding to the AFP gene promoter, as demonstrated by luciferase reporter assay, ChIP, and EMSA. HBV protein HBx promotes AFP expression by binding directly to HBP1 and blocking its transcriptional repression. HBP1-mediated AFP repression attenuated AFP effects on PTEN, MMP9, and caspase-3, inhibiting proliferation, migration, and inducing apoptosis in hepatoma cells. HBP1 knockout mice showed increased AFP expression and hepatoma progression. | PMID:33794968 | Journal of experimental & clinical cancer research |
| 2012 | Low | AFP gene silencing by siRNA in the AFP-high HCC cell line EGHC-9901 inhibited cell proliferation, caused G1-phase arrest, and significantly increased apoptosis with upregulation of caspase-3 expression. No significant changes in caspase-8, caspase-9, or Bcl-2 were detected, suggesting AFP specifically modulates caspase-3-mediated apoptosis. | PMID:22935208 | Discovery medicine |
| 2019 | Medium | AFP activates Wnt signaling in AFP-producing gastric cancer (APGC) cells, evidenced by decreased Axin1 and pGSK3β, and cascade activation of β-catenin, TCF1/TCF7, and c-Myc. Wnt-signaling blockade by Axin1 rescue or pathway inhibitor XAV939 reversed AFP-mediated growth and invasion in GC cell lines and derived xenografts. | PMID:30809100 | Cancer management and research |
| 2023 | Medium | AFP deletion in HepG2 cells inhibited proliferation by inactivating PI3K/AKT signaling. Unexpectedly, AFP knockout also increased metastatic capacity and EMT phenotype via activation of WNT5A/β-catenin signaling, an effect linked to activating mutations of CTNNB1. In a DEN/CCl4 HCC mouse model, AFP knockout suppressed primary tumor growth but promoted lung metastasis. A drug candidate (OA) interrupted AFP-PTEN interaction, suppressed tumor growth, and reduced lung metastasis via angiogenesis suppression. | PMID:37217071 | Cancer letters |
| 2023 | High | Heat shock protein gp96 promotes AFP expression at the transcriptional level in HCC by stabilizing the transcription factor NR5A2. gp96 and the SUMO E3 ligase RanBP2 compete for binding to NR5A2 at residues aa507–539; gp96 binding inhibits SUMOylation and subsequent ubiquitination/degradation of NR5A2, thereby maintaining NR5A2 stability and AFP transcription. In vivo, gp96 expression in tumors positively correlated with serum AFP levels. | PMID:37204028 | Journal of molecular cell biology |
| 2024 | Medium | Intracellular AFP acts as a co-chaperone of HSP90, binding to HSP90 and stabilizing its client oncoproteins c-MYC and c-MET by preventing their ubiquitin-mediated degradation. AFP knockdown or HSP90 inhibition destabilized c-MYC and c-MET and enhanced cytotoxicity of chemotherapeutic agents in AFP-producing HCC and gastric cancer cells. | PMID:39135041 | Cancer cell international |
| 2020 | Medium | FOXM1 transcription factor is upregulated in AFP-positive HCC and positively regulates AFP expression. FOXM1 knockdown reduced AFP expression and induced G2/M cell cycle arrest in AFP-positive HCC cells. The proteasome inhibitor carfilzomib attenuated FOXM1 protein expression and suppressed proliferation of AFP-positive HCC cells. | PMID:35955438 | International journal of molecular sciences |

## Citations

- PMID:1379224
- PMID:16708394
- PMID:21235824
- PMID:22935208
- PMID:24425104
- PMID:25943101
- PMID:26078940
- PMID:30809100
- PMID:33009373
- PMID:33794968
- PMID:34650031
- PMID:35955438
- PMID:37204028
- PMID:37217071
- PMID:39135041
- PMID:7532927
- PMID:7684942
