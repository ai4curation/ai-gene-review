# Chapter 19: Complementary Sources of Protein Functional Information: The Far Side of GO - Summary

**Author:** Nicholas Furnham

## Summary

This chapter explores the complementary functional annotation resources that extend beyond the Gene Ontology (GO), providing enhanced functional descriptions through specialized databases focused on enzymes, protein domains, pathways, and protein interactions. The author demonstrates how these resources can be integrated with GO to provide more comprehensive and detailed functional characterization of proteins, highlighting both the strengths and limitations of different annotation approaches.

### The Need for Complementary Resources

**GO Limitations:**
While GO provides accessible controlled vocabulary for protein function description, it has inherent limitations that other resources can address:
- **Enzyme specificity**: GO cannot capture detailed reaction chemistry and substrate specificity
- **Domain granularity**: GO typically annotates whole proteins rather than specific functional domains
- **Pathway dynamics**: GO lacks explicit representation of pathway dependencies and directional information
- **Interaction networks**: GO doesn't capture protein-protein interaction topology

**Integration Benefits:**
- **Enhanced descriptions**: Mapping between resources provides relationships not readily captured in GO alone
- **Automatic updates**: GO consortium provides regularly updated mappings to complementary resources
- **Comprehensive coverage**: Combined resources offer broader functional annotation landscape

### Enzyme Classification and Function

**Enzyme Commission (E.C.) System:**
- **Historical development**: Created in 1956 to address confused enzyme naming conventions
- **Hierarchical structure**: Four-level classification system
  - **Level 1**: Six broad enzyme classes (Oxidoreductases, Transferases, Hydrolases, Lyases, Isomerases, Ligases)
  - **Level 2-3**: Sub-class and sub-subclass describing reactive species and bond types
  - **Level 4**: Serial number for specific reactions within sub-subclass
- **Current scale**: 6,510 approved E.C. numbers, 5,560 in active use
- **GO mapping**: Only 3,924 (70%) of active E.C. numbers have equivalent GO terms

**E.C. System Complexities:**
- **Mass-balanced reactions**: Described as balanced as possible but not necessarily charge-balanced
- **Multiple reactions per E.C.**: One E.C. number may have multiple associated reactions
- **General vs. specific reactions**: Broad specificity represented as generic reactions with specific alternatives
- **Pseudo E.C. terms**: UniProt-created terms (identifiable by 'n' in fourth level, e.g., 1.1.1.n5)

**Specialized Enzyme Resources:**
- **KEGG**: Curated database of genes, enzyme reactions, metabolites, and metabolic pathways
- **BRENDA**: Comprehensive enzyme function database with GO term integration
- **CSA (Catalytic Site Atlas)**: Catalytic residues and their functions in enzyme reactions
- **MACiE**: Enzyme mechanism steps, bond formation/breaking order, cofactor roles
- **EMO (Enzyme Mechanism Ontology)**: Bridge between chemical and biological descriptors

### Functional Similarity Measurement Challenges

**GO vs. E.C. Similarity Measures:**
- **GO approaches**: Semantic similarity based on ontological graph (information content, Lin score, Wang score)
- **E.C. limitations**: Cannot be used for automated quantitative comparisons between annotations
- **EC-Blast solution**: Atom-atom mapping approach for reaction comparison
  - **Fingerprint generation**: Describes reactions through bond changes and reaction centers
  - **Quantitative comparison**: Enables similarity scoring based on chemical transformation details

**Divergent Results Example:**
- **E.C. 2.1.2.9 vs. E.C. 2.1.2.11**:
  - EC-Blast similarity: 0.22 (low due to different bond cleavage patterns)
  - GO semantic similarity: 0.73 (high due to similar ontological classification)
- **Chemical specificity**: EC-Blast captures differences in bonds cleaved, stereochemistry, and bond order rearrangements

### Domain-Centric Functional Annotation

**Granularity Challenge:**
- **Whole protein vs. domain annotation**: Most genomic annotations assigned to complete gene products
- **Functional unit identification**: Many functions attributable to specific protein domains
- **Multi-domain complexity**: Functions often result from domain combinations rather than individual domains

**Domain Classification Resources:**

