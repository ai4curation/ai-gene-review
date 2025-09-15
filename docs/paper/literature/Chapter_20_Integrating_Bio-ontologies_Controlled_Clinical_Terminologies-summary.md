# Chapter 20: Integrating Bio-ontologies and Controlled Clinical Terminologies: From Base Pairs to Bedside Phenotypes - Summary

**Author:** Spiros C. Denaxas

## Summary

This chapter explores the integration of biological ontologies with controlled clinical terminologies, demonstrating how Electronic Health Records (EHR) can bridge genomic variation and clinical phenotypes through structured data capture and standardized vocabularies. The author provides a comprehensive overview of major clinical terminologies, their applications and challenges, and illustrates integration pathways through a detailed breast cancer case study that traces information flow from genetic variants to bedside phenotypes.

### The Clinical Data Challenge

**EHR Complexity:**
- **Data diversity**: Electronic health records contain structured (clinical terminologies), semi-structured (laboratory results), and unstructured (free text) data
- **Multidisciplinary nature**: Healthcare involves diverse specialties requiring integrated data across primary, secondary, and tertiary care settings
- **Scale and growth**: Vast amounts of EHR data generated but lacking common structure for integration
- **Integration imperative**: Need for standardized approaches to facilitate care across settings and enable research applications

**Transformational Potential:**
- **Personalized medicine**: EHR data considered transformational force for measuring and improving clinical care quality
- **Research acceleration**: Potential to accelerate biomedical research across all translation stages
- **Data-driven approach**: Movement toward evidence-based, personalized medical practice

### Controlled Clinical Terminologies

**Core Purpose:**
Like Gene Ontology for biological concepts, clinical terminologies provide systematic capture, curation, and description of healthcare-related concepts including:
- **Clinical entities**: Diagnoses, symptoms, anatomical locations, prescribed medications, medical tests
- **Procedural information**: Surgical procedures, interventions, investigations
- **Measurement data**: Laboratory results, clinical observations
- **Integration function**: Essential tools for clinical data integration across disparate sources

**Major Clinical Terminologies:**

**1. SNOMED-CT (Systematized Nomenclature of Medicine-Clinical Terms):**
- **Scale**: Over 300,000 healthcare-related concepts
- **Structure**: Four primary components (concepts, descriptions, relationships, reference sets)
- **Hierarchical organization**: Acyclic hierarchy with multiple inheritance capability
- **Post-coordination**: Compositional syntax allowing combination of terms for complex concepts
- **Implementation**: Variable international adoption; UK NHS designated as standard by 2020

**2. ICD-10 (International Classification of Diseases):**
- **Scope**: Diseases, signs, symptoms, abnormal findings, social circumstances, external causes
- **Structure**: Alphanumeric codes up to six characters long with major categorical organization
- **Usage**: Most widely used statistical classification system globally
- **Applications**: Clinical coding for research, official statistics, medical billing, resource planning
- **Variants**: Country-specific extensions (e.g., ICD-9-CM in USA)

**3. Procedural Classifications:**
- **CPT (Current Procedural Terminology)**: American Medical Association maintained, US-focused
- **OPCS-4**: UK National Health Service classification for interventions and procedures
- **Integration**: Combined with diagnosis codes for medical billing and resource allocation

**4. Laboratory Standards:**
- **LOINC (Logical Observation Identifiers Names and Codes)**: Regenstrief Institute maintained
- **Structure**: Six-part format (component, property, time, system, scale, method)
- **Function**: Facilitates laboratory data exchange between providers, laboratories, public health agencies

**5. Medication Terminology:**
- **RxNorm**: US Library of Medicine developed for clinical drug information
- **Content**: Normalized names, active ingredients, strengths, forms, branded versions
- **Applications**: Health records, provider communication, medication decision support

### Applications and Challenges

**Opportunities:**
- **Translational research**: Larger sample sizes at higher clinical resolution through linked EHR data
- **Phenotyping**: Accurate extraction of disease status from EHR data for research cohorts
- **Clinical studies**: Cost-effective alternative to traditional investigator-led studies
- **Pragmatic trials**: Real-world evidence generation through routine clinical data

