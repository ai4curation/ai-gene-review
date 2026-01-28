---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T07:18:11.153620'
end_time: '2026-01-23T07:35:29.258537'
duration_seconds: 1038.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: NF1
  gene_symbol: NF1
  uniprot_accession: P21359
  protein_description: 'RecName: Full=Neurofibromin; AltName: Full=Neurofibromatosis-related
    protein NF-1; Contains: RecName: Full=Neurofibromin truncated;'
  gene_info: Name=NF1;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: ARM-type_fold. (IPR016024); CRAL-TRIO_dom. (IPR001251); CRAL-TRIO_dom_sf.
    (IPR036865); PH-like_dom_sf. (IPR011993); PH_NF1. (IPR054071)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P21359
- **Protein Description:** RecName: Full=Neurofibromin; AltName: Full=Neurofibromatosis-related protein NF-1; Contains: RecName: Full=Neurofibromin truncated;
- **Gene Information:** Name=NF1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ARM-type_fold. (IPR016024); CRAL-TRIO_dom. (IPR001251); CRAL-TRIO_dom_sf. (IPR036865); PH-like_dom_sf. (IPR011993); PH_NF1. (IPR054071)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NF1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NF1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NF1** (gene ID: NF1, UniProt: P21359) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Neurofibromin (NF1): A Comprehensive Functional Annotation Report

## Introduction

Neurofibromin is a large, multifunctional protein encoded by the NF1 tumor suppressor gene located on chromosome 17q11.2. The gene was cloned in 1990 through the convergent efforts of two research groups led by Francis Collins at the University of Michigan and Ray White at the University of Utah [wallace-1990-nf1-cloning-abstract]. The complete sequence revealed that neurofibromin comprises 2,818 amino acids with a molecular weight of approximately 320-327 kDa, making it one of the largest known proteins [marchuk-1991-nf1-complete-sequence-abstract]. Sequence analysis immediately identified a segment with significant homology to mammalian GTPase-activating protein (GAP) and to the Saccharomyces cerevisiae proteins IRA1 and IRA2, suggesting a role as a negative regulator of the Ras proto-oncogene signaling pathway [wallace-1990-nf1-cloning-abstract].

The clinical significance of neurofibromin is profound. Germline mutations in NF1 cause neurofibromatosis type 1, one of the most common autosomal dominant genetic disorders, affecting approximately 1 in 3,000 individuals worldwide [anastasaki-2022-ras-beyond-abstract]. The syndrome is characterized by pigmentary abnormalities (cafe-au-lait macules), peripheral and central nervous system tumors, learning disabilities, skeletal abnormalities, and an increased predisposition to various malignancies [yap-2014-nf1-bench-bedside-abstract]. Beyond its role in the hereditary syndrome, somatic NF1 mutations have been identified in numerous sporadic cancers including glioblastoma (12-23%), melanoma (14%), lung adenocarcinoma (11-12%), and breast cancer (up to 27.7%), establishing neurofibromin as a broadly relevant tumor suppressor [yap-2014-nf1-bench-bedside-abstract].

Over the past three decades, research has revealed that while the GTPase-activating protein (GAP) function of neurofibromin is central to its biological role, the functionally characterized RAS regulatory domain comprises only approximately 10% of the entire protein sequence, indicating substantial additional functions encoded by the remaining domains [anastasaki-2022-ras-beyond-abstract]. This report provides a comprehensive analysis of neurofibromin's structure, enzymatic function, subcellular localization, signaling pathway integration, and protein interactions.

## Domain Architecture and Structure

Neurofibromin possesses a complex multi-domain architecture that has been elucidated through a combination of sequence analysis, crystallography, and cryo-electron microscopy. The major functional domains include the cysteine-serine rich domain (CSRD, residues 543-909), the tubulin-binding domain (TBD, residues 1085-1172), the GAP-related domain (GRD, residues 1198-1530), the Sec14-homology domain, the pleckstrin homology (PH) domain, and the C-terminal domain (CTD, residues 2260-2818) [bergoug-2020-neurofibromin-review-abstract].

The GAP-related domain (GRD) represents the most thoroughly characterized region of neurofibromin. X-ray crystallographic analysis of a proteolytically treated catalytic fragment (NF1-333, residues 1198-1530) revealed that the GRD adopts a helical architecture similar to p120GAP [scheffzek-1998-grd-structure-abstract]. The structure comprises two distinct regions: a central domain (NF1c) containing all residues conserved among RasGAPs, and an extra domain (NF1ex) that, despite limited sequence homology, shows surprising structural similarity to the corresponding region of p120GAP [scheffzek-1998-grd-structure-abstract]. The catalytic residues, including the critical arginine finger (R1276), are situated on a shallow groove that is complementary to the effector region and switch regions of Ras proteins.

