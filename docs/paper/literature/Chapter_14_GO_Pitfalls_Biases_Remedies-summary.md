# Chapter 14: Gene Ontology: Pitfalls, Biases, and Remedies - Summary

**Authors:** Pascale Gaudet and Christophe Dessimoz

## Summary

This chapter provides a comprehensive guide to understanding and mitigating the various pitfalls and biases inherent in Gene Ontology (GO) data and analyses. The authors systematically examine how GO's heterogeneous nature, despite efforts at normalization, can introduce considerable biases in large-scale analyses, and they provide practical solutions for addressing these challenges.

### Core Perspective: Observational vs. Experimental Data

**Fundamental Distinction:**
The chapter establishes GO annotations as **observational data** rather than experimental data, with critical implications:
- **Experimental data**: Controlled conditions where case and control groups differ only in the factor of interest
- **Observational data**: Readily available data with potential unknown confounding factors
- **Critical implication**: Testing and controlling for potential confounders becomes paramount

### Simpson's Paradox and Data Aggregation Perils

**Classic Example - Berkeley Gender Bias Case:**
- **Aggregate data**: 44% men admitted vs. 35% women (appeared discriminatory)
- **Department-level analysis**: Similar admission rates for both sexes, even favoring women in most departments
- **True confounder**: Women tended to apply to more competitive departments with lower admission rates
- **GO relevance**: Heterogeneous GO data can manifest similar paradoxes, emphasizing need for confounder recognition

### Open World Assumption and Data Incompleteness

**Core Principle:**
- **Fundamental assumption**: Absence of evidence ≠ absence of function
- **Database scale**: Over 210 million annotations currently, but incompleteness remains pervasive
- **Uneven distribution**: More comprehensively annotated parts can present contradictory information
- **Evaluation impact**: Can lead to inflated false positive rates in computational method assessment
- **Mitigation strategies**: Annotation thinning, successive database release analysis

### Ontology Structure Pitfalls

**1. Relationship Transitivity Issues:**

**Transitive relationships:**
- **"is a" and "part of"**: Proteins annotated to specific terms implicitly annotated to all parents
- **Example**: "serine/threonine protein kinase activity" → "protein kinase activity"

**Non-transitive relationships:**
- **"regulates" relations**: Semantics don't propagate to parents
- **Critical example**: "peptidase inhibitor activity" connects to "proteolysis" via non-transitive "negatively regulates" - the protein does NOT mediate proteolysis

**2. Inter-ontology Links and Enrichment Impact:**
- **Automatic annotation generation**: "part of" relations across ontology aspects trigger additional annotations
- **Massive scale**: 12 million annotations to 7 million proteins from these links
- **Volatility example**: November 2011 loss of ~2,500 annotations to "transcription, DNA-dependent" due to single link removal
- **Analysis sensitivity**: Can dramatically affect GO enrichment analyses and background distributions

**3. GO File Versions:**
- **GO-basic**: Completely acyclic, for applications requiring graph traversal
- **GO**: Includes cross-hierarchy relationships ("has part", "occurs in")
- **GO-plus**: Most complex, with external ontology connections and biological constraints

### Annotation Qualifiers and Semantic Nuances

**Three Critical Qualifiers:**

**1. "NOT" Qualifier:**
- **Function**: Indicates evidence that gene product lacks expected function
- **Usage cases**: Missing active site residues, negative experimental results
- **Propagation pattern**: Propagates to children terms, not parents (opposite of positive annotations)
- **Impact example**: STRADA pseudokinase annotated as "NOT protein kinase activity"

**2. "contributes to" Qualifier:**
- **Primary use**: Molecular function distributed across complex subunits
- **Permissive usage**: Sometimes applied to all complex subunits regardless of direct contribution
- **Interpretation challenge**: May seem counterintuitive (e.g., cyclin with kinase activity annotation)

**3. "co-localizes with" Qualifier:**
- **Dual meaning problem**: Transient association OR experimental resolution limitation
- **Current limitation**: Cannot distinguish between the two meanings in existing annotations

### Evidence Code Biases and Reliability

**Evidence Code Hierarchy by Reliability:**

**1. Direct Evidence (IDA - Inferred from Direct Assay):**
- **Highest reliability**: Most direct protein-function implication
- **Limitation**: Still doesn't guarantee specific mechanistic details

**2. Mutant Phenotype Evidence (IMP, IGI):**
- **Utility**: Excellent for pathway/process implication
- **Weakness**: Inherently derivative, difficult to assess exact involvement mechanism
- **Same limitation**: Genetic interaction evidence (IGI)

**3. Physical Interaction Evidence (IPI):**
- **Strong for**: Protein binding annotations, cellular component assignments
- **Weak for**: Molecular functions and biological processes ("guilt by association")
- **Low confidence**: Expression pattern evidence (IEP)