**1. Pfam (Sequence-Based):**
- **Goal**: Representative collection of functionally annotated protein families
- **Community curation**: Recent releases use Wikipedia for functional annotations
- **GO mapping**: InterPro provides mapping between Pfam annotations and GO terms

**2. CATH (Structure-Based):**
- **Domain definition**: Uses protein structures for domain classification
- **FunFams**: Functionally coherent clusters within superfamily divisions
- **GO integration**: Uses GO terms associated with sequences to define functional clusters
- **Limitation**: Annotations assigned to whole sequences, not specific domains

**3. SUPERFAMILY (SCOP-Based):**
- **Domain-centric approach**: Statistical inference of domain-specific functional annotations
- **Assumption**: GO terms annotated to proteins sharing domains confer functional indicators
- **SDFO**: Structural Domain Functional Ontology with reduced GO version
- **Phenotype integration**: Incorporates mammalian phenotype ontology (MPO) and Human Phenotype Ontology (HPO)

**4. SFLD (Structure-Function Linkage Database):**
- **Critical domains**: Identifies domains essential for function (often defining superfamilies)
- **Direct linkage**: Links functional annotations directly to domains or domain combinations

### Pathway and Interaction Context

**GO Pathway Limitations:**
- **Individual components**: Molecular function GO terms describe pathway components
- **Process description**: Biological process terms capture overall pathway descriptions
- **Missing dynamics**: GO lacks representation of pathway dependencies and directional information
- **Limited context**: Cannot represent signal transduction or metabolic pathway topology

**Specialized Pathway Resources:**
- **KEGG**: Comprehensive pathway diagrams and metabolic maps
- **BioCarta**: Curated pathway descriptions
- **MetaCyc**: Enzyme and pathway database
- **Pathway Interaction Database**: Curated interaction descriptions
- **Reactome**: Detailed pathway topology and interactions
- **IntAct**: Molecular interaction database with high-confidence subset exported to GO

**Integration Applications:**
- **Proteomics data analysis**: Combined GO enrichment and pathway resource linking
- **Dynamic network construction**: Gene list-based functional network organization
- **Interaction prediction**: Semantic similarity and machine learning for protein-protein interaction prediction

### Multi-Domain Architecture Complexity

**Biological Complexity:**
- **Domain combinations**: Increasing complexity of multi-domain protein architectures
- **Function distribution**: Functions assigned to complete gene products and individual domains
- **Architecture diversity**: Single domains combined in diverse multi-domain arrangements

**Visualization and Analysis:**
- **Force-directed graphs**: Network representation of multi-domain architectures
- **Functional unit identification**: Distinguishing single-domain from multi-domain functions
- **Interactive exploration**: Tools for investigating domain architecture relationships

## Relevance to AI Gene Review Project

This chapter provides **essential perspective** on the limitations of GO-only annotation and the importance of integrating multiple functional annotation sources for comprehensive gene function assessment, directly supporting our over-annotation detection and curation efforts:

### 1. **Multi-Resource Validation Framework**
The chapter's integration approach directly supports comprehensive annotation assessment:
- **Cross-resource consistency**: Comparing GO annotations with E.C., KEGG, and domain classifications helps identify over-annotations that lack support across multiple resources
- **Complementary evidence**: Annotations supported by multiple independent resources (GO + E.C. + domain analysis) provide stronger evidence than GO alone
- **Resource-specific strengths**: Understanding each resource's focus enables targeted validation (e.g., E.C. for enzyme specificity, domain databases for structural function)

### 2. **Enzyme Function Over-Annotation Detection**
The chapter's detailed treatment of enzyme classification provides specific tools for enzyme annotation curation:
- **E.C.-GO mapping gaps**: The 30% of E.C. numbers lacking GO equivalents may indicate areas where GO annotations are either missing or potentially over-interpreted
- **Chemical specificity validation**: EC-Blast similarity measures can identify GO annotations that are too general or too specific compared to actual chemical transformation
- **Pseudo E.C. term recognition**: Identifying UniProt-created "n" terms helps distinguish well-established from preliminary enzyme classifications

