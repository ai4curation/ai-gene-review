# Deep Research Report: DEG1 (Saccharomyces cerevisiae)

## Gene Overview

**Gene Name:** DEG1 (Depressed growth-rate protein 1)  
**Synonyms:** HRM3, PUS3  
**Systematic Name:** YFL001W  
**Species:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c)  
**UniProt ID:** P31115  

DEG1 encodes the third characterized tRNA:pseudouridine synthase (Pus3p) in yeast, responsible for the formation of pseudouridine at positions 38 and 39 in the anticodon loop of transfer RNAs [PMID:9430663 "Lecointe et al., 1998, J Biol Chem - Characterization of yeast protein Deg1 as pseudouridine synthase (Pus3) catalyzing the formation of psi 38 and psi 39 in tRNA anticodon loop"].

## Molecular Function

### Primary Enzymatic Activity
DEG1/Pus3p is a **tRNA pseudouridine(38/39) synthase** (EC 5.4.99.45) that catalyzes the isomerization of uridine to pseudouridine (Ψ) specifically at positions 38 and 39 in the anticodon stem-loop of tRNAs [PMID:9430663 "DEG1-disrupted yeast strain lacks synthase activity for the formation of pseudouridines psi 38 and psi 39 in tRNA whereas the other activities, specific for psi formation at positions 13, 27, 28, 32, 34, 35, 36, and 55 in tRNA, remain unaffected"]. This modification is critical for:

- **tRNA stability**: Pseudouridine formation stabilizes the anticodon loop structure through additional hydrogen bonding
- **Translation fidelity**: The modifications at positions 38/39 affect codon-anticodon interactions and ribosome binding
- **Stress response**: Pseudouridylation helps maintain translation efficiency under stress conditions

### Substrate Specificity
The enzyme shows remarkable specificity for positions 38 and 39 in the anticodon loop, distinguishing it from other yeast pseudouridine synthases:
- **Pus1**: modifies positions 26, 27, 28, 34, 36, 65, and 67
- **Pus2**: modifies position 35 
- **Pus4**: modifies position 55
- **Pus6**: modifies position 31
- **Pus7**: modifies positions 13 and 35
- **Pus8**: modifies position 32
- **Pus9**: modifies position 32

DEG1/Pus3p modifies both **cytoplasmic and mitochondrial tRNAs** [PMID:9430663 "Identification of the pseudouridine residues present (or absent) in selected naturally occurring cytoplasmic and mitochondrial tRNAs from DEG1-disrupted strain points out a common origin of psi 38- and psi 39-synthesizing activity in both of these two cellular compartments"].

### mRNA Pseudouridylation
Recent evidence from high-throughput pseudouridine profiling reveals that Pus3 also modifies mRNAs [PMID:25192136 "We also identified novel targets for Pus3 (20 mRNA, 1 ncRNA)"]. This discovery expands the functional scope of DEG1/Pus3p beyond its canonical tRNA targets and suggests potential roles in:
- Post-transcriptional gene regulation
- mRNA stability
- Translation regulation under stress conditions

## Protein Structure and Domains

### Domain Architecture
DEG1/Pus3p (442 amino acids, ~50.9 kDa) belongs to the **TruA family** of pseudouridine synthases, sharing structural features with:
- **E. coli TruA**: The bacterial ortholog that modifies positions 38, 39, and 40
- **Human PUS3**: The human ortholog with 96% sequence identity in the core domain

The protein contains:
1. **Catalytic core domain**: Contains the conserved active site with the essential aspartate residue (Asp151 in yeast, corresponding to Asp118 in human)
2. **RNA-binding surfaces**: Multiple regions that recognize and bind the L-shaped tRNA substrate
3. **C-terminal region**: May be involved in protein stability or additional RNA contacts

### Active Site
The catalytic mechanism involves:
- A conserved aspartate residue (Asp151) that acts as the nucleophile
- Formation of a covalent enzyme-RNA intermediate
- No requirement for cofactors (unlike snoRNA-guided pseudouridine synthases)

