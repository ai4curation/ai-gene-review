---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T14:03:41.715547'
end_time: '2026-09-08T14:14:03.012860'
duration_seconds: 621.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ALDH7A1
  gene_symbol: ALDH7A1
  uniprot_accession: P49419
  protein_description: 'RecName: Full=Alpha-aminoadipic semialdehyde dehydrogenase
    {ECO:0000305|PubMed:20207735}; Short=Alpha-AASA dehydrogenase {ECO:0000305|PubMed:16491085};
    EC=1.2.1.31 {ECO:0000269|PubMed:16491085, ECO:0000269|PubMed:20207735, ECO:0000269|PubMed:20554659};
    AltName: Full=Aldehyde dehydrogenase family 7 member A1; EC=1.2.1.3 {ECO:0000269|PubMed:20207735,
    ECO:0000269|PubMed:21338592}; AltName: Full=Antiquitin-1 {ECO:0000303|PubMed:9417906};
    AltName: Full=Betaine aldehyde dehydrogenase; EC=1.2.1.8 {ECO:0000269|PubMed:20207735};
    AltName: Full=Delta1-piperideine-6-carboxylate dehydrogenase; Short=P6c dehydrogenase;
    Flags: Precursor;'
  gene_info: Name=ALDH7A1 {ECO:0000303|PubMed:21338592, ECO:0000312|HGNC:HGNC:877};
    Synonyms=ATQ1 {ECO:0000303|PubMed:9417906};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_GLU.
    (IPR029510); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ALDH7A1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P49419
- **Protein Description:** RecName: Full=Alpha-aminoadipic semialdehyde dehydrogenase {ECO:0000305|PubMed:20207735}; Short=Alpha-AASA dehydrogenase {ECO:0000305|PubMed:16491085}; EC=1.2.1.31 {ECO:0000269|PubMed:16491085, ECO:0000269|PubMed:20207735, ECO:0000269|PubMed:20554659}; AltName: Full=Aldehyde dehydrogenase family 7 member A1; EC=1.2.1.3 {ECO:0000269|PubMed:20207735, ECO:0000269|PubMed:21338592}; AltName: Full=Antiquitin-1 {ECO:0000303|PubMed:9417906}; AltName: Full=Betaine aldehyde dehydrogenase; EC=1.2.1.8 {ECO:0000269|PubMed:20207735}; AltName: Full=Delta1-piperideine-6-carboxylate dehydrogenase; Short=P6c dehydrogenase; Flags: Precursor;
- **Gene Information:** Name=ALDH7A1 {ECO:0000303|PubMed:21338592, ECO:0000312|HGNC:HGNC:877}; Synonyms=ATQ1 {ECO:0000303|PubMed:9417906};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_GLU. (IPR029510); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALDH7A1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALDH7A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALDH7A1** (gene ID: ALDH7A1, UniProt: P49419) in human.

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
- **UniProt Accession:** P49419
- **Protein Description:** RecName: Full=Alpha-aminoadipic semialdehyde dehydrogenase {ECO:0000305|PubMed:20207735}; Short=Alpha-AASA dehydrogenase {ECO:0000305|PubMed:16491085}; EC=1.2.1.31 {ECO:0000269|PubMed:16491085, ECO:0000269|PubMed:20207735, ECO:0000269|PubMed:20554659}; AltName: Full=Aldehyde dehydrogenase family 7 member A1; EC=1.2.1.3 {ECO:0000269|PubMed:20207735, ECO:0000269|PubMed:21338592}; AltName: Full=Antiquitin-1 {ECO:0000303|PubMed:9417906}; AltName: Full=Betaine aldehyde dehydrogenase; EC=1.2.1.8 {ECO:0000269|PubMed:20207735}; AltName: Full=Delta1-piperideine-6-carboxylate dehydrogenase; Short=P6c dehydrogenase; Flags: Precursor;
- **Gene Information:** Name=ALDH7A1 {ECO:0000303|PubMed:21338592, ECO:0000312|HGNC:HGNC:877}; Synonyms=ATQ1 {ECO:0000303|PubMed:9417906};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_GLU. (IPR029510); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALDH7A1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALDH7A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALDH7A1** (gene ID: ALDH7A1, UniProt: P49419) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human ALDH7A1 (UniProt P49419): Functional Annotation Research Report

## Executive summary

The requested target is unambiguous: **human ALDH7A1**, UniProt **P49419**, also called **antiquitin**, **α-aminoadipic semialdehyde dehydrogenase**, or **α-AASA/AASAL dehydrogenase**. The literature identity, organism, aldehyde-dehydrogenase family membership, and domain architecture agree with the supplied UniProt record; no similarly named protein from another organism was used. Human genetic and biochemical evidence establishes its principal function in lysine degradation rather than as a generic aldehyde-detoxifying enzyme. (korasick2024biochemicalstructuraland pages 1-3)

