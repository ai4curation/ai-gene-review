---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANGPTL8
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q6UXH0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 32
citation_count: 32
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANGPTL8 (human)

## Current model (mechanistic narrative)

ANGPTL8 is a feeding-induced, secreted hepatokine/adipokine that controls the partitioning of postprandial triglycerides between storage and oxidative tissues by regulating lipoprotein lipase (LPL) activity [PMID:24043787, PMID:32730227]. ANGPTL8 has no intrinsic LPL-inhibitory activity on its own; it must physically bind ANGPTL3 to form the active inhibitory complex, which dramatically enhances ANGPTL3's ability to bind and inhibit LPL while reciprocally increasing ANGPTL8 secretion, with the inhibitory motif residing in the ANGPTL8 N-terminus [PMID:28413163, PMID:29031715]. Hepatic ANGPTL8, acting with ANGPTL3, suppresses intravascular LPL in oxidative tissues such as heart and skeletal muscle in an endocrine manner, while adipose ANGPTL8 enhances local LPL activity by inhibiting ANGPTL4, together routing dietary fat toward adipose storage [PMID:32730227, PMID:26687026]; human genetic mimicry indicates the ANGPTL3–ANGPTL8 complex also inhibits endothelial lipase [PMID:36372100]. In adipocytes, ANGPTL8 promotes adipogenic differentiation and lipid accumulation and restrains intracellular lipolysis [PMID:28528274, PMID:38272177], and an autocrine/paracrine adipocyte pool influences glucose tolerance, adipose inflammation, and energy expenditure [PMID:39640567]. Clean knockout and overexpression studies establish that ANGPTL8 is not required for glucose homeostasis or beta-cell proliferation [PMID:24043787, PMID:25417115, PMID:27410263]. Independent of its lipase-regulating role, intracellular ANGPTL8 self-oligomerizes via its N-terminal domain and, together with p62/SQSTM1, targets IKKγ (NEMO) for selective autophagic degradation, providing negative feedback on TNFα-induced NF-κB inflammatory signaling [PMID:29255244]. Secreted ANGPTL8 also signals through the paired Ig-like receptors PirB/LILRB2/LILRB3 to reset the hepatic circadian clock, restrain pathological cardiac hypertrophy via Akt/GSK-3β, drive hepatic stellate cell activation and liver fibrosis, and damage neuronal synaptic integrity in diabetic conditions [PMID:31388006, PMID:35851270, PMID:36031141, PMID:39095838]. ANGPTL8 expression is transcriptionally activated by HNF-1α and HNF-4α and induced by insulin/feeding signals, and is suppressed by AMPK, repressive chromatin via ZNF638/HDAC1, and the microRNAs miR-221-3p and miR-143-3p [PMID:32561878, PMID:35325025, PMID:32154742, PMID:26254015, PMID:38211696, PMID:28938482, PMID:30261196].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005576 extracellular region, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-9612973 Autophagy
- **partners:** ANGPTL3, ANGPTL4, SQSTM1, IKBKG, LILRB2, LILRB3, PIRB, SREBF1
- **complexes:** ANGPTL3-ANGPTL8 complex, ANGPTL8-p62/SQSTM1 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | ANGPTL8 knockout mice show reduced VLDL secretion and increased lipoprotein lipase (LPL) activity in the fed state, demonstrating that ANGPTL8 is required for directing fatty acids to adipose tissue for storage during the fasting-to-refeeding transition. Despite increased LPL activity, TG uptake is selectively reduced in adipose tissue but preserved in heart, indicating tissue-specific action. | PMID:24043787 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | High | Angptl8 knockout mice show no alterations in glucose homeostasis on chow or high-fat diet, indicating ANGPTL8 is not required for glucose metabolism, contradicting earlier claims of a role in insulin secretion. | PMID:24043787, PMID:25417115 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | High | ANGPTL8 requires ANGPTL3 to inhibit LPL and raise plasma triglycerides; ANGPTL8 alone is inactive despite possessing a functional LPL inhibitory motif. Coexpression of ANGPTL3 and ANGPTL8 produces a far more efficacious increase in plasma TG than ANGPTL3 alone. An antibody to the C-terminus of ANGPTL8 reversed LPL inhibition without disrupting the ANGPTL8:ANGPTL3 complex, placing the inhibitory motif in the N-terminus of ANGPTL8. | PMID:28413163 | Journal of lipid research |
| 2017 | High | ANGPTL8 physically binds ANGPTL3 (co-IP, NanoBiT split-luciferase), and this complex dramatically increases ANGPTL3's ability to bind and inhibit LPL compared to either protein alone. Co-expression with ANGPTL3 also greatly enhances secretion of ANGPTL8. | PMID:29031715 | Molecular metabolism |
| 2017 | High | Intracellular ANGPTL8 functions as a negative feedback regulator of TNFα-induced NF-κB activation by facilitating selective autophagic degradation of IKKγ (NEMO). Mechanistically, ANGPTL8 self-oligomerizes via its N-terminal domain, forms a complex with p62/SQSTM1, and the resulting ANGPTL8-p62 platform recruits IKKγ for autophagic degradation. N-terminal self-oligomerization is essential for this function. | PMID:29255244 | Nature communications |
| 2020 | High | Hepatic ANGPTL8 (acting with ANGPTL3) inhibits intravascular LPL in oxidative tissues in an endocrine fashion to reduce dietary TG delivery, while adipose-tissue ANGPTL8 enhances local LPL activity by autocrine/paracrine inhibition of ANGPTL4. These combined actions coordinate postprandial TG partitioning. | PMID:32730227 | JCI insight |
| 2019 | Medium | ANGPTL8 resets diurnal rhythms of hepatic clock and metabolic genes in mice by signaling through the membrane receptor PirB (paired Ig-like receptor B), inducing phosphorylation of kinases and transcription factors and transiently activating the core clock gene Per1. Inhibition of ANGPTL8 signaling partially blocks food-entrained resetting of the liver clock. | PMID:31388006 | Nature communications |
| 2018 | Medium | HCC-associated protein TD26 (ANGPTL8) interacts via its C-terminus (aa 121–198) with the truncated nuclear form of SREBP1 (nSREBP1), not full-length SREBP1, blocking AMPK-mediated inhibition of SREBP1 activity, resulting in increased lipogenesis and tumor cell proliferation. | PMID:29663480 | Hepatology (Baltimore, Md.) |
| 2015 | Medium | ANGPTL8 (Lipasin) suppresses LPL activity specifically in cardiac and skeletal muscles (not white adipose tissue) postprandially, as shown by elevated postprandial cardiac and skeletal muscle LPL activity in lipasin-deficient mice. A monoclonal antibody targeting the epitope EIQVEE in ANGPTL8 lowered serum triglycerides by increasing postprandial cardiac LPL activity. | PMID:26687026 | Scientific reports |
| 2014 | High | ANGPTL8 overexpression in mouse liver doubles plasma triglycerides but does not induce beta cell expansion or alter glucose metabolism. Angptl8 knockout mice undergo entirely normal beta cell expansion in response to insulin resistance (high-fat diet or S961 insulin receptor antagonist), establishing that ANGPTL8 does not control pancreatic beta cell proliferation. | PMID:25417115, PMID:27410263 | Cell |
| 2020 | Medium | ANGPTL8 overexpression enhances insulin-stimulated AKT phosphorylation (improving insulin sensitivity) via the PI3K/AKT signaling pathway in mouse primary hepatocytes and in vivo. Site-directed mutagenesis identified Ser94 and Thr98 as key residues for ANGPTL8-mediated AKT activation. | PMID:32344005 | Gene |
| 2015 | Medium | AMPK activation (by AICAR or metformin) suppresses ANGPTL8 expression induced by the LXR/SREBP-1 signaling pathway in hepatocytes. SREBP-1c siRNA knockdown shows that AICAR's inhibitory effect on ANGPTL8 is most pronounced via SREBP-1, and PPARα phosphorylation by AMPK is also involved. | PMID:26254015 | Molecular and cellular endocrinology |
| 2020 | Medium | Insulin acutely increases Angptl8 expression in liver and adipose tissue via CCAAT/enhancer-binding protein β (C/EBPβ) transcription factor; glucose further enhances Angptl8 expression in adipose tissue in the presence of insulin. AMPK activation antagonizes the insulin effect on Angptl8 expression in hepatocytes and adipocytes. | PMID:32154742 | American journal of physiology. Endocrinology and metabolism |
| 2020 | High | Transcription factor HNF-1α directly binds the Angptl8 promoter (at -84/-68 bp) and is required for refeeding-induced increases in hepatic Angptl8 expression. HNF-1α expression increases after short-term refeeding in parallel with Angptl8 upregulation, and silencing HNF-1 abolishes insulin-induced Angptl8 expression in primary hepatocytes. | PMID:32561878 | Scientific reports |
| 2016 | Medium | Angptl8 knockdown in 3T3-L1 adipocytes reduces stored triglycerides and enhances intracellular lipolysis (increased NEFA release), and alters cellular phospholipid composition (reduced alkyl-PCs and PE plasmalogens). Angptl8 mRNA is suppressed by lipolysis-inducing agents (isoproterenol, forskolin), supporting its role as an insulin-regulated inhibitor of intracellular lipolysis in adipocytes. | PMID:28528274 | Chemistry and physics of lipids |
| 2016 | Medium | Hepatocyte nuclear factor-4α (HNF4α) binds the ANGPTL8 promoter and drives ANGPTL8 expression in hepatocytes. Sebacic acid (from royal jelly) reduces HNF4α protein levels and its binding to the ANGPTL8 promoter, thereby downregulating ANGPTL8 expression. | PMID:35325025 | Bioscience, biotechnology, and biochemistry |
| 2017 | Medium | miR-221-3p, induced by inflammatory stimuli (macrophage-conditioned medium/LPS) in adipocytes, targets the ANGPTL8 mRNA 3'UTR and reduces adipocyte ANGPTL8 protein expression, establishing miR-221-3p as a post-transcriptional regulator of ANGPTL8 under inflammatory conditions. | PMID:28938482 | The Journal of clinical endocrinology and metabolism |
| 2018 | Medium | miR-143-3p targets the ANGPTL8 3'UTR and downregulates ANGPTL8 transcript and protein in hepatocytes. Inhibition of miR-143-3p amplifies ANGPTL8 responses to hyperglycemic, hyperinsulinemic, and proinflammatory stimuli in HepG2 cells. | PMID:30261196 | Gene |
| 2022 | Medium | ANGPTL8 binds to the receptor LILRB2/PIRB and activates the ROS/ERK signaling pathway in hepatocytes, promoting autophagy and hepatocellular carcinoma cell proliferation. ANGPTL8-LILRB2/PIRB interaction also polarizes macrophages toward an immunosuppressive M2 phenotype and recruits immunosuppressive T cells. | PMID:37188659 | Oncogenesis |
| 2022 | Medium | ANGPTL8 acts as a negative regulator of pathological cardiac hypertrophy by binding to the paired Ig-like receptor LILRB3 (PIRB) and inhibiting Akt/GSK-3β activation in cardiomyocytes. Recombinant ANGPTL8 and ANGPTL8 overexpression attenuate Ang II-induced cardiomyocyte enlargement, and these effects are blocked by anti-LILRB3 antibody or LILRB3 siRNA. | PMID:35851270 | Cell death & disease |
| 2022 | Medium | Liver-derived ANGPTL8 activates hepatic stellate cells (HSCs) by interacting with the LILRB2 receptor to induce ERK signaling and increase expression of profibrotic genes, promoting NAFLD-associated liver fibrosis. | PMID:36031141 | Journal of advanced research |
| 2024 | Medium | ANGPTL8 is secreted by neurons into the hippocampus in diabetic mice, and acts through its receptor PirB in parallel on neurons and microglia: downregulating synaptic/axonal markers in neurons and upregulating proinflammatory cytokines in microglia. PirB knockout mice were resistant to ANGPTL8-induced neuroinflammation and synaptic damage. | PMID:39095838 | Journal of neuroinflammation |
| 2016 | Low | The ANGPTL8 R59W variant (rs2278426) is associated with increased levels of cleaved ANGPTL3 in plasma, suggesting this variant affects ANGPTL8-mediated activation/cleavage of ANGPTL3. | PMID:27117576 | Molecular genetics and metabolism |
| 2018 | Medium | GLP-1 receptor agonists (exendin-4, liraglutide) stimulate ANGPTL8 production in hepatocytes via the PI3K/Akt pathway in a GLP-1 receptor-dependent manner, as demonstrated by blockade with GLP-1R antagonist (exendin 9-39) and PI3K inhibitor (LY294002). | PMID:30003931 | Peptides |
| 2016 | Medium | Hepatic Angptl8 expression is rhythmically expressed, regulated by liver X receptor alpha (LXRα) during feeding and glucocorticoid receptor (GR) during fasting. Angptl8 mRNA is highly unstable, contributing to its daily oscillation. Intracellular (non-secreted) Angptl8 also regulates hepatic lipid homeostasis, as demonstrated by ectopic expression of a non-secreted Angptl8 mutant (Δ25-Angptl8). | PMID:27845381 | Scientific reports |
| 2022 | Medium | ANGPTL8 promotes the differentiation of mesenchymal stem cells (MSCs) into adipocytes by inhibiting the Wnt/β-Catenin pathway and upregulating PPARγ and C/EBPα expression. This effect is reversed by the Wnt/β-Catenin pathway activator LiCl and a GSK3β inhibitor (CHIR99021), establishing the mechanistic pathway. | PMID:36034432 | Frontiers in endocrinology |
| 2024 | Medium | ANGPTL8 knockout in adipose tissue (AT-A8-KO) in mice on a high-fat high-fructose diet improves glucose tolerance, insulin-stimulated glucose uptake in adipose tissue, reduces visceral adipose inflammation (crown-like structures, MCP-1, leptin), and increases energy expenditure, establishing an autocrine/paracrine role of adipocyte ANGPTL8 in glucose and energy homeostasis. | PMID:39640567 | iScience |
| 2024 | Medium | ANGPTL8 deficiency in septic mice activates the PGC1α/PPARα pathway, reduces hepatic lipid accumulation and lipid peroxidation, improves fatty acid oxidation, and increases survival. LPS-induced ANGPTL8 expression is dependent on TNF-α signaling. | PMID:39019343 | Journal of lipid research |
| 2022 | Medium | Human genetic mimicry analysis shows that the ANGPTL3-ANGPTL8 complex inhibits both LPL and endothelial lipase (EL/LIPG) in humans. The ANGPTL8 R59W substitution shows higher concordance with EL activity changes than LPL activity, while a rare protein-truncating ANGPTL8 variant shows LPL-specific effects, indicating the complex has both LPL and EL as substrates. | PMID:36372100 | Journal of lipid research |
| 2024 | Medium | ANGPTL8 knockdown in mouse subcutaneous preadipocytes reduces adipogenic differentiation, cellular TG accumulation, and isoproterenol-stimulated lipolysis. RNA-seq shows ANGPTL8 KD impedes early expression of adipogenic and insulin signaling genes including PPARγ, and reduces insulin-mediated Akt phosphorylation at early stages of differentiation. | PMID:38272177 | Biochimica et biophysica acta. Molecular and cell biology of lipids |
| 2024 | Medium | ZNF638 acts as a transcriptional repressor of ANGPTL8 in adipose tissue by recruiting HDAC1 for histone deacetylation at the Angptl8 locus. ZNF638 adipose-specific KO increases ANGPTL8 in female mice and causes refeeding-induced TG elevation, which is abolished by neutralizing circulating ANGPTL8, establishing ZNF638-ANGPTL8 as an estrogen-dependent axis regulating postprandial TG metabolism. | PMID:38211696 | Metabolism: clinical and experimental |
| 2023 | Low | The ANGPTL8 R59W variant is associated with increased circulating TNFα and IL-7 and increased NF-κB p65 activity. In vitro studies in HepG2 cells show enhanced phosphorylation of NF-κB pathway proteins and increased NF-κB luciferase reporter activity with the R59W variant, especially under TNFα stimulation. Structural modeling indicates the R59W change alters ANGPTL8's transient binding dynamics. | PMID:37947641 | Cells |

## Citations

- PMID:24043787
- PMID:25417115
- PMID:26254015
- PMID:26687026
- PMID:27117576
- PMID:27410263
- PMID:27845381
- PMID:28413163
- PMID:28528274
- PMID:28938482
- PMID:29031715
- PMID:29255244
- PMID:29663480
- PMID:30003931
- PMID:30261196
- PMID:31388006
- PMID:32154742
- PMID:32344005
- PMID:32561878
- PMID:32730227
- PMID:35325025
- PMID:35851270
- PMID:36031141
- PMID:36034432
- PMID:36372100
- PMID:37188659
- PMID:37947641
- PMID:38211696
- PMID:38272177
- PMID:39019343
- PMID:39095838
- PMID:39640567
