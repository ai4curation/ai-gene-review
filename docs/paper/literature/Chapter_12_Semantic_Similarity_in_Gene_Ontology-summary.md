# Chapter 12: Semantic Similarity in the Gene Ontology - Summary

**Author:** Catia Pesquita

## Summary

This chapter provides a comprehensive overview of semantic similarity (SS) measures applied to the Gene Ontology, exploring how the hierarchical structure and annotation corpora can be leveraged to quantitatively assess functional relationships between GO terms and gene products. The author presents a systematic framework for understanding, selecting, and evaluating SS measures, addressing both theoretical foundations and practical applications in biomedical research.

### Fundamentals of Semantic Similarity

**Core Concept:**
Semantic similarity assesses the likeness in meaning between concepts, enabling comparison of GO terms and GO-annotated gene products by exploiting ontology structure and annotation data. This supports crucial inference tasks including protein-protein interaction prediction, disease gene prioritization, and functional coherence evaluation.

**Terminology Distinctions:**
- **Semantic Similarity (SS)**: Limited to hierarchical relations (is-a, synonymy)
- **Semantic Relatedness**: Encompasses broader relations (hyponymic, hypernymic, meronymic, antonymic, functional)
- **Semantic Distance**: Generally considered opposite of similarity, though sometimes used as opposite of relatedness

**Application Levels:**
1. **Term Similarity**: Comparison between individual GO terms
2. **Gene Product Similarity**: Comparison between proteins annotated with GO term sets

### Term Similarity Approaches

**1. Structural/Internal Methods:**

**Simple Distance-Based:**
- **Edge counting**: Number of edges in path between terms
- **Limitations**: Assumes uniform edge weights, disregards hierarchical depth
- **Problem**: Equal-length paths at different ontology depths considered equivalent

**Enhanced Structural Approaches:**
- **Depth weighting**: Edges assigned different weights reflecting hierarchical depth
- **Node density consideration**: Accounting for varying ontology region density
- **Advanced metrics**: Lowest common ancestor (LCA) depth, distance to nearest leaf node, distinct GO subgraph depth

**2. External/Information-Theoretic Methods:**

**Information Content (IC) Based:**
- **Foundation**: IC(c) = -log p(c), where p(c) is occurrence probability in annotation corpus
- **Advantages**: Less sensitive to link density variability and ontology imbalances
- **Normalized IC**: Scaled values [0,1] for easier interpretation

**Common Ancestor Approaches:**
- **MICA (Most Informative Common Ancestor)**: Uses highest IC common ancestor
- **DCA (Disjoint Common Ancestors)**: Considers all disjoint common ancestors
- **Resnik's measure**: Simplest IC-based approach using MICA IC as similarity

**Hybrid Measures:**
- **Combined strategies**: Edge-based and IC-based approaches
- **Corpus-independent IC**: Based on descendants, depth, or entropy
- **Recent advances**: SSDD (semantic totipotency), SORA (structural IC), TCSS (subgraph-based)

### Gene Product Similarity Strategies

**1. Pairwise Approaches:**
- **Method**: Individual term similarities combined into global functional similarity measure
- **Combination strategies**: Average, maximum, sum of pairwise term comparisons
- **Scope options**: All-vs-all term combinations or best-matching pairs only

**2. Groupwise Approaches:**

**Set-based Methods:**
- **Direct annotations only**: Using set similarity techniques
- **Limitation**: Ignores shared ancestry between GO terms

**Graph-based Methods:**
- **Comprehensive representation**: Subgraphs including direct and inherited annotations
- **Similarity calculation**: Graph-matching techniques or set similarity on expanded annotations

**Vector-based Methods:**
- **Vector space representation**: Each term as dimension, functional similarity via vector measures
- **IC weighting**: Terms weighted by information content in vector calculations

### Issues and Challenges in Semantic Similarity

**External Issues (Annotation Corpus-Related):**