ALDH7A1 catalyzes the NAD⁺-dependent oxidation of α-aminoadipic semialdehyde to α-aminoadipate. Loss of this activity causes α-AASA and its cyclic form, Δ¹-piperideine-6-carboxylate (P6C), to accumulate. P6C traps pyridoxal-5′-phosphate (PLP), producing a secondary functional vitamin-B6 deficiency and the treatable neurometabolic disorder **pyridoxine-dependent epilepsy due to ALDH7A1 deficiency (PDE-ALDH7A1)**. Pyridoxine usually controls seizures, but approximately 75% of affected patients have some developmental or intellectual impairment, motivating lysine-reduction therapy and research into metabolite-directed treatments. (marchitti2008nonp450aldehydeoxidizing pages 14-15, gan2024precisiondiagnosisand pages 4-6, salih2024casereportclinical pages 1-2)

| Aspect | Best-supported annotation | Evidence type/strength |
|---|---|---|
| Verified identity/synonyms | Human **ALDH7A1** (UniProt **P49419**) is aldehyde dehydrogenase 7 family member A1, **antiquitin**, and α-aminoadipate/α-aminoadipic semialdehyde dehydrogenase. Literature identity matches the supplied human target; no conflicting gene was used. (korasick2024biochemicalstructuraland pages 1-3) | **High:** human biochemical, structural, and clinical-genetic evidence |
| Enzyme reaction and physiological substrate | Catalyzes **α-aminoadipate semialdehyde (α-AASA/AASAL) + NAD⁺ + H₂O → α-aminoadipate + NADH + H⁺**. α-AASA is the established physiological substrate; one review reports an apparent *K*ₘ of approximately **180 μM**. Broader aldehyde activities do not supersede this primary annotation. (marchitti2008nonp450aldehydeoxidizing pages 14-15, korasick2024biochemicalstructuraland pages 1-3) | **High** for reaction; **moderate** for the reported kinetic value |
| Cofactor/mechanism | An **NAD⁺-dependent aldehyde dehydrogenase**: oxidation is expected to proceed through the conserved ALDH catalytic-cysteine/thiohemiacetal and acyl-enzyme mechanism, followed by hydrolysis and NADH production. NAD⁺ also promotes assembly of the active oligomer. (korasick2024biochemicalstructuraland pages 11-13, marchitti2008nonp450aldehydeoxidizing pages 2-3, korasick2024biochemicalstructuraland pages 1-3) | **High** for NAD⁺ dependence; **moderate** where mechanism is inferred from the conserved ALDH fold |
| Active oligomer and domains | The catalytically competent enzyme is a **homotetramer**. Its ALDH architecture comprises cofactor-binding, catalytic, and oligomerization/bridging regions, consistent with the supplied Ald_DH_N, Aldehyde_DH, and Ald_DH_C annotations. Interface variants can trap inactive dimers. (marchitti2008nonp450aldehydeoxidizing pages 13-14, korasick2024biochemicalstructuraland pages 11-13, korasick2021impactofmissense pages 5-7) | **High:** crystallography, analytical ultracentrifugation, kinetics, and variant biophysics |
| Localization | ALDH7A1 is an intracellular enzyme. Cytosolic and mitochondrial localization claims are **isoform-dependent**; although lysine degradation is often placed in the mitochondrial matrix, the precise compartment used by each human isoform is less firmly established in the retrieved primary literature and should not be reduced to one universal location. (marchitti2008nonp450aldehydeoxidizing pages 2-3, salih2024casereportclinical pages 1-2) | **Moderate/limited:** database and literature annotation; less definitive than catalytic evidence |
| Lysine pathway | Functions in the **pipecolate/saccharopine network of lysine degradation**, oxidizing α-AASA at the step leading to α-aminoadipate and onward catabolism. (marchitti2008nonp450aldehydeoxidizing pages 14-15, marchitti2008nonp450aldehydeoxidizing pages 13-14, korasick2024biochemicalstructuraland pages 1-3) | **High:** biochemical and human loss-of-function evidence |
| Loss-of-function metabolites and PLP trapping | Deficiency causes accumulation of α-AASA and its cyclic Schiff-base form **Δ¹-piperideine-6-carboxylate (P6C)**. P6C forms a Knoevenagel adduct with pyridoxal-5′-phosphate (**PLP**), producing secondary functional vitamin-B6 deficiency and disturbing PLP-dependent neurotransmitter metabolism. (marchitti2008nonp450aldehydeoxidizing pages 14-15, gan2024precisiondiagnosisand pages 4-6, korasick2024biochemicalstructuraland pages 1-3) | **High:** patient biochemistry plus established chemical mechanism |
| Disease | Biallelic pathogenic variants cause autosomal-recessive **pyridoxine-dependent epilepsy due to ALDH7A1 deficiency (PDE-ALDH7A1)**, usually presenting with neonatal, antiseizure-medication-resistant seizures; atypical later onset occurs. Estimates range from roughly **1:65,000 to 1:250,000 live births**, and developmental/intellectual impairment is reported in about **75%** despite seizure control. (gan2024precisiondiagnosisand pages 4-6, salih2024casereportclinical pages 1-2, korasick2024biochemicalstructuraland pages 1-3) | **High** for causality; prevalence and outcome estimates vary by ascertainment |
| Biomarkers | Established markers are **α-AASA/P6C** in urine, plasma, or CSF; pipecolate is less specific. **6-oxo-pipecolate** and **2-OPP** are more stable emerging candidates, but age dependence, analytical interference, and imperfect neonatal sensitivity limit stand-alone use. Molecular confirmation requires biallelic pathogenic ALDH7A1 variants. (lipinski2024casereportearly pages 1-2, wempe2019identificationofa pages 11-16, engelke2021untargetedmetabolomicsand pages 1-9, korasick2024biochemicalstructuraland pages 1-3) | **High** for α-AASA/P6C; **moderate/emerging** for 6-oxo-PIP and 2-OPP |
| Current treatment | Lifelong pharmacological **pyridoxine** is the seizure-directed standard. Lysine-reduction therapy—dietary lysine restriction and/or **L-arginine** to compete with lysine transport—is used to lower toxic metabolites and may improve neurodevelopment; pyridoxine should continue while biochemical and genetic results are pending. (lipinski2024casereportearly pages 1-2, gan2024precisiondiagnosisand pages 4-6, arntsen2024utilityandlimitations pages 1-2) | **High** for seizure control by pyridoxine; **moderate** for neurodevelopmental benefit from adjunctive lysine reduction |
| 2024 advances | Structural work showed clinical variants **R134S** and **R441C** reduce catalytic efficiency approximately **10,000-fold** and **50-fold**, respectively, through defective tetramerization or altered active-site dynamics. A 13-patient EEG study found neonatal burst suppression in **62%**, but acute EEG response to pyridoxine was inconsistent. New clinical reports reinforced early sequencing while documenting persistent developmental deficits despite seizure control. (korasick2024biochemicalstructuraland pages 11-13, arntsen2024utilityandlimitations pages 1-2, salih2024casereportclinical pages 1-2, korasick2024biochemicalstructuraland pages 1-3) | **Strong recent primary evidence**, but cohorts remain small because PDE-ALDH7A1 is rare |


