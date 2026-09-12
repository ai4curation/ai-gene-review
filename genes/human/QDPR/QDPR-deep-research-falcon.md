---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T14:56:24.833079'
end_time: '2026-07-05T15:25:56.164697'
duration_seconds: 1771.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: QDPR
  gene_symbol: QDPR
  uniprot_accession: P09417
  protein_description: 'RecName: Full=Dihydropteridine reductase; EC=1.5.1.34 {ECO:0000269|PubMed:3033643,
    ECO:0000269|PubMed:8262916}; AltName: Full=HDHPR; AltName: Full=Quinoid dihydropteridine
    reductase; AltName: Full=Short chain dehydrogenase/reductase family 33C member
    1;'
  gene_info: Name=QDPR; Synonyms=DHPR, SDR33C1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the short-chain dehydrogenases/reductases (SDR)
  protein_domains: NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR_fam.
    (IPR002347); adh_short (PF00106)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: QDPR-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P09417
- **Protein Description:** RecName: Full=Dihydropteridine reductase; EC=1.5.1.34 {ECO:0000269|PubMed:3033643, ECO:0000269|PubMed:8262916}; AltName: Full=HDHPR; AltName: Full=Quinoid dihydropteridine reductase; AltName: Full=Short chain dehydrogenase/reductase family 33C member 1;
- **Gene Information:** Name=QDPR; Synonyms=DHPR, SDR33C1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR_fam. (IPR002347); adh_short (PF00106)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "QDPR" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'QDPR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **QDPR** (gene ID: QDPR, UniProt: P09417) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P09417
- **Protein Description:** RecName: Full=Dihydropteridine reductase; EC=1.5.1.34 {ECO:0000269|PubMed:3033643, ECO:0000269|PubMed:8262916}; AltName: Full=HDHPR; AltName: Full=Quinoid dihydropteridine reductase; AltName: Full=Short chain dehydrogenase/reductase family 33C member 1;
- **Gene Information:** Name=QDPR; Synonyms=DHPR, SDR33C1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR_fam. (IPR002347); adh_short (PF00106)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "QDPR" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'QDPR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **QDPR** (gene ID: QDPR, UniProt: P09417) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: QDPR (Dihydropteridine Reductase) — Human Gene Functional Annotation

## 1. Gene and Protein Identity

The human *QDPR* gene (synonyms: *DHPR*, *SDR33C1*; UniProt: P09417) encodes **quinoid dihydropteridine reductase** (DHPR), classified under EC 1.5.1.34. The gene is located on **chromosome 4p15.3**, spans over 20 kb, and contains 732 bp of coding sequence distributed across seven exons (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13). DHPR belongs to the **short-chain dehydrogenases/reductases (SDR) family** and contains a characteristic Rossmann-type dinucleotide-binding fold (varughese1992crystalstructureof pages 1-2, pierson2018discoveryofnovel pages 27-31).

The following table provides a consolidated summary of QDPR's key properties:

