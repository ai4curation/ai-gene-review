---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/PKM
affinage_run_date: 2026-06-10T06:43:35
uniprot_accession: P14618
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 40
citation_count: 40
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for PKM (human)

## Current model (mechanistic narrative)

PKM (PKM2 isoform) is a multifunctional glycolytic pyruvate kinase whose tetrameric form drives metabolic flux but whose dimeric/monomeric forms acquire non-canonical activities upon translocation to the nucleus, coordinating metabolism with gene expression, cell-cycle control, and inflammation [PMID:22056988, PMID:24316223]. The interconversion between oligomeric states is the central regulatory switch: tetramerization favors enzymatic pyruvate kinase activity, whereas dimer/monomer formation favors nuclear functions, and this balance is tuned by an extensive set of post-translational modifications including lactylation at K62 [PMID:36439872], palmitoylation at C31 [PMID:39665133], glutathionylation at Cys423/424 [PMID:36815040], sumoylation [PMID:36116159], and several ubiquitin linkages [PMID:40079144]. In the nucleus, PKM2 acts as a co-transcriptional activator that binds c-Src-phosphorylated β-catenin to drive CCND1 transcription [PMID:22056988], and phosphorylates histone H3 at T11 to evict HDAC3 and activate cyclin D1 and c-Myc [PMID:22901803, PMID:36899022]. During mitosis it phosphorylates the spindle-checkpoint protein Bub3 at Y207 to ensure correct kinetochore-microtubule attachment [PMID:24316223], and during cytokinesis Aurora-B-primed PKM2 phosphorylates MLC2 at Y118 at the contractile ring [PMID:25412762]; it also moonlights as a PEP-dependent histidine kinase phosphorylating PGAM1 at H11 [PMID:38750259]. Nuclear PKM2 additionally functions as a non-canonical RNA-binding protein that occupies RNA G-quadruplex structures in pre-mRNAs to promote their expression and cancer cell invasion [PMID:39153475], and binds ribosomes in a PARylation- and ADP-dependent manner to stall translation [PMID:37224531]. Through nuclear partnership with STAT3 and NF-κB, PKM2 controls Th17 differentiation, macrophage and neutrophil inflammatory programs, and tumor angiogenesis [PMID:32697823, PMID:34529778, PMID:33314660]. PKM2 abundance is governed by chaperone-mediated autophagy following K305 acetylation or Jmjd4-catalyzed K66 hydroxylation [PMID:22096030, PMID:37066795]. An in vitro reconstitution study using [32P]-PEP failed to detect PKM2-dependent protein kinase activity, defining a point of contention over the protein-kinase model [PMID:26300261].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0140110 transcription regulator activity, GO:0003723 RNA binding, GO:0016740 transferase activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005739 mitochondrion, GO:0005840 ribosome, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-74160 Gene expression (Transcription), R-HSA-168256 Immune System, R-HSA-1640170 Cell Cycle, R-HSA-8953854 Metabolism of RNA, R-HSA-9612973 Autophagy, R-HSA-8953897 Cellular responses to stimuli
- **partners:** CTNNB1, STAT3, MFN2, PHGDH, PGAM1, MARCH2, ANXA5, FSTL1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | EGFR activation induces translocation of PKM2 (but not PKM1) into the nucleus, where K433 of PKM2 binds to c-Src-phosphorylated Y333 of β-catenin. This PKM2–β-catenin interaction is required for recruitment to the CCND1 promoter, HDAC3 removal, histone H3 acetylation, and cyclin D1 expression, thereby promoting tumor cell proliferation. | PMID:22056988 | Nature |
| 2012 | High | Nuclear PKM2 directly binds histone H3 and phosphorylates it at T11 upon EGF receptor activation. This phosphorylation causes dissociation of HDAC3 from the CCND1 and MYC promoters, leading to H3K9 acetylation and transcriptional activation of cyclin D1 and c-Myc, promoting cell-cycle progression and tumorigenesis. | PMID:22901803 | Cell |
| 2013 | High | PKM2 (but not PKM1) binds the spindle checkpoint protein Bub3 during mitosis and phosphorylates Bub3 at Y207. This phosphorylation is required for Bub3-Bub1 complex recruitment to kinetochores, correct kinetochore-microtubule attachment, mitotic/spindle-assembly checkpoint fidelity, and accurate chromosome segregation. | PMID:24316223 | Molecular cell |
| 2014 | High | Aurora B phosphorylates PKM2 (but not PKM1) at T45, which is required for PKM2 localization to the contractile ring during cytokinesis. PKM2 then phosphorylates MLC2 at Y118, priming ROCK2 binding to MLC2 and subsequent ROCK2-dependent MLC2 S15 phosphorylation, driving cytokinesis completion and cell proliferation. | PMID:25412762 | Nature communications |
| 2011 | Medium | Acetylation of PKM2 at Lys305 decreases its pyruvate kinase activity and targets it for chaperone-mediated autophagy and subsequent lysosomal degradation. | PMID:22096030 | Cold Spring Harbor symposia on quantitative biology |
| 2015 | High | Using [32P]-phosphoenolpyruvate (PEP) with recombinant enzyme and PKM2-deleted in vitro systems, no PKM2-dependent protein kinase activity was detected; labeled protein species required ADP and were not PKM2-dependent, and direct phosphate transfer from ATP to protein by PKM2 was not observed. This constitutes a NEGATIVE finding challenging PKM2 protein kinase activity. | PMID:26300261 | Molecular cell |
| 2016 | High | PKM2-mediated glycolysis promotes NLRP3 and AIM2 inflammasome activation in macrophages by modulating EIF2AK2 phosphorylation. Myeloid cell-specific conditional knockout of PKM2 attenuates inflammasome activation and protects mice from lethal endotoxemia and polymicrobial sepsis. | PMID:27779186 | Nature communications |
| 2019 | Medium | PKM2 interacts with mitofusin 2 (MFN2) to promote mitochondrial fusion and oxidative phosphorylation while attenuating glycolysis. mTOR modulates this interaction by phosphorylating MFN2, establishing an mTOR-MFN2-PKM2 signaling axis that coordinates glycolysis and OXPHOS. | PMID:30887444 | Protein & cell |
| 2020 | High | PKM2 translocates into the nucleus in Th17 cells and interacts with STAT3, enhancing STAT3 activation and thereby promoting Th17 cell differentiation. T cell-specific PKM2 deletion impairs Th17 differentiation and ameliorates experimental autoimmune encephalomyelitis, independent of effects on metabolic reprogramming or proliferation. | PMID:32697823 | The Journal of experimental medicine |
| 2022 | Medium | Lactylation of PKM2 at K62 inhibits its tetramer-to-dimer transition, thereby promoting its pyruvate kinase activity and reducing nuclear distribution, which suppresses the Warburg effect and promotes transition of pro-inflammatory macrophages toward a reparative phenotype. | PMID:36439872 | International journal of biological sciences |
| 2020 | Medium | PKM2 regulates the cardiomyocyte cell cycle and reduces oxidative stress through anabolic pathways and β-catenin. Cardiomyocyte-specific Pkm2 deletion during cardiac development reduces cardiomyocyte cell cycle activity, cardiomyocyte numbers, and myocardial size. | PMID:32078387 | Circulation |
| 2023 | High | PHGDH prevents PKM2 K305 acetylation (catalyzed by PCAF) and subsequent autophagic degradation by directly interacting with PKM2. PHGDH also facilitates p300-catalyzed PKM2 K433 acetylation, which promotes PKM2 nuclear translocation and enables it to phosphorylate H3T11, regulating transcription of senescence-associated genes. | PMID:36899022 | Nature communications |
| 2023 | High | Jmjd4 interacts with Hsp70 to mediate degradation of Pkm2 through chaperone-mediated autophagy, dependent on Jmjd4-catalyzed hydroxylation of K66 of Pkm2. Loss of Jmjd4 in cardiomyocytes leads to Pkm2 accumulation, impaired mitochondrial respiration, and spontaneous dilated cardiomyopathy. | PMID:37066795 | Circulation |
| 2024 | Medium | SIRT1 interacts with and deacetylates PKM2 at K135 and K206, leading to reduced PKM2 enzymatic activity and lactate production, which decreases glial activation in the brain and ameliorates Parkinson's disease phenotypes. | PMID:39128469 | Cell reports. Medicine |
| 2024 | High | PKM2 moonlights as a histidine kinase in a phosphoenolpyruvate (PEP)-dependent manner to catalyze PGAM1 H11 phosphorylation, which is essential for PGAM1 activity. Monomeric and dimeric PKM2 (but not tetrameric) efficiently phosphorylate PGAM1. Src-catalyzed PGAM1 Y119 phosphorylation is a prerequisite for PKM2 binding and subsequent H11 phosphorylation. | PMID:38750259 | The EMBO journal |
| 2024 | High | Nuclear PKM2 functions as a non-canonical RNA-binding protein that specifically interacts with folded RNA G-quadruplex (rG4) structures in precursor mRNAs. PKM2 occupancy at rG4s prevents binding of repressive RBPs (e.g., HNRNPF) and promotes expression of rG4-containing pre-mRNAs. Preventing nuclear PKM2 accumulation represses the rG4ome and reduces cancer cell migration and invasion. | PMID:39153475 | Molecular cell |
| 2023 | High | PKM binds ribosomes in a poly-ADP ribosylation (PARylation)-dependent manner. PKM crosslinks to mRNA sequences downstream of lysine- and glutamate-encoding regions and causes translational stalling near these sequences. PKM-polysome interaction is regulated by ADP levels, linking carbohydrate metabolism to mRNA translation regulation. | PMID:37224531 | Nucleic acids research |
| 2022 | Medium | FSTL1 binds directly to PKM2 through its FK domain, promotes PKM2 phosphorylation and nuclear translocation, and reduces PKM2 ubiquitination, thereby enhancing PKM2-dependent glycolysis and macrophage M1 polarization, promoting liver fibrosis. | PMID:35140065 | Gut |
| 2020 | Medium | Annexin A5 directly interacts with PKM2 at ASP101, LEU104, and ARG106, inhibits phosphorylation of Y105, and promotes PKM2 tetramer formation, thereby switching macrophage metabolism from glycolysis to oxidative phosphorylation and promoting M2 polarization. | PMID:32863213 | Redox biology |
| 2022 | High | PKM2 regulates post-ischemic inflammation in peripheral neutrophils by promoting STAT3 phosphorylation. Myeloid cell-specific PKM2 deletion reduced neutrophil extracellular traps, cerebral thrombo-inflammation, and infarct volume after stroke. Inhibiting PKM2 nuclear translocation pharmacologically reduced neutrophil hyperactivation. | PMID:34529778 | Blood |
| 2022 | Medium | GTPBP4 facilitates SUMO1-mediated sumoylation of PKM2, which promotes PKM2 dimer formation and aerobic glycolysis. Sumoylated PKM2 relocates from cytoplasm to nucleus, activating EMT and STAT3 signaling in hepatocellular carcinoma. | PMID:36116159 | Redox biology |
| 2021 | Medium | Extracellular PKM2 (EcPKM2) secreted by myofibroblasts interacts with integrin αvβ3 on myofibroblast surfaces to activate FAK-PI3K signaling, which activates NF-κB survival pathway (preventing apoptosis) and suppresses PTEN to upregulate arginase-1, facilitating proline biosynthesis and collagen production in organ fibrosis. | PMID:34693222 | iScience |
| 2022 | Medium | Celastrol binds covalently to Cys424 of PKM2, inhibiting its enzymatic activity and suppressing aerobic glycolysis (Warburg effect) in macrophages, thereby attenuating inflammatory responses in sepsis. | PMID:35596191 | Military Medical Research |
| 2022 | High | PKM2-C31 palmitoylation (mediated by palmitoyl acyltransferase zDHHC13) impairs PKM2 tetramerization, inhibits its pyruvate kinase activity and endothelial glycolysis, causing palmitic acid-induced endothelial injury and cardiovascular dysfunction. PKM2-C31S mutation prevents these effects. | PMID:39665133 | Advanced science |
| 2022 | Medium | Prohibitin 2 (PHB2), through its C-terminus, directly interacts with hnRNPA1 (a key modulator of PKM alternative splicing) to counteract hnRNPA1-mediated PKM2 expression and glycolysis, thereby maintaining the contractile VSMC phenotype. | PMID:36200440 | Circulation research |
| 2025 | Medium | PINK1 phosphorylates PKM2 at Ser127, preserving its active tetrameric form and inhibiting its nuclear translocation and interaction with β-catenin, resulting in a metabolic shift toward energy production. SIRT3 deacetylates PINK1 to promote this pathway (SIRT3-PINK1-PKM2 axis) protecting against osteoarthritis. | PMID:40087281 | Bone research |
| 2022 | Medium | DEUBIQUITINASE JOSD2 interacts with PKM2 and reduces its K433 acetylation, thereby blocking PKM2 nuclear localization and downstream non-glycolytic gene expression in acute myeloid leukemia, without affecting PKM2 protein stability. | PMID:35836282 | Experimental hematology & oncology |
| 2025 | Medium | March2 promotes K33-linked polyubiquitination of PKM2, facilitating PKM2 dimer-to-tetramer conversion. Deficiency of March2 lessens PKM2 tetramerization, promotes glycolysis-derived H3K18 lactylation, and drives p53-dependent apoptotic transcription, accelerating aortic aneurysm/dissection pathogenesis. | PMID:40079144 | Circulation research |
| 2025 | Medium | PKM2-derived pyruvate is converted to lactate, which lactylates histone H3 at K9 (H3K9la), upregulating Sox family transcription factors through epigenetic modification to control cochlear development. PKM2 deletion causes a metabolic switch from glycolysis to OXPHOS and impairs cochlear sensory epithelium morphogenesis. | PMID:39773029 | Proceedings of the National Academy of Sciences of the United States of America |
| 2025 | Medium | Tetrameric PKM2 (promoted by TEPP-46) increases ATP production from glycolysis; extracellular ATP is converted to adenosine via ectonucleotidases, activating adenosine receptor A2a (A2aR) to enhance IL-10 production in macrophages. This effect is abolished in PKM2-deficient macrophages. | PMID:39772395 | Cell reports |
| 2022 | Medium | PKM2 dimerization is induced by PKM2 sumoylation (via GTPBP4-SUMO1-UBA2 axis), and dimeric PKM2 promotes aerobic glycolysis and nuclear translocation. Separately, PKM2 nuclear translocation is required for complex formation with STAT3, HIF1α-mediated angiogenesis, and tumor maintenance in bladder cancer. | PMID:34903602 | Cancer research |
| 2022 | Medium | Dimeric/monomeric PKM2 nuclear translocation is promoted by ROS-induced oxidation at Cys423/Cys424, leading to glutathionylation of PKM2. Nuclear PKM2 then acts as a co-factor to promote HIF-1α-dependent gene induction, contributing to cardioprotective adaptive responses. | PMID:36815040 | Acta pharmaceutica Sinica. B |
| 2024 | Medium | PKM2 aggregates form in senescent cells and organs from aged mice, impairing PKM2 enzymatic activity and glycolytic flux, thereby driving cells into senescence. Small molecules capable of dissolving PKM2 aggregates alleviate senescence and extend lifespan in mouse models. | PMID:38982055 | Nature communications |
| 2021 | Medium | PKM2 interacts with NF-κB and induces nuclear translocation of both PKM2 and NF-κB with assistance of importin 4. In the nucleus, PKM2-NF-κB complexes augment VEGFA transcription, promoting tumor angiogenesis. FBP promotes assembly of a FOXM1D-PKM2 heterooctamer that reduces PKM2 metabolic activity. | PMID:33314660 | Molecular oncology |
| 2022 | Medium | CXCL12 signaling through CXCR4 and ACKR3 stimulates protein interactions among β-arrestin 2, PKM2, and ERK2, leading to dissociation of PKM2 from β-arrestin 2, reduced PKM2 oligomerization (tetramers to dimers/monomers), and increased glycolytic intermediates and pentose phosphate pathway metabolites. | PMID:35681470 | Cells |
| 2021 | Medium | PKM2 interacts with Oct4 in glioma stem cells, and this interaction is implicated in the regulation of glioma stemness. Silencing PKM2 enhances apoptosis and differentiation of glioma spheroids. DCA (a PDK inhibitor) increases PKM2/Oct4 complex formation and inhibits Oct4-dependent gene expression. | PMID:24481450 | Cell death & disease |
| 2021 | Low | PKM2 promotes IL-10 production via tetramerization-dependent ATP release and adenosine signaling, and PKM2 mediates autophagic activation by increasing phosphorylation of Beclin-1 in NPM1-mutated AML cells, contributing to cell survival. | PMID:30906218 | International journal of biological sciences |
| 2021 | Medium | PKM2 regulates lipid homeostasis through an ER transmembrane protein TMEM33. Loss of PKM2 upregulates TMEM33, which recruits E3 ligase RNF5 to promote SCAP degradation. TMEM33 is transcriptionally regulated by NRF1, whose cleavage is controlled by PKM2 levels. | PMID:34487377 | The EMBO journal |
| 2022 | Medium | Vitamin B5 (pantothenate) is catabolized to coenzyme A (CoA) in a PANK-dependent manner, and CoA binds directly to PKM2, impeding its phosphorylation and nuclear translocation, thus inhibiting glycolysis and STAT3 phosphorylation, and suppressing Th17 cell differentiation. | PMID:36450257 | Cell reports |
| 2024 | Medium | Mannose directly binds PKM2, inhibiting its enzymatic activity and reducing lactate production, leading to decreased PKM2 lactylation and increased PKM2 acetylation, which causes nuclear translocation of PKM2 and NF-κB pathway activation, inducing NLRP1/Caspase-1/GSDMD/IL-1β-dependent pyroptosis in bladder cancer. | PMID:40312519 | Communications biology |

## Citations

- PMID:22056988
- PMID:22096030
- PMID:22901803
- PMID:24316223
- PMID:24481450
- PMID:25412762
- PMID:26300261
- PMID:27779186
- PMID:30887444
- PMID:30906218
- PMID:32078387
- PMID:32697823
- PMID:32863213
- PMID:33314660
- PMID:34487377
- PMID:34529778
- PMID:34693222
- PMID:34903602
- PMID:35140065
- PMID:35596191
- PMID:35681470
- PMID:35836282
- PMID:36116159
- PMID:36200440
- PMID:36439872
- PMID:36450257
- PMID:36815040
- PMID:36899022
- PMID:37066795
- PMID:37224531
- PMID:38750259
- PMID:38982055
- PMID:39128469
- PMID:39153475
- PMID:39665133
- PMID:39772395
- PMID:39773029
- PMID:40079144
- PMID:40087281
- PMID:40312519
