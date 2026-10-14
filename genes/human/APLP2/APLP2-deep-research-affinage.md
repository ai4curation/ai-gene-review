---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APLP2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q06481
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 37
citation_count: 38
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APLP2 (human)

## Current model (mechanistic narrative)

APLP2 is a type I transmembrane glycoprotein of the APP family that functions in synaptic transmission, neural development, and diverse cell-surface signaling processes, acting largely redundantly with APP [PMID:9461064]. Like APP, APLP2 undergoes sequential proteolytic processing by alpha- and beta-secretases—with BACE modulating its cleavage in vivo [PMID:14970212, PMID:15080893]—and by the metalloproteinases ADAM10 and TACE to shed a soluble neurotrophic ectodomain [PMID:16279945, PMID:9923612], followed by gamma-/epsilon-secretase cleavage that liberates an intracellular domain (AICD2) [PMID:14970212, PMID:15080893]; ectodomain shedding is controlled by MAPK/PKC-epsilon signaling [PMID:11443060]. APLP2 and APP are functionally redundant during postnatal development, with double knockout causing early lethality [PMID:9461064], and together they sustain neuromuscular and central synaptic transmission: they bind the presynaptic release machinery via the N-terminus of their intracellular domains in a complex with Mint2/Munc18 to support quantal glutamate release [PMID:21522131, PMID:26551565], interact with NMDA receptor GluN1 to promote receptor surface expression [PMID:25683482], control VGLUT2 expression through the intracellular domain [PMID:18535156], and maintain neuronal Ca2+ homeostasis through SERCA-ATPase and Stim1/2 [PMID:34172567]. APP family loss in GABAergic interneurons impairs LTP, spatial learning, and excitation/inhibition balance [PMID:32219307], and APLP2 at GABAergic terminals engages microglial CD11b in trans to restrain pain sensitization [PMID:36442651]. APLP2 forms homo- and heterotypic cis complexes with APP, reducing Abeta42 generation [PMID:19126676], and is subject to post-translational regulation including chondroitin-sulfate modification at Ser-614 governed by alternative splicing [PMID:8071334, PMID:7622456] and Bat3-mediated stabilization against proteasomal degradation [PMID:22641691]. APLP2 also modulates copper homeostasis [PMID:10526140], inhibits plasma clotting through its Kunitz-type protease inhibitor domain [PMID:19403832], and regulates glypican-1 heparan sulfate catabolism [PMID:15677459]. Outside the nervous system, APLP2 promotes pancreatic cancer cell migration via actin reorganization [PMID:25576918], inhibits TGF-beta signaling by destabilizing TGFBR2 through competition with Hsp90 [PMID:37479189], suppresses MHC class I surface expression [PMID:24353913], and its AICD2 fragment activates NF-kB via p65 to drive antimicrobial macrophage responses [PMID:37844466]; endothelial APLP2sα promotes postischemic angiogenesis through allosteric activation of the KIT receptor [PMID:42172320].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-112316 Neuronal System, R-HSA-162582 Signal Transduction
- **partners:** APP, MINT2, MUNC18, GLUN1, PCSK9, TGFBR2, BAT3, CD11B
- **complexes:** APP/Mint2/Munc18 presynaptic complex, APP-APLP2 cis heteromer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1993 | Low | APLP2 contains a cytoplasmic domain predicted to couple with the GTP-binding protein G(o), suggesting it may function as a cell surface activator of this G protein, similar to APP. | PMID:8220435 | Nature genetics |
| 1994 | High | APLP2 is modified by chondroitin sulfate (CS) glycosaminoglycan addition at a single site (Ser-614); a serine-to-alanine substitution at position 614 abolishes CS GAG modification, identifying this as the sole modification site. | PMID:8071334 | The Journal of biological chemistry |
| 1995 | High | CS GAG modification of APLP2 is regulated by alternative splicing: the APLP2-763 isoform, containing a 12 amino acid insertion N-terminal to Ser-614, is not modified by CS GAG, whereas APLP2-751 is. Similarly, APP isoforms lacking exon 15 sequences (L-APP) are CS GAG-modified, whereas those containing exon 15 are not. | PMID:7622456 | The Journal of biological chemistry |
| 1995 | Medium | APLP2 is enriched in postsynaptic compartments in cortex and hippocampus, and is abundant in olfactory sensory axons and axon terminals in glomeruli; CS GAG-modified APLP2 forms are enriched in olfactory epithelium and accumulate in the olfactory bulb, consistent with a role in axonal pathfinding and/or synaptogenesis. | PMID:7472397 | The Journal of neuroscience |
| 1997 | High | APLP2 and APP are functionally redundant in vivo: APLP2 single KO mice are viable and fertile, but APP/APLP2 double KO mice exhibit ~80% early postnatal lethality, demonstrating that APLP2 and APP can substitute for each other functionally. | PMID:9461064 | Neurobiology of aging |
| 1998 | Medium | APLP2 is required for correct genomic segregation in dividing cells: homozygous APLP2 deletion embryos arrest before the blastocyst stage with abnormal nuclear DNA content (departing from normal 2-4C values), and antisense suppression in fibroblasts produces daughter cells with abnormal DNA contents, indicating a role in mitotic genome segregation. | PMID:9707424 | The EMBO journal |
| 1999 | Medium | APP and APLP2 expression specifically modulates copper homeostasis in the liver and cerebral cortex; APP(-/-) and APLP2(-/-) mice show significantly elevated copper levels in cerebral cortex (40% and 16%, respectively) and liver (80% and 36%, respectively) compared to wild-type, with no significant differences in zinc or iron. | PMID:10526140 | Brain research |
| 1999 | Medium | Recombinant soluble APLP2 ectodomain (sAPLP2) promotes neurite outgrowth in chick sympathetic neurons with activity similar to APP isoforms sAPP695 and sAPP751. | PMID:9923612 | FEBS letters |
| 2001 | Medium | APLP2 ectodomain shedding in corneal epithelial cells is regulated by MAP kinase (MAPK): basal shedding and that induced by PKC activator PMA or EGF is blocked by the MEK inhibitor U-0126; PKC-epsilon is involved in PMA- and EGF-induced shedding. | PMID:11443060 | American journal of physiology. Cell physiology |
| 2004 | High | APLP2 is processed by alpha-, beta-, gamma-, and epsilon-secretase-like cleavages, producing C-terminal fragments, intracellular domains (AICD-like), and p3-like and Abeta-like fragments. BACE (beta-secretase) modulates APLP2 processing in vivo: APLP2 proteolytic products are decreased in BACE KO mice and increased in BACE transgenic mice; overexpression of BACE in cultured cells increases APLP2 processing. | PMID:14970212, PMID:15080893 | The Journal of biological chemistry; Molecular and cellular neurosciences |
| 2005 | High | APLP2 is a substrate for the disintegrin-metalloproteinases ADAM10 and TACE (ADAM17): overexpression of either proteinase in HEK293 cells increases shedding of soluble APLP2 severalfold; ADAM10-preferring inhibitor most strongly reduces shedding in neuroblastoma cells; ADAM10 transgenic mice show significantly increased soluble APLP2 and its C-terminal fragments. | PMID:16279945 | The FEBS journal |
| 2005 | High | APP and APLP2 modulate Cu/Zn-nitric oxide-catalyzed degradation of glypican-1 heparan sulfate: in cell-free experiments, the Cu(I) form of APP and both Cu(II) and Cu(I) forms of APLP2 inhibit glypican-1 autodegradation; in primary cortical neurons from APP or APLP2 KO mice, nitric oxide-catalyzed heparan sulfate degradation is increased; in APLP2 KO (but not APP KO) fibroblasts, heparan sulfate degradation is also increased. | PMID:15677459 | The Journal of biological chemistry |
| 2006 | High | PAT1a binds directly to APP, APLP1, and APLP2 in vivo and co-localizes with them in trans-Golgi network vesicles or endosomes in primary neurons; PAT1a interacts with the basolateral sorting signal of APP/APLPs; overexpression or RNAi knockdown of PAT1a modulates APP/APLP surface levels and promotes their processing, resulting in increased Abeta secretion. | PMID:17050537 | The Journal of biological chemistry |
| 2006 | Medium | APP and APLP2 are required for keratinocyte proliferation, migration, and adhesion: keratinocytes from APP/APLP2 double KO mice show ~40% reduced proliferation in vivo and in vitro, reduced migration velocity, and compromised cell-substrate adhesion; double KO keratinocytes die within the first week of culture. Proliferation deficits are rescued by exogenous recombinant sAPPalpha. | PMID:16584729 | Experimental cell research |
| 2008 | Medium | APP and APLP2 are required for normal glucose and insulin homeostasis: APP/APLP2 double KO mice show 66% lower plasma glucose and hyperinsulinemia compared to wild-type at postnatal day, identifying a role for APP/APLP2 in modulating plasma insulin and glucose concentrations. | PMID:18393365 | The Journal of pathology |
| 2008 | High | Loss of APP and APLP2 in neurons leads to decreased expression of vesicular glutamate transporter 2 (VGLUT2) and reduced glutamate uptake/release; blocking gamma-secretase in wild-type neurons similarly decreases VGLUT2; VGLUT2 levels can be restored in double KO neurons by a construct encoding the C-terminal intracellular domain of APP, indicating the intracellular domain mediates this function. | PMID:18535156 | Stem cells |
| 2009 | High | APLP2 and APP share overlapping anticoagulant functions: recombinant KPI domains of both proteins inhibit plasma clotting in vitro; APLP2(-/-) and APP(-/-) mice both exhibit significantly shorter times to carotid artery occlusion and produce smaller hematomas in intracerebral hemorrhage models, indicating a prothrombotic phenotype when APLP2 is absent. | PMID:19403832 | The Journal of neuroscience |
| 2009 | High | Live cell imaging shows that APLP2 localizes predominantly to intracellular compartments (unlike APLP1 which is mainly at the cell surface); APLP2 forms homo- and heterotypic cis interactions with APP family members detectable by FRET and co-immunoprecipitation; interactions occur in a modular mode with the N-terminal half of the ectodomain crucial for APP-APLP2 interactions; coexpression of APP with APLP2 leads to diminished Abeta42 generation, attributed to heteromeric complex formation. | PMID:19126676 | Journal of cell science |
| 2011 | High | APLP2 and APP are synergistically required for neuromuscular transmission: APPsα-DM mice (expressing only secreted APPsα on APLP2-null background) show impaired neuromuscular transmission with reductions in quantal content, readily releasable pool, and vesicle release sustainability, resulting in muscular weakness; defects are associated with loss of an APP/Mint2/Munc18 complex; APPsα-DM muscle shows fragmented postsynaptic specializations. | PMID:21522131 | The EMBO journal |
| 2011 | Medium | APLP2 mediates signaling via formation of transcriptionally active triple protein complexes with adaptor protein Mint3 and transcriptional co-activators Taz and Yap; complex formation is regulated by gamma-secretase cleavage of APLP2; Mint1 (instead of Mint3) prevents nuclear translocation of the complex. | PMID:21178287 | Journal of Alzheimer's disease |
| 2013 | Medium | APLP2 is required for proper cell cycle exit of cortical neuronal progenitors: silencing APLP2 in vivo in an APP/APLP1 double KO background causes cortical progenitors to remain undifferentiated longer with a higher number of mitotic cells; neuron-specific APLP2 downregulation does not affect the speed or position of migrating excitatory cortical neurons. | PMID:23345401 | Journal of cell science |
| 2013 | Medium | PCSK9 interacts directly with APLP2 (but not APP) via its C-terminal domain in a pH-dependent manner; APLP2 (but not APP) mediates postendocytic delivery of PCSK9 to lysosomes, making it required for PCSK9 function in LDLR degradation. | PMID:23430252 | The Journal of biological chemistry |
| 2013 | Medium | APLP2 co-immunoprecipitates with MHC class I molecules in Ewing's sarcoma cells; irradiation redistributes APLP2 and MHC class I on the cell surface; APLP2 siRNA knockdown increases MHC class I surface expression, indicating APLP2 inhibits MHC class I surface expression. | PMID:24353913 | Oncoimmunology |
| 2014 | Medium | APP/APLP2 expression is required for transport of anhydromannose-containing heparan sulfate from endosomes to the nucleus and subsequently to autophagosomes: nuclear HS translocation is seen in WT but not APP(-/-) or APLP2(-/-) MEFs; transfection of APP restores nuclear import; beta- and gamma-secretase inhibitors block nuclear transport, implicating APP/APLP2 degradation products. | PMID:24898256 | The Journal of biological chemistry |
| 2015 | High | APP and APLP2 interact with the synaptic release machinery via the NH2-terminal region of their intracellular domains; a peptide (JCasp) naturally produced by gamma-secretase/caspase double-cut of APP interferes with APP-presynaptic protein interactions and reduces glutamate release in hippocampal slices from wild-type but not APP-deficient mice; deletion of APP and APLP2 produces synaptic deficits similar to those caused by JCasp. | PMID:26551565 | eLife |
| 2015 | Medium | APLP2 co-immunoprecipitates with NMDA receptor subunits GluN1/GluN2A and GluN1/GluN2B in mammalian cells and in adult brain; interaction is via GluN1 subunit; APLP2 enhances GluN1/GluN2A and GluN1/GluN2B cell surface expression. | PMID:25683482 | Journal of neurochemistry |
| 2015 | Medium | APLP2 knockdown in pancreatic cancer cells reduces migration and invasion, decreases cortical actin, and increases intracellular actin filaments; APLP2 knockdown reduces tumor weight and metastasis in orthotopic mouse models, indicating APLP2 affects actin cytoskeleton organization to promote cancer cell migration. | PMID:25576918 | Oncotarget |
| 2015 | Medium | Aplp2 knockout mice develop high degrees of hyperopia and exhibit dose-dependent reduction in susceptibility to environmentally induced myopia; the phenotype is associated with reduced contrast sensitivity and changes in electrophysiological properties of retinal amacrine cells, which express Aplp2. | PMID:26313004 | PLoS genetics |
| 2017 | Medium | APP, APLP2, and LRP1 all interact with PCSK9, but none is required for PCSK9-mediated LDLR degradation in vivo: infusion of PCSK9 into App(-/-), Aplp2(-/-), Aplp2-depleted App(-/-), or liver-specific Lrp1(-/-) mice results in similar reductions in hepatic LDLR as in wild-type mice. | PMID:28495363 | Biochimica et biophysica acta |
| 2018 | Medium | APLP2 promotes cell migration in Drosophila via JNK signaling: ectopic APLP2 expression activates JNK by phosphorylation, which triggers MMP1 expression required for basement membrane degradation and cell migration; loss of JNK suppresses APLP2-induced migration while gain of JNK enhances it. | PMID:30155482 | BioMed research international |
| 2020 | High | Loss of APP and APLP2 specifically in GABAergic forebrain neurons (DlxCre cDKO) impairs synaptic plasticity (LTP), spatial learning, and excitation/inhibition balance; reduced action potential firing of CA1 pyramidal cells and altered excitatory/inhibitory synaptic currents indicate APP family proteins in inhibitory interneurons maintain functional network activity. | PMID:32219307 | Cerebral cortex |
| 2021 | High | APP and APLP2 together control neuronal Ca2+ homeostasis; loss of both (but not APLP2 alone) impairs Ca2+ handling, ER Ca2+ store refill, and synaptic plasticity via altered SERCA-ATPase function and expression of store-operated Ca2+ channel-associated proteins Stim1 and Stim2; long-term AAV-mediated expression of APPsα (but not acute application) restores Ca2+ homeostasis and LTP in APP/APLP2 cDKO neurons. | PMID:34172567 | PNAS |
| 2022 | Medium | Peripheral nerve injury reduces APLP2 expression specifically in spinal GABAergic inhibitory interneurons; targeted knockdown of APLP2 in GAD2-positive neurons evokes pain hypersensitivity via microglial activation; APLP2 at GABAergic terminals interacts with microglia-specific integrin CD11b in a trans-cellular manner, and disruption of this interaction leads to microglia-dependent pain sensitization. | PMID:36442651 | Neuropharmacology |
| 2023 | Medium | APLP2 (as YWK-II/APLP2) inhibits TGF-β signaling by promoting degradation of TGFBR2: APLP2 associates with TGFBR2 in a TGF-β activity-dependent manner, binds Hsp90 to interfere with the TGFBR2-Hsp90 stabilizing interaction, and leads to enhanced ubiquitination and degradation of TGFBR2; knockdown of APLP2 increases TGFBR2 protein level and sensitizes cells to TGF-β, while overexpression destabilizes TGFBR2. | PMID:37479189 | Biochimica et biophysica acta. Molecular cell research |
| 2023 | Medium | The APLP2 cleaved intracellular domain product (AICD2), generated by gamma-secretase, translocates to the nucleus where it interacts with p65, enhancing NF-κB transcriptional activity to upregulate IL-1β and iNOS expression; APLP2 mutation/knockdown reduces macrophage-mediated killing of Mycobacterium tuberculosis. | PMID:37844466 | International immunopharmacology |
| 2012 | Medium | Bat3 interacts with APLP2 (YWK-II/APLP2) and enhances its stability by reducing ubiquitylation and proteasomal degradation; the proline-rich domain of Bat3 is required for binding to APLP2; nuclear export of Bat3 under apoptotic stimulation elevates APLP2 protein levels. | PMID:22641691 | Journal of cell science |
| 2026 | Medium | Endothelial APLP2 is required for postischemia angiogenesis after myocardial infarction; hypoxia induces alpha-secretase-mediated processing of APLP2 into soluble APLP2sα; APPsα and APLP2sα exert proangiogenic effects by positive allosteric modulation of the endothelial receptor tyrosine kinase KIT, promoting neovascularization. | PMID:42172320 | Science advances |

## Citations

- PMID:10526140
- PMID:11443060
- PMID:14970212
- PMID:15080893
- PMID:15677459
- PMID:16279945
- PMID:16584729
- PMID:17050537
- PMID:18393365
- PMID:18535156
- PMID:19126676
- PMID:19403832
- PMID:21178287
- PMID:21522131
- PMID:22641691
- PMID:23345401
- PMID:23430252
- PMID:24353913
- PMID:24898256
- PMID:25576918
- PMID:25683482
- PMID:26313004
- PMID:26551565
- PMID:28495363
- PMID:30155482
- PMID:32219307
- PMID:34172567
- PMID:36442651
- PMID:37479189
- PMID:37844466
- PMID:42172320
- PMID:7472397
- PMID:7622456
- PMID:8071334
- PMID:8220435
- PMID:9461064
- PMID:9707424
- PMID:9923612
