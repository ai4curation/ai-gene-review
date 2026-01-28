---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T23:36:42.174279'
end_time: '2026-01-23T23:50:25.362198'
duration_seconds: 823.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TMEM43
  gene_symbol: TMEM43
  uniprot_accession: Q9BTV4
  protein_description: 'RecName: Full=Transmembrane protein 43; AltName: Full=Protein
    LUMA;'
  gene_info: Name=TMEM43; ORFNames=UNQ2564/PRO6244;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TMEM43 family. .
  protein_domains: TMEM43_fam. (IPR012430); TMEM43 (PF07787)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BTV4
- **Protein Description:** RecName: Full=Transmembrane protein 43; AltName: Full=Protein LUMA;
- **Gene Information:** Name=TMEM43; ORFNames=UNQ2564/PRO6244;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TMEM43 family. .
- **Key Domains:** TMEM43_fam. (IPR012430); TMEM43 (PF07787)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TMEM43" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TMEM43' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TMEM43** (gene ID: TMEM43, UniProt: Q9BTV4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TMEM43 (Transmembrane Protein 43 / Protein LUMA): A Comprehensive Functional Analysis

## Introduction and Summary

TMEM43 (Transmembrane Protein 43), also known as protein LUMA, is a highly conserved integral membrane protein that has emerged as a multifunctional molecule with critical roles in cardiac, auditory, and muscular physiology. Originally identified as a protein of unknown function, TMEM43 gained clinical prominence in 2008 when Merner and colleagues identified the p.S358L missense mutation as the causative variant for arrhythmogenic right ventricular cardiomyopathy type 5 (ARVC5) in a founder population from Newfoundland, Canada[merner-2008-ARVC5-abstract]. Since then, research has revealed that TMEM43 functions at multiple subcellular locations and participates in diverse cellular processes including mechanotransduction, gap junction communication, and ion channel function.

The human TMEM43 gene encodes a 400 amino acid protein belonging to the TMEM43 family (InterPro: IPR012430, Pfam: PF07787). According to PubMed, the protein contains four predicted transmembrane domains with one intramembrane domain, and both N- and C-termini oriented extracellularly[kang-2024-TMEM-ion-channels-summary]. Recent evidence has established that TMEM43 functions as a nonselective cation channel, earning it the alternative designation "Gapjinc" (Gap junction interacting channel) due to its intimate association with connexin gap junction proteins[kang-2024-TMEM-ion-channels-summary]. The protein localizes to multiple cellular compartments including the inner nuclear membrane, endoplasmic reticulum, and plasma membrane, as well as cardiac intercalated discs and epithelial adherens junctions[orgil-2025-TMEM43-review-abstract][franke-2014-intercalated-disc-abstract].

## Molecular Structure and Topology

TMEM43 is predicted to contain four transmembrane (TM) domains based on hydrophobicity analysis, with the secondary structure featuring four TMs and one intramembrane domain. Both N-terminal and C-terminal domains are oriented toward the extracellular/luminal space[jang-2021-ANSD-summary]. This topology has been experimentally verified through immunocytochemistry with and without cell permeabilization, demonstrating that the intracellular loop 1 region (residues 203-308) resides in the cytoplasm[jang-2021-ANSD-summary].

A high-resolution three-dimensional structure of TMEM43 has not yet been determined experimentally through crystallography or cryo-electron microscopy. AlphaFold2 predictions of the monomeric architecture reveal a somewhat scrambled intramembrane domain configuration, suggesting that the protein may require additional structural context for proper folding[kang-2024-TMEM-ion-channels-summary]. The protein is phylogenetically conserved across species, with the transmembrane domains showing particularly high conservation from invertebrates to humans[jang-2021-ANSD-summary]. Notably, the serine at position 358, whose mutation to leucine causes ARVC5, lies within a highly conserved transmembrane domain[merner-2008-ARVC5-abstract].

