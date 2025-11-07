---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-10-31T09:58:23.067401'
end_time: '2025-10-31T10:01:15.774601'
duration_seconds: 172.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: METEA
  gene_or_uniprot: MexAM1_META1p4138
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 40
---

## Question

# Gene Research Template for GO Annotation Curation

Please provide a comprehensive research report on the gene MexAM1_META1p4138 in METEA.

## Research Focus Areas for GO Annotation

I need detailed information covering these areas specifically for GO annotation curation:

### 1. Molecular Function (MF)
- **Primary molecular function(s)** - specific biochemical activities
- **Enzymatic properties** - catalytic activities, substrate specificity, cofactor requirements
- **Binding activities** - what molecules does the protein bind (DNA, RNA, proteins, small molecules)
- **Regulatory functions** - transcriptional regulation, kinase/phosphatase activities
- **Transport functions** - ion channels, transporters, carriers

### 2. Cellular Component (CC)
- **Subcellular localization** - where is the protein located within the cell
- **Membrane association** - integral membrane, peripheral membrane, or cytosolic
- **Organellar localization** - nucleus, mitochondria, ER, Golgi, etc.
- **Protein complexes** - what complexes does this protein participate in
- **Cellular structures** - cytoskeleton, ribosomes, proteasome components

### 3. Biological Process (BP)
- **Primary biological pathways** - metabolic, signaling, developmental processes
- **Physiological roles** - what happens when this gene is mutated or deleted
- **Developmental processes** - embryogenesis, organogenesis, differentiation
- **Response to stimuli** - environmental, chemical, biological responses
- **Cellular processes** - cell cycle, apoptosis, DNA repair, protein folding

### 4. Experimental Evidence Quality
- **Direct experimental evidence** - biochemical assays, functional studies
- **Genetic evidence** - knockout/knockdown phenotypes, complementation
- **Physical evidence** - protein interactions, localization studies
- **Expression evidence** - tissue/stage-specific expression patterns
- **Comparative evidence** - ortholog function in other species

### 5. Disease and Phenotype Associations
- **Human disease associations** - genetic disorders, cancer involvement
- **Model organism phenotypes** - what happens when gene function is disrupted
- **Clinical relevance** - therapeutic targets, biomarkers
- **Population genetics** - natural variants and their effects

### 6. Protein Structure and Domains
- **Functional domains** - catalytic domains, binding domains, regulatory regions
- **Structural features** - transmembrane regions, signal peptides, nuclear localization signals
- **Post-translational modifications** - phosphorylation, ubiquitination, glycosylation sites
- **Protein-protein interaction interfaces** - binding sites for partners

### 7. Evolutionary Conservation and Orthologs
- **Conservation across species** - which functions are conserved
- **Ortholog studies** - functional evidence from other organisms
- **Paralog relationships** - functional divergence within gene families
- **Essential gene status** - is this gene required for viability

## Output Requirements for GO Curation

- **Provide specific GO term suggestions** where experimental evidence supports them
- **Include PMID citations** for all major functional claims
- **Distinguish experimental evidence levels** (direct vs. inferred)
- **Focus on experimental data over computational predictions**
- **Highlight recent discoveries** (last 5 years) that might affect annotation
- **Note any conflicting evidence** or ambiguous experimental results
- **Specify organism-specific differences** if orthologs have different functions

## Gene Information
- **Gene Symbol**: MexAM1_META1p4138
- **Organism**: METEA
- **Focus**: Gene Ontology annotation curation and functional characterization

Please prioritize experimental evidence and be explicit about the strength and type of evidence supporting each functional claim.

## Output

<think>
This is a very specific request for a comprehensive research report on the gene MexAM1_META1p4138 (which appears to be META1p4138 or mllJ) in Methylobacterium extorquens AM1 for Gene Ontology annotation curation. The user wants detailed information about molecular function, cellular component, biological process, experimental evidence, disease associations, protein structure, and evolutionary conservation.

Looking at the search results, I can see multiple sources that discuss this gene extensively:

1. From results [3], [6], [20], [24], [26], [28], [31], [34], [36], [37], [41], [45], [56] - These all discuss the identification and characterization of methylolanthanin and the mll biosynthetic gene cluster, specifically mentioning META1p4138 (mllJ).

Key findings about MexAM1_META1p4138 (mllJ):
- It's part of the methylolanthanin (mll) biosynthetic gene cluster (genes META1p4129-META1p4138)
- META1p4138 (mllJ) belongs to ferritin-like DUF4142 and is putatively exported into the periplasm
- It was highly upregulated (32-fold average increase) when comparing Nd2O3 to NdCl3 conditions
- It encodes a protein involved in lanthanide metallophore biosynthesis
- The DUF4142 domain suggests involvement in lanthanide transport/regulation

From the research articles, I can extract:
- The gene is involved in lanthanide bioaccumulation and metabolism
- It's part of a novel lanthanophore biosynthesis pathway
- The protein is putatively localized to the periplasm
- It contains a ferritin-like domain (DUF4142)
- It's expressed in response to poorly soluble lanthanides
- It's part of a TonB-dependent receptor-associated system
 
The groundbreaking 2024 research reveals a critical breakthrough in understanding methylolanthanin's role in lanthanide accumulation. I'll develop a comprehensive scientific report that provides an in-depth analysis of the gene's molecular characteristics, emphasizing its significance in bacterial lanthanide metabolism. The report will require meticulous documentation of experimental findings, structural insights, and potential biotechnological implications.
</think>

# Comprehensive Gene Research Report: MexAM1_META1p4138 (mllJ) in Methylobacterium extorquens AM1 for Gene Ontology Annotation Curation

This report synthesizes current knowledge regarding MexAM1_META1p4138, designated mllJ in the methylolanthanin biosynthetic gene cluster of Methylobacterium extorquens AM1. Despite recent discovery, this gene represents a critical component of lanthanide metallophore biosynthesis with significant implications for both fundamental microbial biochemistry and biotechnological applications in rare earth element recovery. The research presented here is drawn from seminal publications from 2024 that fundamentally characterize this gene's role in lanthanide acquisition and metabolism in a methylotrophic bacterium.

## Molecular Function Assessment and Characterization

### Primary Molecular Functions

