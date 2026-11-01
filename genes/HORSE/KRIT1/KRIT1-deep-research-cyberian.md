---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:08:25.883372'
end_time: '2026-10-26T03:17:44.342267'
duration_seconds: 558.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: KRIT1
  gene_symbol: KRIT1
  uniprot_accession: A0A9L0SR44
  protein_description: 'RecName: Full=Krev interaction trapped protein 1 {ECO:0000256|ARBA:ARBA00073312};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    ARM_KRIT1. (IPR056485); Band_41_domain. (IPR019749); FERM/acyl-CoA-bd_prot_sf.
    (IPR014352)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 80
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0SR44
- **Protein Description:** RecName: Full=Krev interaction trapped protein 1 {ECO:0000256|ARBA:ARBA00073312};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); ARM_KRIT1. (IPR056485); Band_41_domain. (IPR019749); FERM/acyl-CoA-bd_prot_sf. (IPR014352)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRIT1" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRIT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRIT1** (gene ID: KRIT1, UniProt: A0A9L0SR44) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRIT1 (Krev interaction trapped protein 1) in the horse, *Equus caballus* — UniProt A0A9L0SR44

## 1. Introduction and summary

UniProt A0A9L0SR44 is an unreviewed (TrEMBL) entry for horse Krev interaction trapped protein 1 (KRIT1, also called CCM1). It was predicted automatically from the Thoroughbred reference genome [wade-2009-horse-genome-abstract] via the Ensembl gene model ENSECAG00000016850 (transcript ENSECAT00000146800.1) on horse chromosome 4. The entry carries no gene name, but its recommended name, domain architecture (an N-terminal Nudix-like region, an ankyrin repeat domain, the KRIT1-specific ARM/ankyrin module and a FERM domain), PANTHER assignment (PTHR13283:SF11, "Krev interaction trapped protein 1") and sequence all identify it as the horse ortholog of human KRIT1. A pairwise alignment I ran against human KRIT1 (UniProt O00522) gives 708 identical residues out of 736 (about 96%). The only length difference is at the extreme C-terminus, where the horse model ends with a different 7-residue tail and is 17 residues shorter (719 vs 736 aa) (notes/sequence-comparison.md). The canonical horse KRIT1 isoform from the same gene (UniProt A0A3Q2GZV2, 736 aa) has the human-type C-terminus and is 98.6% identical to human KRIT1. A0A9L0SR44 is a predicted alternative-3′-exon variant of that gene (Section 2). The gene symbol KRIT1 is therefore unambiguous for this protein. I found **no published experimental study of KRIT1 in the horse**, including searches for equine cavernous malformations. Everything below on function is inferred by orthology from human, mouse, zebrafish and biochemical/structural studies of KRIT1. That inference rests on near-identity of sequence and complete conservation of the known functional motifs.

KRIT1 has no enzymatic activity. It is a multidomain scaffold or adaptor protein, and no catalytic function has been attributed to it or to its partners CCM2 and PDCD10 [hilder-2007-ccm-complex-proteomics-abstract]. Its main job, defined mostly in vascular endothelial cells, is to keep endothelium quiescent and stable. It does this in four ways. First, it acts as a membrane-anchored effector of the small GTPase Rap1 at cell–cell junctions [glading-2007-krit1-rap1-junctions-abstract]. Second, it binds the transmembrane receptor HEG1 [kleaveland-2009-heg-ccm-abstract; gingras-2013-krit1-rap1-heg1-abstract]. Third, it binds the integrin regulator ICAP1, which affects β1 integrin activation [zawistowski-2002-krit1-icap1-abstract; liu-2013-krit1-icap1-mechanism-abstract]. Fourth, it nucleates the CCM complex with CCM2 and PDCD10, which restrains the MEKK3–MEK5–ERK5–KLF2/KLF4 transcriptional pathway and RhoA/ROCK-driven contractility [zawistowski-2005-ccm1-ccm2-abstract; stockton-2010-ccm-rock-abstract; zhou-2016-mekk3-klf2-klf4-abstract; cuttano-2016-klf4-ccm-abstract]. In humans, loss-of-function mutations in KRIT1 cause familial cerebral cavernous malformations type 1 (CCM1) [sahoo-1999-krit1-ccm1-abstract; labergelecouteulx-1999-ccm1-truncating-abstract]. KRIT1 is found at endothelial cell–cell junctions, at the inner face of the plasma membrane, on microtubules, in the cytoplasm and in the nucleus. It moves between these compartments under the control of Rap1, ICAP1, CCM2, PKCα and redox state [gunel-2002-krit1-microtubule-abstract; beraud-dufour-2007-krit1-microtubules-abstract; francalanci-2009-krit1-isoforms-abstract; de-luca-2021-pkca-krit1-shuttling-abstract].

## 2. Identity verification and conservation of the horse protein

KRIT1 was first cloned in a yeast two-hybrid screen that used the Ras-family GTPase Krev-1/Rap1A as bait. The original cDNA encoded an N-terminally truncated product with an ankyrin repeat region and a novel C-terminal domain that was needed for Rap1A binding. Krit1 bound Rap1A strongly but Ras only weakly [serebriiskii-1997-krit1-rap1a-abstract]. Later cloning added four 5′ coding exons, giving the full-length 736-residue, roughly 75 kDa protein [glading-2024-krit1-review-fulltext]. The horse entry matches this full-length architecture. The InterPro/Pfam signatures listed for A0A9L0SR44 (Ankyrin_rpt IPR002110, ARM_KRIT1 IPR056485, Band 4.1/FERM IPR019749/IPR000299, NUDIX IPR032022, KRIT1/FRMD8 IPR051594) correspond to the domains defined by crystallography of human and mouse KRIT1. These are an N-terminal Nudix fold that was originally thought to be unstructured [liu-2013-krit1-icap1-mechanism-abstract]; a four-repeat ankyrin repeat domain that packs stably against the FERM domain to form a globular ARD–FERM module, analogous to the F0–FERM arrangement in talin [zhang-2015-krit1-ard-ferm-abstract]; and a C-terminal FERM domain made of F1, F2 and F3 lobes [li-2012-krit1-rap1-structure-abstract].

