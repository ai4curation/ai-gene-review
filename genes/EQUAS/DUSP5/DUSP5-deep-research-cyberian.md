---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:21:19.136184'
end_time: '2026-10-25T23:31:32.147425'
duration_seconds: 613.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: DUSP5
  gene_symbol: DUSP5
  uniprot_accession: A0A8C4MED2
  protein_description: 'RecName: Full=Dual specificity protein phosphatase {ECO:0000256|PIRNR:PIRNR000939};
    EC=3.1.3.16 {ECO:0000256|PIRNR:PIRNR000939}; EC=3.1.3.48 {ECO:0000256|PIRNR:PIRNR000939};'
  gene_info: Name=DUSP5 {ECO:0000313|Ensembl:ENSEASP00005021863.2};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the protein-tyrosine phosphatase family. Non-
  protein_domains: Dual-sp_phosphatase_cat-dom. (IPR000340); MKP. (IPR008343); Prot-tyrosine_phosphatase-like.
    (IPR029021); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873)
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
citation_count: 91
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A8C4MED2
- **Protein Description:** RecName: Full=Dual specificity protein phosphatase {ECO:0000256|PIRNR:PIRNR000939}; EC=3.1.3.16 {ECO:0000256|PIRNR:PIRNR000939}; EC=3.1.3.48 {ECO:0000256|PIRNR:PIRNR000939};
- **Gene Information:** Name=DUSP5 {ECO:0000313|Ensembl:ENSEASP00005021863.2};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the protein-tyrosine phosphatase family. Non-
- **Key Domains:** Dual-sp_phosphatase_cat-dom. (IPR000340); MKP. (IPR008343); Prot-tyrosine_phosphatase-like. (IPR029021); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DUSP5" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DUSP5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DUSP5** (gene ID: DUSP5, UniProt: A0A8C4MED2) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# DUSP5 (Dual specificity protein phosphatase 5) in the donkey, *Equus asinus* (UniProt A0A8C4MED2)

## 1. Introduction and summary

The donkey protein A0A8C4MED2 is the *Equus asinus* ortholog of dual-specificity phosphatase 5 (DUSP5), a member of the mitogen-activated protein kinase (MAPK) phosphatase (MKP) subfamily of class I cysteine-based protein tyrosine phosphatases. The UniProt record is unreviewed (TrEMBL). It comes from Ensembl gene-model prediction on the chromosome-level donkey reference genome, and every functional statement in it (EC 3.1.3.16 and 3.1.3.48, nuclear localization, "highest relative activity toward ERK1") is an electronic transfer from family and ortholog rules rather than an observation in donkey cells [uniprot-2026-A0A8C4MED2-entry][wang-2020-donkey-genomes-abstract]. No experimental study of equine DUSP5 turned up in PubMed (the query "DUSP5 AND Equus" returned nothing). This report therefore rests on the large literature for human and mouse DUSP5 and on zebrafish developmental studies. That transfer is well supported: the donkey and human proteins are both 384 residues long and share 364 of 384 positions (about 95% identity) in an ungapped alignment I performed. All catalytic and regulatory residues characterized experimentally in the human enzyme are conserved (Section 2) [uniprot-2026-A0A8C4MED2-sequence][uniprot-2026-Q16690-sequence].

DUSP5's main function is well established. It is an inducible, nucleus-localized phosphatase that removes the activating phosphates from both the threonine and the tyrosine of the TEY motif in the activation loop of the classical MAP kinases ERK1 and ERK2 (MAPK3/MAPK1). This inactivates them. Its selectivity for ERK1/2 over JNK and p38 is unusually strict [ishibashi-1994-dusp-serum-heatshock-abstract][mandl-2005-dusp5-erk2-nuclear-anchoring-abstract][caunt-2013-mkps-review-fulltext]. Specificity comes from a kinase-interaction motif (KIM) in the non-catalytic N-terminal domain, which binds the common docking (CD) site of ERK2. A separate nuclear localization signal in the same domain confines the enzyme to the nucleus [mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. DUSP5 is more than a phosphatase. Through its KIM it also acts as a nuclear anchor for dephosphorylated ERK2, keeping it in the nucleus, and it can do this even when catalytically inactive [mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. ERK signaling itself induces DUSP5 transcription, through SRF and Elk-1 acting on CArG and ETS elements in its promoter. DUSP5 is therefore a delayed, transcription-dependent negative-feedback regulator that shapes the duration and the subcellular distribution of ERK activity [buffet-2015-dusp5-srf-elk1-abstract][kucharska-2009-dusp5-regulation-by-erk-abstract]. In knockout mice, DUSP5 has non-redundant roles in limiting nuclear ERK signaling. These show up in Ras-driven skin and pancreatic tumorigenesis, T-cell and eosinophil homeostasis, and vascular smooth-muscle proliferation [rushworth-2014-dusp5-skin-cancer-abstract][kidger-2022-dusp5-dusp6-kras-pancreas-abstract][kutty-2016-dusp5-tcell-survival-abstract][holmes-2015-dusp5-eosinophil-il33-abstract][ferguson-2021-dusp5-pulmonary-hypertension-abstract].

## 2. Gene identity, domain architecture and conservation in the donkey

The gene symbol fits the protein description and domain content. A0A8C4MED2 is annotated as DUSP5 (Ensembl ENSEASG00005014928; NCBI GeneID 106837561; CTD 1847, the human DUSP5 gene ID) on donkey chromosome 2. It carries the InterPro signatures expected of an MKP: an N-terminal rhodanese-like domain (IPR001763/IPR036873), a C-terminal dual-specificity phosphatase catalytic domain (IPR000340, within the PTP-like fold IPR029021), and the MKP family signature (IPR008343). The Conserved Domain Database assigns it to the DUSP5-specific subfamily cd14639 [uniprot-2026-A0A8C4MED2-entry]. This is the same two-module architecture that defines all ten catalytically active mammalian MKPs: a regulatory N-terminal non-catalytic domain carrying docking and localization signals, followed by the catalytic domain with the PTP active-site consensus [caunt-2013-mkps-review-fulltext]. Human DUSP5 was cloned independently as "B23" from mammary epithelial cells and as "hVH-3" from placenta, and was mapped to chromosome 10q25 [ishibashi-1994-dusp-serum-heatshock-abstract][kwak-1995-dsp-liver-cells-abstract][martell-1994-vh1-like-chromosome-abstract].

