# Chapter 2: The Gene Ontology and the Meaning of Biological Function - Summary

**Author:** Paul D. Thomas

## Summary

This chapter provides a philosophical and practical examination of how "function" is defined and represented within the Gene Ontology framework. Thomas bridges the gap between philosophical debates about biological function and the computational implementation of functional concepts in GO.

### Key Philosophical Frameworks

**Two Major Schools of Thought:**

1. **Causal Role Function (Cummins)**: Function defined by how a part contributes to some overall capacity of a containing system
   - Example: "The function of the heart is to pump blood" (relative to circulatory system)
   - Weakness: No systematic way to identify what the larger system should be

2. **Selected Effect Function (Wright/Millikan/Neander)**: Function defined by evolutionary history - why the entity exists
   - Function = the effect for which it was selected during evolution
   - Distinguishes proper functions from "accidental" effects based on natural selection
   - Incorporates explicit evolutionary considerations

**The Molecular Biology Paradigm:**
Thomas describes how molecular biologists conceptualize function as "specific, coordinated activities that have the appearance of having been designed for a purpose." This approach:
- Uses "biological programs" to avoid connotations of intentional design
- Recognizes nested modularity (proteins have functions at multiple levels)
- Emphasizes that biological programs, when executed, perform functions by resulting in previously selected outcomes

### GO's Implementation of Function

**Three Aspects of Gene Function in GO:**

1. **Molecular Function**: Process carried out by single macromolecular machine via direct physical interactions
   - Described from two perspectives: biochemical activity AND role as component in larger system
   - Examples: binding activities, catalytic activities, receptor functions

2. **Cellular Component**: Location where molecular processes occur
   - Relative to cellular structures/compartments OR stable macromolecular complexes
   - Provides spatial context for molecular processes

3. **Biological Process**: Specific objectives the organism is genetically "programmed" to achieve
   - Described by outcome/ending state
   - Accomplished by regulated sets of molecular processes in temporal sequence
   - Can span from simple enzymatic processes to complex developmental programs

**Critical Distinctions:**
- **Gene products, not genes, have functions** - genes encode instructions, gene products perform activities
- **GO annotations are partial statements** - designed to capture incomplete biological knowledge
- **Evidence-based approach** - each annotation references supporting evidence

### Relationship to Philosophical Debate

**GO's Position:**
- GO concepts are designed to describe **selected effect functions** (evolved functions)
- However, GO concepts may not always be applied that way in practice
- Only annotations referring to biological programs can be considered to generally reflect selected effect functions

**Practical Challenges:**
- **Molecular function annotations alone** cannot automatically be interpreted as selected effect function
- **Cellular component annotations** often made from observational data without functional context
- **Protein binding controversy** - experimental observations may reflect biological noise rather than true function

**Proper vs. Candidate Functions:**
- **Hypothesis-driven studies**: Usually describe proper selected effect functions (focus on specific biological programs)
- **Large-scale studies**: Often identify candidate functions without biological program context
- ENCODE project example: inappropriately claimed to discover proper functions through large-scale biochemical activity cataloging

### Practical Implications

**Annotation Interpretation:**
- Most GO annotations likely refer to selected effect functions in practice (derived from focused molecular biology studies)
- Biological process annotations provide the strongest evidence for selected effect function
- Molecular function and cellular component annotations should be considered candidates until implicated in biological programs

**GO Consortium Initiatives:**
- Exploring computational ways to distinguish different types of biological process relationships (part of, regulates, upstream of)
- Discussing methods to help users distinguish hypothesis-driven annotations from large-scale annotations

## Relevance to AI Gene Review Project

This chapter is **foundational** for understanding the theoretical basis underlying our gene annotation curation work:

### 1. **Philosophical Framework for Function Assessment**
The distinction between proper functions (selected effects) and candidate functions directly informs our curation criteria:
- **ACCEPT**: Should be reserved for annotations representing genuine selected effect functions
- **KEEP_AS_NON_CORE/MARK_AS_OVER_ANNOTATED**: May be appropriate for candidate functions or activities not clearly linked to biological programs
- **REMOVE**: For annotations that likely represent biological noise rather than evolved function

### 2. **Understanding GO's Hierarchical Relationship to Over-annotation**
Thomas's analysis reveals a critical insight: **molecular function annotations are most susceptible to over-annotation** because:
- They can be made without reference to biological programs
- They may represent biochemical capabilities rather than evolved functions
- They require interpretation within larger system contexts to be meaningful

This directly supports our project's focus on identifying over-annotations at the molecular function level.

### 3. **Evidence Quality Assessment Framework**
The chapter's discussion of hypothesis-driven vs. large-scale studies provides a framework for evaluating annotation quality:
- **High-quality evidence**: Publications describing specific biological programs with mechanistic detail
- **Lower-quality evidence**: High-throughput studies measuring activities without biological context
- This aligns with our emphasis on literature-based curation and evidence evaluation

### 4. **Protein Binding as Paradigmatic Over-annotation**
Thomas explicitly identifies the "protein binding" debate within the GO Consortium as a prime example of potential over-annotation - exactly the type of issue our project aims to address. The recognition that "experimental observation of molecular binding may reflect biological noise" validates our skeptical approach to overly general molecular function terms.

### 5. **Systems Context Requirement**
The chapter emphasizes that proper function annotation requires understanding of larger biological systems - supporting our approach of:
- Requiring biological process context for molecular function validation
- Considering pathway and network information in curation decisions
- Evaluating whether activities contribute to survival/reproduction-related programs

### 6. **Temporal and Regulatory Considerations**
Thomas's discussion of biological processes as "regulated sets of molecular processes in temporal sequence" informs our understanding of when annotations represent core vs. peripheral functions, helping distinguish primary gene functions from secondary or developmental roles.

This philosophical foundation is essential for making principled curation decisions that properly distinguish evolved gene functions from experimental artifacts or biological noise.