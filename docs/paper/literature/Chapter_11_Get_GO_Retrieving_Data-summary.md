# Chapter 11: Get GO! Retrieving GO Data Using AmiGO, QuickGO, API, Files, and Tools - Summary

**Authors:** Monica Munoz-Torres and Seth Carbon

## Summary

This chapter provides a comprehensive practical guide to accessing and utilizing Gene Ontology Consortium (GOC) resources through various interfaces and methods. The authors systematically cover web-based interfaces, file formats, programmatic access methods, and tools for retrieving, manipulating, and analyzing GO data, serving as both a tutorial and reference for researchers working with GO resources.

### Web Interfaces for GO Data Access

**Primary Web Browsers:**

1. **AmiGO (http://amigo.geneontology.org)**:
   - **Official GOC browser**: Open-source tool for querying, browsing, and visualizing GO data
   - **Key features**: Basic searching, custom dataset downloads, "wizard" interface for common questions
   - **Recent improvements**: Enhanced speed, multiple search modes, annotation extensions display, protein forms visualization
   - **Data sources**: MODs (model organism databases), UniProtKB, and other consortium members
   - **Funding**: NHGRI-NIH supported, official channel for GO data dissemination

2. **QuickGO (http://www.ebi.ac.uk/QuickGO)**:
   - **EMBL-EBI developed**: Web-based tool for browsing GO and annotations
   - **Advanced features**: Extensive search/filter capabilities, integrated subset/slim interface, historical term views
   - **Data consumption**: Broad-ranging web services, cart functionality for persistence
   - **Management**: EMBL-EBI funded and managed, team members also participate in GOC

**Third-Party Browsers:**
- **OntoBee**: Semantic web community focused, linked data platform
- **EMBL-EBI OLS**: Ontology Lookup Service for general ontology browsing
- **OLSVis**: Visualization-oriented interface
- **BioPortal**: General ontology repository
- **Limitation**: None currently provide access to GO annotations

**Enrichment Analysis Integration:**
- **PANTHER Classification System**: Direct connection from GO website for term enrichment analysis
- **Supported features**: Overrepresentation/underrepresentation analysis, up-to-date GO annotations
- **Gene ID support**: Comprehensive list available from PANTHER website

### GO File Formats and Data Structure

**Ontology File Editions (increasing complexity):**

1. **go-basic**:
   - **Filtered version**: Supports annotation propagation up the graph
   - **Relations included**: is_a, part_of, regulates, negatively_regulates, positively_regulates
   - **Limitation**: Excludes cross-hierarchy relationships
   - **Format**: OBO only
   - **Use case**: Legacy tool compatibility

2. **go**:
   - **Core edition**: Additional relationship types spanning GO hierarchies
   - **Cross-hierarchy relations**: has_part, occurs_in connecting disjoint hierarchies
   - **Formats**: OBO and OWL-RDF/XML
   - **Enhanced connectivity**: Links otherwise separate hierarchical structures

3. **go-plus**:
   - **Most expressive edition**: Maximum relationship complexity and external ontology connections
   - **External integrations**: ChEBI (chemical entities), Uberon (anatomy), Plant Ontology (PO)
   - **Advanced features**: Import modules, cross-ontology queries, biological constraint rules
   - **Validation capabilities**: Spatial exclusivity constraints, automated consistency checking
   - **Format**: OWL-RDF/XML only

**Technical Implementation:**
- **Official language**: Web Ontology Language (OWL), W3C standard
- **Scale**: ~41,000 GO terms + 10,000 imported classes, ~27 million associations, ~470,000 species
- **Axiomatization**: Complete logical definitions (OWL axioms) for systematic reasoning
- **Tool support**: Protégé editor, Java OWL API, OWLTools framework

**Association File Formats:**

1. **GAF (Gene Association Files)**:
   - **Primary format**: Tab-delimited plain text, version 2.1 current
   - **Structure**: One line per gene product-GO term association
   - **Information included**: Evidence codes, references, qualifier information
   - **Standardization**: Consortium-wide submission format

2. **GPAD/GPI Files**:
   - **Normalized version**: Separated gene product information from associations
   - **Future prominence**: Expected to replace GAF format
   - **Advantages**: Cleaner data structure, reduced redundancy

### Programmatic Access and Tool Development

**Java/JVM Ecosystem:**
- **OWLTools**: Primary library for GO data manipulation and analysis
  - **Core operations**: Graph walking, closures, OBO-specific field access
  - **Advanced features**: Ontology reasoning, validation, taxon checks, link prediction
- **OWL API**: Standard Java library for OWL ontology processing
- **Standard reasoners**: Full compatibility with OWL tool stack

**JavaScript Development:**
- **AmiGO APIs**: Client and server-side JavaScript interfaces
- **Widget system**: Reusable components for GO data integration
- **Core components**: Manager and response interfaces for external site integration
- **External linking**: Methods for producing incoming searches and relevantinformation linking

**Database Access:**
- **GOOSE (GO Online SQL/Solr Environment)**: Legacy SQL database access
- **MySQL builds**: Regular conversions for legacy application support
- **Remote querying**: Available for applications requiring SQL interface
- **Schema information**: Comprehensive documentation for database structure

### Ontology Subsets and Customization

**GO Slims/Subsets:**
- **Purpose**: Cut-down versions with reduced term numbers for broad classification
- **Use cases**: Genome annotation summaries, microarray analysis, cDNA collection classification
- **Types**: Species-specific subsets, generic "useful" term collections
- **Benefits**: Overview without fine-grained detail complexity

**Community Contribution Mechanisms:**
- **TermGenie**: Web-based tool for requesting new GO classes with automated review
- **GitHub tracker**: Free-text ontology update and request submissions
- **AmiGO browser**: Term existence searching and validation
- **Feedback integration**: Systematic incorporation of user suggestions and corrections

### Additional Resources and Support

**Cross-System Mappings:**
- **Available mappings**: Enzyme Commission numbers, KEGG pathways
- **Limitations**: Neither complete nor exact, require cautious usage
- **Documentation**: Complete listing available on GO website

**Help and Support Infrastructure:**
- **GO Helpdesk**: User query addressing for data, software, and analysis issues
- **Contact methods**: Site forms with automatic internal tracking
- **Response system**: Queries directed to appropriate consortium personnel
- **Issue tracking**: Systematic responsiveness assurance

## Relevance to AI Gene Review Project

This chapter provides **essential practical knowledge** for effectively accessing and utilizing GO resources in our annotation curation workflow:

### 1. **Data Source Understanding and Quality Assessment**
The chapter's coverage of different GO browsers and their origins directly informs our data evaluation:
- **AmiGO vs. QuickGO differences**: Understanding that both use same datasets but with different implementations helps assess annotation consistency
- **Official vs. third-party sources**: Prioritizing GOC-official resources (AmiGO) for authoritative annotation information
- **Data provenance tracking**: Recognizing MOD and UniProtKB contribution patterns for source reliability assessment

### 2. **File Format Expertise for Systematic Analysis**
Detailed understanding of GO file formats enables sophisticated annotation analysis:
- **GAF format mastery**: Essential for parsing and analyzing existing annotations in our gene review workflow
- **GPAD/GPI transition awareness**: Preparing for future format changes and understanding normalization benefits
- **Ontology edition selection**: Choosing appropriate complexity level (go-basic vs. go vs. go-plus) for specific analysis needs

### 3. **Programmatic Access for Large-Scale Curation**
The chapter's programming interface documentation supports scalable annotation processing:
- **OWLTools integration**: Leveraging advanced reasoning capabilities for annotation validation and consistency checking
- **Batch processing capabilities**: Utilizing file-based access for systematic annotation review across multiple genes
- **API utilization**: Implementing automated quality checks and cross-referencing in our curation pipeline

### 4. **Cross-Hierarchy Relationship Understanding**
Knowledge of ontology structure complexity informs curation decisions:
- **go-basic limitations**: Understanding when cross-hierarchy relationships are excluded affects annotation interpretation
- **go-plus advantages**: Recognizing enhanced relationship types helps identify more sophisticated functional connections
- **External ontology integration**: Leveraging ChEBI, Uberon, and PO connections for comprehensive functional understanding

### 5. **Quality Control Through Multiple Access Methods**
Utilizing different interfaces provides validation opportunities:
- **Cross-browser verification**: Checking annotations across AmiGO and QuickGO for consistency
- **Historical tracking**: Using QuickGO's historical views to understand annotation evolution and stability
- **Search methodology diversity**: Employing different search approaches to identify potential annotation gaps or inconsistencies

### 6. **Subset and Slim Analysis for Over-Annotation Detection**
Understanding GO slims supports systematic annotation evaluation:
- **Broad classification perspective**: Using slims to identify genes with excessive fine-grained annotations
- **Summary-level consistency**: Checking whether detailed annotations align with expected broad functional categories
- **Species-specific validation**: Leveraging organism-specific subsets for contextual annotation appropriateness

### 7. **Community Contribution and Feedback Integration**
The chapter's coverage of contribution mechanisms supports our project's broader impact:
- **Systematic improvement**: Using GitHub tracker and TermGenie to contribute annotation quality feedback
- **Error reporting**: Implementing systematic feedback mechanisms for identified over-annotations or inconsistencies
- **Community engagement**: Connecting our findings with broader GO improvement efforts

### 8. **Tool Development for Specialized Needs**
Programming interface documentation enables custom tool development:
- **Automated validation tools**: Creating specialized scripts for systematic over-annotation detection
- **Integration pipelines**: Building workflows that combine multiple data sources and validation approaches
- **Quality metrics development**: Implementing quantitative measures for annotation appropriateness assessment

### 9. **Historical and Temporal Analysis Capabilities**
Understanding data evolution features supports longitudinal analysis:
- **Annotation stability tracking**: Using historical views to assess annotation persistence and reliability
- **Change pattern analysis**: Identifying systematic trends in annotation modifications over time
- **Version control awareness**: Understanding how ontology and annotation changes affect our curation decisions

This comprehensive understanding of GO data access and manipulation is crucial for implementing sophisticated, scalable approaches to annotation curation that can systematically identify over-annotations while leveraging the full power of GO resources for informed decision-making.