| Property | Summary |
|---|---|
| Gene name | **QDPR**; synonyms **DHPR**, **SDR33C1** (eichwald2023tetrahydrobiopterinbeyondits pages 9-10, opladen2020consensusguidelinefor pages 1-2) |
| Protein name | **Dihydropteridine reductase**; also called **quinoid dihydropteridine reductase** / **DHPR** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12) |
| UniProt ID | **P09417** (user-provided target identity) |
| EC number | **EC 1.5.1.34** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12) |
| Molecular weight | Monomer ~**25–26 kDa**; native enzyme ~**50–52 kDa** (homodimer) (cutler1986dihydropteridinereductase pages 58-64, breuer2018characterizingthefunction pages 19-24) |
| Quaternary structure | **Homodimer**; dimer interface formed by a **four-helix bundle**; Rossmann-type dinucleotide fold in each protomer (varughese1992crystalstructureof pages 4-5, varughese1992crystalstructureof pages 1-2, cutler1986dihydropteridinereductase pages 58-64) |
| Cofactor | Primarily **NADH**; NADPH can support activity in some in vitro settings but is much less efficient, with strong NADH preference (~160-fold in a characterized homolog) (cutler1986dihydropteridinereductase pages 58-64, lye2002characterizationofquinonoiddihydropteridine pages 6-7, pierson2018discoveryofnovel pages 27-31) |
| Substrate | Physiologic substrate is **quinonoid dihydrobiopterin (qBH2)** / quinonoid dihydropteridines; enzyme tolerates several substituted quinonoid pteridines (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12, varughese1992crystalstructureof pages 4-5, cutler1986dihydropteridinereductase pages 58-64) |
| Product | **Tetrahydrobiopterin (BH4)** plus **NAD+** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12) |
| Reaction type | **NADH-dependent oxidoreductase** reaction in BH4 recycling: qBH2 + NADH + H+ → BH4 + NAD+; reaction proceeds by direct hydride transfer and is effectively irreversible under physiologic conditions (cutler1986dihydropteridinereductase pages 58-64, thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12) |
| Kinetic/mechanistic properties | **Ordered bi-bi** mechanism: NADH binds first, then qBH2; **pro-S hydride** transferred from the B-face of NADH to substrate N5; **free sulfhydryl groups** required; example kinetic constants from a well-characterized homolog: **Km(NADH) 23.1 ± 3.8 μM**, **Km(qDMPH2) 36.5 ± 7.1 μM** (cutler1986dihydropteridinereductase pages 58-64, lye2002characterizationofquinonoiddihydropteridine pages 6-7, pierson2018discoveryofnovel pages 27-31) |
| Tissue distribution | Widely distributed in animal tissues including **brain, adrenal medulla, heart, and lung**; functionally important in **CNS and liver**; recent work also identifies strong enrichment in **myelinating oligodendrocytes/myelin** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13, breuer2018characterizingthefunction pages 19-24, siems2025developmentalmaturationand pages 6-8) |
| Subcellular localization | Predominantly **cytosolic** enzyme in BH4 recycling; in CNS myelin studies, QDPR localizes to oligodendrocyte cell bodies and the **adaxonal non-compact compartment of myelin** (siems2025developmentalmaturationand pages 6-8, siems2025developmentalmaturationand pages 8-9) |
| Pathway | **Tetrahydrobiopterin (BH4) regeneration/recycling** pathway: after BH4 is oxidized during aromatic amino acid hydroxylation, **PCD/PCBD1** generates qBH2 and **QDPR** reduces qBH2 back to BH4; this sustains **PAH, TH, TPH**, and influences **NOS**-related BH4 homeostasis (breuer2018characterizingthefunction pages 15-19, eichwald2023tetrahydrobiopterinbeyondits pages 5-7, crabtree2011synthesisandrecycling pages 3-4) |
| Primary biological function | Maintains intracellular **BH4 availability**, thereby supporting **phenylalanine hydroxylation**, **dopamine/serotonin biosynthesis**, and nitric-oxide-related biopterin balance (breuer2018characterizingthefunction pages 15-19, breuer2018characterizingthefunction pages 19-24, eichwald2023tetrahydrobiopterinbeyondits pages 5-7) |
| Additional/putative functions | Literature suggests DHPR may help preserve **tetrahydrofolate** levels in brain where DHFR is low; secondary **ferric reductase** activity has been reported in nonhuman systems, but its physiologic importance in human QDPR remains unclear (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13, lye2002characterizationofquinonoiddihydropteridine pages 6-7) |
| Disease associations | **Dihydropteridine reductase deficiency (DHPRD)** / BH4-deficient hyperphenylalaninemia: causes **hyperphenylalaninemia**, **dopamine and serotonin deficiency**, developmental delay, hypotonia, dystonia, seizures, microcephaly, and severe neurologic disease; DHPRD accounts for about **33% of HPA-associated BH4 deficiencies** in one consensus guideline (eichwald2023tetrahydrobiopterinbeyondits pages 9-10, opladen2020consensusguidelinefor pages 1-2, opladen2020consensusguidelinefor pages 6-7) |
| Emerging disease links | Reduced or dysregulated QDPR/BH4 recycling has been linked to **tumor biology**: decreased QDPR expression in **colorectal cancer** is associated with a lower BH4:BH2 ratio and NOS uncoupling; QDPR loss has also been implicated in **pancreatic cancer immune suppression** in later literature summaries (alam2023uncouplednitricoxide pages 1-2, yan2026overcomingmultidimensionalimmunotherapy pages 5-6) |
| Chromosomal location | **Chromosome 4p15.3**; human gene spans **>20 kb** with **7 exons** and **732 bp coding sequence** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13) |


*Table: This table summarizes the core biochemical, structural, localization, pathway, and disease-related properties of human QDPR/dihydropteridine reductase. It is useful as a compact reference for functional annotation of UniProt P09417.*

## 2. Enzymatic Reaction and Substrate Specificity

DHPR catalyzes the **NADH-dependent reduction of quinonoid dihydrobiopterin (q-BH2) to tetrahydrobiopterin (BH4)**, a reaction that is central to the regeneration of this essential cofactor. The overall reaction is:

**q-BH2 + NADH + H⁺ → BH4 + NAD⁺**