The Sec14-PH bipartite module, located immediately C-terminal to the GRD, represents a lipid-binding region. Crystal structure determination revealed that the Sec14-like portion binds cellular glycerophospholipids including phosphatidylglycerol (PtdGro), phosphatidylethanolamine (PtdEtn), and phosphatidylcholine (PtdCho), with minor binding to phosphatidylserine and phosphatidylinositol [tong-2002-nf1-sec14-lipid-abstract]. Notably, phosphorylated phosphatidylinositol species (PtdInsPs) are not detected as binders, though their soluble inositol-phosphate headgroups can inhibit the lipid exchange reaction [bergoug-2020-neurofibromin-review-abstract].

Recent cryo-electron microscopy studies have provided groundbreaking insights into full-length neurofibromin structure. Two landmark 2021 papers revealed the architecture of the ~640 kDa neurofibromin homodimer. Lupton and colleagues demonstrated that the dimer features a gigantic 30 x 10 nm array of alpha-helices forming a lemniscate (figure-8) shaped core scaffold [lupton-2021-cryoem-nf1-dimer-abstract]. Naschberger and colleagues determined the structure of human NF1 isoform 2 at 3.3 angstrom resolution, identifying two distinct conformational populations [naschberger-2021-nf1-isoform2-structure-abstract].

The structure exists in two distinct conformational states: a closed (auto-inhibited) state and an open (active) state. The major population exhibits a closed conformation stabilized by zinc binding, where HEAT/ARM core domains shield the GRD such that Ras binding is sterically inhibited and the critical arginine finger R1276 is not accessible. A second population shows one protomer in the auto-inhibited conformation and the other in an open configuration [naschberger-2021-nf1-isoform2-structure-abstract]. In the open conformation, a large-scale movement of the GRD exposes the arginine finger for Ras engagement, while the Sec14-PH module reorients to allow interaction with the cellular membrane [anastasaki-2022-ras-beyond-abstract]. This conformational switching represents a key regulatory mechanism for neurofibromin activity, and membrane interaction is proposed to trigger the transition from closed to open states [lupton-2021-cryoem-nf1-dimer-abstract]. The structural data also explains the extreme susceptibility of neurofibromin to loss-of-function mutations, as disruption of the complex interdomain architecture can readily destabilize the protein or prevent conformational switching.

## GAP Function and Ras Regulation

The primary enzymatic function of neurofibromin is to accelerate the intrinsic GTPase activity of Ras proteins, converting them from an active GTP-bound state to an inactive GDP-bound state. This activity was demonstrated shortly after the gene's cloning through studies showing that the NF1 GRD could complement yeast IRA mutants and directly hydrolyze GTP bound to active Ras [anastasaki-2022-ras-beyond-abstract]. Neurofibromin functions as a RasGAP that negatively regulates all three classic RAS proteins (HRAS, NRAS, KRAS) as well as RRAS and MRAS [bergoug-2020-neurofibromin-review-abstract].

The kinetic parameters of neurofibromin's GAP activity have been precisely determined. Ras proteins have an intrinsically slow GTPase activity with a half-life of approximately 16 minutes (koff of 6 x 10^-4 s^-1). Neurofibromin accelerates this hydrolysis rate by approximately 52,000-fold for wild-type Ras at 30 degrees C, comparable to the 70,000-fold acceleration provided by p120GAP [phillips-2003-nf1-mechanism-kinetics-abstract]. Neurofibromin binds to Ras proteins with a dissociation constant (Kd) of approximately 1 micromolar, which is substantially tighter than p120GAP's Kd of 17 micromolar. Detailed kinetic analysis using fluorescent GTP analogs and phosphate sensors revealed that phosphate release from the NF1-Ras-GDP-Pi complex is rate-limiting, occurring approximately 3-fold slower than the preceding cleavage step [phillips-2003-nf1-mechanism-kinetics-abstract]. Phosphate dissociation triggers the conformational change of Ras from the GTP-bound to GDP-bound state, dramatically reducing neurofibromin affinity and enabling product release.

