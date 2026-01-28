---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T20:21:08.182458'
end_time: '2026-01-22T20:41:01.830051'
duration_seconds: 1193.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD18
  gene_symbol: KCTD18
  uniprot_accession: Q6PI47
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD18;'
  gene_info: Name=KCTD18;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: KCTD18_C. (IPR045704); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB.
    (IPR003131); BTB_2 (PF02214); KCTD18_C (PF19321)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6PI47
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD18;
- **Gene Information:** Name=KCTD18;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** KCTD18_C. (IPR045704); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214); KCTD18_C (PF19321)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD18" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD18' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD18** (gene ID: KCTD18, UniProt: Q6PI47) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD18: A BTB/POZ Domain-Containing Protein with Predicted Cullin3 Adapter Function

## Introduction

KCTD18 (Potassium Channel Tetramerization Domain-containing 18; UniProt Q6PI47) is a 426 amino acid human protein encoded by a gene located on chromosome 2q33.1. The protein belongs to the KCTD family, which comprises 25-26 members in humans characterized by the presence of a BTB/POZ (Broad-Complex, Tramtrack, and Bric-à-Brac / Poxvirus and Zinc finger) domain at their N-terminus [liu-2013-kctd-review-abstract]. Despite the extensive characterization of many KCTD family members in diverse biological processes including neurological signaling, cancer, and metabolism, KCTD18 has until recently remained one of the least characterized proteins in this family [angrisani-2021-kctd-cancer-abstract].

The primary molecular function of KCTD18 appears to be participation in protein-protein interactions, specifically as a predicted substrate adapter for the Cullin3-based E3 ubiquitin ligase complex. Recent computational structural analyses using AlphaFold have suggested that KCTD18 forms a stable 1:1 complex with Cullin3, distinguishing it from most other KCTD family members that function as pentameric Cul3 adapters [balasco-2024-kctd-cul3-abstract]. This monomeric behavior, combined with phylogenetic analyses showing KCTD18 as an isolated member not clustering with other KCTD proteins, suggests it may have evolved distinct functional properties [esposito-2021-alphafold-kctd-abstract].

Recent experimental evidence has begun to elucidate KCTD18 function. A 2022 genome-wide association study identified KCTD18 as a regulator of adipocyte progenitor cell proliferation, with siRNA knockdown experiments demonstrating that reduced KCTD18 expression decreases the number of proliferating cells in human adipose-derived stem cells [kulyte-2022-fatcell-gwas-abstract]. This finding represents the first direct experimental evidence for KCTD18's biological role.

The clinical relevance of KCTD18 has been established through genetic association studies, with the most significant finding being a haplotype spanning the KCTD18 gene region associated with restless legs syndrome (RLS) in a South Tyrolean population [pichler-2013-rls4-abstract]. Additional associations have linked KCTD18 variants to fat cell number and type 2 diabetes risk [kulyte-2022-fatcell-gwas-abstract], and chromosomal duplications encompassing KCTD18 have been observed in patients with neurodevelopmental phenotypes [teng-2019-kctd-neuro-abstract].

## Domain Architecture and Structural Features

KCTD18 contains two characterized domains that define its structural architecture. The N-terminal region (residues 12-80) harbors the eponymous BTB/POZ domain, which represents the defining feature of the KCTD protein family [liu-2013-kctd-review-abstract]. This domain shows sequence similarity to the T1 tetramerization domain of voltage-gated potassium channels, from which the family derives its name, although KCTD proteins do not function as ion channels.

The BTB domain in KCTD proteins serves dual roles in mediating protein oligomerization and facilitating interactions with partner proteins, particularly Cullin3 [dementieva-2009-kctd5-pentamer-abstract]. In most characterized KCTD family members, the BTB domain assembles into pentameric rings rather than the tetrameric arrangements observed in voltage-gated potassium channel T1 domains. This difference in stoichiometry has been attributed to four amino acid substitutions at key positions within the oligomerization interface [dementieva-2009-kctd5-pentamer-abstract]. However, KCTD18 appears to deviate from this pentameric paradigm.

