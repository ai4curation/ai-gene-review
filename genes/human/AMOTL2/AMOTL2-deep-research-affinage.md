---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMOTL2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9Y2J4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 24
citation_count: 24
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMOTL2 (human)

## Current model (mechanistic narrative)

AMOTL2 is a junctional scaffold protein that mechanically couples cadherin-based cell-cell junctions to the contractile actin cytoskeleton and the nuclear lamina, and acts as a regulatory hub for the Hippo and Wnt pathways governing cell shape, polarity, and proliferation [PMID:24806444, PMID:28842668, PMID:39195920]. At adherens junctions, the p100 AMOTL2 isoform forms complexes with VE-cadherin or E-cadherin that organize radial actin filaments, transmitting extracellular mechanical force through to the nuclear membrane; this coupling requires Par3 for junctional localization and drives lumen expansion, epithelial packing geometry, blastocyst hatching, and flow-induced endothelial alignment, with its loss in endothelium producing pro-inflammatory aortic aneurysm phenotypes [PMID:24806444, PMID:28790366, PMID:28842668, PMID:39195920]. AMOTL2 represses the transcriptional co-activators YAP/TAZ: it binds TAZ through a PPXY-WW interaction to control its nuclear translocation [PMID:23911299], and WWP1-mediated mono-ubiquitination at K347/K408 enables AMOTL2 to recruit LATS2 and SAV1 to promote YAP phosphorylation and cytoplasmic sequestration under high cell density [PMID:34404733], while it also stabilizes LATS1/2 to sustain YAP repression [PMID:38956029]. This YAP-repressive activity is switched off by mTORC2 phosphorylation at S760 and by CLK2-dependent alternative splicing that yields a membrane-uncoupled isoform [PMID:25998128, PMID:38126343]. AMOTL2 additionally attenuates Wnt signaling by trapping β-catenin in Rab11-positive recycling endosomes [PMID:22362771, PMID:34036399], and a hypoxia-induced p60 isoform sequesters Crb3/Par3 polarity complexes and uncouples p100 AMOTL2 from the actin-nuclear lamina axis to promote tumor invasion [PMID:25080976, PMID:37443716]. Through c-Src binding it facilitates membrane translocation and MAPK/ERK activation [PMID:17293535, PMID:21937427], and it modulates STAT1-dependent type I interferon signaling to restrict Zika virus replication [PMID:40892926].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005886 plasma membrane, GO:0005829 cytosol, GO:0005768 endosome, GO:0005856 cytoskeleton, GO:0005635 nuclear envelope
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-168256 Immune System, R-HSA-1643685 Disease
- **partners:** CDH5, CDH1, TAZ/WWTR1, YAP1, LATS2, CTNNB1, PPP2R2A, PARD3
- **complexes:** VE-cadherin adherens junction complex, E-cadherin/p100-AMOTL2/radial actin complex, LATS2/SAV1 Hippo complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | Medium | Amotl2 interacts preferentially with phosphorylated c-Src and facilitates its outward translocation to the membrane, regulating membrane architecture and F-actin organization; knockdown of amotl2 in zebrafish delays epiboly and impairs convergence/extension cell movements, and amotl2-deficient cells fail to migrate properly with loss of membrane protrusions. | PMID:17293535 | Development (Cambridge, England) |
| 2011 | High | Amotl2 promotes MAPK/ERK activation via c-Src in endothelial cells, dependent on phosphorylation of tyrosine residue at position 103 but independent of the C-terminal PDZ-binding domain; knockdown impairs endothelial cell proliferation, migration, polarity, and tube formation in vitro, and intersegmental vessel growth in zebrafish. | PMID:21937427 | The Journal of biological chemistry |
| 2012 | High | Amotl2 attenuates Wnt/β-catenin signaling by associating with and trapping β-catenin in Rab11-positive recycling endosomes, reducing the amount of β-catenin available in the cytosol and nucleus; knockdown in zebrafish causes embryonic dorsalization rescued by co-knockdown of β-catenin2. | PMID:22362771 | The Journal of biological chemistry |
| 2013 | Medium | AMOTL2 co-immunoprecipitates with TAZ via the WW domain of TAZ and the PPXY motif in the N-terminus of AMOTL2; AMOTL2 co-localizes with TAZ in the cytoplasm and regulates TAZ cytoplasm-to-nucleus translocation through direct protein-protein interaction, inhibiting TAZ-dependent transcription of surfactant genes in lung cells in a Hippo-independent manner. | PMID:23911299 | Gene |
| 2013 | Medium | Amotl2 interacts with the scaffold protein LL5β at synaptic podosomes in myotubes and neuromuscular junctions in vivo; depletion of Amotl2 in myotubes increases size of synaptic podosomes and alters postsynaptic topology, and depletion in fibroblasts disrupts invadopodia. | PMID:23525008 | Journal of cell science |
| 2014 | High | AmotL2 associates with the VE-cadherin adherens junction complex and couples it to contractile actin fibres; inactivation of amotL2 in zebrafish, mouse, and endothelial cell culture dissociates VE-cadherin from cytoskeletal tensile forces, impairing aortic vessel lumen expansion. | PMID:24806444 | Nature communications |
| 2014 | High | Hypoxic stress induces c-Fos-dependent expression of a p60 AmotL2 isoform; p60 AmotL2 interacts with the Crb3 and Par3 polarity complexes, retaining them in large vesicles and preventing them from reaching the apical membrane, causing loss of apical-basal polarity and promoting tumor invasion. | PMID:25080976 | Nature communications |
| 2015 | High | mTORC2 phosphorylates AMOTL2 at serine 760; phosphomimetic S760E mutation blocks AMOTL2's ability to bind and repress YAP, increasing YAP target gene expression, foci formation, and metastatic properties, whereas non-phosphorylatable S760A mutant retains YAP repression activity in glioblastoma cells and xenografts. | PMID:25998128 | The Journal of biological chemistry |
| 2017 | Medium | Par3 is essential for localization of AmotL2 to cellular junctions, where it associates with VE/E-cadherin to organize radial actin filaments; loss of this Par3-AmotL2-cadherin-actin axis impairs aortic lumen expansion and epithelial hexagonal packing. | PMID:28790366 | Scientific reports |
| 2017 | High | p100 AmotL2 forms a complex with E-cadherin that associates with radial actin filaments connecting cells across multiple layers; genetic inactivation of amotL2 leads to loss of contractile actin filaments and perturbed epithelial packing geometry; amotL2 is required for blastocyst hatching in mouse and zebrafish via tension generation, phenocopied by myosin II inhibitor blebbistatin. | PMID:28842668 | Scientific reports |
| 2020 | High | AMOTL2 is a binding partner of PPP2R2A (a PP2A regulatory subunit) in NSCLC cells; AMOTL2 binds PPP2R2A in the cytoplasm, reducing its nuclear localization and thereby preventing PPP2R2A-mediated dephosphorylation of JUN at Thr239, which suppresses AP-1-driven cell proliferation. | PMID:32950569 | Biochimica et biophysica acta. Molecular cell research |
| 2021 | High | E3 ubiquitin ligase WWP1 mono-ubiquitinates AMOTL2 at K347 and K408; mono-ubiquitinated AMOTL2 interacts with LATS2 and facilitates recruitment of SAV1, promoting YAP phosphorylation and cytoplasmic sequestration/degradation; this process is coupled to Crumbs polarity complex at cell junctions under high cell density conditions. | PMID:34404733 | Life science alliance |
| 2021 | Medium | AMOTL2 directly binds β-catenin and regulates its nuclear translocation in glioma cells; knockdown of AMOTL2 promotes β-catenin nuclear localization and downstream Wnt target gene expression, enhancing glioma proliferation, migration, and invasion. | PMID:34036399 | Oncology reports |
| 2021 | Medium | Loss of MAGI1 causes accumulation of E-cadherin and AMOTL2 and increased ROCK and p38 SAPK activities; rescue experiments show that AMOTL2 depletion or p38 inhibition reverses the increased tumorigenicity of MAGI1-deficient cells, placing AMOTL2 upstream of a ROCK/p38 stress pathway in luminal breast cancer. | PMID:33707576 | Scientific reports |
| 2021 | Medium | AMOTL2 restrains YAP1 activation in airway smooth muscle cells; overexpression of AMOTL2 suppresses TGF-β1-induced YAP1 nuclear translocation, and reactivation of YAP1 reverses AMOTL2-mediated suppression of proliferation and ECM deposition. | PMID:34323359 | Environmental toxicology |
| 2022 | Low | MEF2D binds the MEF2 cis-acting element in the upstream promoter region of AMOTL2, inhibiting its transcriptional expression, thereby activating YAP signaling and promoting HCC cell migration and proliferation. | PMID:35698637 | International journal of clinical and experimental pathology |
| 2023 | Medium | CLK2 inhibition promotes alternative splicing of AMOTL2 producing an exon-skipped isoform that can no longer associate with membrane-bound proteins, resulting in decreased YAP phosphorylation and decreased membrane localization of YAP, thereby activating YAP-driven transcription. | PMID:38126343 | eLife |
| 2023 | Medium | p60 AmotL2 (expressed in invading tumor cells) binds to the p100 AmotL2 isoform and uncouples the mechanical constraint of radial actin filaments from E-cadherin; the E-cadherin/p100AmotL2 complex is directly connected to the nuclear membrane, and p60AmotL2 expression inactivates this connection, altering nuclear lamina properties and potentiating ameboid invasion through extracellular matrix micropores. | PMID:37443716 | Cells |
| 2023 | High | AmotL2 connects junctional VE-cadherin and actin filaments to the nuclear lamina in endothelial cells; AmotL2 is essential for radial actin filament formation and endothelial cell alignment in response to blood flow; loss of endothelial AmotL2 in mice causes a pro-inflammatory response and abdominal aortic aneurysms. Molecular analysis showed VE-cadherin binds AmotL2 and actin, transmitting extracellular mechanical signals to the nuclear membrane. | PMID:39195920 | Nature cardiovascular research |
| 2024 | Medium | ARNTL2 negatively regulates AMOTL2 transcription by directly binding to the AMOTL2 promoter; reduced AMOTL2 decreases its recruitment and stabilization of LATS1/2 kinases, reducing LATS-dependent YAP phosphorylation and promoting YAP nuclear translocation and NPC invasion; inhibition of AMOTL2 counteracted the effect of ARNTL2 knockdown. | PMID:38956029 | Cell death & disease |
| 2024 | Low | WBP2 overexpression activates AMOTL2 and nuclear phosphorylated c-JUN in breast cancer cells; AMOTL2 knockdown reduces drug-resistance protein expression caused by WBP2 overexpression, placing AMOTL2 as a mediator in the ITCH/WBP2/AMOTL2/c-JUN chemoresistance axis. | PMID:39709035 | Biochemical pharmacology |
| 2025 | Medium | AMOTL2 is identified as a direct cellular target of celastrol by activity-based protein profiling (ABPP); celastrol-AMOTL2 binding activates the Hippo pathway, promoting YAP1 phosphorylation and degradation; AMOTL2 knockdown attenuates celastrol-induced cardiomyocyte apoptosis by enhancing YAP1 expression and mitochondrial biogenesis. | PMID:41412440 | Chemico-biological interactions |
| 2025 | Medium | AMOTL2 inhibits Zika virus replication by promoting the host type I interferon response; AMOTL2 modulates STAT1 levels and activation in response to type I IFN, promoting downstream expression of interferon-stimulated genes. | PMID:40892926 | Proceedings of the National Academy of Sciences of the United States of America |
| 2025 | Medium | AmotL2 maintains junctional architecture, actomyosin tension, and appropriate cell packing in endothelial cells; loss of AmotL2 disrupts tension homeostasis, increases tissue compaction, and prevents vascular branch regression (pruning) despite normal perfusion in zebrafish; Yap1 plays an opposing stabilizing role, and AmotL2 and Yap1 together constitute a mechanosensitive balancing module for flow-guided vascular remodeling. | PMID:bio_10.1101_2025.11.19.689183 | bioRxiv |

## Citations

- PMID:17293535
- PMID:21937427
- PMID:22362771
- PMID:23525008
- PMID:23911299
- PMID:24806444
- PMID:25080976
- PMID:25998128
- PMID:28790366
- PMID:28842668
- PMID:32950569
- PMID:33707576
- PMID:34036399
- PMID:34323359
- PMID:34404733
- PMID:35698637
- PMID:37443716
- PMID:38126343
- PMID:38956029
- PMID:39195920
- PMID:39709035
- PMID:40892926
- PMID:41412440
- PMID:bio_10.1101_2025.11.19.689183