The enzyme exhibits **ordered bi-bi kinetics**: NADH binds first to form an enzyme–NADH complex, followed by binding of the quinonoid dihydropterin substrate. Products are released in the order BH4 first, then NAD⁺ (cutler1986dihydropteridinereductase pages 58-64, pierson2018discoveryofnovel pages 27-31). The reaction is essentially irreversible under physiological conditions due to differences in reduction potentials (cutler1986dihydropteridinereductase pages 58-64).

DHPR displays a strong cofactor preference for **NADH over NADPH**, with approximately 160-fold higher efficiency with NADH (lye2002characterizationofquinonoiddihydropteridine pages 6-7). The enzyme transfers the **pro-S hydrogen from the B-face of the NADH nicotinamide ring** to the **N5 position of q-BH2** (cutler1986dihydropteridinereductase pages 58-64, thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12, pierson2018discoveryofnovel pages 27-31). Kinetic parameters determined for a well-characterized homolog include Km(NADH) = 23.1 ± 3.8 μM and Km(qDMPH₂) = 36.5 ± 7.1 μM, with a Vmax of 2550 ± 145 μmol/min/mg protein (lye2002characterizationofquinonoiddihydropteridine pages 6-7). The enzyme requires **free sulfhydryl groups** for activity and does not contain detectable prosthetic groups such as flavin or metal ions (cutler1986dihydropteridinereductase pages 58-64, thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12).

DHPR is relatively **substrate-tolerant with respect to quinonoid dihydropterins**, accepting various 2-substituted and 6-substituted dihydropteridine analogs, though it exhibits very low activity toward non-quinonoid pteridines (approximately 66,000-fold lower activity with H₂B compared to quinonoid substrates) (lye2002characterizationofquinonoiddihydropteridine pages 6-7, lye2002characterizationofquinonoiddihydropteridine pages 1-1, varughese1992crystalstructureof pages 4-5). Methotrexate acts as a competitive inhibitor with respect to the pterin substrate, while NAD⁺ is a competitive inhibitor with respect to NADH (cutler1986dihydropteridinereductase pages 58-64). A secondary **NADH-dependent ferric reductase activity** has been described, though at much lower specific activity than the primary reaction (lye2002characterizationofquinonoiddihydropteridine pages 6-7).

## 3. Protein Structure

The crystal structure of DHPR was solved at 2.3 Å resolution from rat liver, revealing an **α/β protein with a central β-sheet** (strands A–H) flanked by major α-helices (varughese1992crystalstructureof pages 4-5, varughese1992crystalstructureof pages 1-2). The enzyme functions as a **homodimer** with a total molecular weight of approximately 50–52 kDa, comprising two identical subunits of ~25–26 kDa each (cutler1986dihydropteridinereductase pages 58-64). The dimer interface is stabilized by a **four-helix bundle** motif composed of two α-helices (αE and αF) contributed by each protomer, with an unusual right-handed twist (varughese1992crystalstructureof pages 4-5, varughese1992crystalstructureof pages 1-2).

The active site is a **U-shaped surface channel** formed by three extended loops connecting β-strands D–E, E–F, and F–G, located at the carboxyl-terminal edge of the dinucleotide fold (varughese1992crystalstructureof pages 4-5). Within this cleft, the quinonoid substrate binds in a **stacked configuration** between the nicotinamide ring of the NADH cofactor and the indole side chain of **Trp-86**, positioning the pteridine ring nearly parallel to the nicotinamide plane. The N5 of q-BH2 is positioned approximately **3.4 Å from the C4 of bound nicotinamide**, enabling direct hydride transfer (varughese1992crystalstructureof pages 4-5). Structurally, DHPR is distinct from dihydrofolate reductase and more closely resembles NAD-requiring flavin-dependent enzymes such as glutathione reductase, despite lacking flavin prosthetic groups (varughese1992crystalstructureof pages 1-2).

## 4. Biochemical Pathway Context: BH4 Recycling

DHPR functions as the terminal enzyme of the **tetrahydrobiopterin (BH4) recycling pathway**. BH4 is an essential cofactor for three aromatic amino acid hydroxylases—**phenylalanine hydroxylase (PAH)**, **tyrosine hydroxylase (TH)**, and **tryptophan hydroxylase (TPH)**—as well as **nitric oxide synthase (NOS)** and alkylglycerol monooxygenase (breuer2018characterizingthefunction pages 15-19, breuer2018characterizingthefunction pages 19-24, eichwald2023tetrahydrobiopterinbeyondits pages 5-7).