TMEM43 forms oligomeric complexes that are essential for its function. Studies by Liang and colleagues demonstrated that the p.E85K mutation in the EDMD-related myopathy causes failure of LUMA oligomerization, a process critical for protein complex formation at the nuclear membrane[liang-2011-EDMD-abstract]. The ability to oligomerize appears to be important for TMEM43's interaction with its various binding partners including emerin, lamins, SUN2, and connexins.

## Subcellular Localization

The subcellular localization of TMEM43 has been a subject of significant investigation and some controversy. Early studies established TMEM43 as an inner nuclear membrane protein, associated with the LINC (Linker of Nucleoskeleton and Cytoskeleton) complex. The LINC complex provides mechanical coupling between the nuclear envelope and the cytoskeleton, playing critical roles in mechanotransduction, nuclear positioning, and chromatin organization[meinke-2011-LINC-complex-abstract][stroud-2018-mouse-knockout-abstract].

However, subsequent immunolocalization studies by Franke and colleagues challenged the exclusive nuclear envelope localization model. Using highly specific antibodies, they discovered that in mammalian tissues, LUMA is a component of zonula adhaerens and punctum adhaerens plaques in diverse epithelia, and is also located in composite junctions (CJs) at myocardial intercalated disks[franke-2014-intercalated-disc-abstract]. Importantly, in these cell types, LUMA was not detected in the nuclear envelope, suggesting tissue-specific or condition-specific localization patterns.

In the cochlea, TMEM43 shows a distinct expression pattern primarily in glia-like supporting cells (GLSs) rather than hair cells. At postnatal day 4 through P20, TMEM43 is mainly expressed in the organ of Corti, becoming more restricted to the apical membrane of inner border cells and cell junctions of inner sulcus cells by P20[jang-2021-ANSD-summary]. Expression persists in adult mice at 1, 2, and 4 months of age, and similar GLS-specific expression has been confirmed in adult primates corresponding to humans in their 40s[jang-2021-ANSD-summary].

In cardiac tissue, mouse studies revealed that Luma is sporadically expressed in cardiomyocytes throughout the heart but is highly and uniformly expressed in cardiac fibroblasts and vascular smooth muscle cells[stroud-2018-mouse-knockout-abstract]. This expression pattern suggests that TMEM43's primary cardiac function may involve non-cardiomyocyte cell populations or intercellular communication rather than intrinsic cardiomyocyte biology.

## Primary Molecular Function: Ion Channel Activity

Based on PubMed, recent electrophysiological studies have established TMEM43 as a bona fide ion channel with nonselective cation permeability. The channel is permeable to Na+, K+, and Cs+ ions and mediates passive conductance-like currents when expressed heterologously[kang-2024-TMEM-ion-channels-summary]. Several lines of evidence support its identity as a pore-forming channel: purified TMEM43 protein reconstituted into lipid bilayers displays stochastic single-channel openings, and gene silencing of TMEM43 eliminates carbenoxolone (CBX)-, gadolinium (Gd3+)-, and low pH-sensitive passive conductance currents in cochlear GLSs[kang-2024-TMEM-ion-channels-summary].

The channel displays sensitivity to extracellular pH, with current amplitude decreasing progressively as pH is lowered from 8 to 5.5[kang-2024-TMEM-ion-channels-summary]. This pH sensitivity is physiologically significant, as lowering the extracellular pH to 6 completely abolishes the passive conductance current in GLSs[jang-2021-ANSD-summary]. The channel is blocked by the nonselective cation channel inhibitor gadolinium chloride (GdCl3) and by carbenoxolone, a gap junction blocker[jang-2021-ANSD-summary].

A crucial aspect of TMEM43's ion channel function is its interaction with gap junction proteins. In the cochlea, TMEM43 interacts physically with Connexin26 (Cx26/GJB2) and Connexin30 (Cx30/GJB6), the two predominant connexins expressed in cochlear GLSs[jang-2021-ANSD-summary]. Co-immunoprecipitation assays demonstrated that both wild-type TMEM43 and the p.R372X mutant can be pulled down with either Cx26 or Cx30 when co-expressed in HEK293T cells. Duolink proximity ligation assays further confirmed close proximity (<40 nm) of TMEM43 and Cx26 in cochlear tissue[jang-2021-ANSD-summary].

