# Chapter 3: Primer on the Gene Ontology - Summary

**Authors:** Pascale Gaudet, Nives Škunca, James C. Hu, and Christophe Dessimoz

## Summary

This chapter serves as a comprehensive practical guide to understanding and using the Gene Ontology (GO), structured around five fundamental questions. It provides essential knowledge for researchers who need to understand GO's structure, interpret annotations, and use GO resources effectively.

### Key Concepts and Structure

**What is the GO?**
- **Controlled vocabulary** organized into three distinct ontologies:
  - **Molecular Function (MF)**: Activities performed by gene products
  - **Biological Process (BP)**: Larger objectives achieved by coordinated molecular functions
  - **Cellular Component (CC)**: Locations where molecular functions occur

- **Graph structure**: Terms connected by relationships (is_a, part_of, regulates) forming directed acyclic graphs
- **Scale**: ~44,000 terms with >73,000 relationships (as of 2015)
- **GO Slims**: Curated subsets for specific applications (e.g., Generic GO slim, ChEMBL Drug Target slim)

**Dynamic Nature:**
- **Daily updates** with version numbers as dates
- **Term obsoletion**: Terms never deleted, but marked obsolete with rationale
- **Relationship changes**: Don't affect existing annotations (annotations tied to specific terms)

### Annotation Framework

**GAF (Gene Association File) Structure:**
The chapter details the 17-field GAF format, covering:
- **Annotation object** (7 fields): Database, accession, symbol, type, organism, etc.
- **GO term information** (3 fields): GO ID, aspect (MF/BP/CC), qualifiers
- **Evidence information** (3 fields): Reference, evidence code, with/from
- **Metadata** (4 fields): Date, annotating database, extensions, isoform info

**Critical Qualifiers:**
- **NOT**: Negates annotation (protein does NOT have this function)
- **contributes_to**: For complex components
- **colocalizes_with**: For cellular component co-location

**Annotation Extensions:**
- Allow combination of multiple terms/concepts in single annotations
- Example: protein localized to "plasma membrane of T-cells"

### Evidence Code Framework

**Three Major Categories:**

1. **Experimental Evidence (6 codes):**
   - **EXP**: General experimental evidence
   - **IDA**: Inferred from Direct Assay
   - **IPI**: Inferred from Physical Interaction
   - **IMP**: Inferred from Mutant Phenotype
   - **IGI**: Inferred from Genetic Interaction
   - **IEP**: Inferred from Expression Pattern

2. **Curated Non-Experimental (14 codes):**
   - **ISS family**: Sequence/structural similarity (ISS, ISO, ISA, ISM)
   - **Phylogenetic**: IBA, IBD, IKR, IRD
   - **Literature**: TAS (traceable), NAS (non-traceable)
   - **Curator inference**: IC, RCA
   - **Context-based**: IGC
   - **No data**: ND

3. **Electronic/Automatic (1 code):**
   - **IEA**: Inferred from Electronic Annotation (most abundant)

### Quality and Bias Considerations

**Evidence Quality Hierarchy:**
- **Experimental > Curated non-experimental > Electronic**
- But this hierarchy isn't empirically validated
- Electronic annotations often target high-level terms (lower information content)
- Experimental evidence can be over-interpreted or contain inaccuracies

**Annotation Redundancy Issues:**
- UniProt contains ~70,000 human protein entries for ~20,000 genes
- **Gene-centric reference proteomes** provide canonical entries
- Multiple annotations to same term with different evidence codes allowed

### Practical Applications

**Common Uses:**
- **Functional profiling**: Comparing gene sets for enriched processes
- **Function prediction**: Transferring annotations based on similarity
- **Database querying**: Finding genes with specific functions/locations
- **High-throughput analysis**: Interpreting expression/interaction data

**Tools and Resources:**
- **Browsers**: AmiGO, QuickGO
- **File formats**: GAF 2.1, GPAD
- **APIs and programmatic access**
- **Analysis tools** for enrichment, similarity, visualization

## Relevance to AI Gene Review Project

This chapter is **critical foundation reading** for our annotation curation work, providing practical knowledge essential for effective GO annotation review:

### 1. **Evidence Code Evaluation Framework**
Understanding evidence codes is fundamental to our curation decisions:
- **Experimental evidence (EXP, IDA, IMP, etc.)** should generally support **ACCEPT** decisions
- **Electronic annotations (IEA)** require skeptical evaluation - prime candidates for **MARK_AS_OVER_ANNOTATED**
- **Curator inference (IC)** annotations need careful assessment of the curator's reasoning
- **Literature-based codes (TAS, NAS)** require verification of source quality

### 2. **Qualifier Awareness for Over-annotation Detection**
The chapter's emphasis on qualifiers directly supports over-annotation detection:
- Missing **"contributes_to"** qualifier for complex components may indicate over-annotation
- Inappropriately broad annotations without **"NOT"** qualifiers where negative evidence exists
- **Over-generalized cellular component** annotations without appropriate context

### 3. **GAF File Structure Understanding**
Knowledge of GAF format enables:
- Proper parsing of existing annotations from GOA files
- Understanding annotation extensions and their impact on specificity
- Recognizing when annotations lack critical contextual information

### 4. **Annotation Uniqueness and Redundancy**
The chapter's discussion of annotation redundancy informs our approach:
- **Gene-centric analysis** focus aligns with our project goals
- Understanding why the same gene may have multiple annotations with different evidence codes
- Recognizing when multiple annotations represent genuine functional diversity vs. redundancy

### 5. **Dynamic Nature of GO**
Understanding GO's evolution is crucial for:
- **Version-aware curation**: Ensuring we're working with current terms
- **Obsolete term recognition**: Identifying outdated annotations that need updating
- **Relationship change impacts**: Understanding how ontology updates affect annotation validity

### 6. **Quality Assessment Criteria**
The chapter's nuanced view of evidence quality supports our sophisticated curation approach:
- **Not just experimental > electronic**: Recognizing that experimental evidence can be over-interpreted
- **Context-dependent evaluation**: Understanding that high-level electronic annotations may be appropriate
- **Training set reliability**: Using high-quality experimental annotations as gold standards

### 7. **Over-annotation Identification Strategies**
Several insights directly support over-annotation detection:
- **Electronic annotation bias** toward high-level terms suggests need for specificity assessment
- **Complex component annotations** without "contributes_to" qualifiers
- **Cellular component annotations** based on trafficking observations rather than functional localization
- **Protein binding annotations** representing experimental artifacts rather than biological function

### 8. **Evidence Integration Approach**
The chapter's multi-evidence framework supports our integrative curation methodology:
- **Combining experimental and computational evidence** for robust assessment
- **Cross-referencing annotation extensions** with biological process context
- **Using phylogenetic evidence codes** (IBA, IBD) to assess evolutionary conservation

This primer provides the practical GO expertise necessary to make informed, evidence-based curation decisions that effectively distinguish genuine gene functions from experimental artifacts and over-annotations.