The catalytic mechanism relies on the "arginine finger" hypothesis for GAP-stimulated GTP hydrolysis. The arginine residue at position 1276 (R1276) is inserted into the active site of Ras to stabilize the transition state of the GTPase reaction [scheffzek-1998-grd-structure-abstract]. Helices alpha-6c and alpha-7c of the GRD form the bottom of the Ras-binding groove, while the variable loop (L6c) and alpha-2c helix participate in the interaction with Ras [bergoug-2020-neurofibromin-review-abstract]. The finger loop (L1c) provides the critical arginine to the Ras active site. Missense mutations mapping to the NF1 GRD that are found in NF1 patients underscore its importance for pathogenesis [scheffzek-1998-grd-structure-abstract].

The efficient inactivation of membrane-bound Ras requires that neurofibromin be recruited to the plasma membrane. This is accomplished through interaction with Spred1 (Sprouty-related, EVH1 domain-containing protein 1) [stowe-2012-spred1-nf1-legius-abstract]. Spred1 is recruited to the plasma membrane through interactions of its C-terminal SPR (Sprouty-Related) domain with phospholipids and caveolin-1. Subsequently, Spred1 recruits neurofibromin to the membrane via an interaction between the Spred1 EVH1 domain and the neurofibromin GRD [naima-2016-spred1-grd-binding-abstract]. The crystal structure of the trimeric KRAS-NF1(GRD)-SPRED1 complex (PDB: 6V65) revealed that the EVH1 domain interacts with the N-terminal 16 amino acids and C-terminal 20 amino acids of the GRD, forming two crossing alpha-helix coils outside the catalytic GAP domain [yan-2020-spred1-nf1-kras-structure-abstract]. Critically, this interaction does not interfere with GAP catalytic activity, allowing neurofibromin to efficiently inactivate membrane-localized Ras.

The biological significance of the Spred1-neurofibromin interaction is underscored by the phenotypic overlap between neurofibromatosis type 1 and Legius syndrome, an autosomal dominant disorder caused by loss-of-function mutations in SPRED1. Both conditions share features such as cafe-au-lait macules and learning difficulties, though Legius syndrome lacks the severe tumor manifestations of NF1 [stowe-2012-spred1-nf1-legius-abstract]. Loss-of-function Spred1 mutations either prevent neurofibromin binding or are incapable of recruiting it to the membrane, providing molecular evidence for the functional interdependence of these proteins [naima-2016-spred1-grd-binding-abstract]. The relatively mild phenotype of Legius syndrome compared to NF1 may be explained by partial functional redundancy from SPRED2 and SPRED3 in most cell types [bergoug-2020-neurofibromin-review-abstract].

## Subcellular Localization

Neurofibromin displays a complex and dynamic subcellular distribution that reflects its multiple cellular functions. The protein is predominantly cytoplasmic but localizes to numerous subcellular compartments under different conditions and in different cell types [bergoug-2020-neurofibromin-review-abstract].

In the cytoplasm, neurofibromin associates with the cytoskeleton through its tubulin-binding domain (TBD) and through additional regions within the CTD. Studies in differentiating telencephalic neurons revealed that neurofibromin exhibits a biphasic pattern of cytoskeletal association: during early differentiation, neurofibromin colocalizes with F-actin; during later differentiation phases, it transitions to colocalization with microtubules [siebert-2001-nf1-cytoskeleton-localization-abstract]. This colocalization was disrupted by nocodazole (a microtubule disruptor) but not by cytochalasin D (an actin disruptor) during the second phase, confirming the specificity of the microtubule association [siebert-2001-nf1-cytoskeleton-localization-abstract].

Plasma membrane localization is essential for neurofibromin's RasGAP function but is not constitutive. Rather, membrane recruitment requires Spred proteins. As predominantly a cytosolic protein, neurofibromin translocates to the plasma membrane through interaction with Spred1, which anchors to membrane lipids and caveolin-1 [stowe-2012-spred1-nf1-legius-abstract]. This recruitment mechanism enables spatial and temporal control of Ras inactivation.

Nuclear localization of neurofibromin has been documented in multiple cell types. A bipartite nuclear localization signal (NLS) is encoded by exon 43 (residues 2555-2572) [siebert-2001-nf1-cytoskeleton-localization-abstract]. The distribution of neurofibromin between cytoplasm and nucleus is cell-cycle dependent. In SF268 glioblastoma cells, neurofibromin is predominantly extra-nuclear at the G1/S transition, progressively accumulates in the nucleus throughout S phase, and becomes primarily nuclear prior to mitosis [bergoug-2020-neurofibromin-review-abstract]. PKC-epsilon-mediated phosphorylation at S2808 increases nuclear accumulation. Within the nucleus, neurofibromin preferentially associates with the nuclear matrix through interaction with nuclear intermediate filaments lamins A/C [bergoug-2020-neurofibromin-review-abstract]. The nuclear pool of neurofibromin may participate in cell cycle regulation and, in breast cancer cells, has been shown to interact with the estrogen receptor as a transcriptional co-repressor [anastasaki-2022-ras-beyond-abstract].

