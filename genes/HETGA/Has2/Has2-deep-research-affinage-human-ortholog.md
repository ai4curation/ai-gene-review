---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/HAS2
affinage_run_date: 2026-06-10T01:55:21
uniprot_accession: Q92819
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

# Affinage mechanistic annotation for HAS2 (human)

## Current model (mechanistic narrative)

HAS2 is a plasma membrane hyaluronan synthase whose synthesis of high-molecular-mass hyaluronan (HA) drives cell migration, epithelial-mesenchymal transition, matrix homeostasis, and developmental morphogenesis [PMID:14729574, PMID:23108409, PMID:27094859]. It assembles into functional homomeric complexes and heteromers with HAS1 and HAS3 through an N-terminal domain, with HAS1 co-expression dampening HAS2/HAS3-driven HA output [PMID:25795779], and exhibits a lower UDP-GlcNAc requirement than HAS1 such that HAS2 activity scales with UDP-sugar availability [PMID:23303191]. Enzyme activity and trafficking are tightly controlled by post-translational modification: AMPK phosphorylation of Thr-110 is inhibitory and retains HAS2 in the ER, ubiquitination at K190 is required for HA synthesis and plasma membrane residence, and O-GlcNAcylation at Ser-221 is stimulatory, with these marks collectively governing ER-to-plasma-membrane transit [PMID:21228273, PMID:30394292]. HAS2 protein is additionally turned over by autophagy through a dynamic interaction with ATG9A [PMID:32084457]. The HAS2 gene is induced by TGFβ via Smad and p38 MAPK signaling [PMID:23108409], by NF-κB downstream of pro-inflammatory cytokines [PMID:20522558], and by transcription factors STAT3, SMAD4, ZEB1, FOXH1, and TCF7L2 [PMID:24847057, PMID:28086235, PMID:30282636, PMID:31489963, PMID:36358989], frequently acting in concert with its natural antisense transcript HAS2-AS1, which remodels chromatin at the HAS2 promoter [PMID:25183006]; it is repressed by AMPK and SIRT1 [PMID:21228273, PMID:31932306] and by microRNAs miR-23 and miR-26b that target the HAS2 transcript directly [PMID:21778427, PMID:26887530]. Functionally, HAS2-derived HA acts upstream of Rac1 to support lamellipodia and directed migration [PMID:14729574], promotes tumor invasion by suppressing TIMP-1 and sustaining FAK/PI3K/Akt signaling [PMID:22016393], drives EMT through a ZEB1-CD44 autocrine loop [PMID:28086235], and is essential in vivo for skeletal growth, chondrocyte maturation, synovial joint cavitation, aggrecan retention in cartilage, and cardiac endocardial cushion formation [PMID:19633173, PMID:27094859, PMID:21778427]. Dysregulated HAS2 expression—via upstream duplication, 3'UTR shortening, or m6A-dependent mRNA stabilization—causes pathological HA accumulation linked to canine periodic fever, pulmonary hypertension, and breast cancer progression [PMID:21437276, PMID:35671866, PMID:37705505], while sustained high-molecular-mass HA production confers anti-cancer and anti-inflammatory benefits [PMID:37612507].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016740 transferase activity
- **localization:** GO:0005886 plasma membrane, GO:0005794 Golgi apparatus, GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-1474244 Extracellular matrix organization, R-HSA-1266738 Developmental Biology, R-HSA-1643685 Disease
- **partners:** HAS1, HAS3, ATG9A
- **complexes:** HAS2 homomer, HAS2-HAS1 heteromer, HAS2-HAS3 heteromer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | Medium | HAS2 overexpression in human HT1080 cells directly increases hyaluronan production and promotes anchorage-independent growth and tumorigenicity in nude mice, demonstrating that HA production by tumor cells per se drives cell proliferation in tissues. | PMID:10070975 | Cancer Research |
| 2002 | Medium | HAS2-driven hyaluronan synthesis (rather than abundance of pericellular hyaluronan per se) controls keratinocyte migration and lamellipodia formation; HAS2-antisense cells show delayed S-phase entry, smaller lamellipodia, and increased vinculin-containing adhesion plaques. | PMID:12186949 | Journal of Cell Science |
| 2004 | High | Zebrafish Has2 is required upstream of Rac1 for lamellipodia formation and dorsal migration of lateral cells during gastrulation; epistasis analyses with constitutively active and dominant-negative Rac1 place Has2 upstream of Rac1 activation, and the effect is cell-autonomous. | PMID:14729574 | Development |
| 2004 | Medium | Vasodilatory prostaglandins (prostacyclin analogue iloprost, PGE2) upregulate HAS2 mRNA and HA synthesis in human arterial smooth muscle cells via EP2 and IP receptors and cAMP signaling; COX-2 activity is required for basal HAS2 expression; HAS2-specific siRNA knockdown abolishes iloprost-stimulated HA secretion and promotes cell spreading. | PMID:14752026 | Circulation Research |
| 2009 | High | Conditional inactivation of Has2 in limb bud mesoderm severely shortens skeletal elements, disrupts growth plate organization, reduces aggrecan deposition, decreases hypertrophic chondrocyte number, prevents secondary ossification center formation, and abolishes synovial joint cavity formation, demonstrating essential roles for HA in skeletal growth, patterning, chondrocyte maturation, and joint formation. | PMID:19633173 | Development |
| 2010 | Medium | Proinflammatory cytokines (IL-1β, TNF-α, TNF-β) induce HA synthesis and monocyte adhesion in human endothelial cells specifically through HAS2 via the NF-κB signaling pathway; HAS2-specific siRNA knockdown abolishes cytokine-induced HA synthesis and monocyte adhesion. | PMID:20522558 | Journal of Biological Chemistry |
| 2011 | High | AMPK phosphorylates Thr-110 of human HAS2, directly inhibiting its enzymatic activity and reducing HA synthesis; the other two HAS isoenzymes (HAS1 and HAS3) are not modified by AMPK. This inhibition reduces AoSMC proliferation, migration, and immune cell recruitment. | PMID:21228273 | Journal of Biological Chemistry |
| 2011 | High | HAS2 knockdown in a bone-metastatic MDA-MB-231 clone completely suppresses invasion through induction of TIMP-1 and dephosphorylation of focal adhesion kinase; HAS2 also supports EGF-mediated FAK/PI3K/Akt signaling. Rescue by HAS2 re-expression, TIMP-1 siRNA, or TIMP-1-blocking antibodies confirms the pathway. | PMID:22016393 | Journal of Biological Chemistry |
| 2011 | High | miR-23 directly targets Has2 (and Icat, Tmem2) to restrict endocardial cushion formation in zebrafish; Has2 upregulation is responsible for excessive endocardial cushion cell differentiation in dicer mutants; miR-23 also inhibits TGF-β-induced endothelial-to-mesenchymal transition in mouse endothelial cells by suppressing Has2. | PMID:21778427 | Circulation Research |
| 2011 | Medium | A novel unstable duplication upstream of HAS2 in Shar-Pei dogs increases HAS2 expression, leading to HA accumulation in skin (thick folded skin phenotype) and a periodic fever syndrome; higher copy number of the 16.1 kb duplication is associated with both increased HAS2 expression and fever syndrome. | PMID:21437276 | PLoS Genetics |
| 2012 | High | TGFβ potently stimulates HA synthesis via upregulation of HAS2 in NMuMG mammary epithelial cells through kinase-active type I TGFβ receptor, Smad signaling, and p38 MAPK activation; HAS2 knockdown inhibits TGFβ-induced EMT (~50% reduction), suppresses EMT markers (fibronectin, Snail1, Zeb1), and completely abolishes TGFβ-induced cell migration; extracellular HA or CD44 blocking are not required. | PMID:23108409 | Oncogene |
| 2013 | Medium | HAS2 requires lower cellular UDP-GlcNAc concentration than HAS1 to synthesize hyaluronan; HAS2 activity increases with UDP-sugar availability; transfected HAS2 consumes enough UDP-sugars to reduce their cellular content. These differences define distinct kinetic properties among the three HAS isoenzymes. | PMID:23303191 | Journal of Biological Chemistry |
| 2014 | Medium | O-GlcNAcylation (induced by glucosamine or PUGNAC) specifically increases HAS2 mRNA among the three HAS isoenzymes; the natural antisense transcript HAS2-AS1 is absolutely required for this O-GlcNAcylation-induced HAS2 transcription; O-GlcNAcylation recruits NF-κB subunit p65 to the HAS2-AS1 promoter, and HAS2-AS1 then regulates HAS2 transcription in cis by altering chromatin structure (O-GlcNAcylation and acetylation) around the HAS2 proximal promoter. | PMID:25183006 | Journal of Biological Chemistry |
| 2014 | High | STAT3 phosphorylated at Tyr705 (via JAK2 and ERK1/2 activation downstream of P2Y14 receptor stimulation by UDP-glucose) directly binds to the HAS2 promoter and induces HAS2 transcription in keratinocytes; chromatin immunoprecipitation confirmed increased Tyr705-STAT3 promoter binding at the time of HAS2 induction. | PMID:24847057 | Journal of Biological Chemistry |
| 2015 | High | HAS2 forms functionally relevant homomeric and heteromeric complexes with HAS1 and HAS3; complexes exist in both Golgi and plasma membrane; interaction is mediated mainly via the N-terminal 86-amino acid domain; HAS1 co-transfection reduces HAS2/HAS3-driven HA synthesis, indicating functional cooperation. HAS2 immunoprecipitates contain functional HAS2 homomers and heteromers with HAS3. | PMID:25795779 | Journal of Biological Chemistry |
| 2016 | High | CRISPR/Cas9 knockout of HAS2 in rat chondrosarcoma chondrocytes abolishes the pericellular HA matrix and completely prevents aggrecan retention; restoration of HAS2 by adenoviral transduction rescues pericellular matrix and aggrecan binding, demonstrating that HA produced by HAS2 is essential for aggrecan retention. | PMID:27094859 | Matrix Biology |
| 2018 | High | Post-translational modifications control HAS2 trafficking and activity: ubiquitination (K190R mutation) blocks HA synthesis and reduces enzyme degradation while increasing plasma membrane residence; phosphorylation site (T110A) retains HAS2 in ER, blocks PM trafficking, and abolishes HA synthesis; O-GlcNAcylation (S221A) reduces HA synthesis; S221 phosphomimetics (S221D/E) block synthesis and accelerate decay, indicating alternative regulation by O-GlcNAc versus phosphorylation. | PMID:30394292 | Matrix Biology |
| 2018 | Medium | ZEB1 directly activates HAS2 expression, and HAS2-derived HA in turn elevates ZEB1 via CD44s, forming a positive autocrine feedback loop that promotes EMT and breast cancer metastasis. | PMID:28086235 | Oncotarget |
| 2018 | Medium | TGFβ induces Has2, Has2as (antisense), and Hmga2 expression via Smad and non-Smad pathways in mouse mammary epithelial cells; Has2as abrogation suppresses TGFβ-induced EMT markers (Snai1, Hmga2, Fn1) and mesenchymal phenotype; CD44, but not Hmmr, is required for TGFβ-mediated EMT phenotype; Akt and Erk1/2 activation is required for Has2as/Has2 induction and cell motility. | PMID:30194979 | Matrix Biology |
| 2018 | Medium | Activin/Smad2 and Wnt/β-catenin signals cooperate via FOXH1 on open chromatin (following EZH2-PRC2 eviction) to activate HAS2 expression during mesendoderm differentiation of human ESCs; HAS2 knockdown greatly attenuates mesendoderm differentiation. | PMID:30282636 | Journal of Biological Chemistry |
| 2019 | Medium | HAS2 overexpression in chondrocytes inhibits MMP3, MMP13, TSG6, and other procatabolic markers and enhances aggrecan retention; however, this inhibitory effect occurs only in HAS2-transduced cells (not in adjacent non-transduced cells), indicating an intracellular mechanism independent of extracellular HA. | PMID:31270213 | Journal of Biological Chemistry |
| 2019 | Medium | SMAD4 directly binds to the HAS2 promoter to induce HAS2 expression and HA secretion in porcine granulosa cells; the downstream CD44-Caspase3 axis is activated by SMAD4 through this HAS2-HA system; miR-26b attenuates HAS2 expression via SMAD4-dependent and -independent mechanisms. | PMID:31489963 | Journal of Cellular Physiology |
| 2020 | Medium | SIRT1 activation reduces HAS2 expression and HA accumulation in aortic smooth muscle cells by preventing nuclear translocation of NF-κB (p65), which reduces HAS2-AS1 levels, and HAS2-AS1 epigenetically controls HAS2 mRNA expression; SIRT1 also reduces RHAMM and TSG6 expression to inhibit HA-mediated monocyte adhesion and cell migration. | PMID:31932306 | Journal of Biological Chemistry |
| 2020 | Medium | HAS2 is degraded in vascular endothelial cells via autophagy (evoked by nutrient deprivation, mTOR inhibition, or proteoglycan fragments endorepellin/endostatin); live-cell and super-resolution microscopy reveal dynamic interaction between HAS2 and ATG9A during autophagic degradation; inhibiting autophagic flux with chloroquine increases HAS2 levels in heart and aorta in vivo; autophagic induction suppresses HA production and inhibits angiogenic sprouting. | PMID:32084457 | Matrix Biology |
| 2022 | High | 3'UTR shortening of HAS2 (caused by depletion of NUDT21, a master regulator of alternative polyadenylation) leads to HAS2 hyper-expression in pulmonary artery smooth muscle cells, driving HA hyper-synthesis, bioenergetic dysfunction (impaired mitochondrial oxidative capacity and glycolytic shift), and pro-remodeling phenotypes; transgenic mice mimicking HAS2 hyper-synthesis in smooth muscle cells develop spontaneous pulmonary hypertension; targeted HAS2 deletion prevents experimental PH. | PMID:35671866 | Matrix Biology |
| 2023 | Medium | KIAA1429/VIRMA (a component of the m6A methyltransferase complex) binds to m6A-reader IGF2BP3, leading to stabilization of m6A-modified HAS2 mRNA in the cytosol of breast cancer cells; VIRMA knockdown inhibits breast cancer cell proliferation, migration, and invasion. | PMID:37705505 | EMBO Reports |
| 2023 | High | Transgenic mice overexpressing naked mole-rat Has2 (nmrHas2) show increased high-molecular-mass hyaluronan in several tissues, reduced spontaneous and induced cancer incidence, extended lifespan, and attenuated multi-tissue inflammation; these beneficial effects are conferred by HMM-HA and are not specific to the nmrHas2 gene sequence, as they can be recapitulated by exogenous HMM-HA. | PMID:37612507 | Nature |
| 2011 | Medium | Nephronectin acts as an upstream regulator of Bmp4-Has2 signaling in zebrafish AV canal differentiation; inhibition of has2 in npnt morphants rescues the endocardial (but not myocardial) expansion, placing Has2 downstream of Bmp4 and upstream of endocardial AV cell fate specification. | PMID:21937601 | Development |
| 2016 | Medium | miR-26b directly binds the 3'UTR of HAS2 mRNA (confirmed by luciferase reporter assay) and negatively regulates HAS2 expression and HA synthesis in porcine granulosa cells; reduced HAS2 via miR-26b promotes granulosa cell apoptosis through the HAS2-HA-CD44-Caspase3 pathway. | PMID:26887530 | Scientific Reports |
| 2018 | Medium | Extracellular ATP activates HAS2 expression in keratinocytes via P2Y2 receptor → Ca2+/calmodulin-dependent protein kinase II, PKC, MAPK, and CREB-dependent pathways; AMP and adenosine (ATP degradation products) inhibit HAS2 expression, providing a feedback mechanism to shut off HA production. | PMID:29626161 | Biochemical Journal |
| 2025 | Medium | Fibroblast-derived Has2 (deleted by fibroblast-specific Cre) limits acute heart failure following myocardial infarction in male mice; Has2-deficient male mice show exacerbated heart failure (lower cardiac output, stroke volume) at 1 week post-MI without changes in fibrosis, cardiomyocyte size, or capillary density; sex-specific effect not evident in females. | PMID:41250926 | Physiological Reports |
| 2022 | Medium | FGF9 promotes HAS2 expression in palatal mesenchyme via the Wnt/β-catenin/TCF7L2 pathway; TCF7L2 binds the HAS2 promoter and activates its transcription; Fgf9 knockout reduces TCF7L2 and HAS2, and TCF-dependent agonist-induced HA expression is blocked in Fgf9-null palate due to TCF7L2 loss. | PMID:36358989 | Biomolecules |

## Citations

- PMID:10070975
- PMID:12186949
- PMID:14729574
- PMID:14752026
- PMID:19633173
- PMID:20522558
- PMID:21228273
- PMID:21437276
- PMID:21778427
- PMID:21937601
- PMID:22016393
- PMID:23108409
- PMID:23303191
- PMID:24847057
- PMID:25183006
- PMID:25795779
- PMID:26887530
- PMID:27094859
- PMID:28086235
- PMID:29626161
- PMID:30194979
- PMID:30282636
- PMID:30394292
- PMID:31270213
- PMID:31489963
- PMID:31932306
- PMID:32084457
- PMID:35671866
- PMID:36358989
- PMID:37612507
- PMID:37705505
- PMID:41250926
