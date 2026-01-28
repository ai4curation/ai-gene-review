---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T07:35:42.122364'
end_time: '2026-01-23T08:01:14.417939'
duration_seconds: 1532.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PARD6A
  gene_symbol: PARD6A
  uniprot_accession: Q9NPB6
  protein_description: 'RecName: Full=Partitioning defective 6 homolog alpha; Short=PAR-6;
    Short=PAR-6 alpha; Short=PAR-6A; AltName: Full=PAR6C; AltName: Full=Tax interaction
    protein 40; Short=TIP-40;'
  gene_info: Name=PARD6A; Synonyms=PAR6A;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PAR6 family. .
  protein_domains: PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270);
    PB1_Par6. (IPR034868); PDZ. (IPR001478)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NPB6
- **Protein Description:** RecName: Full=Partitioning defective 6 homolog alpha; Short=PAR-6; Short=PAR-6 alpha; Short=PAR-6A; AltName: Full=PAR6C; AltName: Full=Tax interaction protein 40; Short=TIP-40;
- **Gene Information:** Name=PARD6A; Synonyms=PAR6A;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PAR6 family. .
- **Key Domains:** PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270); PB1_Par6. (IPR034868); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PARD6A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PARD6A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PARD6A** (gene ID: PARD6A, UniProt: Q9NPB6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PARD6A (Partitioning Defective 6 Homolog Alpha): A Comprehensive Functional Analysis

## Introduction

PARD6A (Partitioning Defective 6 Homolog Alpha), also known as PAR-6, PAR-6A, PAR6C, or Tax-interacting protein 40 (TIP-40), is a 346-amino acid scaffolding protein encoded by the PARD6A gene located on human chromosome 16q22.1 [joberty-2000-par6-cdc42-abstract]. The protein serves as a critical component of the evolutionarily conserved PAR (partitioning-defective) polarity complex, which plays fundamental roles in establishing and maintaining cellular asymmetry across diverse cell types and organisms. Originally identified through genetic screens in *Caenorhabditis elegans* as essential for asymmetric cell division, the PAR proteins have since been recognized as master regulators of cell polarity in metazoans [lin-2000-par3-par6-aPKC-abstract].

PARD6A functions primarily as an adapter protein that links multiple signaling components to coordinate cell polarity. It does not possess intrinsic enzymatic activity; rather, it acts as a molecular scaffold that brings together the small GTPase CDC42, atypical protein kinase C (aPKC), and other polarity determinants to enable spatially restricted signaling [henrique-2003-par6-aPKC-review-abstract]. This scaffolding function is mediated through three principal structural domains: an N-terminal PB1 (Phox and Bem1) domain, a central semi-CRIB (Cdc42/Rac Interactive Binding) motif, and a C-terminal PDZ (PSD95/Discs-large/ZO-1) domain [joberty-2000-par6-cdc42-abstract]. Through these domains, PARD6A integrates signals from Rho family GTPases to regulate aPKC kinase activity and thereby orchestrates the establishment of distinct membrane domains essential for epithelial polarity, asymmetric cell division, and directed cell migration.

## Molecular Structure and Domain Organization

The structural architecture of PARD6A is highly specialized for its scaffolding function. The protein contains three functionally distinct domains that mediate specific protein-protein interactions essential for polarity complex assembly and regulation [garrard-2003-cdc42-par6-structure-abstract].

The N-terminal PB1 domain (amino acids 15-95) mediates the interaction with aPKC isoforms, specifically PKCiota (PRKCI) and PKCzeta (PRKCZ) [dong-2020-aPKC-par6-membrane-abstract]. This domain-domain interaction between the PB1 domains of Par6 and aPKC is critical for complex formation and has been shown to both inhibit aPKC kinase activity and allosterically expose the polybasic pseudosubstrate region of aPKC, enabling its membrane targeting [dong-2020-aPKC-par6-membrane-abstract]. The PB1-mediated interaction creates a constitutive Par6-aPKC heterodimer that forms the core signaling unit of the PAR complex [henrique-2003-par6-aPKC-review-abstract].

The semi-CRIB motif (amino acids 133-150) and adjacent PDZ domain (amino acids 157-250) together form a unique GTPase-binding domain (GBD) that recognizes GTP-bound CDC42 and RAC1 [garrard-2003-cdc42-par6-structure-abstract]. Crystal structure analysis at 2.1 Angstrom resolution revealed that the semi-CRIB motif forms a beta-strand that inserts between the four strands of Cdc42 and the three strands of the PDZ domain to create a continuous eight-stranded beta-sheet [garrard-2003-cdc42-par6-structure-abstract]. This structural arrangement is unique among CRIB-containing proteins and explains why the PDZ domain is required, in addition to the semi-CRIB motif, for CDC42 binding. The structure highlights a novel role for the PDZ domain as a structural scaffold rather than solely a peptide-binding module [garrard-2003-cdc42-par6-structure-abstract].

The PDZ domain also mediates interactions with several other polarity proteins, most notably CRB3 (Crumbs homolog 3), which binds through its C-terminal ERLI motif with an apparent affinity of approximately 300 nM [lemmers-2004-crb3-par6-abstract]. Importantly, CDC42 binding to the semi-CRIB/PDZ region allosterically enhances the affinity of the PDZ domain for its C-terminal peptide ligands by approximately 13-fold, providing a mechanism for signal-dependent complex assembly [garrard-2003-cdc42-par6-structure-abstract].

## The PAR Polarity Complex: Assembly and Regulation

PARD6A is the central organizing component of the PAR polarity complex, which in its canonical form comprises PAR3 (PARD3), PAR6 (PARD6A/B/G), and aPKC (PRKCI or PRKCZ) [chen-2013-par3-par6-aPKC-review-abstract]. The assembly of this complex is regulated by the small GTPase CDC42 in a GTP-dependent manner, providing a mechanism by which extracellular signals and cellular geometry can influence polarity establishment [joberty-2000-par6-cdc42-abstract].

The core of the signaling complex is composed of Par6 and aPKC, with the signaling potential residing in aPKC's kinase activity, while Par6 functions as a key regulator of aPKC kinase activity [henrique-2003-par6-aPKC-review-abstract]. In the basal state, Par6 binding to aPKC via their PB1 domains inhibits aPKC kinase activity. This inhibition is relieved upon binding of GTP-loaded CDC42 to the Par6 CRIB-PDZ domain, which triggers conformational changes that activate aPKC [dong-2020-aPKC-par6-membrane-abstract]. This mechanism ensures that aPKC is only active when the complex is properly assembled and positioned at the appropriate membrane domain.

The molecular basis for Par6-mediated regulation of aPKC membrane targeting has been elucidated by recent structural and biochemical studies [dong-2020-aPKC-par6-membrane-abstract]. The pseudosubstrate region (PSr) of aPKC functions as a polybasic domain that can bind directly to plasma membrane phosphoinositides (PI4P and PIP2). In unbound aPKC, this polybasic region is occluded by the kinase domain. Par6 binding via PB1 domains induces conformational changes that expose the PSr for membrane binding, while simultaneously inhibiting kinase activity [dong-2020-aPKC-par6-membrane-abstract]. Full activation requires additional input from apical membrane proteins such as Crumbs.

PAR3 contributes to complex function primarily as a scaffold that can recruit the Par6-aPKC heterodimer to specific membrane locations [lin-2000-par3-par6-aPKC-abstract]. The interaction between Par3 and Par6 occurs through their PDZ domains, although this interaction appears to be regulated and is not required for all Par6 functions [lin-2000-par3-par6-aPKC-abstract]. Indeed, PAR3 also serves as both a substrate and an inhibitor of aPKC, suggesting complex regulatory relationships within the ternary complex [lin-2000-par3-par6-aPKC-abstract].

## Subcellular Localization and Membrane Targeting

PARD6A exhibits a complex subcellular distribution that reflects its diverse functions in different cellular contexts. The protein localizes to multiple compartments including the cytoplasm, plasma membrane, cell-cell junctions, and the centrosome [solecki-2004-par6-neuronal-migration-abstract].

In polarized epithelial cells, PARD6A is concentrated at tight junctions, where it colocalizes with the tight junction protein ZO-1 (TJP1), CDC42/RAC1, PARD3, and PRKCI [gao-2002-par6-tight-junction-abstract][hurd-2003-par6-pals1-abstract]. This junctional localization is consistent with the protein's role in regulating tight junction assembly and maintenance. Recruitment to the apical membrane is mediated in part through the interaction with CRB3, which binds the Par6 PDZ domain [lemmers-2004-crb3-par6-abstract].

The connection between the PAR complex and the Crumbs complex represents a critical point of integration for apical polarity determination. PARD6A interacts directly with PALS1 (also known as MPP5), a component of the Crumbs complex, through a PDZ-mediated interaction that requires the amino terminus of PALS1 and is enhanced by CDC42-GTP binding to Par6 [hurd-2003-par6-pals1-abstract]. This interaction provides a biochemical link between the two major apical polarity complexes and explains how they cooperate in tight junction assembly.

Beyond junctional localization, PARD6A also accumulates at the centrosome and centriolar satellites in migrating neurons and other cell types [solecki-2004-par6-neuronal-migration-abstract]. This centrosomal pool of Par6 is recruited through interactions with dynactin components (DCTN1/p150Glued) and centrosomal proteins (PCM1), and is important for coordinating centrosome positioning with nuclear movement during cell migration [solecki-2004-par6-neuronal-migration-abstract].

## Role in Epithelial Polarity and Tight Junction Regulation

One of the best-characterized functions of PARD6A is its role in establishing and maintaining apical-basal polarity in epithelial cells. Epithelial cells form polarized sheets with distinct apical and basolateral membrane domains separated by tight junctions, which serve as both physical barriers and signaling platforms [chen-2013-par3-par6-aPKC-review-abstract].

Surprisingly, PARD6A appears to function as a negative regulator of tight junction assembly under certain conditions [gao-2002-par6-tight-junction-abstract]. Overexpression of Par6 in MDCK II epithelial cells inhibited tight junction assembly following calcium switch-induced disruption, without affecting adherens junction formation [gao-2002-par6-tight-junction-abstract]. Transepithelial resistance measurements and paracellular diffusion assays confirmed that assembly of functional tight junctions was delayed by Par6 overexpression [gao-2002-par6-tight-junction-abstract]. This negative regulatory function is likely important for the dynamic remodeling of junctions during epithelial morphogenesis and requires the association of Par6 with aPKC.

The mechanism by which Par6 regulates tight junctions involves its interaction with PAR3 and the junctional adhesion molecule JAM1 (F11R). Association of PARD6A with PARD3 can prevent the interaction of PARD3 with JAM1, thereby inhibiting tight junction assembly [gao-2002-par6-tight-junction-abstract]. This suggests a model in which the relative amounts and activity states of polarity complex components determine the rate of junction formation.

The interaction between Par6 and CRB3 adds another layer of regulation. CRB3 expression in MDCK cells led to slower development of functional tight junctions, and this phenotype depended on the presence of the CRB3 PDZ-binding domain that mediates direct interaction with Par6 [lemmers-2004-crb3-par6-abstract]. Together, these findings indicate that PARD6A plays a complex role in tight junction regulation, potentially serving to modulate the kinetics of junction assembly rather than simply promoting or preventing junction formation.

## Function in Asymmetric Cell Division

The PAR proteins were originally identified through their essential roles in asymmetric cell division in *C. elegans*, and this function is conserved in mammalian cells [lin-2000-par3-par6-aPKC-abstract]. PARD6A participates in the unequal distribution of cell fate determinants during asymmetric divisions, ensuring that daughter cells receive different complements of regulatory proteins and adopt distinct fates.

A principal mechanism by which the PAR complex directs asymmetric division involves the phosphorylation of the cytoskeletal protein Lethal (2) giant larvae (Lgl) by aPKC [betschinger-2003-par-lgl-abstract]. In Drosophila neuroblasts, the Par complex localizes to the apical cortex and phosphorylates Lgl at three conserved serine residues [betschinger-2003-par-lgl-abstract]. This phosphorylation releases Lgl from its association with membranes and the actin cytoskeleton, effectively excluding it from the apical domain [betschinger-2003-par-lgl-abstract]. The non-phosphorylated Lgl remains at the basal cortex, where it helps recruit and retain cell fate determinants including Miranda, Numb, and Prospero.

The Par6-aPKC-Lgl regulatory circuit represents a mutual antagonism that is fundamental to polarity establishment. Lgl can inhibit aPKC, and aPKC phosphorylates Lgl to displace it from the membrane [betschinger-2003-par-lgl-abstract]. This mutual exclusion mechanism generates complementary membrane domains along the polarity axis. Recent studies have shown that Par6 also directly associates with Lgl, and that the Par6-aPKC complex processively phosphorylates all three Lgl sites through a dynamic interaction mechanism that ensures complete substrate modification [betschinger-2003-par-lgl-abstract].

## Role in Neuronal Migration and Centrosome Function

Beyond epithelial polarity, PARD6A plays important roles in the central nervous system, particularly in the regulation of glial-guided neuronal migration during brain development [solecki-2004-par6-neuronal-migration-abstract]. Neuronal migration involves the coordinated two-stroke movement of the centrosome and nucleus, with the centrosome moving forward before nuclear translocation [solecki-2004-par6-neuronal-migration-abstract].

Studies in cerebellar granule neurons revealed that Par6alpha and aPKCzeta are enriched at the centrosome and are essential for the integrity and movement of this organelle [solecki-2004-par6-neuronal-migration-abstract]. The proteins also participate in the assembly of a perinuclear microtubule cage that encompasses the nucleus and coordinates its translocation [solecki-2004-par6-neuronal-migration-abstract]. Overexpression of mPar6alpha disrupted the perinuclear tubulin cage, retargeted PKCzeta and gamma-tubulin away from the centrosome, and inhibited both centrosomal motion and neuronal migration [solecki-2004-par6-neuronal-migration-abstract].

This centrosomal function of Par6 involves interactions with dynactin components, suggesting that Par6 coordinates microtubule motor activity with polarity signaling. The authors of this study proposed that during neuronal migration, the centrosome acts to coordinate cytoskeletal dynamics in response to mPar6alpha-mediated signaling [solecki-2004-par6-neuronal-migration-abstract].

## TGF-beta Signaling and Epithelial-Mesenchymal Transition

A particularly significant discovery was the identification of PARD6A as a direct substrate of TGF-beta receptors and its role in regulating epithelial-mesenchymal transition (EMT) [ozdamar-2005-par6-tgfb-emt-abstract]. EMT is a critical process during development and cancer metastasis in which epithelial cells lose their polarity and cell-cell adhesion to become migratory mesenchymal cells.

The mechanism involves the recruitment of PARD6A to tight junctions through its interaction with TGFBR1, which presents Par6 to the type II TGF-beta receptor (TGFBR2) [ozdamar-2005-par6-tgfb-emt-abstract]. Upon TGF-beta stimulation, activated TGFBR2 phosphorylates Par6 at serine 345 (Ser345) [ozdamar-2005-par6-tgfb-emt-abstract]. This phosphorylation is required for TGF-beta-dependent EMT in mammary gland epithelial cells and controls the interaction of Par6 with the E3 ubiquitin ligase Smurf1.

Phosphorylated Par6 recruits Smurf1 to tight junctions, where Smurf1 ubiquitinates the small GTPase RhoA and targets it for proteasomal degradation [ozdamar-2005-par6-tgfb-emt-abstract]. Since RhoA is essential for actin cytoskeleton organization at tight junctions, its degradation leads to dissolution of tight junctions and loss of epithelial polarity [ozdamar-2005-par6-tgfb-emt-abstract]. Expression of Par6(S345A) mutant cells displayed stable tight junctions even after prolonged TGF-beta stimulation, confirming that this phosphorylation site is critical for TGF-beta-induced EMT [ozdamar-2005-par6-tgfb-emt-abstract].

This represents a Smad-independent pathway by which TGF-beta signaling promotes EMT, demonstrating that PARD6A serves as a critical node connecting growth factor signaling to the polarity machinery.

## Tissue Expression Patterns

PARD6A exhibits a broad but non-uniform expression pattern across human tissues. Northern blot analyses have revealed that PARD6A mRNA is expressed in all tissues examined, with highest levels in brain, pancreas, and skeletal muscle, and lowest expression in placenta and lung [OMIM-607484]. A 1.4-kb transcript has been detected most abundantly in pancreas, skeletal muscle, brain, and heart, with lower levels in kidney and placenta [joberty-2000-par6-cdc42-abstract]. In fetal tissues, expression is highest in brain, consistent with the important roles of Par6 in neural development [OMIM-607484].

At the protein level, data from the Human Protein Atlas indicate that PARD6A shows tissue-enhanced expression primarily in the brain and testis [human-protein-atlas-PARD6A]. Within the brain, the cerebellum exhibits the highest regional expression (38.5 nTPM), while testis demonstrates notably elevated levels (41.3 nTPM). The protein displays cytoplasmic expression across multiple tissues with subcellular localization primarily to actin filaments, plasma membrane, cell junctions, and cytosol [human-protein-atlas-PARD6A].

A striking finding from single-cell RNA sequencing studies is the remarkable enrichment of PARD6A in late spermatids, suggesting a specialized role during spermiogenesis and sperm cell maturation [human-protein-atlas-PARD6A]. This is consistent with the known roles of PAR proteins in establishing cell polarity during germ cell development and the asymmetric organization required for sperm function. Additionally, PARD6A has been identified as a prognostic marker in pancreatic adenocarcinoma, indicating potential clinical relevance in cancer progression assessment [human-protein-atlas-PARD6A].

## Evolutionary Conservation

The PAR proteins represent one of the most highly conserved cell polarity systems in the animal kingdom. Six par genes (par-1 through par-6) were first identified in *Caenorhabditis elegans* through genetic screens for mutants affecting the pattern of early embryonic cell divisions [goldstein-2007-par-proteins-review]. Loss-of-function mutations in any par locus result in loss of anterior-posterior asymmetries during the first embryonic cell divisions, demonstrating their essential and non-redundant roles in polarity establishment.

The PAR-3/PAR-6/aPKC complex is conserved throughout evolution and is required to establish polarity in many different cell types across diverse organisms [goldstein-2007-par-proteins-review]. In *C. elegans*, three PAR polarity proteins localize in the anterior cortex of the one-cell embryo: PAR-3 (containing three PDZ domains), PAR-6 (containing a single PDZ domain and a CRIB-like domain), and PKC-3 (an atypical protein kinase C). In *Drosophila* neuroblasts, the orthologous proteins Bazooka (PAR-3), DmPAR-6, and DaPKC form a cortical crescent required for asymmetric division and proper segregation of cell fate determinants.

The remarkable conservation of PAR protein function extends to mammals, where PARD3, PARD6 (with three isoforms: PARD6A, PARD6B, PARD6G), and aPKC isoforms (PRKCI and PRKCZ) perform analogous functions in epithelial polarity, neuronal development, and asymmetric cell division [lin-2000-par3-par6-aPKC-abstract]. In mammalian epithelia, these orthologues localize to junctional complexes and are required for the establishment and maintenance of apical-basal polarity. Given what is known about PAR protein functions across animal systems, it appears that all PAR proteins except PAR-2 were fundamental players in cell polarization mechanisms more than 500 million years ago, in the ancestors of *C. elegans*, *Drosophila*, mammals, and all other bilateral animals [goldstein-2007-par-proteins-review].

Despite this deep conservation, there are important context-dependent and cell-type-specific differences in PAR protein function. For example, whereas the *C. elegans* embryo uses a distinct anterior (PAR-3/PAR-6/PKC-3) and posterior (PAR-1/PAR-2) system, vertebrate epithelial cells employ a more complex network of interactions involving the PAR complex, the Crumbs complex, and the Scribble complex to establish apical-basal polarity. The expansion of the Par6 family to three isoforms in mammals may allow for tissue-specific regulation and functional specialization that is not possible with a single Par6 gene [chen-2013-par3-par6-aPKC-review-abstract].

## PARD6A in Cancer

Given its central role in maintaining epithelial polarity and tight junction integrity, it is not surprising that PARD6A has been implicated in cancer biology. Disruption of cell polarity is a hallmark of epithelial cancers, and several polarity genes including Dlg, Lgl, Scrib, and aPKC have been identified as tumor suppressors [chen-2013-par3-par6-aPKC-review-abstract].

The role of PARD6A in cancer appears to be context-dependent. Expression of Par6 alone in mammary epithelial cells can induce epidermal growth factor-independent cell proliferation and development of hyperplastic acini through sustained activation of MEK/Erk signaling [chen-2013-par3-par6-aPKC-review-abstract]. This proliferative effect is dependent on the ability of Par6 to interact with aPKC and Cdc42, but independent of Lgl and Par3 interactions [chen-2013-par3-par6-aPKC-review-abstract].

Among the three mammalian Par6 family members, PARD6B appears most strongly implicated in breast cancer, with the PARD6B locus residing in a chromosomal region (20q13.13) that is frequently amplified [chen-2013-par3-par6-aPKC-review-abstract]. PARD6A has been shown to promote epithelial-mesenchymal transition in ovarian cancer through the integrin beta1-ILK-SNAIL1 pathway, suggesting it can act as an inducer of cell migration and invasion during metastasis [chen-2013-par3-par6-aPKC-review-abstract].

## Open Questions

Despite substantial progress in understanding PARD6A function, several important questions remain unresolved:

1. **Isoform-specific functions**: Mammals express three Par6 isoforms (PARD6A, PARD6B, PARD6G) with high sequence homology in their functional domains but variable C-termini. The extent to which these isoforms have distinct versus redundant functions in different cell types remains incompletely characterized.

2. **Regulation of Par6-aPKC complex activity**: While the general mechanism by which CDC42 activates the Par6-aPKC complex is established, the precise molecular details of how allosteric changes propagate from the CDC42 binding site to the aPKC kinase domain remain to be fully elucidated.

3. **Phase separation and complex dynamics**: Recent work has suggested that the Par complex can form condensates through liquid-liquid phase separation, particularly in neuroblasts. The relevance of phase separation to Par complex function in mammalian cells and how it is regulated is an active area of investigation.

4. **Integration with other signaling pathways**: PARD6A interacts with multiple signaling pathways beyond TGF-beta, including ephrin, HTLV-1 Tax, and Wnt signaling. The physiological significance of these interactions and how they are coordinated is not well understood.

5. **Therapeutic targeting**: Given the role of polarity disruption in cancer, the Par complex represents a potential therapeutic target. However, whether selective modulation of Par6 function is feasible and what the consequences would be for normal tissue homeostasis remains to be determined.

6. **Post-translational modifications**: Beyond Ser345 phosphorylation by TGF-beta receptors, PARD6A is subject to additional phosphorylation events and ubiquitination by the SCF(FBXO31) complex. The regulatory significance of these modifications and the signals that control them require further investigation.

## References

1. **joberty-2000-par6-cdc42**: Joberty G, Petersen C, Gao L, Macara IG. The cell-polarity protein Par6 links Par3 and atypical protein kinase C to Cdc42. Nature Cell Biology. 2000;2(8):531-539. PMID: 10934474. DOI: 10.1038/35019573. https://www.nature.com/articles/ncb0800_531

2. **lin-2000-par3-par6-aPKC**: Lin D, Edwards AS, Fawcett JP, Mbamalu G, Scott JD, Pawson T. A mammalian PAR-3-PAR-6 complex implicated in Cdc42/Rac1 and aPKC signalling and cell polarity. Nature Cell Biology. 2000;2(8):540-547. PMID: 10934475. DOI: 10.1038/35019582. https://pubmed.ncbi.nlm.nih.gov/10934475/

3. **gao-2002-par6-tight-junction**: Gao L, Joberty G, Macara IG. Assembly of epithelial tight junctions is negatively regulated by Par6. Current Biology. 2002;12(3):221-225. PMID: 11839275. DOI: 10.1016/s0960-9822(01)00663-7. https://pubmed.ncbi.nlm.nih.gov/11839275/

4. **henrique-2003-par6-aPKC-review**: Henrique D, Schweisguth F. Cell polarity: the ups and downs of the Par6/aPKC complex. Current Opinion in Genetics & Development. 2003;13(4):341-350. PMID: 12888006. DOI: 10.1016/s0959-437x(03)00077-7. https://pubmed.ncbi.nlm.nih.gov/12888006/

5. **garrard-2003-cdc42-par6-structure**: Garrard SM, Capaldo CT, Gao L, Rosen MK, Macara IG, Tomchick DR. Structure of Cdc42 in a complex with the GTPase-binding domain of the cell polarity protein, Par6. EMBO Journal. 2003;22(5):1125-1133. PMID: 12606577. DOI: 10.1093/emboj/cdg110. PDB: 1NF3. https://pmc.ncbi.nlm.nih.gov/articles/PMC150343/

6. **hurd-2003-par6-pals1**: Hurd TW, Gao L, Roh MH, Macara IG, Margolis B. Direct interaction of two polarity complexes implicated in epithelial tight junction assembly. Nature Cell Biology. 2003;5(2):137-142. PMID: 12545177. DOI: 10.1038/ncb923. https://pubmed.ncbi.nlm.nih.gov/12545177/

7. **betschinger-2003-par-lgl**: Betschinger J, Mechtler K, Knoblich JA. The Par complex directs asymmetric cell division by phosphorylating the cytoskeletal protein Lgl. Nature. 2003;422(6929):326-330. PMID: 12629552. DOI: 10.1038/nature01486. https://pubmed.ncbi.nlm.nih.gov/12629552/

8. **lemmers-2004-crb3-par6**: Lemmers C, Michel D, Lane-Guermonprez L, Delgrossi MH, Médina E, Arsanto JP, Le Bivic A. CRB3 binds directly to Par6 and regulates the morphogenesis of the tight junctions in mammalian epithelial cells. Molecular Biology of the Cell. 2004;15(3):1324-1333. PMID: 14718572. DOI: 10.1091/mbc.e03-04-0235. https://pmc.ncbi.nlm.nih.gov/articles/PMC363137/

9. **solecki-2004-par6-neuronal-migration**: Solecki DJ, Model L, Gaetz J, Kapoor TM, Hatten ME. Par6alpha signaling controls glial-guided neuronal migration. Nature Neuroscience. 2004;7(11):1195-1203. PMID: 15475953. DOI: 10.1038/nn1332. https://pubmed.ncbi.nlm.nih.gov/15475953/

10. **ozdamar-2005-par6-tgfb-emt**: Ozdamar B, Bose R, Barrios-Rodiles M, Wang HR, Zhang Y, Wrana JL. Regulation of the Polarity Protein Par6 by TGFβ Receptors Controls Epithelial Cell Plasticity. Science. 2005;307(5715):1603-1609. DOI: 10.1126/science.1105718. https://www.science.org/doi/10.1126/science.1105718

11. **suzuki-2006-par-aPKC-review**: Suzuki A, Ohno S. The PAR-aPKC system: lessons in polarity. Journal of Cell Science. 2006;119(Pt 6):979-987. PMID: 16525119. DOI: 10.1242/jcs.02898. https://journals.biologists.com/jcs/article/119/6/979/29500/The-PAR-aPKC-system-lessons-in-polarity

12. **chen-2013-par3-par6-aPKC-review**: Chen J, Zhang M. The Par3/Par6/aPKC complex and epithelial cell polarity. Experimental Cell Research. 2013;319(10):1357-1364. PMID: 23535009. DOI: 10.1016/j.yexcr.2013.03.021. https://pubmed.ncbi.nlm.nih.gov/23535009/

13. **dong-2020-aPKC-par6-membrane**: Dong W, Lu J, Zhang X, Wu Y, Lettieri K, Hammond GR, Hong Y. A polybasic domain in aPKC mediates Par6-dependent control of membrane targeting and kinase activity. Journal of Cell Biology. 2020;219(7):e201903031. PMID: 32580209. DOI: 10.1083/jcb.201903031. https://pmc.ncbi.nlm.nih.gov/articles/PMC7337507/

14. **nance-2018-par3-par6-aPKC-neurons**: Nance J. PAR3-PAR6-atypical PKC polarity complex proteins in neuronal polarization. Current Opinion in Neurobiology. 2018;50:105-112. PMID: 29696344. DOI: 10.1016/j.conb.2018.01.014. https://pubmed.ncbi.nlm.nih.gov/29696344/

15. **UniProt Q9NPB6**: UniProt Consortium. UniProtKB entry Q9NPB6 - PARD6A_HUMAN. https://www.uniprot.org/uniprotkb/Q9NPB6

16. **OMIM 607484**: Online Mendelian Inheritance in Man. PARD6A - PAR6 FAMILY CELL POLARITY REGULATOR ALPHA. https://www.omim.org/entry/607484

17. **human-protein-atlas-PARD6A**: Human Protein Atlas. PARD6A protein expression summary. https://www.proteinatlas.org/ENSG00000102981-PARD6A

18. **goldstein-2007-par-proteins-review**: Goldstein B, Macara IG. The PAR Proteins: Fundamental Players in Animal Cell Polarization. Developmental Cell. 2007;13(5):609-622. PMCID: PMC2964935. DOI: 10.1016/j.devcel.2007.10.007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2964935/


## Citations

1. betschinger-2003-par-lgl-abstract.md
2. chen-2013-par3-par6-aPKC-review-abstract.md
3. dong-2020-aPKC-par6-membrane-abstract.md
4. etienne-manneville-2001-par6-cell-polarity-summary.md
5. gao-2002-par6-tight-junction-abstract.md
6. garrard-2003-cdc42-par6-structure-abstract.md
7. goldstein-2007-par-proteins-review-summary.md
8. henrique-2003-par6-aPKC-review-abstract.md
9. human-protein-atlas-PARD6A-summary.md
10. hurd-2003-par6-pals1-abstract.md
11. joberty-2000-par6-cdc42-abstract.md
12. lemmers-2004-crb3-par6-abstract.md
13. lin-2000-par3-par6-aPKC-abstract.md
14. nance-2018-par3-par6-aPKC-neurons-summary.md
15. ozdamar-2005-par6-tgfb-emt-abstract.md
16. solecki-2004-par6-neuronal-migration-abstract.md
17. suzuki-2006-par-aPKC-review-summary.md