*Table: Compact evidence map for human ALDH7A1/P49419, covering molecular function, localization, pathway, disease mechanism, diagnostics, treatment, and key 2024 findings. Evidence confidence is qualified to distinguish established enzymology from less certain localization and emerging biomarkers.*

## 1. Identity verification and nomenclature

### 1.1 Required verification

* **Gene:** ALDH7A1; approved name, aldehyde dehydrogenase 7 family member A1.
* **Protein:** α-aminoadipic semialdehyde dehydrogenase/antiquitin.
* **UniProt accession:** P49419.
* **Organism:** *Homo sapiens*.
* **Primary physiological context:** lysine degradation.

Recent structural literature explicitly states that PDE is caused by variants in **ALDH7A1**, encoding α-aminoadipate semialdehyde dehydrogenase, “also known as antiquitin,” and identifies the enzyme’s lysine-catabolic reaction. This directly matches the supplied protein description. (korasick2024biochemicalstructuraland pages 1-3)

The protein belongs to the NAD(P)⁺-dependent aldehyde-dehydrogenase superfamily. Its supplied InterPro annotations—Ald_DH_N, central aldehyde-dehydrogenase catalytic domain, Ald_DH_C, and the conserved catalytic-glutamate signature—are consistent with the canonical ALDH organization into cofactor-binding, catalytic, and oligomerization/bridging regions. (marchitti2008nonp450aldehydeoxidizing pages 2-3)

## 2. Primary molecular function

### 2.1 Catalyzed reaction

The best-supported physiological reaction is:

**α-aminoadipic semialdehyde + NAD⁺ + H₂O → α-aminoadipate + NADH + H⁺.**

This oxidation occurs at a late step of lysine catabolism. A frequently cited biochemical review reports an apparent α-AASA Michaelis constant of approximately **180 μM**. (marchitti2008nonp450aldehydeoxidizing pages 14-15, korasick2024biochemicalstructuraland pages 1-3)

α-AASA exists in reversible equilibrium with its cyclic Schiff-base form, P6C. ALDH7A1 acts on the open-chain aldehyde, not by directly oxidizing PLP or functioning as a vitamin-B6 enzyme. Its effects on vitamin-B6 metabolism are therefore secondary to removal of α-AASA/P6C. (marchitti2008nonp450aldehydeoxidizing pages 14-15, korasick2024biochemicalstructuraland pages 1-3)

### 2.2 Substrate specificity