TMEM43 also interacts with KCNK3 (TASK-1), a two-pore domain potassium (K2P) channel. The intracellular loop domain of TMEM43 is responsible for TASK-1 binding, suggesting a specific structural interface mediates this protein-protein interaction[jang-2021-TASK1-abstract]. Gene silencing of TMEM43 significantly reduces passive conductance current in GLSs, indicating that TMEM43 and its channel partners together mediate the background conductance essential for inner ear homeostasis[jang-2021-TASK1-abstract].

## Role in the LINC Complex and Mechanotransduction

TMEM43/LUMA is associated with the LINC complex, which mechanically links the nucleoskeleton to the cytoskeleton via the nuclear envelope[stroud-2018-mouse-knockout-abstract][meinke-2011-LINC-complex-abstract]. The LINC complex components include emerin, lamin A/C, SUN1, SUN2, nesprin-1, and nesprin-2, all of which interact at the nuclear envelope with additional binding partners including actin filaments and B-type lamins[meinke-2011-LINC-complex-abstract].

TMEM43 was identified as a binding partner of emerin and lamins through protein interaction studies[meinke-2011-LINC-complex-abstract]. Furthermore, Liang and colleagues demonstrated for the first time that LUMA can interact with SUN2, another nuclear membrane protein, in addition to emerin[liang-2011-EDMD-abstract]. Cells expressing mutant LUMA showed reduced nuclear staining with or without aggregates of emerin and SUN2, together with a higher proportion of abnormally shaped nuclei, indicating that proper LUMA function is required for normal nuclear envelope organization[liang-2011-EDMD-abstract].

A key mechanistic insight into TMEM43's role in mechanotransduction comes from atomic force microscopy studies of patient-derived cells. Milting and colleagues demonstrated that skin fibroblasts from individuals carrying the TMEM43 p.S358L ARVC5 mutation exhibit increased nuclear stiffness compared to wild-type controls[milting-2014-european-founder-abstract]. This increased nuclear stiffness is hypothesized to contribute to the massive loss of cardiomyocytes characteristic of ARVC hearts, as stiffer nuclei may be more susceptible to damage under the mechanical strain experienced by beating cardiomyocytes[milting-2014-european-founder-abstract].

## Role in Gap Junction Function and Intercellular Communication

In the cardiac context, the TMEM43 p.S358L mutation profoundly affects intercalated disc protein function. Siragam and colleagues demonstrated that stable expression of this mutation in HL-1 cardiac cells results in decreased expression of Zonula Occludens-1 (ZO-1) and loss of ZO-1 localization to cell-cell junctions[siragam-2014-ARVC-cell-abstract]. Junctional plakoglobin (JUP) and α-catenin proteins redistribute to the cytoplasm with decreased localization at cell-cell junctions. Critically, Connexin-43 (Cx43) phosphorylation is altered, gap junction dye transfer is reduced, and conduction velocity decreases in mutant TMEM43-transfected cells[siragam-2014-ARVC-cell-abstract]. These observations provide a direct mechanistic link between TMEM43 dysfunction and arrhythmogenesis through impaired gap junction communication.

In the cochlea, TMEM43's interaction with connexins is essential for maintaining the passive conductance current in GLSs. The passive current characteristics - sensitivity to CBX, Gd3+, and low pH - are consistent with gap junction-mediated ion flux, and gene silencing of TMEM43 dramatically reduces this current[jang-2021-ANSD-summary]. The p.R372X ANSD-causing mutation shows a dominant-negative effect, with heterozygous animals showing 63% reduction in passive conductance current compared to wild-type, while homozygous animals show 89% reduction[jang-2021-ANSD-summary].

## Involvement in Wnt/β-Catenin Signaling and Adipogenesis