During hydroxylase-catalyzed reactions, BH4 donates electrons and is oxidized to **pterin-4a-carbinolamine**. This intermediate is first dehydrated by **pterin-4a-carbinolamine dehydratase (PCD/PCBD1)** to yield **quinonoid dihydrobiopterin (q-BH2)**. DHPR then catalyzes the final recycling step, reducing q-BH2 back to BH4 using NADH (pierson2018discoveryofnovel pages 14-18, eichwald2023tetrahydrobiopterinbeyondits pages 5-7, crabtree2011synthesisandrecycling pages 3-4). This recycling is critical because BH4 must be continuously regenerated to sustain the catalytic cycles of the hydroxylases and NOS. If q-BH2 is not rapidly reduced by DHPR, it can undergo non-enzymatic rearrangement to 7,8-dihydrobiopterin (BH2), which must then be salvaged by dihydrofolate reductase (DHFR) through an alternative, less efficient pathway (breuer2018characterizingthefunction pages 15-19).

By maintaining BH4 homeostasis, DHPR indirectly supports:
- **Phenylalanine metabolism** (via PAH: phenylalanine → tyrosine)
- **Dopamine biosynthesis** (via TH: tyrosine → L-DOPA)
- **Serotonin biosynthesis** (via TPH: tryptophan → 5-hydroxytryptophan)
- **Nitric oxide production** (via NOS)

Additionally, DHPR may contribute to maintaining **tetrahydrofolate levels** in the brain, where DHFR concentrations are low, suggesting a secondary role in folate metabolism (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13).

## 5. Subcellular Localization and Tissue Expression

DHPR is a **cytosolic enzyme** that is widely distributed across mammalian tissues. It is found at relatively high levels in **brain, adrenal medulla, heart, and lung** (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13). Its presence in brain and adrenal medulla is consistent with its role in supporting tyrosine and tryptophan hydroxylation. However, its abundance in tissues with minimal aromatic amino acid hydroxylase activity, such as heart and lung, suggests additional metabolic functions that remain incompletely understood (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13).

A landmark recent finding by Siems et al. (2025) demonstrated that QDPR is a **highly specific marker for mature myelinating oligodendrocytes and CNS myelin**. Using quantitative mass spectrometry of purified myelin fractions, the study showed that QDPR abundance increases markedly during developmental maturation of myelin (between postnatal day 18 and P75) and remains stable thereafter (siems2025developmentalmaturationand pages 6-8, siems2025developmentalmaturationand pages 1-2). Immunohistochemistry confirmed that over 95% of QDPR-positive cells co-express the oligodendrocyte marker CA2 in both corpus callosum and cortex (siems2025developmentalmaturationand pages 6-8). Ultrastructural analysis by immunogold electron microscopy revealed that QDPR localizes specifically to the **adaxonal, non-compact compartment of CNS myelin** (siems2025developmentalmaturationand pages 6-8, siems2025developmentalmaturationand pages 8-9). This expression pattern is conserved between mouse and human myelinating oligodendrocytes (siems2025developmentalmaturationand pages 8-9, siems2025developmentalmaturationand pages 4-6). The functional significance of QDPR in oligodendrocytes likely relates to its role in monoamine metabolism, with mice lacking QDPR developing hyperphenylalaninemia, brain monoamine deficiency, and enhanced fear responses (siems2025developmentalmaturationand pages 11-12).

## 6. Clinical Significance: QDPR Deficiency

**Dihydropteridine reductase deficiency (DHPRD)** is an autosomal recessive disorder that accounts for approximately **33% of hyperphenylalaninemia (HPA)-associated BH4 deficiencies**, making it the second most common form after 6-pyruvoyltetrahydropterin synthase (PTPS) deficiency (opladen2020consensusguidelinefor pages 1-2). The severe form predominates (267 of 303 reported patients) and represents one of the most devastating BH4 deficiency disorders (eichwald2023tetrahydrobiopterinbeyondits pages 9-10).

Clinical manifestations of DHPRD include **progressive mental retardation** secondary to extensive neuronal loss, **hypotonia**, **developmental delay**, **movement disorders** (particularly dystonia), and **parkinsonism/hypokinetic rigid syndrome** in approximately 10% of patients (opladen2020consensusguidelinefor pages 6-7). A distinctive feature is the high susceptibility to **epileptic seizures** compared to other BH4 disorders. Up to **25% of DHPRD patients present with microcephaly**, a notably higher frequency than in other BH4 deficiencies (opladen2020consensusguidelinefor pages 6-7). Additional neuropathological findings include **basal ganglia calcification**, abnormal vascular proliferation in the brain, and risk of **sudden death** (eichwald2023tetrahydrobiopterinbeyondits pages 9-10).

