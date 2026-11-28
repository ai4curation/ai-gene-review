---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BANP
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N9N5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 43
citation_count: 43
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BANP (human)

## Current model (mechanistic narrative)

BANP (also known as SMAR1) is a BEN-domain transcription factor that binds unmethylated CGCG/T(C/G)-repeat motifs at CpG-island promoters and matrix/scaffold-attachment regions (MARs), where it organizes chromatin and controls gene expression [PMID:34234345, PMID:10950932, PMID:27671416]. Its DNA recognition is methylation-sensitive at the genomic level—DNA methylation of the motif repels binding and restricts occupancy to unmethylated CpG islands—and upon binding BANP opens chromatin, phases nucleosomes, and activates essential metabolic genes [PMID:34234345]. Structural work resolved the BEN domain bound to CGCG DNA, showing that oligomerization underlies its selectivity for unmethylated CGCG motifs [PMID:37086783, PMID:39225042]. At MAR elements BANP most often acts as a transcriptional repressor by recruiting HDAC1/mSin3A and related corepressor complexes to target promoters, silencing genes including cyclin D1, Slug, β-catenin, STAT3, hTERT, calnexin, PPARγ and the miR-371-373 cluster [PMID:16166625, PMID:25086032, PMID:29765542, PMID:27671416, PMID:34551340, PMID:31422285, PMID:34450266]. BANP is also a positive regulator of p53: it directly binds and stabilizes p53 by inhibiting MDM2-mediated degradation, then later forms a p53-MDM2-BANP ternary complex that recruits HDAC1 to deacetylate p53 and switch off the response during stress recovery [PMID:15701641, PMID:19303885, PMID:20075864]. Beyond transcription, BANP regulates alternative splicing by recruiting HDAC6 to deacetylate the RNA-binding proteins Sam68 and PTBP1, controlling CD44 and PKM splicing [PMID:26080397, PMID:33863392], and is required for the DNA-damage response and chromosome segregation, regulating direct targets such as wrnip1, cenpt and ncapg [PMID:35942692]. BANP protein levels are tightly governed by APC/C-Cdc20- and RBX1-mediated D-box-dependent ubiquitin-proteasomal degradation [PMID:28617439, PMID:29765542, PMID:36810109].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus, GO:0005654 nucleoplasm, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-73894 DNA Repair, R-HSA-8953854 Metabolism of RNA, R-HSA-5357801 Programmed Cell Death, R-HSA-392499 Metabolism of proteins
- **partners:** TP53, MDM2, HDAC1, HDAC6, CDC20, RBX1, P300, CUX1
- **complexes:** HDAC1/mSin3A corepressor complex, p53-MDM2-SMAR1 ternary complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | BANP (SMAR1) is the transcription factor that binds the CGCG element (Banp motif) at CpG island promoters in mouse and human genomes, identified by combining single-molecule footprinting with interaction proteomics. BANP binding is repelled by DNA methylation of its motif in vitro and in vivo, restricting binding to unmethylated CGIs. Upon binding, BANP opens chromatin and phases nucleosomes, activating essential metabolic genes in pluripotent stem and neuronal cells. | PMID:34234345 | Nature |
| 2023 | High | Crystal structures of the BANP BEN domain in apo form and in complex with CGCG-containing DNA revealed that the BEN domain uses primarily electrostatic interactions to bind DNA with some base-specific interactions with TC motifs. An optimal binding sequence of AAATCTCG was identified by protein binding microarray and confirmed by isothermal titration calorimetry (ITC) and mutagenesis. ITC showed BANP bound unmethylated and methylated DNAs with comparable affinities in this structural context. | PMID:37086783 | The Journal of biological chemistry |
| 2024 | High | Crystal structures of the BANP BEN domain in complex with cognate DNA substrates revealed that oligomerization is required for BANP to select unmethylated CGCG motif-containing DNA substrates, clarifying the mechanism by which BANP functions as a CpG island-binding protein preferring unmethylated CpG motifs. | PMID:39225042 | Nucleic acids research |
| 2022 | High | In zebrafish, Banp is required for DNA damage response and chromosome segregation during mitosis. banp mutants show DNA replication stress, tp53-dependent DNA damage responses, and defective chromosome segregation from prometaphase to anaphase. RNA- and ATAC-sequencing identified direct Banp target genes carrying the Banp motif, including the DNA replication fork regulator wrnip1 and chromosome segregation regulators cenpt and ncapg. | PMID:35942692 | eLife |
| 2000 | Medium | SMAR1 (BANP) was identified as a novel MAR-binding protein that binds the MARbeta scaffold/matrix-associated region 400 bp upstream of the TCRbeta enhancer. GST-SMAR1 fusion protein binding to MARbeta was competed by excess MAR-containing DNA from the immunoglobulin kappa locus. SMAR1 shares homology with SATB1 and Cux/CDP in the MAR-binding/Cut repeat domain and with the tetramerization domain of Bright. | PMID:10950932 | Genomics |
| 2000 | Low | BANP (BTG3-associated nuclear protein) was identified via yeast two-hybrid screening using BTG3 as bait. The protein was localized to human chromosome 16q24, a region with frequent loss of heterozygosity in tumors. | PMID:10940556 | Gene |
| 2005 | High | SMAR1 represses cyclin D1 gene expression by recruiting a repressor complex containing SIN3, HDAC1, and pocket retinoblastoma proteins to the cyclin D1 promoter MAR, resulting in histone deacetylation spreading at least 5 kb upstream. The interaction is mediated by the SMAR1(160–350) domain. | PMID:16166625 | Molecular and cellular biology |
| 2003 | Medium | SMAR1 physically interacts and colocalizes with p53, and the shorter isoform SMAR1(S) activates p53-mediated reporter gene expression and its downstream effector p21. Overexpression of SMAR1(S) in B16F1 melanoma cells delays tumor growth in C57BL/6 mice and causes G2/M phase retardation. | PMID:12494467 | International journal of cancer |
| 2005 | High | The arginine-serine (RS)-rich domain of SMAR1 is phosphorylated by protein kinase C family proteins and is responsible for p53 interaction, activation, and stabilization within the nucleus. SMAR1-mediated stabilization of p53 occurs by inhibiting Mdm2-mediated degradation of p53. In vitro phosphorylation assays with point-mutated peptides identified serine 347 as indispensable for activity. | PMID:15701641 | The Journal of biological chemistry |
| 2009 | Medium | SMAR1 interacts with MDM2 and the Ser15-phosphorylated form of p53, forming a ternary complex in the post-stress recovery phase. This triple complex recruits HDAC1 to deacetylate p53, which then binds poorly to the p21 promoter, switching off the p53 response. siRNA knockdown of SMAR1 led to prolonged cell-cycle arrest in the post-stress recovery phase. | PMID:19303885 | Journal of molecular biology |
| 2010 | High | SMAR1 selectively represses BAX and PUMA by binding to an identical MAR element in their promoters and inducing HDAC1-mediated p53 deacetylation, generating an anti-apoptotic response and cell cycle arrest upon mild DNA damage. Upon apoptotic DNA damage, PML nuclear bodies sequester SMAR1, releasing BAX and PUMA repression. SMAR1 knockdown induces apoptosis that is abrogated in the absence of p53. | PMID:20075864 | The EMBO journal |
| 2004 | Medium | SMAR1 and Cux/CDP modulate chromatin structure at MARbeta by DNaseI hypersensitivity, independently repress Ebeta-dependent reporter gene expression, and physically interact with each other. The repressor activity of SMAR1 is enhanced by Cux/CDP; they colocalize in the perinuclear region through a SMAR1 repression domain that is separate from the MAR-binding domain and contains a nuclear localization signal and RS-rich domain. | PMID:15371550 | Nucleic acids research |
| 2004 | Medium | SMAR1-overexpressing transgenic mice exhibit severely altered Vbeta T cell frequency and reduced Vbeta5.1/5.2 and Vbeta8.1/8.2/8.3 rearrangements, demonstrating that SMAR1 plays an important role in regulation of V(D)J recombination and T cell development in vivo. | PMID:15623522 | The Journal of biological chemistry |
| 2007 | Medium | SMAR1 transcription is regulated by p53 through a p53 response element in the SMAR1 promoter; upon doxorubicin-induced DNA damage, acetylated p53 is recruited to the SMAR1 promoter, activating its transcription. In turn, SMAR1 inhibits tumor cell migration through inhibition of TGFbeta signaling and its downstream targets including cutl1 and focal adhesion molecules. | PMID:17668048 | PloS one |
| 2015 | High | SMAR1 negatively regulates alternative splicing through HDAC6-mediated deacetylation of RNA-binding protein Sam68. SMAR1 is enriched in nuclear splicing speckles and associates with snRNAs involved in splice site recognition. ERK-1/2-mediated phosphorylation of SMAR1 at threonines 345 and 360 localizes SMAR1 to the cytoplasm, preventing its interaction with Sam68. Loss of SMAR1 increases Sam68 acetylation and CD44 variant exon inclusion, enhancing metastatic propensity. | PMID:26080397 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | High | Cdc20, the substrate receptor of the APC/C ubiquitin ligase complex, binds SMAR1 and promotes its K48-linked polyubiquitylation and proteasomal degradation in a D-box motif-dependent manner. shRNA-mediated inactivation of Cdc20 leads to significant stabilization of SMAR1. Cdc20 fails to target SMAR1 upon genotoxic stress, allowing SMAR1 to support DNA damage repair. Cdc20-mediated degradation of SMAR1 promotes cell migration and invasion. | PMID:28617439 | Cell death & disease |
| 2014 | High | SMAR1 inhibits EMT by two mechanisms: (1) transcriptional repression of Slug via direct recruitment of an SMAR1/HDAC1 complex to the MAR site in the Slug promoter, restoring E-cadherin expression; (2) hindering E-cadherin–MDM2 interaction, thereby reducing ubiquitination and degradation of E-cadherin protein. siRNA knockdown of SMAR1 results in coordinated Slug-mediated E-cadherin repression and MDM2-mediated E-cadherin degradation. | PMID:25086032 | The Journal of biological chemistry |
| 2012 | Medium | TCF-4, β-catenin, and SMAR1 tether together at the -143 nucleotide site on the HIV LTR to inhibit HIV promoter activity, likely by pulling the HIV DNA segment into the nuclear matrix away from transcriptional machinery. Deletion/mutation of this site or TCF-4/β-catenin knockdown enhanced basal HIV promoter activity ~5-fold. | PMID:22674979 | Journal of virology |
| 2010 | Medium | SMAR1 binds to the LTR MAR of HIV-1 and reinforces transcriptional silencing by tethering the LTR MAR to the nuclear matrix. The SMAR1-associated HDAC1-mSin3 corepressor complex is dislodged from the LTR upon cellular activation, increasing histone acetylation and RNA Pol II recruitment. SMAR1 overexpression reduces LTR-mediated transcription in both Tat-dependent and -independent manners, decreasing virion production. | PMID:20153010 | Virology |
| 2008 | Medium | SMAR1 binds to the MAR site in the IκBα promoter, recruits a corepressor complex, and represses IκBα transcription, resulting in formation of functional but phosphorylation-deficient and transactivation-deficient p65-p50 NF-κB complexes. SMAR1 down-regulates a subset of NF-κB target genes involved in tumorigenesis and inhibits TNFα-induced NF-κB activation independently of the classical pathway. | PMID:18981184 | The Journal of biological chemistry |
| 2014 | Medium | SMAR1 coordinates with HDAC6 to maintain Ku70 in a deacetylated state. SMAR1 knockdown results in enhanced Ku70 acetylation, impaired recruitment of Ku70 to chromatin fractions, and altered Bax-mediated apoptosis. Ionizing radiation induces SMAR1 expression and its redistribution as distinct nuclear foci via ATM-mediated phosphorylation at serine 370. SMAR1 regulates IR-induced G2/M arrest by facilitating Chk2 phosphorylation and provides radioresistance by modulating deacetylated Ku70 association with Bax. | PMID:25299772 | Cell death & disease |
| 2021 | Medium | SMAR1 regulates PKM alternative splicing by recruiting HDAC6 to deacetylate PTBP1, which reduces PTBP1 enrichment on PKM pre-mRNA (measured by CLIP). This promotes PKM1 over PKM2 expression, suppresses the Warburg effect, and inhibits tumorigenesis in a PKM2-dependent manner. | PMID:33863392 | Cancer & metabolism |
| 2010 | Medium | SMAR1 directly interacts with and inhibits AKR1a4 enzyme activity in the cytoplasm. Upon stress, ATM kinase promotes nuclear translocation of SMAR1, causing dissociation of the SMAR1-AKR1a4 complex and elevated AKR1a4 activity. AKR1a4 enzyme activity is elevated in higher grades of breast cancer where SMAR1 is downregulated. | PMID:20097305 | The international journal of biochemistry & cell biology |
| 2015 | Medium | SMAR1 negatively regulates STAT3 expression by binding to the MAR element of the STAT3 promoter adjacent to IL-6 response elements, favoring Foxp3 expression and Treg cell differentiation. T-cell-specific conditional knockdown of SMAR1 exhibits increased susceptibility to colitis and compromised Treg suppressor function with increased Th17 differentiation. | PMID:25993445 | Mucosal immunology |
| 2015 | Medium | SMAR1 functions as a negative regulator of Th1 and Th17 differentiation by binding to MAR regions in the promoters of T-bet and IL-17, respectively. Conditional knockout of SMAR1 in T cells resulted in resistance to eosinophilic airway inflammation with skewing toward Th1 response. | PMID:25736456 | Mucosal immunology |
| 2014 | Medium | SMAR1 represses HPV18 E6 transcription by binding to MAR elements in the HPV18 LCR and E6 sequences, recruiting an SMAR1-HDAC1 repressor complex that decreases histone acetylation at H3K9 and H3K18 and inhibits c-Fos binding at AP-1 sites in the E6 promoter. | PMID:25157104 | The Journal of biological chemistry |
| 2009 | Low | SMAR1 directly interacts with MDM2 and inhibits AKR1a4 enzyme activity. In addition, SMAR1 overexpression modulates cell surface roughness as measured by AFM, correlating with cytoskeletal protein expression changes seen by microarray. | PMID:19799771 | BMC cancer |
| 2018 | Medium | SMAR1 inhibits Wnt/β-catenin signaling by recruiting HDAC5 to the β-catenin promoter, resulting in reduced H3K9 acetylation, decreased β-catenin expression, and inhibited cell migration and invasion. During aberrant Wnt3a signaling, SMAR1 undergoes proteasomal degradation dependent on its D-box elements (RCHL and RQRL); substitution mutations in these D-box elements completely abrogated degradation. | PMID:29765542 | Oncotarget |
| 2013 | Medium | miR-320a negatively regulates SMAR1 expression by directly binding to its 3'UTR. In response to mild DNA damage, miR-320a expression decreases, resulting in enhanced SMAR1 protein levels. During hemin-induced erythroid differentiation, enhanced SMAR1 negatively correlates with miR-320a expression. SMAR1 in turn binds to the promoter of miR-221/222 to regulate early erythropoiesis. | PMID:23876508 | The international journal of biochemistry & cell biology |
| 2020 | Medium | In breast cancer stem cells, SMAR1 expression is decreased through cooperative interaction of pluripotency factors Oct4 and Sox2 with HDAC1. Overexpression of SMAR1 sensitizes CSCs to chemotherapy through SMAR1-dependent recruitment of HDAC2 to the ABCG2 gene promoter, repressing its transcription. Aspirin restores SMAR1 expression and ABCG2 repression, enhancing chemosensitivity. | PMID:33082288 | Science signaling |
| 2007 | Medium | SMAR1 mRNA is stabilized by a minor stem-loop structure in its 5'UTR (phi1 UTR) in response to Prostaglandin A2 (PGA2), forming a nucleoprotein complex that increases SMAR1 transcript and protein levels. Breast cancer cell lines express a variant 5'UTR (phi17 UTR) lacking this stem-loop, preventing PGA2-induced stabilization and resulting in low SMAR1 levels. | PMID:17726044 | Nucleic acids research |
| 2010 | Medium | HSP70 binds to a novel site on the phi1 SMAR1 5'UTR upon PGA2 treatment, stabilizing the wild-type SMAR1 transcript. HSP70 knockdown perturbs SMAR1-mediated cell cycle arrest in PGA2-treated cells. HSP70 cannot bind the phi17 SMAR1 UTR variant predominant in breast cancers, accounting for low SMAR1 protein levels. | PMID:20153327 | FEBS letters |
| 2009 | Medium | SMAR1 regulates TNFα-induced CD40 expression: SMAR1 recruits HDAC1 to the CD40 promoter to repress basal transcription; TNFα induces phosphorylation of SMAR1 at Ser-347, promoting its cytoplasmic translocation and releasing repression. Concomitantly, JAK1-mediated STAT1 phosphorylation at Tyr-701 drives nuclear STAT1 activation of CD40 via p300 recruitment. | PMID:20006573 | Biochemical and biophysical research communications |
| 2016 | Medium | ChIP-sequencing revealed that SMAR1 binds to T(C/G) repeat sequences genome-wide, targeting genes in diverse biological pathways. SMAR1 binds and represses the miR-371-373 cluster promoter by recruiting an HDAC1/mSin3A complex; a ~200 bp promoter region is necessary for SMAR1 binding. SMAR1 regulation of miR-371-373 inhibits breast cancer tumorigenesis and metastasis in vivo. | PMID:27671416 | Scientific reports |
| 2011 | Medium | SMAR1 inhibits p53 acetylation and p53-dependent apoptosis by repressing p300 expression in response to DNA damage. SMAR1 interacts with the p53-p300 transcriptional complex and antagonizes p300 interaction with p53, suppressing activation of p53 apoptotic targets and miR-34a. Ectopic p300 expression rescues SMAR1-mediated inhibition on p53. | PMID:22074660 | The international journal of biochemistry & cell biology |
| 2024 | Low | ZNF471 interacts with BANP (demonstrated by Co-IP) in renal cancer cells and suppresses the malignant phenotype by inactivating the PI3K/AKT/mTOR signaling pathway. | PMID:38169650 | International journal of biological sciences |
| 2024 | Low | BANP overexpression in human umbilical vein endothelial cells promotes p53 phosphorylation and nuclear retention, inducing cellular senescence in the context of chronic intermittent hypoxia. | PMID:38168028 | Gerontology |
| 2021 | Medium | SMAR1 suppresses the cancer stem cell population in colorectal cancer by acting as a transcriptional repressor of hTERT. SMAR1 interacts with the HDAC1/mSin3a co-repressor complex at the hTERT promoter to mediate HDAC1-dependent transcriptional repression. Knockdown of SMAR1 promotes cancer stem cell phenotype and sphere-forming ability. | PMID:34551340 | The international journal of biochemistry & cell biology |
| 2019 | Medium | SMAR1 positively regulates MHC class I surface expression by transcriptionally repressing calnexin through binding to a short MAR region in the calnexin promoter and forming a repressor complex with GATA2 and HDAC1. Influenza A (H1N1) infection increases SMAR1 levels, resulting in reduced calnexin expression and increased MHC I presentation. | PMID:31422285 | Neoplasia (New York, N.Y.) |
| 2014 | Medium | SMAR1 represses NF-κB-dependent IL-8 transcription by binding to the IL-8 promoter MAR and recruiting an HDAC1-dependent co-repressor complex. Additionally, SMAR1 antagonizes p300-mediated acetylation of RelA/p65, a modification required for IL-8 transactivation. | PMID:25239884 | The international journal of biochemistry & cell biology |
| 2021 | Medium | SMAR1 negatively regulates adipogenesis by recruiting the HDAC1/mSin3a repressor complex to the PPARγ promoter, suppressing PPARγ expression and adipocyte differentiation. During adipogenesis, cdc20-mediated proteasomal degradation of SMAR1 permits PPARγ upregulation; knockdown of cdc20 stabilizes SMAR1 and reduces adipocyte differentiation. | PMID:34450266 | Biochimica et biophysica acta. Molecular and cell biology of lipids |
| 2022 | Medium | TOPORS, induced via the TLR4-TRIF pathway by LPS, binds the SMAR1 promoter (shown by ChIP) and modulates SMAR1 transcription. LPS-induced SMAR1 expression decreases STAT3 expression and skews tumor-associated macrophage polarization toward the M1 phenotype. | PMID:34689394 | Molecular oncology |
| 2023 | Medium | RBX1, an E3 ubiquitin ligase, degrades SMAR1 through the ubiquitin-proteasome pathway in anaplastic thyroid carcinoma cells, thereby disrupting the SMAR1/HDAC6 complex, leading to increased PKM2 expression, enhanced Warburg effect, and increased ATC cell metastasis. | PMID:36810109 | Cell & bioscience |

## Citations

- PMID:10940556
- PMID:10950932
- PMID:12494467
- PMID:15371550
- PMID:15623522
- PMID:15701641
- PMID:16166625
- PMID:17668048
- PMID:17726044
- PMID:18981184
- PMID:19303885
- PMID:19799771
- PMID:20006573
- PMID:20075864
- PMID:20097305
- PMID:20153010
- PMID:20153327
- PMID:22074660
- PMID:22674979
- PMID:23876508
- PMID:25086032
- PMID:25157104
- PMID:25239884
- PMID:25299772
- PMID:25736456
- PMID:25993445
- PMID:26080397
- PMID:27671416
- PMID:28617439
- PMID:29765542
- PMID:31422285
- PMID:33082288
- PMID:33863392
- PMID:34234345
- PMID:34450266
- PMID:34551340
- PMID:34689394
- PMID:35942692
- PMID:36810109
- PMID:37086783
- PMID:38168028
- PMID:38169650
- PMID:39225042