An important aspect of ARVC pathogenesis involves the Wnt/β-catenin signaling pathway. According to Lombardi and Marian, the pathogenesis of fibro-fatty replacement in ARVC involves partial nuclear translocation of plakoglobin and subsequent suppression of canonical Wnt signaling[lombardi-2011-wnt-signaling-abstract]. Since Wnt signaling is involved in the development of the right ventricle and its outflow tract (the predominant sites of ARVC involvement), suppression of this pathway results in a switch to adipogenesis in second heart field progenitor cells[lombardi-2011-wnt-signaling-abstract].

The TMEM43 gene contains a response element for PPARγ (peroxisome proliferator-activated receptor gamma), an adipogenic transcription factor[merner-2008-ARVC5-abstract]. This finding provides a potential molecular explanation for the fibro-fatty replacement of myocardium that is a characteristic pathological finding in ARVC. Recent work has shown that the TMEM43 p.S358L mutation is associated with increased absorption of lipids, fatty acids, and cholesterol in the mouse small intestine, which may further promote fibro-fatty replacement of cardiac myocytes[orgil-2025-TMEM43-review-abstract].

## Role in Cancer Signaling: EGFR-NF-κB Pathway

Beyond its well-characterized roles in cardiac, auditory, and musculoskeletal function, TMEM43 has emerged as an important mediator of cancer signaling, particularly through the NF-κB pathway. Jiang and colleagues used a Bimolecular Fluorescence Complementation-based functional genomics method to perform high throughput screening and identified TMEM43/LUMA as a critical component in the EGFR signaling network[jiang-2017-cancer-NF-kB-abstract]. Their work revealed that following EGF stimulation, EGFR recruits TMEM43, which then interacts with the scaffold protein CARMA3 (CARD and MAGUK domain-containing protein 3) and its associated complex. This interaction induces downstream NF-κB activation and controls cell survival[jiang-2017-cancer-NF-kB-abstract].

TMEM43 deficiency profoundly affects cancer cell behavior, reducing colony formation, impairing survival of anoikis-induced cell death, and decreasing migration and invasion capabilities[jiang-2017-cancer-NF-kB-abstract]. Importantly, higher TMEM43 expression correlates with brain tumor malignancy, and suppression of TMEM43 in brain tumor cells inhibits tumor growth both in vitro and in vivo[jiang-2017-cancer-NF-kB-abstract]. These findings establish TMEM43 as a potential therapeutic target in EGFR-driven cancers.

The NF-κB connection extends to hepatocellular carcinoma (HCC), where Zhang and colleagues demonstrated that TMEM43 is highly expressed in HCC and promotes tumor development[zhang-2024-HCC-VDAC1-abstract]. Using RNA sequencing and The Cancer Genome Atlas databases, they identified an important regulatory relationship between TMEM43 and VDAC1 (voltage-dependent anion channel 1). TMEM43 affects HCC progression by regulating the ubiquitination level of VDAC1, with USP7 (ubiquitin-specific protease 7) participating in tumor growth through this TMEM43-dependent pathway[zhang-2024-HCC-VDAC1-abstract]. Absence of TMEM43 in cancer cells inhibits tumor development, suggesting that TMEM43 may have predictive value and represent a new treatment strategy for HCC[zhang-2024-HCC-VDAC1-abstract].

The cardiac relevance of NF-κB signaling was further highlighted by Gu and colleagues, who demonstrated that TMEM43 deficiency increases NF-κB activation in mouse hearts following pressure overload-induced hypertrophy[gu-2023-cardiac-hypertrophy-abstract]. In this context, TMEM43 appears to exert a protective role: reduced expression of TMEM43 during cardiac hypertrophy leads to worsening heart failure with deteriorating cardiac function, exacerbated hypertrophy, and increased fibrosis. Conversely, overexpression of TMEM43 in cardiomyocytes ameliorates the hypertrophic response and reduces NF-κB activation upon angiotensin II stimulation[gu-2023-cardiac-hypertrophy-abstract]. This suggests that TMEM43 may have context-dependent effects on NF-κB signaling, suppressing it in cardiac stress but mediating it in cancer cell proliferation.

## Role in Brain Function: Astrocytic Gap Junction Networks