The pathophysiology centers on severe depletion of monoamine neurotransmitters (dopamine, serotonin, norepinephrine) in the CNS, reflected by decreased levels of their metabolites **homovanillic acid (HVA)** and **5-hydroxyindoleacetic acid (5-HIAA)** in cerebrospinal fluid (breuer2018characterizingthefunction pages 19-24, opladen2020consensusguidelinefor pages 1-2). Treatment involves supplementation with neurotransmitter precursors (**L-DOPA with a decarboxylase inhibitor** and **5-hydroxytryptophan**), **folinic acid**, and a **phenylalanine-restricted diet** (eichwald2023tetrahydrobiopterinbeyondits pages 9-10). Recent research has demonstrated that DHPR patient-derived iPSCs can be rescued using CRISPR/Cas9 gene therapy, restoring normal BH4 and tyrosine hydroxylase protein levels in differentiated cells (breuer2018characterizingthefunction pages 19-24).

## 7. Emerging Roles in Cancer and Other Diseases

Recent research has expanded understanding of QDPR beyond inherited metabolic disease into oncology and metabolic disorders.

**Colorectal cancer:** Alam et al. (2023) reported that human stage 1 colon tumors exhibit significantly **decreased QDPR expression**, leading to a reduced BH4:BH2 ratio and **uncoupled nitric oxide synthase (NOS) activity**. This uncoupling generates increased reactive oxygen/nitrogen species that promote pro-inflammatory and proliferative pathways driving cancer progression. Treatment with sepiapterin, which restores the BH4:BH2 ratio, inhibited colon cancer cell proliferation and reduced tumor growth in mouse models (alam2023uncouplednitricoxide pages 1-2).

**Pancreatic cancer:** In pancreatic ductal adenocarcinoma (PDAC), **QDPR knockout** in mouse models led to accumulation of BH2, reduced BH4/BH2 ratios, and resistance to immune checkpoint blockade, indicating that QDPR deficiency creates an immunosuppressive tumor microenvironment (yan2026overcomingmultidimensionalimmunotherapy pages 5-6).

**Type 2 diabetes and diabetic kidney disease:** A recent study identified the **QDPR rs3733570 polymorphism** as potentially associated with increased susceptibility to type 2 diabetes mellitus and, in the presence of dyslipidemia, to diabetic kidney disease in the Chinese Han population, further underscoring the broader metabolic relevance of BH4 homeostasis maintained by QDPR.

**Traumatic brain injury:** Bioinformatics and molecular studies have identified QDPR as a key gene associated with oxidative stress in TBI, with overexpression of QDPR confirmed in TBI models by RT-qPCR and Western blot.

## 8. Summary

QDPR encodes dihydropteridine reductase, the essential terminal enzyme of the tetrahydrobiopterin (BH4) recycling pathway. Through its NADH-dependent reduction of quinonoid dihydrobiopterin back to BH4, DHPR maintains the availability of this critical cofactor for aromatic amino acid hydroxylases (PAH, TH, TPH) and nitric oxide synthase. The enzyme is a cytosolic homodimer of the SDR family with a well-characterized crystal structure featuring a Rossmann fold and a U-shaped active site channel. DHPR is broadly expressed across tissues, with particular importance in the brain for neurotransmitter synthesis and newly recognized enrichment in myelinating oligodendrocytes. Its deficiency causes a severe neurometabolic disorder characterized by hyperphenylalaninemia and monoamine neurotransmitter depletion, while emerging evidence implicates QDPR dysregulation in cancer biology, where reduced QDPR expression contributes to NOS uncoupling and immune evasion in the tumor microenvironment.

References

1. (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13): Beat THÖNY, Günter AUERBACH, and Nenad BLAU. Tetrahydrobiopterin biosynthesis, regeneration and functions. The Biochemical journal, 347 Pt 1:1-16, Apr 2000. URL: https://doi.org/10.1042/bj3470001, doi:10.1042/bj3470001. This article has 1116 citations.

2. (varughese1992crystalstructureof pages 1-2): K. Varughese, Matthew M. Skinner, John M. WHITELEYt, David A. MATrHEWS, and N. Xuong. Crystal structure of rat liver dihydropteridine reductase. Proceedings of the National Academy of Sciences of the United States of America, 89 13:6080-4, Jul 1992. URL: https://doi.org/10.1073/pnas.89.13.6080, doi:10.1073/pnas.89.13.6080. This article has 210 citations and is from a highest quality peer-reviewed journal.