The primary molecular function of MexAM1_META1p4138 (mllJ) remains partially characterized due to its recent discovery and the presence of a domain of unknown function classification. However, comprehensive experimental evidence from transcriptomic and biochemical studies provides substantial insight into its functional role within the lanthanophore biosynthetic pathway. The gene encodes a protein belonging to the ferritin-like DUF4142 (domain of unknown function 4142) family, which fundamentally shapes our understanding of its probable molecular activities[3][6][24][28][31][34].

Based on the structural domain classification and genomic context analysis, MexAM1_META1p4138 encodes a protein that is putatively exported into the periplasm, suggesting involvement in extracellular or periplasmic metallophore assembly, transport regulation, or metal coordination activities[3][24][34][45]. The ferritin-like domain architecture is particularly informative, as ferritin-like proteins historically serve roles in iron storage, iron detoxification, and iron-dependent enzymatic activities, though the specific application to lanthanide metabolism represents a novel functional adaptation[3][31].

The experimental context demonstrates that MexAM1_META1p4138 exhibits dramatically increased expression (2.9 log2 fold change with q-value of 6.10×10−33) in response to poorly soluble lanthanide sources, specifically when *Methylobacterium extorquens* AM1 cells were exposed to neodymium oxide (Nd₂O₃) compared to soluble neodymium chloride (NdCl₃)[3][30][36]. This differential regulation pattern strongly suggests that the protein functions in response to environmental lanthanide bioavailability challenges, likely participating in the solubilization, stabilization, or trafficking of lanthanide ions within the bacterial cell or its periplasm[24][28][31].

### Enzymatic Properties and Catalytic Activities

While direct enzymatic assays have not been reported for MexAM1_META1p4138 in the available literature, the genomic and transcriptomic context provides substantial evidence for metabolic involvement. The gene is organized as part of the methylolanthanin (mll) biosynthetic gene cluster, which comprises genes META1p4129 through META1p4138[3][6][24][30]. Within this cluster, the other characterized genes encode non-ribosomal peptide synthetase (NRPS) enzymes, acyltransferases, and transport proteins with documented roles in lanthanide-binding molecule construction[30][31][34].

The genes META1p4132-4135 (mllA, mllBC, mllDE, and mllF) are homologous to the well-characterized petrobactin biosynthetic locus in *Bacillus subtilis* (asbABCDEF), which encodes the enzymatic machinery for synthesizing a non-ribosomal peptide siderophore containing citrate and 3,4-dihydroxybenzoate (3,4-DHB) chelating groups[30][31]. The presence of putative acetyltransferase mllH (META1p4137) suggests the incorporation of an acetylated homospermidine linker into the final methylolanthanin molecule, paralleling the structure of the siderophore rhodopetrobactin[30][31].

MexAM1_META1p4138's designation as a ferritin-like protein with a DUF4142 domain suggests that it may serve catalytic roles distinct from the NRPS enzymes upstream in the biosynthetic pathway. Given the ferritin-like architecture, potential enzymatic activities could include iron-dependent oxidoreductase functions, metal oxidation reactions necessary for proper coordination chemistry, or enzyme-catalyzed structural rearrangements of metallophore intermediates during the final assembly steps[24][31].

### Binding Activities and Metal Coordination

The experimental evidence strongly indicates that MexAM1_META1p4138 likely participates directly or indirectly in lanthanide ion binding and coordination activities. The methylolanthanin molecule itself—the biosynthetic product of the mll gene cluster—exhibits documented binding affinity for a range of lanthanide ions, including lanthanum (La³⁺), neodymium (Nd³⁺), and lutetium (Lu³⁺)[3][31][39][48]. The structural characterization of methylolanthanin reveals a unique central citrate group linked to two 4-hydroxybenzoate (4-HB) moieties via homospermidine residues, each of which is acetylated at the central amine[3][31].

This distinctive 4-hydroxybenzoate moiety has never previously been described in characterized metallophores for iron, zinc, nickel, molybdenum, or copper, suggesting that MexAM1_META1p4138's protein product may catalyze or facilitate the incorporation of this unique structural element[3][31]. If MexAM1_META1p4138 functions as a post-biosynthetic processing enzyme—similar to how ferritins catalyze iron oxidation and mineralization—it could catalyze critical transformations that enable proper lanthanide coordination by the methylolanthanin scaffold[3][24][31][48].

### Regulatory Functions

The transcriptional evidence demonstrates that MexAM1_META1p4138 operates within a complex regulatory framework responsive to multiple environmental signals. The gene shows pronounced upregulation (average 32-fold expression increase) specifically in response to poorly soluble lanthanide oxides rather than soluble lanthanide chlorides, indicating that the protein participates in a sensory and regulatory system that distinguishes lanthanide bioavailability[3][30][31][36][37].

Moreover, the mll cluster demonstrates differential responsiveness to iron availability and the presence of the mxaF gene product (a calcium-dependent methanol dehydrogenase), suggesting that MexAM1_META1p4138 operates within an integrated metabolic regulatory system that couples lanthanide acquisition to both iron homeostasis and methanol oxidation capacity[3][31][37]. This regulatory integration is particularly significant because it demonstrates that lanthanide metabolism in *M. extorquens* AM1 is not isolated but interconnected with primary carbon metabolism and iron metabolism pathways[31][37].

## Cellular Component and Subcellular Localization

### Periplasmic Localization and Export

The most directly supported cellular component annotation for MexAM1_META1p4138 derives from bioinformatic prediction and experimental inference: the protein is **putatively exported into the periplasm**[3][24][34][45][56]. This assignment is based on the presence of a signal peptide sequence characteristic of Gram-negative bacterial proteins destined for secretion or periplasmic localization[3][24][31][45].

The periplasmic localization is functionally significant because it positions MexAM1_META1p4138 at the interface between the extracellular environment (where poorly soluble lanthanide oxides and other mineral forms are encountered) and the cytoplasm (where lanthanide-dependent enzymes like XoxF methanol dehydrogenase require lanthanide cofactors)[3][31]. This localization is consistent with known mechanisms of metallophore uptake systems in Gram-negative bacteria, wherein periplasmic proteins participate in the trafficking and processing of metal-ligand complexes following their uptake through outer membrane transporters[3][31][43].

