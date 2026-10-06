---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AZGP1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P25311
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 30
citation_count: 30
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AZGP1 (human)

## Current model (mechanistic narrative)

AZGP1 (zinc-alpha-2-glycoprotein, ZAG) is a secreted MHC class I-like glycoprotein, structurally resembling a class I MHC heavy chain but lacking beta2-microglobulin binding, whose groove accommodates a nonpeptidic lipid-related ligand consistent with a role in lipid catabolism [PMID:10206894]. It is encoded on chromosome 7q22, distinct from classical MHC genes [PMID:8162703]. As a metabolic effector, ZAG binds beta3- and beta2-adrenergic receptors (but not beta1-AR) with nanomolar affinity to stimulate cAMP production, and its anti-obesity, lipolytic, and insulin-sensitizing actions are abolished by propranolol, establishing a beta-AR-mediated mechanism [PMID:22227600, PMID:21245862]. Through this axis ZAG induces uncoupling proteins (UCP-1, UCP-2 via beta3-AR/cAMP; UCP-3 via MAPK) [PMID:15246563] and drives white adipose tissue browning by promoting PPARgamma/EBF2 recruitment to the Prdm16 promoter and PPARgamma/PGC-1alpha recruitment to the Ucp1 promoter [PMID:29570397]. In hypothalamic POMC neurons, AZGP1 enhances leptin-JAK2-STAT3 signaling by binding acylglycerol kinase (AGK) and blocking its ubiquitination, increasing neuronal excitability and regulating whole-body energy homeostasis [PMID:38643150]. AZGP1 also acts broadly as a tumor suppressor and anti-fibrotic factor: it blocks TGF-beta1-mediated ERK2 phosphorylation to suppress epithelial-mesenchymal transition in pancreatic and hepatocellular carcinoma [PMID:20581862, PMID:26902423], inhibits proliferation, glycolysis, and angiogenesis [PMID:24918753, PMID:38659028, PMID:41535762], and signals additionally through PTEN/Akt, mTOR/FASN, TGF-beta1/Smad3, and PI3K/AKT pathways [PMID:27993894, PMID:24918753, PMID:37669935, PMID:40305469]. Its expression is tightly controlled at multiple levels: transcriptionally by the androgen receptor and Ikaros [PMID:30820960, PMID:27993894], epigenetically by histone deacetylation and promoter methylation [PMID:18978557, PMID:41535762], post-transcriptionally by the MIR155HG/miR-155 axis [PMID:38729323], and post-translationally by TRIM25-mediated ubiquitination and proteasomal degradation [PMID:38183356, PMID:37927217].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0048018 receptor ligand activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease, R-HSA-168256 Immune System
- **partners:** PIP, ADRB3, ADRB2, AGK, TRIM25
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | High | Crystal structure of ZAG solved at 2.8 Å resolution, revealing it resembles a class I MHC heavy chain but does not bind beta2-microglobulin. The ZAG groove (analogous to MHC peptide-binding groove) contains a nonpeptidic compound, suggesting a role in lipid catabolism. | PMID:10206894 | Science |
| 2008 | High | Crystal structure of the ZAG–PIP (prolactin-inducible protein) complex purified from human seminal plasma determined by X-ray crystallography; PIP's beta-structure aligns with the alpha3 domain of ZAG forming a long interface stabilized by 12 hydrogen bonds and 3 salt bridges, with a buried area of ~914 Å². | PMID:18930737 | Journal of Molecular Biology |
| 2004 | Medium | ZAG induces uncoupling protein (UCP) expression in adipose and muscle cells: UCP-1 in brown adipose tissue via beta3-adrenergic receptor (beta3-AR)/cAMP pathway; UCP-2 in C2C12 myotubes via beta3-AR/cAMP; UCP-3 in myotubes via MAPK (not beta3-AR). | PMID:15246563 | Cancer Letters |
| 2010 | High | AZGP1 suppresses TGF-beta-mediated EMT in pancreatic cancer cells by blocking TGF-beta-mediated ERK2 phosphorylation. Silencing AZGP1 increases invasiveness and induces mesenchymal markers (vimentin, integrin-alpha5) while reducing epithelial markers (CDH1, desmoplakin, keratin-19). AZGP1 expression is epigenetically silenced by histone deacetylation. | PMID:20581862 | Oncogene |
| 2011 | High | ZAG binds to the beta3-adrenergic receptor (Kd 46 nM) and beta2-AR (Kd 71 nM) but not beta1-AR in CHO-K1 cells transfected with human beta-ARs, and stimulates cAMP production. Anti-obesity and anti-diabetic effects of ZAG in ob/ob mice (weight loss, improved glucose tolerance, insulin sensitivity, glucose transport) are abolished by propranolol, confirming beta-AR-mediated mechanism. | PMID:22227600 | Biochimica et Biophysica Acta |
| 2008 | High | Recombinant Zag suppresses proliferation of primary renal epithelial cells, while siRNA knockdown of Zag increases proliferation. In vivo siRNA-mediated Zag suppression in aged mice increases epithelial cell proliferation after renal ischemia/reperfusion but also increases parenchymal fibrosis. | PMID:18815245 | Journal of the American Society of Nephrology |
| 2018 | High | ZAG induces white adipose tissue (WAT) browning in mice by stimulating PPARgamma and EBF2 expression, promoting their recruitment to the Prdm16 promoter, inducing Prdm16 expression. In brown adipose tissue, ZAG promotes PPARgamma and PGC-1alpha and their recruitment to the Ucp1 promoter, increasing Ucp1 expression. | PMID:29570397 | FASEB Journal |
| 2016 | Medium | AZGP1 suppresses EMT and hepatic carcinogenesis by blocking TGF-beta1-mediated ERK2 phosphorylation in hepatocellular carcinoma cells, reducing mesenchymal markers and inhibiting cell invasion in vitro; local AZGP1 injection in vivo significantly inhibits lung metastasis. | PMID:26902423 | Cancer Letters |
| 2017 | Medium | Transcription factor Ikaros binds to the AZGP1 promoter and transactivates its expression in HCC cells. Downregulation of AZGP1 in HCC is associated with histone deacetylation. Positive feedback between H4 acetylation-mediated Ikaros transactivation and Ikaros-mediated H4 acetylation regulates AZGP1 expression. AZGP1 inhibits HCC cell migration and invasion through regulation of PTEN/Akt and CD44s pathways. | PMID:27993894 | Carcinogenesis |
| 2019 | High | AZGP1 is an androgen-responsive gene regulated by the androgen receptor (AR): ChIP-Seq identifies canonical androgen-responsive elements (AREs) at the AZGP1 enhancer, and dual-luciferase reporter assays show AREs are highly responsive to androgen; mutations in AREs abolish reporter activity. AZGP1 promotes G1/S phase transition by increasing cyclin D1 levels. | PMID:30820960 | Journal of Cellular Physiology |
| 2014 | Medium | AZGP1 overexpression in LoVo colorectal cancer cells suppresses mTOR pathway activation and FASN-regulated endogenous fatty acid synthesis, reducing proliferation, inducing G2 arrest and apoptosis, and decreasing migration. | PMID:24918753 | PLoS One |
| 2010 | Medium | Macrophage-conditioned medium and TNF-alpha suppress ZAG mRNA expression and protein secretion by human adipocytes, while ZAG is produced primarily by mature adipocytes (not preadipocytes or macrophages), identifying macrophage-associated inflammation as a regulator of ZAG in adipose tissue. | PMID:20595026 | Molecular and Cellular Endocrinology |
| 2024 | High | AZGP1 in hypothalamic POMC neurons regulates whole-body energy homeostasis: POMC-specific overexpression of Azgp1 reduces food intake, raises energy expenditure, improves leptin and insulin sensitivity, reduces liver steatosis, and promotes adipose browning under high-fat diet. Mechanistically, AZGP1 enhances leptin-JAK2-STAT3 signaling by interacting with acylglycerol kinase (AGK) to block its ubiquitination and degradation, increasing POMC neuron excitability. | PMID:38643150 | Nature Communications |
| 2024 | Medium | AZGP1 interacts with TRIM25 (tripartite motif-containing protein 25) via co-immunoprecipitation. TRIM25 catalyzes ubiquitination of AZGP1, promoting its proteasomal degradation. TRIM25 knockdown leads to AZGP1 upregulation and induces cholangiocarcinoma cell apoptosis. AZGP1 overexpression suppresses tumor growth in xenograft models. | PMID:38183356 | Journal of Cellular and Molecular Medicine |
| 2024 | High | AZGP1 deficiency in mouse prostate promotes angiogenesis in vivo (increased vessel density by 6 months in AZGP1-/- mice). AZGP1 overexpression in xenograft tumors decreases microvessel density. AZGP1 directly inhibits human umbilical vein endothelial cell proliferation, migration, tubular formation, and branching in vitro. Proteomics of AZGP1-overexpressing xenografts identifies enrichment of angiogenesis pathway proteins (YWHAZ, EPHA2, SERPINE1, PDCD6, MMP9, etc.). | PMID:38659028 | Journal of Translational Medicine |
| 2023 | Medium | AZGP1 interacts with lenvatinib as a key target in intrahepatic cholangiocarcinoma (ICC). Lenvatinib increases H3K27Ac acetylation at the AZGP1 promoter to upregulate AZGP1 expression. AZGP1, in turn, inhibits ICC EMT by regulating the TGF-beta1/Smad3 signaling pathway in an AZGP1-dependent manner. | PMID:37669935 | Cell Death & Disease |
| 2008 | Medium | AZGP1 expression in lung adenocarcinoma cell lines is regulated by histone deacetylation: treatment with trichostatin A (TSA, HDAC inhibitor) induced 713-fold and 169-fold increase in AZGP1 mRNA in A549 and SKLU1 cells, respectively, while 5-aza-2'-deoxycytidine (demethylating agent) had minimal effect. | PMID:18978557 | Journal of Thoracic Oncology |
| 2011 | Medium | Recombinant ZAG stimulates lipolysis in human adipocytes in vitro, and ZAG expression and secretion by subcutaneous adipose tissue is elevated in cachectic cancer patients correlating with weight loss and serum glycerol levels. | PMID:21245862 | British Journal of Cancer |
| 2012 | Medium | Oral ZAG administration in ob/ob mice increases endogenous murine ZAG serum levels through interaction with beta-adrenergic receptors in the gastrointestinal tract (particularly esophagus), as effects on body weight, temperature, urinary glucose, and insulin sensitivity are abolished by co-administration of propranolol. Tryptic digestion inactivates ZAG. | PMID:22903615 | Endocrinology |
| 2024 | High | AZGP1 aggravates macrophage M1 polarization and pyroptosis in periodontitis through NLRP3/caspase-1 signaling. AAV-mediated Azgp1 overexpression in the periodontium enhances M1 macrophage proportion and pyroptosis markers; Azgp1-/- mice show opposite effects. NLRP3 or caspase-1 inhibition rescues the effects of Azgp1 overexpression. | PMID:38491721 | Journal of Dental Research |
| 2025 | Medium | AZGP1 inhibits EMT in retinal pigment epithelial (RPE) cells and subretinal fibrosis by regulating the PI3K/AKT signaling pathway. Knockdown and overexpression studies in ARPE-19 cells confirm AZGP1 modulates PI3K/AKT activity. Intravitreal injection of recombinant AZGP1 in a laser-induced SRF mouse model reduces collagen I, CD31-positive area, and fibrosis markers. | PMID:40305469 | Investigative Ophthalmology & Visual Science |
| 2022 | Medium | AZGP1 has protective anti-fibrotic effects in kidney disease: recombinant AZGP1 treatment in mice with unilateral ureteric obstruction preserves tubular integrity, reduces collagen deposition and fibrosis markers, and reduces stress-induced tubular lipid droplet accumulation by improving lipid metabolism/fatty acid oxidation gene expression. | PMID:35054830 | International Journal of Molecular Sciences |
| 2024 | Medium | TRIM25 promotes ubiquitination and degradation of AZGP1 in breast cancer, identified through co-immunoprecipitation. AZGP1 knockdown promotes breast cancer cell proliferation, migration, and invasion in vitro and in vivo. TRIM25 overexpression partially reverses the pro-tumorigenic effects of AZGP1 overexpression. | PMID:37927217 | Environmental Toxicology |
| 2026 | Medium | Promoter methylation (at cg26429636 region) silences AZGP1 transcription in prostate cancer cells, and low AZGP1 expression is associated with upregulated glycolysis (elevated L-lactic acid production, higher ECAR, reduced OCR). AZGP1 overexpression reduces glycolysis, suggesting AZGP1 suppresses aerobic glycolysis to inhibit metastasis. | PMID:41535762 | Cellular & Molecular Biology Letters |
| 2025 | Medium | Adipocyte-specific AZGP1 ablation aggravates insulin resistance and adipose tissue inflammation by increasing M1 macrophage proportion and inhibiting AKT signaling in mice on high-fat diet. Exogenous ZAG inhibits palmitic acid-induced M1 macrophage polarization via beta3-AR/PKA/STAT3 signaling in RAW264.7 macrophages. | PMID:40068519 | International Immunopharmacology |
| 2024 | Medium | MIR155HG/miR-155-5p/-3p axis targets AZGP1 through direct binding to the AZGP1 3'UTR (confirmed by dual-luciferase assay). miR-155-5p/-3p suppress AZGP1, and AZGP1 overexpression rescues inhibition of inflammatory cytokine production (IL-1beta, IL-6) and alpha-SMA expression induced by miR-155 overexpression in hypertrophic scar fibroblasts. | PMID:38729323 | Cellular Signalling |
| 1994 | High | The human AZGP1 gene was mapped to chromosome 7q22 by fluorescent in situ hybridization (FISH), distinct from classical MHC genes on chromosome 6, indicating evolutionary transposition events. | PMID:8162703 | Cytogenetics and Cell Genetics |
| 2024 | Medium | ZAG promotes white adipose tissue progenitor cell differentiation toward fibrosis (not adipogenesis) in triple-negative breast cancer: TNBC-secreted ZAG inhibits adipogenesis and instead induces fibrotic gene expression in adipose stem and progenitor cells (ASPCs). ZAG depletion in TNBC cells attenuates fibrosis in white adipose tissue and inhibits tumor growth. | PMID:38496643 | bioRxiv |
| 2009 | Low | Recombinant ZAG stimulates adiponectin release from human differentiated adipocytes in vitro, establishing a functional link between ZAG and adiponectin production. | PMID:19549246 | Clinical Endocrinology |
| 2024 | Low | AZGP1 functions as an RNA-binding protein (RBP) in lung epithelial cells, regulating alternative splicing events (including DDAH1 and SFRP1) and inhibiting AT2 cell proliferation by modulating expression of SAMD5, DNER, DPYSL3, GBP5, GBP3, and KCNJ2, as identified through scRNA-seq and bulk RNA-seq analyses in COPD. | PMID:38950687 | Gene |

## Citations

- PMID:10206894
- PMID:15246563
- PMID:18815245
- PMID:18930737
- PMID:18978557
- PMID:19549246
- PMID:20581862
- PMID:20595026
- PMID:21245862
- PMID:22227600
- PMID:22903615
- PMID:24918753
- PMID:26902423
- PMID:27993894
- PMID:29570397
- PMID:30820960
- PMID:35054830
- PMID:37669935
- PMID:37927217
- PMID:38183356
- PMID:38491721
- PMID:38496643
- PMID:38643150
- PMID:38659028
- PMID:38729323
- PMID:38950687
- PMID:40068519
- PMID:40305469
- PMID:41535762
- PMID:8162703