3. (pierson2018discoveryofnovel pages 27-31): Yann Mathieu Pierson. Discovery of novel competitive dihydropteridine reductase inhibitors via high throughput screening and their effect on metabolic pterin balance of fibroblast. ArXiv, Jan 2018. URL: https://doi.org/10.5075/epfl-thesis-8371, doi:10.5075/epfl-thesis-8371. This article has 0 citations.

4. (eichwald2023tetrahydrobiopterinbeyondits pages 9-10): Tuany Eichwald, Lucila de Bortoli da da Silva, Ananda Christina Staats Staats Pires, Laís Niero, Erick Schnorrenberger, Clovis Colpani Filho, Gisele Espíndola, Wei-Lin Huang, Gilles J. Guillemin, José E. Abdenur, and Alexandra Latini. Tetrahydrobiopterin: beyond its traditional role as a cofactor. Antioxidants, 12:1037, May 2023. URL: https://doi.org/10.3390/antiox12051037, doi:10.3390/antiox12051037. This article has 92 citations.

5. (opladen2020consensusguidelinefor pages 1-2): Thomas Opladen, Eduardo López-Laso, Elisenda Cortès-Saladelafont, Toni S. Pearson, H. Serap Sivri, Yilmaz Yildiz, Birgit Assmann, Manju A. Kurian, Vincenzo Leuzzi, Simon Heales, Simon Pope, Francesco Porta, Angeles García-Cazorla, Tomáš Honzík, Roser Pons, Luc Regal, Helly Goez, Rafael Artuch, Georg F. Hoffmann, Gabriella Horvath, Beat Thöny, Sabine Scholl-Bürgi, Alberto Burlina, Marcel M. Verbeek, Mario Mastrangelo, Jennifer Friedman, Tessa Wassenberg, Kathrin Jeltsch, Jan Kulhánek, and Oya Kuseyri Hübschmann. Consensus guideline for the diagnosis and treatment of tetrahydrobiopterin (bh4) deficiencies. Orphanet Journal of Rare Diseases, May 2020. URL: https://doi.org/10.1186/s13023-020-01379-8, doi:10.1186/s13023-020-01379-8. This article has 182 citations and is from a peer-reviewed journal.

6. (thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12): Beat THÖNY, Günter AUERBACH, and Nenad BLAU. Tetrahydrobiopterin biosynthesis, regeneration and functions. The Biochemical journal, 347 Pt 1:1-16, Apr 2000. URL: https://doi.org/10.1042/bj3470001, doi:10.1042/bj3470001. This article has 1116 citations.

7. (cutler1986dihydropteridinereductase pages 58-64): Dihydropteridine reductase This article has 1 citations.

8. (breuer2018characterizingthefunction pages 19-24): Maximilian Breuer. Characterizing the function and role of three dihydropteridine reductase homologs qdpra, qdprb1 and qdprb2 in the embryonic development of danio rerio. Text, Jan 2018. URL: https://doi.org/10.11588/heidok.00024357, doi:10.11588/heidok.00024357. This article has 0 citations and is from a peer-reviewed journal.

9. (varughese1992crystalstructureof pages 4-5): K. Varughese, Matthew M. Skinner, John M. WHITELEYt, David A. MATrHEWS, and N. Xuong. Crystal structure of rat liver dihydropteridine reductase. Proceedings of the National Academy of Sciences of the United States of America, 89 13:6080-4, Jul 1992. URL: https://doi.org/10.1073/pnas.89.13.6080, doi:10.1073/pnas.89.13.6080. This article has 210 citations and is from a highest quality peer-reviewed journal.

10. (lye2002characterizationofquinonoiddihydropteridine pages 6-7): Lon-Fye Lye, Mark L. Cunningham, and Stephen M. Beverley. Characterization of quinonoid-dihydropteridine reductase (qdpr) from the lower eukaryote leishmania major *. The Journal of Biological Chemistry, 277:38245-38253, Oct 2002. URL: https://doi.org/10.1074/jbc.m206543200, doi:10.1074/jbc.m206543200. This article has 37 citations.

11. (siems2025developmentalmaturationand pages 6-8): Sophie B. Siems, Vasiliki‐Ilya Gargareta, Leonie C. Schadt, Vinicius Daguano Gastaldi, Ramona B. Jung, Lars Piepkorn, Patrizia Casaccia, Ting Sun, Olaf Jahn, and Hauke B. Werner. Developmental maturation and regional heterogeneity but no sexual dimorphism of the murine cns myelin proteome. Glia, 73:38-56, Sep 2025. URL: https://doi.org/10.1002/glia.24614, doi:10.1002/glia.24614. This article has 12 citations and is from a domain leading peer-reviewed journal.