### Oligomerization
Like other TruA family members, DEG1/Pus3p likely functions as a **homodimer**, with dimerization potentially important for:
- Substrate binding and positioning
- Simultaneous modification of positions 38 and 39
- Enzyme stability

## Cellular Localization

DEG1/Pus3p displays **dual localization** [PMID:9430663 "Deg1p localizes both in the nucleus and in the cytoplasm, as shown by immunofluorescence microscopy"]:

### Nuclear Localization
- Site of initial tRNA modification during tRNA maturation
- Co-localization with nascent tRNA transcripts
- Approximately 5,860 molecules/cell in log phase (from proteomic studies)

### Cytoplasmic Localization  
- May provide quality control for tRNA modifications
- Potential role in stress-responsive tRNA modification
- Could be involved in mRNA pseudouridylation

### Mitochondrial Activity
While direct mitochondrial localization remains uncertain, DEG1/Pus3p clearly modifies mitochondrial tRNAs [PMID:9430663 "lacking pseudouridines at position 38 or 39 in cytoplasmic tRNAGly and in mitochondrial tRNAArg present in DEG1-disrupted yeast strain"], suggesting either:
- Import of the protein into mitochondria
- Modification of mitochondrial tRNAs before their import
- A separate mitochondrial pool of the enzyme

## Biological Processes and Phenotypes

### Growth and Temperature Sensitivity
Deletion of DEG1 causes significant growth defects [PMID:9430663 "Disruption of the DEG1 gene is not lethal but reduces considerably the yeast growth rate, especially at an elevated temperature (37 degrees C)"]:
- **Normal conditions (30°C)**: Reduced growth rate but viable
- **Heat stress (37°C)**: Severe growth impairment
- **Cold sensitivity**: Some reports suggest cold-sensitive phenotypes

The temperature sensitivity likely reflects:
- Increased demand for properly modified tRNAs under stress
- Destabilization of unmodified tRNAs at extreme temperatures
- Impaired translation efficiency

### Translation and Protein Synthesis
Loss of Pus3-mediated pseudouridylation affects:
- **Translation fidelity**: Unmodified tRNAs may have altered codon recognition
- **Translation efficiency**: Reduced protein synthesis rates
- **Stress response**: Impaired adaptation to nutrient limitation or temperature stress

### Specific tRNA Functionality
Recent studies show that loss of DEG1/Pus3 specifically impairs **tRNAGlnUUG** function under conditions of temperature-induced down-regulation of wobble uridine thiolation [PMID: from web search "Loss of Deg1/Pus3 and concomitant elimination of pseudouridine in tRNA at positions 38 and 39 (ψ38/39) was shown to specifically impair the function of tRNAGlnUUG"].

### Regulated mRNA Pseudouridylation
The 2014 Carlile et al. study revealed that Pus3-dependent mRNA modifications are **regulated by growth conditions** [PMID:25192136]:
- Many mRNA Ψ sites are induced during post-diauxic growth
- Modification patterns change in response to nutrient availability
- Suggests a role in adapting the translatome to environmental conditions

## Evolutionary Conservation

### Cross-Species Conservation
DEG1/Pus3p is highly conserved across all domains of life:

**Bacterial ortholog (E. coli TruA)**:
- Modifies positions 38, 39, and 40 in tRNA
- Essential for growth at high temperatures
- Structural studies have revealed the catalytic mechanism

**Human ortholog (PUS3)**:
- 96% amino acid identity in the catalytic core domain
- Mutations cause intellectual disability syndrome (MRT55/NEDMIGS)
- Characterized by microcephaly, seizures, and developmental delays
- Demonstrates the fundamental importance of tRNA modification for brain development

**Conservation of function**:
- The catalytic aspartate and key sequence motifs are invariant from bacteria to humans
- Cross-species complementation is possible (human PUS3 can rescue yeast deg1Δ)
- The anticodon loop modification at positions 38/39 is universally important

