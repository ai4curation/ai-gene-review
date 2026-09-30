---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AHNAK
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q09666
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 45
citation_count: 45
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AHNAK (human)

## Current model (mechanistic narrative)

AHNAK is a giant (~700 kDa) scaffolding phosphoprotein built from highly conserved central repeated units whose subcellular distribution between nucleus, cytoplasm, and plasma membrane is dynamically controlled by phosphorylation: PKB/Akt phosphorylation of Ser5535 drives nuclear export through an adjacent NES [PMID:11535620], while PKC activation and Ca2+-dependent signals translocate it toward the cell membrane via determinants in its C-terminal domain [PMID:7698224, PMID:10771490]. At the cytosolic face of the plasma membrane AHNAK assembles a cortical actin-organizing platform: its C-terminal domain binds G- and F-actin and the annexin A2/S100A10 (A2t) heterotetramer through a defined 20-residue motif (resolved at 2.5 Å), and these interactions are required for cortical actin reorganization and cell architecture [PMID:12153988, PMID:14699089, PMID:16984913, PMID:23275167]. Through its central repeated units AHNAK functions as a signaling scaffold, binding and activating PLC-γ1 in an arachidonic-acid-dependent manner and recruiting PKC-α—disrupting the inhibitory PKC-α/PP2A complex—to amplify Ca2+ mobilization and Raf/MEK/Erk and Rac signaling [PMID:10318799, PMID:15033986, PMID:18174170, PMID:23042471]. A second major role is regulation of L-type voltage-gated Ca2+ channels: AHNAK binds the Cavβ2 subunit (Kd ~55–60 nM via a C-terminal PxxP motif) to act as a brake on Cav1.2 current that is relieved by PKA phosphorylation of either partner, and is required for surface expression and Ca2+ influx of L-type channels in T cells, neurons, and other cell types [PMID:10593863, PMID:12153988, PMID:14722071, PMID:16319140, PMID:22497893, PMID:20607281, PMID:30760886, PMID:18191595, PMID:19497879]. AHNAK is a structural component of muscle membrane complexes including the dysferlin complex and the costamere/β-dystroglycan network, linking these to the actin cytoskeleton and influencing membrane mechanics and Schwann cell morphology [PMID:17185750, PMID:20833135, PMID:24796807]. In the nucleus AHNAK shapes growth and stress responses: it potentiates TGFβ/Smad3 signaling by promoting Smad3 nuclear accumulation and drives BMP2/Smad1-dependent adipogenesis at the PPARγ promoter [PMID:24662814, PMID:26466345, PMID:30258109], and it restrains 53BP1 oligomerization and phase separation to tune the p53 DNA-damage response and senescence [PMID:33961796]. Its protein levels are controlled by the UBE3C and RNF38 E3 ubiquitin ligases, providing post-translational control over its context-dependent tumor-suppressive and pro-metastatic activities [PMID:30503554, PMID:30836988].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity, GO:0008289 lipid binding, GO:0042393 histone binding
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005829 cytosol, GO:0005856 cytoskeleton, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-73894 DNA Repair, R-HSA-1643685 Disease, R-HSA-1640170 Cell Cycle, R-HSA-1266738 Developmental Biology
- **partners:** ANXA2, S100A10, CACNB2, PLCG1, PRKCA, SMAD3, TP53BP1, DYSF
- **complexes:** annexin A2/S100A10 (A2t) heterotetramer complex, dysferlin complex, L-type Ca2+ channel (Cav1.2/Cavβ2) complex, costamere / β-dystroglycan network

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1992 | Medium | AHNAK encodes an unusually large (~700 kDa) protein with a large internal domain composed of highly conserved 128-amino-acid repeated elements displaying a redundant proline-at-every-seventh-residue motif; preliminary fractionation indicated predominantly nuclear residence. | PMID:1608957 | Proceedings of the National Academy of Sciences of the United States of America |
| 1993 | Medium | AHNAK protein is located principally in the nucleus and is phosphorylated on both serine and threonine; protein abundance increases when cells withdraw from the division cycle (serum withdrawal or differentiation), while the degree of phosphorylation diminishes in those settings. | PMID:8381120 | The Journal of cell biology |
| 1993 | Medium | Desmoyokin, a 680 kDa desmosomal plaque protein, is identical to AHNAK; its distribution in keratinocytes (closely associated with the plasma membrane) differs from non-keratinocyte cells where it is diffusely cytoplasmic, suggesting cell-type-specific localization and function. | PMID:8408266 | Journal of cell science |
| 1995 | Medium | PKC activation (by TPA or high calcium) is required for translocation of desmoyokin/AHNAK from the cytoplasm/nucleus to the plasma membrane in keratinocytes; selective PKC inhibitors completely block this translocation, and calcium-induced phosphorylation of AHNAK was confirmed by [32P] labeling. | PMID:7698224 | Experimental cell research |
| 1995 | Medium | In human epidermis, desmoyokin/AHNAK localizes to the non-desmosomal and non-hemidesmosomal plasma membrane of keratinocytes, not to desmosomes themselves, established by post-embedding immunoelectron microscopy with double-labeling against desmosomal markers. | PMID:7769263 | The Journal of investigative dermatology |
| 1999 | High | AHNAK binds and activates phospholipase C-gamma1 (PLC-γ1) in the presence of arachidonic acid; arachidonic acid promotes a physical interaction between AHNAK and PLC-γ1, and activation is attributable to reduction of the enzyme's apparent Km toward PIP2. Recombinant AHNAK fragments containing one or four repeated motifs activated PLC-γ1 at nanomolar concentrations, establishing multiple activation sites per molecule. | PMID:10318799 | The Journal of biological chemistry |
| 1999 | Medium | AHNAK (pp700) interacts specifically with the beta2 subunit of cardiac L-type Ca2+ channels as revealed by co-precipitation with anti-channel subunit antibodies; membrane-associated AHNAK undergoes substantial in vivo PKA phosphorylation upon beta-adrenergic stimulation (isoproterenol), specifically in the fraction that co-precipitates with the Ca2+ channel beta subunit. | PMID:10593863 | FASEB journal |
| 2000 | Medium | The C-terminal domain of desmoyokin/AHNAK is responsible for its nuclear localization in low-calcium conditions and for its calcium/PKC-induced translocation from nucleus toward the cytoplasm and cell membrane; N-terminal and central domains alone showed no calcium-dependent redistribution. | PMID:10771490 | The Journal of investigative dermatology |
| 2001 | Medium | AHNAK is the major and most specific Ca2+-dependent target of S100B in fibroblast and astrocytoma cells; interaction requires both Ca2+ and Zn2+ (2 Zn2+ per S100B enhance Ca2+-dependent binding), and the binding domains on AHNAK map to its repeated motifs. AHNAK does not bind calmodulin, S100A6, or S100A11 under these conditions. | PMID:11312263 | The Journal of biological chemistry |
| 2001 | High | PKB/Akt phosphorylates AHNAK in vitro and in vivo on serine 5535; this phosphorylation mediates nuclear export of AHNAK via a nuclear export signal (NES) and is a major determinant of AHNAK's extranuclear localization in epithelial cells. | PMID:11535620 | The Journal of cell biology |
| 2002 | High | The C-terminal region of AHNAK (aa 5262–5643) interacts with the beta2a subunit of the cardiac L-type Ca2+ channel with Kd ~55 nM (for the beta2a C-terminal truncate), and the same region binds G-actin and co-sediments with F-actin, providing a structural link between the L-type Ca2+ channel and the actin-based cytoskeleton. | PMID:12153988 | FASEB journal |
| 2003 | High | AHNAK forms a multimeric complex with actin and the annexin 2/S100A10 heterotetramer at the cytosolic face of the plasma membrane; the S100A10 subunit mediates the annexin 2–AHNAK interaction at the AHNAK C-terminal domain. siRNA-mediated knockdown of annexin 2/S100A10 prevents AHNAK plasma membrane association, and AHNAK siRNA prevents cortical actin cytoskeleton reorganization required for cell height in MDCK cells. | PMID:14699089 | The Journal of cell biology |
| 2004 | High | Four central repeated units (4 CRUs) of AHNAK act as a scaffolding motif that binds both PKC-α and PLC-γ1; AHNAK-bound PKC-α stimulates arachidonic acid release near PLC-γ1, and the concerted action of 4 CRUs with arachidonic acid activates PLC-γ1, leading to IP3 generation and intracellular Ca2+ mobilization in a PLC-γ1-dependent manner. | PMID:15033986 | The Journal of biological chemistry |
| 2004 | High | The C-terminal ahnak fragment (ahnak-C2) induces actin filament bundling into paracrystalline-like structures in vitro and stabilizes isometric force development in demembranated skeletal muscle fibers. An endogenous 72 kDa C-terminal ahnak fragment co-purifies with myofibrillar proteins and localizes to intercalated discs and near the Z-line in cardiomyocytes. | PMID:15001564 | FASEB journal |
| 2004 | High | The carboxyl-terminal ahnak fragments P3 (aa 5456–5556) and P4 (aa 5556–5643) modulate the L-type Ca2+ current in rat ventricular cardiomyocytes: P4 increases current amplitude by ~23% while both P3 and P4 slow current inactivation. These effects are mediated via the ahnak–beta2 subunit interaction rather than the ahnak–F-actin interaction, as actin-stabilizing agents did not alter their effect. | PMID:14722071 | The Journal of biological chemistry |
| 2004 | Medium | AHNAK interacts specifically with the DNA ligase IV–XRCC4 complex (but not with other DNA ligases or other NHEJ components), stimulates the double-stranded ligation activity of DNA ligase IV–XRCC4, has weak DNA-binding activity, and forms a stable complex with DNA ligase IV–XRCC4 on DNA. | PMID:15177040 | DNA repair |
| 2005 | High | A naturally occurring missense variant Ile5236Thr in AHNAK critically reduces beta2 subunit binding affinity (~50% decrease after PKA phosphorylation or with the mutant peptide) and, when applied intracellularly, mimics PKA effects on L-type Ca2+ current (increases amplitude ~60%, slows inactivation, leftward voltage shift) and prevents further up-regulation by isoprenaline. | PMID:16319140 | FASEB journal |
| 2006 | High | AHNAK is a component of the dysferlin protein complex in skeletal muscle; the C2A domain of dysferlin binds the C-terminal domain of AHNAK (defined by GST pulldown); reduction or absence of dysferlin causes secondary muscle-specific loss of AHNAK from the sarcolemma; during regeneration, both proteins redistribute to the cytoplasm in concert. | PMID:17185750 | FASEB journal |
| 2006 | High | A specific 20-amino-acid peptide in the AHNAK C-terminal domain (A2tBP1) constitutes the minimal binding motif for the annexin 2/S100A10 tetramer (A2t); binding requires both the annexin 2 N-terminal tail and S100A10 together (neither alone is sufficient); a second, lower-affinity A2t-binding motif (A2tBP2) exists in the N-terminal AHNAK domain. Overexpressed A2tBP1-EGFP co-fractionates with and co-immunoprecipitates S100A10/annexin 2 in a calcium-dependent manner, and relocalizes to the plasma membrane under oxidative/mechanical stress. | PMID:16984913 | The Journal of biological chemistry |
| 2008 | High | AHNAK1 is required for plasma membrane expression of L-type calcium channel alpha1S (Cav1.1) subunit in CD4+ T cells, likely through interaction with the beta regulatory subunit; AHNAK1-deficient mice exhibit reduced Ca2+ influx upon TCR crosslinking and poor NFAT activation. | PMID:18191595 | Immunity |
| 2008 | High | AHNAK central repeated units (CRUs) bind and activate PKC-α in a phosphatidylserine/DAG-independent manner and disrupt the PKC-α–protein phosphatase 2A (PP2A) inhibitory complex, thereby potentiating PKC-α activation and downstream Raf/MEK/Erk phosphorylation; Ahnak-null MEFs show enhanced PKC–PP2A complex formation and reduced membrane translocation of PKC-α in response to stimuli. | PMID:18174170 | The Journal of biological chemistry |
| 2009 | High | AHNAK1 is required for Ca2+ entry into mature cytolytic CD8+ T cells (CTLs); AHNAK1-deficient CTLs show markedly reduced Cav1.1 alpha1S subunit expression, reduced granzyme-B production, cytolytic activity, and IFN-γ secretion after TCR stimulation. | PMID:19497879 | Proceedings of the National Academy of Sciences of the United States of America |
| 2009 | Medium | The C-type natriuretic peptide receptor (NPR-C) tethers AHNAK1 at the plasma membrane via the AHNAK1 C1 domain; siRNA knockdown of NPR-C results in AHNAK1 nuclear accumulation, and knockdown of either NPR-C or AHNAK1 attenuates arachidonic acid/phorbol ester-induced intracellular Ca2+ mobilization. | PMID:19710363 | American journal of physiology. Cell physiology |
| 2009 | Medium | In osteoblastic MC3T3-E1 cells, AHNAK associates with the Cav1.2/beta2-subunit complex at the plasma membrane via the beta2 subunit; siRNA knockdown of AHNAK significantly impairs Ca2+ influx without disrupting the actin cytoskeleton or disassembling the Cav1.2/beta2 complex. | PMID:19261907 | American journal of physiology. Cell physiology |
| 2009 | Medium | AHNAK is constitutively expressed by myelinating Schwann cells; siRNA silencing of AHNAK affects Schwann cell morphology and laminin-substrate attachment, and alters expression and distribution of dystroglycan, suggesting AHNAK targets the dystroglycan-associated receptor complex at the plasma membrane. | PMID:18837049 | Glia |
| 2010 | Medium | AHNAK1 and AHNAK2 are both components of the costameric network in skeletal muscle (co-localize with vinculin); AHNAK1 is absent from the T-tubule system; AHNAK1-deficient fibers show significantly higher transverse stiffness by atomic force microscopy, but AHNAK1 is not required for membrane repair in a laser wounding assay. | PMID:20833135 | Biochemical and biophysical research communications |
| 2011 | Medium | AHNAK interaction with dysferlin is lost upon cleavage by calpain 3 protease; in muscular dystrophies (LGMD2B from dysferlin mutations and LGMD2A from calpain 3 mutations), ahnak1 loses sarcolemmal localization and appears in muscle connective tissue. Ca2+-stimulated vesicle shedding from primary human myotubes releases ahnak1-containing vesicles (~150 nm diameter), establishing a vesicle-release mechanism for abnormal ahnak1 localization. | PMID:22057634 | Journal of muscle research and cell motility |
| 2011 | Medium | A small 17 kDa AHNAK isoform (generated by alternative splicing) interacts with the large 700 kDa AHNAK in the cytoplasm; the small isoform is also present in the nucleus and establishes a positive feedback loop to regulate mRNA splicing at its own locus during muscle differentiation. | PMID:21940993 | FASEB journal |
| 2012 | High | Crystal structure of a 20-aa AHNAK C-terminal peptide (residues 5654–5673) bound to the annexin A2/S100A10 heterotetramer at 2.5 Å resolution shows that binding is governed by hydrophobic interactions between AHNAK side chains and pockets on S100A10, while hydrogen bonds predominantly involve backbone AHNAK atoms, explaining the binding's specificity for S100A10 over other S100 proteins. | PMID:23275167 | Acta crystallographica. Section D, Biological crystallography |
| 2012 | High | Ahnak1 interacts with the SH3-HOOK-GK core region of Cavβ2 (C- and N-terminal Cavβ2 regions are dispensable); PKA phosphorylation of Ser-296 in the GK domain of Cavβ2 increases ahnak1 binding affinity ~2.4-fold but reduces binding capacity ~60%, constituting a mechanism by which PKA phosphorylation modulates ahnak1's effect on Cav1.2 channel activity. | PMID:22497893 | Biochemical and biophysical research communications |
| 2012 | High | Ahnak functions as a scaffolding protein in aortic smooth muscle cells (ASMCs) connecting a complex of Erk, PAK (p21-activated kinase), and PIXβ (PAK-interacting exchange factor β); Ahnak knockout ASMCs show reduced Rac activation, impaired lamellipodial protrusion, and decreased PDGF-dependent migration; neointimal formation and SMC migration after carotid ligation injury are significantly retarded in Ahnak knockout mice. | PMID:23042471 | Cardiovascular research |
| 2014 | High | Ahnak directly interacts with Smad3 through its MH2 domain and stimulates Smad3 nuclear localization, potentiating TGFβ-induced transcriptional activity; Ahnak overexpression causes c-Myc and cyclin D1/D2 downregulation and cell cycle arrest; Ahnak-null mice in the MMTV-middle T background show significantly accelerated mammary hyperplasia. | PMID:24662814 | Oncogene |
| 2014 | Medium | Crystal structures of the PDZ-like domain of AHNAK2 reveal intertwined, domain-swapped homodimers; the AHNAK2 PDZ domain contains a bound class III ligand peptide in the preformed binding pocket with two salt bridges and weak C-terminus recognition, providing a structural basis for homodimerization and scaffolding function. | PMID:24675079 | The Journal of biological chemistry |
| 2015 | High | AHNAK directly interacts with SMAD1 and facilitates Smad1 binding to the PPARγ2 promoter, thereby stimulating BMP2-mediated adipocyte differentiation; loss of AHNAK impairs Smad1 phosphorylation and nuclear localization, downregulates PPARγ expression, and severely impairs adipocyte differentiation. | PMID:26466345 | PloS one |
| 2016 | Medium | AHNAK is the most abundant protein component of extracellular vesicles produced by mammary carcinoma cells and is necessary for their formation; AHNAK-depleted carcinoma cells produce fewer vesicles that are less capable of promoting recipient fibroblast migration. | PMID:27374178 | Oncotarget |
| 2018 | Medium | UBE3C ubiquitin E3 ligase ubiquitinates AHNAK and promotes its proteasomal degradation; AHNAK functions as a cofactor assisting p53 binding to stemness-related gene promoters to inhibit transcription; UBE3C-mediated AHNAK degradation removes this p53-mediated inhibition, enhancing cancer stem cell properties. | PMID:30503554 | Cancer letters |
| 2018 | Medium | Ahnak induces EMT in response to TGFβ by activating Smad3 phosphorylation and enhancing Smad3 transcriptional activity; stable knockdown of Ahnak in B16F10 cells reduces N-cadherin expression and Smad3 phosphorylation, and abrogates TGFβ-induced migration, invasion, and lung metastasis in C57BL/6 mice. | PMID:30258109 | Scientific reports |
| 2019 | Medium | RNF38 RING-finger E3 ubiquitin ligase ubiquitinates and degrades AHNAK, thereby relieving AHNAK-mediated inhibition of TGFβ signaling and promoting HCC cell migration and invasion; re-introduction of AHNAK interference restores invasion capacity diminished by RNF38 downregulation. | PMID:30836988 | Journal of experimental & clinical cancer research |
| 2019 | High | Ahnak scaffolds the p11 (S100A10)/Anxa2 complex and L-type VGCC: through its N-terminal region it interacts with the pore-forming α1 subunit, and through its C-terminal region it interacts with the β subunit and the p11/Anxa2 complex. Ahnak knockout neurons show reduced α1 surface expression and L-type Ca2+ current, and constitutive or forebrain-specific Ahnak KO mice display depression-like behavior similar to p11 KO mice. | PMID:30760886 | Molecular psychiatry |
| 2019 | Medium | AHNAK C-terminal peptide (residues 5654–5673) preferentially and strongly binds negatively charged phospholipids with unsaturated acyl chains, established by Langmuir monolayer tensiometry, ellipsometry, and 31P solid-state NMR on lipid bilayers. | PMID:31825630 | Langmuir |
| 2021 | High | AHNAK binds to the 53BP1 oligomerization domain and controls 53BP1 multimerization and phase separation; loss of AHNAK results in hyper-accumulation of 53BP1 on chromatin, enhanced phase separation, and elevated p53 response, leading to senescence in non-transformed cells and sensitizing cancer cells. | PMID:33961796 | Molecular cell |
| 2021 | Medium | Ahnak regulates tumor metastasis colonization through PCSK9 expression: Ahnak-/- mice show higher resistance to pulmonary B16F10 metastasis; transcriptomic analysis of Ahnak-/- pulmonary endothelial cells reveals PCSK9 downregulation, and lung epithelium-specific PCSK9 conditional KO mice also show suppressed B16F10 pulmonary metastasis. | PMID:34352405 | Neoplasia |
| 2022 | High | In mitotic HeLa cells, annexin A2 (Anx2) recruits AHNAK to the cell cortex facing spindle poles; depletion of either protein or impaired cortical AHNAK localization causes delayed anaphase onset and unstable spindle anchoring, resulting in altered spindle orientation; AHNAK is found in a complex with dynein-dynactin, and both AHNAK and Anx2 are required for correct NuMA and dynein cortical localization and dynamics. | PMID:35362526 | Journal of cell science |
| 2014 | High | AHNAK1 modulates L-type Ca2+ channel inactivation in cardiomyocytes; in vitro binding studies show that the most C-terminal 188 aa of ahnak1 containing a PxxP motif (188-PSTP) binds Cavβ2 with Kd ~60 nM, while proline-to-alanine substitutions reduce affinity ~20-fold; both 188-PSTP and 188-ASTA affect I(CaL) only in ahnak1-expressing cardiomyocytes and not in ahnak1-deficient cardiomyocytes, demonstrating that endogenous ahnak1 is required. | PMID:20607281 | Pflugers Archiv : European journal of physiology |
| 2014 | High | AHNAK1 co-localizes with β-dystroglycan in Cajal bands of myelinated Schwann cells; β-dystroglycan co-immunoprecipitates with AHNAK1, shows reduced expression in ahnak1-/- Schwann cells, and is undetectable in Cajal bands of ahnak1-/- sciatic nerve. AHNAK1-deficient Schwann cells show reduced migration velocity on laminin, greater mechanical rigidity of processes, and decreased internodal lengths, suggesting AHNAK1 links dystroglycan to F-actin to regulate Schwann cell morphology and myelination. | PMID:24796807 | Glia |

## Citations

- PMID:10318799
- PMID:10593863
- PMID:10771490
- PMID:11312263
- PMID:11535620
- PMID:12153988
- PMID:14699089
- PMID:14722071
- PMID:15001564
- PMID:15033986
- PMID:15177040
- PMID:1608957
- PMID:16319140
- PMID:16984913
- PMID:17185750
- PMID:18174170
- PMID:18191595
- PMID:18837049
- PMID:19261907
- PMID:19497879
- PMID:19710363
- PMID:20607281
- PMID:20833135
- PMID:21940993
- PMID:22057634
- PMID:22497893
- PMID:23042471
- PMID:23275167
- PMID:24662814
- PMID:24675079
- PMID:24796807
- PMID:26466345
- PMID:27374178
- PMID:30258109
- PMID:30503554
- PMID:30760886
- PMID:30836988
- PMID:31825630
- PMID:33961796
- PMID:34352405
- PMID:35362526
- PMID:7698224
- PMID:7769263
- PMID:8381120
- PMID:8408266