12. (siems2025developmentalmaturationand pages 8-9): Sophie B. Siems, Vasiliki‐Ilya Gargareta, Leonie C. Schadt, Vinicius Daguano Gastaldi, Ramona B. Jung, Lars Piepkorn, Patrizia Casaccia, Ting Sun, Olaf Jahn, and Hauke B. Werner. Developmental maturation and regional heterogeneity but no sexual dimorphism of the murine cns myelin proteome. Glia, 73:38-56, Sep 2025. URL: https://doi.org/10.1002/glia.24614, doi:10.1002/glia.24614. This article has 12 citations and is from a domain leading peer-reviewed journal.

13. (breuer2018characterizingthefunction pages 15-19): Maximilian Breuer. Characterizing the function and role of three dihydropteridine reductase homologs qdpra, qdprb1 and qdprb2 in the embryonic development of danio rerio. Text, Jan 2018. URL: https://doi.org/10.11588/heidok.00024357, doi:10.11588/heidok.00024357. This article has 0 citations and is from a peer-reviewed journal.

14. (eichwald2023tetrahydrobiopterinbeyondits pages 5-7): Tuany Eichwald, Lucila de Bortoli da da Silva, Ananda Christina Staats Staats Pires, Laís Niero, Erick Schnorrenberger, Clovis Colpani Filho, Gisele Espíndola, Wei-Lin Huang, Gilles J. Guillemin, José E. Abdenur, and Alexandra Latini. Tetrahydrobiopterin: beyond its traditional role as a cofactor. Antioxidants, 12:1037, May 2023. URL: https://doi.org/10.3390/antiox12051037, doi:10.3390/antiox12051037. This article has 92 citations.

15. (crabtree2011synthesisandrecycling pages 3-4): Mark J. Crabtree and Keith M. Channon. Synthesis and recycling of tetrahydrobiopterin in endothelial function and vascular disease. Nitric oxide : biology and chemistry, 25 2:81-8, Aug 2011. URL: https://doi.org/10.1016/j.niox.2011.04.004, doi:10.1016/j.niox.2011.04.004. This article has 273 citations.

16. (opladen2020consensusguidelinefor pages 6-7): Thomas Opladen, Eduardo López-Laso, Elisenda Cortès-Saladelafont, Toni S. Pearson, H. Serap Sivri, Yilmaz Yildiz, Birgit Assmann, Manju A. Kurian, Vincenzo Leuzzi, Simon Heales, Simon Pope, Francesco Porta, Angeles García-Cazorla, Tomáš Honzík, Roser Pons, Luc Regal, Helly Goez, Rafael Artuch, Georg F. Hoffmann, Gabriella Horvath, Beat Thöny, Sabine Scholl-Bürgi, Alberto Burlina, Marcel M. Verbeek, Mario Mastrangelo, Jennifer Friedman, Tessa Wassenberg, Kathrin Jeltsch, Jan Kulhánek, and Oya Kuseyri Hübschmann. Consensus guideline for the diagnosis and treatment of tetrahydrobiopterin (bh4) deficiencies. Orphanet Journal of Rare Diseases, May 2020. URL: https://doi.org/10.1186/s13023-020-01379-8, doi:10.1186/s13023-020-01379-8. This article has 182 citations and is from a peer-reviewed journal.

17. (alam2023uncouplednitricoxide pages 1-2): Asim Alam, Steven C. Smith, Sundaresan Gobalakrishnan, Mina McGinn, Vasily A. Yakovlev, and Christopher S. Rabender. Uncoupled nitric oxide synthase activity promotes colorectal cancer progression. Frontiers in Oncology, Mar 2023. URL: https://doi.org/10.3389/fonc.2023.1165326, doi:10.3389/fonc.2023.1165326. This article has 12 citations.

18. (yan2026overcomingmultidimensionalimmunotherapy pages 5-6): Jin Yan, Huiyi Ou, Shuai Wang, Kaizhou Jin, Xianjun Yu, and Weiding Wu. Overcoming multidimensional immunotherapy resistance in pdac: from microenvironment to clinic. Frontiers in Immunology, Mar 2026. URL: https://doi.org/10.3389/fimmu.2026.1782960, doi:10.3389/fimmu.2026.1782960. This article has 1 citations and is from a peer-reviewed journal.

19. (lye2002characterizationofquinonoiddihydropteridine pages 1-1): Lon-Fye Lye, Mark L. Cunningham, and Stephen M. Beverley. Characterization of quinonoid-dihydropteridine reductase (qdpr) from the lower eukaryote leishmania major *. The Journal of Biological Chemistry, 277:38245-38253, Oct 2002. URL: https://doi.org/10.1074/jbc.m206543200, doi:10.1074/jbc.m206543200. This article has 37 citations.