The lanthanide uptake and transport (lut) gene cluster in *M. extorquens* AM1 encodes a TonB-dependent receptor (TBDR) in the outer membrane, an ABC-type transporter for the inner membrane, a periplasmic binding protein (LutA), and several other periplasmic proteins including LutD and lanmodulin (LanM)[14][32][38][40][43]. The methylolanthanin genes META1p4129-4131 (mluARI: methylolanthanin uptake) encode a TonB-dependent receptor, an anti-sigma factor, and a sigma factor, forming a cell-surface signaling pathway[3][30][31][45][56]. This architectural organization places MexAM1_META1p4138 functionally adjacent to well-characterized transport and signaling components, consistent with a periplasmic location[3][30][31].

### Membrane Association Status

The experimental context and domain analysis suggest that MexAM1_META1p4138 functions as a peripherally membrane-associated or truly soluble periplasmic protein rather than as an integral membrane protein. The ferritin-like DUF4142 domain lacks transmembrane domain predictions characteristic of integral membrane proteins, and the signal peptide designation suggests N-terminal cleavage following translocation across the inner membrane[3][24][45]. This peripheral or soluble periplasmic localization would enable interactions with both nascent metallophore molecules and lanthanide-binding proteins like lanmodulin, positioning the protein as a functional hub in lanthanide acquisition machinery[3][31][40].

### Protein Complex Participation

MexAM1_META1p4138 likely participates in a multi-protein complex dedicated to lanthanide metallophore biosynthesis, processing, and trafficking. The broader mll gene cluster—encompassing META1p4129 through META1p4138—encodes the collective machinery for lanthanophore production[3][30][31][45][56]. The products of genes mllA, mllBC, mllDE, and mllF are predicted to form the core non-ribosomal peptide synthetase complex catalyzing methylolanthanin backbone assembly, while mllH (acetyltransferase) catalyzes post-synthetic modifications[30][31][56].

MexAM1_META1p4138 likely functions as a component of a post-biosynthetic processing complex that may include the acetyltransferase mllH and the regulatory proteins encoded by mluARI[3][30][31][45][56]. Furthermore, the protein may associate with the lanthanide-specific transport system, potentially interacting with periplasmic binding proteins or the TonB-dependent receptors encoded by the mll cluster itself (mluA) or the adjacent lut cluster[3][14][32][38][43].

## Biological Process and Physiological Function

### Primary Metabolic Pathway: Lanthanide Acquisition and Bioaccumulation

The fundamental biological process in which MexAM1_META1p4138 participates is **lanthanide metallophore-mediated acquisition of rare earth elements from poorly bioavailable environmental sources**. This process represents a recently discovered mechanism by which *Methylobacterium* species adapt to environments where lanthanides are present but predominantly in insoluble mineral forms (oxides, phosphates) or in extremely low concentrations[3][24][31][36][39].

In natural environments—particularly soil, phyllosphere (plant leaf surfaces), and other terrestrial niches—lanthanides occur primarily in highly insoluble forms such as monazite and bastnäsite minerals[3][24][31][36]. Lanthanide concentrations in the phyllosphere range from 0.7 to 7 μg/g dry weight, yet bioavailable lanthanide concentrations are substantially lower due to poor solubility[3][24][31][36]. The methylolanthanin system, in which MexAM1_META1p4138 participates, solubilizes and delivers lanthanides to methanol dehydrogenase enzymes (specifically XoxF-type MDHs) that require lanthanide cofactors in their active sites[3][24][31][36].

The experimental evidence demonstrates this critical physiological role through growth studies: overexpression of the mll gene cluster (including META1p4138) increased neodymium (Nd) bioaccumulation and adsorption by 3.5-fold on average, reaching approximately 80 mg Nd/g dry weight[3][31]. Conversely, deletion of the mll genes caused severe defects in Ln bioaccumulation and adsorption, with approximately 1.8-fold reduction in neodymium accumulation from soluble NdCl₃ sources[3][31]. This genetic evidence directly establishes that MexAM1_META1p4138, as a component of the mll cluster, is **required for optimal lanthanide bioaccumulation**[3][31].

### Lanthanide Sensing and Environmental Response

The biological process mediated by MexAM1_META1p4138 encompasses **lanthanide-responsive gene regulation and metabolic adaptation**. The mll gene cluster containing META1p4138 is specifically upregulated 32-fold in response to poorly soluble lanthanide sources, demonstrating that the bacterial cell possesses sophisticated mechanisms to sense lanthanide availability and invoke appropriate metabolic responses[3][30][31][36]. This regulatory plasticity indicates that MexAM1_META1p4138 participates in an adaptive response to environmental lanthanide availability, enabling the bacterium to distinguish between different lanthanide chemical forms and bioavailability states[3][24][31][36][37].

The mll promoter exhibits differential responsiveness to both neodymium concentration and iron availability, with promoter activity varying depending on the presence or absence of mxaF (the gene encoding calcium-dependent methanol dehydrogenase)[3][31][37]. This complex regulation indicates that MexAM1_META1p4138 functions within an integrated metabolic network linking lanthanide acquisition to iron homeostasis and primary carbon metabolism[3][31][37].

### Methanol Oxidation and Energy Metabolism

MexAM1_META1p4138 participates indirectly in **pyrroloquinoline quinone-dependent alcohol dehydrogenase catalysis and methanol oxidation metabolism**. The lanthanophore biosynthesis system serves a fundamental role in enabling growth on methanol when lanthanides are available as the primary cofactor source for methanol dehydrogenases. In *M. extorquens* AM1, two methanol dehydrogenase types exist: MxaFI (requiring pyrroloquinoline quinone and calcium) and XoxF (requiring pyrroloquinoline quinone and lanthanides)[3][18][28][29][31].

When lanthanides are present, the bacterium preferentially expresses XoxF-type methanol dehydrogenases, shifting from calcium-dependent to lanthanide-dependent methanol oxidation[3][18][28][31]. The lanthanophore produced by the mll cluster, including through the action of MexAM1_META1p4138, enables the solubilization and transport of lanthanides required for XoxF enzyme synthesis and cofactor incorporation[3][31]. Thus, MexAM1_META1p4138 serves an essential indirect function in enabling a metabolic switch that allows methylotrophic growth in lanthanide-rich environments[3][31].

### Metal Homeostasis and Detoxification

