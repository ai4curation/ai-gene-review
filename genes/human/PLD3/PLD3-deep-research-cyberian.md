---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:52:44.262968'
end_time: '2026-01-23T16:52:44.264797'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PLD3
  gene_symbol: PLD3
  uniprot_accession: Q8IV08
  protein_description: 'RecName: Full=5''-3'' exonuclease PLD3 {ECO:0000305}; EC=3.1.16.1
    {ECO:0000269|PubMed:30111894, ECO:0000269|PubMed:30312375}; AltName: Full=(S,S)-bis(monoacylglycero)phosphate
    synthase PLD3 {ECO:0000305|PubMed:39423811}; EC=3.1.4.- {ECO:0000269|PubMed:39423811};
    AltName: Full=HindIII K4L homolog; AltName: Full=Hu-K4 {ECO:0000303|PubMed:15794758};
    AltName: Full=Phospholipase D3;'
  gene_info: Name=PLD3 {ECO:0000303|PubMed:26411346, ECO:0000312|HGNC:HGNC:17158};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the phospholipase D family. .
  protein_domains: Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase.
    (IPR001736); PLDc_3 (PF13918)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8IV08
- **Protein Description:** RecName: Full=5'-3' exonuclease PLD3 {ECO:0000305}; EC=3.1.16.1 {ECO:0000269|PubMed:30111894, ECO:0000269|PubMed:30312375}; AltName: Full=(S,S)-bis(monoacylglycero)phosphate synthase PLD3 {ECO:0000305|PubMed:39423811}; EC=3.1.4.- {ECO:0000269|PubMed:39423811}; AltName: Full=HindIII K4L homolog; AltName: Full=Hu-K4 {ECO:0000303|PubMed:15794758}; AltName: Full=Phospholipase D3;
- **Gene Information:** Name=PLD3 {ECO:0000303|PubMed:26411346, ECO:0000312|HGNC:HGNC:17158};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the phospholipase D family. .
- **Key Domains:** Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase. (IPR001736); PLDc_3 (PF13918)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PLD3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PLD3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PLD3** (gene ID: PLD3, UniProt: Q8IV08) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PLD3 (Phospholipase D3): A Comprehensive Review

## Introduction

Phospholipase D3 (PLD3), encoded by the PLD3 gene on human chromosome 19q13.2, represents a fascinating case of misleading nomenclature in molecular biology. Despite being assigned to the phospholipase D family based on sequence homology to viral K4L proteins and the presence of characteristic HKD catalytic motifs, PLD3 has been definitively shown to function primarily as a 5'-3' exonuclease rather than a phospholipase[gavin-2018-exonuclease-abstract]. This lysosomal enzyme degrades single-stranded DNA and RNA substrates and was recently discovered to also synthesize bis(monoacylglycero)phosphate (BMP), a critical lysosomal lipid[singh-2024-bmp-abstract]. PLD3 has attracted significant attention due to its genetic association with late-onset Alzheimer's disease[cruchaga-2014-alzheimer-abstract] and spinocerebellar ataxia type 46[nibbeling-2017-sca46-abstract], positioning it at the intersection of nucleic acid metabolism, lipid homeostasis, and neurodegeneration.

The history of PLD3 research spans more than five decades. In 1968, Bernardi and Bernardi purified and characterized an acidic ssDNA-specific 5' DNase from bovine spleen, which they termed "spleen exonuclease"[bernardi-1968-spleen-abstract]. However, the gene encoding this enzyme remained unidentified for 50 years until 2018, when Gavin et al. demonstrated that PLD3 (and its paralogue PLD4) possess 5' exonuclease activity indistinguishable from classical spleen exonuclease and detected PLD3 in commercial preparations of this enzyme[gavin-2018-exonuclease-abstract]. This discovery represented a paradigm shift in understanding PLD3 function, transforming it from a presumed phospholipase of unknown activity into a key regulator of lysosomal nucleic acid metabolism and innate immunity.

## The Phospholipase D Family: PLD3 in Context