20. (pierson2018discoveryofnovel pages 14-18): Yann Mathieu Pierson. Discovery of novel competitive dihydropteridine reductase inhibitors via high throughput screening and their effect on metabolic pterin balance of fibroblast. ArXiv, Jan 2018. URL: https://doi.org/10.5075/epfl-thesis-8371, doi:10.5075/epfl-thesis-8371. This article has 0 citations.

21. (siems2025developmentalmaturationand pages 1-2): Sophie B. Siems, Vasiliki‐Ilya Gargareta, Leonie C. Schadt, Vinicius Daguano Gastaldi, Ramona B. Jung, Lars Piepkorn, Patrizia Casaccia, Ting Sun, Olaf Jahn, and Hauke B. Werner. Developmental maturation and regional heterogeneity but no sexual dimorphism of the murine cns myelin proteome. Glia, 73:38-56, Sep 2025. URL: https://doi.org/10.1002/glia.24614, doi:10.1002/glia.24614. This article has 12 citations and is from a domain leading peer-reviewed journal.

22. (siems2025developmentalmaturationand pages 4-6): Sophie B. Siems, Vasiliki‐Ilya Gargareta, Leonie C. Schadt, Vinicius Daguano Gastaldi, Ramona B. Jung, Lars Piepkorn, Patrizia Casaccia, Ting Sun, Olaf Jahn, and Hauke B. Werner. Developmental maturation and regional heterogeneity but no sexual dimorphism of the murine cns myelin proteome. Glia, 73:38-56, Sep 2025. URL: https://doi.org/10.1002/glia.24614, doi:10.1002/glia.24614. This article has 12 citations and is from a domain leading peer-reviewed journal.

23. (siems2025developmentalmaturationand pages 11-12): Sophie B. Siems, Vasiliki‐Ilya Gargareta, Leonie C. Schadt, Vinicius Daguano Gastaldi, Ramona B. Jung, Lars Piepkorn, Patrizia Casaccia, Ting Sun, Olaf Jahn, and Hauke B. Werner. Developmental maturation and regional heterogeneity but no sexual dimorphism of the murine cns myelin proteome. Glia, 73:38-56, Sep 2025. URL: https://doi.org/10.1002/glia.24614, doi:10.1002/glia.24614. This article has 12 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](QDPR-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. thony2000tetrahydrobiopterinbiosynthesisregeneration pages 12-13
2. thony2000tetrahydrobiopterinbiosynthesisregeneration pages 10-12
3. cutler1986dihydropteridinereductase pages 58-64
4. lye2002characterizationofquinonoiddihydropteridine pages 6-7
5. varughese1992crystalstructureof pages 4-5
6. varughese1992crystalstructureof pages 1-2
7. breuer2018characterizingthefunction pages 15-19
8. siems2025developmentalmaturationand pages 6-8
9. siems2025developmentalmaturationand pages 11-12
10. opladen2020consensusguidelinefor pages 1-2
11. eichwald2023tetrahydrobiopterinbeyondits pages 9-10
12. opladen2020consensusguidelinefor pages 6-7
13. breuer2018characterizingthefunction pages 19-24
14. alam2023uncouplednitricoxide pages 1-2
15. yan2026overcomingmultidimensionalimmunotherapy pages 5-6
16. pierson2018discoveryofnovel pages 27-31
17. siems2025developmentalmaturationand pages 8-9
18. eichwald2023tetrahydrobiopterinbeyondits pages 5-7
19. crabtree2011synthesisandrecycling pages 3-4
20. lye2002characterizationofquinonoiddihydropteridine pages 1-1
21. pierson2018discoveryofnovel pages 14-18
22. siems2025developmentalmaturationand pages 1-2
23. siems2025developmentalmaturationand pages 4-6
24. https://doi.org/10.1042/bj3470001,
25. https://doi.org/10.1073/pnas.89.13.6080,
26. https://doi.org/10.5075/epfl-thesis-8371,
27. https://doi.org/10.3390/antiox12051037,
28. https://doi.org/10.1186/s13023-020-01379-8,
29. https://doi.org/10.11588/heidok.00024357,
30. https://doi.org/10.1074/jbc.m206543200,
31. https://doi.org/10.1002/glia.24614,
32. https://doi.org/10.1016/j.niox.2011.04.004,
33. https://doi.org/10.3389/fonc.2023.1165326,
34. https://doi.org/10.3389/fimmu.2026.1782960,