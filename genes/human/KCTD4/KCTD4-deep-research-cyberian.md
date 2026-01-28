---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T20:41:15.296097'
end_time: '2026-01-22T20:54:45.506194'
duration_seconds: 810.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD4
  gene_symbol: KCTD4
  uniprot_accession: Q8WVF5
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD4;'
  gene_info: Name=KCTD4;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: BTB/POZ_dom. (IPR000210); KCTD4_C. (IPR045740); SKP1/BTB/POZ_sf.
    (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8WVF5
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD4;
- **Gene Information:** Name=KCTD4;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BTB/POZ_dom. (IPR000210); KCTD4_C. (IPR045740); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD4** (gene ID: KCTD4, UniProt: Q8WVF5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD4: A BTB/POZ Domain-Containing Protein with Emerging Roles in Calcium Homeostasis and Cancer Metastasis

## Introduction

KCTD4 (Potassium Channel Tetramerization Domain-containing protein 4) is a human protein encoded by the KCTD4 gene, located on chromosome 13q14.12-q14.13 (UniProt: Q8WVF5, NCBI Gene ID: 386618). The protein is 259 amino acids in length with a molecular mass of approximately 30 kDa. KCTD4 belongs to the KCTD protein family, a group of 25 human proteins characterized by the presence of a conserved N-terminal BTB/POZ (Bric-a-brac, Tramtrack, Broad complex/Poxvirus and Zinc finger) domain [liu-2013-kctd-family-review-abstract][teng-2019-kctd-family-abstract].

Despite its name suggesting a relationship to potassium channels, KCTD4 is a soluble, non-channel protein that lacks transmembrane domains. The "potassium channel tetramerization domain" nomenclature derives from the sequence similarity between the BTB domains of KCTD proteins and the T1/BTB domains that mediate tetramerization of voltage-gated potassium channel subunits [liu-2013-kctd-family-review-abstract]. Until recently, KCTD4 was among the least characterized members of the KCTD family, with its biological functions remaining largely unknown [teng-2019-kctd-family-abstract]. However, a landmark 2023 study has now revealed a specific molecular function for KCTD4 in regulating calcium homeostasis through interaction with the chloride intracellular channel protein CLIC1, with significant implications for cancer metastasis [zheng-2023-kctd4-clic1-abstract].

## Protein Structure and Domain Architecture

KCTD4 contains a single BTB/POZ domain (residues 34-119) at its N-terminus, followed by a C-terminal domain (CTD) that is specific to KCTD4 and its closest family members [esposito-2022-alphafold-kctd-abstract]. The BTB domain is a highly versatile protein-protein interaction motif approximately 120 amino acids in length, consisting of a core fold of five alpha helices and three beta sheets [bonchuk-2023-btb-domains-abstract]. This domain mediates homo- and hetero-oligomerization and enables interactions with non-BTB-containing partner proteins.

AlphaFold structural predictions have revealed that KCTD4 adopts a pentameric quaternary structure, similar to many other KCTD family members [esposito-2022-alphafold-kctd-abstract]. The three-dimensional structure of the KCTD4 pentamer is characterized by a propeller-like fold with a central cavity surrounded by regular and exposed beta-strands. Molecular dynamics simulations (200 ns timescale) have validated these predictions, demonstrating that the KCTD4 pentamer exhibits interdomain motions consisting of relative rotations between the CTD and BTB domains [esposito-2022-alphafold-kctd-abstract]. This dynamic behavior resembles that observed for other pentameric KCTD proteins such as KCTD5.

Notably, KCTD4 belongs to a subset of KCTD proteins that do not interact with Cullin 3 (Cul3), the E3 ubiquitin ligase component with which many KCTD family members associate [smaldone-2024-kctd-cullin3-abstract]. AlphaFold predictions consistently fail to generate stable KCTD4-Cul3 complex models, producing only "meaningless" complexes, which distinguishes KCTD4 from the 15 family members known to function as Cul3 substrate adaptors [smaldone-2024-kctd-cullin3-abstract]. This structural feature suggests that KCTD4 operates through mechanisms independent of the ubiquitin-proteasome system.

An important finding regarding KCTD4's oligomeric behavior is that it does not form hetero-oligomeric complexes with KCTD5, unlike many other KCTD family members [brogi-2023-kctd5-heterooligomers-abstract]. Using both co-immunoprecipitation and bioluminescence resonance energy transfer (BRET) assays, researchers found that while KCTD5 interacts with numerous KCTD family members (including KCTD2, KCTD3, KCTD6, KCTD8, KCTD10, KCTD13, KCTD14, KCTD15, KCTD16, KCTD17, KCTD20, KCTD21, BTBD10, SHKBP1, and KCNRG), KCTD4 was specifically tested and found not to interact [brogi-2023-kctd5-heterooligomers-abstract]. This finding suggests that KCTD4 functions primarily as homomeric pentamers rather than participating in heteromeric assemblies with other family members.

## Primary Molecular Function: Regulation of CLIC1 and Calcium Homeostasis

The most detailed functional characterization of KCTD4 comes from the work of Zheng and colleagues, who identified KCTD4 as a regulator of intracellular calcium levels through its interaction with CLIC1 (Chloride Intracellular Channel 1) [zheng-2023-kctd4-clic1-abstract]. This interaction represents the first well-characterized molecular function for KCTD4.

CLIC1 is a metamorphic protein that exists in equilibrium between soluble monomeric, soluble dimeric, and membrane-bound forms [wong-2019-clic1-calcium-abstract]. Dimerization of CLIC1 is essential for its membrane insertion and chloride channel activity. KCTD4 directly binds to CLIC1 through specific residues: LYS17, ASP72, and ASP74 on KCTD4 interact with GLU102, LYS138, and ARG208 on CLIC1 [zheng-2023-kctd4-clic1-abstract]. This interaction disrupts CLIC1 dimerization, thereby impairing chloride channel function.

The functional consequence of KCTD4-mediated CLIC1 inhibition is an increase in intracellular chloride concentration, which subsequently activates L-type calcium channels (LTCCs), leading to elevated intracellular calcium levels [zheng-2023-kctd4-clic1-abstract][wong-2019-clic1-calcium-abstract]. Experimental evidence supports this model: overexpression of KCTD4 increases intracellular Ca2+ levels, while KCTD4 knockdown decreases them. Furthermore, CRISPR/Cas9-mediated knockout of CLIC1 abolishes KCTD4's effects on calcium levels, establishing CLIC1 as an essential mediator of KCTD4 function [zheng-2023-kctd4-clic1-abstract].

## Signaling Pathways: The KCTD4-CLIC1-Ca2+-NFATc1-Fibronectin Axis

KCTD4-induced calcium elevation activates downstream signaling through the transcription factor NFATc1 (Nuclear Factor of Activated T cells, cytoplasmic 1) [zheng-2023-kctd4-clic1-abstract]. Elevated intracellular calcium promotes NFATc1 dephosphorylation and nuclear translocation, where it functions as a transcriptional activator. Chromatin immunoprecipitation (ChIP) assays have confirmed that NFATc1 directly binds to the fibronectin promoter, significantly enhancing fibronectin transcription [zheng-2023-kctd4-clic1-abstract].

Fibronectin, an extracellular matrix glycoprotein, plays critical roles in cell adhesion, migration, and tissue remodeling. KCTD4-overexpressing cells secrete elevated levels of fibronectin into the tumor microenvironment, which activates surrounding fibroblasts through paracrine signaling, converting them to cancer-associated fibroblasts (CAFs) [zheng-2023-kctd4-clic1-abstract]. These activated fibroblasts, in turn, secrete MMP24 (matrix metalloproteinase 24), which promotes cancer cell invasion in a positive feedback loop that amplifies metastatic capacity.

## Weak Interaction with G Protein Beta-Gamma Subunits

Beyond its interaction with CLIC1, KCTD4 has been identified as a weak interactor with Gbetagamma subunits of heterotrimeric G proteins [spiombi-2023-gbetagamma-abstract]. Immunoprecipitation experiments placed KCTD4 among the weaker Gbetagamma binders within the KCTD family, in contrast to strong interactors such as KCTD2, KCTD5, and KCTD17.

Functional studies in primary striatal neurons examined KCTD4's effects on dopamine-induced cAMP signaling. While KCTD4 did not significantly alter the amplitude of cAMP responses in D1R-positive neurons, it did modulate cAMP kinetics, reducing the overall wave of cAMP response (measured as area under the curve) [spiombi-2023-gbetagamma-abstract]. This suggests that even weak Gbetagamma engagement can influence neuronal signaling, though the physiological significance of this interaction remains to be fully elucidated.

## Cellular and Tissue Localization

According to the Human Protein Atlas, KCTD4 exhibits brain-enriched expression, with the highest RNA levels detected in the basal ganglia (45.2 nTPM), amygdala (25.5 nTPM), and hippocampal formation (14.5 nTPM) [human-protein-atlas-kctd4-summary]. This brain enrichment is consistent with NCBI Gene expression data showing overexpression in the nucleus accumbens, amygdala, caudate, hippocampus, and putamen. Additional expression has been documented in frontal cortex, spinal cord, and testis.

At the subcellular level, KCTD4 has been localized to centriolar satellites, membraneless electron-dense granules that cluster around centrosomes and cilia [human-protein-atlas-kctd4-summary]. Centriolar satellites serve as important regulators of centrosome function and primary cilium assembly, suggesting potential roles for KCTD4 in these processes that remain to be investigated. The protein is predicted to be predominantly intracellular, consistent with its lack of signal peptide or transmembrane domains.

At the single-cell level, particularly high expression has been observed in retinal pigment epithelial cells (72.5 nCPM), as well as in oligodendrocytes, oligodendrocyte progenitor cells, and cardiomyocytes [human-protein-atlas-kctd4-summary]. Expression clustering analysis has categorized KCTD4 within "Neurons - Mixed function," suggesting potential roles in diverse neuronal cell types.

## Role in Cancer

KCTD4's role in cancer has primarily been characterized in esophageal squamous cell carcinoma (ESCC), where it functions as a driver of metastasis [zheng-2023-kctd4-clic1-abstract]. Transcriptome sequencing of primary ESCC and matched metastatic tissues revealed KCTD4 upregulation in metastatic samples. Clinical correlation analyses demonstrated that high KCTD4 expression is associated with lymph node metastasis and dramatically reduced patient survival (median 13.0 months vs. 37.0 months for low expressors) [zheng-2023-kctd4-clic1-abstract].

Functional experiments have confirmed KCTD4's pro-metastatic role: KCTD4-overexpressing cells showed enhanced capacity to metastasize to popliteal lymph nodes and lungs in mouse models, while KCTD4 knockdown markedly suppressed invasion and metastasis [zheng-2023-kctd4-clic1-abstract]. These effects depend on CLIC1, as CLIC1 knockout abolishes the pro-metastatic effects of KCTD4 overexpression.

Database mining analyses have also identified KCTD4 overexpression in approximately 5% of lung cancer samples (fold-change 1.32, p < 0.001) [canettieri-2021-kctd-cancer-abstract]. The Human Protein Atlas has identified KCTD4 as a prognostic marker in colon adenocarcinoma, with cancer-enhanced expression patterns observed in glioblastoma multiforme and kidney renal papillary cell carcinoma [human-protein-atlas-kctd4-summary].

## Therapeutic Potential

The identification of the KCTD4-CLIC1 interaction as a driver of cancer metastasis has opened potential therapeutic avenues. Zheng et al. performed virtual screening of 1.5 million compounds to identify inhibitors of this protein-protein interaction, leading to the discovery of lead compound K279-0738 [zheng-2023-kctd4-clic1-abstract]. This compound successfully targets the KCTD4-CLIC1 interface and produces the following effects: reduction of intracellular calcium levels, inhibition of NFATc1 nuclear translocation, suppression of fibronectin expression, blockade of cancer cell invasion in a dose-dependent manner, and significant inhibition of tumor metastasis in vivo [zheng-2023-kctd4-clic1-abstract]. These findings validate KCTD4 as a potential therapeutic target for metastatic esophageal cancer.

## Evolutionary Context and Family Relationships

KCTD4 is evolutionarily conserved across vertebrates, with orthologs present in mouse (Gene ID: 67516, MGI:1914766), rat, cattle, chicken, and zebrafish [human-protein-atlas-kctd4-summary][mgi-kctd4-summary]. The zebrafish ortholog (kctd4) shows expression in hindbrain, hypothalamus, and telencephalon, suggesting conserved neuronal functions. Within the human KCTD family, KCTD11 is listed as an important paralog of KCTD4 [canettieri-2021-kctd-cancer-abstract].

The mouse ortholog (Kctd4) has been the subject of limited functional studies. According to the Mouse Genome Informatics database, six phenotype references and six mutant alleles (including three targeted mutations) have been documented for Kctd4 [mgi-kctd4-summary]. The gene shows broad developmental expression across 710 expression assay results, with functional annotations associating it with carbohydrate metabolism, cell differentiation, immune function, transcription, and programmed cell death [mgi-kctd4-summary]. However, detailed phenotypic characterization of Kctd4 knockout mice has not been published in the primary literature, leaving the physiological consequences of KCTD4 deficiency in mammals largely unknown.

Structurally, KCTD4 belongs to Cluster 4 of the KCTD family based on phylogenetic and structural analyses [esposito-2022-alphafold-kctd-abstract]. This cluster includes pentameric proteins that, unlike many other KCTD members, do not function as Cullin 3 adaptors. This classification is consistent with the experimental and computational evidence demonstrating that KCTD4 does not form stable complexes with Cul3 [smaldone-2024-kctd-cullin3-abstract].

## Open Questions

Several important questions about KCTD4 biology remain unresolved:

1. **Physiological function in the brain**: Given KCTD4's prominent brain expression, particularly in basal ganglia and limbic structures, what is its normal physiological role in neurons? Does it regulate calcium homeostasis and NFAT signaling in neural contexts?

2. **Centriolar satellite function**: What is the significance of KCTD4's localization to centriolar satellites? Does it play roles in centrosome function, ciliogenesis, or cell division?

3. **Relationship to Gbetagamma signaling**: While KCTD4 weakly interacts with Gbetagamma subunits, the physiological relevance of this interaction is unclear. Does this contribute to KCTD4's neuronal functions?

4. **Oligomeric state in vivo**: While KCTD4 forms pentamers in structural predictions and does not hetero-oligomerize with KCTD5, its actual oligomeric state in cells and whether it can form heteromers with KCTD proteins other than KCTD5 remains to be fully determined.

5. **Additional binding partners**: Beyond CLIC1 and Gbetagamma, does KCTD4 have other physiologically relevant interaction partners that might explain its diverse tissue expression?

6. **Role in other cancers**: Beyond ESCC, what is KCTD4's function in other cancers where it shows altered expression, such as lung cancer, glioblastoma, and colon adenocarcinoma?

7. **Developmental roles**: Given its expression in fetal tissues, does KCTD4 play roles in development?

8. **Therapeutic window**: Further characterization of KCTD4's normal physiological functions will be essential to assess whether targeting KCTD4 or the KCTD4-CLIC1 interaction would have acceptable side effect profiles.

## References

- [zheng-2023-kctd4-clic1-abstract] Zheng CC, Yu C, Xu TY, et al. KCTD4 interacts with CLIC1 to disrupt calcium homeostasis and promote metastasis in esophageal cancer. Acta Pharm Sin B. 2023;13(9):3712-3726. PMID: 37719378; PMCID: PMC10547965. DOI: 10.1016/j.apsb.2023.06.011. https://pmc.ncbi.nlm.nih.gov/articles/PMC10547965/

- [teng-2019-kctd-family-abstract] Teng X, Aouacheria A, Lionnard L, et al. KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders. CNS Neurosci Ther. 2019;25(7):887-902. PMID: 31111679; PMCID: PMC6566181. DOI: 10.1111/cns.13156. https://pmc.ncbi.nlm.nih.gov/articles/PMC6566181/

- [spiombi-2023-gbetagamma-abstract] Spiombi E, et al. Multiple potassium channel tetramerization domain (KCTD) family members interact with Gbetagamma, with effects on cAMP signaling. J Biol Chem. 2023;299(3):102907. PMID: 36736897; PMCID: PMC9976452. DOI: 10.1016/j.jbc.2023.102907. https://pmc.ncbi.nlm.nih.gov/articles/PMC9976452/

- [esposito-2022-alphafold-kctd-abstract] Esposito L, Balasco N, Smaldone G, et al. Alphafold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family. Int J Mol Sci. 2022;23(21):13346. PMID: 36362128; PMCID: PMC9658877. DOI: 10.3390/ijms232113346. https://pmc.ncbi.nlm.nih.gov/articles/PMC9658877/

- [smaldone-2024-kctd-cullin3-abstract] Smaldone G, Ruggiero A, Esposito L, et al. A Comprehensive Analysis of the Structural Recognition between KCTD Proteins and Cullin 3. Int J Mol Sci. 2024;25(3):1881. PMID: 38339162; PMCID: PMC10856315. DOI: 10.3390/ijms25031881. https://pmc.ncbi.nlm.nih.gov/articles/PMC10856315/

- [pinkas-2017-kctd-structural-complexity-abstract] Pinkas DM, Sanvitale CE, Jovanović B, et al. Structural complexity in the KCTD family of Cullin3-dependent E3 ubiquitin ligases. Biochem J. 2017;474(22):3747-3761. PMID: 28963344; PMCID: PMC5664961. DOI: 10.1042/BCJ20160717. https://pmc.ncbi.nlm.nih.gov/articles/PMC5664961/

- [liu-2013-kctd-family-review-abstract] Liu Z, Xiang Y, Sun G. The KCTD family of proteins: structure, function, disease relevance. Cell Biosci. 2013;3(1):45. PMID: 24289649; PMCID: PMC3882106. DOI: 10.1186/2045-3701-3-45. https://pmc.ncbi.nlm.nih.gov/articles/PMC3882106/

- [canettieri-2021-kctd-cancer-abstract] De Smaele E, et al. The emerging role of the KCTD proteins in cancer. Cell Commun Signal. 2021;19(1):56. PMID: 33958002; PMCID: PMC8127222. DOI: 10.1186/s12964-021-00737-8. https://pmc.ncbi.nlm.nih.gov/articles/PMC8127222/

- [bonchuk-2023-btb-domains-abstract] Bonchuk A, Kamalyan S, Maksimenko O, Georgiev P. BTB domains: A structural view of evolution, multimerization, and protein-protein interactions. BioEssays. 2023;45(2):e2200179. PMID: 36449605. DOI: 10.1002/bies.202200179. https://onlinelibrary.wiley.com/doi/10.1002/bies.202200179

- [wong-2019-clic1-calcium-abstract] Wong R, et al. The inhibition of chloride intracellular channel 1 enhances Ca2+ and reactive oxygen species signaling in A549 human lung cancer cells. Exp Mol Med. 2019;51(8):1-11. PMID: 31316050; PMCID: PMC6802611. DOI: 10.1038/s12276-019-0279-2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6802611/

- [human-protein-atlas-kctd4-summary] Human Protein Atlas - KCTD4 (ENSG00000180332). https://www.proteinatlas.org/ENSG00000180332-KCTD4

- [brogi-2023-kctd5-heterooligomers-abstract] Brogi S, et al. KCTD5 Forms Hetero-Oligomeric Complexes with Various Members of the KCTD Protein Family. Int J Mol Sci. 2023;24(18):14317. PMID: 37762629; PMCID: PMC10531988. DOI: 10.3390/ijms241814317. https://pmc.ncbi.nlm.nih.gov/articles/PMC10531988/

- [mgi-kctd4-summary] Mouse Genome Informatics - Kctd4 (MGI:1914766). https://www.informatics.jax.org/marker/MGI:1914766


## Citations

1. bonchuk-2023-btb-domains-abstract.md
2. brogi-2023-kctd5-heterooligomers-abstract.md
3. canettieri-2021-kctd-cancer-abstract.md
4. esposito-2022-alphafold-kctd-abstract.md
5. human-protein-atlas-kctd4-summary.md
6. liu-2013-kctd-family-review-abstract.md
7. mgi-kctd4-summary.md
8. pinkas-2017-kctd-structural-complexity-abstract.md
9. smaldone-2024-kctd-cullin3-abstract.md
10. spiombi-2023-gbetagamma-abstract.md
11. teng-2019-kctd-family-abstract.md
12. wong-2019-clic1-calcium-abstract.md
13. zheng-2023-kctd4-clic1-abstract.md