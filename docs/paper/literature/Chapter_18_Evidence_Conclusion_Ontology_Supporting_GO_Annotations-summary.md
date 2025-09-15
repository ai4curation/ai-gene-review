# Chapter 18: The Evidence and Conclusion Ontology (ECO): Supporting GO Annotations - Summary

**Authors:** Marcus C. Chibucos, Deborah A. Siegele, James C. Hu, and Michelle Giglio

## Summary

This chapter describes the Evidence and Conclusion Ontology (ECO), a community resource that provides structured vocabulary for describing the diverse types of evidence used to support scientific assertions in biological databases. ECO addresses the critical need for systematic evidence documentation in biocuration by offering a hierarchical ontology that captures both the types of evidence (experimental, computational, author statements, and curator inferences) and the methods by which annotations are made (manual vs. automatic).

### The Critical Need for Evidence Documentation

**Scientific Foundation:**
- **Evidence diversity**: Scientific investigations generate data from diverse methodologies using wide-ranging tools and techniques
- **Assertion support**: Evidence forms the basis for conclusions and assertions about biological function
- **Biocuration goal**: Extract both assertions and supporting evidence from literature in structured format
- **Database integration**: Structured evidence representation enables automated quality control and selective data retrieval

**Essential Benefits of Evidence Documentation:**
1. **Methodological transparency**: Understanding what methodologies were used is central to scientific method and impacts data evaluation
2. **Query capability**: Structured evidence allows selective data queries and retrieval from large databases
3. **Quality control**: Automated quality control becomes possible with structured evidence representation

### ECO Ontological Framework

**Dual Root Structure:**
ECO comprises two main hierarchical branches:

**1. Evidence Hierarchy:**
- **Root class**: "evidence" - defined as "a type of information that is used to support an assertion"
- **Major categories**:
  - **Experimental evidence**: Laboratory and field experiment results (e.g., "chromatography evidence")
  - **Computational evidence**: In silico analysis results (e.g., "sequence similarity evidence")
  - **Author statements**: Direct statements made by authors in publications
  - **Curator inferences**: Conclusions drawn during literature curation process

