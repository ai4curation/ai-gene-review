---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARID5B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q14865
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 23
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARID5B (human)

## Current model (mechanistic narrative)

ARID5B is an AT-rich interaction domain (ARID) transcription factor that functions as a sequence-specific DNA-targeting subunit for chromatin-modifying complexes, coupling promoter recognition to histone demethylation and deacetylation to control cell differentiation and metabolism [PMID:21532585, PMID:10329386]. Its ARID domain recognizes the core AATA(C/T) motif through major- and minor-groove contacts, with two flexible interhelical loops (L1, L2) mediating phosphate-backbone and AT base-pair contacts [PMID:10329386, PMID:17407261]. Mechanistically, ARID5B associates with the PKA-activated H3K9me2 demethylase PHF2 and targets this complex to promoters to erase repressive methyl marks and activate transcription [PMID:21532585]; this ARID5B–PHF2 module promotes chondrocyte differentiation through Sox9 target genes [PMID:24276541] and activates SORBS2 to suppress epithelial-to-mesenchymal transition [PMID:37948999]. In an opposing capacity, ARID5B assembles a chromatin repressor complex with MIER1, C16ORF87, HDAC1 and HDAC2, tethering deacetylase activity to active distal regulatory elements and promoters to repress B-cell proliferation and signaling genes [PMID:bio_10.1101_2025.10.17.683040]. ARID5B is a central regulator of fuel selection and lipid storage: knockout mice show defective brown/white adipose lipid accumulation and resistance to diet-induced obesity [PMID:14651970, PMID:33757861], and muscle-specific loss reprograms substrate use through control of prostanoid (PGI2) biosynthesis, GLUT4/TBC1D1-dependent glucose handling, and mitochondrial pyruvate transport [PMID:29196500, PMID:33023658, PMID:36743919]. In hematopoiesis, ARID5B governs Pre-B cell expansion and metabolism [PMID:37483604, PMID:35924577], and acts as a collaborating oncogenic factor by co-occupying genomic targets with the TAL1 complex and activating MYC in T-ALL [PMID:29326336]. ARID5B's own expression is set by lineage transcription factors and enhancer variants, including Ikaros [PMID:30420689] and a MEF2C/RUNX1-bound enhancer harboring an ALL risk allele [PMID:35575404].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1430728 Metabolism, R-HSA-1643685 Disease, R-HSA-1266738 Developmental Biology
- **partners:** PHF2, SOX9, TAL1, MIER1, HDAC1, HDAC2, C16ORF87
- **complexes:** ARID5B-PHF2 demethylase complex, ARID5B-MIER1-HDAC1-HDAC2 repressor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ARID5B forms a histone demethylase complex with PHF2. PHF2 is enzymatically inactive alone but becomes an active H3K9Me2 demethylase upon PKA-mediated phosphorylation; phosphorylated PHF2 then associates with ARID5B (a DNA-binding protein), and ARID5B itself is demethylated. The PHF2-ARID5B complex is then targeted to promoters where it removes the repressive H3K9Me2 mark to activate transcription. | PMID:21532585 | Nature cell biology |
| 2013 | High | ARID5B physically associates with the transcription factor Sox9 and recruits the histone demethylase PHF2 to the promoter regions of Sox9 target genes, stimulating H3K9me2 demethylation and thereby promoting chondrocyte differentiation. Arid5b-/- mice show retarded growth and delayed endochondral ossification, and H3K9me2 levels are increased at chondrogenic marker gene promoters in Arid5b-deficient chondrocytes. | PMID:24276541 | Nature communications |
| 1999 | High | The ARID (MRF2/ARID5B) DNA-binding domain recognizes the core sequence AATA(C/T) through contacts in both major and minor grooves. Major groove contacts at positions 2, 3, and 4 of the core sequence are required for high-affinity binding, while positions 1 and 5 are contacted through the minor groove. The core sequence alone is not sufficient for high-affinity binding. | PMID:10329386 | Biochemical and biophysical research communications |
| 2001 | High | NMR backbone dynamics of the MRF2/ARID5B ARID domain show that two flexible interhelical loops (and the C-terminal tail) are involved in DNA recognition. Upon DNA binding, flexible loops show reduced mobility while some well-structured regions (including the putative DNA-contacting helix) show decreased order parameters, indicating that protein dynamics are integral to DNA binding. | PMID:11478881 | Biochemistry |
| 2007 | High | The three-dimensional structure of the MRF2/ARID5B ARID domain in complex with target DNA was determined by NMR using paramagnetic spin-label distance constraints. MRF2 contacts DNA mainly through two flexible loops (L1 and L2): L1 contacts the phosphate backbone, while L2 and residues in adjacent helices interact with AT base pairs in the major groove. | PMID:17407261 | Biochemistry |
| 2003 | High | Targeted disruption of Mrf2/Arid5b in mice results in high neonatal mortality, severely reduced lipid accumulation in brown adipose tissue in neonates, and lean adult phenotype with significant reductions in brown and white adipose tissues. Mrf2-/- mice are resistant to high-fat diet-induced obesity, demonstrating that ARID5B is essential for lipid accumulation in postnatal life. | PMID:14651970 | Biochemical and biophysical research communications |
| 2018 | High | A short isoform of ARID5B is selectively induced through DNA hypomethylation in adaptive (cytomegalovirus-expanded) NK cells. Knockdown and overexpression studies demonstrated that ARID5B directly promotes mitochondrial membrane potential, expression of genes encoding electron transport chain components, oxidative metabolism, survival, and IFN-γ production in these cells. | PMID:30061358 | The Journal of experimental medicine |
| 2018 | High | ARID5B is a direct transcriptional target of the TAL1 oncogenic complex in T-ALL and functions as a collaborating oncogenic factor. ARID5B co-occupies target genes with TAL1 and coordinately controls their expression. ARID5B positively regulates expression of TAL1 and its regulatory partners, and activates MYC expression. Forced expression of ARID5B in immature thymocytes causes thymus retention, differentiation arrest, radioresistance, and tumor formation in zebrafish. | PMID:29326336 | Genes & development |
| 2018 | Medium | ARID5B physically interacts with PHF2 in acute lymphoblastic leukemia cells. Ikaros directly regulates ARID5B expression, and restoring Ikaros function via Casein Kinase II inhibition promotes ARID5B expression through recruitment of H3K4me3 at the ARID5B promoter. | PMID:30420689 | Oncogenesis |
| 2018 | High | Arid5b-/- primary skeletal muscle cells exhibit differentiation defects and impaired sarcomeric assembly. Mechanistically, Arid5b-/- cells show down-regulation of COX-1 (Ptgs1) and PGI synthase (Ptgis), leading to reduced PGI2 production. Treatment with the PGI2 analog iloprost rescues defects in myotube formation, migration, and fusion, placing ARID5B upstream of the prostanoid biosynthesis pathway in myogenesis. | PMID:29196500 | FASEB journal |
| 2020 | Medium | Arid5b knockout in skeletal muscle leads to increased basal glucose uptake, glycogen content, glucose oxidation, and ATP production. The mechanistic basis involves downregulation of TBC1D1 (a negative regulator of GLUT4 translocation), resulting in increased GLUT4 localization at the plasma membrane in Arid5b-/- muscle. | PMID:33023658 | Biological research |
| 2021 | Medium | Fabp4-Cre conditional Arid5b knockout mice (adipocyte-specific) are resistant to high-fat diet-induced weight gain, with decreased lipid accumulation specifically in subcutaneous (inguinal) white adipose tissue and liver, but not in gonadal WAT. RNA-seq revealed decreased expression of inflammation-associated genes in IWAT adipocytes of FSKO mice, suggesting ARID5B regulates inflammatory signaling from specific WAT depots to the liver. | PMID:33757861 | Molecular and cellular endocrinology |
| 2022 | High | ARID5B risk variants at the ALL susceptibility locus function through cis-regulatory elements. CRISPR-based enhancer screening identified six cis-regulatory elements at the ARID5B locus. The top ALL risk variant (rs7090445) lies within the strongest enhancer, which is distally tethered to the ARID5B promoter. The risk allele disrupts the MEF2C binding motif, reducing MEF2C affinity and decreasing local chromatin accessibility. MEF2C influences ARID5B expression in ALL, likely via a transcription factor complex with RUNX1. | PMID:35575404 | Journal of the National Cancer Institute |
| 2023 | Medium | ARID5B-PHF2 complex promotes histone demethylation at H3K36me2 at the SORBS2 promoter, thereby activating SORBS2 transcription and suppressing epithelial-to-mesenchymal transition (EMT) and tumor generation in ovarian cancer cells. | PMID:37948999 | Pathology, research and practice |
| 2023 | Medium | ARID5B regulates B cell development at the Pre-B cell stage: Arid5b deletion in vivo and ex vivo causes increased large and small Pre-B cell proportions with enhanced proliferation, and enhanced fatty acid uptake and oxidation at the Pre-B stage. ARID5B expression is upregulated at the Pre-B stage and maintained through later B cell development. | PMID:37483604 | Frontiers in immunology |
| 2023 | Medium | Arid5b overexpression in mice (Vav1-driven transgenic) causes a dramatic reduction in circulating B cells and B cell fractions in peripheral blood, bone marrow, and spleen. ARID5B overexpression leads to defects in B cell activation in vitro with hyperactivation of B-cell receptor signaling at baseline, and increases mitochondrial oxygen consumption rate in naïve and stimulated B cells. | PMID:35924577 | Haematologica |
| 2023 | Medium | Muscle-specific deletion of Arid5b leads to preferential utilization of fatty acids for energy generation in skeletal muscle, decreased adipose tissue weight (via increased phospho-HSL/HSL in WAT), and glucose diversion into the pentose phosphate pathway and glycolysis for lactate export. Glucose oxidation is reduced in conjunction with downregulation of the mitochondrial pyruvate carrier (MPC). This establishes ARID5B as a regulator of fuel selection in skeletal muscle that systemically influences adipose and liver metabolism. | PMID:36743919 | Frontiers in endocrinology |
| 2024 | Medium | ARID5B directly activates LINC01128 transcription by binding to its promoter (confirmed by ChIP). The long isoform of ARID5B is negatively regulated by TNF-α in rheumatoid arthritis synovial fibroblasts, and suppresses IL-6 production stimulated by TNF-α. siRNA knockdown and lentiviral overexpression of ARID5B isoforms confirmed the long isoform as a negative modulator of IL-6. | PMID:38224186, PMID:38747454 | Clinical and translational medicine / Immunological medicine |
| 2025 | Medium | ARID5B assembles into a chromatin repressor complex with MIER1, C16ORF87, HDAC1, and HDAC2 in B-ALL cells. CUT&RUN mapping showed ARID5B binds active regions of the genome and tethers HDAC1/HDAC2 to distal regulatory elements and promoters. Genes actively repressed by this ARID5B complex are involved in B cell proliferation and B cell-specific signaling. | PMID:bio_10.1101_2025.10.17.683040 | bioRxiv |
| 2025 | Medium | In epileptogenesis, WDR5 enhances H3K4me3 deposition at the Arid5b promoter, driving transcriptional upregulation of ARID5B in hippocampal neurons. The upregulated ARID5B subsequently represses GABA-A receptor (GABAAR) subunit expression, impairing inhibitory synaptic transmission and facilitating epileptogenesis. | PMID:41510154 | Theranostics |
| 2025 | Low | ApoM upregulates Arid5b expression in hepatocytes, and Arid5b knockdown increases culture-medium prothrombin levels while decreasing cellular prothrombin levels, reversing ApoM's inhibitory effect on prothrombin secretion. This places ARID5B downstream of ApoM in regulation of hepatic prothrombin secretion, independent of S1P receptors. | PMID:40719152 | Thrombosis and haemostasis |
| 2024 | Low | Two transcriptionally distinct ARID5B isoforms (short and long) differ in an encoded BAH-like chromatin interaction domain. Both isoforms have functionally independent proximal promoters as shown by luciferase reporter assays. Increased short isoform expression is associated with decreased event-free and overall survival in B-ALL, and the isoform ratio strongly correlates with B-ALL prognostic stratification. | PMID:38382358 | Biochemical and biophysical research communications |

## Citations

- PMID:10329386
- PMID:11478881
- PMID:14651970
- PMID:17407261
- PMID:21532585
- PMID:24276541
- PMID:29196500
- PMID:29326336
- PMID:30061358
- PMID:30420689
- PMID:33023658
- PMID:33757861
- PMID:35575404
- PMID:35924577
- PMID:36743919
- PMID:37483604
- PMID:37948999
- PMID:38224186
- PMID:38382358
- PMID:38747454
- PMID:40719152
- PMID:41510154
- PMID:bio_10.1101_2025.10.17.683040