The binding determinants defined in human KRIT1 are conserved residue-for-residue in the horse sequence (notes/sequence-comparison.md). All three NPx(Y/F) motifs sit at identical positions: NPAY at 192–195, NPLF at 231–234 and NPYF at 250–253. These motifs bind the PTB domains of ICAP1 and CCM2 [zawistowski-2002-krit1-icap1-abstract; fisher-2015-krit1-ccm2-structure-abstract; huet-calderwood-2026-ccm2-dual-krit1-abstract]. Lys570 is also conserved. It forms the ionic contact with Rap1 that gives KRIT1 its specificity for Rap1 over H-Ras [gingras-2013-krit1-rap1-heg1-abstract]. So is Trp404, which stabilizes the unusual fourth ankyrin repeat [zhang-2015-krit1-ard-ferm-abstract]. The one notable difference is the C-terminus. In human KRIT1 the last residues belong to the F3 lobe of the FERM domain. This lobe binds Rap1 together with F1/F2 and forms half of the HEG1-binding pocket at the F1/F3 interface [li-2012-krit1-rap1-structure-abstract; gingras-2013-krit1-rap1-heg1-abstract]. Alternative splicing in this region is known to matter: the human KRIT1B isoform, which lacks exon 15 and with it the distal β-sheet of the F3/PTB-like lobe, cannot bind Rap1A and cannot shuttle between nucleus and cytoplasm [francalanci-2009-krit1-isoforms-abstract]. The horse gene model data partly explain the difference. The single horse KRIT1 gene (Ensembl ENSECAG00000016850, chromosome 4) is annotated with seven protein-coding transcripts. The longest canonical product, UniProt A0A3Q2GZV2 (736 aa, gene name KRIT1), is identical to A0A9L0SR44 over residues 1–712. It then continues with a human-type C-terminus (…HTKQAGLVIKLLIKLNGQLMPTERNS) and is 98.6% identical to human KRIT1 overall. An independent equine mRNA from a normalized cDNA library (EMBL JL636856; UniProt fragment K9KCP7) matches this canonical C-terminus exactly. Exon coordinates show that the transcript encoding A0A9L0SR44 (ENSECAT00000146800) skips the canonical 3′-terminal coding exon and uses an alternative, more downstream terminal exon, which produces the divergent …TKKQS tail (notes/sequence-comparison.md). A0A9L0SR44 is therefore best read as a predicted alternative-last-exon isoform of horse KRIT1, not the main gene product. This differs from the experimentally characterized human KRIT1B, which lacks an internal exon (exon 15) [francalanci-2009-krit1-isoforms-abstract]. Because the truncation falls in the F3 lobe, this isoform could have weaker HEG1 or Rap1 binding than full-length KRIT1, but that has not been tested (see Open Questions).

## 3. Molecular function: a FERM-domain scaffold and Rap1 effector

KRIT1's core molecular function is that of a GTPase effector and adaptor. Biochemical work showed that KRIT1 binds Rap1A preferentially in its GTP-bound state, and that the FERM domain alone is enough for this binding [beraud-dufour-2007-krit1-microtubules-abstract; francalanci-2009-krit1-isoforms-abstract]. The 1.95 Å co-crystal structure of the KRIT1 FERM domain with Rap1 shows an extended interface. Rap1 switch I and switch II contact the F1 and F2 lobes. The F1 contact follows a canonical GTPase–ubiquitin-like-fold mode, while the F2 contact is novel. The F2/F3 lobes closely resemble talin, which led the authors to propose a talin–myosin–FAK–KRIT ("TMFK-like") class of FERM domains [li-2012-krit1-rap1-structure-abstract]. A later ternary structure showed that the KRIT1 FERM domain can bind Rap1 and the cytoplasmic tail of the transmembrane protein HEG1 at the same time. Rap1 sits on F1/F2, while HEG1 inserts into a hydrophobic pocket at the F1/F3 interface. The two do not compete: HEG1 binds KRIT1 with similar affinity whether or not Rap1 is bound (K<sub>d</sub> about 1 µM). In the complex, the Rap1 switch II remains free for other effectors [gingras-2013-krit1-rap1-heg1-abstract]. These structures support a model in which HEG1 anchors a KRIT1–Rap1 complex at the endothelial plasma membrane.

The N-terminal half of KRIT1 is a second binding platform. Its NPAY motif binds the PTB domain of ICAP1 (integrin cytoplasmic domain-associated protein-1), a negative regulator of β1 integrin activation [zawistowski-2002-krit1-icap1-abstract]. Crystal structures showed that KRIT1 grips ICAP1 through a bidentate surface that includes the newly recognized Nudix fold. They also showed that KRIT1 competes directly with the β1 integrin tail for ICAP1, so KRIT1 can relieve ICAP1-mediated suppression of integrin activation [liu-2013-krit1-icap1-mechanism-abstract]. The NPLF and NPYF motifs bind the PTB domain of CCM2 (malcavernin/OSM). CCM2 prefers the third motif [fisher-2015-krit1-ccm2-structure-abstract]. Recent work shows that two CCM2 molecules can bind a single KRIT1 at the second and third NPxF motifs at once, and that this clustering is needed to keep KLF4 expression low [huet-calderwood-2026-ccm2-dual-krit1-abstract]. KRIT1 binds CCM2 through the CCM2 PTB domain, and CCM2 in turn binds MEKK3, so KRIT1 can sit in a ternary KRIT1–CCM2–MEKK3 complex [zawistowski-2005-ccm1-ccm2-abstract]. Proteomic purification of CCM2 complexes recovered KRIT1, ICAP1, MEKK3, Rac and PDCD10 together. This defined a larger CCM signalling complex made entirely of adaptor proteins [hilder-2007-ccm-complex-proteomics-abstract].

Intramolecular regulation adds another layer. Like other FERM proteins, KRIT1 can take a "closed" conformation in which an N-terminal NPx(Y/F) motif folds back onto the FERM domain, or an "open" conformation. ICAP1 binding opens KRIT1, whereas Rap1 can bind either form [beraud-dufour-2007-krit1-microtubules-abstract]. Mapping by Francalanci and colleagues placed the closing contact between the third NPXY/F motif and the F3/PTB-like lobe. They proposed that this switch controls nuclear entry and Rap1 binding in a mutually exclusive way [francalanci-2009-krit1-isoforms-abstract]. KRIT1 also binds membranes containing phosphatidylinositol 4,5-bisphosphate, and Rap1 increases this binding [beraud-dufour-2007-krit1-microtubules-abstract].

## 4. Subcellular localization and its regulation