Computational predictions using AlphaFold have revealed that attempts to model KCTD18 in a pentameric state result in highly unreliable structures with large expected errors between chains [esposito-2022-alphafold-oligomers-abstract]. The only reliably predicted portions of the pentameric model are the individual BTB and C-terminal domain (CTD) chains. This finding strongly suggests that KCTD18 operates in a non-pentameric, likely monomeric state, distinguishing it fundamentally from the majority of KCTD family members [esposito-2022-alphafold-oligomers-abstract].

The C-terminal portion of KCTD18 contains a conserved KCTD18_C domain (Pfam PF19321, InterPro IPR045704). Interestingly, AlphaFold-based structural analyses have revealed that despite lacking detectable sequence similarity in the C-terminal region, most KCTD proteins share a structurally similar C-terminal domain [esposito-2021-alphafold-kctd-abstract]. The protein also contains disordered regions between residues 305-371 and 389-408, as annotated in UniProt.

## Molecular Function: Predicted Cullin3 Adapter Activity and Role in Cell Proliferation

The primary molecular function of KCTD18 appears to involve serving as a substrate adapter for the Cullin3 (Cul3)-based E3 ubiquitin ligase system. Multiple KCTD family members have been experimentally validated as Cul3 adapters, recruiting specific substrate proteins for ubiquitination and subsequent proteasomal degradation [pinkas-2017-kctd-structural-abstract]. The structural basis for this interaction involves the BTB domain of KCTD proteins binding to the N-terminal region of Cullin3, while the C-terminal region of Cul3 associates with the RING protein Rbx1 and E2-ubiquitin conjugating enzymes.

For KCTD18 specifically, computational structural analysis using AlphaFold has predicted a stable 1:1 complex between the KCTD18 BTB domain and Cullin3 [balasco-2024-kctd-cul3-abstract]. This monomeric stoichiometry is unusual within the KCTD family, where most Cul3-interacting members form pentameric BTB assemblies that bind five Cul3 molecules to create 5:5 heterodecameric complexes [pinkas-2017-kctd-structural-abstract]. The reliability of the predicted KCTD18-Cul3 complex, as assessed by AlphaFold confidence metrics, provides computational support for functional Cullin3 interaction, though experimental validation remains pending [balasco-2024-kctd-cul3-abstract].

The most significant experimental evidence for KCTD18 function comes from Kulyté et al. (2022), who performed a genome-wide association study of fat cell number in 896 participants with adipose tissue biopsies [kulyte-2022-fatcell-gwas-abstract]. This study identified a variant in the KCTD18 locus (rs565245989) that was strongly associated with fat cell number (β = 0.154, P = 4.61 × 10⁻⁶). Notably, this SNP comprises a frameshift mutation, suggesting it may have direct functional consequences for the protein. Subsequent siRNA knockdown experiments in human adipose-derived stem cells (hASCs) demonstrated that reduction of KCTD18 expression (by 70-90%) resulted in decreased numbers of proliferating cells. Importantly, the impact of KCTD18 knockdown on proliferation was not associated with altered lipid accumulation, suggesting its mechanism operates independently of adipogenesis per se and instead affects progenitor cell proliferation directly [kulyte-2022-fatcell-gwas-abstract].

If KCTD18 functions as a Cul3 adapter, its ubiquitination substrates remain unidentified. For other KCTD family members, known substrates include transcription factors (such as c-Myc for KCTD2), developmental signaling pathway components (such as Gli transcription factors for KCTD11), and cytoskeletal regulators (such as RhoA for KCTD13). Given KCTD18's demonstrated role in cell proliferation, potential substrates may include cell cycle regulators or growth factor signaling components, though this remains speculative.

## Subcellular Localization

Data from the Human Protein Atlas indicates that KCTD18 localizes primarily to mitochondria, with additional cytoplasmic and nuclear expression observed in most tissues. The protein is classified as a "predicted intracellular protein" consistent with its lack of signal peptide or transmembrane domains.