An emerging area of TMEM43 research concerns its function in the central nervous system, particularly in astrocytes. Kim and colleagues characterized TMEM43 as a pH-sensing cation channel that conducts transjunctional potentials between adjacent cells, further facilitating electrical couplings of gap junctions[kim-2023-astrocyte-memory-preprint]. This work, which represents the first direct characterization of TMEM43 function in the brain, demonstrated that the protein actively participates in gap junction networks of the hippocampus.

Studies of TMEM43 knockout mice revealed several hippocampal abnormalities: decreased astrocytic dye diffusion indicating impaired gap junction communication, decreased potassium buffering capacity, and increased neuronal excitability[kim-2023-astrocyte-memory-preprint]. These physiological changes were accompanied by alterations in the AMPA/NMDA receptor ratio and disrupted long-term potentiation (LTP), a cellular mechanism considered the neural substrate of memory formation[kim-2023-astrocyte-memory-preprint].

Critically, the electrophysiological changes in knockout mice led to a disturbance in memory retrieval, which could be rescued by TMEM43 overexpression[kim-2023-astrocyte-memory-preprint]. These results indicate that TMEM43 actively participates in gap junction networks of the hippocampus to prevent neurons from hyperexcitability, which is critical for memory retrieval. This work expands our understanding of TMEM43 beyond its originally characterized roles in cardiac and auditory systems to include a fundamental function in cognitive processes.

## Disease Associations

### Arrhythmogenic Right Ventricular Cardiomyopathy Type 5 (ARVC5)

The p.S358L mutation in TMEM43 causes a fully penetrant, lethal form of arrhythmogenic cardiomyopathy. In the Newfoundland founder population, median life expectancy was 41 years in affected males compared to 71 years in affected females (relative risk 6.8), demonstrating significant sex influence on disease severity[merner-2008-ARVC5-abstract]. The mutation is of European origin, estimated to be 1300-1500 years old, and has been identified in families from Newfoundland, Germany, Denmark, the UK, and the USA, all sharing a common ancestral haplotype[milting-2014-european-founder-abstract].

Interestingly, germline Luma null mice are viable and exhibit normal cardiac function, and Luma S358L knock-in mice also display normal cardiac function and morphology[stroud-2018-mouse-knockout-abstract]. These findings suggest either species-specific differences in LUMA function or the requirement for additional factors to manifest the disease phenotype in mice, representing an important area for continued investigation.

### Emery-Dreifuss Muscular Dystrophy-Related Myopathy

Mutations in TMEM43 have been identified in patients with EDMD-related myopathy. Liang and colleagues identified two heterozygous missense mutations, p.E85K and p.I91V, in patients presenting with muscular dystrophy, joint contractures, and cardiomyopathy with conduction defects[liang-2011-EDMD-abstract]. The p.E85K mutation causes failure of LUMA oligomerization and reduces nuclear staining with aggregation of emerin and SUN2, leading to abnormally shaped nuclei[liang-2011-EDMD-abstract].

### Auditory Neuropathy Spectrum Disorder (ANSD)

The p.R372X nonsense mutation in TMEM43 causes autosomal dominant late-onset progressive ANSD, characterized by inability to discriminate speech despite preserved sensitivity to sound[jang-2021-ANSD-summary]. This mutation was identified in two large Asian families (Chinese and Korean) through linkage analysis and exome sequencing. Unlike the cardiac phenotype of the p.S358L mutation, ANSD patients with p.R372X show no cardiac abnormalities, demonstrating pleiotropy with mutation-specific phenotypes[jang-2021-ANSD-summary].

Knock-in mice with the p.R372X variant recapitulate progressive hearing loss with onset at 5-6 months of age (equivalent to human twenties). Morphological analysis reveals narrowed inner border cells in GLSs without significant hair cell loss or spiral ganglion neuron changes[jang-2021-ANSD-summary]. Based on the mechanistic understanding that the primary damage is restricted to GLSs rather than hair cells or neurons, cochlear implantation was successfully performed on affected patients, with rapid restoration of speech discrimination ability[jang-2021-ANSD-summary].

## Experimental Evidence Summary

The functions of TMEM43 have been established through multiple lines of experimental evidence:

1. **Genetic evidence**: Human mutations cause ARVC5, EDMD-related myopathy, and ANSD with clear genotype-phenotype correlations[merner-2008-ARVC5-abstract][liang-2011-EDMD-abstract][jang-2021-ANSD-summary]

2. **Biochemical evidence**: Co-immunoprecipitation and proximity ligation assays demonstrate physical interactions with emerin, lamins, SUN2, Cx26, Cx30, Cx43, and TASK-1[liang-2011-EDMD-abstract][jang-2021-ANSD-summary][jang-2021-TASK1-abstract]

3. **Electrophysiological evidence**: Whole-cell patch clamp recordings show TMEM43-dependent passive conductance currents in cochlear GLSs; single-channel recordings from reconstituted protein confirm pore-forming capability[kang-2024-TMEM-ion-channels-summary][jang-2021-ANSD-summary]

4. **Biophysical evidence**: Atomic force microscopy demonstrates increased nuclear stiffness in cells carrying the p.S358L mutation[milting-2014-european-founder-abstract]

5. **Animal model evidence**: Knock-in mice with p.R372X mutation recapitulate progressive hearing loss with GLS-specific morphological and electrophysiological defects[jang-2021-ANSD-summary]

6. **Cell biology evidence**: Mutant TMEM43 disrupts localization of intercalated disc proteins (ZO-1, plakoglobin, α-catenin), alters Cx43 phosphorylation, reduces gap junction dye transfer, and decreases conduction velocity[siragam-2014-ARVC-cell-abstract]

7. **Cancer biology evidence**: High throughput screening identified TMEM43 as critical for EGFR-induced NF-κB activation; TMEM43 knockdown inhibits tumor growth in vitro and in vivo[jiang-2017-cancer-NF-kB-abstract]; TMEM43 regulates VDAC1 ubiquitination in hepatocellular carcinoma[zhang-2024-HCC-VDAC1-abstract]

8. **Neurobiology evidence**: TMEM43 knockout mice show decreased astrocytic dye diffusion, impaired potassium buffering, increased neuronal excitability, altered LTP, and memory retrieval deficits that can be rescued by TMEM43 overexpression[kim-2023-astrocyte-memory-preprint]

## Open Questions

Several important questions regarding TMEM43 function remain unresolved:

1. **High-resolution structure**: No experimental three-dimensional structure of TMEM43 has been determined. Cryo-EM or crystal structure analysis is needed to understand the ion conduction pathway, gating mechanism, and interaction interfaces with partner proteins.

2. **Species-specific differences**: Why do Luma knockout mice and S358L knock-in mice show normal cardiac function while humans with the same mutation develop lethal cardiomyopathy? Are there modifier genes, environmental factors, or species-specific mechanical stresses that explain this discrepancy?

3. **Tissue-specific localization**: What determines whether TMEM43 localizes to the nuclear envelope, plasma membrane, or intercalated discs in different cell types? Are there tissue-specific post-translational modifications or binding partners?

4. **Ion channel versus scaffold function**: Is TMEM43's primary function as an ion channel, or does it serve primarily as a scaffold for gap junction protein complexes? Can these functions be separated genetically?

5. **Mutation-specific mechanisms**: Why do different TMEM43 mutations cause distinct diseases (cardiac vs. muscular vs. auditory phenotypes)? The p.S358L and p.R372X mutations affect different domains - how do their molecular effects differ?

6. **Late-onset progressive phenotype**: What triggers the progressive nature of both ARVC5 and ANSD? Is there age-dependent reduction in passive conductance current, accumulation of damage, or decline in compensatory mechanisms?

7. **Therapeutic opportunities**: Could TMEM43 or its interacting partners serve as therapeutic targets? The successful cochlear implantation in ANSD patients suggests that understanding cellular pathology can guide treatment - are there analogous approaches for cardiac disease?

8. **Context-dependent NF-κB effects**: How does TMEM43 suppress NF-κB activation in cardiomyocytes under stress while mediating EGFR-induced NF-κB activation in cancer cells? Are there tissue-specific interacting partners or post-translational modifications that determine this functional switch?