**4. High-throughput Experiment Biases:**
- **Term bias**: Tend toward high-level GO terms with limited functional diversity
- **Information content distortion**: Artificial decrease due to frequent annotation
- **Database impact**: ~25% of annotations from high-throughput papers
- **Current limitation**: GO doesn't record high-throughput vs. focused study origin

**5. Electronic Annotation Methods:**
- **Method diversity**: InterPro domains, Enzyme Commission numbers, BLAST, orthology
- **Reference code tracking**: Available but not integrated into standard evidence codes
- **Disproportionate impact**: Large numbers can skew analyses
- **Normalization challenges**: Multiple annotations to same term with different evidence

### Species-Specific and Systematic Biases

**1. Species Research Focus Bias:**
- **Zebrafish**: Heavily developmental biology focused
- **Rat**: Standard toxicology model
- **Implication**: GO term frequencies vary dramatically across species
- **Solution**: Use species-specific backgrounds for enrichment analyses

**2. Authorship Bias:**
- **Striking finding**: Annotations from same paper ~50× more similar than different papers
- **Impact on evolution studies**: Same-species paralogs appeared more functionally conserved than orthologs due to annotation source bias
- **Controlled analysis**: Bias elimination revealed orthologs actually more conserved
- **Partial effect**: Even different papers with common authors show increased similarity

**3. Annotator/Database Bias:**
- **Example comparison**: MGI vs. UniProt mouse annotations
- **Evidence code distribution**: Similar overall (IMP most common), but different term focus
- **Specific divergences**: MGI emphasizes "in utero embryonic development" (1,170 annotations); UniProt focuses on "regulation of circadian rhythm"
- **Implication**: Annotations biased toward specific biological aspects, not uniform representation

**4. Propagation Bias (Electronic vs. Experimental):**
- **Observation**: Electronic annotations show higher similarity between homologs than experimental annotations
- **Explanation**: Electronic methods infer annotations among homologous sequences, artificially inflating functional similarity
- **Analysis caution**: Problematic when comparing model organisms (experimental-rich) with non-model organisms (electronic-rich)

### Advanced Bias Categories

**1. Annotation Extensions:**
- **New mechanism**: Increased expressivity through contextual information
- **Examples**: Location specificity (retinal ganglion cells), dynamic localization (mitotic anaphase), enzyme substrates
- **Current challenges**: Inconsistent implementation across databases, guidelines still developing
- **Analysis impact**: Creates "virtual" GO classes, substantial annotation inflation potential

**2. Positive/Negative Annotation Imbalance:**
- **Scale**: <1% of experimental annotations are negative in UniProt-GOA
- **Publication bias**: Negative results less publishable, harder to establish experimentally
- **Machine learning impact**: Class imbalance problems, metric reliability issues
- **Evaluation effects**: Particularly problematic under Open World Assumption

### Remedies and Best Practices Framework

**1. Data Completeness Management:**
- **Acknowledge incompleteness**: Don't assume absence of annotation implies absence of function
- **Impact assessment**: Use annotation thinning or successive database releases to gauge incompleteness effects
- **Open World Assumption**: Always consider in evaluation frameworks

**2. Structural Relationship Handling:**
- **Transitivity awareness**: Understand which relationships propagate annotations ("is a", "part of") vs. which don't ("regulates")
- **Graph file selection**: Use GO-basic for acyclic requirements, GO-plus for full expressivity
- **Inter-ontology link tracking**: Monitor database releases for structural changes affecting analyses

**3. Enrichment Analysis Robustness:**
- **Background specification**: Use appropriate, consistent background distributions
- **Multiple release validation**: Ensure conclusions hold across recent database versions
- **Tool currency**: Avoid outdated tools (example: DAVID not updated since 2009)
- **Current recommendation**: PantherDB GO analysis service for up-to-date analyses

**4. Evidence Code Stratification:**
- **Code-aware analysis**: Consider evidence type distribution in statistical analyses
- **Bias control**: Account for high-throughput vs. focused study differences
- **Multiple evidence integration**: Appropriately normalize when genes have multiple evidence types for same term

**5. Species and Systematic Bias Control:**
- **Species-specific analysis**: Use organism-appropriate backgrounds and term frequencies
- **Authorship bias mitigation**: Control for publication source in analyses with varying paper origin distributions
- **Annotator bias awareness**: Understand database-specific annotation focus patterns

**6. Qualifier Integration:**
- **Mandatory consideration**: Always account for NOT, "contributes to", and "co-localizes with" qualifiers
- **Tool verification**: Ensure analysis software properly handles qualifiers
- **Semantic precision**: Understand qualifier-specific propagation patterns

### Comprehensive Pitfall Summary Table

The chapter provides an extensive table of 13 major pitfalls with specific remedies:

1. **Open World Assumption violations** → Impact assessment and incompleteness acknowledgment
2. **Transitivity misunderstanding** → Relationship-aware reasoning
3. **Background distribution errors** → Consistent database versions and appropriate backgrounds
4. **Inter-ontology link volatility** → Database release tracking
5. **Qualifier ignorance** → Mandatory qualifier consideration
6. **Evidence code bias** → Stratified analysis approaches
7. **Species research bias** → Species-specific frequency usage
8. **Authorship bias** → Publication source control
9. **Propagation bias** → Experimental annotation restriction for evolution studies
10. **Positive/negative imbalance** → Separate rate consideration and focused subset analysis

## Relevance to AI Gene Review Project

This chapter provides **fundamental guidance** for understanding and addressing the systematic biases that contribute to over-annotation problems in our gene curation workflow:

### 1. **Over-Annotation Source Identification**
The chapter's bias catalog directly maps to over-annotation mechanisms:
- **Electronic annotation propagation bias**: Explains why electronic annotations (IEA) often appear inflated among homologs
- **High-throughput experiment bias**: Identifies why certain terms become over-represented in databases
- **Authorship bias**: Explains clustering of similar annotations from same research groups, leading to apparent functional convergence

### 2. **Evidence Quality Assessment Framework**
The evidence code hierarchy provides structured approach to annotation evaluation:
- **IDA (Direct Assay)**: Highest confidence, ACCEPT unless contradicted
- **IMP/IGI (Phenotype/Interaction)**: Moderate confidence, require mechanistic validation
- **IPI (Physical Interaction)**: Context-dependent, strong for binding/localization, weak for molecular functions
- **IEP (Expression Pattern)**: Low confidence, often suitable for REMOVE actions
- **Electronic methods**: Systematic over-annotation risk, requiring careful evaluation

### 3. **Systematic Bias Recognition in Literature**
Understanding systematic biases helps identify over-annotation patterns in publications:
- **Same-paper bias**: Multiple annotations from single publication may reflect methodological artifacts rather than true functional diversity
- **Species research focus**: Over-representation of certain functional categories due to model organism specializations
- **High-throughput study bias**: Shallow, broad annotations rather than specific, mechanistic insights

### 4. **Qualifier-Based Curation Precision**
The chapter's qualifier analysis directly supports sophisticated curation decisions:
- **"NOT" annotations**: Critical for identifying proteins that lack expected homolog functions (STRADA pseudokinase example)
- **"contributes to"**: Helps distinguish direct catalytic activity from regulatory/structural roles
- **"co-localizes with"**: Enables recognition of transient vs. permanent associations

### 5. **Open World Assumption Application**
Critical for avoiding over-interpretation of database completeness:
- **Annotation absence interpretation**: Cannot conclude functional absence from annotation absence
- **Comparative analysis caution**: Different annotation coverage across genes may reflect curation history rather than functional differences
- **Negative annotation scarcity**: <1% negative annotations suggests systematic under-representation of negative results

### 6. **Enrichment Analysis Sophistication**
Insights for evaluating functional coherence in gene annotation sets:
- **Background distribution criticality**: Inappropriate backgrounds can create false functional enrichments
- **Inter-ontology link awareness**: Automatic annotation generation can inflate apparent functional complexity
- **Species-specific analysis**: Essential for appropriate functional characterization

### 7. **Transitivity-Aware Annotation Evaluation**
Structural relationship understanding prevents logical errors:
- **"is a"/"part of" transitivity**: Specific annotations imply general annotations
- **"regulates" non-transitivity**: Regulatory relationships don't propagate through hierarchies (peptidase inhibitor ≠ proteolysis mediator)
- **Cross-ontology propagation**: Molecular function annotations can automatically generate process annotations

### 8. **Electronic Annotation Skepticism Framework**
Systematic approach to IEA evaluation based on propagation bias understanding:
- **Homology inference bias**: Electronic annotations artificially inflate similarity between related genes
- **Method-specific evaluation**: Different electronic methods (InterPro, orthology, BLAST) have distinct error profiles
- **Model vs. non-model organism considerations**: Electronic annotation proportion varies dramatically

### 9. **Multi-Evidence Integration**
Framework for handling conflicting or redundant evidence:
- **Evidence code weighting**: Appropriate confidence assignment based on experimental directness
- **Contradictory result interpretation**: Understanding when conflicts reflect genuine biological complexity vs. methodological differences
- **Multiple annotation normalization**: Avoiding artificial inflation when same function supported by multiple evidence types

### 10. **Temporal and Database Evolution Awareness**
Understanding how annotation landscapes change over time:
- **Database release sensitivity**: Major structural changes can affect annotation sets dramatically
- **Annotation accumulation patterns**: New experimental evidence tends to confirm rather than contradict existing annotations
- **Tool currency requirements**: Outdated analysis tools can provide misleading results due to structural changes

This comprehensive understanding of GO biases and pitfalls provides essential foundation for implementing sophisticated over-annotation detection that distinguishes genuine biological complexity from systematic artifacts, methodological biases, and database incompleteness effects. The chapter's remedies directly inform our curation decision framework and quality control approaches.