Additional localization sites include the endoplasmic reticulum, mitochondria, melanosomes, the mitotic spindle, centrosomes, and PML nuclear bodies [bergoug-2020-neurofibromin-review-abstract]. One alternatively spliced isoform containing exon 10a-2 harbors a transmembrane segment that directs localization to perinuclear granular structures including the endoplasmic reticulum [anastasaki-2022-ras-beyond-abstract].

## Signaling Pathway Integration

Neurofibromin functions as a central integrator of multiple signaling pathways, extending well beyond its canonical role as a Ras-GAP. The four major signaling axes regulated by neurofibromin are the Ras/MAPK pathway, the PI3K/AKT/mTOR pathway, the cAMP/PKA pathway, and the Rho/ROCK/LIMK/cofilin pathway.

### Ras/MAPK Pathway

The most well-characterized function of neurofibromin is negative regulation of the Ras/MAPK pathway. By converting active GTP-bound Ras to inactive GDP-bound Ras, neurofibromin suppresses downstream signaling through RAF, MEK, and ERK kinases [yap-2014-nf1-bench-bedside-abstract]. Loss of neurofibromin results in constitutive Ras hyperactivation, leading to increased cell proliferation and survival. This pathway dysregulation underlies tumor formation in NF1 patients and provides the rationale for therapeutic targeting with MEK inhibitors. Selumetinib, a MEK1/2 inhibitor, became the first FDA-approved therapy for inoperable plexiform neurofibromas based on clinical trials demonstrating decreased tumor burden [anastasaki-2022-ras-beyond-abstract].

### PI3K/AKT/mTOR Pathway

Neurofibromin critically regulates the mTOR pathway through mechanisms involving the TSC2 tumor suppressor. Studies demonstrated that mTOR is constitutively activated in NF1-deficient primary cells and human tumors even in the absence of growth factors [johannessen-2005-nf1-tsc2-mtor-abstract]. This aberrant activation depends on Ras and PI3 kinase and is mediated by AKT-dependent phosphorylation and inactivation of tuberin (TSC2). Tuberin normally functions to inhibit mTOR by promoting GTP hydrolysis of the Ras-related GTPase Rheb; when inactivated by AKT phosphorylation at T1462 and S939, mTOR becomes constitutively active [johannessen-2005-nf1-tsc2-mtor-abstract]. This mechanistic link explains why NF1-deficient tumor cells show sensitivity to the mTOR inhibitor rapamycin, though clinical trials have shown only modest efficacy [yap-2014-nf1-bench-bedside-abstract].

An additional Ras-independent mechanism for mTOR regulation involves neurofibromin interaction with LAMTOR1 at lysosomes, participating in the nutrient-sensing pathway that controls mTORC1 activity [bergoug-2020-neurofibromin-review-abstract].

### cAMP/PKA Pathway

Studies initially performed in Drosophila revealed that neurofibromin regulates cAMP signaling independent of its RasGAP function [hsueh-2001-nf1-camp-adenylyl-cyclase-abstract]. Loss of Drosophila Nf1 reduces potassium currents due to diminished activation of adenylyl cyclase and cAMP production. The small body size defect in Nf1-deficient Drosophila was rescued by overexpression of activated PKA but not by manipulating Ras signaling, demonstrating Ras-independence [anastasaki-2022-ras-beyond-abstract].

In mammals, neurofibromin regulates cAMP through two distinct adenylyl cyclase pathways: a growth factor-stimulated Ras-dependent pathway downstream of receptor tyrosine kinases, and a G-protein-dependent pathway activated by neurotransmitters [bergoug-2020-neurofibromin-review-abstract]. The PH domain of neurofibromin interacts with the serotonin receptor 5-HT6R, and disruption of this interaction by patient-derived mutations inhibits constitutive receptor activity and reduces basal cAMP levels [bergoug-2020-neurofibromin-review-abstract]. Neurofibromin heterozygosity impairs CNS neuronal morphology through a cAMP/PKA/ROCK-dependent mechanism, with NF1+/- neurons showing reduced PKA substrate phosphorylation both in vitro and in vivo. Pharmacological elevation of cAMP with forskolin or phosphodiesterase inhibitors can reverse neuronal deficits in NF1-deficient cells [bergoug-2020-neurofibromin-review-abstract].

