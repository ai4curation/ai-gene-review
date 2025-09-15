# Chapter 6: Text Mining to Support Gene Ontology Curation and Vice Versa - Summary

**Author:** Patrick Ruch

## Summary

This chapter explores the symbiotic relationship between text mining technologies and GO curation, demonstrating how automated text categorization can support functional annotation while curated databases enable advances in text mining capabilities. Ruch presents a decade of progress in automatic GO term assignment, showing dramatic improvements in precision and recall, while introducing the concept of "Deep Question-Answering" systems that leverage curated content for generating complex functional descriptions.

### Key Technological Approaches

**Text Mining Pipeline for Curation:**
The chapter outlines a comprehensive 6-9 step curation workflow supported by text mining:
1. **Retrieval/Collection**: Document search and identification
2. **Selection/Triage**: Filtering relevant papers for curation
3. **Reading/Passage retrieval**: Identifying key sections within articles
4. **Entity extraction/indexing**: Named entity recognition for genes, proteins, chemicals
5. **Entity normalization**: Assigning unique identifiers to recognized entities
6. **Relationship + evidence annotation**: Extracting functional relationships
7. **Evidence extraction**: Capturing supporting images, figures
8. **Feed-back/Check of records**: Iterative quality control

**Two Main Computational Strategies:**

### 1. Lexical Approaches
- **Direct string matching** between document text and GO term labels/synonyms
- Uses term frequency, inverse document frequency, and positional information
- **Major limitation**: Complex GO terms (containing dozen words) are "virtually unmatchable" in literature
- Early BioCreative results were disappointing: best systems achieved 80% precision but <20% recall

### 2. Machine Learning Approaches (k-Nearest Neighbors)
- **Training on GOA database**: Uses existing [GO term; PMID] pairs as training data
- **k-NN methodology**: For new documents, finds k most similar annotated instances
- **Superior performance**: k-NN approaches significantly outperform lexical methods
- **Stability over time**: Remarkably, models trained on old data (2003-2007) perform nearly as well as recent models

### Performance Evolution and Achievements

**Dramatic Improvements (2005-2015):**
- **+225% improvement** in both precision and recall over decade
- **GOCat system** now achieves ~67% accuracy (2 out of 3 correct assignments)
- **BioCreative IV results**: Full-text analysis shows high content redundancy - only 10-20% of article content needed for top-ranked GO assignments

**Key Findings on Information Content:**
- **80-90% redundancy** in published literature from information-theoretic perspective
- **Abstract superiority**: Higher information density than full-text articles
- **Sentence selection**: Few high-precision sentences sufficient for accurate GO assignment

### Named Entity Recognition Challenges

**Biomedical NER Complexity:**
- **Diverse entity types**: Genes, proteins, species, chemicals, diseases, phenotypes
- **GO term recognition particularly challenging**: Requires "deeper understanding" of biological concepts
- **Complex concept integration**: GO terms combine subconcepts from multiple semantic types (molecules, processes, locations)

**Limitations of Traditional NER:**
- **Textual contiguity assumption**: Entities assumed to be contiguous text strings
- **Complex GO concepts**: May require combination of distant text elements
- **Entity normalization challenges**: Lexical ambiguity requires context for disambiguation

### Advanced Applications: Deep Question-Answering

**Traditional QA Limitations:**
- Standard QA systems effective for factual questions (70-80% precision)
- **Cannot answer complex functional questions** like "What molecular functions are associated with tp53?"
- **Expected answers don't exist** in any corpus - require generation from curated knowledge

**Deep QA Innovation:**
- **DeepQA4GO system**: Generates complex GO descriptor answers
- **Performance**: ~67% accuracy vs. ~33% for traditional QA systems
- **Novel capability**: Can generate answers like "RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription"

### Data Stewardship and Future Directions

**Critical Data Loss Problem:**
- **Curation decisions not recorded**: Valuable positive/negative selection information lost
- **Training data shortage**: Text mining systems need explicit records of what curators accept/reject
- **Recommendation**: Databases must record all curation decisions, including rejected materials

**Integration with Biological Databases:**
- **Cross-product databases**: Additional valuable resources for GO assignment
- **Complementary approaches**: Lexical methods can assign rare terms; k-NN methods depend on training data volume
- **Interactive vs. automatic modes**: Systems can provide ranked lists for human review or make autonomous assignments

## Relevance to AI Gene Review Project

This chapter provides **crucial insights** for understanding and improving our automated annotation review system:

### 1. **Electronic Annotation Quality Assessment**
The chapter's analysis of text mining limitations directly informs our over-annotation detection:
- **IEA annotation origins**: Many electronic annotations derive from text mining systems with known precision limitations (~67%)
- **Method-specific biases**: Lexical approaches favor simple terms; k-NN approaches reflect training data biases
- **Information redundancy**: 80-90% of literature content is redundant, potentially leading to confidence over-estimation

### 2. **Understanding Computational Annotation Propagation**
Text mining contributes significantly to annotation databases, creating cascading effects:
- **Error propagation cycles**: Text mining systems trained on databases containing previous text mining predictions
- **Concept drift resistance**: Surprisingly, older training data remains effective, suggesting stable functional concepts
- **Training data dependency**: All automatic systems ultimately rely on experimental annotations as ground truth

### 3. **Complex Term Recognition Challenges**
The chapter explains why certain annotation patterns are problematic:
- **Long, specific GO terms**: "Virtually unmatchable" in literature, likely leading to under-representation
- **Multi-component concepts**: Complex molecular functions combining multiple semantic elements prone to oversimplification
- **Context sensitivity**: Same experimental results can support different functional interpretations

### 4. **Literature-Based Curation Optimization**
Insights for improving our literature-based review process:
- **Information density variation**: Abstracts contain higher-quality functional information than full text
- **Section-specific value**: Results sections more informative than background for novel findings
- **Redundancy exploitation**: Multiple papers often describe same functions with different terminology

### 5. **Deep QA Relevance for Over-Annotation Detection**
The DeepQA4GO concept parallels our annotation synthesis challenges:
- **Complex answer generation**: Like our system, requires combining curated knowledge to generate appropriate functional descriptions
- **Training on expert curation**: Our approach of learning from high-quality manual annotations mirrors Deep QA methodology
- **Unmatchable answer problem**: Many appropriate GO terms may not appear explicitly in literature

### 6. **Evidence Quality Stratification**
Chapter findings inform our evidence evaluation framework:
- **Inter-annotator agreement**: Even expert curators agree only 39-43% of the time, highlighting annotation subjectivity
- **Precision vs. recall trade-offs**: High-precision systems often have low coverage, suggesting conservative annotation approaches
- **Full-text vs. abstract utility**: Abstract-based systems may be more reliable than full-text approaches

### 7. **Systematic Bias Recognition**
Understanding text mining biases helps identify over-annotation patterns:
- **Training set limitations**: Systems cannot predict functions absent from training data
- **Frequency bias**: Common annotations over-represented; rare but specific functions under-predicted
- **Temporal bias**: Annotation practices may reflect historical understanding rather than current knowledge

### 8. **Quality Control Integration**
The chapter's emphasis on recording curation decisions supports our systematic approach:
- **Decision documentation**: Our structured annotation review format captures valuable training signal
- **Positive/negative examples**: Recording both accepted and rejected annotations provides balanced training data
- **Iterative improvement**: Using our curation decisions to improve future annotation quality

This understanding of text mining capabilities and limitations is essential for making informed curation decisions that account for the computational origins of many existing GO annotations, helping distinguish genuine functional predictions from over-interpretation or methodological artifacts.