The physiological annotation should be **α-AASA dehydrogenase**, despite historical names such as betaine-aldehyde dehydrogenase and reports of activity toward other aldehydes. Nonhuman ALDH7A1 orthologs can oxidize acetaldehyde, propionaldehyde, or benzaldehyde at low affinity, but these observations do not establish those compounds as principal human substrates. Human loss-of-function genetics, patient metabolite accumulation, and purified-enzyme studies converge on α-AASA as the biologically decisive substrate. (marchitti2008nonp450aldehydeoxidizing pages 14-15, marchitti2008nonp450aldehydeoxidizing pages 13-14, korasick2024biochemicalstructuraland pages 1-3)

Accordingly, the broad EC 1.2.1.3 aldehyde-dehydrogenase annotation describes catalytic capability, while **EC 1.2.1.31** best represents the primary physiological reaction.

### 2.3 Catalytic mechanism

ALDH7A1 uses the conserved ALDH mechanism: NAD⁺ binding organizes the cofactor site; a catalytic cysteine attacks the substrate aldehyde to form a thiohemiacetal; hydride transfer to NAD⁺ generates an acyl-enzyme intermediate and NADH; hydrolysis then releases the carboxylic-acid product. The detailed chemical sequence is strongly supported by the conserved ALDH fold, although some residue-level steps are inferred from the wider superfamily rather than measured independently in human ALDH7A1. (marchitti2008nonp450aldehydeoxidizing pages 2-3)

NAD⁺ has an additional structural role: it promotes assembly of the active tetramer. Thus variants can impair activity through altered oligomerization even when they do not contact the substrate or cofactor directly. (korasick2024biochemicalstructuraland pages 11-13, korasick2024biochemicalstructuraland pages 1-3)

## 3. Structure and genotype-to-function relationships

The functional enzyme is a **homotetramer**. Each subunit contains the ALDH cofactor-binding, catalytic, and oligomerization elements reflected by the supplied Ald_DH_N, Aldehyde_DH_dom, and Ald_DH_C annotations. Pathogenic variants occur not only in the catalytic pocket but also at dimer/tetramer interfaces and buried structural positions. Experiments show that some variants cause insolubility or misfolding, while others prevent tetramerization or active-site closure. (marchitti2008nonp450aldehydeoxidizing pages 13-14, korasick2021impactofmissense pages 5-7)

A notable 2024 study, published **1 May 2024**, examined two patient variants. R134S/p.Arg162Ser reduced catalytic efficiency approximately **10,000-fold** and remained an inactive dimer even with NAD⁺; R441C/p.Arg469Cys reduced efficiency approximately **50-fold** despite retaining the tetramer and an apparently intact NAD⁺ site. Molecular dynamics implicated altered intersubunit contacts and active-site-gate dynamics in R441C. This demonstrates why sequence location alone is often insufficient to predict residual activity. DOI/URL: https://doi.org/10.1016/j.cbi.2024.110993. (korasick2024biochemicalstructuraland pages 11-13, korasick2024biochemicalstructuraland pages 1-3)

More than 70 missense variants had been described by that study, among broader classes including insertions, deletions, and nonsense variants across 18 exons. A 2024 review cited 165 reported pathogenic variants and emphasized the absence of a clear genotype–phenotype correlation. (gan2024precisiondiagnosisand pages 4-6, korasick2024biochemicalstructuraland pages 1-3)

## 4. Biochemical pathway

ALDH7A1 functions in the interconnected pipecolate and saccharopine routes of **lysine degradation**. Both routes feed into α-AASA/P6C; ALDH7A1 oxidizes α-AASA to α-aminoadipate, permitting downstream conversion toward central metabolic intermediates. Its precise role is therefore removal of a reactive aldehyde at a pathway convergence point, not initiation of lysine breakdown. (marchitti2008nonp450aldehydeoxidizing pages 14-15, marchitti2008nonp450aldehydeoxidizing pages 13-14)

When ALDH7A1 activity is deficient:

1. α-AASA and P6C accumulate in blood, urine, CSF, and tissues.
2. P6C reacts with PLP through a Knoevenagel-type condensation.
3. PLP availability falls, compromising PLP-dependent amino-acid and neurotransmitter reactions.
4. Altered GABA, serotonin, noradrenaline, and other neurotransmitter pathways contribute to seizures.
5. Persistent lysine-derived metabolite toxicity likely contributes to neurodevelopmental impairment beyond the seizures themselves. (marchitti2008nonp450aldehydeoxidizing pages 14-15, gan2024precisiondiagnosisand pages 4-6, korasick2024biochemicalstructuraland pages 1-3)

The final point is important: pyridoxine replaces depleted vitamin B6 and usually controls seizures, but it does not remove the upstream lysine-catabolic block.

## 5. Cellular and tissue localization