### Rho/ROCK/LIMK/cofilin Pathway

Neurofibromin regulates actin cytoskeleton dynamics through inhibition of the Rho/ROCK/LIMK2/cofilin and Rac1/Pak1/LIMK1/cofilin pathways [bergoug-2020-neurofibromin-review-abstract]. The SecPH domain directly interacts with LIMK2, a kinase that phosphorylates and inactivates the actin-severing protein cofilin. By inhibiting this pathway, neurofibromin promotes actin dynamics required for cell migration, neurite outgrowth, and cytoskeletal reorganization. This function is independent of RasGAP activity and represents an important mechanism for neurofibromin's role in neuronal development and plasticity.

## Protein Interactions and Molecular Complexes

Beyond its catalytic function, neurofibromin participates in numerous protein-protein interactions that mediate its diverse cellular roles. Major interaction partners and their functional significance include:

**Ras proteins:** The GRD directly binds to GTP-loaded HRAS, KRAS, NRAS, MRAS, and RRAS to catalyze GTP hydrolysis [bergoug-2020-neurofibromin-review-abstract].

**Spred1:** The EVH1 domain of Spred1 binds to the GRD without affecting catalytic activity, mediating membrane recruitment essential for efficient Ras inactivation [naima-2016-spred1-grd-binding-abstract]. Oncogenic EGFR can disrupt this interaction by phosphorylating Spred1 at S105 [yan-2020-spred1-nf1-kras-structure-abstract].

**Tubulin and microtubules:** The TBD and CTD mediate association with microtubules, with neurofibromin also interacting with motor proteins (kinesin-1, dynein) involved in vesicle trafficking and RNA granule transport [bergoug-2020-neurofibromin-review-abstract].

**CRMP2:** The CTD binds to the active (non-phosphorylated) form of collapsin response mediator protein 2, protecting it from inactivation by Cdk5, GSK-3beta, and Rho-kinase [mouber-2018-crmp2-nf1-pain-abstract]. This interaction is essential for neurite outgrowth during neuronal differentiation. In NF1-deficient cells, freed CRMP2 interacts with syntaxin 1A and CaV2.2 calcium channels, leading to increased release of pro-nociceptive neurotransmitters and contributing to NF1-associated pain [mouber-2018-crmp2-nf1-pain-abstract].

**FAK:** The CTD interacts with focal adhesion kinase, linking neurofibromin to cell adhesion and motility regulation [bergoug-2020-neurofibromin-review-abstract].

**Syndecans:** The syndecan-binding domain in the CTD mediates interactions important for membrane localization and dendritic spine formation [bergoug-2020-neurofibromin-review-abstract].

**5-HT6R:** The PH domain interacts with the serotonin receptor 5-HT6R, mediating cAMP pathway regulation [bergoug-2020-neurofibromin-review-abstract].

**HCN1:** Neurofibromin binds the N-terminal domain of hyperpolarization-activated cyclic nucleotide-gated channel 1, modulating neuronal inward cationic currents (Ih) in a RAS-independent manner [anastasaki-2022-ras-beyond-abstract].

**Estrogen receptor:** In breast cancer cells, neurofibromin translocates to the nucleus to bind ER and function as a transcriptional co-repressor, independent of Ras signaling [anastasaki-2022-ras-beyond-abstract].

## Regulation of Neurofibromin

The activity and abundance of neurofibromin are tightly controlled through post-translational modifications, particularly phosphorylation and ubiquitin-mediated proteolysis.

**Phosphorylation:** Multiple kinases phosphorylate neurofibromin at distinct sites with different functional consequences. PKC-alpha phosphorylates the CSRD in response to EGF stimulation, increasing GAP activity and promoting association with actin [bergoug-2020-neurofibromin-review-abstract]. PKC-epsilon phosphorylates S2808 in the CTD, promoting nuclear accumulation in a cell-cycle-dependent manner. PKA phosphorylates both the CSRD and CTD; CTD phosphorylation promotes 14-3-3 protein binding, which inhibits GAP activity [bergoug-2020-neurofibromin-review-abstract].

