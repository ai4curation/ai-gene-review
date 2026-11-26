---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABI1
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q8IZP0
self_evaluation_pairwise: win
faith_pct: 88.88888888888889
n_discoveries: 51
citation_count: 50
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABI1 (human)

## Current model (mechanistic narrative)

ABI1 (Abelson interactor 1/E3B1) is a multivalent cytoskeletal scaffold that couples Rho-family GTPase and tyrosine-kinase signaling to Arp2/3-dependent actin polymerization at protrusive structures [PMID:10499589, PMID:15048123]. Its central function is to nucleate and stabilize the WAVE regulatory complex: ABI1 binds the WHD domain of WAVE2 and an N-terminal WAVE-binding domain of WAVE1 to stimulate WAVE-mediated actin polymerization and assemble the WAVE2-NAP1-PIR121 complex, and Abi1 loss in mice destabilizes WAVE1/WAVE2/NAP1/Sra-1, abolishes lamellipodial protrusion, and causes embryonic lethality with heart and brain malformations [PMID:15048123, PMID:15143189, PMID:21482783]. In parallel, ABI1 acts as the scaffold of an EPS8-ABI1-SOS1 tri-complex (SH3 domain binding SOS1, proline-rich/PxxDY region binding EPS8) that, upon recruitment of the PI3K p85 subunit and PIP3, exhibits Rac-specific GEF activity downstream of Ras to drive actin remodeling [PMID:10499589, PMID:12515821, PMID:31488087]. ABI1 also directly activates N-WASP cooperatively with Cdc42 to govern actin-based vesicular transport, EGFR endocytosis, and macropinocytosis, functions distinct from its WAVE-dependent membrane protrusion role [PMID:16155590]. ABI1 allosterically regulates c-Abl: phospho-Y213 binds the Abl SH2 domain in trans while a proximal PXXP motif engages the Abl SH3 domain, and ABI1 reciprocally bridges c-Abl to WAVE2 phosphorylation [PMID:18328268, PMID:26428302]. Its activity is gated by post-translational control including CDK1/cyclin B phosphorylation at S216 at mitosis, CaMKIIα phosphorylation at S88, and PTEN-mediated Y213/S216 dephosphorylation that triggers calpain-dependent degradation and reorganizes the actin cytoskeleton during epithelial polarization [PMID:21900237, PMID:22993434, PMID:32673396]. Alternative splicing of exon 10 produces isoforms with opposite Rac1-binding and macropinocytosis behavior [PMID:20479892]. Beyond actin, synaptically stimulated ABI1 translocates to the nucleus in an Abl-dependent manner to co-activate Myc/Max E-box transcription and shapes dendritic spine and synapse maturation [PMID:17304222]. Loss of ABI1 in hematopoietic cells causes a myeloproliferative/myelofibrosis-like disease through derepressed SFK/STAT3/NF-κB signaling, and ABI1 loss promotes EMT, while ABI1 is a fusion partner of MLL in acute myeloid leukemia [PMID:9694699, PMID:30213875, PMID:31530281].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-1266738 Developmental Biology, R-HSA-1643685 Disease
- **partners:** WAVE2, EPS8, SOS1, ABL1, WASL, PIK3R1, ITGA4, SHANK3
- **complexes:** WAVE regulatory complex (WAVE2-ABI1-NAP1-PIR121), EPS8-ABI1-SOS1 tri-complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | Medium | E3B1/ABI1 was identified as a binding partner of the EPS8 SH3 domain and the ABL SH3 domain in vitro, and associates with EPS8 in vivo; the protein exists as multiple phosphoserine-containing isoforms (65, 68, 72 kDa) whose hyperphosphorylation is induced by EGF stimulation. | PMID:9010225 | Oncogene |
| 1999 | High | EPS8 and E3B1/ABI1 transduce signals from Ras to Rac by forming a tri-complex with SOS-1 that exhibits Rac-specific GEF activity in vitro, placing ABI1 as an essential scaffold in the Ras→Rac signaling axis. | PMID:10499589 | Nature |
| 1998 | Medium | ABI1 (human ABI-1) was identified as a fusion partner of MLL in acute myeloid leukemia with t(10;11)(p11.2;q23); the MLL-ABI1 fusion combines MLL AT-hook/DNA methyltransferase homology domains with ABI1's homeodomain homology region, polyproline stretches, and SH3 domain. | PMID:9694699 | Blood |
| 2000 | Low | Abi-1 and Abi-2 proteins are expressed in the developing nervous system, are concentrated in synaptosomes and growth cone particles, and their phosphorylation state changes with age in brain lysates, consistent with participation in Abl kinase signaling at neuronal structures. | PMID:10995551 | Molecular and cellular neurosciences |
| 2000 | Medium | ABI-1 SH3 domain interacts with ENL (an MLL fusion partner) via an internal ENL region; the interaction was confirmed by yeast two-hybrid, far-Western blot, GST pulldown, and co-immunoprecipitation. | PMID:10777208 | Oncogene |
| 2003 | High | PI3K (via its p85 regulatory subunit) is recruited by ABI1 into the EPS8-ABI1-SOS1 complex; PIP3 (the PI3K catalytic product) and p85 recruitment cooperate to unmask the Rac-GEF activity of the complex in vitro and are required for Rac activation and actin remodeling in vivo. | PMID:12515821 | The Journal of cell biology |
| 2004 | High | ABI1 directly interacts with the WHD domain of WAVE2, stimulates WAVE2-mediated actin polymerization activity in vitro, and mediates assembly of the WAVE2-ABI1-NAP1-PIR121 complex; RNAi knockdown of ABI1 abrogates Rac-dependent lamellipodia protrusion in vivo. | PMID:15048123 | Nature cell biology |
| 2004 | Medium | ABI1 binds WAVE1 through an amino-terminal WAVE-binding (WAB) domain; disruption of this interaction prevents ABI1 from reaching lamellipodia tips and reduces WAVE1 protein levels in fibroblasts lacking one Abi1 allele and null for Abi2, an effect rescued by Abi1 constructs retaining WAVE1 binding. ABI1 also contains an overlapping SNARE domain that interacts with Syntaxin-1 and undergoes leptomycin B-sensitive nucleocytoplasmic shuttling. | PMID:15143189 | Molecular and cellular biology |
| 2005 | High | ABI1 binds N-WASP with nanomolar affinity and, cooperating with Cdc42, potently induces N-WASP actin polymerization activity in vitro. ABI1 and WAVE are both required for Rac-dependent membrane protrusion and macropinocytosis, whereas ABI1 and N-WASP (but not WAVE) regulate actin-based vesicular transport, EGFR endocytosis, and receptor surface distribution. | PMID:16155590 | Nature cell biology |
| 2005 | Low | Eps8 promotes actin filopodia-like structures; interaction with ABI1 modulates actin architecture toward cables and star-like structures, and the Eps8/ABI1 complex recruits N-WASP to regulate actin nucleator localization/activity. | PMID:16225669 | BMC cell biology |
| 2005 | Medium | In response to CSF-1, WAVE2 and ABI1 form a stable complex in macrophages and are co-recruited to F-actin-rich protrusions; knockdown of either WAVE2 or ABI1 by RNAi impairs CSF-1-induced membrane protrusions and macrophage migration. | PMID:16280551 | Journal of cell science |
| 2006 | Low | ABI1 interacts with betaPIX (a Rac1 GEF) via its C-terminal region in vitro and via N-terminal region in vivo; co-expression of ABI1 with truncated betaPIX blocks PDGF-induced dorsal membrane ruffle formation. | PMID:16940963 | Cell research |
| 2007 | Medium | ABI1 is localized in neurites, growth cones, and later enriched in dendritic spines and PSDs. It co-immunoprecipitates with the ProSAP2/Shank3 scaffold and with Eps8/SOS1. Upon NMDA stimulation, ABI1 translocates from PSDs to nuclei in an Abl kinase-dependent manner, where it associates with Myc/Max transcription factor complex and enhances E-box-regulated gene transcription. Knockdown causes excessive dendritic branching and immature spine/synapse morphology. | PMID:17304222 | The EMBO journal |
| 2007 | Medium | Chlamydia trachomatis infection promotes Rac interaction with WAVE2 and ABI1 (but not IRSp53) as shown by co-immunoprecipitation; siRNA depletion of WAVE2 or ABI1 abrogates chlamydia-induced actin recruitment and significantly reduces uptake. | PMID:17501982 | Cellular microbiology |
| 2007 | Medium | Abi-1 forms an EGF-inducible complex with the Cbl ubiquitin ligase; an Abi-1 mutant lacking the SH3 domain fails to interact with Cbl, inhibits EGFR internalization, and prevents Cbl membrane accumulation after EGF. Oncogenic Abl disrupts the EGF-inducible Abi-1/Cbl complex. | PMID:17395426 | Cellular signalling |
| 2008 | High | Phosphotyrosine pY213 of ABI1 allosterically inhibits nonmyristoylated c-Abl kinase in trans by concurrent binding of pY213 to the Abl SH2 domain and a proximal PXXP motif to the Abl SH3 domain; wild-type ABI1 (but not Y213F mutant) inhibits Abl pY412 autophosphorylation in vivo. | PMID:18328268 | Biochimica et biophysica acta |
| 2009 | Medium | In C. elegans, ABI-1 interacts with the UNC-53/NAV2 scaffolding protein via a restricted calponin homology (CH) domain of UNC-53; ABI-1 and UNC-53 share overlapping expression and similar cell-migration phenotypes, and ABI-1 links UNC-53 to the ARP2/3 complex for actin remodeling during cell migration. | PMID:19168673 | Development |
| 2010 | Medium | ABI1 isoform 3 (lacking exon 10) constitutively activates Rac1 and promotes macropinocytosis; isoform 2 (containing exon 10) preferentially binds activated Rac1 via an exon-10 site, suppresses macropinocytosis, and is more cytoplasmic. Both isoforms bind inactive Rac1 through a non-exon-10 site. | PMID:20479892 | PloS one |
| 2010 | Medium | ABI1 pY213 links Abl kinase signaling to the p85 regulatory subunit of PI3K: phosphorylation of Y213 is required for Abl to regulate macropinocytosis, and pY213 interacts with the C-terminal SH2 domain of p85. | PMID:20598684 | FEBS letters |
| 2010 | Medium | Dysbindin-1 interacts with WAVE2 (but not N-WASP) and with ABI1, and dysbindin-1 promotes the WAVE2-ABI1 interaction; the three proteins form a ternary complex. RNAi knockdown of dysbindin-1 produces abnormally elongated immature dendritic protrusions, phenocopying ABI1 loss. | PMID:20531346 | Molecular psychiatry |
| 2010 | Medium | Integrity of the SOS1/EPS8/ABI1 tri-complex is essential for LPA-induced Rac activation, cell migration, and peritoneal metastatic colonization of ovarian cancer cells; ABI1 acts as the scaffold holding SOS1 and EPS8 together in the complex. | PMID:21118970 | Cancer research |
| 2010 | High | Abi1 directly binds the α4 integrin cytoplasmic tail (confirmed by purified protein binding assay), colocalizes with phosphorylated α4 at the leading edge, and Abi1-deficient cells expressing α4 have impaired cell spreading rescued by wild-type but not α4-binding-deficient Abi1. | PMID:21173240 | Proceedings of the National Academy of Sciences |
| 2011 | High | Abi1 knockout in mice causes embryonic lethality (~E11.5) with heart and brain malformations. Abi1-KO cells show reduced WAVE1, WAVE2, NAP1, and Sra-1/PIR121 levels, decreased migration rate and distance, and decreased dorsal ruffling, demonstrating that Abi1 is critical for WAVE complex integrity and stability. | PMID:21482783 | Proceedings of the National Academy of Sciences |
| 2011 | High | CDK1/cyclin B phosphorylates ABI1 at serine 216 at mitotic entry, and this phosphorylation attenuates Bcr-Abl-induced tyrosine phosphorylation of the WAVE complex and F-actin assembly; phosphomimetic S216D mutation in ABI1 is sufficient to recapitulate this attenuation and interferes with cell cycle progression. | PMID:21900237 | The Journal of biological chemistry |
| 2011 | Medium | Abi1 knockdown by shRNA in Bcr-Abl-transformed cells attenuates abnormal actin remodeling, inhibits cell adhesion and migration on fibronectin, and impairs leukemogenesis in NOD/SCID mice; Abi1 silencing also attenuates Bcr-Abl-stimulated activation of Lyn (Src family kinase). | PMID:18453543 | Carcinogenesis |
| 2011 | Medium | Abi-1 and CaMKIIα interact at resting conditions through Abi1's tSNARE domain (which has homology to CaMKIIα regulatory domain); this interaction mutually inhibits both proteins including Abi1-dependent Rac activation. Glutamate receptor activation causes calmodulin binding leading to dissociation; CaMKIIα phosphorylates Abi1 at serine 88 prior to dissociation, contributing to Rac activation and spine maturation. | PMID:22993434 | The Journal of neuroscience |
| 2011 | Low | An SK3 channel/nWASP/Abi-1 trimeric complex is present in neural stem cells and postsynaptic compartments; SK3 and nWASP act synergistically to induce filopodial outgrowth, while Abi-1 acts antagonistically to these partners to regulate neurite outgrowth. | PMID:21464958 | PloS one |
| 2011 | Low | hnRNPK interacts with the Abi-1 SH3 domain through the hnRNPK KI domain; knockdown of hnRNPK phenocopies Abi-1 knockdown (enlarged dendritic tree, increased filopodia, decreased mature synapses), indicating synergistic function in a multiprotein complex regulating spine/filopodia balance. | PMID:22102872 | PloS one |
| 2012 | Medium | C. elegans ABI-1 SH3 domain directly binds MIG-10 (lamellipodin); epistasis analysis places ABI-1 and WVE-1 downstream of MIG-10 to mediate axon guidance in both UNC-6 (netrin) and SLT-1 (slit) pathways; this ABI-1/MIG-10 interaction also promotes lamellipodia formation in cultured mammalian cells. | PMID:23209429 | PLoS genetics |
| 2012 | Medium | MIG-10B isoform interacts with ABI-1 to organize the actin cytoskeleton at presynaptic sites and instruct synaptic vesicle clustering through Synapsin-1 (SNN-1) downstream of Netrin; a dominant-negative MIG-10B construct expressing a specific N-terminal domain disrupts vesicle clustering and thermotaxis behavior in vivo. | PMID:23028145 | Genes & development |
| 2013 | High | Stimulation with acetylcholine induces Abi1 association with N-WASP in smooth muscle; Abi1 knockdown inhibits N-WASP activation, actin polymerization, and contraction without affecting myosin light chain phosphorylation. A multiprotein complex of c-Abl, CAS, and Abi1 forms upon contractile activation, and Abi1 is activated by c-Abl/CAS while Abi1 reciprocally controls c-Abl activation (pY412) and CAS interaction. | PMID:23740246 | The Journal of biological chemistry |
| 2014 | Medium | Y435-phosphorylated ABI1 localizes at sites of extracellular matrix degradation in colorectal carcinoma cells; RNAi knockdown of ABI1 suppresses matrix dissolution by 95%, and STI571 treatment abolishes ABI1 Y435-phosphorylation and suppresses matrix degradation, fibronectin attachment, and cell invasion. | PMID:24913355 | Molecular cancer |
| 2010 | Medium | Activated Rac1 specifically binds to a site encoded by exon 10 in ABI1 isoform 2 in vitro; because exon 10 is absent in isoform 3 due to alternative splicing, the isoform-2 WAVE2 complex and isoform-3 WAVE2 complex display differential binding to activated versus inactive Rac1. | PMID:20479892 | PloS one |
| 2015 | Medium | ABI1 acts as a scaffold protein in the SOS1/EPS8/ABI1 tri-complex: the SH3 domain of ABI1 mediates SOS1 binding, and the poly-proline+PxxDY region mediates EPS8 binding; TAT-conjugated inhibitory peptides disrupting ABI1-EPS8 interaction suppress ovarian cancer invasion and metastasis in vivo. | PMID:31488087 | BMC cancer |
| 2015 | Medium | ABI1 bridges c-Abl and WAVE2: a linker region between the proline-rich and SH3 domains of ABI1 is required for c-Abl interaction and c-Abl-mediated WAVE2 phosphorylation; the NESH/Abi-3-based WAVE2 complex, lacking this c-Abl-binding linker, is unable to generate lamellipodial protrusions and instead may promote invadopodia. | PMID:26428302 | Cell communication and signaling |
| 2018 | High | Bone marrow-specific deletion of Abi1 in mice results in an MPN-like phenotype with increased activity of Src family kinases (SFKs), STAT3, and NF-κB signaling, impaired hematopoietic stem cell self-renewal, and features resembling human myelofibrosis; ABI1 thus negatively regulates SFK/STAT3/NF-κB signaling in hematopoietic cells. | PMID:30213875 | Blood |
| 2019 | Medium | ABI1 loss in benign prostate epithelial cells induces EMT and activation of non-canonical WNT signaling; FYN SH2 domain interacts with ABI1 pY421 (high-affinity), and ABI1 loss leads to increased STAT3 phosphorylation downstream of FZD2, suggesting ABI1 inhibits EMT through suppressing FYN-STAT3 activation. | PMID:31530281 | Cell communication and signaling |
| 2020 | High | PTEN dephosphorylates ABI1 at Y213 and S216 (identified by phosphotyrosine immunoprecipitation/MS), leading to ABI1 degradation through the calpain pathway; this down-regulates the WAVE regulatory complex, reorganizes the actin cytoskeleton, and is required for epiblast epithelial polarization. | PMID:32673396 | The Journal of cell biology |
| 2020 | Medium | PTEN's protein phosphatase activity dephosphorylates and downregulates ABI1 in breast cancer cells; gain- and loss-of-function of ABI1 demonstrates that ABI1 mediates PTEN-loss-induced EMT and cancer stem cell activity. | PMID:32728066 | Scientific reports |
| 2020 | Medium | ABI1 localizes to the tip of lamellipodia and its protrusion coordinates with F-actin at the leading edge; ABI1 knockdown reduces smooth muscle cell migration and decreases leading-edge recruitment of profilin-1 (Pfn-1, identified as a new ABI1 partner), c-Abl, and N-WASP but not pVASP, cortactin, or vinculin. Integrin β1 and c-Abl regulate ABI1 positioning at the leading edge. | PMID:32606387 | Scientific reports |
| 2011 | Medium | Y398 in the SH3 domain of Abi-1 is a new phosphorylation site; combined disruption of Y213 and Y398 significantly weakens Abi-1 binding to c-Abl (SH3-Abl proline-rich domain interaction); Abi-1 phosphorylation at both sites stimulates Mena phosphorylation through c-Abl kinase activation. | PMID:21320496 | FEBS letters |
| 2004 | Low | E3B1/ABI1 levels are regulated by the Ca2+-activated protease calpain; serum starvation activates calpain-dependent E3B1 degradation, which is prevented by constitutively active PAK1 or by Rac1 activation downstream of PDGF; conversely, PAK auto-inhibitory domain expression causes E3B1 degradation even in serum. | PMID:15178460 | Biochemical and biophysical research communications |
| 2012 | Medium | Abi1 mediates airway smooth muscle (ASM) cell proliferation by regulating JAK2 and STAT3 activation; Abi1 knockdown reduces JAK2 and STAT3 activation and ASM proliferation. | PMID:35198891 | iScience |
| 2020 | Medium | CRISPR/Cas9 knockout of Abi1 in Bcr-Abl-transformed hematopoietic cells reduces ERK and PI3K/Akt signaling, inhibits IL3-independent growth and SDF-1α-mediated chemotaxis, abrogates abnormal actin remodeling, and abolishes leukemogenesis in syngeneic mice. | PMID:32276588 | Journal of hematology & oncology |
| 2013 | Medium | Xenopus Abi1 knockdown by morpholino disrupts eye morphogenesis; the SH3 domain of Abi1 is required for proper retinal progenitor cell movement and differentiation, and this requires an interaction with WASP (Wiskott-Aldrich syndrome protein). | PMID:23558677 | The Journal of biological chemistry |
| 2021 | Medium | Loss of MBNL1 promotes expression of the Abi1-Δe10 splice isoform (lacking exon 10); Abi1-Δe10 activates Rac1 independently of upstream stimulation and triggers the Rac1-NOX1-ROS pathway leading to KLF4 upregulation, VSMC macrophage-like transdifferentiation, increased proliferation and migration. | PMID:33759281 | Cell proliferation |
| 2024 | Low | Caskin2 associates with the WAVE regulatory complex in an ABI1-dependent manner to promote cell migration; growth factor-induced phosphorylation of Caskin2 at serine 878 regulates the Caskin2-ABI1 interaction. | PMID:38587458 | Journal of cell science |
| 2026 | High | During Listeria monocytogenes infection, the pore-forming toxin LLO triggers Ca2+ influx leading to calpain-mediated spectrin cleavage; this mobilizes ABI1 from its spectrin-bound cortical state, allowing ABI1 to bind EPS8 within protrusions and activate EPS8's actin-capping activity to enable actin recycling and protrusion elongation for cell-to-cell spread. Conditional Abi1 KO mice show significantly reduced Lm infection susceptibility. | PMID:41974702 | Nature communications |
| 2024 | Medium | ABI1 is imported to the plant cell nucleus by SAD2 (an importin β family protein) upon coronatine (COR) treatment; nuclear ABI1 accumulation requires SAD2 and enables COR to antagonize ABA signaling and reopen stomata during bacterial pathogen invasion. | PMID:38683723 | The Plant journal |
| 2020 | Medium | CaMKIIα phosphorylates Shank3 at Ser685; this phosphorylation significantly increases binding of ABI1 to Shank3 in vitro (pre-phosphorylated GST-Shank3), whereas Ser685Ala or Ser685Asp mutation reduces ABI1-Shank3 co-immunoprecipitation from cells. | PMID:31983435 | Biochemical and biophysical research communications |
| 2024 | Medium | ABI1 degradation through ubiquitination by the E3 ligase CBLC activates ERK signaling in colorectal cancer; ABI1 upregulation abolishes the pro-tumorigenic effects of CBLC. | PMID:38743987 | Translational oncology |

## Citations

- PMID:10499589
- PMID:10777208
- PMID:10995551
- PMID:12515821
- PMID:15048123
- PMID:15143189
- PMID:15178460
- PMID:16155590
- PMID:16225669
- PMID:16280551
- PMID:16940963
- PMID:17304222
- PMID:17395426
- PMID:17501982
- PMID:18328268
- PMID:18453543
- PMID:19168673
- PMID:20479892
- PMID:20531346
- PMID:20598684
- PMID:21118970
- PMID:21173240
- PMID:21320496
- PMID:21464958
- PMID:21482783
- PMID:21900237
- PMID:22102872
- PMID:22993434
- PMID:23028145
- PMID:23209429
- PMID:23558677
- PMID:23740246
- PMID:24913355
- PMID:26428302
- PMID:30213875
- PMID:31488087
- PMID:31530281
- PMID:31983435
- PMID:32276588
- PMID:32606387
- PMID:32673396
- PMID:32728066
- PMID:33759281
- PMID:35198891
- PMID:38587458
- PMID:38683723
- PMID:38743987
- PMID:41974702
- PMID:9010225
- PMID:9694699