ALDH7A1 is an **intracellular metabolic enzyme**, not a secreted or membrane protein. Literature and annotation resources describe cytosolic and mitochondrial forms, while lysine degradation is frequently discussed in relation to the mitochondrial matrix. However, the retrieved primary literature was much stronger on catalysis and tetramer structure than on isoform-resolved localization. Therefore, “exclusively mitochondrial” or “exclusively cytosolic” would be overconfident; the most defensible annotation is **isoform-dependent cytosolic/mitochondrial localization**, with function wherever α-AASA is generated and accessible. (marchitti2008nonp450aldehydeoxidizing pages 2-3, salih2024casereportclinical pages 1-2)

A tissue-expression review reported high expression in fetal cochlea, eye, ovary, heart, and kidney, with moderate expression in liver, spleen, skeletal muscle, lung, and brain. These older expression data establish broad distribution but should not be interpreted as a quantitative contemporary atlas. (marchitti2008nonp450aldehydeoxidizing pages 13-14)

In the nervous system, ALDH7A1 has been reported in glial cells and implicated in early neurogenesis and migration, but those broader developmental roles are less firmly established than its enzymatic lysine-catabolic function. (gan2024precisiondiagnosisand pages 4-6)

## 6. Human disease mechanism and quantitative clinical data

Biallelic damaging variants cause autosomal-recessive PDE-ALDH7A1. Open Targets independently links human ALDH7A1 to epilepsy, seizures, pyridoxine-dependent epilepsy, and the ALDH7A1-mutant disease entity, with the association supported by foundational human genetic literature. (OpenTargets Search: -ALDH7A1)

Published incidence estimates vary from approximately **1:65,000 to 1:250,000 live births**. A 2024 review estimated population prevalence at **1:64,352**, with a higher estimate of **1:16,556 in Asia**; ascertainment and founder effects probably account for some variation. (gan2024precisiondiagnosisand pages 4-6, salih2024casereportclinical pages 1-2)

Classically, seizures start within hours or days of birth, resist conventional antiseizure medication, and respond to pharmacological pyridoxine. Later infantile or childhood onset, temporary response to standard medication, and incomplete immediate pyridoxine response can occur. Approximately **75%** of patients are reported to have developmental delay or intellectual disability despite early seizure control. (gan2024precisiondiagnosisand pages 4-6, salih2024casereportclinical pages 1-2)

A Norwegian retrospective study published **14 February 2024** evaluated **13 patients and 163 EEGs**, including 101 recordings from the first year. Median seizure onset was **9 hours**; median delay to first pyridoxine injection was **2 days**. Eight patients (**62%**) had burst suppression within the first five days. Of 11 monitored during pyridoxine injections, only three showed immediate EEG improvement concordant with seizure control; clinical and electrographic responses often diverged. The authors advised continuing pyridoxine until biomarkers and genetic results are available rather than excluding PDE after one inconclusive trial. DOI/URL: https://doi.org/10.3389/fneur.2024.1355861. (arntsen2024utilityandlimitations pages 1-2)

## 7. Diagnostics and biomarkers

### Established testing

The principal biochemical markers are **α-AASA and P6C** in urine, plasma, or CSF. Pipecolic acid can also be elevated but is less specific. Definitive diagnosis combines the clinical phenotype and biochemical findings with demonstration of biallelic pathogenic ALDH7A1 variants. (lipinski2024casereportearly pages 1-2, korasick2024biochemicalstructuraland pages 1-3)

α-AASA/P6C are chemically unstable, complicating transport, storage, and newborn-screening workflows. A study of 272 samples found that urinary α-AASA/creatinine was significantly elevated but age-dependent. (gan2024precisiondiagnosisand pages 4-6)

### Emerging markers

**6-Oxo-pipecolate (6-oxo-PIP)** is substantially more stable than P6C. In an early analytical study, affected patients—but not 14 blood/urine controls or three CSF controls—showed 6-oxo-PIP and related abnormal metabolites. Illustrative plasma concentrations were **2.7 ± 0.1** and **4.1 ± 0.1 μM**, while two urine samples contained **156.8** and **122.2 μmol/mg creatinine**. Sensitivity and specificity nevertheless required further validation. DOI/URL, March 2019: https://doi.org/10.1002/jimd.12059. (wempe2019identificationofa pages 11-16)

**2-OPP**—2S,6S- and 2S,6R-oxopropylpiperidine-2-carboxylic acid—was identified through untargeted metabolomics and infrared ion spectroscopy. It occurs in patient brain and experimental models and may itself be neuroactive. Analytical correlations included R² values of **0.886** between plasma 2-OPP concentration and metabolomics signal and **0.785** between urinary 2-OPP and α-AASA. In six massively ketotic non-PDE controls, plasma 2-OPP remained below the proposed 1.0-μM patient cutoff, although larger screening studies are needed. DOI/URL, 2021: https://doi.org/10.1172/JCI148272. (engelke2021untargetedmetabolomicsand pages 1-9)