**Ubiquitination and proteasomal degradation:** Neurofibromin is dynamically regulated by the ubiquitin-proteasome pathway. Growth factor stimulation triggers rapid neurofibromin ubiquitination and proteasomal degradation, transiently releasing negative regulation of Ras to allow signal propagation; subsequently, neurofibromin levels are restored to terminate signaling [cichowski-2003-nf1-proteolysis-ras-abstract]. The Cul3 E3 ligase and its BTB adaptor protein KBTBD7 catalyze PKC-driven ubiquitination of neurofibromin [bergoug-2020-neurofibromin-review-abstract]. Hypoxia-associated factor (HAF) also promotes neurofibromin ubiquitination and degradation, particularly under hypoxic conditions. Pathological hyperactivation of PKC, as observed in some glioblastomas, can cause chronic neurofibromin destabilization even in cells with intact NF1 genes, representing a non-mutational mechanism of Ras pathway activation [bergoug-2020-neurofibromin-review-abstract].

**Alternative splicing:** The NF1 gene undergoes alternative splicing generating multiple isoforms with distinct properties. The most studied variant involves exon 23a (30alt31), located within the GRD. Inclusion of exon 23a results in reduced RasGAP activity; this Type II isoform is preferentially expressed in differentiated cells, while Type I (lacking exon 23a) predominates in proliferating cells [anastasaki-2022-ras-beyond-abstract]. Other tissue-specific isoforms include exon 9a (CNS neurons), exon 48a (heart and muscle), and exon 10a-2 (transmembrane segment for ER localization) [bergoug-2020-neurofibromin-review-abstract].

## Evolutionary Conservation

Neurofibromin is an ancient and highly conserved protein with clear orthologs from yeast to humans. The budding yeast Saccharomyces cerevisiae possesses two neurofibromin homologs, IRA1 and IRA2, which encode Ras-GTPase activating proteins with conserved sequence and function [wallace-1990-nf1-cloning-abstract]. The initial identification of neurofibromin as a RasGAP came from the observation of extensive homology to IRA1 and IRA2, covering exons 16-22 and 26-40 outside the core GRD [bergoug-2020-neurofibromin-review-abstract]. Functional conservation is demonstrated by the ability of the NF1 GRD to complement yeast IRA mutants and to inhibit both wild-type and mutant activated human H-ras genes when co-expressed in yeast.

The conserved domains extend beyond the GRD. The cysteine-serine-rich domain (CSRD), RasGAP domain, and C-terminal domain (CTD) of neurofibromin are all conserved in yeast Ira1 and Ira2 proteins. Yeast Ira proteins also contain bipartite phospholipid binding modules consisting of Sec14-homologous segments and pleckstrin homology-like domains, indicating that lipid-binding function is evolutionarily ancient. The CTD has been shown to regulate the metaphase-to-anaphase transition in both human cells and yeast, demonstrating conserved cell cycle functions.

In Drosophila melanogaster, the Nf1 gene encodes proteins of 2764 or 2802 amino acids (depending on alternative splicing) that are 60% identical to human neurofibromin. Loss of Drosophila Nf1 results in excess Ras-Raf-ERK signaling and a non-cell-autonomous cAMP/PKA signaling defect, phenotypes that parallel human NF1 deficiency. Studies in Drosophila were particularly important for establishing the Ras-independent cAMP regulatory function of neurofibromin.

Among vertebrates, conservation is extremely high. Fugu rubripes (pufferfish) neurofibromin shows 91.5% identity to human neurofibromin despite over 400 million years of evolutionary divergence. Mouse and human neurofibromin share 98% identity, enabling the use of mouse models to study NF1 disease mechanisms. This extraordinary degree of conservation across vertebrates underscores the fundamental importance of neurofibromin in cellular regulation and suggests strong evolutionary constraint against mutations that alter protein function.

## Open Questions

Despite three decades of intensive research, significant questions remain about neurofibromin biology:

1. **Full-length structure and dynamics:** While the cryo-EM structure of neurofibromin isoform 2 has been determined, the precise mechanisms controlling the transition between closed (auto-inhibited) and open (active) conformations remain incompletely understood. What cellular signals trigger conformational switching, and how is this coupled to membrane recruitment?

2. **Non-canonical functions:** The RasGAP domain comprises only ~10% of neurofibromin. What are the precise molecular functions of the remaining 90% of the protein? The diverse phenotypes in NF1 patients suggest cell-type-specific functions that remain to be fully characterized.

3. **Nuclear function:** Although neurofibromin clearly localizes to the nucleus in a cell-cycle-dependent manner and interacts with the estrogen receptor and nuclear matrix proteins, the full scope of its nuclear functions remains unclear. Does neurofibromin have direct roles in transcription regulation or chromatin organization?

