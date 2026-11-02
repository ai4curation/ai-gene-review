---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMIGO2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q86SJ2
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for AMIGO2 (human)

## Current model (mechanistic narrative)

AMIGO2 is a type I transmembrane cell-surface protein that functions as a membrane scaffold and homophilic adhesion molecule to promote cell survival, adhesion, and tissue patterning [PMID:26553931, PMID:15107827, PMID:31693896]. Its central survival mechanism is direct binding of the PH domain of PDK1 through AMIGO2 residues 465–474, which recruits PDK1 to the plasma membrane and activates Akt; disrupting this interaction with a competing peptide abrogates Akt activation, triggers apoptosis, and blocks pathological angiogenesis [PMID:26553931]. This PDK1/Akt axis underlies AMIGO2's protective roles in cardiomyocytes after myocardial infarction [PMID:29718531] and its suppression of cisplatin-induced caspase activation, GSDME cleavage, and pyroptosis in lung cancer [PMID:37438979]. As a homophilic surface adhesion factor, AMIGO2 scales dendrite arbors of specific retinal neuron types and tunes downstream direction selectivity [PMID:31693896], and mediates fasciculation of medial habenular axons in the fasciculus retroflexus [PMID:35727300]. In cancer, AMIGO2 promotes tumor cell adhesion to hepatic sinusoidal endothelial cells to drive liver metastasis [PMID:28272394, PMID:35843033], a process that also proceeds paracrine: AMIGO2 carried in tumor-derived extracellular vesicles is internalized by hepatic endothelial cells to enhance their adhesiveness [PMID:35039535] and activates hepatic stellate cells via NF-κB to secrete IL-8 that boosts cancer cell migration [PMID:40155010]. AMIGO2 additionally interacts with the pseudokinase PTK7 and regulates its proteolytic processing in melanoma, where it is driven by a BET-dependent super-enhancer [PMID:29149598], and it induces EMT through TGFβ/Smad signaling at the invasive front [PMID:39379686]. AMIGO2 expression is post-transcriptionally controlled by METTL3-deposited m6A in its 5′-UTR, read context-dependently by YTHDC1 to regulate splicing or YTHDC2 to regulate stability [PMID:38360124, PMID:38432455].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity, GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005886 plasma membrane, GO:0031410 cytoplasmic vesicle, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease, R-HSA-5357801 Programmed Cell Death, R-HSA-1266738 Developmental Biology
- **partners:** PDK1, PTK7
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | High | AMIGO2 directly binds the pleckstrin homology (PH) domain of PDK1 via amino acid residues 465–474 in AMIGO2, acting as a membrane scaffold that recruits PDK1 to the plasma membrane and promotes Akt activation. Loss of AMIGO2 in endothelial cells leads to apoptosis and inhibition of angiogenesis with Akt inactivation. A synthetic peptide containing AMIGO2 residues 465–474 abrogated the AMIGO2–PDK1 interaction, Akt activation, and pathological angiogenesis in vivo. | PMID:26553931 | The Journal of cell biology |
| 2017 | High | AMIGO2 interacts with the pseudokinase PTK7, and AMIGO2 regulates PTK7 proteolytic processing. BET bromodomain proteins BRD2/4 occupy a melanoma-specific promoter and super-enhancer at the AMIGO2 locus; BET inhibitor treatment evicts BRD2/4, silences AMIGO2, and alters PTK7 processing. AMIGO2 silencing in melanoma cells induces G1/S cell-cycle arrest followed by apoptosis. | PMID:29149598 | Molecular cell |
| 2004 | Medium | DEGA/AMIGO2 is a type I transmembrane protein that localizes to the cell surface (confirmed by DEGA-GFP fusion construct in 293 cells). Stable antisense-mediated knockdown in gastric adenocarcinoma AGS cells caused altered morphology, increased ploidy, chromosomal instability, decreased cell adhesion and migration, and near-complete abrogation of tumorigenicity in nude mice. | PMID:15107827 | Oncogene |
| 2017 | High | AMIGO2 expression in tumor cells mediates their preferential adhesion to liver endothelial cells (but not lung endothelial cells), promoting liver metastasis. siRNA-mediated knockdown reduced liver endothelial cell adhesion in vitro, and forced expression of AMIGO2 in low-AMIGO2 cells increased liver endothelial cell adhesion and liver metastasis in vivo. | PMID:28272394 | Scientific reports |
| 2019 | High | AMIGO2 functions as a homophilic cell-surface protein in the retina; starburst amacrine cells (SACs) and rod bipolar cells (RBCs) express AMIGO2, and Amigo2 knockout mice display expanded SAC and RBC dendrite arbors while other retinal neuron arbors remain unchanged. Increased SAC dendrite coverage was accompanied by increased direction selectivity of downstream direction-selective ganglion cells (DSGCs), identifying AMIGO2 as a cell-type-specific dendritic scaling factor. | PMID:31693896 | Cell reports |
| 2017 | Medium | AMIGO2 modulates T-cell functions: Amigo2 knockout impairs T-cell infiltration into secondary lymphoid organs and dampens Th-cell activation, while promoting splenic Th-cell proliferation. Mechanistically, AMIGO2 overexpression in 293T cells dampens NF-κB transcriptional activity, and AMIGO2 deficiency enhances Akt but suppresses GSK-3β phosphorylation and promotes nuclear translocation of NF-κB and NFAT1 in Th cells. Amigo2 KO mice exhibit ameliorated experimental autoimmune encephalomyelitis (EAE). | PMID:28119027 | Brain, behavior, and immunity |
| 2016 | Medium | IL-17A and TNF-α synergistically upregulate AMIGO2 expression in RA synoviocytes via an ERK-dependent mechanism (JNK inhibits AMIGO2 induction). Elevated AMIGO2 promotes cell survival and reduces apoptosis (cadmium-induced toxicity). HMGB1 in inflammatory conditions further increases AMIGO2 expression and reduces cell toxicity. | PMID:27446084 | Frontiers in immunology |
| 2022 | Medium | AMIGO2 contained in cancer cell-derived extracellular vesicles (EVs) is internalized by human hepatic sinusoidal endothelial cells (HHSECs) and, once inside, significantly enhances adhesion of HHSECs to cancer cells (including cells that themselves lack AMIGO2 expression), identifying a paracrine mechanism for liver metastasis initiation. | PMID:35039535 | Scientific reports |
| 2024 | Medium | METTL3-mediated m6A methylation in the 5'-UTR of AMIGO2 mRNA recruits the reader YTHDC2, stabilizing/upregulating AMIGO2 expression in RA fibroblast-like synoviocytes. METTL3 knockdown reduces m6A on AMIGO2 5'-UTR, decreases YTHDC2–AMIGO2 mRNA interaction, and lowers AMIGO2 protein, suppressing RA-FLS proliferation and migration; AMIGO2 overexpression rescues these phenotypes. | PMID:38432455 | Biochimica et biophysica acta. Molecular basis of disease |
| 2024 | Medium | In esophageal squamous cell carcinoma, METTL3-mediated m6A modification in the 5'-UTR of AMIGO2 pre-mRNA is read by YTHDC1, which regulates AMIGO2 splicing. METTL3 knockdown reduces m6A on AMIGO2 pre-mRNA, impairs YTHDC1-mediated splicing, and decreases AMIGO2 expression, suppressing ESCC proliferation and migration; AMIGO2 overexpression rescues these effects. | PMID:38360124 | Gene |
| 2018 | Medium | AMIGO2 deficiency in mice (KO) causes increased cardiomyocyte apoptosis, reduced proliferation, and reduced angiogenesis after myocardial infarction, with weaker cardiac function and larger infarct scar. Molecularly, AMIGO2 KO increases active caspase-3 and decreases PDK1, p-Akt, Bcl-2/Bax, and VEGF expression, consistent with inactivation of the PDK1/Akt survival pathway in cardiomyocytes. | PMID:29718531 | Cardiology journal |
| 2023 | Medium | AMIGO2 suppresses innate cisplatin sensitivity in NSCLC by inhibiting cisplatin-induced activation of caspase-8, caspase-9, and caspase-3, thereby preventing GSDME cleavage and pyroptosis. AMIGO2 acts by stimulating the PDK1/Akt (T308) signaling axis. Alteration of AMIGO2 expression changed cisplatin-induced pyroptosis both in vitro and in vivo. | PMID:37438979 | Journal of cellular and molecular medicine |
| 2022 | Medium | AMIGO2 expression in human gastric and colorectal cancer cells is directly associated with their adhesion to human hepatic sinusoidal endothelial cells (HHSECs) in vitro. Constitutive AMIGO2 knockdown clones showed significantly attenuated adhesion to HHSECs and suppressed liver metastasis in nude mice following intrasplenic inoculation, validating the mouse findings in human cancer cells. | PMID:35843033 | Pathology, research and practice |
| 2024 | Medium | AMIGO2 promotes EMT in colorectal cancer cells via activation of the TGFβ/Smad signaling pathway. Treatment with TGFβ receptor inhibitor LY2109761 suppressed AMIGO2-induced EMT. In CRC tissue samples, AMIGO2 was found at the invasive front where it localizes to the nucleus and associates with EMT marker expression, suggesting nuclear translocation of AMIGO2 as a mechanism for inducing EMT. | PMID:39379686 | Cancer gene therapy |
| 2025 | Medium | AMIGO2-containing small extracellular vesicles (sEVs) from gastric cancer cells activate hepatic stellate cells (HSCs) via NF-κB nuclear translocation, inducing IL-8 secretion. The resulting IL-8-rich conditioned medium significantly enhances gastric cancer cell migration; neutralizing IL-8 with antibodies suppresses this migration, establishing an AMIGO2 sEV→HSC→IL-8→cancer cell migration axis in liver metastasis. | PMID:40155010 | Anticancer research |
| 2022 | Medium | AMIGO2 expression in cancer-associated fibroblasts (CAFs) of colorectal cancer is induced by TGF-β. Conditioned media from NAFs with AMIGO2 overexpression enhanced CRC tumor cell proliferation and migration; siRNA-mediated inhibition of AMIGO2 in CAFs attenuated these effects, showing AMIGO2 regulates paracrine tumorigenic secretomes in CAFs. | PMID:39523830 | The Journal of pathology |
| 2024 | Low | AMIGO2 knockdown in bladder cancer cells suppresses PPAR-γ expression; PPAR-γ overexpression rescues the proliferation and migration suppressed by AMIGO2 knockdown, placing PPAR-γ downstream of AMIGO2 in a signaling axis controlling bladder cancer cell growth. | PMID:38978149 | Hereditas |
| 2021 | Medium | AMIGO2 knockdown via CRISPR/Cas9 in high-grade serous ovarian cancer cells reduces sphere-forming potential, adhesion, and invasion in vitro, and significantly attenuates intraperitoneal metastasis in vivo. | PMID:33524500 | Cancer letters |
| 2022 | Medium | Adhesion molecule Amigo2 is selectively expressed in medial habenula neurons and mediates fasciculation of the fasciculus retroflexus. Amigo2 loss-of-function in mice causes defasciculation of medial habenular axons; gain-of-function generates a more condensed tract and rescues the KO phenotype. AMIGO2 does not alter the course of habenular fibers, only their fasciculation. | PMID:35727300 | Developmental dynamics |

## Citations

- PMID:15107827
- PMID:26553931
- PMID:27446084
- PMID:28119027
- PMID:28272394
- PMID:29149598
- PMID:29718531
- PMID:31693896
- PMID:33524500
- PMID:35039535
- PMID:35727300
- PMID:35843033
- PMID:37438979
- PMID:38360124
- PMID:38432455
- PMID:38978149
- PMID:39379686
- PMID:39523830
- PMID:40155010
