# Chapter 9: Evaluating Functional Annotations of Enzymes Using the Gene Ontology - Summary

**Authors:** Gemma L. Holliday, Rebecca Davidson, Eyal Akiva, and Patricia C. Babbitt

## Summary

This chapter provides a specialized framework for evaluating GO annotations specifically for enzymes, drawing on the Structure-Function Linkage Database (SFLD) approach to hierarchical classification. The authors address unique challenges in enzyme annotation, including the relationship between EC numbers and GO terms, the complexity of superfamily-based annotation transfer, and sophisticated methods for detecting and preventing misannotation through sequence similarity networks and orthogonal evidence.

### Enzyme-Specific Annotation Challenges

**EC Numbers vs. GO Molecular Function Ontology:**
- **EC Number Structure**: Four-level hierarchy (A.B.C.D) where A=enzyme class, B.C=chemical details, D=substrate specificity
- **GO MFO Coverage**: Contains ~70% of all available EC numbers (limited by proteins not assigned in UniProtKB)
- **Hierarchy Complexity**: GO hierarchies often much more complex than simple 4-step EC classification
- **Complementary Information**: EC focuses on overall chemical transformation; GO provides broader functional context

**Key Limitations of Current Systems:**
- **EC Numbers**: Don't describe mechanism, cofactors, regulatory information, or structural context
- **Structural Non-contextuality**: Similar EC numbers don't necessarily imply sequence/structural similarity
- **Annotation Transfer Risk**: Especially problematic for remote homologous proteins

### Confidence-Based Annotation Framework

**SFLD Three-Tier Evidence Classification:**

1. **Fully Manually Curated (High Confidence)**:
   - Experimental evidence identified by human curators
   - Associated with relevant evidence codes
   - Greatest weight in SFLD annotation system

2. **Computational with Curator Input (Medium Confidence)**:
   - Rules derived from curator expertise
   - **>98% of GO annotations** fall into this category
   - Dependent on rule quality and specificity

3. **Computational with No Curator Input (Low Confidence)**:
   - Purely automated inference without human oversight
   - Highest risk for error propagation
   - Requires additional validation

**Evidence Quality Considerations:**
- **Reproducibility**: Higher confidence for experiments replicated across multiple studies
- **Experimental Type**: High-throughput screens often have higher false positive rates
- **Context Dependency**: Same evidence may have different confidence depending on research application
- **Annotation Accumulation**: Even low-confidence annotations may collectively support high-confidence conclusions

### Superfamily-Based Annotation Transfer

**SFLD Hierarchical Classification:**
- **Superfamily**: Largest grouping with demonstrable common ancestry
- **Subgroups**: Defined by similarity thresholds where members share more characteristics within than between groups
- **Families**: Enzymes catalyzing same reaction with same mechanism and catalytic machinery
- **Conserved Features**: Key residues, substrate/product subgraphs, partial reactions at each level

**Structure vs. Sequence-Based Approaches:**
- **Structure-based**: CATH, Gene3D, SCOP, SUPERFAMILY
- **Sequence-based**: Pfam, PANTHER, TIGRFAMs
- **Mechanistic component**: SFLD adds requirement for conserved chemical capability

**Annotation Transfer Challenges:**
- **Function-sequence similarity disconnect**: Function and sequence similarity don't always correlate
- **Unexplored protein space**: Vast majority of proteins lack experimental characterization
- **Transitivity problems**: A→B→C annotation chains may become unreliable over evolutionary distance

### Misannotation Detection and Prevention

**Sources of Misannotation:**
- **Human curation errors**: Propagated top-down through databases
- **Overly permissive rules**: Automated transfer with insufficient specificity
- **Transitivity issues**: Multi-step annotation transfer losing reliability (A 70% → B 65% → C)
- **Domain architecture changes**: Partial alignments may miss functional shifts

**Sequence Similarity Networks (SSNs) for Quality Control:**
- **Visualization approach**: Nodes represent proteins, edges represent similarity relationships
- **Cluster analysis**: Network topology reveals functional boundaries
- **Misannotation detection**: Annotations spanning multiple distinct clusters indicate over-broad transfer
- **Representative networks**: Handle large datasets by clustering highly similar sequences

**Quality Assessment Methods:**

1. **GO Enrichment Analysis for Enzyme Families**:
   - **Modified approach**: Standard enrichment doesn't work well for species-diverse enzyme sets
   - **Simple method**: Count annotation frequency, upweight experimental evidence
   - **Rigorous approach**: Statistical testing against background models using hypergeometric tests

2. **Semantic Similarity Integration**:
   - **Controlled vocabulary advantage**: Semantic relationships between GO terms
   - **Hierarchical inheritance**: Proteins inherit parent term annotations
   - **Correlation validation**: Protein sequence similarity often correlates with GO annotation semantic similarity
   - **Tools available**: Argot2, GraSM utilize semantic similarity for annotation transfer

3. **Orthogonal Information Validation**:
   - **Genomic context**: Co-location of pathway components (especially effective in prokaryotes)
   - **Domain architecture**: InterProScan analysis of predicted domains and their consistency with assigned function
   - **Hidden Markov Models**: Family-specific models for sequence placement
   - **Conservation analysis**: Presence of functionally important active site residues

### Advanced Quality Control Strategies

**Evidence Integration Approaches:**
- **Multiple evidence sources**: Combining sequence similarity, domain architecture, genomic context
- **Confidence scoring**: Weighting different types of evidence appropriately
- **Cross-validation**: Consistency checking across different annotation approaches