9. **Cancer therapeutic potential**: Given that TMEM43 knockdown inhibits tumor growth and its expression correlates with tumor malignancy, could TMEM43 inhibitors be developed as cancer therapeutics? What would be the cardiac side effects given TMEM43's protective role in cardiac hypertrophy?

10. **Cognitive function in disease**: Do patients with ARVC5 or other TMEM43 mutations exhibit subtle cognitive or memory deficits? The hippocampal findings from mouse studies suggest potential CNS effects that have not been systematically evaluated in human patients.

## References

* **merner-2008-ARVC5**: Merner ND, Hodgkinson KA, Haywood AFM, et al. Arrhythmogenic right ventricular cardiomyopathy type 5 is a fully penetrant, lethal arrhythmic disorder caused by a missense mutation in the TMEM43 gene. *Am J Hum Genet*. 2008;82(4):809-21. PMID: 18313022. DOI: [10.1016/j.ajhg.2008.01.010](https://doi.org/10.1016/j.ajhg.2008.01.010)

* **jang-2021-ANSD**: Jang MW, Oh DY, Yi E, et al. A nonsense TMEM43 variant leads to disruption of connexin-linked function and autosomal dominant auditory neuropathy spectrum disorder. *Proc Natl Acad Sci USA*. 2021;118(22):e2019681118. PMID: 34050020. DOI: [10.1073/pnas.2019681118](https://doi.org/10.1073/pnas.2019681118)

* **kang-2024-TMEM-ion-channels**: Kang H, Lee CJ. Transmembrane proteins with unknown function (TMEMs) as ion channels: electrophysiological properties, structure, and pathophysiological roles. *Exp Mol Med*. 2024;56(4):850-860. PMID: 38556553. DOI: [10.1038/s12276-024-01206-1](https://doi.org/10.1038/s12276-024-01206-1)

* **liang-2011-EDMD**: Liang WC, Mitsuhashi H, Keduka E, et al. TMEM43 mutations in Emery-Dreifuss muscular dystrophy-related myopathy. *Ann Neurol*. 2011;69(6):1005-13. PMID: 21391237. DOI: [10.1002/ana.22338](https://doi.org/10.1002/ana.22338)

* **franke-2014-intercalated-disc**: Franke WW, Dörflinger Y, Kuhn C, et al. Protein LUMA is a cytoplasmic plaque constituent of various epithelial adherens junctions and composite junctions of myocardial intercalated disks. *Cell Tissue Res*. 2014;357(1):159-72. PMID: 24770932. DOI: [10.1007/s00441-014-1865-1](https://doi.org/10.1007/s00441-014-1865-1)

* **stroud-2018-mouse-knockout**: Stroud MJ, Fang X, Zhang J, et al. Luma is not essential for murine cardiac development and function. *Cardiovasc Res*. 2018;114(3):378-388. PMID: 29040414. DOI: [10.1093/cvr/cvx205](https://doi.org/10.1093/cvr/cvx205)

* **siragam-2014-ARVC-cell**: Siragam V, Cui X, Masse S, et al. TMEM43 mutation p.S358L alters intercalated disc protein expression and reduces conduction velocity in arrhythmogenic right ventricular cardiomyopathy. *PLoS One*. 2014;9(10):e109128. PMID: 25343256. DOI: [10.1371/journal.pone.0109128](https://doi.org/10.1371/journal.pone.0109128)

* **meinke-2011-LINC-complex**: Meinke P, Nguyen TD, Wehnert MS. The LINC complex and human disease. *Biochem Soc Trans*. 2011;39(6):1693-7. PMID: 22103509. DOI: [10.1042/BST20110658](https://doi.org/10.1042/BST20110658)

* **milting-2014-european-founder**: Milting H, Klauke B, Christensen AH, et al. The TMEM43 Newfoundland mutation p.S358L causing ARVC-5 was imported from Europe and increases the stiffness of the cell nucleus. *Eur Heart J*. 2014;36(14):872-81. PMID: 24598986. DOI: [10.1093/eurheartj/ehu077](https://doi.org/10.1093/eurheartj/ehu077)

* **jang-2021-TASK1**: Jang MW, Kim TY, Sharma K, et al. A Deafness Associated Protein TMEM43 Interacts with KCNK3 (TASK-1) Two-pore Domain K(K2P) Channel in the Cochlea. *Exp Neurobiol*. 2021;30(5):319-328. PMID: 34737237. DOI: [10.5607/en21028](https://doi.org/10.5607/en21028)

* **lombardi-2011-wnt-signaling**: Lombardi R, Marian AJ. Molecular genetics and pathogenesis of arrhythmogenic right ventricular cardiomyopathy: a disease of cardiac stem cells. *Pediatr Cardiol*. 2011;32(3):360-5. PMID: 21267716. DOI: [10.1007/s00246-011-9890-2](https://doi.org/10.1007/s00246-011-9890-2)

* **orgil-2025-TMEM43-review**: Orgil BO, Spaulding MS, Smith HP, et al. Transmembrane Protein 43: Molecular and Pathogenetic Implications in Arrhythmogenic Cardiomyopathy and Various Other Diseases. *Int J Mol Sci*. 2025;26(14):6856. PMID: 40725103. DOI: [10.3390/ijms26146856](https://doi.org/10.3390/ijms26146856)

* **jiang-2017-cancer-NF-kB**: Jiang C, Zhu Y, Zhou Z, et al. TMEM43/LUMA is a key signaling component mediating EGFR-induced NF-κB activation and tumor progression. *Oncogene*. 2017;36(20):2813-2823. PMID: 27991920. DOI: [10.1038/onc.2016.430](https://doi.org/10.1038/onc.2016.430)

* **zhang-2024-HCC-VDAC1**: Zhang N, Wang F, Yang X, et al. TMEM43 promotes the development of hepatocellular carcinoma by activating VDAC1 through USP7 deubiquitination. *Transl Gastroenterol Hepatol*. 2024;9:9. PMID: 38317750. PMCID: PMC10838614. DOI: [10.21037/tgh-23-108](https://doi.org/10.21037/tgh-23-108)

* **gu-2023-cardiac-hypertrophy**: Gu Y, Yao YR, Ding Y, Zhang XW. Reduced expression of transmembrane protein 43 during cardiac hypertrophy leads to worsening heart failure in mice. *Exp Biol Med*. 2023;248(17):1437-1445. PMID: 37697676. PMCID: PMC10666727. DOI: [10.1177/15353702231191111](https://doi.org/10.1177/15353702231191111)

* **kim-2023-astrocyte-memory**: Kim TY, Bhattacharya A, et al. Astrocytic Gapjinc (TMEM43) modulates gap junction networks by facilitating transjunctional potentials. *bioRxiv preprint*. 2023. URL: [https://www.biorxiv.org/content/10.1101/2022.11.08.515259v2](https://www.biorxiv.org/content/10.1101/2022.11.08.515259v2) (Note: preprint, not yet peer-reviewed)


## Citations

1. franke-2014-intercalated-disc-abstract.md
2. gu-2023-cardiac-hypertrophy-abstract.md
3. hodgkinson-2012-natural-history-abstract.md
4. jang-2021-ANSD-summary.md
5. jang-2021-TASK1-abstract.md
6. jiang-2017-cancer-NF-kB-abstract.md
7. kang-2024-TMEM-ion-channels-summary.md
8. kim-2023-astrocyte-memory-preprint.md
9. liang-2011-EDMD-abstract.md
10. lombardi-2011-wnt-signaling-abstract.md
11. meinke-2011-LINC-complex-abstract.md
12. merner-2008-ARVC5-abstract.md
13. milting-2014-european-founder-abstract.md
14. orgil-2025-TMEM43-review-abstract.md
15. siragam-2014-ARVC-cell-abstract.md
16. stroud-2018-mouse-knockout-abstract.md
17. zhang-2024-HCC-VDAC1-abstract.md
18. zink-2022-zebrafish-abstract.md