The mammalian phospholipase D (PLD) family comprises six members (PLD1-PLD6), which share the characteristic HxKxxxxD (HKD) catalytic motif but have diverged substantially in function and localization. PLD1 and PLD2 are the classical cytosolic phospholipases, catalyzing hydrolysis of phosphatidylcholine to generate phosphatidic acid and choline, thereby mediating critical intracellular signaling pathways. These enzymes share approximately 53% sequence homology and require phosphatidylinositol 4,5-bisphosphate (PIP2) as a cofactor. Both contain PX (phox homology) and PH (pleckstrin homology) domains that regulate their membrane association and subcellular dynamics during signal transduction.

In contrast, PLD3 and PLD4 represent a functionally distinct subgroup within the family. While they retain the paired HKD motifs characteristic of the superfamily, they lack the PX and PH domains present in PLD1 and PLD2. More fundamentally, PLD3 and PLD4 function as 5'-to-3' exonucleases rather than phospholipases[gavin-2018-exonuclease-abstract]. These enzymes are glycosylated type II transmembrane proteins that localize to endolysosomes, in contrast to the primarily cytosolic distribution of PLD1 and PLD2. Structural analysis confirms that critical residues required for phospholipase activity are not conserved in PLD3[ishii-2024-structure-abstract], providing a molecular explanation for this functional divergence.

The products of PLD3 and PLD4 nuclease activity also differ from other nucleases in the PLD superfamily. While enzymes such as PLD6 (Zucchini), Nuc, and BfiI generate products with 5'-phosphate and 3'-hydroxyl termini, PLD3 and PLD4 produce fragments with 5'-hydroxyl and 3'-phosphate[gavin-2018-exonuclease-abstract]. This allows them to further process the products of RNase T2 and DNase II, which generate 5'-OH nucleotides, positioning PLD3/4 as terminal degradative enzymes in lysosomal nucleic acid catabolism.

PLD3 and PLD4 exhibit complementary tissue expression patterns. PLD4 is highly expressed in dendritic cells and other myeloid cells, with lower expression in B cells. PLD3 is more broadly expressed, with highest levels in the brain, followed by thymus. In some tissues such as spleen and liver during early development, PLD3 and PLD4 expression levels are comparable and exceed those of PLD1 and PLD2[gavin-2018-exonuclease-abstract].

## Tissue Expression and Cellular Distribution

PLD3 exhibits a distinctive tissue expression pattern with notable enrichment in neuroendocrine tissues. According to Human Protein Atlas data, the pituitary gland shows the highest RNA expression levels (672.4 nTPM), classifying PLD3 as "tissue enhanced" for this endocrine organ. Brain regions consistently demonstrate elevated PLD3 levels, particularly the hypothalamus (391.2 nTPM), cerebral cortex (359.4 nTPM), basal ganglia (278 nTPM), and hippocampal formation (261.1 nTPM). This brain-enriched expression pattern is significant given PLD3's association with neurodegenerative diseases.

At the cellular level, PLD3 displays cytoplasmic expression at variable levels in most cell types, with the highest abundance in neuronal cells and immune cells. Within the brain, nearly all cortical neurons, hippocampal pyramidal neurons, and dentate gyrus granule cells express intense PLD3 immunoreactivity, with the protein concentrated in the cytoplasm forming fine granular structures enriched in the soma and proximal neurites[satoh-2014-plaques-abstract]. A subset of pericytes surrounding capillaries also express PLD3. Notably, reactive astrocytes and activated microglia do not express PLD3, even when accumulated around senile plaques in Alzheimer's disease brains[satoh-2014-plaques-abstract].

The subcellular distribution of PLD3 reflects its trafficking pathway and functional roles. While newly synthesized PLD3 can be detected in the endoplasmic reticulum, the mature functional form localizes primarily to lysosomes. Immunohistochemistry in human tissue demonstrates strong colocalization with lysosomal markers including LAMP2, cathepsin B, cathepsin D, and progranulin[nackenoff-2021-lysosomal-abstract]. This lysosomal localization is consistent with PLD3's acidic pH optimum and its role in terminal nucleic acid degradation.