**Handling Complex Evolutionary Scenarios:**
- **Circular permutations**: Sequence rearrangements that obscure residue conservation
- **Conservative mutations**: Functionally equivalent amino acid substitutions
- **Moonlighting proteins**: Same sequence performing different functions in different contexts
- **Multi-domain architectures**: Proteins requiring multiple domains or subunits for function

**Statistical Approaches:**
- **Hypergeometric testing**: Standard for GO enrichment analysis
- **Background model selection**: Choosing appropriate comparison sets for significance testing
- **Multiple testing correction**: Accounting for multiple hypothesis testing in large-scale analyses

### Limitations and Caveats

**SSN Methodology Challenges:**
- **Threshold selection**: Critical for obtaining meaningful network clustering
- **Size limitations**: Computational constraints for very large protein sets
- **Domain assumptions**: Networks assume shared domain architecture
- **Expert knowledge requirement**: Interpretation requires superfamily expertise

**Complex Evolutionary Patterns:**
- **Functional promiscuity**: Proteins performing multiple reactions with different efficiencies
- **Convergent evolution**: Same reaction specificity evolving from different ancestors
- **Context-dependent function**: Same protein functioning differently in different cellular locations
- **Plurality voting pitfalls**: Majority opinion may perpetuate historical errors

**Annotation Transfer Complexity:**
- **Evolutionary relationship assessment**: Difficulty determining appropriate transfer boundaries
- **False positive thresholds**: Balance between over-conservative and over-permissive annotation
- **Experimental validation gaps**: Limited experimental data for validation
- **Multi-component systems**: Proteins requiring multiple chains or cofactors for activity

## Relevance to AI Gene Review Project

This chapter provides **essential specialized knowledge** for enzyme annotation evaluation that directly enhances our curation capabilities:

### 1. **Enzyme-Specific Over-Annotation Patterns**
Key insights for identifying problematic enzyme annotations:
- **EC number over-generalization**: Annotations may be too broad when EC hierarchy doesn't match GO complexity
- **Mechanistic assumptions**: GO terms may imply specific mechanisms not supported by evidence
- **Substrate specificity errors**: Overly specific or overly general substrate assignments
- **Cofactor requirements**: Missing or incorrect cofactor dependencies

### 2. **Evidence Quality Stratification for Enzymes**
Specialized confidence assessment framework:
- **Experimental evidence hierarchy**: Direct assays > indirect assays > computational predictions
- **Reproducibility weighting**: Multiple independent studies increase confidence
- **Assay context evaluation**: In vitro vs. in vivo evidence quality differences
- **High-throughput data skepticism**: Screen results require additional validation

### 3. **Superfamily-Based Validation**
Advanced approaches for enzyme family analysis:
- **Hierarchical validation**: Check annotation consistency at superfamily, subgroup, and family levels
- **Conserved feature analysis**: Verify presence of catalytically important residues
- **Mechanistic coherence**: Ensure annotations consistent with known reaction mechanisms
- **Evolutionary constraint assessment**: Evaluate functional conservation across phylogenetic distances

### 4. **Sequence Similarity Network Integration**
Powerful visualization and analysis tools:
- **Misannotation detection**: Identify annotations spanning functionally distinct clusters
- **Boundary determination**: Establish reliable annotation transfer thresholds
- **Quality assessment**: Visualize annotation consistency within protein families
- **Systematic bias identification**: Recognize patterns of over-broad annotation transfer

### 5. **Orthogonal Evidence Integration**
Multi-source validation strategies:
- **Genomic context validation**: Particularly valuable for bacterial enzyme annotation
- **Domain architecture consistency**: InterPro domain predictions supporting functional assignments
- **HMM family placement**: Hidden Markov Model scores for family membership confidence
- **Active site conservation**: Critical residue presence/absence analysis

### 6. **Statistical Rigor for Enzyme Families**
Sophisticated quantitative approaches:
- **Species-diverse enrichment**: Modified GO enrichment approaches for taxonomically broad enzyme sets
- **Confidence-weighted scoring**: Incorporating evidence quality into statistical tests
- **Background model selection**: Appropriate comparison sets for enzyme family analysis
- **Semantic similarity metrics**: Quantitative assessment of annotation relatedness

### 7. **Complex Annotation Scenarios**
Handling challenging enzyme cases:
- **Multi-domain enzymes**: Proteins with multiple catalytic activities requiring complex annotation
- **Enzyme complexes**: Multi-subunit systems requiring coordinated annotation
- **Moonlighting enzymes**: Context-dependent functional assignment
- **Promiscuous enzymes**: Multiple substrate specificities and reaction capabilities

### 8. **Quality Control Pipeline Integration**
Systematic approaches for our curation workflow:
- **Evidence triangulation**: Combining sequence, structure, and functional evidence
- **Annotation consistency checking**: Cross-referencing within enzyme families
- **Literature validation**: Prioritizing experimental studies over computational predictions
- **Systematic bias detection**: Identifying patterns of computational over-annotation

### 9. **Specialized Enzyme Databases**
Understanding alternative annotation sources:
- **SFLD integration**: Leveraging hierarchical enzyme classification
- **EC number validation**: Cross-referencing GO terms with enzyme commission assignments
- **InterPro family consistency**: Checking domain-function correspondence
- **Pathway context validation**: Ensuring annotations consistent with metabolic roles

This enzyme-specific expertise significantly enhances our ability to identify over-annotations, validate computational predictions, and make informed curation decisions for the substantial portion of genes that encode enzymes, providing both theoretical framework and practical tools for sophisticated functional annotation evaluation.