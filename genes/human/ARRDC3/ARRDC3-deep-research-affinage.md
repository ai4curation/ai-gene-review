---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARRDC3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96B67
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 20
citation_count: 20
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARRDC3 (human)

## Current model (mechanistic narrative)

ARRDC3 is an α-arrestin adaptor protein that controls the trafficking, ubiquitination, and degradation of plasma-membrane receptors, thereby restraining receptor-driven proliferative and migratory signaling across multiple cancers [PMID:20603614, PMID:29416926, PMID:38389126]. It engages target receptors through an electropositive N-terminal lobe — paralleling the receptor-recognition surface of β-arrestins for the β2-adrenergic receptor [PMID:25220262] — while its two C-terminal PPXY motifs recruit NEDD4-family E3 ubiquitin ligases (NEDD4, WWP2, Itch) that mediate substrate ubiquitination, with crystallography and binding measurements defining a high-affinity, avid engagement of both PPXY motifs with tandem WW domains [PMID:24379409, PMID:26490116, PMID:29416926]. Through this adaptor logic ARRDC3 drives internalization and degradation of integrin β4 [PMID:20603614], directs the activated GPCR PAR1 into the ALIX/ESCRT-III lysosomal degradative pathway to terminate persistent JNK signaling [PMID:26490116, PMID:29348172], and promotes ubiquitination and degradation of AXL receptor tyrosine kinase to dampen AKT and ERK output [PMID:38389126]. ARRDC3 also localizes to EEA1-positive early endosomes, where it binds β2AR ligand-independently and delays its SNX27-dependent recycling [PMID:27226565]. Independently of its ligase-adaptor activity, ARRDC3 sequesters the Hippo co-activators YAP and TAZ via PPXY–WW interactions and routes YAP to lysosomal degradation, suppressing oncogenic transcription and metastasis [PMID:29416926, PMID:29364502, PMID:33722977]. Its activity is gated by post-translational and transcriptional inputs: ubiquitination of its own PPXY motifs is required for PAR1 trafficking and controls ARRDC3 stability and localization [PMID:37223976]; phosphorylation of Y394 within a PPXY motif switches ARRDC3 between c-Src binding and WWP2 binding [PMID:40409556]; phosphorylation of Y382 by the insulin receptor links ARRDC3 to hepatic insulin sensitivity and glucose production [PMID:32156724]; and its expression is set by SIRT2-mediated promoter deacetylation, promoter methylation, and the transcription factors SRF and ZBTB10 [PMID:24457910, PMID:39873948, PMID:32509187]. Beyond these receptor and Hippo axes, ARRDC3 has been implicated in adipose UCP1 regulation, liver fibrosis, and antiviral defense.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005768 endosome, GO:0005764 lysosome, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-9609507 Protein localization, R-HSA-5653656 Vesicle-mediated transport, R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction
- **partners:** NEDD4, WWP2, ITCH, YAP1, WWTR1, ITGB4, AXL, SRC
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | ARRDC3 directly binds to a phosphorylated form of integrin β4 (ITGβ4), leading to its internalization, ubiquitination, and degradation, thereby suppressing breast cancer progression. | PMID:20603614 | Oncogene |
| 2013 | High | ARRDC3 recruits the NEDD4-family E3 ubiquitin ligase NEDD4 via two C-terminal PPXY motifs; highest-affinity binding (Kd ~300 nM) involves avid interaction of both PPXY motifs with WW2-WW3 or WW3-WW4 combinations of NEDD4, with the third WW domain of NEDD4 binding PPXY1 (Kd = 3 μM) and a 310-helix Val-352' contributing to high-affinity binding. | PMID:24379409 | The Journal of biological chemistry |
| 2014 | High | Crystal structures of the N-terminal lobe of ARRDC3 reveal a large electropositive region; residues within this basic patch are important for binding to the β2-adrenergic receptor (β2AR), paralleling receptor-recognition mechanisms of β-arrestins. | PMID:25220262 | Protein science |
| 2014 | Medium | ARRDC3 expression in basal-like breast cancer cells is epigenetically silenced via SIRT2-dependent deacetylation of the ARRDC3 promoter; SIRT2 binds the ARRDC3 promoter (ChIP) and class III HDAC inhibitors restore ARRDC3 levels. | PMID:24457910 | Scientific reports |
| 2015 | High | ARRDC3 mediates ubiquitination of the ESCRT adaptor ALIX via the E3 ubiquitin ligase WWP2 (which interacts with ARRDC3 but not ALIX directly), enabling ALIX interaction with activated PAR1 and CHMP4B ESCRT-III subunit, thereby promoting lysosomal sorting of the GPCR PAR1. | PMID:26490116 | Molecular biology of the cell |
| 2016 | High | ARRDC3 primarily localizes to EEA1-positive early endosomes, directly interacts with β2AR in a ligand-independent manner, and negatively regulates β2AR entry into SNX27-occupied endosomal tubules, thereby delaying receptor recycling and increasing β2AR-dependent endosomal signaling. | PMID:27226565 | The Journal of biological chemistry |
| 2018 | High | ARRDC3 re-expression in invasive breast carcinoma restores normal PAR1 lysosomal trafficking through the ALIX-dependent degradative pathway, attenuates PAR1-stimulated persistent JNK signaling, and reduces breast carcinoma invasion in a JNK-dependent manner. | PMID:29348172 | The Journal of biological chemistry |
| 2018 | High | ARRDC3 interacts with YAP1 via YAP1 WW domains and ARRDC3 PPXY motifs, facilitates Itch E3 ubiquitin ligase-mediated ubiquitination and degradation of YAP1, thereby suppressing renal cell carcinoma growth, migration, invasion, and EMT. | PMID:29416926 | American journal of cancer research |
| 2018 | Medium | ARRDC3 binds YAP in colorectal cancer and decreases YAP protein levels via lysosome-mediated degradation, suppressing CRC progression; this ARRDC3-YAP regulatory axis is conserved from Drosophila to mammals. | PMID:29364502 | FEBS letters |
| 2020 | High | ARRDC3 directly interacts with the insulin receptor (IR) and is phosphorylated on a conserved tyrosine Y382 in its carboxyl-terminal domain by IR; liver-specific Arrdc3 knockout increases IR protein at the plasma membrane, enhances insulin sensitivity (increased FOXO1 phosphorylation, reduced PEPCK, increased glucokinase), and reduces hepatic glucose production. | PMID:32156724 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | High | ARRDC3 suppresses PAR1-induced Hippo signaling by sequestering TAZ (WWTR1) independently of ARRDC3-regulated PAR1 trafficking; ARRDC3 C-terminal PPXY motifs interact with TAZ WW domain, and this interaction is required for suppression of TNBC migration and lung metastasis in vivo. | PMID:33722977 | Journal of cell science |
| 2017 | Medium | Adipocyte-specific deletion of Arrdc3 increases Ucp1 expression in subcutaneous and parametrial white adipose tissue; however, canonical β-adrenergic receptor signaling is not altered in Arrdc3-null adipocytes, and Arrdc3-null adipocytes treated with β-adrenergic agonist show decreased (not increased) Ucp1—indicating the effect on Ucp1 is independent of canonical β-adrenergic signaling. | PMID:28291835 | PloS one |
| 2023 | High | Ubiquitination of ARRDC3 is mediated primarily through its two C-terminal PPXY motifs and is required for ARRDC3 function in GPCR (PAR1) trafficking and signaling; ubiquitination and the PPXY motifs also control ARRDC3 protein degradation, subcellular localization, and interaction with the NEDD4-family E3 ligase WWP2. | PMID:37223976 | Molecular biology of the cell |
| 2024 | Medium | ARRDC3 interacts with AXL receptor tyrosine kinase and promotes its ubiquitination and degradation, negatively regulating downstream AKT and ERK phosphorylation; ARRDC3 deficiency decreases sunitinib sensitivity in clear cell renal cell carcinoma cells. | PMID:38389126 | Cell cycle |
| 2025 | High | ARRDC3 tyrosine Y394 phosphorylation within its C-terminal PPxY motif functions as a phospho-regulatory switch: phosphorylated Y394 promotes interaction with c-Src via its SH2 domain and enables regulation of c-Src activity, while non-phosphorylated Y394 binds WWP2; Y394 phosphorylation disrupts WWP2 interaction and perturbs ARRDC3-dependent lysosomal trafficking of PAR1. | PMID:40409556 | The Journal of biological chemistry |
| 2022 | Medium | ARRDC3 inhibits liver fibrosis and epithelial-to-mesenchymal transition (EMT) via the ITGB4/PI3K/Akt signaling pathway; ARRDC3 overexpression reduced collagen deposition and EMT markers while decreasing ITGB4/PI3K/Akt activity in CCl4-induced rat fibrosis and TGF-β-treated LX-2 cells. | PMID:36154540 | Immunopharmacology and immunotoxicology |
| 2025 | Medium | ARRDC3 promotes lysosome-mediated YAP degradation during enterovirus infection, inhibiting enterovirus replication; YAP facilitates enterovirus replication by suppressing the interferon pathway independently of its transcriptional activity, and the ARRDC3-YAP axis shows broad-spectrum antiviral effects against HPIV3 and VSV. | PMID:40701343 | Virologica Sinica |
| 2025 | Medium | ZBTB10 transcription factor enhances ARRDC3 expression by binding to a specific response element in the ARRDC3 promoter (ChIP); elevated ARRDC3 then directly interacts with ITGB4 leading to its ubiquitination and degradation, downregulating PI3K/AKT phosphorylation in gastric cancer. | PMID:39873948 | Cellular oncology |
| 2020 | Medium | Serum response factor (SRF) promotes ARRDC3 transcription by binding the ARRDC3 promoter region; promoter methylation suppresses ARRDC3 expression and impairs SRF-promoter interaction; ARRDC3 inhibits breast cancer growth through the STAT3 signaling pathway. | PMID:32509187 | American journal of translational research |
| 2026 | Low | ARRDC3 promotes Drp1-dependent mitochondrial fragmentation and exacerbates neuronal ferroptosis in cerebral ischemia/reperfusion injury; exosomal CRYAB suppresses this pathway by reducing ARRDC3 expression, providing neuroprotection. | PMID:41555725 | Advanced healthcare materials |

## Citations

- PMID:20603614
- PMID:24379409
- PMID:24457910
- PMID:25220262
- PMID:26490116
- PMID:27226565
- PMID:28291835
- PMID:29348172
- PMID:29364502
- PMID:29416926
- PMID:32156724
- PMID:32509187
- PMID:33722977
- PMID:36154540
- PMID:37223976
- PMID:38389126
- PMID:39873948
- PMID:40409556
- PMID:40701343
- PMID:41555725