Real-world limitations remain important. A case published **12 September 2024** showed that levetiracetam can produce a GC–MS peak with a similar retention time and mask urinary 6-oxo-PIP. An 83-gene neonatal-seizure panel instead identified two truncating ALDH7A1 variants; treatment controlled seizures within three days. DOI/URL: https://doi.org/10.3389/fgene.2024.1464556. (lipinski2024casereportearly pages 1-2)

## 8. Current treatment and implementation

### Pyridoxine

Lifelong pharmacological **pyridoxine** is standard mechanism-based therapy. It replenishes the vitamin-B6 pool depleted by P6C and often produces dramatic seizure control. Abrupt withdrawal can precipitate life-threatening status epilepticus. Dosing and monitoring should follow specialist metabolic/neurological guidance because chronic high doses can cause peripheral neuropathy. (korasick2024biochemicalstructuraland pages 1-3)

### Lysine-reduction therapy

Because pyridoxine does not correct metabolite accumulation, experts increasingly recommend substrate reduction, especially early in life:

* a lysine-restricted diet reduces precursor supply;
* L-arginine competitively limits lysine transport, including entry into the CNS;
* combined pyridoxine, lysine restriction, and arginine is commonly termed **triple therapy**.

Clinical studies cited by the 2024 review found substantial reductions in plasma and CSF α-AASA/P6C with lysine restriction, alongside seizure control and some developmental gains. Arginine lowered CSF α-AASA and was associated with improved motor-verbal function. Evidence for seizure control is strongest for pyridoxine; evidence that lysine reduction improves long-term cognition is promising but remains observational rather than based on large randomized trials. (gan2024precisiondiagnosisand pages 4-6)

### Molecular diagnosis in practice

Recent case reports demonstrate routine implementation of rapid sequencing. On **23 December 2024**, investigators reported siblings homozygous for a new p.Gly390Arg variant. Seizures beginning at 6 and 10 hours were controlled by pyridoxine, yet both had delayed milestones and one had dyslexia, reinforcing the distinction between seizure rescue and complete neurodevelopmental rescue. DOI/URL: https://doi.org/10.3389/fpsyt.2024.1501238. (salih2024casereportclinical pages 1-2)

## 9. Recent developments, 2023–2024

1. **Precision metabolic therapy:** A 2023 review framed ALDH7A1 disease treatment as a combination of cofactor replacement and lysine reduction, while identifying enzyme replacement, gene replacement/editing, and biomarkers as longer-term directions. DOI/URL, July 2023: https://doi.org/10.1212/WNL.0000000000207133. (lipinski2024casereportearly pages 5-6)
2. **Variant interpretation:** The May 2024 R134S/R441C study showed that pathogenicity can arise from failed tetramerization or altered dynamics without gross active-site disruption, supporting functional assays for variants of uncertain significance. (korasick2024biochemicalstructuraland pages 11-13, korasick2024biochemicalstructuraland pages 1-3)
3. **EEG limitations:** The February 2024 Norwegian cohort showed that a single acute pyridoxine EEG challenge is not sufficiently reliable to exclude PDE. (arntsen2024utilityandlimitations pages 1-2)
4. **Improved molecular diagnosis:** September and December 2024 reports demonstrated the value of targeted panels or exome sequencing where unstable or analytically confounded biomarkers delay diagnosis. (lipinski2024casereportearly pages 1-2, salih2024casereportclinical pages 1-2)
5. **Mechanisms of residual cognitive disease:** A 2024 review emphasized persistent metabolite toxicity and reported that roughly 75% of patients retain developmental impairment despite pyridoxine. Emerging animal work links α-AASA/P6C accumulation to impaired neurogenesis and metabolic processes; these findings are mechanistically important but are not yet validated human therapies. (gan2024precisiondiagnosisand pages 4-6)

## 10. Expert interpretation and evidence gaps

The functional annotation is unusually secure: human genetics, patient metabolomics, purified-enzyme kinetics, and structures all identify α-AASA oxidation as ALDH7A1’s primary role. Conversely, generic “aldehyde detoxification,” osmotic-stress responses, and cancer associations should be treated as secondary or context-dependent functions, not substitutes for the lysine-catabolic annotation.

The major unresolved questions are clinical rather than enzymatic: which metabolites directly cause intellectual disability, how early substrate reduction must begin, whether biomarker normalization predicts cognition, and which variants retain therapeutically meaningful activity. Small cohorts and heterogeneous treatment histories constrain current outcome estimates. Likewise, the exact compartment-specific contribution of human ALDH7A1 isoforms requires stronger direct localization evidence.

## Conclusion