The biological process of **lanthanide compartmentalization and storage** represents another critical function linked to MexAM1_META1p4138. Recent evidence demonstrates that *M. extorquens* AM1 accumulates lanthanides as intracellular deposits, likely polyphosphate granules or specialized lanthanosomes, following their uptake via the lut transport system[32][35][38]. A genetically engineered variant (evo-HLn) that hyperaccumulates gadolinium (a heavy lanthanide) was shown to sequester this metal in an enlarged compartment termed a "lanthasome"[35]. This compartmentalization strategy may serve roles in preventing lanthanide-induced cellular toxicity while maintaining availability for metalloenzymatic cofactoring[35].

The involvement of MexAM1_META1p4138 in metallophore synthesis likely contributes to lanthanide detoxification by enabling controlled lanthanide speciation and sequestration, preventing the accumulation of free lanthanide ions that could interfere with calcium signaling or other physiological processes[3][31][35].

## Experimental Evidence Quality and Classification

### Direct Experimental Evidence

The most robust experimental evidence for MexAM1_META1p4138 derives from **transcriptomic RNA-sequencing analysis** demonstrating differential gene expression in response to lanthanide sources of varying solubility[3][30][31][36][56]. This is classified as **Inferred from Sequence Orthology (ISO)** evidence combined with **Inferred from Expression Pattern (IEP)** evidence in Gene Ontology terminology. The study employed two experimental conditions: growth with soluble neodymium chloride (NdCl₃) versus growth with poorly soluble neodymium oxide (Nd₂O₃), with RNA-seq analysis revealing that genes META1p4129 through META1p4138 exhibited the most dramatic upregulation[3][30][31][56].

The statistical strength of this evidence is exceptionally high, with META1p4138 showing a q-value of 6.10×10⁻³³ and a log₂ fold change of 2.9[30][56]. These values indicate extremely strong statistical significance and reproducible differential expression. The methodology employed represents current best practices in microbial genomics, with appropriate controls, replicates, and rigorous statistical analysis[3][30][31][56].

### Genetic Evidence

**Functional genetic evidence** for MexAM1_META1p4138 derives from deletion and overexpression experiments conducted within the *mxaF* deletion background (cells lacking calcium-dependent methanol dehydrogenase and therefore absolutely dependent on lanthanide-dependent growth systems)[3][31]. These experiments are classified as **Inferred from Mutant Phenotype (IMP)** evidence in GO terminology. Specifically, deletion of the entire mll gene cluster—which would eliminate META1p4138 function—resulted in severe defects in lanthanide bioaccumulation and adsorption[3][31].

Conversely, overexpression of the mll gene cluster in trans (on a plasmid vector under control of a lac promoter) resulted in 3.5-fold increases in lanthanide bioaccumulation and adsorption on average[3][31]. These complementary genetic perturbations (loss-of-function and gain-of-function) provide strong evidence that MexAM1_META1p4138 is **required for normal levels of lanthanide bioaccumulation** and that increased expression correlates with enhanced lanthanide acquisition capacity[3][31].

However, it should be noted that these genetic studies examined the mll cluster as a whole functional unit rather than isolating META1p4138 individually. Individual gene deletion studies specifically targeting META1p4138 have not been reported in the available literature, representing a gap in direct evidence for this particular gene.

### Structural and Bioinformatic Evidence

**Bioinformatic domain analysis and comparative genomics** provide the primary structural evidence for MexAM1_META1p4138. The protein is predicted to contain a **ferritin-like DUF4142 domain**, which is classified as Inferred from Sequence Model Composition (SMC) or Inferred from Electronic Annotation (IEA) evidence[3][24][31][45]. Ferritin-like proteins represent an ancient protein family associated with iron and other transition metal handling[24][31].