This mitochondrial localization, if validated experimentally, would be notable as it could suggest roles in mitochondrial quality control, metabolism, or mitochondria-associated ubiquitination processes. However, it should be noted that subcellular localization data for KCTD18 appears to be derived primarily from immunohistochemistry and prediction algorithms rather than detailed fractionation or live-cell imaging studies.

## Tissue Expression and Clinical Associations

KCTD18 demonstrates low tissue specificity with broad, relatively uniform expression across human tissues. According to NCBI Gene and Human Protein Atlas data, the highest expression levels are observed in thyroid gland (13.0 nTPM), blood vessels (11.7 nTPM), spinal cord (11.5 nTPM), and pancreas (11.2 nTPM). At the single-cell level, KCTD18 shows enrichment in early primary spermatocytes, adrenal cortex cells, and thyroid glandular cells.

### Restless Legs Syndrome

The most significant clinical association for KCTD18 comes from genetic linkage studies of restless legs syndrome (RLS). Pichler et al. (2013) performed fine-mapping of the RLS4 locus on chromosome 2q33 in South Tyrolean families and identified a 46.9 kb candidate region spanning KCTD18 and portions of the neighboring SPATS2L gene [pichler-2013-rls4-abstract]. A haplotype of 23 SNPs within this region was shared by all affected members of three linked families, representing strong genetic evidence implicating this locus in RLS susceptibility. However, the causative variant and whether KCTD18 or SPATS2L (or both) contribute to disease pathogenesis remains undetermined.

### Adiposity and Metabolic Disease

The genome-wide association study by Kulyté et al. (2022) provided evidence linking KCTD18 to metabolic phenotypes [kulyte-2022-fatcell-gwas-abstract]. Variants in the KCTD18 locus were associated with fat cell number, and 30 type 2 diabetes-associated SNPs displayed nominal associations with fat cell number in this cohort. The experimental demonstration that KCTD18 knockdown reduces adipocyte progenitor proliferation suggests a potential mechanism by which KCTD18 variants might influence body composition and diabetes risk.

### Neurodevelopmental Phenotypes

Teng et al. (2019) documented that chromosomal duplication of the 2q33 region encompassing KCTD18 and ADAM23 has been observed in patients with epilepsy, developmental delay, and autistic behavior [teng-2019-kctd-neuro-abstract]. These observations suggest potential neurodevelopmental roles for KCTD18, consistent with the broader involvement of the KCTD family in neurological disorders, though causality has not been established.

### Cancer

The Human Protein Atlas notes KCTD18 as a prognostic marker in kidney renal clear cell carcinoma, though the direction of this association and its mechanistic basis have not been characterized in the primary literature [angrisani-2021-kctd-cancer-abstract]. KCTD18 has also been identified as a potential driver gene in a case of signet ring cell carcinoma of the bladder in a genomic sequencing study, though further validation is needed.

## Phylogenetic Position and Family Relationships

KCTD18 occupies a unique phylogenetic position within the KCTD protein family. Liu et al. (2013) classified KCTD proteins into seven major groups (A-G) based on amino acid sequence alignment, but noted that KCTD18, along with KCTD4, KCTD19, and KCTD20, "do not belong to these seven groups" [liu-2013-kctd-review-abstract]. This phylogenetic isolation has been confirmed by structure-based analyses using AlphaFold-predicted structures, which showed that "with the exception of KCTD18, all other canonical members of the family are clustered in groups that contain two or more members" [esposito-2021-alphafold-kctd-abstract].

Database annotations indicate KCTD12 as an important paralog of KCTD18, though the functional implications of this relationship remain unclear. KCTD12 belongs to the D group (or F clade in some classifications) of KCTD proteins and has been well-characterized as an auxiliary subunit of GABA-B receptors, modulating receptor pharmacology and signaling kinetics. In contrast, KCTD18 shows no evidence for GABA receptor association and lacks the conserved C-terminal domain features that mediate KCTD12's receptor interactions.

The evolutionary isolation of KCTD18 suggests potential functional divergence from other family members. This divergence is reflected structurally in its predicted monomeric behavior and may indicate specialized roles that distinguish it from the canonical pentameric Cullin3 adapters that predominate in the KCTD family.

## Model Organisms and Functional Genomics Resources