1. **Shallow Annotation Problem:**
   - **Issue**: Many proteins annotated only to general GO terms
   - **Impact**: High term overlap between dissimilar proteins
   - **Relevance**: Particularly problematic for electronic annotations (IEA)

2. **Annotation Length Bias:**
   - **Issue**: Positive correlation between similarity scores and annotation number
   - **Cause**: Non-uniform annotation distribution among proteins
   - **Impact**: Well-annotated proteins appear more similar to everything

3. **Evidence Code Effects:**
   - **IEA annotation impact**: Generally positive or null effect on performance
   - **Specific problems**: Maximum combination approaches with IEA can decrease similarity detection
   - **Quality trends**: Electronic annotation specificity improving over time

**Internal Issues (Measure Design-Related):**

1. **Term Specificity Level:**
   - **IC measures**: Corpus bias effect - rare generic terms may have high IC
   - **Depth measures**: Independent of corpus but insensitive to biological specificity variation

2. **Term Similarity Level:**
   - **Distance measures**: Same issues as depth-based specificity
   - **Ancestor selection**: Choice between single MICA vs. multiple ancestors affects performance

3. **Gene Product Similarity Level:**
   - **Maximum approach**: Focuses only on most similar aspect, missing global similarity
   - **Average approach**: Counterintuitive results for multi-functional proteins
   - **Best-match approach**: Generally superior performance by considering significant matches only

### Evaluation and Performance Assessment

**Evaluation Challenge:**
No gold standard exists for functional similarity, making measure comparison inherently subjective. Each measure formalizes functional similarity differently.

**Comparison Proxies:**
- **Sequence similarity**: Positive correlation generally found, particularly with binned data
- **Family similarity**: Pfam-based functional groupings
- **Protein-protein interactions**: SS measures generally good PPI predictors
- **Expression profiles**: Co-expression as functional similarity proxy
- **Functional modules/complexes**: Known functional groupings

**Top-Performing Measures by Application:**

| Application | Best Measures |
|-------------|---------------|
| Sequence similarity | SSDD, SimGIC, HRSS |
| Pfam similarity | SORA, SSDD, SimGIC |
| ECC similarity | SSDD, HRSS, SORA |
| Expression similarity | TCSS, SimGIC, SimIC, Best-Match-Avg (Resnik) |
| Protein-protein interaction | TCSS, SimIC, Max(Resnik) |

**Performance Trends:**
- **Classic measures**: Resnik still competitive in some settings
- **New generation dominance**: Structural and hybrid measures (SSDD, SORA, TCSS) now leading
- **Historical shift**: From pure IC-based measures to complex structural approaches
- **GO evolution impact**: Measure performance affected by ontology growth and complexity changes

### Tools and Implementation

**Web Servers:**
- **ProteInOn**: Multi-measure platform with easy interface
- **FunSimMat**: Comprehensive functional similarity database
- **GOssToWeb**: Web-based semantic similarity calculation
- **Limitations**: Fixed ontology/annotation versions, limited parametrization

**Software Packages:**
- **GoSemSim (R)**: Flexible parametrization and programmatic access
- **GOssTo**: Standalone application with version control
- **Java library**: 50+ measures, multiple input formats (OWL, OBO, RDF), high-performance (100M+ comparisons/hour)

**Selection Criteria:**
- **Web tools**: Check update frequency for current GO versions
- **Software packages**: Better for large datasets and custom analyses
- **Performance needs**: Consider computational requirements for large-scale applications

### Future Challenges and Opportunities

**GO Evolution Integration:**
- **Unexplored features**: Regulatory relationships, evidence code categorization, logical definitions
- **Cross-products**: Internal and external ontology connections
- **Axiomatization**: GO's OWL structure underutilized by current measures

**Computational Efficiency:**
- **Current limitation**: Most applications offline, speed not prioritized
- **Emerging needs**: Real-time similarity search, genomic-scale datasets
- **Solution approaches**: Parallel computation, efficiency-accuracy balance

**Semantic Sophistication:**
- **OWL axiom utilization**: Moving beyond simple DAG representation
- **Disjointness exploration**: Recently proposed for ChEBI, applicable to GO
- **Enhanced accuracy**: More semantically sound measures needed