**Integration Challenges:**
- **Terminology mismatch**: Different clinical settings use different terminologies (SNOMED-CT vs. ICD-10)
- **Granularity differences**: Information recorded at varying levels of detail across sources
- **Mapping complexities**: Not all terms have direct one-to-one mappings between systems
- **Resolution requirements**: Manual rule creation often needed for complex integration scenarios

**Semantic Mapping Solutions:**
- **UMLS (Unified Medical Language System)**: Provides relationship mapping between terminologies
- **Cross-referencing**: Facilitates translation and integration across different clinical vocabularies
- **Limitation acknowledgment**: Information loss possible due to insufficient resolution or mapping conflicts

### Biological-Clinical Data Integration

**Genotype-Phenotype Challenge:**
- **Complex associations**: Even Mendelian diseases show complex genotype-phenotype relationships
- **Interpretation shift**: Focus moving from sequence generation to efficient interpretation
- **Perspective differences**: Clinical vs. molecular scientist viewpoints require different data organization
- **Data incompatibility**: Phenotypic and molecular properties recorded in different, often incompatible formats

**Integration Solutions:**

**Human Phenotype Ontology (HPO):**
- **Structure**: Three independent sub-ontologies covering phenotypic abnormalities, inheritance modes, onset/clinical course
- **Focus**: Phenotypic abnormalities rather than diseases themselves
- **Organization**: "Is_a" relationships with multiple parent term capability
- **Qualitative emphasis**: Descriptions of excess/reduction rather than quantitative measurements

**Cross-System Integration:**
- **UMLS mapping**: HPO terms reference Unified Medical Language System for clinical terminology mapping
- **External linkages**: Connections to OMIM, DECIPHER, Orphanet databases
- **Evidence coding**: Analogous to GO evidence codes for annotation quality tracking
- **Metadata support**: Onset, frequency, and modifier effect specifications

### Case Study: Breast Cancer Integration Pathway

**Multi-Level Data Flow:**
The chapter demonstrates integration through a comprehensive breast cancer example tracing:
1. **Genomic variation** → 2. **Genotype** → 3. **Transcripts** → 4. **Phenotype** → 5. **Clinical phenotype**

**Resource Integration at Each Level:**

**Genomic Level:**
- **dbSNP**: SNP rs144848 in BRCA2 gene with cancer risk association
- **Location data**: Chromosomal position, source assays, population diversity
- **Risk assessment**: Cumulatively significant increased breast cancer risk