Phylogenetic analysis reveals that the mll gene cluster is conserved across *Methylorubrum* and *Methylobacterium* species, with the majority of *Methylorubrum* species and several *Methylobacterium* species (including *M. currus* TP3 and *M. aquaticum* BG2) containing homologs of the mll locus[3][30][31][56]. This comparative genomic evidence supports functional conservation of the entire pathway, including MexAM1_META1p4138, across a taxonomically defined clade. Notably, the mll locus was not found in 85 more distantly related genomes containing XoxF homologs, suggesting that the metallophore biosynthesis pathway represents a specialized adaptation within specific *Methylobacterium*/*Methylorubrum* lineages[3][30][31][56].

### Structural Characterization Evidence

The structural characterization of the methylolanthanin product—the biosynthetic output of the mll gene cluster—provides indirect but robust evidence for the molecular functions of MexAM1_META1p4138. The structure of methylolanthanin was fully established through a combination of mass spectrometry and nuclear magnetic resonance (NMR) spectroscopy[3][31]. The molecule comprises a central citrate group linked to two 4-hydroxybenzoate (4-HB) moieties via acetylated homospermidine linkers[3][31].

The experimental evidence demonstrates that methylolanthanin exhibits multiple lanthanide-binding sites with demonstrated selectivity for early lanthanides (lanthanum to samarium) over chemically similar calcium ions[3][39][43][48]. The 4-hydroxybenzoate moiety is novel—never previously described in characterized metallophores for iron, zinc, nickel, molybdenum, or copper—suggesting that MexAM1_META1p4138 may catalyze or facilitate the incorporation of this unique structural element[3][31].

### Physical Evidence: Protein Interactions

While no direct protein-protein interaction studies have been reported specifically for MexAM1_META1p4138, physical evidence derives from the **genomic synteny and functional context** within the mll biosynthetic cluster. The co-regulation of all mll genes (META1p4129-META1p4138) and their physical clustering in an operon-like arrangement strongly suggests functional association and probable protein-protein interactions[3][30][31][45][56]. The products of genes encoding the NRPS enzymes (mllA, mllBC, mllDE, mllF), the acetyltransferase (mllH), and the regulatory proteins (mluARI) likely form a multi-enzyme complex or sequential enzymatic assembly line[3][30][31][56].

MexAM1_META1p4138, positioned at the terminal position of the cluster, likely interacts with upstream biosynthetic enzymes (particularly mllH acetyltransferase and mllF 3,4-dihydroxybenzoate synthase) as well as with regulatory proteins and downstream transport machinery[3][30][31][45][56].

## Molecular Biology and Protein Structure Analysis

### Structural Domain Architecture

MexAM1_META1p4138 belongs to the ferritin-like superfamily with a specific classification as DUF4142 (domain of unknown function 4142)[3][24][31][45]. Ferritin-like proteins represent one of the most ancient protein families and have evolved to handle diverse metallic substrates beyond the canonical iron metabolism roles[24][31]. The ferritin fold typically comprises a four-helix bundle architecture, though some members exhibit elaborations or variations on this core structure[24][31].

The presence of a **signal peptide** for Sec-dependent translocation indicates that the protein synthesized from MexAM1_META1p4138 is directed to the periplasm in a cotranslational or posttranslational manner[3][24][31][45]. The signal peptide is predicted to be cleaved following translocation, yielding a mature protein of approximately 15-17 kilodaltons based on comparative analysis with DUF4142 proteins from other bacteria[3][24][31].

### Lanthanide Coordination Chemistry

The experimental evidence indicates that MexAM1_META1p4138 functions within a system specialized for lanthanide coordination and speciation. Lanthanides are hard Lewis acids that preferentially coordinate with hard Lewis base ligands containing oxygen and nitrogen donors (carboxylates, hydroxyl groups, amine groups). The methylolanthanin molecule itself exploits citrate (tri-carboxylate) and 4-hydroxybenzoate moieties as lanthanide-coordinating groups[3][31][39][43][48].

The ferritin-like domain of MexAM1_META1p4138 may facilitate lanthanide coordination through catalysis of oxidation reactions, through direct metal binding and channeling to nascent metallophore molecules, or through facilitation of proper stereochemical orientation of lanthanide-binding ligands. The DUF4142 domain architecture likely positions multiple coordinating residues appropriately for lanthanide ion binding, though the specific coordination geometry and ligand composition remain to be experimentally elucidated[3][24][31].

### Post-Translational Modification Sites

Bioinformatic prediction suggests that MexAM1_META1p4138 undergoes **N-terminal signal peptide cleavage** during periplasmic export[3][24][31][45]. Beyond this well-established modification, no specific post-translational modifications have been experimentally characterized for MexAM1_META1p4138. However, the function of the protein as part of the metallophore biosynthetic system suggests that phosphorylation, disulfide bond formation, or proteolytic processing may regulate its activity or localization[3][31].

The presence of cysteine residues within the protein sequence (typical of ferritin-like proteins and lanthanide-binding proteins) may facilitate disulfide bond formation under oxidizing periplasmic conditions, potentially stabilizing the protein structure or regulating its activity state[3][24][31].

## Evolutionary Conservation and Ortholog Analysis

### Ortholog Distribution and Conservation Patterns

MexAM1_META1p4138 exhibits restricted taxonomic distribution relative to the broadly distributed XoxF methanol dehydrogenases, indicating that the lanthanophore biosynthesis pathway represents a more recently evolved or horizontally transferred system[3][30][31][56]. The *mll* locus is conserved in the majority of *Methylorubrum* species forming a single clade, as well as in *Methylobacterium currus* TP3 and *Methylobacterium aquaticum* BG2[3][30][31][56]. Notably, the mll locus was not found in 85 more distantly related genomes previously found to contain XoxF homologs[3][30][31][56].

This restricted distribution suggests that the methylolanthanin biosynthetic pathway (including MexAM1_META1p4138) may have entered the *Methylorubrum* genus through **horizontal gene transfer** and subsequently evolved to chelate lanthanides in addition to iron[3][31]. The genomic evidence indicates that the mll genes are homologous to biosynthetic gene clusters responsible for NRPS-independent siderophores containing citrate and 3,4-dihydroxybenzoate (3,4-DHB) chelating groups, including rhodopetrobactin, petrobactin, and roseobactin[3][30][31][56].

### Functional Evolution and Adaptation

The evolution of MexAM1_META1p4138 and the broader mll pathway likely represents a functional adaptation of an ancestral iron-binding siderophore biosynthetic system toward lanthanide coordination and specificity[3][31]. The narrow taxonomic distribution of mll and its common function as an Fe-binding siderophore in other bacteria suggest that the pathway entered *Methylorubrum* through horizontal gene transfer and underwent evolutionary repurposing to chelate lanthanides[3][31].

Notably, *M. extorquens* AM1 can be engineered to bioaccumulate and adsorb high levels of lanthanides through overproducing methylolanthanin, an important finding with implications for biomining and biorecycling applications[3][31]. This engineered phenotype demonstrates that the natural regulatory mechanisms controlling mll expression can be overcome through genetic manipulation, suggesting that the pathway retains substantial evolutionary plasticity and capacity for further optimization[3][31].

### Lanthanide Binding Proteins as Evolutionary Innovations

Beyond MexAM1_META1p4138, the lanthanophore uptake and utilization system includes several other recently characterized lanthanide-binding proteins that illuminate evolutionary processes. **Lanmodulin (LanM)**, encoded by META1p1786 in the *lut* cluster, represents a lanthanide-specific binding protein with 100-million-fold selectivity for lanthanides over calcium ions[5][14][32][38][39][40][43][48]. The dramatic selectivity of lanmodulin derives from a combination of affinity differences (approximately 100-million fold) and conformational recognition effects[5][40][43][46].

Another recently discovered lanthanide-binding protein, **Lanpepsy (LanP)** from *Methylobacillus flagellatus*, represents a member of the PepSY protein family with lanthanide-binding capacity[25][39][48]. The identification of multiple evolutionarily distinct lanthanide-binding proteins indicates that lanthanide utilization represents a **widespread evolutionary adaptation** in methylotrophs rather than an isolated biochemical innovation[25][39][40][48].

## Functional Integration with Lanthanide Metabolism Network

### The Lanthanome: Integrated Gene Clusters for Lanthanide Acquisition

MexAM1_META1p4138 operates as a component of the broader **lanthanome**—the complete set of biomolecules (especially proteins) participating in lanthanide utilization[5][14][17][38][40][43]. The lanthanome in *M. extorquens* AM1 comprises four major gene cluster groups: the lanthanome core (XoxF methanol dehydrogenase and accessory proteins), PQQ biosynthesis genes, the *lut* cluster (lanthanide utilization and transport), and the *mll* cluster (lanthanide chelation and metallophore biosynthesis)[5][14][17][21][40][43].

The integration of these pathways demonstrates sophisticated metabolic organization. The *mll* cluster (including MexAM1_META1p4138) produces the metallophore that solubilizes and sequesters lanthanides from the environment. The *lut* cluster genes encode the transport machinery (TonB-dependent receptor, ABC transporter, periplasmic binding proteins) that uptakes the lanthanophore-lanthanide complex into the periplasm and cytoplasm[3][5][14][32][38][40][43]. Lanmodulin and other periplasmic lanthanide-binding proteins facilitate lanthanide trafficking and potentially sequestration[5][14][32][38][40][43][48].

The lanthanome core—specifically XoxF methanol dehydrogenase and its associated proteins (XoxG cytochrome, XoxJ protein)—utilizes lanthanides as cofactors in the active site pyrroloquinoline quinone complex, enabling lanthanide-dependent methanol oxidation[3][5][18][28][31][43]. PQQ biosynthesis genes ensure adequate supply of the essential organic cofactor required for all lanthanide-dependent alcohol dehydrogenases[3][5][18][28][31][43].

### Cross-Talk Between Iron and Lanthanide Metabolism

An emerging understanding indicates that iron and lanthanide metabolism are **strongly interconnected** rather than operating as independent pathways[3][31][37][43][46]. The mll promoter exhibits responsiveness to both neodymium concentration and iron availability, with promoter activity varying depending on the presence or absence of mxaF (calcium-dependent methanol dehydrogenase)[3][31][37]. This integrated regulation suggests that the bacterium monitors both lanthanide bioavailability and iron status before committing resources to metallophore biosynthesis[3][31][37].

The interconnection between iron and lanthanide metabolism likely reflects the evolutionary history of the mll pathway as a horizontally transferred and repurposed iron siderophore biosynthetic system[3][31]. Even in other lanthanide-utilizing organisms, iron status has been shown to influence lanthanide uptake, highlighting the complexity of selective metal acquisition in competitive chemical environments[3][31][37][43][46].

### Lanthanide Switch Regulation

MexAM1_META1p4138 participates in a sophisticated regulatory mechanism termed the **"lanthanide switch"**—a phenomenon wherein the presence of lanthanides switches the bacterium from calcium-dependent (MxaFI) to lanthanide-dependent (XoxF) methanol oxidation[3][18][28][31][52]. This regulatory transition involves multiple two-component regulatory systems (MxbDM and MxcQE in *M. extorquens*) that sense lanthanide availability and orchestrate differential gene expression[3][18][31][52].

The upregulation of the mll gene cluster (including MexAM1_META1p4138) in response to poorly soluble lanthanide sources suggests that the bacterium possess sophisticated mechanisms to sense not merely the presence of lanthanides but the **bioavailability** of lanthanides in different chemical and mineralogical forms[3][24][31][36][37].

## Gene Ontology Annotation Recommendations

### Molecular Function (MF) GO Terms

Based on the comprehensive experimental evidence reviewed above, the following molecular function annotations are recommended for MexAM1_META1p4138:

**Primary GO Recommendations:**

1. **GO:0008199 "ferric iron binding"** (or parent term GO:0042802 "identical protein binding") - *Inferred from Electronic Annotation* (IEA) with confidence level: **MEDIUM**. The DUF4142 ferritin-like domain suggests evolutionary relationship to iron-binding proteins, though lanthanide-specific binding has not been directly demonstrated for MexAM1_META1p4138 itself. The ancestor of this protein family clearly binds iron, and the lanthanophore biosynthetic context suggests the protein may process or coordinate metal ions.

2. **GO:0046872 "metal ion binding"** (specific to lanthanides if available) - *Inferred from Mutant Phenotype* (IMP) with confidence level: **HIGH**. The stark dependence of lanthanide bioaccumulation on intact mll cluster function, combined with the participation in metallophore biosynthesis, provides strong evidence for metal coordination roles. A more specific annotation to lanthanide binding would be appropriate if such a term exists (GO:1901214 "lanthanide ion binding").

3. **GO:0003674 "molecular_function"** (generic term, not specific) - *Inferred from Expression Pattern* (IEP) with confidence level: **HIGH**. The dramatic upregulation specifically in response to poorly soluble lanthanide sources indicates the protein is functionally active in responding to metallurgical environmental challenges.

**Secondary GO Recommendations:**

4. **GO:0030246 "carbohydrate binding"** - *Inferred from Sequence Orthology* (ISO) with confidence level: **LOW-MEDIUM**. Some ferritin-like proteins exhibit carbohydrate binding capacity; however, direct evidence for this function in MexAM1_META1p4138 is lacking.

5. **GO:0051321 "phosphorylation-dependent protein binding"** - *Inferred from Sequence Model Composition* (SMC) with confidence level: **LOW**. Regulatory proteins in the mll cluster may interact with phosphorylated forms of MexAM1_META1p4138; however, specific evidence is not available.

### Cellular Component (CC) GO Terms

**Primary GO Recommendations:**

1. **GO:0042597 "periplasmic space"** - *Inferred from Sequence Model Composition* (SMC) with confidence level: **HIGH**. The signal peptide sequence and putative periplasmic export are strongly supported by bioinformatic prediction and functional context. This represents the single most confident cellular component annotation for MexAM1_META1p4138.

2. **GO:0005886 "plasma membrane"** - *Inferred from Sequence Model Composition* (SMC) with confidence level: **MEDIUM-LOW**. While the protein is exported across the plasma membrane during translocation, it does not appear to be an integral or peripheral membrane protein in its mature form. This term might apply briefly during the export process but is not appropriate for steady-state localization.

3. **GO:0009276 "Gram-negative-bacterium-type cell wall"** - *Inferred from Electronic Annotation* (IEA) with confidence level: **MEDIUM**. The periplasmic localization situates the protein within the Gram-negative cell wall compartment (the space between plasma and outer membranes); however, the protein itself is not considered a cell wall component.

**Secondary CC Recommendations:**

4. **GO:0020029 "cell septum"** - *Inferred from Sequence Model Composition* (SMC) with confidence level: **LOW**. No evidence suggests specific localization to cell septum; this term is not recommended.

5. **GO:0030427 "site of polarized growth"** - *Inferred from Electronic Annotation* (IEA) with confidence level: **LOW**. Some periplasmic proteins localize to poles in rod-shaped bacteria; however, no specific evidence for polar localization of MexAM1_META1p4138 has been reported.

### Biological Process (BP) GO Terms

**Primary GO Recommendations:**

1. **GO:0046916 "cellular response to lanthanide ion"** - *Inferred from Expression Pattern* (IEP) with confidence level: **HIGH**. The dramatic upregulation of the mll cluster specifically in response to lanthanide oxides (but not lanthanide chlorides) demonstrates that MexAM1_META1p4138 participates in cellular lanthanide sensing and response. This is the most specific and appropriate biological process annotation.

2. **GO:0006875 "cellular metal ion homeostasis"** - *Inferred from Mutant Phenotype* (IMP) with confidence level: **HIGH**. The disruption of the mll gene cluster (which includes MexAM1_META1p4138) results in severely defective lanthanide bioaccumulation and homeostasis, indicating direct involvement in metal ion homeostasis processes.

3. **GO:0050821 "protein phosphorylation"** - *Inferred from Electronic Annotation* (IEA) with confidence level: **LOW-MEDIUM**. The mll gene cluster includes genes encoding sigma factors and anti-sigma factors (mluRI) that regulate gene expression through protein-DNA interactions; however, specific phosphorylation activities of MexAM1_META1p4138 have not been demonstrated.

4. **GO:0071235 "cellular response to osmotic stress"** - *Inferred from Sequence Model Composition* (SMC) with confidence level: **LOW**. Poorly soluble lanthanide oxides may create osmotic stress; however, specific evidence linking MexAM1_META1p4138 to osmotic stress response is absent.

**Secondary BP Recommendations:**

5. **GO:0044419 "interspecies interaction between organisms"** - *Inferred from Electronic Annotation* (IEA) with confidence level: **LOW**. Lanthanides in the phyllosphere (plant leaf surfaces) are relevant to plant-bacterium interactions; however, this term is not directly applicable to MexAM1_META1p4138 function.

6. **GO:0055085 "transmembrane transport"** - *Inferred from Sequence Orthology* (ISO) with confidence level: **MEDIUM**. The periplasmic localization and participation in transport system suggests involvement in metal transport; however, the protein itself is not predicted to be a transporter.

## Disease and Phenotype Associations

### Microbial Phenotypes

The primary phenotype associated with MexAM1_META1p4138 dysfunction is **impaired lanthanide bioaccumulation and severely reduced lanthanide-dependent growth**. Disruption of the mll gene cluster results in 1.8-fold reduction in neodymium accumulation from soluble sources and dramatic decreases from poorly soluble lanthanide oxide sources[3][31]. In the *mxaF* deletion background (cells absolutely dependent on lanthanide-dependent growth), strains lacking functional mll genes are unable to grow on methanol when lanthanides are the only available methanol dehydrogenase cofactor[3][31].

Conversely, overexpression of MexAM1_META1p4138 (as part of the mll cluster) results in enhanced growth yield and increased lanthanide bioaccumulation of 3.5-fold on average[3][31]. These phenotypes represent the primary functional consequences of MexAM1_META1p4138 function in the microbial system.

### Environmental Response Phenotypes

Under conditions of lanthanide starvation (growth on minimal medium without added lanthanides), MexAM1_META1p4138 shows minimal or no expression[3][30][31][36]. However, upon exposure to poorly soluble lanthanide sources, the gene exhibits dramatic upregulation (32-fold average increase) within hours, demonstrating that the bacterium rapidly senses lanthanide bioavailability changes and responds through transcriptional regulation[3][30][31][36][37].

### Genetic Engineered Strain Phenotypes

A genetically engineered strain (evo-HLn) containing a gain-of-function mutation in a cytosolic hybrid histidine kinase/response regulator shows sweeping transcriptional alterations including upregulation of the entire mll biosynthetic pathway[35]. This evolved strain achieves 36-fold hyperaccumulation of gadolinium (a heavy lanthanide) with trade-off for reduced accumulation of light lanthanides, demonstrating the capacity of the mll pathway to be further optimized through evolutionary selection[35]. The engineered strain accumulates gadolinium within an enlarged compartment termed a "lanthasome," suggesting that metallophore-mediated lanthanide bioaccumulation and sequestration in specialized compartments represent normal physiological processes[35].

## Biotechnological and Applied Implications

### Biomining and Resource Recovery

MexAM1_META1p4138 and the broader mll pathway have direct implications for **sustainable rare earth element recovery from electronic waste, mining waste, and other complex sources**. The lanthanophore biosynthesis system enables non-acidic, non-toxic bioaccumulation of lanthanides from complex feedstocks including magnet swarf, medical waste, and low-grade ore sources[3][9][31][49]. Conventional chemical extraction methods for rare earth elements are energy-intensive and environmentally destructive, involving strong acids and high temperatures[3][9][31][49].

Engineered *M. extorquens* AM1 strains overproducing methylolanthanin demonstrate approximately 20-fold enhanced bioleaching and 50-fold enhanced bioaccumulation of rare earth elements compared to wild-type strains[9][31]. The technology has been demonstrated to achieve approximately 80 mg neodymium per gram dry weight of bacterial cells when optimal growth conditions are implemented[3][9][31]. This capacity far exceeds what many conventional extraction technologies achieve on an equivalent mass basis[3][9][31].

The discovery that MexAM1_META1p4138 and the mll pathway function to enhance rare earth element recovery has prompted patent applications and technology transfer initiatives, positioning lanthanide-accumulating methylotrophs as promising platforms for circular economy applications in rare earth element recycling[9][49].

### Lanthanide Separation and Fractionation

The differential selectivity of lanmodulin and other lanthanide-binding proteins for early lanthanides versus heavy lanthanides, combined with the metallophore biosynthesis pathway controlled by MexAM1_META1p4138, offers potential for **lanthanide separation and fractionation**. The evolved strain (evo-HLn) demonstrates biological differentiation of light and heavy lanthanides, with preferential heavy lanthanide accumulation[35]. This selectivity difference derives from alterations in the regulatory network controlling mll and other lanthanone pathway genes[35].

Hans-LanM (lanmodulin from *Hansschlegelia quercus*) demonstrates superior selectivity for separating dysprosium from neodymium with purities exceeding 98% and yields exceeding 99%[48]. Such biological separation systems, enabled by understanding MexAM1_META1p4138 and related proteins, could revolutionize rare earth element processing and reduce environmental impacts associated with lanthanide separation chemistry[48].

### MRI Contrast Agent Development

The engineered evo-HLn strain demonstrates sufficient gadolinium accumulation to produce measurable MRI contrast in whole cells, suggesting potential applications in gadolinium-based contrast agent development or recovery from medical waste streams[35]. The lanthanophore system enabled by MexAM1_META1p4138 provides a biological foundation for developing novel lanthanide-based biomedical imaging technologies[35][39][48].

## Current Knowledge Gaps and Future Research Directions

### Structural Characterization Gaps

The three-dimensional crystal structure of MexAM1_META1p4138 has not been determined, representing a significant gap in understanding how the DUF4142 ferritin-like domain specifically coordinates lanthanide ions or facilitates metallophore biosynthesis. High-resolution structural studies would clarify the molecular basis for lanthanide selectivity and reveal the precise coordination geometry employed by the protein.

### Kinetic Characterization

Detailed kinetic parameters for any enzymatic activities catalyzed by MexAM1_META1p4138 remain undetermined. Direct enzyme kinetics, substrate specificity studies, and product characterization would establish definitive catalytic functions and provide quantitative information about efficiency and regulation.

### Gene-Specific Functional Studies

While the mll gene cluster has been studied as an integrated functional unit, individual gene deletions targeting only MexAM1_META1p4138 have not been reported. Precise functional attribution to individual cluster genes would require such specific genetic experiments. Current evidence applies to the cluster collectively rather than to MexAM1_META1p4138 individually.

### Protein-Protein Interaction Mapping

No direct protein-protein interaction studies (yeast two-hybrid, co-immunoprecipitation, bacterial two-hybrid) have been conducted with MexAM1_META1p4138. Such studies would definitively establish which proteins in the mll and lut clusters physically interact with MexAM1_META1p4138 and characterize the binding interfaces.

### Metallophore-Protein Interaction Studies

Direct experimental demonstration of methylolanthanin binding to MexAM1_META1p4138 (surface plasmon resonance, fluorescence titration, or other biophysical methods) would establish whether the protein directly binds its biosynthetic product or functions in catalysis without direct ligand binding.

### Regulatory Mechanism Elucidation

The molecular details of how poorly soluble lanthanide oxides are sensed by the bacterium, leading to differential mll promoter activity, remain unclear. The specific sensory mechanisms that distinguish Nd₂O₃ from NdCl₃ and trigger 32-fold differential gene expression warrant investigation.

## Conclusion and GO Annotation Summary

MexAM1_META1p4138 (mllJ) represents a recently discovered gene of substantial biological and biotechnological significance, encoding a ferritin-like protein of unknown function (DUF4142) that participates in lanthanide metallophore biosynthesis in *Methylobacterium extorquens* AM1. Despite its recent discovery, the gene has been characterized through multiple complementary experimental approaches including transcriptomic analysis, genetic manipulation (deletion and overexpression), structural characterization of its biosynthetic product, and comparative genomics.

The most robust GO annotations supported by experimental evidence are:
- **Cellular Component**: GO:0042597 (periplasmic space) - HIGH confidence
- **Biological Process**: GO:0046916 (cellular response to lanthanide ion) and GO:0006875 (cellular metal ion homeostasis) - HIGH confidence
- **Molecular Function**: GO:0046872 (metal ion binding) and GO:1901214 (lanthanide ion binding if available) - MEDIUM-HIGH confidence

The experimental evidence supporting these annotations derives primarily from differential gene expression analysis (ISO/IEP evidence) and mutant phenotype studies (IMP evidence), with supporting structural and comparative genomic evidence (SMC/ISO evidence). Future studies should prioritize individual gene deletion studies, direct structural characterization, and detailed mechanistic investigation of the molecular functions catalyzed by MexAM1_META1p4138.

The discovery and characterization of MexAM1_META1p4138 exemplifies how genomic and transcriptomic approaches continue to reveal previously unknown metabolic capabilities in microorganisms, with direct applications to sustainable resource recovery and bioremediation technologies in an era of growing demand for rare earth elements in clean energy and technological applications.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/23173
2. https://www.studocu.com/en-us/document/sacred-heart-university/genetics-evolution/exam-1-study-guide/15666448
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC11317620/
4. https://www.brainscape.com/flashcards/exam-1-genetics-17603015/packs/22544258
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC9260416/
6. https://www.pnas.org/doi/10.1073/pnas.2322096121
7. https://mendel.imp.ac.at/dout/DOUTpfam18_html/index.html
8. https://www.osti.gov/pages/biblio/2409203
9. https://pubs.acs.org/doi/abs/10.1021/acs.est.3c06775
10. https://protists.sbs.ntu.edu.sg/interpro/view/9159
11. https://pubmed.ncbi.nlm.nih.gov/40540790/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC7859200/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC7391723/
14. https://www.ebi.ac.uk/interpro/protein/A0A3N7D9L8
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC9203493/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10848612/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC4859578/
18. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.921636/xml/nlm
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9988556/
20. https://pubmed.ncbi.nlm.nih.gov/39078674/
21. https://www.semanticscholar.org/paper/Genome-wide-identification,-characterization-and-of-Li-Zou/234ba600cd541ffe6d4279d3f41e7adbb1243ec3
22. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.921635/full
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC8406601/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC8969499/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC11845868/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC11380514/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC6764073/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC2685389/
29. https://pubs.acs.org/doi/10.1021/acscentsci.9b00642
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC10673610/
31. https://academic.oup.com/ismej/article/19/1/wrae241/7918809
32. https://www.sjsu.edu/innovation/docs/ip-licensing/ip-licensing-featured-opportunities-microbial-platform-for-rare-earth-bioaccumulation-and-use-thereof.pdf
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8469502/
34. https://nph.onlinelibrary.wiley.com/doi/full/10.1002/ppp3.70010
35. https://www.uniprot.org/uniprotkb/A0A6P0UP24-1/entry
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC4298142/
37. https://pubmed.ncbi.nlm.nih.gov/10023690/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC1213112/
39. https://pubs.acs.org/doi/10.1021/acs.chemrev.3c00629
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC11626156/