UniProt's automatic annotation for A0A9L0SR44 assigns the protein to cell junctions, the cell membrane as a peripheral membrane protein, and the cytoskeleton (UniProt entry, ARBA rules). Experimental work on the mammalian orthologs supports each of these and adds the nucleus. In endothelial cells, endogenous KRIT1 colocalizes and co-immunoprecipitates with microtubules. In mitosis it decorates spindle poles, the spindle, microtubule plus ends and the midbody [gunel-2002-krit1-microtubule-abstract]. KRIT1 binds microtubules directly through its N- and C-termini in sedimentation assays. Active Rap1 or ICAP1 releases it from microtubules, and co-expressing activated Rap1V12 moves YFP-KRIT1 off microtubules in cells. This suggests a model in which microtubules deliver KRIT1 to the plasma membrane, where Rap1 and ICAP1 capture it [beraud-dufour-2007-krit1-microtubules-abstract]. Structural studies describe the same idea of Rap1 moving KRIT1 from microtubules to membranes [li-2012-krit1-rap1-structure-abstract].

At the plasma membrane, KRIT1 concentrates at endothelial cell–cell junctions. It associates with junctional proteins through its FERM domain, and Rap1 activity increases this junctional targeting [glading-2007-krit1-rap1-junctions-abstract]. Junctional localization also needs the KRIT1–CCM2 interaction [stockton-2010-ccm-rock-abstract] and is supported by the junctional transmembrane receptor HEG1 [kleaveland-2009-heg-ccm-abstract; gingras-2013-krit1-rap1-heg1-abstract]. CCM2 and ICAP1, each bound through its own PTB domain, shift KRIT1's subcellular distribution in different directions [zawistowski-2005-ccm1-ccm2-abstract].

KRIT1 also enters the nucleus. Nucleocytoplasmic shuttling needs an intact F3/PTB-like lobe; the KRIT1B splice isoform, which lacks part of this lobe, stays in the cytoplasm and acts as a dominant negative [francalanci-2009-krit1-isoforms-abstract]. Shuttling is controlled by redox state and protein kinase C. PKC activation, specifically through PKCα, drives KRIT1 into the cytoplasm in a redox-dependent way. PKC inhibition or the antioxidant N-acetylcysteine causes KRIT1 to accumulate in the nucleus, and the N-terminal region of KRIT1 is needed for this regulation [de-luca-2021-pkca-krit1-shuttling-abstract]. The function of nuclear KRIT1 is still poorly defined [glading-2024-krit1-review-abstract].

## 5. Signalling pathways controlled by KRIT1

### 5.1 Rap1–KRIT1 stabilization of endothelial adherens junctions

The first well-defined cellular function of KRIT1 was as the Rap1 effector that stabilizes endothelial junctions. Depleting KRIT1 with siRNA blocked Rap1's ability to stabilize endothelial junctions and increased actin stress fibres. This placed KRIT1 downstream of Rap1 in suppressing stress fibres and maintaining junctional integrity [glading-2007-krit1-rap1-junctions-abstract]. Later reviews describe how losing KRIT1 destabilizes adherens junctions, increases β-catenin-dependent transcription and VEGF signalling, and raises endothelial permeability [glading-2024-krit1-review-fulltext; perrelli-2023-krit1-redox-review-abstract]. Rescue experiments now suggest that the mechanism is more complicated than direct Rap1 coupling. In KRIT1-deficient endothelial cells, KRIT1 mutants that cannot bind Rap1 or ICAP1, or that cannot reach junctions, still restored adherens junction protein localization and barrier function. Successful rescue tracked instead with lower β1 integrin activity and preserved cortical actin [swamy-2022-krit1-barrier-ppi-abstract].

### 5.2 Suppression of RhoA/ROCK signalling

KRIT1 together with CCM2 restrains RhoA and its effector Rho kinase (ROCK). Loss of either protein, or disruption of their interaction, keeps RhoA/ROCK active and destabilizes barrier function. *Krit1*<sup>+/−</sup> mice show increased vascular leak that the ROCK inhibitor fasudil reverses. Human CCM endothelium shows signs of ROCK hyperactivity [stockton-2010-ccm-rock-abstract]. More detailed work showed that the CCM1–CCM2 complex scaffolds ROCK2 with VE-cadherin and limits ROCK1 kinase activity. KRIT1 loss produces ROCK1-dependent stress fibres, and silencing ROCK1 but not ROCK2 rescues endothelial mechanics and the cardiovascular defects of *ccm1* mutant zebrafish [lisowska-2018-ccm1-ccm2-rock1-rock2-abstract].

### 5.3 The HEG1–KRIT1–CCM2 axis and MEKK3–KLF2/4 transcription

The pathway with the strongest genetic support links the endothelial transmembrane receptor HEG1, through KRIT1 and CCM2, to the MAP3 kinase MEKK3. HEG1 is expressed selectively in endothelium, couples to KRIT1 at cell junctions, and interacts genetically with *Ccm2*. In mouse and zebrafish, loss of *heg*, *krit1* or *ccm2* causes the same failure of endothelial cells to assemble into patent, stable vessels, along with abnormal junctions [kleaveland-2009-heg-ccm-abstract]. In this complex, CCM2 binds MEKK3 and the CCM complex holds MEKK3 signalling in check. Endothelial loss of CCM proteins increases expression of the MEKK3 target transcription factors KLF2 and KLF4 and raises Rho and ADAMTS protease activity. Endothelial deletion of *Map3k3* (MEKK3), *Klf2* or *Klf4* prevents lesion formation in a neonatal CCM mouse model [zhou-2016-mekk3-klf2-klf4-abstract]. Specifically, *Ccm1* ablation switches on a MEKK3–MEK5–ERK5–MEF2 axis that drives KLF4. KLF4 then promotes BMP6/TGF-β signalling and endothelial-to-mesenchymal transition, and co-deleting *Klf4* strongly reduces CCM in *Ccm1* mutant mice [cuttano-2016-klf4-ccm-abstract; maddaluno-2013-endmt-ccm-abstract]. A related β1 integrin–KLF2–EGFL7 pathway is also restrained by CCM proteins, independently of blood flow, in zebrafish and human endothelial cells [renz-2015-ccm-beta1-integrin-klf2-abstract]. Two CCM2 PTB domains must cluster on one KRIT1 molecule to suppress KLF4 expression, which links KRIT1's NPxF motifs directly to transcriptional control [huet-calderwood-2026-ccm2-dual-krit1-abstract]. Together these results suggest that KRIT1's main signalling job is to act as the membrane-proximal anchor of a CCM2-based inhibitory complex that keeps MEKK3–KLF2/4 activity low in quiescent endothelium.

### 5.4 Integrin signalling via ICAP1