In my pairwise comparison of A0A8C4MED2 with human Q16690, the 20 amino-acid differences are almost all conservative substitutions. They cluster in the linker between the two domains and in the proline-rich C-terminal tail. The N-terminal segment containing the arginine-rich docking region (…VLRRARGGAVSARYVLPDEAARARLL…, residues ~51–76) is identical [uniprot-2026-A0A8C4MED2-sequence][uniprot-2026-Q16690-sequence]. The active-site signature HCEAGISRS (residues 262–270) is identical, matching the HCXAGXXR PTP motif first noted at positions 261–268 in the original B23 clone [ishibashi-1994-dusp-serum-heatshock-abstract]. Every residue that has been characterized functionally in the human protein is present in the donkey sequence. These include the catalytic nucleophile Cys263 and the adjacent Glu264, which forms a regulatory salt bridge with Arg269 [talipov-2016-dusp5-secondary-pocket-abstract], and the conserved His262 and Ser270 of the HCX5RS motif [gupta-2019-dusp5-hcx5rs-motif-abstract]. Also conserved are the Cys197–Cys219 pair proposed to form a redox-sensitive disulfide [talipov-2016-dusp5-secondary-pocket-abstract] and Ser147, whose replacement by proline in tissue from vascular-anomaly patients makes the enzyme hypoactive [nayak-2014-dusp5-mutant-activity-abstract]. The same holds for the three proline-directed ERK phosphorylation sites in the C-terminal tail, Thr321, Ser346 and Ser376 [kucharska-2009-dusp5-regulation-by-erk-abstract].

Comparison with orthologs from other vertebrates puts these observations in evolutionary context. I aligned donkey A0A8C4MED2 globally with DUSP5 sequences retrieved from UniProt [uniprot-2026-dusp5-orthologs-summary]. The horse protein (F7ALT2) differs from the donkey protein at only one of 384 positions, as expected for two species of *Equus*. Identity is 92% with mouse (Q1HL35) and 91% with rat (O54838), against 95% with human. Among mammals, the KIM arginine pair, the HCEAG(I/V)SRS active-site loop, the Cys197/Cys219 pair, Ser147 and all three ERK phosphorylation sites are invariant. The chicken (72% identity) and zebrafish (55% identity) orthologs also keep the active-site loop and the KIM arginines unchanged. However, the zebrafish protein lacks both Cys197 and Cys219, and the chicken protein lacks Cys219, and the C-terminal ERK phosphorylation sites are only partly conserved outside mammals. The core enzymatic and docking machinery is therefore deeply conserved across vertebrates. The proposed redox-sensitive disulfide and the ERK-dependent phosphorylation of the tail look like later, amniote- or mammal-specific features, and these are the parts of the human model whose transfer is best supported within mammals, including equids. The near-identity of donkey and horse DUSP5 also means that any future experimental data from the much better studied horse would apply directly to the donkey protein.

## 3. Catalytic activity and substrate specificity

DUSP5 hydrolyzes phosphomonoesters on both phosphotyrosine and phosphoserine/phosphothreonine in protein substrates. That is the basis for its two EC numbers: 3.1.3.48 (protein-tyrosine-phosphatase) and 3.1.3.16 (protein-serine/threonine phosphatase) [uniprot-2026-A0A8C4MED2-entry]. Its physiological reaction is the dual dephosphorylation of the pThr-Glu-pTyr activation-loop motif of ERK1/2, which converts the active kinase to its inactive, unphosphorylated form. The first biochemical study used a recombinant catalytic domain of human DUSP5 (B23). Its activity was real but lower than that of the atypical DSP VHR, and among the substrates tested it was highest toward phosphorylated ERK1. This is the experimental source of the "highest relative activity toward ERK1" statement that UniProt propagates to the donkey entry [ishibashi-1994-dusp-serum-heatshock-abstract][uniprot-2026-Q16690-entry]. Like other VH1-like phosphatases, hVH-3 dephosphorylates ERK [kwak-1995-dsp-liver-cells-abstract]. Later studies showed full-length DUSP5 directly dephosphorylating pERK2 in vitro, and also hydrolyzing the small generic substrate p-nitrophenyl phosphate with a Km in the millimolar range (7.6 mM for the phosphatase domain) [nayak-2014-dusp5-mutant-activity-abstract][neumann-2015-dusp5-inhibitors-abstract].

