---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T19:39:12.527267'
end_time: '2026-01-23T19:55:58.953158'
duration_seconds: 1006.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RASAL1
  gene_symbol: RASAL1
  uniprot_accession: O95294
  protein_description: 'RecName: Full=RasGAP-activating-like protein 1 {ECO:0000305};
    AltName: Full=RAS protein activator like 1 {ECO:0000312|HGNC:HGNC:9873}; AltName:
    Full=Ras GTPase-activating-like protein {ECO:0000303|PubMed:9751798};'
  gene_info: Name=RASAL1 {ECO:0000312|HGNC:HGNC:9873}; Synonyms=RASAL {ECO:0000303|PubMed:9751798};
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf.
    (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O95294
- **Protein Description:** RecName: Full=RasGAP-activating-like protein 1 {ECO:0000305}; AltName: Full=RAS protein activator like 1 {ECO:0000312|HGNC:HGNC:9873}; AltName: Full=Ras GTPase-activating-like protein {ECO:0000303|PubMed:9751798};
- **Gene Information:** Name=RASAL1 {ECO:0000312|HGNC:HGNC:9873}; Synonyms=RASAL {ECO:0000303|PubMed:9751798};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASAL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASAL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASAL1** (gene ID: RASAL1, UniProt: O95294) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASAL1: A Calcium-Regulated RasGAP with Dual Specificity and Tumor Suppressor Function

## Introduction

RASAL1 (RAS Protein Activator Like 1, UniProt O95294) is a member of the GAP1 subfamily of GTPase-activating proteins (GAPs) that functions as a negative regulator of Ras signaling. Originally cloned from human frontal cortex cDNA by Allen and colleagues in 1998, RASAL1 encodes an 804-amino acid protein with a distinctive modular architecture consisting of two N-terminal C2 domains, a central catalytic RasGAP domain, and a C-terminal pleckstrin homology (PH) domain [allen-1998-rasal-cloning-abstract]. The protein exhibits a remarkably restricted tissue expression pattern compared to other RasGAPs, being highly expressed in thyroid follicular cells, adrenal medulla, and at lower levels in the brain [allen-1998-rasal-cloning-abstract]. This tissue specificity distinguishes RASAL1 from other GAP1 family members, which show more widespread expression patterns.

RASAL1 functions as a tumor suppressor by enhancing the intrinsic GTPase activity of wild-type Ras proteins, thereby converting Ras from its active GTP-bound state to its inactive GDP-bound state. This regulation is essential for controlling cellular proliferation and differentiation downstream of receptor tyrosine kinase signaling. Importantly, RASAL1 exhibits dual specificity, capable of inactivating both Ras and the related GTPase Rap, although the mechanisms and regulation of these two activities differ substantially [sot-2013-rasal-membrane-abstract]. Loss of RASAL1 function through epigenetic silencing or mutation has been implicated in multiple cancer types and in fibrotic diseases, establishing it as an important regulator of cellular homeostasis.

## Domain Architecture and Structure

RASAL1 possesses a characteristic domain organization shared with other members of the GAP1 subfamily, which includes GAP1m/RASA2, GAPIP4BP/RASA3, and CAPRI/RASA4 [simanshu-2019-rasgap-review-abstract]. The approximately 95 kDa protein contains four distinct functional domains arranged in the order C2A-C2B-GAP-PH from N-terminus to C-terminus.

The two tandem C2 domains at the N-terminus share structural similarity with the calcium-dependent phospholipid-binding domains found in synaptotagmin and protein kinase C [allen-1998-rasal-cloning-abstract]. These domains are critical for RASAL1's calcium-regulated membrane translocation and possess distinct lipid-binding specificities. Detailed biochemical analysis by Sot and colleagues demonstrated that the C2A domain binds specifically to phosphatidylserine (PS), while the C2B domain interacts with several phosphoinositide lipids [sot-2013-rasal-membrane-abstract]. This dual lipid recognition enables precise membrane targeting in response to calcium signals.

The central GAP-related domain (GRD) contains the catalytic machinery necessary for stimulating GTP hydrolysis on Ras family members. This domain contributes the critical arginine finger that is essential for RasGAP catalysis [sondermann-2010-dual-gap-mechanism-abstract]. The C-terminal PH domain provides additional membrane-targeting capability and has been shown to interact with calcium-sensing proteins including CaMKII-α and protein kinase C [deurloo-2024-rasal1-neuronal-abstract].

Electron microscopy studies have begun to reveal the relative organization of these individual domains, though high-resolution structural information remains limited [simanshu-2019-rasgap-review-abstract]. The interdomain interactions appear to be critical for regulating RASAL1's catalytic activity, as the protein exists in an autoinhibited state in solution that is relieved upon membrane binding.

## Molecular Function and Catalytic Mechanism

The primary molecular function of RASAL1 is to accelerate the hydrolysis of GTP bound to Ras family GTPases, converting them from the active signaling state to the inactive GDP-bound form. A remarkable and distinguishing feature of RASAL1 is its dual specificity for both Ras and Rap GTPases, combined with the unusual property that isolated soluble RASAL1 protein exhibits RapGAP activity but lacks RasGAP activity [sot-2013-rasal-membrane-abstract].

The activation of RASAL1's RasGAP function requires both colocalization with membrane-bound Ras and calcium-dependent binding of the C2 domains to membrane phospholipids [sot-2013-rasal-membrane-abstract]. This spatial and conformational regulation ensures that RASAL1 only inactivates Ras when both proteins are appropriately positioned at the plasma membrane. In contrast, the RapGAP activity of RASAL1 does not require membrane association and can be observed with the soluble protein in vitro. The molecular basis for this regulatory switch involves conformational changes in the GAP domain that are triggered by C2 domain-lipid interactions, though the precise structural mechanism remains to be elucidated.

The catalytic mechanism for GTP hydrolysis on Ras involves the conserved "arginine finger" mechanism characteristic of RasGAPs. The GAP provides an arginine residue that inserts into the active site and helps orient the catalytic glutamine (Gln61) of Ras, which in turn positions a water molecule for nucleophilic attack on the gamma-phosphate of GTP [sondermann-2010-dual-gap-mechanism-abstract]. For Rap substrates, which lack the equivalent of Gln61 (possessing instead a non-catalytic threonine at that position), the mechanism differs. Dual-specificity GAPs like RASAL1 use their extra-GAP domains (C2 and PH) to promote a different orientation of Rap's switch-II region, allowing Rap Gln63 to serve as the catalytic residue [sondermann-2010-dual-gap-mechanism-abstract]. Deletion of the C2 domains dramatically reduces RapGAP activity by more than 1000-fold while having minimal impact on RasGAP activity, demonstrating the essential role of these domains in dual specificity.

## Calcium-Dependent Regulation and Membrane Translocation

A defining characteristic of RASAL1 is its regulation by intracellular calcium oscillations. The C2 domains function as calcium sensors that enable RASAL1 to shuttle dynamically between the cytoplasm and the plasma membrane in response to changes in intracellular calcium concentration [simanshu-2019-rasgap-review-abstract]. This behavior differs from the related protein CAPRI, which associates stably with membranes upon calcium elevation; RASAL1 instead senses calcium oscillations and continuously shuttles between compartments.

Live cell imaging studies have demonstrated that elevation of intracellular calcium induces rapid plasma membrane association of RASAL1. In neurons, perfusion with depolarizing solution induced plasma membrane translocation that began within 2 seconds and was complete within 8 seconds [deurloo-2024-rasal1-neuronal-abstract]. This translocation is reversible, with RASAL1 returning to the cytoplasm as calcium levels decline. The calcium dependence is mediated entirely through the C2 domains rather than through direct effects on the catalytic domain; addition of calcium in the absence of membranes has no effect on RasGAP activity, confirming that membrane colocalization is the critical activating event [sot-2013-rasal-membrane-abstract].

The functional consequence of this calcium regulation is that RASAL1 acts as a decoder of calcium signaling, translating patterns of calcium oscillations into modulation of Ras activity [jin-2007-rasal-methylation-abstract]. This provides a mechanism for integrating calcium-dependent signaling pathways with the Ras-MAPK cascade, allowing cells to coordinate diverse extracellular signals that elevate intracellular calcium with growth factor signaling through receptor tyrosine kinases.

## Subcellular Localization

Under basal conditions with low intracellular calcium, RASAL1 exhibits a diffuse cytoplasmic distribution throughout the cell body. In neurons, this includes expression in soma, dendrites, and axons [deurloo-2024-rasal1-neuronal-abstract]. Upon calcium elevation, RASAL1 rapidly translocates to the plasma membrane where it colocalizes with its Ras substrates. This membrane localization is essential for its RasGAP function, as the colocalization of RASAL1 and Ras at the membrane is required for catalytic activity.

The PH domain at the C-terminus may provide additional membrane-targeting capability through interactions with phosphoinositides, potentially stabilizing membrane association or directing RASAL1 to specific membrane microdomains. However, the C2 domains appear to be the primary determinants of calcium-regulated localization.

## Signaling Pathways and Downstream Effects

RASAL1 functions as a negative regulator of the Ras signaling cascade, and its activity impacts two major downstream pathways: the MAPK pathway (RAF→MEK→ERK) and the PI3K pathway (PI3K→AKT→mTOR). Functional studies in thyroid cancer cells demonstrated that wild-type RASAL1 expression reduces levels of both phosphorylated ERK and phosphorylated AKT, indicating suppression of both pathways [liu-2013-rasal1-thyroid-abstract]. Cancer-associated mutations in RASAL1 that impair RasGAP function lost the ability to suppress these pathways, confirming that the tumor suppressor activity of RASAL1 is mediated through Ras inactivation.

Beyond classical Ras signaling, RASAL1 has been shown to have additional signaling functions in specific cellular contexts. In T lymphocytes, RASAL1 associates with the tyrosine kinase ZAP-70, a critical component of T-cell receptor (TCR) signaling [thaker-2019-rasal1-zap70-abstract]. This interaction involves binding of RASAL1 to the kinase domain of ZAP-70, resulting in inhibition of ZAP-70 kinase activity. Thus, RASAL1 inhibits T-cell activation through two parallel mechanisms: direct inhibition of ZAP-70 and GAP-mediated inhibition of the p21ras-ERK pathway downstream of the TCR.

In neurons, RASAL1 participates in a calcium-decoding complex that includes CaMKII-α and protein kinase C (PKC), both of which are calcium-sensing proteins [deurloo-2024-rasal1-neuronal-abstract]. Additionally, RASAL1 interacts with α- and β-tubulin, suggesting roles in regulating the cytoskeleton. Functional studies showed that RASAL1 promotes tubulin detyrosination, a post-translational modification that stabilizes microtubules. This activity inhibits dendritic outgrowth while promoting synapse formation and NMDA receptor-mediated synaptic transmission, illustrating how RASAL1 coordinates multiple aspects of neuronal maturation [deurloo-2024-rasal1-neuronal-abstract].

## Tissue Expression and Physiological Roles

RASAL1 exhibits a remarkably restricted tissue expression pattern. The highest expression levels are found in thyroid follicular cells and the adrenal medulla, with lower expression in brain, spinal cord, and trachea [allen-1998-rasal-cloning-abstract]. This endocrine-enriched expression pattern distinguishes RASAL1 from other GAP1 family members and suggests specialized physiological functions in these tissues.

In the thyroid, RASAL1 appears to be a critical regulator of cell proliferation. The Ras-cyclic AMP pathway is particularly important in thyroid physiology, and RASAL1 acts as an inhibitory regulator of this pathway [allen-1998-rasal-cloning-abstract]. Loss of RASAL1 function through methylation or mutation is strongly associated with thyroid cancer development, consistent with its role as a major tumor suppressor in this tissue [liu-2013-rasal1-thyroid-abstract].

In the nervous system, despite high expression levels in brain, the physiological functions of RASAL1 have only recently begun to be characterized. RASAL1 appears to regulate calcium-dependent neuronal maturation, balancing neurite outgrowth against synapse formation [deurloo-2024-rasal1-neuronal-abstract]. This suggests roles in neural development and potentially in synaptic plasticity.

## Role in Cancer

RASAL1 has been established as an important tumor suppressor, with its inactivation contributing to cancer development through loss of Ras pathway regulation. The mechanisms of RASAL1 inactivation in cancer include both epigenetic silencing through promoter hypermethylation and genetic inactivation through missense or nonsense mutations.

Epigenetic silencing of RASAL1 was first systematically characterized by Jin and colleagues, who demonstrated that RASAL1 is silenced through CpG methylation in multiple tumor types including hepatocellular carcinoma, esophageal carcinoma, breast carcinoma, nasopharyngeal carcinoma, and lymphoma [jin-2007-rasal-methylation-abstract]. Importantly, RASAL1 methylation was observed in tumor tissues but not in corresponding normal tissues, and treatment with the demethylating agent 5-aza-2'-deoxycytidine restored RASAL1 expression. Ectopic expression of RASAL1 in cancer cells inhibited tumor cell growth, confirming its tumor suppressor function.

In thyroid cancer, Liu and colleagues performed a comprehensive analysis that established RASAL1 as a major tumor suppressor [liu-2013-rasal1-thyroid-abstract]. Among 13 negative modulators of the RAS pathway screened, RASAL1 was most frequently hypermethylated. Additionally, RASAL1 mutations were found in 8 of 101 thyroid tumors examined, including one nonsense mutation (W594X) and seven missense mutations, all located within the RasGAP domain. The mutation frequency was highest in anaplastic thyroid cancer (16.67%) and follicular thyroid cancer (4.88%). Functional studies showed that cancer-associated mutations impaired RASAL1's ability to suppress MAPK and PI3K signaling and to inhibit tumor growth in xenograft models. Notably, RASAL1 inactivation was found primarily in tumors lacking classical RAS pathway mutations, suggesting it represents an alternative genetic mechanism for Ras pathway activation.

In colorectal cancer, decreased RASAL1 expression was associated with tumor progression [ohta-2009-rasal1-colorectal-abstract]. RASAL1 expression was reduced in most colorectal cancers with wild-type KRAS but rarely in those with mutant KRAS, demonstrating mutual exclusivity consistent with their shared pathway. RASAL1 was detected in approximately 47% of adenocarcinomas but absent in small adenomas, suggesting its loss occurs during the progression from benign to malignant lesions.

In gastric cancer, RASAL1 promoter hypermethylation is particularly frequent, occurring in 70% of gastric cancer tissues compared to 30% in paired adjacent non-cancerous tissues [chen-2013-rasal1-gastric-methylation-abstract]. Significant correlations were found between RASAL1 promoter methylation and clinicopathological features including tumor differentiation, tumor size, invasive depth, and lymph node metastasis. RASAL1 expression was found to be lowest in poorly differentiated gastric cancer cell lines, consistent with a tumor suppressor role [chen-2014-rasal1-gastric-abstract]. Functional studies demonstrated that RASAL1 knockdown increased RAS-GTP and phosphorylated ERK1/2 levels, promoting gastric cancer cell proliferation, invasion, and migration while reducing apoptosis. Conversely, RASAL1 overexpression inhibited these cancer cell behaviors. Treatment with the demethylating agent 5-Aza-CdR restored RASAL1 protein expression and decreased RAS/ERK pathway activation, confirming that epigenetic mechanisms regulate RASAL1 expression in gastric cancer [chen-2013-rasal1-gastric-methylation-abstract].

## Role in Fibrosis

Beyond cancer, RASAL1 hypermethylation has been implicated in fibrotic diseases, particularly kidney fibrosis. Bechtel and colleagues demonstrated that RASAL1 hypermethylation is associated with the perpetuation of fibroblast activation and fibrogenesis in the kidney [bechtel-2010-rasal1-kidney-fibrosis-abstract]. The profibrotic cytokine TGF-β1 induces RASAL1 silencing through a mechanism involving the DNA methyltransferase Dnmt1. Treatment with TGF-β1 caused decreased Rasal1 mRNA expression within 8 hours, and Dnmt1 knockdown prevented this hypermethylation.

The epigenetic silencing of RASAL1 provides a mechanism for the perpetuation of fibroblast activation. Once methylated, the RASAL1 promoter remains silenced even after the initial fibrogenic stimulus is removed, and this methylation pattern can be inherited by daughter cells. This explains how transient exposure to profibrotic signals can lead to persistent myofibroblast activation. Importantly, kidney fibrosis was ameliorated in Dnmt1+/- heterozygous mice, and RASAL1 hypermethylation could be reversed by treatment with BMP-7, an endogenous TGF-β antagonist [bechtel-2010-rasal1-kidney-fibrosis-abstract]. These findings identify RASAL1 epigenetic regulation as a potential therapeutic target in fibrotic disease.

RASAL1 also plays an important role in liver fibrosis through regulation of hepatic stellate cell (HSC) activation. HSCs are the primary cell type responsible for liver fibrosis, and RASAL1 expression levels are inversely correlated with HSC activation [qiu-2017-rasal1-liver-fibrosis-abstract]. RASAL1 suppresses HSC activity through two distinct pathways: the Ras-MAPK pathway, which inhibits cell proliferation by reducing Ras-GTP activity, and an AGTR1-PKA-AMPK-SRF pathway involving interaction with angiotensin II receptor type 1 that suppresses fibrogenic gene expression including alpha-smooth muscle actin and collagen genes. Studies using RASAL1-deficient mice demonstrated enhanced susceptibility to liver fibrosis following chemical induction with carbon tetrachloride or thioacetamide, despite comparable levels of liver damage [qiu-2017-rasal1-liver-fibrosis-abstract]. These mice showed significantly greater fibrotic scarring than wild-type littermates, although no spontaneous pathological tumors were observed up to 48 weeks of age under normal conditions.

In cardiac fibrosis, RASAL1 methylation has been identified as a key driver of endothelial-to-mesenchymal transition (EndMT), a process contributing to the progression of heart fibrosis [xu-2015-rasal1-cardiac-fibrosis-abstract]. Long-term exposure to TGF-β1 induces aberrant CpG island promoter methylation of RASAL1 in coronary endothelial cells, leading to transcriptional silencing. This silencing increases intrinsic Ras-GTP activity and promotes EndMT. In non-failing human myocardium, increased fibrosis was associated with significantly increased RASAL1 promoter methylation, decreased RASAL1 expression, increased Ras-GTP activity, and increased expression of EndMT markers [xu-2015-rasal1-cardiac-fibrosis-abstract]. Importantly, BMP-7 treatment significantly reduced RASAL1 promoter methylation in mouse models of pressure overload-induced cardiac fibrosis, through a mechanism involving restoration of the demethylating enzyme TET3, which was found to be decreased in fibrotic hearts. This study established that epigenetic balance between methylation and hydroxymethylation at the RASAL1 promoter is a critical determinant of cardiac fibrosis progression.

## Role in T-Cell Regulation and Tumor Immunity

RASAL1 has been identified as a negative regulator of T-cell activation and anti-tumor immunity through its interaction with ZAP-70 [thaker-2019-rasal1-zap70-abstract]. RASAL1 is expressed in activated CD4+ and CD8+ T-cells, where it associates with the kinase domain of ZAP-70, a critical mediator of TCR signaling. This interaction inhibits ZAP-70 kinase activity, providing a mechanism distinct from RASAL1's RasGAP function.

Functional studies demonstrated that RASAL1 inhibits CD4+ T-cell responses to antigenic peptides both in vitro (when presented by dendritic cells) and in vivo. From a therapeutic perspective, siRNA-mediated reduction of RASAL1 expression in T-cells enhanced anti-tumor immunity, resulting in shrinkage of B16 melanoma and EL-4 lymphoma tumors in mouse models [thaker-2019-rasal1-zap70-abstract]. This tumor shrinkage was accompanied by increased infiltration of CD8+ T-cells expressing the effector molecules granzyme B and interferon-γ. These findings identify RASAL1 as a potential immune checkpoint that could be targeted to enhance anti-tumor T-cell responses.

## Open Questions

Several important questions about RASAL1 biology remain to be addressed:

1. **Structural basis for dual specificity and membrane regulation**: While biochemical studies have established that RASAL1 requires membrane binding for RasGAP but not RapGAP activity, the structural mechanism by which membrane association activates RasGAP function remains unclear. High-resolution structural studies of membrane-bound RASAL1 would provide important insights.

2. **Physiological significance of dual Ras/Rap specificity**: It is not known whether the RapGAP activity of RASAL1 is physiologically important or represents a vestigial function. Studies examining Rap-dependent processes in RASAL1-deficient cells could address this question.

3. **Roles in specific tissues**: The restricted expression pattern of RASAL1, particularly its high expression in thyroid and adrenal tissue, suggests tissue-specific functions that are not fully understood. The consequences of RASAL1 loss in adrenal physiology have not been characterized.

4. **Contribution to neural function**: While recent work has begun to characterize RASAL1 in neuronal development, its roles in adult brain function, synaptic plasticity, and neurological disease remain unexplored.

5. **Therapeutic targeting**: Given the tumor suppressor function of RASAL1 and its epigenetic silencing in cancer, strategies to reactivate RASAL1 expression (such as DNMT inhibitors or targeted demethylation approaches) could have therapeutic potential. Similarly, targeting RASAL1 in T-cells could enhance anti-tumor immunity. The therapeutic potential of these approaches requires further investigation.

6. **Integration with calcium signaling**: The physiological contexts in which RASAL1's calcium-responsive shuttling is important, and how this integrates with other calcium-dependent signaling pathways, warrants further study.

## References

* **[allen-1998-rasal-cloning-abstract]**: Allen M, Chu S, Brill S, Stotler C, Buckler A. Restricted tissue expression pattern of a novel human rasGAP-related gene and its murine ortholog. *Gene*. 1998 Sep 18;218(1-2):17-25. PMID: 9751798. DOI: 10.1016/s0378-1119(98)00394-3

* **[sot-2013-rasal-membrane-abstract]**: Sot B, Behrmann E, Raunser S, Wittinghofer A. Ras GTPase activating (RasGAP) activity of the dual specificity GAP protein Rasal requires colocalization and C2 domain binding to lipid membranes. *Proc Natl Acad Sci U S A*. 2013 Jan 2;110(1):111-6. PMID: 23251034. DOI: 10.1073/pnas.1201658110

* **[liu-2013-rasal1-thyroid-abstract]**: Liu D, Yang C, Bojdani E, Murugan AK, Xing M. Identification of RASAL1 as a major tumor suppressor gene in thyroid cancer. *J Natl Cancer Inst*. 2013 Nov 6;105(21):1617-27. PMID: 24136889. PMCID: PMC3818169. DOI: 10.1093/jnci/djt249

* **[jin-2007-rasal-methylation-abstract]**: Jin H, Wang X, Ying J, Wong AH, Cui Y, Srivastava G, Shen ZY, Li EM, Zhang Q, Jin J, Kupzig S, Chan AT, Cullen PJ, Tao Q. Epigenetic silencing of a Ca(2+)-regulated Ras GTPase-activating protein RASAL defines a new mechanism of Ras activation in human cancers. *Proc Natl Acad Sci U S A*. 2007 Jul 24;104(30):12353-8. PMID: 17640920. PMCID: PMC1941473. DOI: 10.1073/pnas.0700153104

* **[thaker-2019-rasal1-zap70-abstract]**: Thaker YR, Raab M, Strebhardt K, Rudd CE. GTPase-activating protein Rasal1 associates with ZAP-70 of the TCR and negatively regulates T-cell tumor immunity. *Nat Commun*. 2019 Oct 22;10(1):4804. PMID: 31641113. PMCID: PMC6805893. DOI: 10.1038/s41467-019-12544-4

* **[bechtel-2010-rasal1-kidney-fibrosis-abstract]**: Bechtel W, McGoohan S, Zeisberg EM, Müller GA, Kalbber H, Salant DJ, Müller CA, Kalluri R, Zeisberg M. Methylation determines fibroblast activation and fibrogenesis in the kidney. *Nat Med*. 2010 May;16(5):544-50. PMID: 20418885. PMCID: PMC3106179. DOI: 10.1038/nm.2135

* **[deurloo-2024-rasal1-neuronal-abstract]**: Deurloo MHS, Eide S, Turlova E, Li Q, Spijker S, Sun H-S, Groffen AJA, Feng Z-P. Rasal1 regulates calcium dependent neuronal maturation by modifying microtubule dynamics. *Cell Biosci*. 2024 Jan 21;14(1):13. PMID: 38246997. PMCID: PMC10800070. DOI: 10.1186/s13578-024-01193-w

* **[ohta-2009-rasal1-colorectal-abstract]**: Ohta M, Seto M, Ijichi H, Miyabayashi K, Kudo Y, Mohri D, Asaoka Y, Tanaka Y, Maeda S, Kawabe T, Omata M, Koike K. Decreased expression of the RAS-GTPase activating protein RASAL1 is associated with colorectal tumor progression. *Gastroenterology*. 2009 Jan;136(1):206-16. PMID: 18992247. DOI: 10.1053/j.gastro.2008.09.063

* **[sondermann-2010-dual-gap-mechanism-abstract]**: Sondermann H. Unravelling the mechanism of dual-specificity GAPs. *EMBO J*. 2010 Apr 7;29(7):1205-6. PMID: 20186121. PMCID: PMC2857463. DOI: 10.1038/emboj.2010.42

* **[simanshu-2019-rasgap-review-abstract]**: Ras-Specific GTPase-Activating Proteins—Structures, Mechanisms, and Interactions. *Cold Spring Harb Perspect Med*. 2019 Mar 1;9(3):a031500. PMCID: PMC6396337. DOI: 10.1101/cshperspect.a031500

* **[chen-2014-rasal1-gastric-abstract]**: Chen H, Cheng ZY, Pan Y, Wang Z, Liu Y, Zhang JQ. RASAL1 influences the proliferation and invasion of gastric cancer cells by regulating the RAS/ERK signaling pathway. *Hum Cell*. 2014 Jul;27(3):103-10. PMID: 24531877. DOI: 10.1007/s13577-014-0090-2

* **[chen-2013-rasal1-gastric-methylation-abstract]**: Chen H, Pan Y, Cheng ZY, Wang Z, Liu Y, Zhao ZJ, Fan H. Hypermethylation and clinicopathological significance of RASAL1 gene in gastric cancer. *Asian Pac J Cancer Prev*. 2013;14(11):6261-5. PMID: 24377515. DOI: 10.7314/apjcp.2013.14.11.6261

* **[qiu-2017-rasal1-liver-fibrosis-abstract]**: Qiu W, Weng J, Lan S, Zheng X, Xu L, Huang Z, Chen L, Li H, Cheng M. RASAL1 is a potent regulator of hepatic stellate cell activity and liver fibrosis. *Oncotarget*. 2017;8(42):73050-73062. DOI: 10.18632/oncotarget.17609

* **[xu-2015-rasal1-cardiac-fibrosis-abstract]**: Xu X, Tan X, Tampe B, Nyamsuren G, Liu X, Maier LS, Sossalla S, Kalluri R, Zeisberg M, Hasenfuss G, Zeisberg EM. Epigenetic balance of aberrant Rasal1 promoter methylation and hydroxymethylation regulates cardiac fibrosis. *Cardiovasc Res*. 2015 Mar 1;105(3):279-91. PMID: 25616414. DOI: 10.1093/cvr/cvv015


## Citations

1. allen-1998-rasal-cloning-abstract.md
2. bechtel-2010-rasal1-kidney-fibrosis-abstract.md
3. chen-2013-rasal1-gastric-methylation-abstract.md
4. chen-2014-rasal1-gastric-abstract.md
5. deurloo-2024-rasal1-neuronal-abstract.md
6. jin-2007-rasal-methylation-abstract.md
7. liu-2013-rasal1-thyroid-abstract.md
8. ohta-2009-rasal1-colorectal-abstract.md
9. qiu-2017-rasal1-liver-fibrosis-abstract.md
10. simanshu-2019-rasgap-review-abstract.md
11. sondermann-2010-dual-gap-mechanism-abstract.md
12. sot-2013-rasal-membrane-abstract.md
13. thaker-2019-rasal1-zap70-abstract.md
14. xu-2015-rasal1-cardiac-fibrosis-abstract.md