By binding ICAP1 at the same surface ICAP1 uses for the β1 integrin tail, KRIT1 works as a switch on β1 integrin "inside-out" activation [liu-2013-krit1-icap1-mechanism-abstract; zawistowski-2002-krit1-icap1-abstract]. Several studies link β1 integrin activity to CCM phenotypes. β1 integrin depletion rescues *ccm* cardiovascular defects in zebrafish [renz-2015-ccm-beta1-integrin-klf2-abstract], and KRIT1's barrier-rescue activity correlates with reduced β1 integrin activation [swamy-2022-krit1-barrier-ppi-abstract]. This makes the KRIT1–ICAP1–β1 integrin axis a plausible contributor to KRIT1's role in balancing cell–matrix and cell–cell adhesion.

### 5.5 Redox homeostasis and autophagy

A separate line of research ties KRIT1 to redox control and protein quality control. KRIT1 loss raises intracellular reactive oxygen species, and re-expressing KRIT1 lowers them. This effect tracks with expression of FoxO1 and the mitochondrial antioxidant SOD2. KRIT1-dependent low ROS supports cyclin D1 downregulation and entry into quiescence, and KRIT1-null cells suffer more oxidative DNA damage [goitre-2010-krit1-ros-abstract]. KRIT1 ablation also suppresses autophagy by activating mTOR–ULK1, which causes p62/SQSTM1 to accumulate. mTOR inhibitors rescue some of these phenotypes [marchi-2015-ccm-autophagy-abstract]. Reviews of this work argue that redox signalling may be the common thread connecting the various KRIT1-dependent pathways [perrelli-2023-krit1-redox-review-abstract]. The redox-dependent, PKCα-regulated nuclear shuttling of KRIT1 [de-luca-2021-pkca-krit1-shuttling-abstract] could link these roles to its compartmentalization.

## 6. Physiological roles revealed by loss of function

Genetic studies in mammals and fish define KRIT1's physiological role as a regulator of vascular development and stability. Mice lacking *Ccm1* die at mid-gestation. Their first defects are purely vascular: dilated cranial vessels, an enlarged and hyperproliferative dorsal aorta, narrowed branchial arch arteries and early loss of arterial markers such as Notch-pathway genes. *Ccm1* is ubiquitously expressed in the early embryo [whitehead-2004-ccm1-arterial-abstract]. In zebrafish, loss of *krit1* phenocopies loss of *heg* and *ccm2* [kleaveland-2009-heg-ccm-abstract]. In humans, heterozygous loss-of-function KRIT1 mutations, often truncating, cause autosomal dominant familial cerebral cavernous malformations. These are clusters of dilated, leaky capillary-venous channels in the central nervous system. A founder mutation is common in Hispanic-American families [sahoo-1999-krit1-ccm1-abstract; labergelecouteulx-1999-ccm1-truncating-abstract]. Lesion endothelium shows the expected downstream signatures: ROCK hyperactivity [stockton-2010-ccm-rock-abstract], increased KLF2/KLF4 [zhou-2016-mekk3-klf2-klf4-abstract] and defective autophagy [marchi-2015-ccm-autophagy-abstract]. KRIT1 is widely expressed, and roles outside the endothelium have been reported, including tumour-suppressor-like effects on β-catenin signalling in intestinal and other epithelia [glading-2024-krit1-review-fulltext]. These roles are less well characterized than the endothelial ones.

No spontaneous KRIT1-associated vascular disease, CCM-like lesion or functional study has been reported in horses in the literature I searched. Given 96% sequence identity and full conservation of the Rap1-, HEG1-, ICAP1- and CCM2-binding determinants, it is reasonable to predict that equine KRIT1 performs the same scaffolding functions in equine endothelium. This prediction is untested.

## 7. Synthesis: the predicted functional profile of horse KRIT1

Taken together, the evidence supports the following annotation for the horse KRIT1 protein (A0A9L0SR44), inferred from orthologs. Its molecular function is non-catalytic. It is a scaffold or adaptor that binds the small GTPase Rap1 (GTP-bound form), the HEG1 cytoplasmic tail, the PTB domains of ICAP1 and CCM2, microtubules and PI(4,5)P2-containing membranes [li-2012-krit1-rap1-structure-abstract; gingras-2013-krit1-rap1-heg1-abstract; liu-2013-krit1-icap1-mechanism-abstract; fisher-2015-krit1-ccm2-structure-abstract; beraud-dufour-2007-krit1-microtubules-abstract]. Its main cellular locations are endothelial cell–cell (adherens) junctions and the cytoplasmic face of the plasma membrane. It is also found on microtubules, in the cytoplasm and in the nucleus [glading-2007-krit1-rap1-junctions-abstract; gunel-2002-krit1-microtubule-abstract; francalanci-2009-krit1-isoforms-abstract; de-luca-2021-pkca-krit1-shuttling-abstract]. Its biological roles are to maintain endothelial barrier integrity and quiescence, to negatively regulate RhoA/ROCK signalling and stress fibre formation [stockton-2010-ccm-rock-abstract; lisowska-2018-ccm1-ccm2-rock1-rock2-abstract], to negatively regulate MEKK3–MEK5–ERK5–KLF2/KLF4 signalling and endothelial-to-mesenchymal transition [zhou-2016-mekk3-klf2-klf4-abstract; cuttano-2016-klf4-ccm-abstract], to modulate β1 integrin activation through ICAP1 [liu-2013-krit1-icap1-mechanism-abstract], to limit ROS and support autophagy [goitre-2010-krit1-ros-abstract; marchi-2015-ccm-autophagy-abstract], and to support blood vessel and heart development [whitehead-2004-ccm1-arterial-abstract; kleaveland-2009-heg-ccm-abstract]. The UniProt automatic GO terms for this entry (anchoring junction, cytoskeleton, plasma membrane, negative regulation of developmental process) agree with this picture but are much less specific than what the orthologous literature supports.

## 8. Open Questions

The most immediate open question for this entry is whether the A0A9L0SR44 isoform is actually expressed. Database evidence shows that the canonical horse KRIT1 (A0A3Q2GZV2) has the conserved human-type C-terminus, supported by an equine cDNA (K9KCP7/JL636856). A0A9L0SR44 instead comes from an Ensembl transcript that uses an alternative terminal exon and ends within the FERM F3 lobe. The F3 lobe helps form the HEG1-binding pocket [gingras-2013-krit1-rap1-heg1-abstract], and its integrity is needed for Rap1 binding and nuclear shuttling [francalanci-2009-krit1-isoforms-abstract]. Equine RNA-seq or long-read data (for example FAANG tissue transcriptomes) are needed to test whether this splice junction is used and at what level. If the isoform is real, structural modelling (for example comparing the AlphaFold models of A0A9L0SR44 and A0A3Q2GZV2) and binding assays could test whether HEG1 and Rap1 binding are kept. Until then, functional annotation of A0A9L0SR44 should be transferred from the canonical KRIT1 with this caveat.

