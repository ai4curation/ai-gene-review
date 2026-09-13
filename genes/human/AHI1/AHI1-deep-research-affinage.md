---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AHI1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q8N157
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 31
citation_count: 31
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AHI1 (human)

## Current model (mechanistic narrative)

AHI1 (Jouberin) is a modular SH3- and WD40-repeat scaffolding/adaptor protein that operates at the primary cilium transition zone and in neuronal cytoplasmic signaling, with loss-of-function mutations causing Joubert syndrome featuring cerebellar malformation and abnormal axonal decussation [PMID:15322546, PMID:15467982]. At the ciliary base, AHI1 localizes to the mother centriole/basal body, where its recruitment to a ring-shaped transition-zone domain depends on Cby1, and where it is required for ciliogenesis and polarized vesicular trafficking by stabilizing the small GTPase Rab8a [PMID:19625297, PMID:25103236]. AHI1 governs ciliary cargo: it sustains Arl13b ciliary membrane localization and proteasomal stability to support Sonic hedgehog signaling and proper axoneme length, mediates outer-segment protein transport in photoreceptors, and targets the GPCRs MCHR1 to the ciliary membrane for downstream cAMP/ERK signaling [PMID:20592197, PMID:31391239, PMID:33741721]. Its WD40 region binds NPHP1, and Joubert/retinitis pigmentosa mutations in this region destabilize AHI1 and impair its ciliary-base enrichment, whereas the C-terminal SH3 domain is dispensable for normal development [PMID:23532844, PMID:25616960, PMID:28442542]. In neurons AHI1 forms a stable complex with HAP1 that regulates TrkB receptor endocytic sorting and signaling, and AHI1 controls additional partners including 5-HT2CR, Cend1, GR, and APP to influence neurite outgrowth, feeding behavior, and stress-related/depressive phenotypes [PMID:18636121, PMID:20956301, PMID:22123816, PMID:23658157, PMID:31062249, PMID:33782379]. Beyond ciliary and neuronal roles, AHI1 has hematopoietic and immune functions: an AHI-1/BCR-ABL/JAK2 complex assembled via its SH3 domain modulates JAK2-STAT5 phosphorylation and tyrosine kinase inhibitor resistance in leukemia, and AHI1 recruits the deubiquitinase OTUD1 to stabilize Tyk2 and maintain basal type-I interferon signaling [PMID:18936234, PMID:22623184, PMID:35821088].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005815 microtubule organizing center, GO:0005929 cilium, GO:0005829 cytosol, GO:0005739 mitochondrion, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-9609507 Protein localization, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-168256 Immune System, R-HSA-392499 Metabolism of proteins
- **partners:** HAP1, NPHP1, RAB8A, ARL13B, BCR-ABL, JAK2, OTUD1, GR
- **complexes:** AHI-1/BCR-ABL/JAK2 complex, AHI1-HAP1 complex, AHI1-OTUD1-Tyk2 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | Medium | AHI1 encodes a modular protein containing one SH3 domain and seven WD40 repeats, and was identified as a gene targeted by provirus insertional mutations in Abelson pre-B-cell lymphomas. Proviral insertions at the 3' end of the gene produced truncated Ahi-1/viral fused transcripts, including splicing variants with deletion of the SH3 domain, implicating it in signal transduction. | PMID:12186888 | Journal of virology |
| 2004 | High | AHI1 is most highly expressed in neurons that give rise to the crossing axons of the corticospinal tract and superior cerebellar peduncles, and loss-of-function mutations cause Joubert syndrome with abnormal axonal decussation and cerebellar malformation. | PMID:15322546 | Nature genetics |
| 2004 | Medium | AHI1 (encoding Jouberin) contains WD40 repeats, an SH3 domain, and numerous SH3-binding sites, and is expressed strongly in embryonic hindbrain and forebrain, indicating roles in cerebellar and cortical development. Frameshift and missense mutations cause Joubert syndrome with cortical polymicrogyria. | PMID:15467982 | American journal of human genetics |
| 2008 | High | Ahi1 protein localizes to the mother centriole (basal body of the primary cilium). Knockdown of Ahi1 by shRNAi or targeted Ahi1 deletion impairs ciliogenesis. In Ahi1-knockdown cells, Rab8a (a small GTPase critical for polarized membrane trafficking) is destabilized and fails to localize properly to the basal body, causing defects in endocytic vesicle trafficking from the plasma membrane to the Golgi and back. | PMID:19625297 | Human molecular genetics |
| 2008 | High | Mouse Ahi1 forms a stable protein complex with huntingtin-associated protein 1 (Hap1). Hap1-knockout mice show significantly reduced Ahi1 levels, defective cerebellar development, and abnormal axonal decussation. Suppression of Ahi1 also decreases Hap1 levels. Truncated Ahi1 (corresponding to Joubert syndrome mutations) inhibits neurite outgrowth in neuronal culture. The Ahi1-Hap1 complex regulates TrkB receptor internalization and signaling (reducing TrkB-mediated neurogenesis/differentiation). | PMID:18636121 | The Journal of clinical investigation |
| 2008 | Medium | Murine Ahi1 is distributed throughout the cytoplasm, dendrites, and axons of neurons but is absent from glial cells. Ahi1 protein consistently accumulates in the stigmoid body, a cytoplasmic organelle found in neurons. | PMID:18785627 | The Journal of comparative neurology |
| 2008 | High | AHI-1 overexpression in murine and human hematopoietic cells confers growth advantages in vitro and induces leukemia in vivo, enhancing BCR-ABL effects. AHI-1, BCR-ABL, and JAK2 form a physical interaction complex. Modulation of AHI-1 expression regulates phosphorylation of BCR-ABL and JAK2-STAT5. RNAi-mediated suppression of AHI-1 in CML stem/progenitor cells reduces growth autonomy. This complex mediates tyrosine kinase inhibitor (TKI) resistance. | PMID:18936234 | The Journal of experimental medicine |
| 2009 | Medium | Knockdown of AHI-1 in CTCL cells identifies HCK (tyrosine kinase) and BIN1 (tumor suppressor) as downstream effectors. Changes in HCK phosphorylation were observed upon AHI-1 suppression or overexpression. BIN1 physically interacts with MYC in CTCL cells. AHI-1 suppression alters autocrine cytokine production (IL-2, IL-4, TNFα). | PMID:19211505 | Blood |
| 2010 | High | Ahi1-null mice fail to form retinal photoreceptor outer segments and have abnormal distribution of opsin throughout photoreceptors. Photoreceptor apoptosis occurs rapidly between 2-4 weeks of age. This phenotype shows dosage-sensitive genetic interaction with Nphp1 (another ciliopathy gene), and reducing opsin dosage significantly delays cell death. | PMID:20081859 | Nature genetics |
| 2010 | High | In Ahi1-/- mice, photoreceptor outer segment proteins (transducin, Rom1) fail to be transported appropriately or are significantly reduced, while synaptic proteins are correctly trafficked. Vesicular targeting defects are cilium-specific. Rab8a expression is decreased in Ahi1-/- mice, suggesting Ahi1 stabilizes Rab8a to mediate polarized vesicular trafficking to the outer segment. | PMID:20592197 | The Journal of neuroscience |
| 2010 | High | Neuronal-specific Ahi1 deficiency (Cre-loxP) reduces TrkB levels in the brain and causes depressive phenotypes. Ahi1 deficiency promotes degradation of endocytic TrkB and reduces TrkB signaling in neuronal cells. Overexpression of TrkB in the amygdala rescues depressive phenotypes. | PMID:20956301 | Proceedings of the National Academy of Sciences of the United States of America |
| 2011 | Medium | In zebrafish ahi1 morphants, knockdown causes loss of cilia at Kupffer's vesicle and subsequently defects in cardiac left-right asymmetry. siRNA knockdown in renal epithelial cells demonstrates a role for Ahi1 in both ciliogenesis and cell-cell junction formation. | PMID:21959375 | Cellular and molecular life sciences : CMLS |
| 2011 | Medium | Hypothalamic Ahi1 interacts with serotonin receptor 2C (5-HT2CR) and promotes its degradation via the lysosomal pathway. Knockdown of hypothalamic Ahi1 increases 5-HT2CR expression and decreases food intake and body weight. Ahi1 regulates neuropeptide Y and POMC expression downstream of this interaction. | PMID:22123816 | The Journal of biological chemistry |
| 2012 | High | Crystal structure of the AHI-1 SH3 domain resolved at 1.53-Å resolution reveals canonical SH3 folding with an unusual C-terminal α-helix. Deletion of the SH3 domain significantly enhances apoptotic response of BCR-ABL+ cells to TKIs. A novel interaction between AHI-1 and Dynamin-2 (a GTPase) was identified through the SH3 domain. PD1R peptide modeling suggests an 'Arg-Arg-Trp' stack forms within the binding interface. | PMID:22623184 | Proteomics |
| 2013 | High | Full-length (but not N-terminal) Ahi1 binds Hap1, and this interaction is regulated by nerve growth factor: NGF induces dephosphorylation of Hap1A and decreases its association with Ahi1. Ahi1 associates with phosphorylated Hap1A in cytosolic but not synaptosomal fractions. Mass spectrometry of cytosolic Ahi1 immunoprecipitates identifies Cend1 (BM88) as a binding partner. Loss of Ahi1 reduces Cend1 levels in the hypothalamus; overexpressed Ahi1 stabilizes Cend1; and Cend1 overexpression rescues neurite extension defects in Ahi1-KO hypothalamic neurons. | PMID:23658157 | The Journal of neuroscience |
| 2013 | High | The Joubert syndrome-associated AHI1 missense mutation V443D (in a region with no known protein motifs) reduces AHI1 stability by 50%, causes aberrant localization of AHI1 at basal bodies and cell-cell junctions, and decreases AHI1 binding to NPHP1. Another JBTS-causing mutation, R351L, shows similar mislocalization. Primary cilia formation is decreased in fibroblasts from individuals with JBTS and AHI1 mutations. HAP1 has decreased binding to AHI1-V443D, but Hap1-deficient fibroblasts and neurons form primary cilia normally, indicating Hap1-Ahi1 binding is not critical for ciliary function. | PMID:23532844 | The Journal of biological chemistry |
| 2014 | High | Cby1 promotes Ahi1 recruitment to a ring-shaped domain (~250 nm) at the distal end of mature centrioles (centriole-cilium interface), as revealed by superresolution microscopy (3D-SIM and STED). The amount of centriole-localized Ahi1 (but not Ofd1) is reduced in Cby1-/- cells, indicating Cby1 is required for efficient recruitment of Ahi1 to the transition zone. | PMID:25103236 | Molecular biology of the cell |
| 2015 | High | C-terminal truncations of AHI1 (p.Arg1066* and p.Trp1088Leufs*16) are non-pathogenic when homozygous in humans — carriers do not manifest Joubert syndrome. Morpholinos against N-terminal zebrafish Ahi1 (orthologous to where human mutations cluster) produced ciliopathy phenotype, but targeting near the human C-terminal truncation sites did not, establishing that the C-terminal SH3 domain is dispensable for normal development and that pathogenicity requires disruption of N-terminal WD40-repeat-containing regions. | PMID:25616960 | Human molecular genetics |
| 2017 | Medium | AHI1 missense variants in the WD40 domain cause non-syndromic retinitis pigmentosa. Expression of mutant recombinant Jouberin in ciliated RPE cells shows significantly decreased enrichment at the ciliary base, without changes in overall ciliation percentage, cilium length, or IFT. 3D structure homology modeling predicts structural implications of WD40-domain missense variants. | PMID:28442542 | Journal of medical genetics |
| 2017 | Medium | Zebrafish ahi1lri46 (TALEN-generated) mutants develop shorter cone outer segments but normal rod morphology at 5 dpf; by 5 months, cone degeneration and rhodopsin mislocalization in rods occurs. The connecting cilium forms normally and Cc2d2a and Cep290 localize properly, indicating Ahi1 is required for disc morphogenesis and outer segment maintenance but not for basic connecting cilium formation. | PMID:28118669 | Investigative ophthalmology & visual science |
| 2018 | Medium | AHI1 loss in Ahi1-KO mice downregulates tyrosine hydroxylase (TH) in the midbrain. Rev-Erbα (a TH transcriptional repressor) and BMAL1 (Rev-Erbα transcriptional regulator) are upregulated in Ahi1-KO midbrains. AHI1 decreases BMAL1/Rev-Erbα expression by interacting with and repressing RORα (a nuclear receptor and circadian gene transcriptional regulator). Bmal1 deficiency reverses TH reduction caused by Ahi1 deficiency. Rev-Erbα inhibitor microinfusion into ventral midbrain of Ahi1-KO mice increases TH and improves depressive symptoms. | PMID:29449373 | The Journal of biological chemistry |
| 2019 | High | Deletion of Ahi1 in mouse embryonic fibroblasts (MEFs) reduces localization of Arl13b to the ciliary membrane (without changing total or membrane-associated Arl13b levels), decreases non-membrane-associated Arl13b stability via the proteasome pathway, decreases sonic hedgehog signaling, and causes abnormally elongated ciliary axoneme with increased ciliary IFT88. Ahi1-/- MEFs display defects in cell motility and Pdgfr-α-dependent migration. Exogenous Ahi1-GFP restores ciliary length, Arl13b ciliary recruitment, and Arl13b stability. | PMID:31391239 | Journal of cell science |
| 2019 | Medium | AHI1 physically interacts with APP (amyloid precursor protein) in mouse brain and transfected cells. AHI1 expression facilitates intracellular translocation of APP and inhibits APP amyloidogenic processing, reducing APP-CTFβ and secreted Aβ42. AHI1 is reduced in AD model cells (expressing Swedish/Indiana APP) and in 3xTg-AD mouse brain. AHI1-APP interaction enhances Erk activation and restores cell survival and differentiation. | PMID:31062249 | Molecular neurobiology |
| 2019 | High | Mutant Ahi1 lacking intact WD40 repeats (generated by morpholino or CRISPR/Cas9 truncation in zebrafish) causes retinal ganglion cell axon misprojection and ocular dysplasia, whereas ahi1 null zebrafish show normal RGC axon projection and ocular morphology, demonstrating that the aberrant retinal axon projection phenotype is caused by a toxic gain-of-function of truncated Ahi1 rather than loss of Ahi1. | PMID:30949029 | Frontiers in cellular neuroscience |
| 2021 | Medium | Ahi1 regulates the nuclear translocation of glucocorticoid receptor (GR): stress-mediated GR nuclear translocation reduces Ahi1 in stressed cells and mouse brains. Ahi1 interacts with GR to stabilize each other in the cytoplasm. Ahi1 deficiency promotes GR degradation in the cytoplasm and reduces GR nuclear translocation in response to stress. Ahi1-KO mice show hyposensitivity to antidepressants under stress. | PMID:33782379 | Translational psychiatry |
| 2021 | High | AHI1 regulates neuronal ciliary trafficking of melanin-concentrating hormone receptor 1 (MCHR1): loss of Ahi1 in mouse neurons significantly reduces MCHR1 in the ciliary membrane without affecting total or surface MCHR1 expression. Ahi1-/- neurons show decreased cAMP and ERK signaling upon MCH stimulation, demonstrating that ciliary localization of MCHR1 is necessary for its downstream signaling. | PMID:33741721 | The Journal of neuroscience |
| 2021 | Medium | Chronic stress induces abnormal nuclear translocation of Tet2. Ahi1 physically interacts with Tet2 (identified by Tet2 immunoprecipitation and mass spectrometry). Ahi1 knockout or knockdown causes accumulation of Tet2 in the cytosol. Reduction of Ahi1 protein under chronic stress explains Ahi1-dependent Tet2 nuclear translocation defects. | PMID:34218273 | Human molecular genetics |
| 2022 | High | AHI1 acts as a critical stabilizer of basal type-I interferon (IFN-I) signaling. Mechanistically, AHI1 recruits OTUD1 (a deubiquitinase) to deubiquitinate and stabilize Tyk2. AHI1 reduction (induced by depression-related AVP/arginine vasopressin) downregulates Tyk2 and IFN-I signaling activity in macrophages. AVP reduces AHI1 in macrophages, leading to attenuated antiviral immune response. | PMID:35821088 | Cell research |
| 2022 | Medium | Ahi1 regulates serotonin production via the GR/ERβ/TPH2 pathway: GR acts as a transcription factor that binds to the ERβ promoter glucocorticoid response elements and inhibits ERβ transcription. Ahi1 regulates GR nuclear translocation (established in prior work), thereby modulating the ERβ/TPH2 serotonin synthesis pathway. Brain E2 (17β-estradiol) levels decrease in male but not female Ahi1-KO mice, explaining sex differences in depressive behavior. | PMID:35643536 | Cell communication and signaling : CCS |
| 2023 | Medium | Mitochondrial Ahi1 and GR form a complex that, together with TFAM, regulates mtDNA copy number and brain ATP levels by binding to the D-loop control region of mitochondrial DNA. Loss of mitochondrial Ahi1/GR increases mtDNA copy numbers and decreases ATP levels. Regular exercise increases mitochondrial Ahi1/GR levels and improves depressive behavior in stressed but not Ahi1-KO mice. | PMID:36691038 | Cell communication and signaling : CCS |
| 2025 | Low | In CEP290-null photoreceptors, AHI1 (normally a transition zone protein) is abnormally restricted to the proximal connecting cilium rather than distributed throughout the transition zone, indicating that CEP290 is required for proper spatial distribution of AHI1 within the connecting cilium. | PMID:bio_10.1101_2025.01.20.633784 | bioRxiv |

## Citations

- PMID:12186888
- PMID:15322546
- PMID:15467982
- PMID:18636121
- PMID:18785627
- PMID:18936234
- PMID:19211505
- PMID:19625297
- PMID:20081859
- PMID:20592197
- PMID:20956301
- PMID:21959375
- PMID:22123816
- PMID:22623184
- PMID:23532844
- PMID:23658157
- PMID:25103236
- PMID:25616960
- PMID:28118669
- PMID:28442542
- PMID:29449373
- PMID:30949029
- PMID:31062249
- PMID:31391239
- PMID:33741721
- PMID:33782379
- PMID:34218273
- PMID:35643536
- PMID:35821088
- PMID:36691038
- PMID:bio_10.1101_2025.01.20.633784