The mouse ortholog of KCTD18 (Kctd18; MGI:3603813) is located on chromosome 1. The Mouse Genome Informatics database documents 20 mutations/alleles for Kctd18, including 15 gene trap mutations, 2 targeted knockouts, and chemically/radiation-induced mutations. Nine phenotype references are listed in the literature. However, comprehensive phenotyping data from the International Mouse Phenotyping Consortium (IMPC) is not yet available for this gene; while ES cells have been produced, the gene is listed as "selected for production" rather than phenotyped.

KCTD18 is profiled in the DepMap (Cancer Dependency Map) project, which provides CRISPR and RNAi screening data across hundreds of cancer cell lines. This resource can be used to assess whether KCTD18 is essential in specific cancer contexts, though detailed analysis of these data is beyond the scope of this review.

## Protein-Protein Interactions

UniProt and interaction databases document multiple protein interactions for KCTD18, though most await detailed validation. BioGRID reports 15 interactions while IntAct documents 11 interactions. The most confidently predicted interaction is with Cullin3, based on AlphaFold structural modeling that predicts a stable 1:1 KCTD18-Cul3 complex [balasco-2024-kctd-cul3-abstract].

Gene Ontology annotations indicate KCTD18 participates in "protein homooligomerization," though structural predictions suggest this may occur differently than in other KCTD proteins. The predicted monomeric behavior of KCTD18 contrasts with the documented pentameric assemblies of KCTD1, KCTD5, KCTD9, KCTD12, and KCTD17 [smaldone-2016-btb-pentamers-abstract].

The identification of physiological KCTD18 interaction partners and potential ubiquitination substrates represents a critical gap in understanding this protein's biological function. Given the demonstrated role in cell proliferation [kulyte-2022-fatcell-gwas-abstract], identifying the relevant substrates would be particularly valuable for understanding the molecular mechanism.

## Open Questions

Several fundamental questions about KCTD18 biology remain unanswered and represent opportunities for future investigation:

1. **Identification of ubiquitination substrates**: Given KCTD18's predicted Cul3 adapter function and demonstrated role in cell proliferation, what proteins does it target for ubiquitination? Candidate substrates may include cell cycle regulators or growth factor signaling components.

2. **Mechanism of cell proliferation regulation**: How does KCTD18 regulate adipocyte progenitor proliferation? Does this involve Cul3-mediated ubiquitination of specific substrates, and does this mechanism extend to other cell types?

3. **Experimental validation of Cul3 interaction**: While AlphaFold predictions support a monomeric KCTD18-Cul3 complex, direct experimental evidence (co-immunoprecipitation, structural studies) is needed to confirm this interaction.

4. **Mechanism of restless legs syndrome association**: Does the RLS4 haplotype affect KCTD18 expression or function? What is the molecular pathway connecting KCTD18 to sleep-related motor symptoms? Is the association mediated through KCTD18, SPATS2L, or both genes?

5. **Confirmation of monomeric state**: Experimental validation (analytical ultracentrifugation, size-exclusion chromatography, native mass spectrometry) is needed to confirm whether KCTD18 indeed functions as a monomer rather than a pentamer.

6. **Subcellular localization validation**: The reported mitochondrial localization requires confirmation through multiple approaches and investigation of potential mitochondrial functions.

7. **Mouse phenotype characterization**: The Kctd18 knockout mouse model exists but has not been comprehensively phenotyped. Systematic analysis could reveal in vivo functions relevant to human disease associations.

8. **Metabolic disease connection**: Given the genetic associations with fat cell number and type 2 diabetes risk, what are the in vivo metabolic consequences of KCTD18 deficiency?

## References

- [liu-2013-kctd-review-abstract] Liu Z, Xiang Y, Sun G. The KCTD family of proteins: structure, function, disease relevance. Cell & Bioscience. 2013;3:45. DOI: 10.1186/2045-3701-3-45. PMCID: PMC3882106.