## Relevance to AI Gene Review Project

This chapter provides **essential quantitative tools** for assessing functional relationships and annotation quality in our curation workflow:

### 1. **Annotation Consistency Assessment**
Semantic similarity measures offer sophisticated methods for evaluating annotation quality:
- **Term coherence analysis**: Using SS to identify annotations that don't fit with gene's primary functional profile
- **Cross-validation approaches**: Comparing our curated annotations with SS-predicted functional relationships
- **Outlier detection**: Identifying potentially over-annotated terms that show low similarity to core function set

### 2. **Evidence Quality Stratification Using SS**
Different SS measure performance characteristics inform evidence evaluation:
- **IC-based measure limitations**: Understanding corpus bias effects helps interpret annotation frequency as quality indicator
- **Shallow annotation problem**: Directly relevant to identifying over-general annotations requiring REMOVE actions
- **Electronic annotation effects**: SS findings about IEA impact support our evidence code-based curation decisions

### 3. **Functional Coherence Validation**
SS measures provide quantitative frameworks for assessing functional annotation sets:
- **Multi-functional protein handling**: Best-match approaches align with our understanding that proteins may have distinct functional aspects
- **Core vs. peripheral function distinction**: SS clustering approaches can help distinguish ACCEPT from KEEP_AS_NON_CORE annotations
- **Global similarity assessment**: Groupwise approaches relevant for evaluating overall annotation set appropriateness

### 4. **Over-Annotation Detection Through SS Analysis**
Several chapter insights directly support over-annotation identification:
- **Maximum combination problems**: Awareness that single high-similarity aspects can mask overall functional mismatch
- **Annotation length bias**: Understanding that similarity scores increase with annotation number helps identify annotation inflation
- **Corpus-independent measures**: Useful for validating annotations without dependency on potentially biased annotation databases

### 5. **Literature-Based Curation Enhancement**
SS measures can augment our literature-based approach:
- **Publication relevance scoring**: Using SS between paper-derived functions and existing annotations to assess literature quality
- **Functional prediction validation**: Cross-checking computationally predicted functions against literature-derived evidence using SS measures
- **Citation analysis**: Applying SS to assess consistency between different publications' functional claims

### 6. **Systematic Bias Recognition**
Understanding SS measure limitations helps identify annotation biases:
- **Depth vs. specificity issues**: Recognizing that ontology depth doesn't always correlate with biological specificity
- **Link density problems**: Understanding that GO's uneven structure affects annotation reliability assessment
- **Common ancestor artifacts**: Awareness that MICA-based approaches may miss functionally relevant relationships

### 7. **Quality Control Integration**
SS evaluation frameworks provide templates for our curation assessment:
- **Multiple validation proxies**: Using sequence, domain, interaction, and expression data as orthogonal validation approaches
- **Comparative measure assessment**: Applying multiple SS measures to build confidence in curation decisions
- **Performance benchmarking**: Using established SS evaluation approaches to assess our curation effectiveness

### 8. **Tool Integration for Scalable Analysis**
Software and computational approaches support systematic curation:
- **High-performance libraries**: For large-scale annotation consistency analysis across multiple genes
- **Programmatic access**: Enabling automated quality checks and systematic over-annotation detection
- **Custom measure development**: Framework for developing domain-specific similarity measures for our curation needs

### 9. **Advanced Curation Strategies**
Emerging SS approaches suggest future opportunities:
- **OWL axiom utilization**: Leveraging GO's logical structure for more sophisticated over-annotation detection
- **Disjointness constraints**: Using semantic exclusion principles to identify incompatible annotation combinations
- **Hybrid evidence integration**: Combining structural and information-theoretic approaches for robust quality assessment

This comprehensive understanding of semantic similarity provides both theoretical foundation and practical tools for implementing quantitative approaches to annotation curation that can systematically identify over-annotations while maintaining sensitivity to genuine functional complexity.