4. **Isoform-specific functions:** How do the different alternatively spliced isoforms of neurofibromin contribute to tissue-specific functions and disease manifestations? Are there therapeutic opportunities in modulating splicing?

5. **Membrane lipid interactions:** The Sec14-PH module binds specific phospholipids, but the functional significance of these interactions for neurofibromin localization and activity is not fully understood.

6. **Dopamine regulation mechanism:** While reduced dopamine levels in NF1 heterozygotes are well-documented and respond to L-DOPA treatment, the precise molecular mechanism by which neurofibromin regulates dopamine homeostasis remains unknown.

7. **Non-tumor manifestations:** The majority of NF1 patients experience learning disabilities, attention deficits, and other cognitive problems that are not explained solely by Ras hyperactivation. Understanding the full spectrum of Ras-independent neurofibromin functions is critical for developing therapies targeting these common manifestations.

8. **Therapeutic targeting of non-GAP functions:** Current therapeutic strategies focus on downstream pathway inhibition (MEK inhibitors, mTOR inhibitors). Could direct targeting of neurofibromin-protein interactions, such as the CRMP2 interaction for pain or HCN channel modulation for learning deficits, provide more specific therapeutic approaches?

## References

- [wallace-1990-nf1-cloning-abstract] Wallace MR, Marchuk DA, Andersen LB, et al. "Type 1 neurofibromatosis gene: identification of a large transcript disrupted in three NF1 patients." Science. 1990 Jul 13;249(4965):181-186. PMID: 2134734. DOI: 10.1126/science.2134734

- [marchuk-1991-nf1-complete-sequence-abstract] Marchuk DA, Saulino AM, Tavakkol R, et al. "cDNA cloning of the type 1 neurofibromatosis gene: complete sequence of the NF1 gene product." Genomics. 1991 Dec;11(4):931-940. PMID: 1783401. DOI: 10.1016/0888-7543(91)90017-9

- [bergoug-2020-neurofibromin-review-abstract] Bergoug M, Doudeau M, Godin F, et al. "Neurofibromin Structure, Functions and Regulation." Cells. 2020 Oct 27;9(11):2365. PMID: 33121128. PMCID: PMC7692384. DOI: 10.3390/cells9112365

- [anastasaki-2022-ras-beyond-abstract] Anastasaki C, Orozco P, Gutmann DH. "RAS and beyond: the many faces of the neurofibromatosis type 1 protein." Disease Models & Mechanisms. 2022 Feb 21;15(2):dmm049362. PMID: 35188187. PMCID: PMC8891636. DOI: 10.1242/dmm.049362

- [scheffzek-1998-grd-structure-abstract] Scheffzek K, Ahmadian MR, Wiesmuller L, et al. "Structural analysis of the GAP-related domain from neurofibromin and its implications." The EMBO Journal. 1998 Aug 3;17(15):4313-4327. PMID: 9687500. PMCID: PMC1170765. DOI: 10.1093/emboj/17.15.4313

- [yap-2014-nf1-bench-bedside-abstract] Yap YS, et al. "The NF1 gene revisited – from bench to bedside." Oncotarget. 2014 Jul 7;5(15):5873-5892. PMID: 25026295. PMCID: PMC4171599. DOI: 10.18632/oncotarget.2194

- [stowe-2012-spred1-nf1-legius-abstract] Stowe IB, et al. "A shared molecular mechanism underlies the human rasopathies Legius syndrome and Neurofibromatosis-1." Genes & Development. 2012 Jul 1;26(13):1421-1426. PMID: 22751498. PMCID: PMC3403010. DOI: 10.1101/gad.190876.112

- [yan-2020-spred1-nf1-kras-structure-abstract] Yan W, et al. "Structural Insights into the SPRED1-Neurofibromin-KRAS Complex and Disruption of SPRED1-Neurofibromin Interaction by Oncogenic EGFR." Cell Reports. 2020 Aug 4;32(5):107988. PMID: 32755583. PMCID: PMC7437355. DOI: 10.1016/j.celrep.2020.107988

- [naima-2016-spred1-grd-binding-abstract] Naima S, Stehle J, et al. "The neurofibromin recruitment factor Spred1 binds to the GAP related domain without affecting Ras inactivation." PNAS. 2016 Jun 28;113(26):7299-7304. PMID: 27313208. PMCID: PMC4941445. DOI: 10.1073/pnas.1607298113