Human ALDH7A1/P49419 is an NAD⁺-dependent, tetrameric α-aminoadipic semialdehyde dehydrogenase operating at a key convergence point in lysine degradation. Its failure causes α-AASA/P6C accumulation, PLP sequestration, and PDE-ALDH7A1. Pyridoxine is an effective seizure-directed precision therapy, while lysine restriction and arginine address the upstream biochemical burden. Recent 2024 studies improved variant interpretation, exposed limitations of acute EEG and biochemical testing, and strengthened the case for early genetic diagnosis. The highest-priority translational objective is now prevention of residual neurodevelopmental injury, not merely seizure suppression.

References

1. (korasick2024biochemicalstructuraland pages 1-3): David A. Korasick, David P. Buckley, Alessandra Palpacelli, Ida Cursio, Elisabetta Cesaroni, Jianlin Cheng, and John J. Tanner. Biochemical, structural, and computational analyses of two new clinically identified missense mutations of aldh7a1. May 2024. URL: https://doi.org/10.1016/j.cbi.2024.110993, doi:10.1016/j.cbi.2024.110993. This article has 1 citations and is from a peer-reviewed journal.

2. (marchitti2008nonp450aldehydeoxidizing pages 14-15): Satori A Marchitti, Chad Brocker, Dimitrios Stagos, and Vasilis Vasiliou. Non-p450 aldehyde oxidizing enzymes: the aldehyde dehydrogenase superfamily. Expert Opinion on Drug Metabolism & Toxicology, 4:697-720, Jun 2008. URL: https://doi.org/10.1517/17425255.4.6.697, doi:10.1517/17425255.4.6.697. This article has 1054 citations and is from a peer-reviewed journal.

3. (gan2024precisiondiagnosisand pages 4-6): Ya-Jing Gan, Guo-Yan Li, Zihan Wei, Yan Feng, Yuqing Shi, and Yanchun Deng. Precision diagnosis and treatment of vitamin metabolism-related epilepsy. Acta Epileptologica, Oct 2024. URL: https://doi.org/10.1186/s42494-024-00169-0, doi:10.1186/s42494-024-00169-0. This article has 10 citations.

4. (salih2024casereportclinical pages 1-2): Mustafa A. Salih, Albandary AlBakheet, Rawan Almass, Ahlam A. A. Hamed, Ali AlOdaib, and Namik Kaya. Case report: clinical and genetic characterization of a novel aldh7a1 variant causing pyridoxine-dependent epilepsy, developmental delay, and intellectual disability in two siblings. Frontiers in Psychiatry, Dec 2024. URL: https://doi.org/10.3389/fpsyt.2024.1501238, doi:10.3389/fpsyt.2024.1501238. This article has 5 citations.

5. (korasick2024biochemicalstructuraland pages 11-13): David A. Korasick, David P. Buckley, Alessandra Palpacelli, Ida Cursio, Elisabetta Cesaroni, Jianlin Cheng, and John J. Tanner. Biochemical, structural, and computational analyses of two new clinically identified missense mutations of aldh7a1. May 2024. URL: https://doi.org/10.1016/j.cbi.2024.110993, doi:10.1016/j.cbi.2024.110993. This article has 1 citations and is from a peer-reviewed journal.

6. (marchitti2008nonp450aldehydeoxidizing pages 2-3): Satori A Marchitti, Chad Brocker, Dimitrios Stagos, and Vasilis Vasiliou. Non-p450 aldehyde oxidizing enzymes: the aldehyde dehydrogenase superfamily. Expert Opinion on Drug Metabolism & Toxicology, 4:697-720, Jun 2008. URL: https://doi.org/10.1517/17425255.4.6.697, doi:10.1517/17425255.4.6.697. This article has 1054 citations and is from a peer-reviewed journal.

7. (marchitti2008nonp450aldehydeoxidizing pages 13-14): Satori A Marchitti, Chad Brocker, Dimitrios Stagos, and Vasilis Vasiliou. Non-p450 aldehyde oxidizing enzymes: the aldehyde dehydrogenase superfamily. Expert Opinion on Drug Metabolism & Toxicology, 4:697-720, Jun 2008. URL: https://doi.org/10.1517/17425255.4.6.697, doi:10.1517/17425255.4.6.697. This article has 1054 citations and is from a peer-reviewed journal.

8. (korasick2021impactofmissense pages 5-7): David A. Korasick and John J. Tanner. Impact of missense mutations in the aldh7a1 gene on enzyme structure and catalytic function. Apr 2021. URL: https://doi.org/10.1016/j.biochi.2020.09.016, doi:10.1016/j.biochi.2020.09.016. This article has 14 citations and is from a peer-reviewed journal.

9. (lipinski2024casereportearly pages 1-2): Patryk Lipiński, Katarzyna Wójcicka-Kowalczyk, Anna Bogdańska, Ewa Ehmke, Magdalena Pajdowska, Katarzyna Skrzypek, Agnieszka Charzewska, and Dorota Hoffman-Zacharska. Case report: early (molecular) diagnosis is the clue: report on aldh7a1 deficiency in newborns. Frontiers in Genetics, Sep 2024. URL: https://doi.org/10.3389/fgene.2024.1464556, doi:10.3389/fgene.2024.1464556. This article has 2 citations and is from a peer-reviewed journal.