## Protein Structure and Domain Organization

Human PLD3 is a 490-amino acid type II transmembrane protein, first characterized in detail by Munck et al. in 2005 under the name Hu-K4[munck-2005-huk4-abstract]. The protein consists of a short N-terminal cytoplasmic tail (residues 1-36), a single transmembrane domain (residues 37-59), and a large C-terminal luminal domain (residues 60-490) that contains the two characteristic phospholipase D superfamily HKD motifs[roske-2024-structure-abstract]. The type II topology ensures that the catalytically active C-terminal domain resides within the lumen of the endolysosomal system.

Recent crystallographic studies have provided detailed structural insights into PLD3. Roske et al. determined the structure of the human PLD3 luminal domain at 1.9 Å resolution, revealing a typical phospholipase fold organized as a bilobal architecture[roske-2024-structure-abstract]. Ishii et al. independently solved the structure at 2.3 Å resolution, confirming the bilobal organization with the catalytic site positioned between the lobes[ishii-2024-structure-abstract]. A striking finding from both structural studies is that while PLD3 retains the overall fold of the phospholipase D superfamily, the critical residues required for phospholipase activity are either not conserved or entirely absent[ishii-2024-structure-abstract]. This structural evidence definitively explains why PLD3 lacks phospholipase activity despite belonging to this enzyme family.

PLD3 forms homodimers through a newly identified dimerization interface involving helices α10 and α11, creating an interface area of approximately 1042 Å²[roske-2024-structure-abstract]. This dimeric architecture positions the two N-termini (where the transmembrane domains connect in the full-length protein) pointing in the same direction, enabling proper membrane anchoring. Each dimer contains two independent catalytic centers, doubling the enzyme's nuclease capacity. The active site is formed by residues from two HKD motifs: H201, K203, and D208 from the first motif oppose H416, K418, and E423 from the second motif at the pseudo-dimer interface[roske-2024-structure-abstract].

## Enzymatic Activities and Catalytic Mechanism

### Exonuclease Activity

The primary enzymatic function of PLD3 is as a 5'-to-3' exonuclease that hydrolyzes the phosphodiester bonds of single-stranded DNA and RNA substrates[gavin-2018-exonuclease-abstract]. The enzyme cleaves nucleotides sequentially from the 5' end, releasing nucleoside 3'-monophosphates as products. PLD3 exhibits several key characteristics that define its substrate specificity: it requires unphosphorylated 5' ends, lacks endonuclease activity, and operates optimally at acidic pH (below 6) consistent with its endolysosomal localization[gavin-2018-exonuclease-abstract]. The enzyme can still function at neutral pH 7, albeit with reduced efficiency. Importantly, PLD3 cleaves single-stranded RNA with similar efficiency to ssDNA[gavin-2021-dna-rna-abstract].

The catalytic mechanism of PLD3 proceeds via a classical phospholipase D superfamily ping-pong reaction involving a covalent phosphohistidine intermediate[roske-2024-structure-abstract]. In the first step, H416 (using PLD3 numbering) attacks the phosphodiester bond of the substrate, forming a phospho-histidine intermediate while H201 protonates the leaving 5'-OH nucleic acid fragment. In the second step, the now-deprotonated H201 accepts a proton from an attacking water molecule, which hydrolyzes the phospho-histidine intermediate to release the nucleoside 3'-monophosphate product. Structural snapshots of PLD4, a close paralogue, captured intermediate states that confirmed this mechanism and unexpectedly revealed phosphatase activity capable of removing 5'-phosphate groups via the same phosphohistidine intermediate.

The crystal structure of PLD3 in complex with ssDNA reveals key substrate-binding features[roske-2024-structure-abstract]. The first 5'-thymidine of the substrate undergoes hydrophobic stacking against Tyr411, with additional stabilization through hydrogen bonding interactions. This binding mode positions the phosphodiester bond appropriately for nucleophilic attack by the catalytic histidine.

### BMP Synthase Activity

