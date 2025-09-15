# Chapter 5: Computational Methods for Annotation Transfers from Sequence - Summary

**Authors:** Domenico Cozzetto and David T. Jones

## Summary

This chapter provides a comprehensive overview of computational methods for predicting protein function from amino acid sequences, focusing on GO term assignment approaches. The authors emphasize that while experimental functional data acquisition is slow, sequence data grows exponentially, creating a massive annotation gap that computational methods are essential to bridge.

### The Functional Annotation Gap

**Scale of the Problem:**
- Only 0.03% of sequences in UniProtKB have experimental GO annotations for all three domains
- Exponential growth in sequences vs. linear growth in experimental annotations
- Even with electronic inference, >80% of sequences lack complete GO coverage
- Manual curation cannot scale to meet demand

**Knowledge-Based Approach:**
- No general theory linking sequence to function from first principles
- Current methods implement **knowledge-based heuristics** transferring functional information from annotated to unannotated proteins
- All computational approaches ultimately depend on experimental annotations as training data

### Four Main Computational Approaches

### 1. Homology-Based Annotation Transfer

**Basic Principle:**
- Find homologous proteins (common ancestry) with known function
- Transfer annotations under assumption that function is evolutionarily conserved
- Uses BLAST, PSI-BLAST, HMMs for sequence comparison

**Challenges and Limitations:**
- **Error propagation**: Iterative transfers of computational annotations compound errors
- **Domain architecture changes**: Partial alignments may indicate functional shifts
- **Similarity thresholds**: 80% global sequence identity suggested as "safe" threshold, but this is context-dependent
- **Evolutionary rate variation**: Different proteins/families evolve at different rates

**Advanced Methods:**
- **GOtcha**: First tool to weight GO terms by enrichment in BLAST hits, considering hierarchical context
- **PFP**: Targets difficult cases using high E-value PSI-BLAST hits and GO term co-occurrence data
- **Machine learning approaches**: Use alignment-derived features to train classifiers for GO term prediction

### 2. Orthology-Based Annotation Transfer

**Conceptual Advancement:**
- Distinguishes **orthologs** (evolved after speciation) from **paralogs** (evolved after duplication)
- Based on assumption that orthologs retain function better than paralogs
- Accounts for functional divergence after gene duplication events

**Key Findings:**
- Ortholog/paralog distinction provides **modest improvement** over simple homology
- Functional similarity between orthologs only slightly higher than paralogs at same sequence divergence
- Signal strongest for cellular components, weaker for biological processes/molecular functions
- Both orthologs and paralogs can diverge or retain function

**Implementation Approaches:**
- **Phylogenetic methods**: SIFTER uses Bayesian inference on phylogenetic trees
- **PAINT**: GO Consortium's tool allowing uncoupled functional changes, no assumptions about evolutionary distance
- **Clustering methods**: EggNOG, Ensembl Compara, PANTHER, OMA create ortholog groups for annotation transfer

### 3. Protein Family-Based Annotation Transfer

**Domain/Motif Recognition:**
- Uses **short linear motifs** (10-20 amino acids) for molecular recognition, targeting, regulation
- **Sequence profiles** and **hidden Markov models** for family assignment
- Can predict function even with limited sequence similarity to characterized proteins

**Major Resources:**
- **InterPro**: Collates results from 11 specialized databases, provides hierarchical family organization
- **InterPro2GO mapping**: Links protein domain families to most specific applicable GO terms
- Forms bulk of electronic annotations in UniProtKB

**Structural Classification Methods:**
- **CATH-Gene3D**: Uses CATH structural classification, clusters into functional families
- **SUPERFAMILY**: Based on SCOP structural classification
- **dcGO**: Builds HMM models for domains and supra-domains, provides confidence scores

### 4. De Novo Feature-Based Prediction

**When Needed:**
- No detectable homologs or no functional annotations for homologs
- Most challenging scenario requiring inference from sequence features alone

**Feature-Based Approach:**
- Transform sequence into component features (transmembrane helices, disordered regions, signal peptides, etc.)
- Relate features to broad functional classes using supervised machine learning
- Address question: "What functions can proteins perform with given features?"

**Key Methods:**
- **ProtFun**: Neural networks using biochemical attributes (charged amino acids, transmembrane helices, etc.)
- **FFPred**: Support vector machines incorporating intrinsic disorder patterns

