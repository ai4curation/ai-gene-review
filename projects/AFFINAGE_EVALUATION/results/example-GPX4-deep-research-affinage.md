---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/GPX4
affinage_run_date: 2026-06-10T01:55:21
uniprot_accession: P36969
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 37
citation_count: 37
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for GPX4 (human)

## Current model (mechanistic narrative)

GPX4 is a selenocysteine-dependent glutathione peroxidase that constitutes the central cellular defense against iron-dependent lipid peroxidation, and its loss precipitates ferroptotic cell death [PMID:24439385, PMID:31634900]. It is uniquely capable of reducing esterified phospholipid hydroperoxides within membranes to non-toxic lipid alcohols, a reaction no other enzyme performs in a cellular context [PMID:31634900, PMID:34931062]; an electrostatic cationic patch mediates membrane and cardiolipin binding adjacent to the catalytic site [PMID:34492183], and the selenolate active-site catalysis is specifically required to resist irreversible overoxidation, distinguishing GPX4 from a cysteine variant and being essential for neuronal survival in vivo [PMID:29290465]. This antioxidant function makes GPX4 a survival dependency in therapy-resistant high-mesenchymal persister cancer cells [PMID:29088702], and a patient-derived R152H active-site loop mutation that abolishes activity links GPX4 dysfunction to human disease [PMID:34931062]. Beyond its canonical hydroperoxidase role, GPX4 acts as a protein-thiol peroxidase that cross-links mitochondrial capsule proteins during spermatogenesis [PMID:11568459], and alternative-promoter usage generates cytosolic, mitochondrial, and arginine-rich nuclear isoforms with distinct localizations [PMID:12751792, PMID:14583338]. GPX4 abundance is set by a dense post-translational network: stabilizing palmitoylation at C66/C75 (ZDHHC20/ZDHHC8, reversed by APT2) [PMID:39833225, PMID:40108413], R152 symmetric dimethylation by PRMT5 that excludes the Cullin1-FBW7 ligase [PMID:40033101], S104 phosphorylation by CKB that blocks chaperone-mediated autophagy [PMID:37156912], stabilizing deubiquitination (USP8, OTUD5, OTUB1 recruited by CST1) and linear ubiquitination by LUBAC [PMID:36369321, PMID:36279464, PMID:38598341, PMID:38110369], opposed by degradative ubiquitination (STUB1 at K191, NEDD4L, copper-induced modification of C107/C148) and selective/chaperone-mediated autophagy via TAX1BP1, p62/TRAF6, legumain-HSC70, and FUNDC1-mediated mitochondrial import [PMID:36622894, PMID:38110356, PMID:33431801, PMID:36828120, PMID:40394165], with transcriptional and m6A control by STAT3 and the PKA-ALKBH5 axis [PMID:35859150, PMID:39901038]. Functionally, GPX4-maintained redox homeostasis sustains follicular helper T cell and germinal center responses [PMID:34413521], enables cGAS-STING innate immunity by preventing lipid-peroxidation-driven STING carbonylation at C88 [PMID:32541831], confers host resistance to Mycobacterium tuberculosis [PMID:36069923], and in adipocytes suppresses metabolic inflammation independently of overt ferroptotic death [PMID:35031697]. Direct covalent modification of C66 by itaconate allosterically activates the enzyme to protect neurons [PMID:38719928].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016491 oxidoreductase activity, GO:0140098 catalytic activity, acting on RNA, GO:0008289 lipid binding, GO:0003677 DNA binding, GO:0016209 antioxidant activity
- **localization:** GO:0005829 cytosol, GO:0005739 mitochondrion, GO:0005634 nucleus, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-5357801 Programmed Cell Death, R-HSA-8953897 Cellular responses to stimuli, R-HSA-168256 Immune System, R-HSA-392499 Metabolism of proteins, R-HSA-9612973 Autophagy
- **partners:** STING, CKB, PRMT5, ZDHHC20, USP8, OTUD5, STUB1, TRAF6
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | GPX4 is directly inhibited by a class of ferroptosis-inducing compounds (e.g., RSL3) identified via chemoproteomics; GPX4 overexpression suppresses and knockdown promotes ferroptotic cell death induced by 12 different ferroptosis inducers, establishing GPX4 as an essential regulator of ferroptosis. | PMID:24439385 | Cell |
| 2019 | High | GPX4 functions as the glutathione-dependent lipid hydroperoxidase that converts lipid hydroperoxides into non-toxic lipid alcohols, thereby suppressing ferroptosis; FSP1 acts in a parallel non-mitochondrial CoQ antioxidant pathway independent of GPX4. | PMID:31634900 | Nature |
| 2017 | High | Selenocysteine utilization by GPX4 confers exquisite resistance to irreversible overoxidation; cells expressing a cysteine variant of GPX4 (Sec→Cys) are highly sensitive to peroxide-induced ferroptosis, demonstrating that selenolate-based catalysis is specifically required for neuronal survival and prevention of fatal epileptic seizures in vivo. | PMID:29290465 | Cell |
| 2017 | High | Drug-tolerant persister cancer cells in a high mesenchymal therapy-resistant state acquire dependency on GPX4 for survival; loss of GPX4 function causes selective ferroptotic death of persister cells in vitro and prevents tumor relapse in mice. | PMID:29088702 | Nature |
| 2020 | High | GPX4 deficiency enhances cellular lipid peroxidation, which leads to carbonylation of STING at C88 and inhibits STING trafficking from the ER to the Golgi complex, thereby specifically attenuating the cGAS-STING innate immune pathway; GPX4-maintained redox homeostasis is required for STING activation. | PMID:32541831 | Nature immunology |
| 2001 | High | PHGPx (GPX4) acts as a protein thiol peroxidase in sperm, using its selenocysteine to oxidize specific capsule protein thiols via a peroxide-dependent mechanism, leading to cross-linking of mitochondrial capsule proteins and accounting for the selenium dependency of spermatogenesis. | PMID:11568459 | BioFactors (Oxford, England) |
| 2021 | High | GPX4 is the only enzyme capable of reducing esterified phospholipid hydroperoxides within a cellular context; a patient-derived R152H mutation destabilizes a critical loop adjacent to the active site, causing substantial loss of enzymatic function while paradoxically reducing GPX4 susceptibility to degradation. | PMID:34931062 | Nature chemical biology |
| 2022 | High | An allosteric site on GPX4 (distinct from the active site) is involved in native regeneration of GPX4 under low glutathione conditions; covalent binding of inhibitors to this site causes conformational change, inhibition of activity, and subsequent cellular GPX4 protein degradation. Co-crystal structures of six inhibitors bound in this site were determined. | PMID:36423641 | Cell chemical biology |
| 2021 | High | NMR characterization of GPX4 reveals an electrostatic (cationic patch) mechanism for membrane binding; mutagenesis identifies specific cationic patch residues required for membrane and cardiolipin headgroup binding, and a novel lipid binding site adjacent to the catalytic site. The cationic patch also mediates DNA binding, explaining the nuclear isoform's ability to target DNA-bound protamines. | PMID:34492183 | Biochemistry |
| 2003 | High | Testis-specific nuclear form of GPX4 (PHGPx/snGPx) is generated by transcription initiation from an alternative promoter (not by alternative splicing) located in intron 1, producing an arginine-rich N-terminus responsible for nuclear localization and chromatin binding, with expression restricted to late stages of spermatogenesis. | PMID:12751792 | Biological chemistry |
| 2023 | Medium | Copper promotes GPX4 autophagic degradation and ferroptosis by directly binding to GPX4 cysteines C107 and C148, inducing GPX4 ubiquitination and aggregation; TAX1BP1 then acts as the autophagic receptor mediating GPX4 degradation. | PMID:36622894 | Autophagy |
| 2023 | High | Creatine kinase B (CKB), when phosphorylated at T133 by AKT downstream of IGF1R signaling, acts as a non-canonical protein kinase to phosphorylate GPX4 at S104; this phosphorylation prevents HSC70 binding to GPX4 and blocks chaperone-mediated autophagy (CMA)-dependent GPX4 degradation, thereby suppressing ferroptosis. | PMID:37156912 | Nature cell biology |
| 2021 | Medium | Legumain facilitates chaperone-mediated autophagy (CMA) of GPX4 in acute kidney injury: legumain directly interacts with HSC70, HSP90, and GPX4 (shown by immunoprecipitation), and legumain deficiency prevents CMA-dependent GPX4 degradation and tubular ferroptosis. | PMID:33431801 | Cell death & disease |
| 2022 | Medium | CST1 interacts with GPX4 (confirmed by Co-IP and mass spectrometry) and recruits the deubiquitinase OTUB1 to relieve GPX4 ubiquitination, thereby stabilizing GPX4 protein and inhibiting ferroptosis. | PMID:36369321 | Oncogene |
| 2022 | Medium | LUBAC (via its catalytic subunit HOIP) binds GPX4 and stabilizes it through linear (M1-linked) ubiquitination both under basal conditions and oxidative stress; LUBAC deficiency promotes GPX4 degradation and sensitizes cells to ferroptosis. | PMID:36279464 | Proceedings of the National Academy of Sciences of the United States of America |
| 2023 | Medium | USP8 (ubiquitin-specific protease 8) directly interacts with and deubiquitinates GPX4, leading to GPX4 protein stabilization; USP8 inhibition destabilizes GPX4 and sensitizes cancer cells to ferroptosis. | PMID:38598341 | Proceedings of the National Academy of Sciences of the United States of America |
| 2023 | Medium | OTUD5 acts as a deubiquitinase that binds GPX4, stabilizes it, and confers ferroptosis resistance; during ischemia-reperfusion, mTORC1-mediated autophagy degrades OTUD5, causing GPX4 decay and subsequent ferroptosis in renal tubular cells. | PMID:38110369 | Nature communications |
| 2023 | Medium | TRIM26 directly interacts with GPX4 via its RING domain and catalyzes K63-linked ubiquitination of GPX4 at K107 and K117, switching polyubiquitination from K48 to K63 linkage and thereby enhancing GPX4 protein stability; PLK1-mediated S127 phosphorylation of TRIM26 enhances this interaction. | PMID:37872147 | Cell death & disease |
| 2025 | High | GPX4 is S-palmitoylated on cysteine 66 by the acyltransferase ZDHHC20, which increases GPX4 protein stability; APT2 acts as the depalmitoylase of GPX4. Disrupting GPX4 palmitoylation sensitizes cancer cells to ferroptosis in vitro and in vivo. | PMID:39833225 | Nature communications |
| 2025 | Medium | ZDHHC8 palmitoylates GPX4 at Cys75, stabilizing GPX4 and suppressing ferroptosis; pharmacological inhibition of ZDHHC8 with PF-670462 promotes ZDHHC8 degradation, reduces GPX4 palmitoylation, and enhances ferroptosis sensitivity in tumor cells. | PMID:40108413 | Nature cancer |
| 2025 | High | PRMT5 catalyzes symmetric dimethylation of GPX4 at arginine 152 (R152), which prevents Cullin1-FBW7 E3 ligase binding to GPX4 and blocks ubiquitination-mediated GPX4 degradation, thereby prolonging GPX4 half-life and suppressing ferroptosis. | PMID:40033101 | Nature cell biology |
| 2023 | Low | NEDD4L directly interacts with GPX4 (confirmed by Co-IP) and promotes GPX4 ubiquitination and degradation, facilitating granulosa cell ferroptosis and contributing to PCOS pathology. | PMID:36662677 | Endocrine connections |
| 2023 | Medium | STUB1 is identified as an E3 ubiquitin ligase of GPX4, promoting GPX4 ubiquitination at site K191 and its degradation, thereby inducing ferroptosis in gastrointestinal stromal tumors. | PMID:38110356 | Cell death & disease |
| 2024 | Medium | OTUD5 deubiquitylates and stabilizes GPX4; p53 suppresses OTUD5 transcription, thereby promoting GPX4 ubiquitination and degradation and inducing ferroptosis in gastric cancer cells. | PMID:40070026 | Clinical and translational medicine |
| 2026 | Medium | FUNDC1 interacts with GPX4 via its 96–133 amino acid domain (shown by Co-IP), facilitating GPX4 recruitment from cytoplasm into mitochondria via the TOM/TIM import complex; within mitochondria, GPX4 is degraded by mitophagy, triggering hepatocyte ferroptosis. | PMID:36828120 | Journal of advanced research |
| 2023 | Medium | STAT3 binds to the GPX4 promoter region and promotes its transcription (confirmed by ChIP and dual-luciferase reporter assay); thiostrepton blocks GPX4 expression by inhibiting STAT3, thereby inducing ferroptosis in pancreatic cancer cells. | PMID:35859150 | Cell death & disease |
| 2024 | High | Itaconate (produced by Irg1/aconitate decarboxylase 1) directly alkylates GPX4 at cysteine 66, allosterically enhancing GPX4 enzymatic activity, thereby protecting neurons from ferroptosis after intracerebral hemorrhage. | PMID:38719928 | Cell death and differentiation |
| 1997 | Medium | PHGPx (GPX4) shares an active site catalytic triad (selenocysteine, glutamine, tryptophan) with tetrameric GPXs; its unique ability to accommodate large lipophilic substrates (phospholipid hydroperoxides) is defined by structural and kinetic data. PHGPx also exhibits broad donor-substrate specificity (not restricted to GSH) and binds specific mitochondrial proteins via protein-protein interaction, suggesting a role in oxidizing specific protein thiols. | PMID:9315326 | Biomedical and environmental sciences : BES |
| 2003 | Medium | Overexpression of mitochondrial PHGPx (mPHGPx) in neonatal rat cardiac myocytes reduces lipid peroxidation (malondialdehyde/HNE), decreases cytochrome c release from mitochondria, and preserves electron transport chain complex IV function following simulated ischemia/reoxygenation, demonstrating a direct mitochondrial protective role. | PMID:14583338 | Free radical biology & medicine |
| 2021 | High | GPX4 is required for follicular helper T (TFH) cell survival; selective deletion of GPX4 in T cells abrogates TFH cells and germinal center responses in immunized mice, establishing the selenium-GPX4-ferroptosis axis as a critical regulator of TFH homeostasis. | PMID:34413521 | Nature immunology |
| 2022 | High | GPX4 deficiency in macrophages and lung tissue results in ferroptotic cell death during Mycobacterium tuberculosis infection; Gpx4-deficient mice show increased lung necrosis and bacterial burden while Gpx4-overexpressing transgenic mice show decreased necrosis, establishing the GPX4/GSH axis as a host-resistance determinant in TB. | PMID:36069923 | The Journal of experimental medicine |
| 2022 | High | Adipocyte-specific GPX4 knockout spontaneously causes adipocyte hypertrophy, lipid peroxidation, inflammatory cytokine expression (TNF-α, IL-1β, IL-6, CXCL1), macrophage infiltration, glucose intolerance, and hepatic insulin resistance independent of ferroptosis-associated cell death. | PMID:35031697 | International journal of obesity (2005) |
| 2024 | Medium | PKA phosphorylates and promotes degradation of ALKBH5 (an m6A demethylase), thereby increasing m6A modification and stability of GPX4 mRNA; ALKBH5 deletion maintains GPX4 m6A modification and suppresses ferroptotic cell death, establishing a PKA-ALKBH5-GPX4 m6A regulatory axis. | PMID:39901038 | Cell death and differentiation |
| 2023 | Medium | RSL3 and ML162 (commonly used GPX4 inhibitors) completely lack capacity to inhibit recombinant selenoprotein GPX4 enzymatic activity in vitro; instead, they are efficient inhibitors of TXNRD1. This negative result suggests prior mechanistic studies attributing ferroptosis induction by these compounds solely to GPX4 inhibition need re-evaluation. | PMID:37087975 | Redox biology |
| 2025 | Medium | TRAF6 ubiquitinates GPX4, promoting its recognition by the autophagic receptor p62 and selective autophagic degradation; a GPX4-targeted AUTAC exploiting this pathway induces GPX4 degradation and ferroptosis in breast cancer. | PMID:40394165 | Cell death and differentiation |
| 2001 | Medium | PHGPx (GPX4) was cloned as an anti-apoptotic and growth-promoting gene in Burkitt lymphoma cells, where cystine availability limiting glutathione biosynthesis determines cell susceptibility to oxidative stress-induced apoptosis, and PHGPx overexpression provides protection. | PMID:11568455 | BioFactors (Oxford, England) |
| 1997 | Medium | Co-transfection of both PHGPx cDNA and selenophosphate synthase (SelD) cDNA into endothelial cells produces significantly higher PHGPx activity than either alone, especially under selenium-limiting conditions, demonstrating that selenocysteine incorporation machinery (SelD) is rate-limiting for GPX4 expression and function. | PMID:9315307 | Biomedical and environmental sciences : BES |

## Citations

- PMID:11568455
- PMID:11568459
- PMID:12751792
- PMID:14583338
- PMID:24439385
- PMID:29088702
- PMID:29290465
- PMID:31634900
- PMID:32541831
- PMID:33431801
- PMID:34413521
- PMID:34492183
- PMID:34931062
- PMID:35031697
- PMID:35859150
- PMID:36069923
- PMID:36279464
- PMID:36369321
- PMID:36423641
- PMID:36622894
- PMID:36662677
- PMID:36828120
- PMID:37087975
- PMID:37156912
- PMID:37872147
- PMID:38110356
- PMID:38110369
- PMID:38598341
- PMID:38719928
- PMID:39833225
- PMID:39901038
- PMID:40033101
- PMID:40070026
- PMID:40108413
- PMID:40394165
- PMID:9315307
- PMID:9315326