A remarkable 2024 discovery by Singh et al. revealed that PLD3 (along with PLD4) possesses a second, mechanistically distinct enzymatic activity: the synthesis of (S,S)-bis(monoacylglycero)phosphate (S,S-BMP)[singh-2024-bmp-abstract]. BMP is an abundant and unique lysosomal phospholipid essential for the degradation of lipids, particularly gangliosides. Unlike typical glycerophospholipids that contain glycerol in the R stereo-configuration, lysosomal BMP possesses two chiral glycerol carbons in the S configuration, which protects it from lysosomal degradative enzymes.

How this unusual stereochemistry was achieved had been a 50-year mystery. Singh et al. demonstrated that PLD3 and PLD4 catalyze the critical glycerol stereo-inversion reaction required for S,S-BMP synthesis[singh-2024-bmp-abstract]. Deletion of PLD3 markedly reduced BMP levels in brain tissue (where PLD3 is highly expressed), while PLD4 deletion reduced BMP in spleen (where PLD4 predominates). Loss of either enzyme led to gangliosidosis and lysosomal abnormalities. Critically, disease-associated PLD3 variants (including those linked to Alzheimer's disease and spinocerebellar ataxia) showed diminished BMP synthase activity, suggesting this function may be mechanistically important for neurodegeneration.

## Subcellular Localization and Trafficking

PLD3 is a resident lysosomal protein that reaches its destination through an unconventional trafficking pathway[roske-2024-structure-abstract]. The protein is synthesized as an N-glycosylated type II transmembrane protein in the endoplasmic reticulum. Munck et al. initially observed PLD3 localization to the ER when expressed exogenously[munck-2005-huk4-abstract], but subsequent studies clarified that the mature, active form localizes to endolysosomes.

Trafficking to lysosomes depends on the ESCRT (endosomal sorting complex required for transport) machinery, representing an uncommon biosynthetic route for mammalian lysosomal proteins. Upon reaching acidic compartments, PLD3 undergoes proteolytic processing by an as-yet-unidentified protease, releasing the soluble luminal domain[roske-2024-structure-abstract]. Mass spectrometry analysis identified Gln72 as the neo-N-terminus after processing, with this glutamine residue modified to pyroglutamate through spontaneous cyclization, forming a stable N-terminus.

PLD3 also participates in endosomal trafficking beyond its role as a lysosomal enzyme. Mukadam et al. demonstrated that PLD3 co-localizes with amyloid precursor protein (APP) in endosomes and regulates endosomal protein sorting[mukadam-2018-endosome-abstract]. Loss of PLD3 function reduces endosomal tubules, impairs trafficking of multiple membrane proteins, and disrupts the association between sortilin-like receptor 1 (SorL1) and APP. This endosomal sorting function appears distinct from, though potentially related to, PLD3's catalytic activities.

## Role in Innate Immunity and Inflammation

A critical physiological function of PLD3 is the negative regulation of nucleic acid-sensing toll-like receptors (TLRs) within the endolysosomal system[gavin-2018-exonuclease-abstract][gavin-2021-dna-rna-abstract]. By degrading single-stranded DNA and RNA that enters lysosomes, PLD3 limits the activation of TLR9 (which recognizes unmethylated CpG DNA) and TLR7 (which recognizes ssRNA). This regulatory function prevents excessive inflammatory responses to endogenous nucleic acids.

The immunological importance of PLD3 became strikingly apparent in knockout mouse studies. While Pld3-/- mice show exaggerated TLR9 responses but are viable, combined Pld3-/-Pld4-/- double knockout mice develop fatal hemophagocytic lymphohistiocytosis (HLH) within the first weeks of life[gavin-2018-exonuclease-abstract]. This severe autoinflammatory condition is characterized by inflammatory liver damage and overproduction of interferon-γ. The accumulation of undegraded nucleic acids constitutively activates both TLR7 and TLR9 signaling through NF-κB[gavin-2021-dna-rna-abstract].

Importantly, PLD3 and PLD4 also regulate cytoplasmic nucleic acid sensing through the cGAS-STING pathway. When lysosomal PLD3 is deficient, accumulated nucleic acids (particularly mitochondrial DNA) can leak to the cytosol, activating STING and triggering type I interferon responses[gavin-2021-dna-rna-abstract][van-acker-2023-mtdna-abstract]. This represents a second tier of innate immune surveillance that becomes aberrantly activated when lysosomal nucleotide catabolism fails.

## Connection to Alzheimer's Disease

PLD3 gained prominence in the neurodegeneration field when Cruchaga et al. reported in 2014 that rare coding variants in PLD3 confer risk for late-onset Alzheimer's disease (LOAD)[cruchaga-2014-alzheimer-abstract]. Using whole-exome sequencing in 14 families with LOAD, they identified the V232M variant (rs145999145) that segregated with disease in two independent families and approximately doubled Alzheimer's risk across seven case-control series comprising over 11,000 participants of European descent (OR=2.10, CI=1.47-2.99). PLD3 is highly expressed in brain regions vulnerable to Alzheimer's pathology, including the hippocampus and cortex, and expression is significantly reduced in neurons from AD brains compared to controls[cruchaga-2014-alzheimer-abstract]. However, subsequent replication studies yielded mixed results, and meta-analyses have suggested a more modest effect size (OR approximately 1.53 in larger cohorts).

### Accumulation on Neuritic Plaques

A striking neuropathological observation is that PLD3 accumulates on neuritic plaques in Alzheimer's disease brains[satoh-2014-plaques-abstract]. Immunohistochemical studies revealed numerous senile plaques containing swollen dystrophic neurites with intense PLD3 immunoreactivity in the frontal cortex of AD patients. In contrast, PLD3-labeled senile plaques were barely found in age-matched non-AD control brains. This accumulation occurs specifically within neuronal elements; reactive astrocytes and activated microglia at the center and periphery of senile plaques do not express PLD3[satoh-2014-plaques-abstract].

Nackenoff et al. provided additional evidence that PLD3 enrichment occurs within lysosomal accumulations in dystrophic neurites surrounding β-amyloid plaques[nackenoff-2021-lysosomal-abstract]. This pattern was conserved across both human AD brain specimens and the 5xFAD mouse model. Interestingly, higher prefrontal cortex PLD3 expression correlated inversely with β-amyloid plaque burden in the ROS/MAP human cohort, suggesting that PLD3 may have a protective role and that reduced expression contributes to pathology.

### Axonal Spheroids and Network Dysfunction

A major 2022 study in Nature by Yuan et al. established a mechanistic link between PLD3 and axonal pathology in AD[yuan-2022-spheroids-abstract]. They demonstrated that amyloid-plaque-associated axonal spheroids significantly disrupt neural network function through conduction blockades, acting as electrical current sinks that progressively impair action potential transmission. PLD3 was found to be highly enriched in these axonal spheroids, and the accumulation of abnormal endolysosomal vesicles correlated with spheroid expansion.

Critically, the study showed that neuronal overexpression of PLD3 triggered endolysosomal vesicle accumulation and spheroid enlargement, worsening axonal conduction blockades. Conversely, PLD3 deletion reduced both endolysosomal vesicles and spheroid size, leading to improved electrical conduction and enhanced neural network function[yuan-2022-spheroids-abstract]. This suggests that targeted modulation of PLD3 or endolysosomal biogenesis could potentially reverse axonal spheroid-induced neural circuit abnormalities independently of amyloid removal.

### Mechanistic Pathways

Multiple mechanistic pathways link PLD3 dysfunction to neurodegeneration. Van Acker et al. identified mitochondrial DNA (mtDNA) as a major physiological substrate of PLD3 in neurons[van-acker-2023-mtdna-abstract]. In PLD3-deficient cells, mtDNA accumulates in lysosomes, creating a degradative bottleneck visible as abundant multilamellar bodies containing mitochondrial remnants. This triggers increased PINK1-dependent mitophagy. When mtDNA leaks from compromised lysosomes to the cytosol, it activates cGAS-STING signaling, which upregulates autophagy and induces accumulation of APP C-terminal fragments (APP-CTF) and cholesterol. Notably, STING inhibition largely normalized APP-CTF levels, while APP knockout reduced STING activation, revealing reciprocal regulatory relationships.

The V232M substitution has been shown to impair O-glycosylation at pT271, a post-translational modification essential for normal trafficking and localization, leading to enlarged lysosomes. Nackenoff et al. also found that the V232M variant eliminates phospholipase D enzymatic activity in lysosomes[nackenoff-2021-lysosomal-abstract]. Thus, the AD-associated variant may cause disease through effects on multiple PLD3 functions including enzymatic activity and lysosomal localization.

The 2024 discovery of BMP synthase activity adds another dimension[singh-2024-bmp-abstract]. AD-associated PLD3 variants showed reduced BMP synthesis capacity. Since BMP is essential for ganglioside degradation, impaired PLD3 function could lead to ganglioside accumulation and lysosomal dysfunction, representing a lipid-centric mechanism complementary to the nucleic acid-focused pathways. Additionally, PLD3 was found to interact with progranulin (PGRN), another lysosomal protein implicated in neurodegeneration[satoh-2014-plaques-abstract], suggesting potential functional crosstalk.

## Spinocerebellar Ataxia Type 46

In 2017, Nibbeling et al. identified PLD3 as the causative gene for spinocerebellar ataxia type 46 (SCA46), a rare autosomal dominant cerebellar ataxia[nibbeling-2017-sca46-abstract]. In a Dutch family (RF28), they identified the heterozygous L308P mutation (c.923T>C) that segregated with disease in eight affected family members. The mutation affects a highly conserved residue within the second PLD phosphodiesterase domain.

SCA46 presents clinically as adult-onset sensory ataxic neuropathy with cerebellar signs, typically beginning between ages 41-65 years (average 53.5 years)[nibbeling-2017-sca46-abstract]. Patients present with swaying during walking in the dark, with additional features including oculomotor abnormalities, cerebellar dysarthria, and distal sensory impairment in a stocking-and-glove pattern. A case report identified a younger patient with onset at 13 years presenting with sensorineural hearing loss followed by pancerebellar ataxia, optic atrophy, and sensorimotor axonal neuropathy.

The pathogenic mechanism of PLD3 mutations in SCA46 has been debated. Gonzalez et al. generated PLD3 knockout mice that did not develop cerebellar degeneration, challenging a simple loss-of-function model[gonzalez-2018-sca46-abstract]. However, they demonstrated that the L308P mutation causes retention of PLD3 in the endoplasmic reticulum rather than proper lysosomal localization, resulting in loss of exonuclease function at its normal site of action. This suggests that the disease mechanism may involve loss of lysosomal function combined with potential ER stress from protein accumulation, rather than simple haploinsufficiency.

Singh et al. showed that SCA46-associated mutations also reduce BMP synthase activity[singh-2024-bmp-abstract], providing an additional mechanistic link between PLD3 dysfunction and neurodegeneration through impaired lysosomal lipid homeostasis.

## Autoimmune and Autoinflammatory Associations

Genome-wide association studies have linked PLD4 (the PLD3 paralogue) to autoimmune diseases including rheumatoid arthritis and systemic sclerosis[gavin-2018-exonuclease-abstract]. While PLD3 itself has not been directly implicated in classical autoimmune conditions in human GWAS, the severe autoinflammatory phenotype of Pld3-/-Pld4-/- mice demonstrates its importance in preventing aberrant immune activation.

More recently, loss-of-function mutations in PLD4 were shown to cause systemic lupus erythematosus (SLE) in humans, highlighting the clinical relevance of defective lysosomal nucleic acid degradation in autoimmunity. Given the functional redundancy between PLD3 and PLD4, variants affecting both paralogues could potentially modify autoimmune disease risk or severity.

The dual regulation of TLR7/TLR9 and STING pathways by PLD3 has therapeutic implications[gavin-2021-dna-rna-abstract]. Understanding how lysosomal nucleases control nucleic acid-driven inflammation may enable new treatments for conditions ranging from systemic autoimmunity to neurodegenerative diseases with inflammatory components.

## Open Questions

Several important questions remain regarding PLD3 biology:

1. **Relative importance of enzymatic activities**: PLD3 possesses both exonuclease and BMP synthase activities. What is the relative contribution of each to its physiological functions and disease associations? Can these activities be genetically or pharmacologically separated?

2. **Substrate specificity in vivo**: While mtDNA has been identified as a major neuronal substrate, the full spectrum of physiological PLD3 substrates (including specific RNA species) remains incompletely characterized. What determines substrate selectivity in different cell types?

3. **Mechanism of neurodegeneration**: Multiple pathways connect PLD3 dysfunction to neurodegeneration (nucleic acid accumulation, STING activation, BMP deficiency, endosomal trafficking defects, APP processing, axonal spheroid formation). Which pathway(s) are primary drivers, and do they interact?

4. **SCA46 pathogenesis**: Why does the L308P mutation cause a predominantly cerebellar phenotype when PLD3 is broadly expressed? What cell-autonomous versus non-cell-autonomous mechanisms contribute?

5. **Therapeutic potential**: Can PLD3 or its downstream pathways be targeted therapeutically? Would STING inhibitors, BMP supplementation, or modulation of endolysosomal biogenesis benefit patients with PLD3-associated diseases? The finding that PLD3 deletion improves network function in AD models suggests reduction of PLD3 activity might be beneficial in some contexts.

6. **Regulatory mechanisms**: How is PLD3 expression and activity regulated? What controls its proteolytic processing and activation in lysosomes?

7. **Relationship to aging**: Does PLD3 function decline with age, potentially contributing to late-onset disease phenotypes?

8. **Progranulin interaction**: What is the functional significance of PLD3-progranulin interaction in lysosomes, and how does this relate to frontotemporal dementia caused by progranulin mutations?

## References

- [bernardi-1968-spleen-abstract]: Bernardi A, Bernardi G. Studies on acid hydrolases. IV. Isolation and characterization of spleen exonuclease. *Biochimica et Biophysica Acta*. 1968;155(2):360-370. doi: 10.1016/0005-2744(68)90018-5

- [munck-2005-huk4-abstract]: Munck A, Böhm C, Seibel NM, Hashemol Hosseini Z, Hampe W. Hu-K4 is a ubiquitously expressed type 2 transmembrane protein associated with the endoplasmic reticulum. *FEBS Journal*. 2005 Apr;272(7):1718-26. doi: 10.1111/j.1742-4658.2005.04601.x. PMID: 15794758

- [cruchaga-2014-alzheimer-abstract]: Cruchaga C, Karch CM, Jin SC, et al. Rare coding variants in the phospholipase D3 gene confer risk for Alzheimer's disease. *Nature*. 2014 Jan 23;505(7484):550-4. doi: 10.1038/nature12825. PMID: 24336208; PMCID: PMC4050701

- [satoh-2014-plaques-abstract]: Satoh J, Kino Y, Yamamoto Y, et al. PLD3 is accumulated on neuritic plaques in Alzheimer's disease brains. *Alzheimer's Research & Therapy*. 2014 Nov 2;6(9):70. doi: 10.1186/s13195-014-0070-5. PMID: 25478031; PMCID: PMC4255636

- [nibbeling-2017-sca46-abstract]: Nibbeling EAR, Duarri A, Verschuuren-Bemelmans CC, et al. Exome sequencing and network analysis identifies shared mechanisms underlying spinocerebellar ataxia. *Brain*. 2017 Nov 1;140(11):2860-2878. doi: 10.1093/brain/awx251. PMID: 29053787; PMCID: PMC5841203

- [gavin-2018-exonuclease-abstract]: Gavin AL, Huang D, Huber C, et al. PLD3 and PLD4 are single-stranded acid exonucleases that regulate endosomal nucleic-acid sensing. *Nature Immunology*. 2018 Sep;19(9):942-953. doi: 10.1038/s41590-018-0179-y. PMID: 30111894; PMCID: PMC6105523

- [gonzalez-2018-sca46-abstract]: Gonzalez AC, Stroobants S, Reisdorf P, et al. PLD3 and spinocerebellar ataxia. *Brain*. 2018 Nov 1;141(11):e78. doi: 10.1093/brain/awy258. PMID: 30312375; PMCID: PMC6202572

- [mukadam-2018-endosome-abstract]: Mukadam AS, Breusegem SY, Seaman MNJ. Analysis of novel endosome-to-Golgi retrieval genes reveals a role for PLD3 in regulating endosomal protein sorting and amyloid precursor protein processing. *Cellular and Molecular Life Sciences*. 2018 Jul;75(14):2613-2625. doi: 10.1007/s00018-018-2752-9. PMID: 29368044; PMCID: PMC6003983

- [gavin-2021-dna-rna-abstract]: Gavin AL, Huang D, Blane TR, et al. Cleavage of DNA and RNA by PLD3 and PLD4 limits autoinflammatory triggering by multiple sensors. *Nature Communications*. 2021 Oct 7;12(1):5874. doi: 10.1038/s41467-021-26150-w. PMID: 34620855; PMCID: PMC8497607

- [nackenoff-2021-lysosomal-abstract]: Nackenoff AG, Hohman TJ, Neuner SM, et al. PLD3 is a neuronal lysosomal phospholipase D associated with β-amyloid plaques and cognitive function in Alzheimer's disease. *PLOS Genetics*. 2021 Apr 8;17(4):e1009406. doi: 10.1371/journal.pgen.1009406. PMID: 33830999; PMCID: PMC8031396

- [yuan-2022-spheroids-abstract]: Yuan P, Zhang M, Tong L, et al. PLD3 affects axonal spheroids and network defects in Alzheimer's disease. *Nature*. 2022 Dec;612(7939):328-337. doi: 10.1038/s41586-022-05491-6. PMID: 36450991

- [van-acker-2023-mtdna-abstract]: Van Acker ZP, Perdok A, Hellemans R, et al. Phospholipase D3 degrades mitochondrial DNA to regulate nucleotide signaling and APP metabolism. *Nature Communications*. 2023 May 24;14(1):2847. doi: 10.1038/s41467-023-38501-w. PMID: 37225734; PMCID: PMC10209153

- [roske-2024-structure-abstract]: Roske Y, Cappel C, Cremer N, et al. Structural analysis of PLD3 reveals insights into the mechanism of lysosomal 5' exonuclease-mediated nucleic acid degradation. *Nucleic Acids Research*. 2024 Jan 11;52(1):370-384. doi: 10.1093/nar/gkad1114. PMID: 37994783; PMCID: PMC10783504

- [ishii-2024-structure-abstract]: Ishii K, Hermans SJ, Georgopoulou ME, et al. Crystal structure of Alzheimer's disease phospholipase D3 provides a molecular basis for understanding its normal and pathological functions. *FEBS Journal*. 2024 Dec;291(24):5398-5419. doi: 10.1111/febs.17277. PMID: 39325669; PMCID: PMC11653685

- [singh-2024-bmp-abstract]: Singh S, Dransfeld UE, Ambaw YA, et al. PLD3 and PLD4 synthesize S,S-BMP, a key phospholipid enabling lipid degradation in lysosomes. *Cell*. 2024 Oct 17;187(21):6820-6834.e18. doi: 10.1016/j.cell.2024.09.020. PMID: 39423811


## Citations

1. bernardi-1968-spleen-abstract.md
2. cruchaga-2014-alzheimer-abstract.md
3. gavin-2018-exonuclease-abstract.md
4. gavin-2021-dna-rna-abstract.md
5. gonzalez-2018-sca46-abstract.md
6. ishii-2024-structure-abstract.md
7. mukadam-2018-endosome-abstract.md
8. munck-2005-huk4-abstract.md
9. nackenoff-2021-lysosomal-abstract.md
10. nibbeling-2017-sca46-abstract.md
11. roske-2024-structure-abstract.md
12. satoh-2014-plaques-abstract.md
13. singh-2024-bmp-abstract.md
14. van-acker-2023-mtdna-abstract.md
15. yuan-2022-spheroids-abstract.md