10. (wempe2019identificationofa pages 11-16): Michael F. Wempe, Amit Kumar, Vijay Kumar, Yu J. Choi, Michael A. Swanson, Marisa W. Friederich, Keith Hyland, Wyatt W. Yue, Johan L. K. Van Hove, and Curtis R. Coughlin. Identification of a novel biomarker for pyridoxine‐dependent epilepsy: implications for newborn screening. Journal of Inherited Metabolic Disease, 42:565-574, Mar 2019. URL: https://doi.org/10.1002/jimd.12059, doi:10.1002/jimd.12059. This article has 69 citations and is from a peer-reviewed journal.

11. (engelke2021untargetedmetabolomicsand pages 1-9): Udo F.H. Engelke, Rianne E. van Outersterp, Jona Merx, Fred A.M.G. van Geenen, Arno van Rooij, Giel Berden, Marleen C.D.G. Huigen, Leo A.J. Kluijtmans, Tessa M.A. Peters, Hilal H. Al-Shekaili, Blair R. Leavitt, Erik de Vrieze, Sanne Broekman, Erwin van Wijk, Laura A. Tseng, Purva Kulkarni, Floris P.J.T. Rutjes, Jasmin Mecinović, Eduard A. Struys, Laura A. Jansen, Sidney M. Gospe, Saadet Mercimek-Andrews, Keith Hyland, Michèl A.A.P. Willemsen, Levinus A. Bok, Clara D.M. van Karnebeek, Ron A. Wevers, Thomas J. Boltje, Jos Oomens, Jonathan Martens, and Karlien L.M. Coene. Untargeted metabolomics and infrared ion spectroscopy identify biomarkers for pyridoxine-dependent epilepsy. Aug 2021. URL: https://doi.org/10.1172/jci148272, doi:10.1172/jci148272. This article has 75 citations and is from a highest quality peer-reviewed journal.

12. (arntsen2024utilityandlimitations pages 1-2): Vibeke Arntsen, Ahmed Jamali, Alma Sikiric, Erle Kristensen, Trine Tangeraas, Guste Kupliauskiene, Sigurbjörg Stefansdottir, Laurence A. Bindoff, Trond Sand, and Eylert Brodtkorb. Utility and limitations of eeg in the diagnosis and management of aldh7a1-related pyridoxine-dependent epilepsy. a retrospective observational study. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1355861, doi:10.3389/fneur.2024.1355861. This article has 6 citations and is from a peer-reviewed journal.

13. (OpenTargets Search: -ALDH7A1): Open Targets Query (-ALDH7A1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

14. (lipinski2024casereportearly pages 5-6): Patryk Lipiński, Katarzyna Wójcicka-Kowalczyk, Anna Bogdańska, Ewa Ehmke, Magdalena Pajdowska, Katarzyna Skrzypek, Agnieszka Charzewska, and Dorota Hoffman-Zacharska. Case report: early (molecular) diagnosis is the clue: report on aldh7a1 deficiency in newborns. Frontiers in Genetics, Sep 2024. URL: https://doi.org/10.3389/fgene.2024.1464556, doi:10.3389/fgene.2024.1464556. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ALDH7A1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. korasick2024biochemicalstructuraland pages 1-3
2. gan2024precisiondiagnosisand pages 4-6
3. arntsen2024utilityandlimitations pages 1-2
4. wempe2019identificationofa pages 11-16
5. engelke2021untargetedmetabolomicsand pages 1-9
6. lipinski2024casereportearly pages 1-2
7. salih2024casereportclinical pages 1-2
8. lipinski2024casereportearly pages 5-6
9. korasick2024biochemicalstructuraland pages 11-13
10. korasick2021impactofmissense pages 5-7
11. https://doi.org/10.1016/j.cbi.2024.110993.
12. https://doi.org/10.3389/fneur.2024.1355861.
13. https://doi.org/10.1002/jimd.12059.
14. https://doi.org/10.1172/JCI148272.
15. https://doi.org/10.3389/fgene.2024.1464556.
16. https://doi.org/10.3389/fpsyt.2024.1501238.
17. https://doi.org/10.1212/WNL.0000000000207133.
18. https://doi.org/10.1016/j.cbi.2024.110993,
19. https://doi.org/10.1517/17425255.4.6.697,
20. https://doi.org/10.1186/s42494-024-00169-0,
21. https://doi.org/10.3389/fpsyt.2024.1501238,
22. https://doi.org/10.1016/j.biochi.2020.09.016,
23. https://doi.org/10.3389/fgene.2024.1464556,
24. https://doi.org/10.1002/jimd.12059,
25. https://doi.org/10.1172/jci148272,
26. https://doi.org/10.3389/fneur.2024.1355861,