- [pichler-2013-rls4-abstract] Pichler I, Schwienbacher C, Zanon A, et al. Fine-mapping of restless legs locus 4 (RLS4) identifies a haplotype over the SPATS2L and KCTD18 genes. J Mol Neurosci. 2013;49(3):600-605. DOI: 10.1007/s12031-012-9891-5. PMID: 23054586.

- [teng-2019-kctd-neuro-abstract] Teng X, Aouacheria A, Lionnard L, et al. KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders. CNS Neurosci Ther. 2019;25(7):887–902. DOI: 10.1111/cns.13156. PMCID: PMC6566181.

- [angrisani-2021-kctd-cancer-abstract] Angrisani A, Di Fiore A, De Smaele E, Moretti M. The emerging role of the KCTD proteins in cancer. Cell Commun Signal. 2021;19(1):56. DOI: 10.1186/s12964-021-00737-8. PMCID: PMC8127222.

- [kulyte-2022-fatcell-gwas-abstract] Kulyté A, Aman A, Strawbridge RJ, Arner P, Dahlman IA. Genome-Wide Association Study Identifies Genetic Loci Associated With Fat Cell Number and Overlap With Genetic Risk Loci for Type 2 Diabetes. Diabetes. 2022;71(6):1350-1362. DOI: 10.2337/db21-0804. PMID: 35320353. PMCID: PMC9163556.

- [balasco-2024-kctd-cul3-abstract] Balasco N, Esposito L, Smaldone G, Salvatore M, Vitagliano L. A Comprehensive Analysis of the Structural Recognition between KCTD Proteins and Cullin 3. Int J Mol Sci. 2024;25(3):1881. DOI: 10.3390/ijms25031881. PMCID: PMC10856315.

- [esposito-2022-alphafold-oligomers-abstract] Esposito L, Balasco N, Vitagliano L. Alphafold predictions provide insights into the structural features of the functional oligomers of all members of the KCTD family. Int J Mol Sci. 2022;23(21):13346. DOI: 10.3390/ijms232113346. PMCID: PMC9658877.

- [esposito-2021-alphafold-kctd-abstract] Esposito L, Balasco N, Smaldone G, Berisio R, Ruggiero A, Vitagliano L. AlphaFold-Predicted Structures of KCTD Proteins Unravel Previously Undetected Relationships among the Members of the Family. Biomolecules. 2021;11(12):1862. DOI: 10.3390/biom11121862. PMCID: PMC8699099. PMID: 34944504.

- [smaldone-2016-btb-pentamers-abstract] Smaldone G, Pirone L, Pedone E, Marlovits T, Vitagliano L, Ciccarelli L. The BTB domains of the potassium channel tetramerization domain proteins prevalently assume pentameric states. FEBS Lett. 2016;590(11):1663-71. DOI: 10.1002/1873-3468.12203. PMID: 27152988.

- [dementieva-2009-kctd5-pentamer-abstract] Dementieva IS, Tereshko V, McCrossan ZA, et al. Pentameric Assembly of Potassium Channel Tetramerization Domain-Containing Protein 5 (KCTD5). J Mol Biol. 2009;387(1):175–191. DOI: 10.1016/j.jmb.2009.01.030. PMCID: PMC2670943. PMID: 19361449.

- [pinkas-2017-kctd-structural-abstract] Pinkas DM, Sanvitale CE, Bufton JC, et al. Structural complexity in the KCTD family of Cullin3-dependent E3 ubiquitin ligases. Biochem J. 2017;474(22):3747–3761. DOI: 10.1042/BCJ20170527. PMCID: PMC5664961.


## Citations

1. angrisani-2021-kctd-cancer-abstract.md
2. balasco-2024-kctd-cul3-abstract.md
3. dementieva-2009-kctd5-pentamer-abstract.md
4. esposito-2021-alphafold-kctd-abstract.md
5. esposito-2022-alphafold-oligomers-abstract.md
6. kulyte-2022-fatcell-gwas-abstract.md
7. liu-2013-kctd-review-abstract.md
8. pichler-2013-rls4-abstract.md
9. pinkas-2017-kctd-structural-abstract.md
10. smaldone-2016-btb-pentamers-abstract.md
11. teng-2019-kctd-neuro-abstract.md