### 3. **Functional Similarity Assessment**
The chapter's comparison of GO vs. E.C. similarity measures directly informs curation decisions:
- **Divergent similarity scores**: Cases where GO and EC-Blast measures differ significantly (like the 0.73 vs. 0.22 example) flag potential over-annotation issues
- **Chemical vs. ontological grouping**: Understanding when GO groups functions ontologically that are chemically distinct helps identify inappropriate functional generalizations
- **Method selection**: Choosing appropriate similarity measures based on specific functional aspects being evaluated

### 4. **Domain-Level Annotation Precision**
The chapter's domain-centric perspective addresses a major source of over-annotation:
- **Whole protein vs. domain function**: Many GO annotations assigned to complete proteins may actually represent domain-specific functions, leading to over-annotation of proteins with that domain
- **Multi-domain complexity**: Proteins with multiple domains may be over-annotated when domain-specific functions are attributed to the entire protein
- **Domain architecture analysis**: Understanding domain combinations helps identify when annotations are inappropriately broad or narrow

### 5. **Evidence Source Stratification**
The chapter's resource categorization supports systematic evidence evaluation:
- **Resource reliability hierarchy**: Understanding the curation quality and evidence basis of different resources enables weighted assessment of annotation support
- **Experimental vs. computational origins**: Distinguishing between resources based on experimental evidence (CSA, MACiE) vs. computational inference (some domain predictions) helps prioritize evidence
- **Community vs. expert curation**: Understanding annotation source (expert curators vs. community editing) informs confidence assessment

### 6. **Pathway Context Validation**
The chapter's pathway integration approach supports system-level annotation assessment:
- **Pathway consistency**: Annotations should be consistent with known pathway roles and interactions
- **Directional information**: Using pathway databases to validate GO biological process annotations against known pathway topology
- **Interaction network support**: Protein-protein interaction data can validate or contradict functional annotations

### 7. **Over-Annotation Pattern Recognition**
The chapter's comprehensive resource survey enables systematic bias detection:
- **Database-specific biases**: Understanding each resource's focus and limitations helps identify systematic over-annotation patterns
- **Resource correlation analysis**: Genes with annotations supported by multiple resources vs. those supported only by GO may indicate over-annotation
- **Functional coherence assessment**: Using multiple resources to evaluate whether gene annotation sets show appropriate functional coherence

### 8. **Quality Control Through Resource Integration**
The chapter's integration strategies provide frameworks for systematic quality assessment:
- **Cross-validation approaches**: Using multiple resources to validate individual annotations
- **Consensus-based curation**: Requiring support from multiple resources before accepting complex functional annotations
- **Resource-specific quality indicators**: Understanding reliability indicators specific to each resource type

### 9. **Specialized Function Assessment**
The chapter's specialized resource descriptions enable targeted evaluation:
- **Enzyme mechanism validation**: Using CSA and MACiE to validate detailed enzyme function annotations
- **Domain function verification**: Using CATH FunFams and SUPERFAMILY to assess domain-specific annotations
- **Pathway role confirmation**: Using Reactome and KEGG to validate biological process annotations

### 10. **Annotation Granularity Optimization**
The chapter's discussion of annotation levels supports appropriate specificity assessment:
- **Function unit identification**: Determining whether annotations should be applied to whole proteins, domains, or domain combinations
- **Specificity calibration**: Using E.C. hierarchy and domain classifications to ensure GO annotations are at appropriate specificity levels
- **Complexity management**: Understanding when multi-domain proteins warrant multiple specific annotations vs. general functional descriptions

### 11. **Future-Proofing Curation Approaches**
The chapter's comprehensive resource landscape prepares for evolving annotation needs:
- **Resource evolution tracking**: Understanding how different resources develop helps anticipate new validation opportunities
- **Integration methodology**: Systematic approaches to combining multiple resource types for comprehensive functional assessment
- **Technology advancement**: Preparation for new tools like EC-Blast that provide novel functional comparison capabilities

This comprehensive understanding of complementary functional annotation resources provides essential foundation for implementing sophisticated, multi-resource approaches to over-annotation detection that can systematically distinguish well-supported functional annotations from those lacking appropriate evidence across multiple independent functional classification systems, enabling precise curation decisions that maintain comprehensive functional coverage while removing inappropriately broad or insufficiently supported annotations.