### Evolutionary Adaptations
While the core function is conserved, eukaryotic Pus3 enzymes have evolved additional features:
- Extended N- and C-termini not present in bacterial orthologs
- Potential for regulated activity through post-translational modifications
- Expanded substrate repertoire (mRNA targets in addition to tRNA)

## Expression and Regulation

### Basal Expression
- Constitutively expressed under standard growth conditions
- Present at approximately 5,860 molecules/cell in log phase
- Expression levels relatively stable across different growth phases

### Transcriptional Regulation
- No specific transcription factors identified
- Likely regulated as a housekeeping gene
- May be upregulated under certain stress conditions (requires further investigation)

### Post-translational Regulation
- Potential phosphorylation sites identified in large-scale studies
- Stability and activity may be regulated by cellular stress
- No evidence for regulated degradation under normal conditions

## Genetic Interactions

### Synthetic Interactions
While specific synthetic lethal partners for DEG1 are not well-documented, potential genetic interactions may include:
- Other tRNA modification enzymes
- Translation factors
- RNA quality control pathways
- Stress response genes

### Functional Redundancy
Limited redundancy with other Pus enzymes:
- No other yeast Pus enzyme modifies positions 38/39
- Some functional overlap in supporting translation under stress
- Potential compensation through upregulation of other tRNA modifications

## Clinical Relevance and Human Disease Connection

The human ortholog PUS3 is associated with **intellectual disability syndrome** (MRT55/NEDMIGS), demonstrating that:
- tRNA modifications are critical for neurodevelopment
- The brain is particularly sensitive to translational defects
- Pseudouridine at positions 38/39 cannot be compensated by other modifications

Key features of human PUS3 deficiency:
- Severe intellectual disability
- Microcephaly
- Seizures
- Growth retardation
- Gray sclerae (in some cases)

## Recent Discoveries and Future Directions

### mRNA Modification Functions
The discovery of Pus3-dependent mRNA pseudouridylation opens new research avenues:
- Identifying specific mRNA targets and their functional significance
- Understanding the regulation of mRNA vs tRNA modification
- Exploring the role in stress responses and adaptation

### Structural Studies
Recent structural work on human PUS3 provides insights that can be applied to understanding the yeast enzyme:
- Substrate recognition mechanisms
- Basis for position 38/39 specificity
- Potential for developing specific inhibitors

### Systems Biology Approaches
Integration of DEG1/Pus3 function into larger cellular networks:
- Role in the epitranscriptome
- Connections to cellular stress responses
- Interactions with other RNA modification pathways

## Key Publications

1. **Lecointe et al., 1998** [PMID:9430663]: Foundational characterization of DEG1 as Pus3, demonstrating its role in modifying positions 38/39 in tRNA

2. **Carlile et al., 2014** [PMID:25192136]: Discovery of mRNA pseudouridylation by Pus3 and other synthases, revealing regulated modification in response to growth conditions

3. **Agostoni Carbone et al., 1991** [PMID:2036682]: Initial identification of DEG1 as important for growth in S. cerevisiae

4. **Ghaemmaghami et al., 2003** [PMID:14562106]: Quantification of Pus3 protein levels in yeast cells

## Summary

DEG1/Pus3p is a critical tRNA pseudouridine synthase that modifies positions 38 and 39 in the anticodon loop of tRNAs, with additional roles in mRNA modification. Its function is essential for:
- Maintaining translation efficiency and fidelity
- Cellular adaptation to stress conditions
- Normal growth, especially at elevated temperatures

The high evolutionary conservation from bacteria to humans, coupled with the severe phenotypes associated with its loss in both yeast and humans, underscores the fundamental importance of this enzyme in cellular biology. Recent discoveries of its role in mRNA modification suggest that DEG1/Pus3p may have broader functions in post-transcriptional gene regulation than previously appreciated.

The temperature-sensitive phenotype of deg1Δ yeast and the neurological defects in humans with PUS3 mutations highlight the particular importance of pseudouridine modifications in maintaining cellular homeostasis under stress and supporting the high translational demands of metabolically active tissues like the brain.