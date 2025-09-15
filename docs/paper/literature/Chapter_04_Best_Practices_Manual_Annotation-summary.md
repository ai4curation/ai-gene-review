# Chapter 4: Best Practices in Manual Annotation with the Gene Ontology - Summary

**Authors:** Sylvain Poux and Pascale Gaudet

## Summary

This chapter provides comprehensive guidelines for expert GO annotation curation, emphasizing the complex process of translating experimental findings into accurate GO terms. The authors stress that biocuration requires sophisticated interpretation skills, as the same experimental results can lead to different annotations depending on biological context and prior knowledge.

### Key Principles of Knowledge Inference

**Scientific Method Foundation:**
- Annotation process mirrors scientific method: hypothesis → experiment → results → inference
- Same experimental setup can yield different conclusions depending on hypothesis tested
- Experimental conditions, controls, and current knowledge state affect interpretation
- Low-resolution experiments may be refuted by better techniques

**GO Framework Structure:**
- **Molecular Function (MF)**: Biochemical/molecular activity of gene product
- **Biological Process (BP)**: Wider biological module where MF acts (most challenging aspect)
- **Cellular Component (CC)**: Specific cellular localization where gene product is active
- Two classification axes: subtypes (is_a) vs. sub-processes (part_of)

### Best Practices for High-Quality Curation

**1. Contextual Interpretation (The GO Inference Process)**
The chapter emphasizes that **the same experimental readout requires different annotations based on biological context**:

- **DDFB nuclease** → DNA fragmentation assay → "apoptotic DNA fragmentation" (direct nuclease activity)
- **CYCS cytochrome C** → DNA fragmentation assay → "caspase activation" (upstream role, not direct fragmentation)
- **FOXL2 transcription factor** → DNA fragmentation assay → "positive regulation of apoptotic process" (regulatory role)

**2. Publication Selection and Prioritization:**
- **Careful prioritization**: Focus on papers providing most added value
- **Recent publications**: Help resolve conflicts and detect experimental discrepancies
- **Multiple paper confirmation**: Seek confirmation for unusual findings
- **Avoid non-replicated data**: Don't systematically annotate accessory findings

**3. Granularity Control:**
- **Evidence-dictated specificity**: Annotation depth must match available evidence
- **ADCK3 example**: Contains protein kinase domain but unclear substrate → use general "kinase activity" rather than "protein kinase activity"
- **Avoid over-interpretation**: Don't infer more specific functions than data supports

**4. Avoiding Over-Interpretation:**

**Biological Relevance:**
- **Experimental vs. biological context**: Distinguish between experimental setup and physiological relevance
- **E3 ubiquitin ligase example**: In vitro autoubiquitination assay doesn't prove in vivo autoubiquitination
- **Cell type specificity**: Only annotate when data indicates physiological importance

**Downstream Effects:**
- **Indirect effects problem**: Gene products with housekeeping functions have many indirect effects
- **Histone modification cascade**: RNF20 directly ubiquitinates H2B → indirectly promotes H3 methylation
- **Annotation principle**: Only annotate primary enzyme function, not downstream modifications

**Phenotype Interpretation:**
- **Knockout limitations**: Knockout experiments show requirement, not participation
- **Housekeeping gene problem**: Knockouts can affect all cellular processes
- **Over-interpretation risk**: Don't annotate to every affected process

**5. Main vs. Secondary Functions:**
- **CYP4F2 enzyme example**: Main function is vitamin K catabolism, but also acts on other substrates
- **Current limitation**: GO doesn't distinguish main from secondary functions explicitly
- **Annotation extensions**: Help clarify main roles for specific reactions

**6. Evolving Knowledge Management:**
- **NOTUM protein example**: Initially thought to cleave GPI anchors → actually deacylates WNT proteins
- **Mechanisms for updates**: New terms added, NOT qualifier for disproven functions
- **Protein2GO dispute mechanism**: Allows challenging questionable annotations

### Quality Control Approaches

**1. Automated Validation:**
- **GO annotation rulebase**: Validates syntactic and biological content
- **Taxon checks**: Ensure species-appropriate annotations
- **Evidence type validation**: Correct object types with different evidence codes