In cells, substrate selectivity comes mainly from docking rather than from the catalytic site. Mandl and colleagues showed that DUSP5 binds ERK2 specifically through a KIM in its N-terminal non-catalytic domain. This interaction decides what DUSP5 acts on in vivo: it inactivates ERK2 but not JNK or p38 MAPK [mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. Caunt and Keyse group DUSP5 with DUSP6 as having "high selectivity for ERK substrates". DUSP6 is cytoplasmic and DUSP5 is nuclear. They also note that DUSP5 has much greater substrate selectivity for ERK than its nuclear relative DUSP4/MKP-2 [caunt-2013-mkps-review-fulltext]. ERK-selective DUSP5 activity has been confirmed in many cell types. Examples include IL-2-stimulated T cells, where wild-type DUSP5 suppresses and a catalytically inactive mutant enhances ERK1/2 activity [kovanen-2003-dusp5-il2-signaling-abstract], and p53-expressing cancer cells, where DUSP5 overexpression dephosphorylates Erk1/2 [ueda-2003-dusp5-p53-target-abstract].

## 4. Structural basis of catalysis

The crystal structure of the human DUSP5 catalytic domain has been solved: PDB 2G6Z, residues 178–384, at 2.70 Å [jeong-2007-dusp5-crystal-structure-abstract][uniprot-2026-Q16690-entry]. It was obtained with a Cys263Ser active-site mutant and crystallized as a dimer [nayak-2014-dusp5-mutant-activity-fulltext]. Two sulfate ions sit about 7 Å apart in the active-site region. These are thought to mark where the two phosphates of the pThr-Glu-pTyr substrate bind, and they have been used to dock pERK2 and to design inhibitors that occupy both phosphate pockets [nayak-2014-dusp5-mutant-activity-fulltext][neumann-2015-dusp5-inhibitors-abstract]. DUSP5 differs mechanistically from DUSP6/MKP-3 in one important respect. In DUSP6, binding to ERK2 triggers catalytic activation by moving the general-acid aspartate loop into position. DUSP5 binds ERK2 tightly, but the binding does not raise its basal activity. The crystal structure explains why: the general-acid loop is already in the catalytically optimal conformation [caunt-2013-mkps-review-fulltext].

Molecular dynamics and mutagenesis point to further regulatory features of the DUSP5 phosphatase domain that other nuclear DUSPs lack. One is a secondary anion-binding site next to the catalytic centre. Another is Glu264, adjacent to the catalytic Cys263, which forms a salt bridge with Arg269 that restrains activity; the E264Q mutant is more active toward pERK. The simulations also suggest that the redox state of a remote Cys197–Cys219 disulfide could control the secondary pocket and therefore activity [talipov-2016-dusp5-secondary-pocket-abstract]. Mutating the conserved His262 or Ser270 changes kinetic behavior toward both pNPP and pERK [gupta-2019-dusp5-hcx5rs-motif-abstract]. The disease-associated S147P substitution, which lies outside the catalytic domain, also lowers activity [nayak-2014-dusp5-mutant-activity-abstract]. All of these residues are conserved in donkey DUSP5 (Section 2), but the redox and allosteric models rest largely on computation and have not been confirmed structurally.

## 5. Subcellular localization: a nuclear phosphatase and anchor for ERK

DUSP5 acts in the nucleus. The VH1-like phosphatases, including hVH-3, were early on described as commonly localizing to the nucleus [kwak-1995-dsp-liver-cells-abstract]. Mandl et al. used GFP fusions to define a functional nuclear localization signal in the N-terminal domain of DUSP5 that works independently of the KIM [mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. Caunt and Keyse describe this element as a short, noncanonical NLS lying just N-terminal to the conserved KIM arginines. It is conserved in nuclear MKPs but absent from cytoplasmic ones [caunt-2013-mkps-review-fulltext].

The localization has a functional consequence: DUSP5 is a spatial regulator of ERK. Expressing DUSP5 causes inactive ERK2 to move into and stay in the nucleus. This anchoring is specific to ERK2 and requires both the KIM–CD docking interaction and the DUSP5 NLS. A catalytically inactive DUSP5 mutant still tethers ERK2 in the nucleus. That nuclear ERK2 can then be re-phosphorylated by MEK in response to growth factors and can activate Elk-1, which suggests that the cytoplasm is not the only place ERK can be activated [mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. Endogenous DUSP5 performs the same role. In Dusp5-knockout mouse embryonic fibroblasts, nuclear phospho-ERK is higher after TPA stimulation, and total ERK fails to accumulate in the nucleus as it does in wild-type cells [rushworth-2014-dusp5-skin-cancer-abstract]. In the current model, MEK anchors ERK in the cytoplasm under basal conditions. DUSP6 sequesters dephosphorylated ERK in the cytoplasm, and DUSP5 does the same in the nucleus [caunt-2013-mkps-review-fulltext].

These compartment-specific effects can spread through the pathway in unexpected ways. Kidger et al. found that DUSP5 inactivates and anchors ERK in the nucleus but increases and prolongs cytoplasmic ERK activity. Part of the reason is that nuclear ERK inhibition relieves ERK-mediated negative feedback phosphorylation of RAF. In cells driven by the feedback-insensitive BRAF^V600E oncogene, DUSP5 instead becomes a cell-wide ERK inhibitor [kidger-2017-dusp5-localized-erk-abstract]. Cardiomyocytes show a similar compartment selectivity: when DUSP5 is induced by inhibiting class I HDACs, nuclear ERK1/2 signaling is suppressed while cytosolic ERK1/2 activation is preserved [ferguson-2013-hdac-dusp5-cardiomyocyte-abstract]. One study reported that DUSP5 is recruited to the mitochondrial outer membrane after oxidative stress [ohwada-2020-dusp5-mitochondria-abstract]. This is a non-canonical observation from overexpression and fractionation experiments and should be treated as provisional next to the well-established nuclear localization. The cytoplasm (GO:0005737) annotation on the donkey entry is likewise only an electronic inference from phylogenetic grouping (TreeGrafter) [uniprot-2026-A0A8C4MED2-entry].

## 6. Regulation of DUSP5 and its place in the RAS–RAF–MEK–ERK pathway

DUSP5 sits at the final step of the RAS–RAF–MEK–ERK cascade, and its own expression depends on that cascade. It is a classical inducible gene: transcripts rise after serum stimulation and heat shock in fibroblasts [ishibashi-1994-dusp-serum-heatshock-abstract], and expression is sustained for more than three hours after stimulation, unlike some more transient MKPs [kwak-1995-dsp-liver-cells-abstract]. Induction of both mRNA and protein by growth factors requires ERK1/2 activity [kucharska-2009-dusp5-regulation-by-erk-abstract]. It is transcriptional rather than a change in mRNA stability, and it is mediated by SRF bound to CArG boxes together with the ERK-activated ternary complex factor Elk-1 bound at adjacent ETS sites in the DUSP5 promoter [buffet-2015-dusp5-srf-elk1-abstract]. Because transcription and translation take time, this feedback loop acts after the faster mechanisms such as receptor desensitization and ERK phosphorylation of RAF, so it mainly shapes sustained phases of ERK signaling [caunt-2013-mkps-review-fulltext]. Experimentally strengthening this slow DUSP5-mediated feedback changes how faithfully single cells transmit information about GnRH concentration to ERK [garner-2016-gnrh-erk-feedback-abstract].

DUSP5 is also controlled at the protein level. It is rapidly degraded by the proteasome. ERK1/2 phosphorylates DUSP5 at three C-terminal sites (Thr321, Ser346 and Ser376), and this phosphorylation depends entirely on an intact KIM. No clear effect of these phosphorylations on DUSP5 stability or function has been found. Binding to ERK2, independent of ERK2 kinase activity, does stabilize DUSP5 and reduces its ubiquitination, which reinforces DUSP5's activity as phosphatase and anchor [kucharska-2009-dusp5-regulation-by-erk-abstract]. Other inputs into the DUSP5 gene include direct transcriptional activation by p53 after DNA damage [ueda-2003-dusp5-p53-target-abstract], induction by IL-2, IL-7 and IL-15 (but not IL-4) in T cells [kovanen-2003-dusp5-il2-signaling-abstract], induction by IL-33 in eosinophils [holmes-2015-dusp5-eosinophil-il33-abstract], transient induction by LPS in macrophages [seo-2017-dusp5-antiinflammatory-abstract], and MEK-dependent repression by class I HDACs in cardiomyocytes [ferguson-2013-hdac-dusp5-cardiomyocyte-abstract]. One report describes a phosphatase-independent function. In LPS-stimulated macrophages, DUSP5 bound TAK1 and the IKKs and interfered with TAK1–IKK association, which inhibited NF-κB, separately from its ERK phosphatase activity toward AP-1 [seo-2017-dusp5-antiinflammatory-abstract]. This scaffolding role has not yet been confirmed independently.

## 7. Physiological roles revealed by genetic models

Genetic studies in mice, rats, zebrafish and frogs show what DUSP5's nuclear, ERK-specific activity contributes to physiology. Global Dusp5 knockout mice show no gross abnormalities [kutty-2016-dusp5-tcell-survival-abstract], but they reveal non-redundant roles when the RAS–ERK pathway is driven hard by an oncogene. In the DMBA/TPA skin carcinogenesis model, Dusp5-null mice develop many more HRas^Q61L-driven papillomas. Only a few ERK-dependent transcripts are de-repressed in these mice, the most strongly up-regulated being *SerpinB2*, and deleting *SerpinB2* abolishes the increased tumour susceptibility. This identifies a specific nuclear ERK→SerpinB2 transcriptional output that DUSP5 normally restrains [rushworth-2014-dusp5-skin-cancer-abstract]. Loss of either Dusp5 or its cytoplasmic counterpart Dusp6 likewise increases KRAS^G12D-driven pancreatic hyperplasia, acinar-to-ductal metaplasia and PanIN formation, so the two phosphatases suppress oncogenic RAS signalling in partially non-redundant ways that correspond to their different compartments [kidger-2022-dusp5-dusp6-kras-pancreas-abstract]. In cells expressing BRAF^V600E, by contrast, deleting DUSP5 causes ERK hyperactivation and senescence, so DUSP5's net effect on cell fate depends on which oncogene drives the pathway [kidger-2017-dusp5-localized-erk-abstract]. These tumour-suppressor roles depend on context. In colorectal cancer, the DUSP5 promoter is methylated in CIMP-high tumours, yet depleting or overexpressing DUSP5 had little effect on ERK signalling or intestinal tumorigenesis [togel-2018-dusp5-colorectal-abstract].

In the immune system, transgenic overexpression of DUSP5 in lymphocytes blocks thymocyte development at the double-positive stage, impairs IL-2-dependent proliferation and causes autoimmunity [kovanen-2008-dusp5-tcell-development-abstract]. Conversely, Dusp5-deficient CD8^+ T cells have a T-cell-intrinsic shift from short-lived effector toward memory-precursor fates after viral infection, together with greater proliferation and apoptosis [kutty-2016-dusp5-tcell-survival-abstract]. Dusp5-null eosinophils show increased IL-33-driven ERK1/2 activation, more BCL-XL, prolonged survival and enhanced effector function during helminth infection [holmes-2015-dusp5-eosinophil-il33-abstract].

In the cardiovascular system, ectopic DUSP5 blocks agonist-induced cardiomyocyte hypertrophy [ferguson-2013-hdac-dusp5-cardiomyocyte-abstract]. Dusp5-null mice infused with angiotensin II develop pulmonary hypertension with medial thickening of small pulmonary arteries and right-ventricular hypertrophy, and DUSP5 overexpression blocks ANG II-driven proliferation of human pulmonary artery smooth muscle cells [ferguson-2021-dusp5-pulmonary-hypertension-abstract]. In zebrafish, *dusp5* is expressed specifically in vascular endothelium and angioblasts [sumanas-2005-zebrafish-vascular-genes-abstract][pramanik-2009-dusp5-snrk1-vascular-abstract]. There it acts downstream of, and antagonistically to, the kinase Snrk-1 to control angioblast numbers in the lateral plate mesoderm, and DUSP5 mutations have been found in affected tissue from human vascular anomalies [pramanik-2009-dusp5-snrk1-vascular-abstract]. Work in rats adds a vascular-physiology dimension. A Dusp5 knockout rat made with zinc-finger nucleases (a frameshift that truncates the protein at residue 121) has higher phospho-ERK1/2, an enhanced pressure-induced myogenic response in the middle cerebral artery and better autoregulation of cerebral blood flow [fan-2014-dusp5-ko-rat-myogenic-abstract]. siRNA knockdown of DUSP5 in organ-cultured cerebral arteries similarly enhances myogenic constriction, while pharmacological ERK1/2 inhibition blunts it [wickramasekera-2013-dusp5-cerebral-myogenic-abstract]. In the kidney, Dusp5 knockout rats have elevated phospho-ERK1/2 and phospho-PKCα and stronger afferent-arteriole myogenic tone, and they are protected from renal injury caused by DOCA-salt hypertension [zhang-2019-dusp5-ko-renal-injury-abstract]. In this setting, losing the ERK brake is protective, because ERK-dependent vascular tone is needed for blood-flow autoregulation. This contrasts with the harm that DUSP5 loss does in pulmonary smooth-muscle proliferation, and both results are consistent with DUSP5 setting the gain of ERK signalling in vascular smooth muscle.

DUSP5 also acts as an inducible ERK feedback regulator in metabolic and developmental settings. Diet-induced obesity and TNFα induce DUSP5 in white adipose tissue and adipocytes, and loss of DUSP5 exaggerates TNFα-driven ERK1/2 activation and inflammatory gene expression [habibian-2017-dusp5-adipocyte-tnf-abstract]. In human skeletal muscle, DUSP5 is the most strongly regulated MKP after acute exercise: its mRNA rises about nine-fold and returns to baseline within two hours, and in cultured myotubes this induction requires ERK1/2 activity [pourteymour-2017-dusp5-dusp6-exercise-abstract]. In early *Xenopus* embryos, DUSP5 is a transcriptional target of FGF signalling and a negative regulator of it [branney-2009-xenopus-fgf-transcriptome-abstract]. In mouse embryonic stem cells, Dusp5 helps maintain Nanog expression and pluripotency by restraining ERK, and its knockdown impairs embryoid-body expression of endodermal (Gata6) and mesodermal markers [chen-2011-dusp5-mouse-esc-abstract]. These developmental results are the closest experimental counterpart to the electronically propagated "endoderm formation" annotation on the donkey entry, and they again place DUSP5 within growth-factor/ERK feedback rather than in a dedicated developmental pathway. The common thread in all these systems is that DUSP5 is an inducible feedback brake on ERK-driven programs of proliferation, survival, inflammation and vascular tone. None of these roles has been tested in equids. Given the sequence conservation, the donkey protein is expected to work the same way.

## 8. Synthesis: predicted function of donkey DUSP5

Donkey A0A8C4MED2 is therefore best annotated as a nuclear, ERK1/2-selective MAP kinase phosphatase. Its molecular function is dual-specificity dephosphorylation of the phosphothreonine and phosphotyrosine residues in the ERK1/2 activation loop (GO "MAP kinase tyrosine/serine/threonine phosphatase activity"; EC 3.1.3.16 and 3.1.3.48), mediated by a Cys263-dependent PTP mechanism. Substrate specificity comes from KIM-mediated docking to the ERK common docking site. It acts in the nucleus, where it also binds and retains dephosphorylated ERK2. Its biological process is negative regulation of the ERK1/2 cascade, operating as an ERK-induced (SRF/Elk-1-dependent) delayed negative-feedback loop. The supporting evidence is a combination of (i) direct experiments on human and mouse orthologs [ishibashi-1994-dusp-serum-heatshock-abstract][mandl-2005-dusp5-erk2-nuclear-anchoring-abstract][kucharska-2009-dusp5-regulation-by-erk-abstract][rushworth-2014-dusp5-skin-cancer-abstract], (ii) structural data on the human catalytic domain [jeong-2007-dusp5-crystal-structure-abstract][caunt-2013-mkps-review-fulltext], and (iii) the near-identity of donkey and human sequences, including every functionally characterized residue (Section 2). The broader annotations on the donkey entry need more caution. "Endoderm formation" (TreeGrafter IEA) rests at best on knockdown effects on embryoid-body marker expression in mouse ES cells, which are better explained as a consequence of ERK feedback [chen-2011-dusp5-mouse-esc-abstract]. Cytoplasmic localization has little direct experimental support in mammals [uniprot-2026-A0A8C4MED2-entry][mandl-2005-dusp5-erk2-nuclear-anchoring-abstract]. Conservation of the protein across vertebrates (Section 2) also implies that the phosphatase and docking functions are ancestral, while some of the regulatory features proposed for human DUSP5 may be specific to mammals [uniprot-2026-dusp5-orthologs-summary].

## Open Questions

Several points remain unresolved, both for DUSP5 generally and for the equine protein specifically. First, there are no data on donkey or horse DUSP5 at all. The basic facts could be checked directly by confirming that the predicted transcript (ENSEAST00005023722) is expressed, mapping its tissue distribution with existing equine RNA-seq resources, and showing that recombinant donkey DUSP5 dephosphorylates equine ERK1/2 and localizes to the nucleus. Second, the noncanonical NLS and the exact KIM residues have been defined only by deletion and mutation in human DUSP5. A structure of full-length DUSP5, or of its N-terminal domain in complex with ERK2, would show how docking, nuclear import and anchoring are coordinated, and why binding does not activate catalysis as it does in DUSP6. Third, the proposed allosteric secondary pocket and redox-sensitive Cys197–Cys219 disulfide rest mainly on molecular dynamics and need experimental structural and redox-proteomic validation. The disulfide's absence from the zebrafish and chicken orthologs makes this question more interesting, because it suggests a regulatory mechanism that arose later in vertebrate evolution [uniprot-2026-dusp5-orthologs-summary]. Fourth, it is unclear how the opposite consequences of DUSP5 loss in different vascular beds (protective in the rat kidney, harmful in the mouse pulmonary circulation) relate to its nuclear compartmentalization of ERK [zhang-2019-dusp5-ko-renal-injury-abstract][ferguson-2021-dusp5-pulmonary-hypertension-abstract]. Fifth, the functions of the ERK phosphorylation sites (Thr321, Ser346, Ser376, all conserved in donkey) are still unknown. Sixth, reports of phosphatase-independent inhibition of NF-κB through TAK1/IKK binding and of mitochondrial recruitment of DUSP5 need independent confirmation with endogenous protein. Finally, from a comparative and veterinary angle, it would be worth asking whether DUSP5 variation contributes to equine traits associated with ERK signalling, such as vascular, immune (for example eosinophilic or parasite responses) or neoplastic conditions like equine sarcoid and melanoma. No such studies were found.

## References

- [uniprot-2026-A0A8C4MED2-entry] UniProt Consortium. UniProtKB/TrEMBL entry A0A8C4MED2_EQUAS, Dual specificity protein phosphatase (DUSP5), *Equus asinus*; entry version 22 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A8C4MED2.txt (sequence: [uniprot-2026-A0A8C4MED2-sequence], https://rest.uniprot.org/uniprotkb/A0A8C4MED2.fasta)
- [uniprot-2026-Q16690-entry] UniProt Consortium. UniProtKB/Swiss-Prot entry Q16690 (DUS5_HUMAN). https://rest.uniprot.org/uniprotkb/Q16690.txt (sequence: [uniprot-2026-Q16690-sequence], https://rest.uniprot.org/uniprotkb/Q16690.fasta)
- [wang-2020-donkey-genomes] Wang C, et al. Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020;11:6014. PMID: 33293529; DOI: 10.1038/s41467-020-19813-7; PMCID: PMC7723042.
- [ishibashi-1994-dusp-serum-heatshock] Ishibashi T, Bottaro DP, Michieli P, Kelley CA, Aaronson SA. A novel dual specificity phosphatase induced by serum stimulation and heat shock. J Biol Chem. 1994;269:29897-902. PMID: 7961985. https://pubmed.ncbi.nlm.nih.gov/7961985/
- [martell-1994-vh1-like-chromosome] Martell KJ, et al. Chromosomal localization of four human VH1-like protein-tyrosine phosphatases. Genomics. 1994. PMID: 7806236; DOI: 10.1006/geno.1994.1411.
- [kwak-1995-dsp-liver-cells] Kwak SP, Dixon JE. Multiple dual specificity protein tyrosine phosphatases are expressed and regulated differentially in liver cell lines. J Biol Chem. 1995;270(3):1156-60. PMID: 7836374; DOI: 10.1074/jbc.270.3.1156.
- [mandl-2005-dusp5-erk2-nuclear-anchoring] Mandl M, Slack DN, Keyse SM. Specific inactivation and nuclear anchoring of extracellular signal-regulated kinase 2 by the inducible dual-specificity protein phosphatase DUSP5. Mol Cell Biol. 2005;25(5):1830-1845. PMID: 15713638; DOI: 10.1128/MCB.25.5.1830-1845.2005; PMCID: PMC549372.
- [kucharska-2009-dusp5-regulation-by-erk] Kucharska A, et al. Regulation of the inducible nuclear dual-specificity phosphatase DUSP5 by ERK MAPK. Cell Signal. 2009. PMID: 19666109; DOI: 10.1016/j.cellsig.2009.07.015.
- [caunt-2013-mkps-review] Caunt CJ, Keyse SM. Dual-specificity MAP kinase phosphatases (MKPs): shaping the outcome of MAP kinase signalling. FEBS J. 2013;280:489-504. PMID: 22812510; DOI: 10.1111/j.1742-4658.2012.08716.x; PMCID: PMC3594966.
- [jeong-2007-dusp5-crystal-structure] Jeong DG, et al. Crystal structure of the catalytic domain of human DUSP5, a dual specificity MAP kinase protein phosphatase. Proteins. 2007. PMID: 17078075; DOI: 10.1002/prot.21224.
- [nayak-2014-dusp5-mutant-activity] Nayak J, et al. Protein expression, characterization and activity comparisons of wild type and mutant DUSP5 proteins. BMC Biochem. 2014. PMID: 25519881; DOI: 10.1186/s12858-014-0027-0; PMCID: PMC4299175.
- [talipov-2016-dusp5-secondary-pocket] Talipov MR, et al. Critical Role of the Secondary Binding Pocket in Modulating the Enzymatic Activity of DUSP5 toward Phosphorylated ERKs. Biochemistry. 2016. PMID: 27739308; DOI: 10.1021/acs.biochem.6b00498.
- [gupta-2019-dusp5-hcx5rs-motif] Gupta A, et al. Role of Conserved Histidine and Serine in the HCXXXXXRS Motif of Human Dual-Specificity Phosphatase 5. J Chem Inf Model. 2019. PMID: 30835471; DOI: 10.1021/acs.jcim.8b00919.
- [neumann-2015-dusp5-inhibitors] Neumann TS, et al. Identification of inhibitors that target dual-specificity phosphatase 5 provide new insights into the binding requirements for the two phosphate pockets. BMC Biochem. 2015. PMID: 26286528; DOI: 10.1186/s12858-015-0048-3; PMCID: PMC4545774.
- [buffet-2015-dusp5-srf-elk1] Buffet C, et al. Dual Specificity Phosphatase 5, a Specific Negative Regulator of ERK Signaling, Is Induced by Serum Response Factor and Elk-1 Transcription Factor. PLoS One. 2015. PMID: 26691724; DOI: 10.1371/journal.pone.0145484; PMCID: PMC4687125.
- [ueda-2003-dusp5-p53-target] Ueda K, et al. Dual-specificity phosphatase 5 (DUSP5) as a direct transcriptional target of tumor suppressor p53. Oncogene. 2003. PMID: 12944906; DOI: 10.1038/sj.onc.1206845.
- [kovanen-2003-dusp5-il2-signaling] Kovanen PE, et al. Analysis of gamma c-family cytokine target genes. Identification of dual-specificity phosphatase 5 (DUSP5) as a regulator of mitogen-activated protein kinase activity in interleukin-2 signaling. J Biol Chem. 2003. PMID: 12435740; DOI: 10.1074/jbc.M209015200.
- [kovanen-2008-dusp5-tcell-development] Kovanen PE, et al. T-cell development and function are modulated by dual specificity phosphatase DUSP5. J Biol Chem. 2008. PMID: 18430737; DOI: 10.1074/jbc.M709887200; PMCID: PMC2427334.
- [kutty-2016-dusp5-tcell-survival] Kutty RG, et al. Dual Specificity Phosphatase 5 Is Essential for T Cell Survival. PLoS One. 2016. PMID: 27936095; DOI: 10.1371/journal.pone.0167246; PMCID: PMC5147890.
- [holmes-2015-dusp5-eosinophil-il33] Holmes DA, et al. Dusp5 negatively regulates IL-33-mediated eosinophil survival and function. EMBO J. 2015. PMID: 25398911; DOI: 10.15252/embj.201489456; PMCID: PMC4337062.
- [rushworth-2014-dusp5-skin-cancer] Rushworth LK, et al. Dual-specificity phosphatase 5 regulates nuclear ERK activity and suppresses skin cancer by inhibiting mutant Harvey-Ras (HRasQ61L)-driven SerpinB2 expression. Proc Natl Acad Sci U S A. 2014. PMID: 25489104; DOI: 10.1073/pnas.1420159112; PMCID: PMC4280588.
- [kidger-2017-dusp5-localized-erk] Kidger AM, et al. Dual-specificity phosphatase 5 controls the localized inhibition, propagation, and transforming potential of ERK signaling. Proc Natl Acad Sci U S A. 2017. PMID: 28053233; DOI: 10.1073/pnas.1614684114; PMCID: PMC5255582.
- [kidger-2022-dusp5-dusp6-kras-pancreas] Kidger AM, et al. Suppression of mutant Kirsten-RAS (KRASG12D)-driven pancreatic carcinogenesis by dual-specificity MAP kinase phosphatases 5 and 6. Oncogene. 2022. PMID: 35418690; DOI: 10.1038/s41388-022-02302-0; PMCID: PMC9106580.
- [ferguson-2013-hdac-dusp5-cardiomyocyte] Ferguson BS, et al. Signal-dependent repression of DUSP5 by class I HDACs controls nuclear ERK activity and cardiomyocyte hypertrophy. Proc Natl Acad Sci U S A. 2013. PMID: 23720316; DOI: 10.1073/pnas.1301509110; PMCID: PMC3683796.
- [ferguson-2021-dusp5-pulmonary-hypertension] Ferguson BS, et al. DUSP5-mediated inhibition of smooth muscle cell proliferation suppresses pulmonary hypertension and right ventricular hypertrophy. Am J Physiol Heart Circ Physiol. 2021. PMID: 34142888; DOI: 10.1152/ajpheart.00115.2021; PMCID: PMC8410116.
- [pramanik-2009-dusp5-snrk1-vascular] Pramanik K, et al. Dusp-5 and Snrk-1 coordinately function during vascular development and disease. Blood. 2009. PMID: 18927432; DOI: 10.1182/blood-2008-06-162180; PMCID: PMC2635084.
- [sumanas-2005-zebrafish-vascular-genes] Sumanas S, et al. Identification of novel vascular endothelial-specific genes by the microarray analysis of the zebrafish cloche mutants. Blood. 2005. PMID: 15802528; DOI: 10.1182/blood-2004-12-4653; PMCID: PMC1895181.
- [seo-2017-dusp5-antiinflammatory] Seo H, et al. Dual-specificity phosphatase 5 acts as an anti-inflammatory regulator by inhibiting the ERK and NF-κB signaling pathways. Sci Rep. 2017. PMID: 29229953; DOI: 10.1038/s41598-017-17591-9; PMCID: PMC5725455.
- [ohwada-2020-dusp5-mitochondria] Ohwada W, et al. Distinct intra-mitochondrial localizations of pro-survival kinases and regulation of their functions by DUSP5 and PHLPP-1. Biochim Biophys Acta Mol Basis Dis. 2020. PMID: 32480039; DOI: 10.1016/j.bbadis.2020.165851.
- [togel-2018-dusp5-colorectal] Tögel L, et al. DUSP5 is methylated in CIMP-high colorectal cancer but is not a major regulator of intestinal cell proliferation and tumorigenesis. Sci Rep. 2018. PMID: 29379130; DOI: 10.1038/s41598-018-20176-9; PMCID: PMC5788859.
- [garner-2016-gnrh-erk-feedback] Garner KL, et al. Information Transfer in Gonadotropin-releasing Hormone (GnRH) Signaling: EXTRACELLULAR SIGNAL-REGULATED KINASE (ERK)-MEDIATED FEEDBACK LOOPS CONTROL HORMONE SENSING. J Biol Chem. 2016;291:2246-59. PMID: 26644469; DOI: 10.1074/jbc.M115.686964; PMCID: PMC4732208.
- [uniprot-2026-dusp5-orthologs] UniProt Consortium. DUSP5 ortholog sequences: F7ALT2 (*Equus caballus*), Q1HL35 (*Mus musculus*), O54838 (*Rattus norvegicus*, Swiss-Prot DUS5_RAT), A0A1D5P5S2 (*Gallus gallus*), Q6PBT4 (*Danio rerio*). https://rest.uniprot.org/uniprotkb/F7ALT2.fasta ; https://rest.uniprot.org/uniprotkb/Q1HL35.fasta ; https://rest.uniprot.org/uniprotkb/O54838.fasta ; https://rest.uniprot.org/uniprotkb/A0A1D5P5S2.fasta ; https://rest.uniprot.org/uniprotkb/Q6PBT4.fasta (pairwise alignments by the author of this report: [uniprot-2026-dusp5-orthologs-summary])
- [chen-2011-dusp5-mouse-esc] Chen Q, Zhou Y, Zhao X, et al. Effect of dual-specificity protein phosphatase 5 on pluripotency maintenance and differentiation of mouse embryonic stem cells. J Cell Biochem. 2011;112:3185-93. PMID: 21732408; DOI: 10.1002/jcb.23244.
- [branney-2009-xenopus-fgf-transcriptome] Branney PA, Faas L, Steane SE, et al. Characterisation of the fibroblast growth factor dependent transcriptome in early development. PLoS One. 2009;4:e4951. PMID: 19333377; DOI: 10.1371/journal.pone.0004951; PMCID: PMC2659300.
- [habibian-2017-dusp5-adipocyte-tnf] Habibian JS, Jefic M, Bagchi RA, et al. DUSP5 functions as a feedback regulator of TNFα-induced ERK1/2 dephosphorylation and inflammatory gene expression in adipocytes. Sci Rep. 2017;7:12879. PMID: 29018280; DOI: 10.1038/s41598-017-12861-y; PMCID: PMC5635013.
- [pourteymour-2017-dusp5-dusp6-exercise] Pourteymour S, Hjorth M, Lee S, et al. Dual specificity phosphatase 5 and 6 are oppositely regulated in human skeletal muscle by acute exercise. Physiol Rep. 2017;5. PMID: 28989118; DOI: 10.14814/phy2.13459; PMCID: PMC5641939.
- [fan-2014-dusp5-ko-rat-myogenic] Fan F, Geurts AM, Pabbidi MR, et al. Zinc-finger nuclease knockout of dual-specificity protein phosphatase-5 enhances the myogenic response and autoregulation of cerebral blood flow in FHH.1BN rats. PLoS One. 2014;9:e112878. PMID: 25397684; DOI: 10.1371/journal.pone.0112878; PMCID: PMC4232417.
- [wickramasekera-2013-dusp5-cerebral-myogenic] Wickramasekera NT, Gebremedhin D, Carver KA, et al. Role of dual-specificity protein phosphatase-5 in modulating the myogenic response in rat cerebral arteries. J Appl Physiol. 2013;114:252-61. PMID: 23172031; DOI: 10.1152/japplphysiol.01026.2011; PMCID: PMC3544499.
- [zhang-2019-dusp5-ko-renal-injury] Zhang C, He X, Murphy SR, et al. Knockout of Dual-Specificity Protein Phosphatase 5 Protects Against Hypertension-Induced Renal Injury. J Pharmacol Exp Ther. 2019;370:206-217. PMID: 31118214; DOI: 10.1124/jpet.119.258954; PMCID: PMC6636243.


## Citations

1. branney-2009-xenopus-fgf-transcriptome-abstract.md
2. branney-2009-xenopus-fgf-transcriptome-summary.md
3. buffet-2015-dusp5-srf-elk1-abstract.md
4. buffet-2015-dusp5-srf-elk1-fulltext.txt
5. buffet-2015-dusp5-srf-elk1-summary.md
6. caunt-2013-mkps-review-abstract.md
7. caunt-2013-mkps-review-fulltext.txt
8. caunt-2013-mkps-review-summary.md
9. chen-2011-dusp5-mouse-esc-abstract.md
10. chen-2011-dusp5-mouse-esc-summary.md
11. fan-2014-dusp5-ko-rat-myogenic-abstract.md
12. fan-2014-dusp5-ko-rat-myogenic-fulltext.txt
13. fan-2014-dusp5-ko-rat-myogenic-summary.md
14. ferguson-2013-hdac-dusp5-cardiomyocyte-abstract.md
15. ferguson-2013-hdac-dusp5-cardiomyocyte-summary.md
16. ferguson-2021-dusp5-pulmonary-hypertension-abstract.md
17. ferguson-2021-dusp5-pulmonary-hypertension-fulltext.txt
18. ferguson-2021-dusp5-pulmonary-hypertension-summary.md
19. garner-2016-gnrh-erk-feedback-abstract.md
20. garner-2016-gnrh-erk-feedback-summary.md
21. gupta-2019-dusp5-hcx5rs-motif-abstract.md
22. gupta-2019-dusp5-hcx5rs-motif-summary.md
23. habibian-2017-dusp5-adipocyte-tnf-abstract.md
24. habibian-2017-dusp5-adipocyte-tnf-fulltext.txt
25. habibian-2017-dusp5-adipocyte-tnf-summary.md
26. holmes-2015-dusp5-eosinophil-il33-abstract.md
27. holmes-2015-dusp5-eosinophil-il33-summary.md
28. ishibashi-1994-dusp-serum-heatshock-abstract.md
29. ishibashi-1994-dusp-serum-heatshock-summary.md
30. jeong-2007-dusp5-crystal-structure-abstract.md
31. jeong-2007-dusp5-crystal-structure-summary.md
32. keyse-2008-mkps-cancer-abstract.md
33. keyse-2008-mkps-cancer-summary.md
34. kidger-2017-dusp5-localized-erk-abstract.md
35. kidger-2017-dusp5-localized-erk-summary.md
36. kidger-2022-dusp5-dusp6-kras-pancreas-abstract.md
37. kidger-2022-dusp5-dusp6-kras-pancreas-fulltext.txt
38. kidger-2022-dusp5-dusp6-kras-pancreas-summary.md
39. kovanen-2003-dusp5-il2-signaling-abstract.md
40. kovanen-2003-dusp5-il2-signaling-summary.md
41. kovanen-2008-dusp5-tcell-development-abstract.md
42. kovanen-2008-dusp5-tcell-development-summary.md
43. kucharska-2009-dusp5-regulation-by-erk-abstract.md
44. kucharska-2009-dusp5-regulation-by-erk-summary.md
45. kutty-2016-dusp5-tcell-survival-abstract.md
46. kutty-2016-dusp5-tcell-survival-fulltext.txt
47. kutty-2016-dusp5-tcell-survival-summary.md
48. kwak-1995-dsp-liver-cells-abstract.md
49. kwak-1995-dsp-liver-cells-summary.md
50. mandl-2005-dusp5-erk2-nuclear-anchoring-abstract.md
51. mandl-2005-dusp5-erk2-nuclear-anchoring-summary.md
52. martell-1994-vh1-like-chromosome-abstract.md
53. martell-1994-vh1-like-chromosome-summary.md
54. nayak-2014-dusp5-mutant-activity-abstract.md
55. nayak-2014-dusp5-mutant-activity-fulltext.txt
56. nayak-2014-dusp5-mutant-activity-summary.md
57. neumann-2015-dusp5-inhibitors-abstract.md
58. neumann-2015-dusp5-inhibitors-summary.md
59. ohwada-2020-dusp5-mitochondria-abstract.md
60. ohwada-2020-dusp5-mitochondria-summary.md
61. pourteymour-2017-dusp5-dusp6-exercise-abstract.md
62. pourteymour-2017-dusp5-dusp6-exercise-fulltext.txt
63. pourteymour-2017-dusp5-dusp6-exercise-summary.md
64. pramanik-2009-dusp5-snrk1-vascular-abstract.md
65. pramanik-2009-dusp5-snrk1-vascular-summary.md
66. rushworth-2014-dusp5-skin-cancer-abstract.md
67. rushworth-2014-dusp5-skin-cancer-summary.md
68. seo-2017-dusp5-antiinflammatory-abstract.md
69. seo-2017-dusp5-antiinflammatory-fulltext.txt
70. seo-2017-dusp5-antiinflammatory-summary.md
71. sumanas-2005-zebrafish-vascular-genes-abstract.md
72. sumanas-2005-zebrafish-vascular-genes-summary.md
73. talipov-2016-dusp5-secondary-pocket-abstract.md
74. talipov-2016-dusp5-secondary-pocket-summary.md
75. togel-2018-dusp5-colorectal-abstract.md
76. togel-2018-dusp5-colorectal-summary.md
77. ueda-2003-dusp5-p53-target-abstract.md
78. ueda-2003-dusp5-p53-target-summary.md
79. uniprot-2026-A0A8C4MED2-entry.txt
80. uniprot-2026-A0A8C4MED2-sequence.fasta
81. uniprot-2026-A0A8C4MED2-summary.md
82. uniprot-2026-Q16690-entry.txt
83. uniprot-2026-Q16690-sequence.fasta
84. uniprot-2026-Q16690-summary.md
85. uniprot-2026-dusp5-orthologs-summary.md
86. wang-2020-donkey-genomes-abstract.md
87. wang-2020-donkey-genomes-summary.md
88. wickramasekera-2013-dusp5-cerebral-myogenic-abstract.md
89. wickramasekera-2013-dusp5-cerebral-myogenic-summary.md
90. zhang-2019-dusp5-ko-renal-injury-abstract.md
91. zhang-2019-dusp5-ko-renal-injury-summary.md