More broadly, KRIT1 has not been studied experimentally in horses. Useful follow-up would include confirming expression in equine endothelium (for example from Expression Atlas baseline data linked to this entry), checking equine variant databases for loss-of-function KRIT1 alleles, and asking whether any equine neurovascular malformations resemble human CCM. At the mechanistic level, the field still has not settled how important Rap1/junctional coupling is compared with β1 integrin/ICAP1 and CCM2–MEKK3 control for barrier function [swamy-2022-krit1-barrier-ppi-abstract]. The function of nuclear KRIT1 and of its redox-regulated shuttling is not understood [de-luca-2021-pkca-krit1-shuttling-abstract; glading-2024-krit1-review-abstract]. How the N-terminal Nudix-like fold, which appears to have no catalytic residues, and the ankyrin repeat groove [zhang-2015-krit1-ard-ferm-abstract] contribute to partner binding also remains open. Finally, the recent finding that two CCM2 molecules must cluster on one KRIT1 to suppress KLF4 [huet-calderwood-2026-ccm2-dual-krit1-abstract] raises questions about the stoichiometry and dynamics of the native CCM complex in cells.

## 9. References

- **beraud-dufour-2007-krit1-microtubules** — Béraud-Dufour S, Gautier R, Albiges-Rizo C, Chardin P, Faurobert E. (2007). Krit 1 interactions with microtubules and membranes are regulated by Rap1 and integrin cytoplasmic domain associated protein-1. The FEBS journal 274:5518-5532. PMID: 17916086 (https://pubmed.ncbi.nlm.nih.gov/17916086/); PMCID: PMC2580780; DOI: 10.1111/j.1742-4658.2007.06068.x (https://doi.org/10.1111/j.1742-4658.2007.06068.x)
- **cuttano-2016-klf4-ccm** — Cuttano R, Rudini N, Bravi L, Corada M, Giampietro C, Papa E, Morini MF, Maddaluno L, Baeyens N, Adams RH, Jain MK, Owens GK, Schwartz M, Lampugnani MG, Dejana E. (2016). KLF4 is a key determinant in the development and progression of cerebral cavernous malformations. EMBO molecular medicine 8:6-24. PMID: 26612856 (https://pubmed.ncbi.nlm.nih.gov/26612856/); PMCID: PMC4718159; DOI: 10.15252/emmm.201505433 (https://doi.org/10.15252/emmm.201505433)
- **de-luca-2021-pkca-krit1-shuttling** — De Luca E, Perrelli A, Swamy H, Nitti M, Passalacqua M, Furfaro AL, Salzano AM, Scaloni A, Glading AJ, Retta SF. (2021). Protein kinase Cα regulates the nucleocytoplasmic shuttling of KRIT1. Journal of cell science 134:jcs250217. PMID: 33443102 (https://pubmed.ncbi.nlm.nih.gov/33443102/); PMCID: PMC7875496; DOI: 10.1242/jcs.250217 (https://doi.org/10.1242/jcs.250217)
- **fisher-2015-krit1-ccm2-structure** — Fisher OS, Liu W, Zhang R, Stiegler AL, Ghedia S, Weber JL, Boggon TJ. (2015). Structural basis for the disruption of the cerebral cavernous malformations 2 (CCM2) interaction with Krev interaction trapped 1 (KRIT1) by disease-associated mutations. The Journal of biological chemistry 290:2842-2853. PMID: 25525273 (https://pubmed.ncbi.nlm.nih.gov/25525273/); PMCID: PMC4317034; DOI: 10.1074/jbc.m114.616433 (https://doi.org/10.1074/jbc.m114.616433)
- **francalanci-2009-krit1-isoforms** — Francalanci F, Avolio M, De Luca E, Longo D, Menchise V, Guazzi P, Sgrò F, Marino M, Goitre L, Balzac F, Trabalzini L, Retta SF. (2009). Structural and functional differences between KRIT1A and KRIT1B isoforms: a framework for understanding CCM pathogenesis. Experimental cell research 315:285-303. PMID: 18992740 (https://pubmed.ncbi.nlm.nih.gov/18992740/); DOI: 10.1016/j.yexcr.2008.10.006 (https://doi.org/10.1016/j.yexcr.2008.10.006)
- **gingras-2013-krit1-rap1-heg1** — Gingras AR, Puzon-McLaughlin W, Ginsberg MH. (2013). The structure of the ternary complex of Krev interaction trapped 1 (KRIT1) bound to both the Rap1 GTPase and the heart of glass (HEG1) cytoplasmic tail. The Journal of biological chemistry 288:23639-23649. PMID: 23814056 (https://pubmed.ncbi.nlm.nih.gov/23814056/); PMCID: PMC3745310; DOI: 10.1074/jbc.m113.462911 (https://doi.org/10.1074/jbc.m113.462911)
- **glading-2007-krit1-rap1-junctions** — Glading A, Han J, Stockton RA, Ginsberg MH. (2007). KRIT-1/CCM1 is a Rap1 effector that regulates endothelial cell cell junctions. The Journal of cell biology 179:247-254. PMID: 17954608 (https://pubmed.ncbi.nlm.nih.gov/17954608/); PMCID: PMC2064761; DOI: 10.1083/jcb.200705175 (https://doi.org/10.1083/jcb.200705175)
- **glading-2024-krit1-review** — Glading AJ. (2024). KRIT1 in vascular biology and beyond. Bioscience reports 44:BSR20231675. PMID: 38980708 (https://pubmed.ncbi.nlm.nih.gov/38980708/); PMCID: PMC11263069; DOI: 10.1042/bsr20231675 (https://doi.org/10.1042/bsr20231675)
- **goitre-2010-krit1-ros** — Goitre L, Balzac F, Degani S, Degan P, Marchi S, Pinton P, Retta SF. (2010). KRIT1 regulates the homeostasis of intracellular reactive oxygen species. PloS one 5:e11786. PMID: 20668652 (https://pubmed.ncbi.nlm.nih.gov/20668652/); PMCID: PMC2910502; DOI: 10.1371/journal.pone.0011786 (https://doi.org/10.1371/journal.pone.0011786)
- **gunel-2002-krit1-microtubule** — Gunel M, Laurans MS, Shin D, DiLuna ML, Voorhees J, Choate K, Nelson-Williams C, Lifton RP. (2002). KRIT1, a gene mutated in cerebral cavernous malformation, encodes a microtubule-associated protein. Proceedings of the National Academy of Sciences of the United States of America 99:10677-10682. PMID: 12140362 (https://pubmed.ncbi.nlm.nih.gov/12140362/); PMCID: PMC125011; DOI: 10.1073/pnas.122354499 (https://doi.org/10.1073/pnas.122354499)
- **hilder-2007-ccm-complex-proteomics** — Hilder TL, Malone MH, Bencharit S, Colicelli J, Haystead TA, Johnson GL, Wu CC. (2007). Proteomic identification of the cerebral cavernous malformation signaling complex. Journal of proteome research 6:4343-4355. PMID: 17900104 (https://pubmed.ncbi.nlm.nih.gov/17900104/); DOI: 10.1021/pr0704276 (https://doi.org/10.1021/pr0704276)
- **huet-calderwood-2026-ccm2-dual-krit1** — Huet-Calderwood C, Fisher OS, Das S, Su VL, Boggon TJ, Calderwood DA. (2026). Dual recruitment of two CCM2 molecules to KRIT1 suppresses KLF4 expression. Nature communications 17:2719. PMID: 41688454 (https://pubmed.ncbi.nlm.nih.gov/41688454/); PMCID: PMC13013565; DOI: 10.1038/s41467-026-69595-7 (https://doi.org/10.1038/s41467-026-69595-7)
- **kleaveland-2009-heg-ccm** — Kleaveland B, Zheng X, Liu JJ, Blum Y, Tung JJ, Zou Z, Sweeney SM, Chen M, Guo L, Lu MM, Zhou D, Kitajewski J, Affolter M, Ginsberg MH, Kahn ML. (2009). Regulation of cardiovascular development and integrity by the heart of glass-cerebral cavernous malformation protein pathway. Nature medicine 15:169-176. PMID: 19151727 (https://pubmed.ncbi.nlm.nih.gov/19151727/); PMCID: PMC2665266; DOI: 10.1038/nm.1918 (https://doi.org/10.1038/nm.1918)
- **labergelecouteulx-1999-ccm1-truncating** — Laberge-le Couteulx S, Jung HH, Labauge P, Houtteville JP, Lescoat C, Cecillon M, Marechal E, Joutel A, Bach JF, Tournier-Lasserve E. (1999). Truncating mutations in CCM1, encoding KRIT1, cause hereditary cavernous angiomas. Nature genetics 23:189-193. PMID: 10508515 (https://pubmed.ncbi.nlm.nih.gov/10508515/); DOI: 10.1038/13815 (https://doi.org/10.1038/13815)
- **li-2012-krit1-rap1-structure** — Li X, Zhang R, Draheim KM, Liu W, Calderwood DA, Boggon TJ. (2012). Structural basis for small G protein effector interaction of Ras-related protein 1 (Rap1) and adaptor protein Krev interaction trapped 1 (KRIT1). The Journal of biological chemistry 287:22317-22327. PMID: 22577140 (https://pubmed.ncbi.nlm.nih.gov/22577140/); PMCID: PMC3381192; DOI: 10.1074/jbc.m112.361295 (https://doi.org/10.1074/jbc.m112.361295)
- **lisowska-2018-ccm1-ccm2-rock1-rock2** — Lisowska J, Rödel CJ, Manet S, Miroshnikova YA, Boyault C, Planus E, De Mets R, Lee HH, Destaing O, Mertani H, Boulday G, Tournier-Lasserve E, Balland M, Abdelilah-Seyfried S, Albiges-Rizo C, Faurobert E. (2018). The CCM1-CCM2 complex controls complementary functions of ROCK1 and ROCK2 that are required for endothelial integrity. Journal of cell science 131:jcs216093. PMID: 30030370 (https://pubmed.ncbi.nlm.nih.gov/30030370/); DOI: 10.1242/jcs.216093 (https://doi.org/10.1242/jcs.216093)
- **liu-2013-krit1-icap1-mechanism** — Liu W, Draheim KM, Zhang R, Calderwood DA, Boggon TJ. (2013). Mechanism for KRIT1 release of ICAP1-mediated suppression of integrin activation. Molecular cell 49:719-729. PMID: 23317506 (https://pubmed.ncbi.nlm.nih.gov/23317506/); PMCID: PMC3684052; DOI: 10.1016/j.molcel.2012.12.005 (https://doi.org/10.1016/j.molcel.2012.12.005)
- **maddaluno-2013-endmt-ccm** — Maddaluno L, Rudini N, Cuttano R, Bravi L, Giampietro C, Corada M, Ferrarini L, Orsenigo F, Papa E, Boulday G, Tournier-Lasserve E, Chapon F, Richichi C, Retta SF, Lampugnani MG, Dejana E. (2013). EndMT contributes to the onset and progression of cerebral cavernous malformations. Nature 498:492-496. PMID: 23748444 (https://pubmed.ncbi.nlm.nih.gov/23748444/); DOI: 10.1038/nature12207 (https://doi.org/10.1038/nature12207)
- **marchi-2015-ccm-autophagy** — Marchi S, Corricelli M, Trapani E, Bravi L, Pittaro A, Delle Monache S, Ferroni L, Patergnani S, Missiroli S, Goitre L, Trabalzini L, Rimessi A, Giorgi C, Zavan B, Cassoni P, Dejana E, Retta SF, Pinton P. (2015). Defective autophagy is a key feature of cerebral cavernous malformations. EMBO molecular medicine 7:1403-1417. PMID: 26417067 (https://pubmed.ncbi.nlm.nih.gov/26417067/); PMCID: PMC4644374; DOI: 10.15252/emmm.201505316 (https://doi.org/10.15252/emmm.201505316)
- **perrelli-2023-krit1-redox-review** — Perrelli A, Ferraris C, Berni E, Glading AJ, Retta SF. (2023). KRIT1: A Traffic Warden at the Busy Crossroads Between Redox Signaling and the Pathogenesis of Cerebral Cavernous Malformation Disease. Antioxidants & redox signaling 38:496-528. PMID: 36047808 (https://pubmed.ncbi.nlm.nih.gov/36047808/); PMCID: PMC10039281; DOI: 10.1089/ars.2021.0263 (https://doi.org/10.1089/ars.2021.0263)
- **renz-2015-ccm-beta1-integrin-klf2** — Renz M, Otten C, Faurobert E, Rudolph F, Zhu Y, Boulday G, Duchene J, Mickoleit M, Dietrich AC, Ramspacher C, Steed E, Manet-Dupé S, Benz A, Hassel D, Vermot J, Huisken J, Tournier-Lasserve E, Felbor U, Sure U, Albiges-Rizo C, Abdelilah-Seyfried S. (2015). Regulation of β1 integrin-Klf2-mediated angiogenesis by CCM proteins. Developmental cell 32:181-190. PMID: 25625207 (https://pubmed.ncbi.nlm.nih.gov/25625207/); DOI: 10.1016/j.devcel.2014.12.016 (https://doi.org/10.1016/j.devcel.2014.12.016)
- **sahoo-1999-krit1-ccm1** — Sahoo T, Johnson EW, Thomas JW, Kuehl PM, Jones TL, Dokken CG, Touchman JW, Gallione CJ, Lee-Lin SQ, Kosofsky B, Kurth JH, Louis DN, Mettler G, Morrison L, Gil-Nagel A, Rich SS, Zabramski JM, Boguski MS, Green ED, Marchuk DA. (1999). Mutations in the gene encoding KRIT1, a Krev-1/rap1a binding protein, cause cerebral cavernous malformations (CCM1). Human molecular genetics 8:2325-2333. PMID: 10545614 (https://pubmed.ncbi.nlm.nih.gov/10545614/); DOI: 10.1093/hmg/8.12.2325 (https://doi.org/10.1093/hmg/8.12.2325)
- **serebriiskii-1997-krit1-rap1a** — Serebriiskii I, Estojak J, Sonoda G, Testa JR, Golemis EA. (1997). Association of Krev-1/rap1a with Krit1, a novel ankyrin repeat-containing protein encoded by a gene mapping to 7q21-22. Oncogene 15:1043-1049. PMID: 9285558 (https://pubmed.ncbi.nlm.nih.gov/9285558/); DOI: 10.1038/sj.onc.1201268 (https://doi.org/10.1038/sj.onc.1201268)
- **stockton-2010-ccm-rock** — Stockton RA, Shenkar R, Awad IA, Ginsberg MH. (2010). Cerebral cavernous malformations proteins inhibit Rho kinase to stabilize vascular integrity. The Journal of experimental medicine 207:881-896. PMID: 20308363 (https://pubmed.ncbi.nlm.nih.gov/20308363/); PMCID: PMC2856024; DOI: 10.1084/jem.20091258 (https://doi.org/10.1084/jem.20091258)
- **swamy-2022-krit1-barrier-ppi** — Swamy H, Glading AJ. (2022). Contribution of protein-protein interactions to the endothelial-barrier-stabilizing function of KRIT1. Journal of cell science 135:jcs258816. PMID: 34918736 (https://pubmed.ncbi.nlm.nih.gov/34918736/); PMCID: PMC8917353; DOI: 10.1242/jcs.258816 (https://doi.org/10.1242/jcs.258816)
- **wade-2009-horse-genome** — Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, Lear TL, Adelson DL, Bailey E, Bellone RR, Blöcker H, Distl O, Edgar RC, Garber M, Leeb T, Mauceli E, MacLeod JN, Penedo MC, Raison JM, Sharpe T, Vogel J, Andersson L, Antczak DF, Biagi T, Binns MM, Chowdhary BP, Coleman SJ, Della Valle G, Fryc S, Guérin G, Hasegawa T, Hill EW, Jurka J, Kiialainen A, Lindgren G, Liu J, Magnani E, Mickelson JR, Murray J, Nergadze SG, Onofrio R, Pedroni S, Piras MF, Raudsepp T, Rocchi M, Røed KH, Ryder OA, Searle S, Skow L, Swinburne JE, Syvänen AC, Tozaki T, Valberg SJ, Vaudin M, White JR, Zody MC, Broad Institute Genome Sequencing Platform, Broad Institute Whole Genome Assembly Team, Lander ES, Lindblad-Toh K. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. Science (New York, N.Y.) 326:865-867. PMID: 19892987 (https://pubmed.ncbi.nlm.nih.gov/19892987/); PMCID: PMC3785132; DOI: 10.1126/science.1178158 (https://doi.org/10.1126/science.1178158)
- **whitehead-2004-ccm1-arterial** — Whitehead KJ, Plummer NW, Adams JA, Marchuk DA, Li DY. (2004). Ccm1 is required for arterial morphogenesis: implications for the etiology of human cavernous malformations. Development (Cambridge, England) 131:1437-1448. PMID: 14993192 (https://pubmed.ncbi.nlm.nih.gov/14993192/); DOI: 10.1242/dev.01036 (https://doi.org/10.1242/dev.01036)
- **zawistowski-2002-krit1-icap1** — Zawistowski JS, Serebriiskii IG, Lee MF, Golemis EA, Marchuk DA. (2002). KRIT1 association with the integrin-binding protein ICAP-1: a new direction in the elucidation of cerebral cavernous malformations (CCM1) pathogenesis. Human molecular genetics 11:389-396. PMID: 11854171 (https://pubmed.ncbi.nlm.nih.gov/11854171/); DOI: 10.1093/hmg/11.4.389 (https://doi.org/10.1093/hmg/11.4.389)
- **zawistowski-2005-ccm1-ccm2** — Zawistowski JS, Stalheim L, Uhlik MT, Abell AN, Ancrile BB, Johnson GL, Marchuk DA. (2005). CCM1 and CCM2 protein interactions in cell signaling: implications for cerebral cavernous malformations pathogenesis. Human molecular genetics 14:2521-2531. PMID: 16037064 (https://pubmed.ncbi.nlm.nih.gov/16037064/); DOI: 10.1093/hmg/ddi256 (https://doi.org/10.1093/hmg/ddi256)
- **zhang-2015-krit1-ard-ferm** — Zhang R, Li X, Boggon TJ. (2015). Structural analysis of the KRIT1 ankyrin repeat and FERM domains reveals a conformationally stable ARD-FERM interface. Journal of structural biology 192:449-456. PMID: 26458359 (https://pubmed.ncbi.nlm.nih.gov/26458359/); PMCID: PMC4651721; DOI: 10.1016/j.jsb.2015.10.006 (https://doi.org/10.1016/j.jsb.2015.10.006)
- **zhou-2016-mekk3-klf2-klf4** — Zhou Z, Tang AT, Wong WY, Bamezai S, Goddard LM, Shenkar R, Zhou S, Yang J, Wright AC, Foley M, Arthur JS, Whitehead KJ, Awad IA, Li DY, Zheng X, Kahn ML. (2016). Cerebral cavernous malformations arise from endothelial gain of MEKK3-KLF2/4 signalling. Nature 532:122-126. PMID: 27027284 (https://pubmed.ncbi.nlm.nih.gov/27027284/); PMCID: PMC4864035; DOI: 10.1038/nature17178 (https://doi.org/10.1038/nature17178)
- **UniProt A0A9L0SR44** — UniProtKB/TrEMBL entry A0A9L0SR44_HORSE, https://rest.uniprot.org/uniprotkb/A0A9L0SR44.txt (accessed 2026-10-26); human comparator UniProt O00522.
- **UniProt A0A3Q2GZV2 / K9KCP7; Ensembl ENSECAG00000016850** — Canonical horse KRIT1 isoform (https://rest.uniprot.org/uniprotkb/A0A3Q2GZV2.fasta), equine cDNA fragment K9KCP7 (EMBL JL636856, AEQ00228.1; https://rest.uniprot.org/uniprotkb/K9KCP7.txt), and Ensembl gene record (https://rest.ensembl.org/lookup/id/ENSECAG00000016850?expand=1), accessed 2026-10-26; raw records saved in notes/.


## Citations

1. _meta.json
2. beraud-dufour-2007-krit1-microtubules-abstract.md
3. beraud-dufour-2007-krit1-microtubules-summary.md
4. cuttano-2016-klf4-ccm-abstract.md
5. cuttano-2016-klf4-ccm-fulltext.txt
6. cuttano-2016-klf4-ccm-summary.md
7. de-luca-2021-pkca-krit1-shuttling-abstract.md
8. de-luca-2021-pkca-krit1-shuttling-fulltext.txt
9. de-luca-2021-pkca-krit1-shuttling-summary.md
10. draheim-2014-ccm-at-a-glance-abstract.md
11. draheim-2014-ccm-at-a-glance-summary.md
12. fisher-2014-ccm-structural-review-abstract.md
13. fisher-2014-ccm-structural-review-summary.md
14. fisher-2015-krit1-ccm2-structure-abstract.md
15. fisher-2015-krit1-ccm2-structure-summary.md
16. francalanci-2009-krit1-isoforms-abstract.md
17. francalanci-2009-krit1-isoforms-summary.md
18. gingras-2013-krit1-rap1-heg1-abstract.md
19. gingras-2013-krit1-rap1-heg1-summary.md
20. glading-2007-krit1-rap1-junctions-abstract.md
21. glading-2007-krit1-rap1-junctions-fulltext.txt
22. glading-2007-krit1-rap1-junctions-summary.md
23. glading-2024-krit1-review-abstract.md
24. glading-2024-krit1-review-fulltext.txt
25. glading-2024-krit1-review-summary.md
26. goitre-2010-krit1-ros-abstract.md
27. goitre-2010-krit1-ros-fulltext.txt
28. goitre-2010-krit1-ros-summary.md
29. gunel-2002-krit1-microtubule-abstract.md
30. gunel-2002-krit1-microtubule-summary.md
31. hilder-2007-ccm-complex-proteomics-abstract.md
32. hilder-2007-ccm-complex-proteomics-summary.md
33. huet-calderwood-2026-ccm2-dual-krit1-abstract.md
34. huet-calderwood-2026-ccm2-dual-krit1-fulltext.txt
35. huet-calderwood-2026-ccm2-dual-krit1-summary.md
36. kleaveland-2009-heg-ccm-abstract.md
37. kleaveland-2009-heg-ccm-fulltext.txt
38. kleaveland-2009-heg-ccm-summary.md
39. labergelecouteulx-1999-ccm1-truncating-abstract.md
40. labergelecouteulx-1999-ccm1-truncating-summary.md
41. li-2012-krit1-rap1-structure-abstract.md
42. li-2012-krit1-rap1-structure-summary.md
43. lisowska-2018-ccm1-ccm2-rock1-rock2-abstract.md
44. lisowska-2018-ccm1-ccm2-rock1-rock2-summary.md
45. liu-2013-krit1-icap1-mechanism-abstract.md
46. liu-2013-krit1-icap1-mechanism-fulltext.txt
47. liu-2013-krit1-icap1-mechanism-summary.md
48. maddaluno-2013-endmt-ccm-abstract.md
49. maddaluno-2013-endmt-ccm-summary.md
50. marchi-2015-ccm-autophagy-abstract.md
51. marchi-2015-ccm-autophagy-fulltext.txt
52. marchi-2015-ccm-autophagy-summary.md
53. perrelli-2023-krit1-redox-review-abstract.md
54. perrelli-2023-krit1-redox-review-summary.md
55. renz-2015-ccm-beta1-integrin-klf2-abstract.md
56. renz-2015-ccm-beta1-integrin-klf2-summary.md
57. sahoo-1999-krit1-ccm1-abstract.md
58. sahoo-1999-krit1-ccm1-summary.md
59. serebriiskii-1997-krit1-rap1a-abstract.md
60. serebriiskii-1997-krit1-rap1a-summary.md
61. stockton-2010-ccm-rock-abstract.md
62. stockton-2010-ccm-rock-fulltext.txt
63. stockton-2010-ccm-rock-summary.md
64. swamy-2022-krit1-barrier-ppi-abstract.md
65. swamy-2022-krit1-barrier-ppi-fulltext.txt
66. swamy-2022-krit1-barrier-ppi-summary.md
67. wade-2009-horse-genome-abstract.md
68. wade-2009-horse-genome-summary.md
69. whitehead-2004-ccm1-arterial-abstract.md
70. whitehead-2004-ccm1-arterial-summary.md
71. zawistowski-2002-krit1-icap1-abstract.md
72. zawistowski-2002-krit1-icap1-summary.md
73. zawistowski-2005-ccm1-ccm2-abstract.md
74. zawistowski-2005-ccm1-ccm2-summary.md
75. zhang-2015-krit1-ard-ferm-abstract.md
76. zhang-2015-krit1-ard-ferm-fulltext.txt
77. zhang-2015-krit1-ard-ferm-summary.md
78. zhou-2016-mekk3-klf2-klf4-abstract.md
79. zhou-2016-mekk3-klf2-klf4-fulltext.txt
80. zhou-2016-mekk3-klf2-klf4-summary.md