**Genotype Level:**
- **OMIM**: Breast Cancer, Familial phenotype entity (#114480) with BRCA2 gene entry
- **Cross-references**: Links to Entrez Gene ID 675, Ensembl ENSG00000139618
- **Gene family**: Fanconi anemia complementation group (FANC) classification

**Transcript Level:**
- **UniProt**: BRCA2_HUMAN (P51587) protein information
- **GO annotation**: Double-strand break repair, DNA repair, cytokinesis, protease binding
- **Functional context**: Researchers can identify related gene products sharing pathways/functions

**Phenotype Level:**
- **HPO**: Breast carcinoma term (HP:0003002) with hierarchical relationships
- **UMLS integration**: Malignant Neoplasm of Breast (UMLS:C0006142) concept
- **Clinical mapping**: ICD-10 C50, SNOMED-CT 254837009 terminology connections

**Clinical Phenotype Level:**
- **Multisystem storage**: Pathology, radiology, surgery, medical oncology, radiotherapy systems
- **Diagnostic procedures**: Mammograms, ultrasounds, MRI, biopsy with PACS system storage
- **Treatment documentation**: Pharmacy information systems for therapeutic interventions

## Relevance to AI Gene Review Project

This chapter provides **crucial insights** for integrating clinical and biological annotation systems, directly supporting our gene curation work through systematic approaches to evidence validation and multi-resource integration:

### 1. **Multi-Terminology Validation Framework**
The chapter's comprehensive terminology survey supports robust evidence evaluation:
- **Cross-system verification**: Annotations supported across multiple terminologies (GO, HPO, SNOMED-CT, ICD-10) provide stronger evidence than single-system support
- **Clinical correlation**: Genes with GO annotations should show consistent representation in clinical terminologies when medically relevant
- **Integration consistency**: Discrepancies between biological and clinical terminology representations may indicate over-annotation or under-annotation issues

### 2. **Evidence Quality Stratification Through Clinical Context**
Understanding clinical terminology integration enables sophisticated evidence assessment:
- **Clinical relevance validation**: GO annotations should align with clinical phenotype representations when medically applicable
- **Disease association verification**: HPO connections provide independent validation of GO biological process annotations
- **Therapeutic context**: Drug terminology (RxNorm) connections can validate GO molecular function annotations for therapeutic targets

### 3. **Phenotype-Genotype Consistency Evaluation**
The chapter's integration approach supports systematic annotation coherence assessment:
- **HPO-GO alignment**: Phenotypic abnormalities described in HPO should be consistent with GO biological process annotations
- **Clinical manifestation validation**: GO annotations should be compatible with known clinical presentations and disease associations
- **Multi-level consistency**: Annotations should maintain coherence across genomic variation, gene function, and clinical phenotype levels

### 4. **Over-Annotation Detection Through Clinical Disconnects**
Integration patterns help identify inappropriate functional annotations:
- **Clinical relevance gaps**: GO annotations lacking corresponding clinical terminology representations may indicate over-interpretation
- **Phenotype mismatch**: Biological functions not reflected in clinical phenotype databases may suggest over-annotation
- **Therapeutic disconnect**: Molecular functions without corresponding drug targets or clinical interventions may be over-interpreted

### 5. **Systematic Bias Recognition Across Domains**
Understanding clinical vs. research perspectives helps identify annotation biases:
- **Perspective-specific emphasis**: Clinical terminologies focus on diagnostically/therapeutically relevant functions vs. research emphasis on mechanistic detail
- **Disease-centric bias**: Clinical systems emphasize pathological states, potentially missing normal physiological functions
- **Application-driven focus**: Medical billing and clinical care priorities may not align with comprehensive functional annotation

### 6. **Evidence Integration Across Data Types**
The chapter's multi-resource approach enables comprehensive evidence synthesis:
- **Literature-clinical alignment**: Published functional studies should align with clinical observations when medically relevant
- **Genetic association validation**: GO annotations should be consistent with known disease-gene associations in clinical databases
- **Population-level verification**: Clinical terminology frequency patterns can validate GO annotation prevalence expectations

### 7. **Quality Control Through Integration Patterns**
Multi-system integration provides quality assessment opportunities:
- **Annotation completeness**: Genes with extensive GO annotations should show corresponding representation in relevant clinical terminologies
- **Functional coherence**: GO molecular function annotations should align with clinical procedure terminologies when therapeutically relevant
- **Systematic gaps**: Missing connections between biological and clinical terminologies may indicate curation opportunities

### 8. **Translation-Ready Annotation Assessment**
The chapter's translational focus supports clinically-relevant curation:
- **Translational potential**: GO annotations should provide foundation for clinical application when medically relevant
- **Drug development relevance**: Molecular function annotations should align with pharmaceutical terminology when appropriate
- **Diagnostic utility**: GO annotations should support clinical phenotyping when diagnostically relevant

### 9. **Precision Medicine Integration**
Understanding clinical data integration supports precision medicine applications:
- **Personalized relevance**: GO annotations should contribute to individualized clinical interpretation
- **Biomarker potential**: Molecular function annotations should align with clinical measurement terminologies
- **Therapeutic targeting**: GO annotations should provide foundation for precision therapeutic approaches

### 10. **Educational and Training Applications**
The chapter's integration examples provide training frameworks:
- **Multi-domain literacy**: Understanding both biological and clinical terminology systems
- **Integration competency**: Skills in cross-system validation and evidence synthesis
- **Translation awareness**: Understanding how biological annotations relate to clinical applications

### 11. **Automated Integration Validation**
The chapter's systematic approach enables computational quality control:
- **Cross-system mapping**: Automated validation of GO annotations against clinical terminology representations
- **Integration consistency**: Computational checks for coherence across biological and clinical annotation systems
- **Gap identification**: Systematic detection of missing connections between related terminologies

This comprehensive understanding of clinical-biological integration provides essential foundation for implementing sophisticated, multi-domain approaches to annotation curation that can systematically validate GO annotations against clinical reality, ensuring functional annotations maintain both biological accuracy and clinical relevance while identifying over-annotations that lack corresponding clinical support or therapeutic relevance.