- [johannessen-2005-nf1-tsc2-mtor-abstract] Johannessen CM, Reczek EE, James MF, et al. "The NF1 tumor suppressor critically regulates TSC2 and mTOR." PNAS. 2005 Jun 21;102(24):8573-8578. PMID: 15937108. PMCID: PMC1150820. DOI: 10.1073/pnas.0503224102

- [tong-2002-nf1-sec14-lipid-abstract] Tong J, et al. "The sec14 homology module of neurofibromin binds cellular glycerophospholipids: mass spectrometry and structure of a lipid complex." Journal of Molecular Biology. 2007 Jan 19;365(5):1276-1292. PMID: 17187824. DOI: 10.1016/j.jmb.2006.10.066

- [mouber-2018-crmp2-nf1-pain-abstract] Mouber SL, et al. "CRMP2-Neurofibromin Interface Drives NF1-related Pain." Neuroscience. 2018 May 1;381:79-90. PMID: 29684481. PMCID: PMC5963520. DOI: 10.1016/j.neuroscience.2018.04.018

- [siebert-2001-nf1-cytoskeleton-localization-abstract] Siebert K, et al. "Differential localization of the neurofibromatosis 1 (NF1) gene product, neurofibromin, with the F-actin or microtubule cytoskeleton during differentiation of telencephalic neurons." Brain Research. Developmental Brain Research. 2001 Oct 15;130(2):201-213. PMID: 11675125. DOI: 10.1016/S0165-3806(01)00190-0

- [hsueh-2001-nf1-camp-adenylyl-cyclase-abstract] Hsueh JC, et al. "Neurofibromin regulates G protein-stimulated adenylyl cyclase activity." Nature Neuroscience. 2001 Apr;4(4):428-433. PMID: 11276236. DOI: 10.1038/nn792

- [cichowski-2003-nf1-proteolysis-ras-abstract] Cichowski K, Santiago S, Jardim M, et al. "Dynamic regulation of the Ras pathway via proteolysis of the NF1 tumor suppressor." Genes & Development. 2003 Feb 15;17(4):449-454. PMID: 12600939. PMCID: PMC195996. DOI: 10.1101/gad.1054703

- [phillips-2003-nf1-mechanism-kinetics-abstract] Phillips RA, Hunter JL, Eccleston JF, Webb MR. "The mechanism of Ras GTPase activation by neurofibromin." Biochemistry. 2003 Apr 8;42(13):3956-3965. PMID: 12667087. DOI: 10.1021/bi027316z

- [lupton-2021-cryoem-nf1-dimer-abstract] Lupton CJ, Bayly-Jones C, D'Andrea L, et al. "The cryo-EM structure of the human neurofibromin dimer reveals the molecular basis for neurofibromatosis type 1." Nature Structural & Molecular Biology. 2021 Dec;28(12):982-988. PMID: 34887559. DOI: 10.1038/s41594-021-00687-2

- [naschberger-2021-nf1-isoform2-structure-abstract] Naschberger A, et al. "The structure of neurofibromin isoform 2 reveals different functional states." Nature. 2021;599:315-319. PMID: 34645999. DOI: 10.1038/s41586-021-04024-x


## Citations

1. anastasaki-2022-ras-beyond-abstract.md
2. anastasaki-2022-ras-beyond-summary.md
3. bergoug-2020-neurofibromin-review-abstract.md
4. bergoug-2020-neurofibromin-review-summary.md
5. cichowski-2003-nf1-proteolysis-ras-abstract.md
6. hsueh-2001-nf1-camp-adenylyl-cyclase-abstract.md
7. johannessen-2005-nf1-tsc2-mtor-abstract.md
8. lupton-2021-cryoem-nf1-dimer-abstract.md
9. marchuk-1991-nf1-complete-sequence-abstract.md
10. mouber-2018-crmp2-nf1-pain-abstract.md
11. naima-2016-spred1-grd-binding-abstract.md
12. naschberger-2021-nf1-isoform2-structure-abstract.md
13. phillips-2003-nf1-mechanism-kinetics-abstract.md
14. scheffzek-1998-grd-structure-abstract.md
15. scheffzek-1998-grd-structure-summary.md
16. siebert-2001-nf1-cytoskeleton-localization-abstract.md
17. stowe-2012-spred1-nf1-legius-abstract.md
18. tong-2002-nf1-sec14-lipid-abstract.md
19. wallace-1990-nf1-cloning-abstract.md
20. yan-2020-spred1-nf1-kras-structure-abstract.md
21. yap-2014-nf1-bench-bedside-abstract.md