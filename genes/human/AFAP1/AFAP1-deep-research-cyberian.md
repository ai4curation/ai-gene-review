---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T13:39:52.473310'
end_time: '2026-01-15T13:58:51.319508'
duration_seconds: 1138.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AFAP1
  gene_symbol: AFAP1
  uniprot_accession: Q8N556
  protein_description: 'RecName: Full=Actin filament-associated protein 1; AltName:
    Full=110 kDa actin filament-associated protein; Short=AFAP-110;'
  gene_info: Name=AFAP1; Synonyms=AFAP;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849);
    PH (PF00169)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8N556
- **Protein Description:** RecName: Full=Actin filament-associated protein 1; AltName: Full=110 kDa actin filament-associated protein; Short=AFAP-110;
- **Gene Information:** Name=AFAP1; Synonyms=AFAP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); PH (PF00169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AFAP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AFAP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AFAP1** (gene ID: AFAP1, UniProt: Q8N556) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AFAP1 (Actin Filament-Associated Protein 1): A Comprehensive Research Report

## Introduction

Actin filament-associated protein 1 (AFAP1), also known as AFAP-110 due to its apparent molecular weight of 110 kDa, is a multidomain adapter protein that plays a central role in linking signal transduction pathways to the actin cytoskeleton in human cells. The protein was first identified in the early 1990s as a major substrate of the oncogenic viral tyrosine kinase v-Src and was subsequently cloned by Flynn and colleagues [flynn-1993-afap110-identification-abstract]. The human gene encoding AFAP1 (UniProt: Q8N556) is located on chromosome 4p16.1 and produces a protein of approximately 635 amino acids. AFAP1 is the prototypical member of a family of three structurally related proteins that also includes AFAP1-like 1 (AFAP1L1) and AFAP1-like 2 (AFAP1L2, also known as XB130) [cunnick-2015-mammary-gland-abstract].

The defining characteristic of AFAP1 is its dual capacity to both bind and crosslink actin filaments while simultaneously serving as a scaffold for signaling molecules, most notably the non-receptor tyrosine kinase c-Src and protein kinase C alpha (PKCalpha). This unique combination of properties positions AFAP1 at the interface between extracellular signals and cytoskeletal reorganization, making it a key player in cellular processes including migration, adhesion, and invasion. The following sections describe the molecular architecture, biochemical functions, cellular localization, and physiological roles of this important signaling adapter.

## Molecular Architecture and Domain Structure

AFAP1 is organized into a series of modular protein-binding domains that facilitate its diverse functions. The domain architecture of AFAP1 has been extensively characterized through biochemical and mutational analyses [baisden-2001-afap110-review-abstract]. The protein contains two pleckstrin homology (PH) domains located in the amino-terminal half of the protein. The first PH domain (PH1), which shows highest sequence homology to PH domains from beta-spectrin and dynamin, serves as the primary binding site for PKC family members [qian-2002-pkc-crosslinking-abstract]. The second PH domain (PH2) has been less extensively characterized but may contribute to membrane targeting through phosphoinositide binding.

Between and flanking the PH domains, AFAP1 contains two juxtaposed proline-rich SH3-binding motifs of approximately 10 amino acids each, which are essential for its interaction with the Src family kinases. These motifs engage the SH3 domain of c-Src and related kinases such as Fyn. Additionally, AFAP1 contains SH2-binding motifs with phosphotyrosine residues that, when phosphorylated, can engage the SH2 domains of Src family kinases [flynn-1993-afap110-identification-abstract]. This dual SH2/SH3 binding capacity allows AFAP1 to form stable complexes with Src under various activation states.

The carboxy-terminal region of AFAP1 contains two critical functional domains: an alpha-helical actin-binding domain and a leucine zipper motif. The actin-binding domain is both necessary and sufficient for direct association with filamentous actin (F-actin), showing approximately 40% sequence similarity with other known actin-binding motifs [qian-2000-carboxy-terminus-abstract]. The leucine zipper motif, located immediately adjacent to the actin-binding domain, mediates AFAP1 self-association and multimerization [qian-1998-src-self-association-abstract]. This multimerization is functionally significant because it allows AFAP1 to form complexes with multiple actin-binding sites, thereby enabling the protein to crosslink actin filaments.

## Actin Crosslinking Function

One of the primary molecular functions of AFAP1 is its capacity to crosslink actin filaments. Biochemical studies using purified recombinant AFAP1 demonstrated that the protein binds cooperatively to actin filaments and can organize them into either loose meshwork or tight bundle structures depending on protein concentration and phosphorylation status [qian-2002-pkc-crosslinking-abstract]. The crosslinking activity depends critically on AFAP1's ability to multimerize through its leucine zipper domain, which allows the formation of complexes containing multiple actin-binding sites.

The leucine zipper motif serves a dual regulatory role in AFAP1 function. On one hand, it facilitates multimerization and thus enables actin crosslinking. On the other hand, it participates in an auto-inhibitory mechanism by making intramolecular contacts with sequences in the amino-terminal PH1 domain [qian-2004-leucine-zipper-abstract]. This auto-inhibitory configuration maintains AFAP1 in a relatively inactive conformation under basal conditions. Disruption of the leucine zipper, either through deletion mutagenesis or through phosphorylation-induced conformational changes, releases this auto-inhibition and dramatically increases the actin crosslinking capability of AFAP1. Notably, deletion of the leucine zipper motif causes AFAP1 to alter actin filament integrity and induce the formation of lamellipodia in untransformed cells, mimicking the effects of Src transformation [qian-2000-carboxy-terminus-abstract].

Size exclusion chromatography analyses have revealed that AFAP1 can exist in multiple oligomeric states in cells, ranging from monomers to tetramers in vivo and potentially higher-order multimers (up to nonamers) in vitro [qian-2004-leucine-zipper-abstract]. The transition between these oligomeric states is regulated by signaling inputs, particularly from Src and PKC.

## Regulation by Protein Kinase C

AFAP1 is a direct substrate of protein kinase C alpha (PKCalpha) and this phosphorylation plays a key regulatory role in AFAP1 function. PKCalpha binds to AFAP1 through the amino-terminal PH1 domain, and this interaction results in phosphorylation of AFAP1 on serine residues [qian-2002-pkc-crosslinking-abstract]. Mutational analysis identified Ser277 as a critical PKC phosphorylation site in AFAP1. Upon treatment with phorbol esters such as phorbol 12-myristate 13-acetate (PMA) or phorbol 12,13-dibutyrate (PDBu), which activate PKC, AFAP1 becomes phosphorylated on Ser277 and undergoes conformational changes that alter its multimerization state [qian-2002-pkc-crosslinking-abstract].

PKC phosphorylation uniquely enhances the actin crosslinking ability of AFAP1. This is in marked contrast to other actin-regulatory proteins such as fascin, MARCKS, SSeCKS, and VASP, for which PKC phosphorylation decreases actin crosslinking activity. The mechanism appears to involve reduction in AFAP1 self-association, which paradoxically increases crosslinking activity, possibly by generating a population of smaller oligomers that are more effective at bridging between filaments [qian-2002-pkc-crosslinking-abstract].

Phosphorylation of Ser277 also regulates podosome dynamics. Studies in vascular smooth muscle A7r5 cells demonstrated that expression of a non-phosphorylatable AFAP1 mutant (S277A) resulted in an increased number of long-lived podosomes, suggesting that phosphorylation and dephosphorylation at this site regulate podosome turnover and stability [dorfleutner-2008-podosome-lifespan, from Journal of Cell Science 121:2394-2405]. The Ser277 site is conserved between human, chicken, rat, and mouse AFAP1, indicating evolutionary conservation of this regulatory mechanism.

## Src Kinase Activation and Signaling

A defining feature of AFAP1 is its capacity to activate c-Src tyrosine kinase. AFAP1 was originally identified as an SH2/SH3 binding partner of Src, and subsequent studies have established that AFAP1 can function as an activator of Src family kinases in response to upstream signals [baisden-2001-afap110-review-abstract]. The mechanism involves phosphorylation-induced conformational changes in AFAP1 that relieve auto-inhibitory intramolecular interactions and expose the SH3-binding motifs, enabling engagement with the Src SH3 domain.

The intrinsic connection between AFAP1's ability to alter actin filament integrity and its capacity to activate tyrosine kinases was demonstrated through studies of the leucine zipper deletion mutant (AFAP1-ΔLzip) [baisden-2001-intrinsic-ability-abstract]. Unlike wild-type AFAP1, the ΔLzip mutant is capable of activating cellular tyrosine kinases, including Src family members, and is itself hyperphosphorylated on tyrosine residues. Critically, a point mutation that disrupts the SH3-binding motif of AFAP1-ΔLzip prevents it from activating tyrosine kinases and altering actin filament integrity. These findings demonstrate that conformational changes in AFAP1, whether induced by leucine zipper deletion or by physiological signals, enable it to activate cellular kinases through a mechanism requiring functional SH3-binding motifs. Furthermore, the downstream effects on actin filaments were shown to require RhoA activity, placing AFAP1-mediated Src activation upstream of Rho GTPase signaling in the cytoskeletal reorganization pathway.

The seminal study by Gatesman and colleagues demonstrated that AFAP1 is required for PKCalpha to activate c-Src and induce podosome formation [gatesman-2004-pkc-src-podosome-abstract]. In cell lines lacking AFAP1 expression, PKC activation by phorbol esters was unable to activate c-Src or induce podosome formation. Ectopic expression of wild-type AFAP1 rescued these responses, while mutant forms of AFAP1 that cannot bind or colocalize with c-Src were unable to do so. The data establish a linear signaling pathway in which PKCalpha phosphorylation of AFAP1 leads to AFAP1-mediated activation of c-Src, which in turn drives cytoskeletal reorganization and podosome formation.

Further studies identified an additional requirement for PI3K (phosphoinositide 3-kinase) signaling in this pathway [walker-2007-pi3k-csrc-abstract]. PI3K activity is required for PMA-induced colocalization between AFAP1 and c-Src and for subsequent c-Src activation. Cells lacking the p85 regulatory subunits of PI3K or treated with PI3K inhibitors showed defects in this signaling axis, resulting in impaired cell migration.

## Tissue Expression and Distribution

AFAP1 exhibits broad but heterogeneous expression across human tissues. According to data from the Human Protein Atlas, AFAP1 shows ubiquitous cytoplasmic expression with a granular pattern in multiple tissues. The protein is expressed in diverse cell types including stromal cells of the endometrium, cortical neurons, peripheral nerve tissue, and over 120 other cell types and tissues. Notably, AFAP1 shows relatively high expression in peripheral blood mononuclear cells and breast tissue.

The expression pattern of AFAP1 in breast tissue is of particular interest in the context of cancer biology. While normal breast epithelial cell lines such as MCF-10A show low AFAP1 expression, and tumorigenic but less invasive breast cancer cell lines (MCF-7, T-47D, ZR-75-1) also exhibit low levels, highly invasive breast cancer cell lines MDA-MB-231 and MDA-MB-435 show markedly elevated AFAP1 expression [dorfleutner-2007-breast-cancer-abstract]. This expression pattern suggests that AFAP1 may be particularly important for the invasive phenotype rather than for proliferation per se.

AFAP1 is also expressed in ocular tissues including the retina, optic nerve, trabecular meshwork, and retinal ganglion cells [gharahkhani-2014-glaucoma-gwas-abstract]. This expression pattern has become significant in light of genome-wide association studies linking AFAP1 variants to glaucoma risk (discussed below).

## Cellular Localization

AFAP1 displays a characteristic localization pattern that reflects its association with actin structures and its regulation by signaling pathways. In quiescent, untransformed cells, AFAP1 colocalizes with actin stress fibers and the cortical actin network along the cell membrane [flynn-1993-afap110-identification-abstract]. This localization depends on the carboxy-terminal actin-binding domain and positions AFAP1 to respond to signals that regulate the actin cytoskeleton.

Upon activation of PKC or transformation by Src, AFAP1 redistributes from stress fibers to specialized actin-rich adhesion structures called podosomes [gatesman-2004-pkc-src-podosome-abstract]. Podosomes are highly dynamic structures consisting of an F-actin-rich core surrounded by a ring of focal adhesion components. They are found on the ventral membrane of cells and are involved in cell adhesion and extracellular matrix degradation. AFAP1 consistently colocalizes with podosomes and has been established as a reliable molecular marker for these structures, along with cortactin and Tks5 [dorfleutner-2008-podosome-lifespan].

In cancer cells, AFAP1 also localizes to invadopodia, which are related structures that mediate invasive behavior. AFAP1 is recruited to invadopodia along with other components including Arp2/3, cortactin, and Tks5. The phosphorylation status of AFAP1 affects the dynamics of both podosomes and invadopodia, with serine phosphorylation promoting structure turnover [dorfleutner-2007-breast-cancer-abstract].

AFAP1 is also found at focal adhesions, which are larger, more stable adhesion structures that connect the actin cytoskeleton to the extracellular matrix. Studies in prostate cancer cells and breast cancer cells have demonstrated that AFAP1 is required for proper focal adhesion formation and function, with knockdown of AFAP1 resulting in disrupted focal contacts and decreased cell adhesion [zhang-2007-prostate-cancer-abstract; dorfleutner-2007-breast-cancer-abstract].

## Role in Cell Adhesion and Migration

AFAP1 plays an essential role in cell adhesion and migration through its effects on the actin cytoskeleton and focal adhesion structures. Studies in MDA-MB-231 breast cancer cells demonstrated that knockdown of AFAP1 expression resulted in loss of actin stress fiber crosslinking and decreased adhesion to fibronectin [dorfleutner-2007-breast-cancer-abstract]. Although AFAP1 knockdown did not affect cell proliferation, it prevented the formation of focal contacts even when cells were treated with lysophosphatidic acid (LPA), a known stimulator of stress fiber formation and adhesion. This suggests that AFAP1 provides cytoskeletal tension through stress fiber crosslinking that is required for focal adhesion assembly.

The role of AFAP1 in cell migration was established through wound healing assays using mouse embryo fibroblasts [walker-2007-pi3k-csrc-abstract]. Cells expressing dominant-negative AFAP1 or lacking c-Src showed significantly reduced migration rates. Similarly, cells lacking the p85 regulatory subunits of PI3K showed migration defects, establishing that the PI3K-AFAP1-cSrc signaling axis is required for efficient cell migration.

In prostate cancer cells, AFAP1 knockdown reduced cell migration and invasion while disrupting focal adhesion organization [zhang-2007-prostate-cancer-abstract]. The effects were dependent on the PKC-binding capacity of AFAP1, as re-expression of wild-type AFAP1 but not a PKC-binding-deficient mutant restored normal phenotypes.

## Role in Blood-Brain Barrier Function

A novel function for AFAP1 was identified in the regulation of P-glycoprotein (P-gp) activity at the blood-brain barrier [hoshi-2017-pgp-bbb-abstract]. P-glycoprotein is a critical efflux transporter that protects the brain from potentially harmful substances and affects drug delivery to the central nervous system. Using phosphoproteomic analysis in human brain capillary endothelial cells, researchers discovered that inflammatory mediators such as TNF-alpha rapidly attenuate P-gp efflux activity without changing P-gp protein expression levels. AFAP1 was identified as a key mediator of this inflammatory signaling pathway. Knockdown of AFAP1 expression blocked the TNF-alpha-induced reduction in P-gp efflux activity, establishing AFAP1 as essential for this regulatory mechanism. This finding suggests that AFAP1 plays a role in the dynamic regulation of blood-brain barrier function during inflammation, potentially through its effects on cytoskeletal organization and membrane protein function in brain endothelial cells.

## Physiological Function: Lactation

A major physiological function of AFAP1 was revealed through the generation of AFAP1 knockout mice [cunnick-2015-mammary-gland-abstract]. These mice displayed a striking lactation defect resulting in inability to efficiently nurse their pups. Histological analysis of mammary glands from lactating AFAP1-null mice revealed accumulation of large cytoplasmic lipid droplets in alveolar epithelial cells, along with reduced lipid synthesis and expression of lipogenic genes. Importantly, protein secretion (as assessed by beta-casein production) was not affected, indicating a specific defect in lipid secretion rather than a general secretory failure.

The lactation defect in AFAP1-null mice was associated with reduced c-Src activity during early lactation and selective loss of active c-Src localization at the apical surface of luminal epithelial cells. AFAP1 was found to respond to prolactin, a key lactogenic hormone, by forming a complex with c-Src and becoming tyrosine phosphorylated. These findings established that AFAP1 is required for the spatial and temporal regulation of c-Src activity in the normal mammary gland, specifically for milk production [cunnick-2015-mammary-gland-abstract].

## Role in Cancer

AFAP1 has been implicated in cancer progression, particularly in prostate cancer. Immunohistochemical analysis of human tissue arrays revealed that AFAP1 is absent or expressed at very low levels in normal prostatic epithelium and benign prostatic hyperplasia, but is significantly overexpressed in prostate carcinomas [zhang-2007-prostate-cancer-abstract]. The level of AFAP1 expression correlated with Gleason scores, indicating association with disease aggressiveness.

Functional studies demonstrated that knockdown of AFAP1 in prostate cancer cell lines inhibited cell proliferation, tumor growth in xenograft models, cell adhesion, and migration. Re-expression of wild-type AFAP1 rescued these phenotypes, but a mutant lacking PKC-binding capacity did not, indicating that the tumorigenic effects of AFAP1 depend on its interaction with PKC and downstream signaling [zhang-2007-prostate-cancer-abstract].

Similarly, AFAP1 is overexpressed in breast cancer cell lines MDA-MB-231 and MDA-MB-435, where it contributes to stress fiber formation and adhesion [dorfleutner-2007-breast-cancer-abstract]. The capacity of AFAP1 to activate c-Src and promote podosome/invadopodia formation suggests a role in cancer cell invasion.

A significant finding in the cancer biology of AFAP1 was the identification of a naturally occurring polymorphic variant that enhances c-Src activation [clump-2010-polymorphic-variant-abstract]. Analysis of the AFAP1 coding sequence revealed a nonsynonymous single-nucleotide polymorphism resulting in a serine-to-cysteine substitution at position 403 (S403C). This variant, designated AFAP1(403C), is present in approximately one-quarter of the general population. Importantly, in cells with elevated c-Src expression, AFAP1(403C) directs c-Src activation and podosome formation independently of upstream signals, in contrast to wild-type AFAP1 which requires PKC activation. In an analysis of ovarian cancer samples, AFAP1 and c-Src were found to be overexpressed in 30 and 32 of 33 samples, respectively. These findings suggest that individuals carrying the 403C polymorphism may be at increased risk for cancer progression when c-Src is overexpressed, providing a mechanism by which inherited genetic variation could influence cancer biology.

## Genetic Association with Glaucoma

A surprising connection between AFAP1 and eye disease emerged from genome-wide association studies (GWAS) of primary open-angle glaucoma (POAG), the most common form of glaucoma and a leading cause of irreversible blindness worldwide. In a landmark study published in Nature Genetics, Gharahkhani and colleagues performed a GWAS in an Australian discovery cohort of 1,155 POAG cases and 1,992 controls, with replication in additional Australian and US cohorts [gharahkhani-2014-glaucoma-gwas-abstract]. Meta-analysis identified a common variant within the AFAP1 gene (rs4619890[G]) that conferred significantly increased risk of POAG (odds ratio = 1.20, P = 7.0 × 10^-10).

The mechanistic connection between AFAP1 and glaucoma pathophysiology remains to be fully elucidated. AFAP1 is expressed in key ocular tissues including the trabecular meshwork (which regulates aqueous humor outflow and thus intraocular pressure), the optic nerve, retina, and retinal ganglion cells (whose death underlies vision loss in glaucoma). The extracellular matrix remodeling functions suggested for AFAP1, potentially through its regulation of cytoskeletal dynamics and cell-matrix adhesions, may be relevant to trabecular meshwork function. Subsequent GWAS meta-analyses have confirmed the association of AFAP1 variants with both POAG and elevated intraocular pressure across diverse ancestral populations, establishing AFAP1 as one of the most robust genetic risk factors for this disease. Fine-mapping studies incorporating data from multiple ancestries have improved the localization of the likely causal variant at this locus.

## AFAP1-AS1: An Antisense Long Non-coding RNA

An antisense long non-coding RNA (lncRNA), designated AFAP1-AS1, is transcribed from the AFAP1 locus in the opposite direction. AFAP1-AS1 has emerged as a topic of considerable research interest in cancer biology, independent of AFAP1 protein function. This lncRNA is overexpressed in multiple cancer types including gastric cancer, breast cancer, lung cancer, and others, and its elevated expression generally correlates with poor prognosis. AFAP1-AS1 functions through multiple mechanisms including sequestration of microRNAs (acting as a "sponge") and direct effects on signaling pathways involved in cancer progression. While AFAP1-AS1 can influence AFAP1 protein expression in some contexts, it also has AFAP1-independent functions. The existence of this cancer-associated lncRNA at the AFAP1 locus adds another layer of complexity to understanding the biology of this genomic region, though the functional relationship between AFAP1-AS1 and AFAP1 protein remains an area of active investigation.

## The AFAP Protein Family

AFAP1 is the founding member of a three-protein family that also includes AFAP1L1 and AFAP1L2/XB130. All three proteins share a similar modular domain structure with two PH domains flanking a serine/threonine-rich region, SH2-binding motifs, and SH3-binding motifs. Cladistic analysis indicates that AFAP1 and AFAP1L1 are more closely related to each other than to AFAP1L2/XB130.

A major structural difference between the family members lies in the carboxy terminus. AFAP1 and AFAP1L1 contain a leucine zipper and actin-binding domain, enabling direct F-actin binding and crosslinking. In contrast, AFAP1L2/XB130 contains a related coiled-coil but lacks an actin-binding motif and does not bind efficiently to actin filaments. Consequently, AFAP1L2/XB130 appears to have distinct functions, acting as an intermediary between the RET/PTC kinase and PI3K pathway in the thyroid rather than primarily regulating actin dynamics.

AFAP1L1 shares many functional properties with AFAP1, including the ability to associate with actin filaments, localize to invadosomes, and induce podosomes upon overexpression. However, the tissue distribution patterns differ, with AFAP1L1 showing unique localization to muscle tissue and the dentate nucleus of the brain where AFAP1 is not detectable.

## Open Questions

Despite the substantial body of research on AFAP1, several important questions remain unresolved:

1. **Structural basis of function:** No experimentally determined high-resolution crystal or cryo-EM structure of AFAP1 or its domains is currently available. However, an AlphaFold-predicted structure is available through the AlphaFold Protein Structure Database (entry Q8N556), which may provide insights into domain organization and the auto-inhibitory mechanism. Experimental validation of the predicted structure and its conformational dynamics would greatly enhance understanding of AFAP1 function.

2. **Regulation of multimerization:** While it is clear that AFAP1 exists in multiple oligomeric states and that transitions between these states are regulated, the precise structural changes and the upstream signals that control them remain incompletely defined.

3. **Tissue-specific functions:** The lactation defect in AFAP1 knockout mice suggests tissue-specific functions, but the roles of AFAP1 in other tissues have not been systematically investigated.

4. **Relationship to metastasis:** Although AFAP1 is overexpressed in prostate and breast cancers and contributes to migration and invasion, its precise contribution to metastatic dissemination in vivo remains to be determined.

5. **Therapeutic targeting:** Given its overexpression in certain cancers and its role in promoting tumorigenic phenotypes, AFAP1 might represent a therapeutic target, but no small-molecule inhibitors or other targeting strategies have been developed.

6. **Coordination with other actin-binding proteins:** How AFAP1 coordinates with other actin-binding and crosslinking proteins in cells to produce coherent cytoskeletal responses to signals is not well understood.

7. **Non-canonical functions:** Whether AFAP1 has signaling functions independent of its actin-binding and Src-activation roles remains an open question.

8. **Mechanism of glaucoma association:** The GWAS association between AFAP1 variants and primary open-angle glaucoma is robust, but the mechanistic basis for this association remains unknown. Does AFAP1 play a direct role in trabecular meshwork function, retinal ganglion cell survival, or optic nerve health? Is the risk variant a gain- or loss-of-function allele?

9. **Functional consequences of the S403C polymorphism:** The polymorphic variant AFAP1(403C) appears to constitutively activate c-Src, but the structural basis for this gain-of-function, and whether it contributes to cancer risk in the general population, requires further investigation.

10. **Role in neuronal function:** AFAP1 is expressed in neuronal tissues but its specific functions in neurons have not been characterized. Given the involvement of cytoskeletal dynamics in neuronal processes such as axon guidance and synaptic plasticity, AFAP1 may have important neurological functions.

## References

- [flynn-1993-afap110-identification-abstract] Flynn DC, Leu TH, Reynolds AB, Parsons JT. Identification and sequence analysis of cDNAs encoding a 110-kilodalton actin filament-associated pp60src substrate. Mol Cell Biol. 1993;13(12):7892-7900. PMID: 8247004. DOI: 10.1128/mcb.13.12.7892-7900.1993

- [baisden-2001-afap110-review-abstract] Baisden JM, Qian Y, Zot HM, Flynn DC. The actin filament-associated protein AFAP-110 is an adaptor protein that modulates changes in actin filament integrity. Oncogene. 2001;20(44):6435-6447. PMID: 11607843. DOI: 10.1038/sj.onc.1204784

- [qian-2002-pkc-crosslinking-abstract] Qian Y, Baisden JM, Cherezova L, Summy JM, Guappone-Koay A, Shi X, Mast T, Pustula J, Zot HG, Mazloum N, Lee MY, Flynn DC. PKC phosphorylation increases the ability of AFAP-110 to cross-link actin filaments. Mol Biol Cell. 2002;13(7):2311-2322. PMID: 12134071. DOI: 10.1091/mbc.e01-12-0148

- [qian-2000-carboxy-terminus-abstract] Qian Y, Baisden JM, Zot HG, Van Winkle WB, Flynn DC. The carboxy terminus of AFAP-110 modulates direct interactions with actin filaments and regulates its ability to alter actin filament integrity and induce lamellipodia formation. Exp Cell Res. 2000;255(1):102-113. PMID: 10666339. DOI: 10.1006/excr.1999.4795

- [qian-1998-src-self-association-abstract] Qian Y, Baisden JM, Westin EH, Guappone AC, Koay TC, Flynn DC. Src can regulate carboxy terminal interactions with AFAP-110, which influence self-association, cell localization and actin filament integrity. Oncogene. 1998;16(17):2185-2195. PMID: 9619827. DOI: 10.1038/sj.onc.1201753

- [qian-2004-leucine-zipper-abstract] Qian Y, Gatesman AS, Baisden JM, Zot HG, Cherezova L, Qazi I, Mazloum N, Lee MY, Guappone-Koay A, Flynn DC. Analysis of the role of the leucine zipper motif in regulating the ability of AFAP-110 to alter actin filament integrity. J Cell Biochem. 2004;91(3):602-620. PMID: 14755689. DOI: 10.1002/jcb.10725

- [gatesman-2004-pkc-src-podosome-abstract] Gatesman A, Walker VG, Baisden JM, Weed SA, Flynn DC. Protein kinase Calpha activates c-Src and induces podosome formation via AFAP-110. Mol Cell Biol. 2004;24(17):7578-7597. PMID: 15314167. DOI: 10.1128/MCB.24.17.7578-7597.2004

- [walker-2007-pi3k-csrc-abstract] Walker VG, Ammer A, Cao Z, Clump AC, Jiang BH, Kelley LC, Weed SA, Zot H, Flynn DC. PI3K activation is required for PMA-directed activation of cSrc by AFAP-110. Am J Physiol Cell Physiol. 2007;293(1):C119-132. PMID: 17360811. DOI: 10.1152/ajpcell.00525.2006

- [zhang-2007-prostate-cancer-abstract] Zhang J, Park SI, Artime MC, Summy JM, Shah AN, Bomser JA, Dorfleutner A, Flynn DC, Gallick GE. AFAP-110 is overexpressed in prostate cancer and contributes to tumorigenic growth by regulating focal contacts. J Clin Invest. 2007;117(10):2962-2973. PMID: 17885682. DOI: 10.1172/JCI30710

- [dorfleutner-2007-breast-cancer-abstract] Dorfleutner A, Stehlik C, Zhang J, Gallick GE, Flynn DC. AFAP-110 is required for actin stress fiber formation and cell adhesion in MDA-MB-231 breast cancer cells. J Cell Physiol. 2007;213(3):740-749. PMID: 17520695. DOI: 10.1002/jcp.21143

- [cunnick-2015-mammary-gland-abstract] Cunnick JM, Kim S, Hadsell J, Collins S, Cerra C, Reiser P, Flynn DC, Cho Y. Actin filament-associated protein 1 is required for cSrc activity and secretory activation in the lactating mammary gland. Oncogene. 2015;34(20):2640-2649. PMID: 25043309. DOI: 10.1038/onc.2014.205

- [baisden-2001-intrinsic-ability-abstract] Baisden JM, Gatesman AS, Cherezova L, Jiang BH, Flynn DC. The intrinsic ability of AFAP-110 to alter actin filament integrity is linked with its ability to also activate cellular tyrosine kinases. Oncogene. 2001;20(45):6607-6616. PMID: 11641786. DOI: 10.1038/sj.onc.1204802

- [clump-2010-polymorphic-variant-abstract] Clump DA, Yu JJ, Cho Y, Gao R, Jett J, Zot H, Cunnick JM, Snyder B, Clump AC, Dodrill M, Gannett P, Coad JE, Shurina R, Figg WD, Reed E, Flynn DC. A polymorphic variant of AFAP-110 enhances cSrc activity. Transl Oncol. 2010;3(4):276-285. PMID: 20689769. DOI: 10.1593/tlo.10106

- [gharahkhani-2014-glaucoma-gwas-abstract] Gharahkhani P, Burdon KP, Fogarty R, Sharma S, Hewitt AW, Martin S, Law MH, Cremin K, Bailey JNC, Loomis SJ, et al. Common variants near ABCA1, AFAP1 and GMDS confer risk of primary open-angle glaucoma. Nat Genet. 2014;46:1120-1125. PMID: 25173106. DOI: 10.1038/ng.3079

- [dorfleutner-2008-podosome-lifespan-abstract] Dorfleutner A, Cho Y, Vincent D, Cunnick J, Lin H, Weed SA, Stehlik C, Flynn DC. Phosphorylation of AFAP-110 affects podosome lifespan in A7r5 cells. J Cell Sci. 2008;121(14):2394-2405. PMID: 18577569. DOI: 10.1242/jcs.024943

- [hoshi-2017-pgp-bbb-abstract] Hoshi Y, Uchida Y, Tachikawa M, Ohtsuki S, Terasaki T. Actin filament-associated protein 1 (AFAP-1) is a key mediator in inflammatory signaling-induced rapid attenuation of intrinsic P-gp function in human brain capillary endothelial cells. J Neurochem. 2017;141(2):247-262. PMID: 28112407. DOI: 10.1111/jnc.13960


## Citations

1. baisden-2001-afap110-review-abstract.md
2. baisden-2001-intrinsic-ability-abstract.md
3. clump-2010-polymorphic-variant-abstract.md
4. cunnick-2015-mammary-gland-abstract.md
5. dorfleutner-2007-breast-cancer-abstract.md
6. dorfleutner-2008-podosome-lifespan-abstract.md
7. flynn-1993-afap110-identification-abstract.md
8. gatesman-2004-pkc-src-podosome-abstract.md
9. gharahkhani-2014-glaucoma-gwas-abstract.md
10. hoshi-2017-pgp-bbb-abstract.md
11. qian-1998-src-self-association-abstract.md
12. qian-2000-carboxy-terminus-abstract.md
13. qian-2002-pkc-crosslinking-abstract.md
14. qian-2004-leucine-zipper-abstract.md
15. walker-2007-pi3k-csrc-abstract.md
16. zhang-2007-prostate-cancer-abstract.md