**2. Assertion Method Hierarchy:**
- **Root class**: "assertion method" - defined as "a means by which a statement is made about an entity"
- **Two branches**:
  - **Manual assertion**: Human-performed annotation process
  - **Automatic assertion**: Computer-performed annotation process (equivalent to GO's IEA code)

**Cross-Product Architecture:**
- **Current version**: 630 terms describing evidence, assertion method, or "evidence × assertion method" cross products
- **Granular specificity**: Leaf nodes represent most specific evidence types (e.g., "thin layer chromatography evidence")
- **Hierarchical organization**: Child terms are more specific than parents, enabling hierarchical queries

### Evolution from GO Evidence Codes

**Historical Development:**
- **Origin**: Evolved from original GO evidence codes created for systematic evidence documentation
- **Model organism contribution**: Terms from FlyBase and TAIR incorporated into first ECO version
- **Name change**: "Evidence Code Ontology" → "Evidence and Conclusion Ontology" to reflect broader scope
- **GO integration**: GO remains active user and participant in ECO development

**Advantages over Traditional GO Codes:**
1. **Formal ontology structure**: Hierarchical relationships vs. shallow controlled vocabulary
2. **Comprehensive coverage**: Broader range of evidence types than GO codes alone
3. **Future-proof naming**: Avoids limitations of three-letter acronym system
4. **Enhanced expressivity**: More detailed evidence descriptions than simple codes

**Transition Strategy:**
- **One-to-one mapping**: Most GO evidence codes map directly to ECO terms
- **Complex mappings**: Some codes (IEA, IGC, ISS) map to specific ECO terms based on context
- **GAF format evolution**: Future transition from "evidence code" to "ECO term" in GAF format
- **Backward compatibility**: Filtering by previous codes remains possible

### Practical Applications in GO Annotation

**1. Hierarchical Data Querying:**
- **Selective queries**: Search for specific evidence types (e.g., "thin layer chromatography evidence")
- **Grouped queries**: Search for broad categories that include all specific subtypes (e.g., "chromatography evidence")
- **Scale**: Over 365 million GO annotations currently linked to evidence terms

**2. Phylogenetic Annotation Support:**
- **Tree-based approach**: GO Consortium uses phylogenetic methodology for homology-based annotations
- **New evidence terms**: Specialized terms created for inference processes
- **Current scale**: Over 150,000 annotations associated with phylogenetic evidence terms

**3. Quality Control Mechanisms:**
- **Computable rules**: Evidence requirements enforce annotation consistency
- **Protein alignment rules**: Annotations based on protein alignment must include matching protein identity
- **Ontology restrictions**: Expression pattern evidence restricted to biological process ontology
- **Circular annotation prevention**: Evidence chains evaluated to ensure experimental foundation

**4. Enhanced Integration:**
- **UniProt-GOA project**: ECO terms replace original UniProtKB evidence types
- **GPAD format**: Gene Product Association Data format includes ECO terms
- **Cross-referencing**: ECO terms cross-referenced to GO codes for seamless mapping
- **Multiple resource adoption**: Over 30 resources now use ECO for evidence representation

### Technical Implementation Benefits

**Database Management:**
- **Structured queries**: Leverage hierarchical structure for sophisticated database searches
- **Quality control pipelines**: Automated checking of evidence-annotation consistency
- **Rule enforcement**: Computational validation of evidence requirements
- **Annotation grouping**: Evidence hierarchy enables logical grouping of related annotations

**Integration Advantages:**
- **Multiple format support**: GAF and GPAD formats accommodate ECO terms
- **Cross-database compatibility**: ECO enables integration across diverse annotation sources
- **Future extensibility**: Ontological structure supports addition of new evidence types
- **Tool development**: Structured evidence supports development of analysis software

### Future Developments

**Confidence and Quality Integration:**
- **Active exploration**: Work begun on incorporating quality information into ECO
- **Confidence assessment**: Future possibility of describing evidence quality in addition to evidence type
- **Standalone systems**: Alternative approach of creating separate confidence assessment systems

**Anticipated Applications:**
- **Enhanced quality control**: More sophisticated automated quality assessment
- **Confidence scoring**: Quantitative assessment of annotation reliability
- **Evidence integration**: Better integration of multiple evidence sources
- **Community standards**: Broader adoption across biological databases

## Relevance to AI Gene Review Project

This chapter provides **essential framework** for systematic evidence evaluation and quality control in our annotation curation work, directly addressing core challenges in over-annotation detection and evidence-based decision making:

### 1. **Systematic Evidence Quality Assessment**
ECO's hierarchical structure directly supports our evidence-based curation approach:
- **Evidence hierarchy utilization**: ECO's evidence classification enables systematic ranking of annotation reliability based on evidence type strength
- **Experimental vs. computational distinction**: Clear separation between manual assertion and automatic assertion methods helps identify potentially over-annotated computational predictions
- **Evidence granularity**: Specific evidence types (e.g., "thin layer chromatography evidence") enable fine-grained assessment of annotation support quality

### 2. **Over-Annotation Detection Through Evidence Analysis**
ECO framework provides systematic approaches to identify over-annotation patterns:
- **Circular annotation detection**: ECO's chain-of-evidence evaluation directly applies to identifying annotations that lack experimental foundation
- **Computational bias recognition**: Distinction between evidence types helps identify genes with disproportionate reliance on computational predictions
- **Evidence strength stratification**: Hierarchical evidence structure enables identification of annotations supported only by weak evidence types

### 3. **Enhanced Curation Decision Framework**
ECO concepts directly inform our structured curation actions:
- **ACCEPT decisions**: Annotations supported by strong experimental evidence (direct assay, mutant phenotype) align with ECO's high-confidence categories
- **REMOVE decisions**: Annotations based on weak computational evidence or lacking evidence chains should be flagged for removal
- **MODIFY decisions**: ECO's specificity levels help determine when annotations are inappropriately general or specific

### 4. **Quality Control Pipeline Development**
ECO's systematic approach provides templates for our automated quality assessment:
- **Evidence requirement rules**: ECO's computable rules for evidence requirements can be adapted for gene-specific annotation validation
- **Ontology-specific restrictions**: ECO's approach to restricting evidence types to appropriate ontology aspects informs our validation rules
- **Cross-product validation**: ECO's evidence × assertion method combinations help ensure annotation methods match evidence types

### 5. **Literature Integration and Evidence Capture**
ECO framework supports systematic literature evidence evaluation:
- **Author statement classification**: ECO's distinction between traceable and non-traceable author statements helps evaluate literature-based evidence quality
- **Experimental evidence hierarchy**: ECO's experimental evidence categories (chromatography, assay, phenotype analysis) provide framework for evaluating publication evidence
- **Manual curation support**: ECO's manual assertion methods align with our literature-based annotation approach

### 6. **Computational Annotation Evaluation**
ECO's treatment of automatic assertion directly addresses IEA annotation challenges:
- **Electronic annotation skepticism**: ECO's automatic assertion category helps systematically evaluate computational predictions
- **Algorithm-specific assessment**: ECO's granular computational evidence types enable method-specific reliability assessment
- **Propagation bias detection**: ECO's sequence similarity and homology evidence categories help identify over-annotation through computational propagation

### 7. **Multi-Source Evidence Integration**
ECO's comprehensive evidence framework supports complex curation decisions:
- **Evidence weight integration**: ECO hierarchy enables weighted assessment when multiple evidence types support single annotations
- **Conflicting evidence resolution**: ECO's structured approach to evidence types helps resolve contradictory annotation evidence
- **Evidence gap identification**: ECO framework helps identify annotations lacking appropriate supporting evidence

### 8. **Database Integration and Standardization**
ECO's multi-database adoption provides foundation for our systematic approach:
- **Cross-database comparison**: ECO standardization enables comparison of annotation quality across different sources (UniProt-GOA, model organism databases)
- **Evidence mapping consistency**: ECO's cross-referencing to GO codes ensures consistent evidence interpretation
- **Quality benchmarking**: ECO adoption by multiple resources provides community standards for evidence quality

### 9. **Automated Quality Control Implementation**
ECO's computational applications directly translate to our quality control needs:
- **Rule-based validation**: ECO's computable rules provide templates for automated annotation validation
- **Evidence chain analysis**: ECO's circular annotation prevention methods apply directly to our over-annotation detection
- **Systematic flagging**: ECO's quality control mechanisms enable automated identification of problematic annotations

### 10. **Training and Consistency Framework**
ECO's structured approach supports systematic curation training:
- **Evidence evaluation standards**: ECO hierarchy provides objective framework for training consistent evidence assessment
- **Quality control education**: ECO's systematic approach to evidence documentation provides examples of best practices
- **Decision consistency**: ECO framework enables reproducible, systematic annotation decisions across different curators

### 11. **Future-Proofing and Extension**
ECO's extensible framework supports evolution of our curation approaches:
- **Confidence integration**: ECO's planned confidence assessment features align with our need for annotation reliability scoring
- **New evidence types**: ECO's ontological structure supports addition of new evidence categories as scientific methods evolve
- **Community integration**: ECO's broad adoption enables integration with community-wide quality control initiatives

This comprehensive understanding of evidence ontology and systematic evidence evaluation provides essential foundation for implementing sophisticated, evidence-based approaches to over-annotation detection that can systematically distinguish well-supported functional annotations from computationally over-interpreted or inadequately supported assertions, enabling precise curation decisions that maintain high-quality functional annotation while removing inappropriate over-annotations.