**2. Consistency Exercises:**
- **Inter-annotator reliability**: Multiple curators annotate same papers
- **Guideline updates**: Discrepancies lead to clarified guidelines
- **Cross-group coordination**: >20 contributing groups need consistent interpretation

**3. PAINT System (Reference Genome Project):**
- **Phylogenetic annotation**: Propagates high-confidence data across gene families
- **Inconsistency detection**: Makes family-wide annotation patterns visible
- **Quality improvement**: Identifies systematic biases in ontology or guidelines

### Annotation Guidelines Summary

**Publication Selection:**
- Only annotate papers providing most added value
- Read recent publications to resolve conflicts
- Check annotation consistency with related proteins
- Look for confirmation from multiple papers

**Experimental Interpretation:**
- Avoid annotations not directly implicating the protein
- Annotate the conclusion, not just the results
- Be especially careful with mutant phenotypes
- Distinguish experimental context from biological relevance

**Knowledge Evolution:**
- Remove obsolete annotations when findings are invalidated
- Use challenge mechanisms for questionable annotations
- Stay current with recent publications in the field

## Relevance to AI Gene Review Project

This chapter is **essential reading** for our annotation curation work, providing the theoretical foundation and practical guidelines for expert-level GO annotation review:

### 1. **Contextual Interpretation Framework**
The chapter's core message - that **identical experimental results require different annotations based on biological context** - is fundamental to avoiding over-annotation:
- **Direct vs. indirect effects**: Essential for distinguishing core functions from downstream consequences
- **Mechanistic understanding**: Required to assess whether annotations represent genuine gene functions
- **Biological relevance**: Critical for evaluating whether experimental conditions reflect physiological roles

### 2. **Over-Interpretation Recognition**
Multiple examples directly applicable to over-annotation detection:
- **Downstream effects**: Chromatin modifiers, signaling proteins with pleiotropic effects
- **Experimental artifacts**: In vitro autoubiquitination not proving in vivo function
- **Phenotypic over-interpretation**: Knockout effects don't equal participation
- **Housekeeping gene problem**: Indirect effects on all cellular processes

### 3. **Evidence Quality Assessment**
Guidelines for evaluating annotation appropriateness:
- **Publication selection criteria**: Focus on high-value, confirmed findings
- **Experimental directness**: Prefer direct over indirect evidence
- **Biological context**: Distinguish experimental setup from physiological relevance
- **Granularity control**: Match annotation specificity to evidence strength

### 4. **Systematic Biases in Annotation**
The chapter identifies common sources of over-annotation:
- **Phenotypic over-interpretation**: Particularly relevant for developmental genes
- **Downstream effect propagation**: Especially problematic for regulatory proteins
- **Experimental condition confusion**: Cell culture vs. physiological context
- **Secondary function over-emphasis**: Treating all activities as equally important

### 5. **Quality Control Integration**
Approaches we can adapt for our curation workflow:
- **Consistency checking**: Compare annotations across gene families
- **Literature prioritization**: Focus on high-confidence, recent publications
- **Contextual evaluation**: Assess biological relevance of experimental conditions
- **Systematic bias detection**: Identify patterns suggesting over-annotation

### 6. **Evolving Knowledge Framework**
Understanding how biological knowledge changes informs our curation approach:
- **Literature currency**: Importance of considering recent contradictory findings
- **Mechanistic refinement**: How improved techniques invalidate previous conclusions
- **Annotation updating**: Principles for revising outdated functional assignments

### 7. **Multi-Evidence Integration**
The chapter's examples demonstrate sophisticated evidence integration:
- **Cross-referencing related proteins**: Consistency checking within biological processes
- **Mechanistic coherence**: Ensuring annotations reflect known biochemical pathways
- **Evidence triangulation**: Using multiple experimental approaches to validate functions

This chapter provides the conceptual foundation for making principled curation decisions that distinguish genuine gene functions from experimental artifacts, indirect effects, and over-interpreted results - exactly the sophisticated reasoning required for effective over-annotation detection and remediation.