**Advantages and Limitations:**
- **Advantages**: Works without homology, can handle orphan proteins, predicts alternative splicing effects
- **Limitations**: Requires sufficient training examples, generally limited to high-level GO terms, cannot make highly specific predictions

### Integration and Future Directions

**Multi-Data Integration:**
- **Structural information**: 3D structure enables binding site and catalytic site prediction
- **Genomic context**: Gene fusion events, chromosomal proximity, co-occurrence patterns
- **Phylogenetic profiling**: Co-evolution suggests functional coupling
- **Systems data**: Protein-protein interactions, expression profiles, phenotypic data

**Performance Characteristics:**
- **Sequence/structure data**: Better for molecular function prediction
- **Genome-wide datasets**: Better for biological processes and subcellular localization
- **Integrative approaches**: Combine heterogeneous data sources to reduce errors and overcome individual method limitations

### Error Propagation and Quality Control

**Critical Issues:**
- **Annotation error rates**: Approach 0% only in manually curated SwissProt, substantially higher in unreviewed databases
- **Iterative error amplification**: Computational predictions used as input for further predictions
- **Similarity threshold challenges**: Fixed thresholds (80% identity) can be too stringent or too lax depending on protein family
- **Training set dependency**: All computational methods ultimately rely on experimental annotations

## Relevance to AI Gene Review Project

This chapter provides **crucial context** for understanding the computational origins of many GO annotations we encounter in our curation work:

### 1. **Electronic Annotation Critical Assessment**
Understanding computational prediction limitations directly informs our over-annotation detection:
- **IEA annotations** (most abundant evidence code) represent computational predictions with inherent error rates
- **Error propagation concern**: Computational annotations used as training data for more computational annotations
- **Family-specific accuracy**: Different protein families have different reliability thresholds for computational transfer

### 2. **Evidence Code Interpretation Framework**
The chapter's method classification helps interpret annotation quality:
- **ISS/ISO family codes**: Represent homology-based transfers with varying reliability based on similarity levels
- **InterPro2GO mappings**: Source of many IEA annotations, limited to broad functional categories
- **Phylogenetic codes (IBA/IBD)**: From orthology-based methods with modest improvement over simple homology

### 3. **Systematic Bias Identification**
Computational methods introduce predictable biases relevant to over-annotation:
- **High-level term bias**: Feature-based methods limited to general GO terms
- **Homology transfer bias**: May propagate inappropriate specificity levels
- **Domain architecture insensitivity**: May miss functional changes despite sequence similarity
- **Training set bias**: Reflect biases in underlying experimental annotations

### 4. **Quality Assessment Criteria**
The chapter provides frameworks for evaluating computational annotation quality:
- **Similarity threshold awareness**: 80% identity rule-of-thumb has many exceptions
- **Alignment coverage importance**: Partial alignments may indicate functional divergence
- **Evolutionary context consideration**: Ortholog/paralog relationships provide modest quality signals
- **Evidence integration**: Multiple computational methods provide higher confidence than single methods

### 5. **Over-annotation Pattern Recognition**
Understanding computational methods helps identify over-annotation patterns:
- **Inappropriate specificity**: Computational methods may assign overly specific terms when evidence supports only general functions
- **Domain-function mismatch**: Family-based methods may not account for multi-domain architecture complexity
- **Context insensitivity**: May miss tissue/condition-specific functional restrictions
- **Evolutionary distance errors**: May transfer annotations across inappropriate evolutionary distances

### 6. **Annotation Source Traceability**
Knowledge of computational pipelines helps trace annotation origins:
- **UniProtKB electronic pipeline**: Understanding which computational tools contribute to IEA annotations
- **Database cross-contamination**: Computational annotations from one database used as input to others
- **Method combination effects**: Different computational approaches may reinforce each other's biases

### 7. **Curation Decision Framework**
The chapter's insights inform our curation criteria:
- **REMOVE decisions**: For annotations likely representing computational errors or inappropriate transfers
- **MODIFY decisions**: When computational methods assign wrong specificity level but correct general function
- **KEEP_AS_NON_CORE**: For computationally-derived annotations that may be correct but lack strong evidence
- **Evidence requirement standards**: Higher evidence standards for annotations contradicting computational predictions

This understanding of computational annotation methods is essential for making informed decisions about which electronic annotations represent legitimate functional predictions versus over-interpretation or error propagation.