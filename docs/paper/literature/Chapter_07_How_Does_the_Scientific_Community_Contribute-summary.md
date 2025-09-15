# Chapter 7: How Does the Scientific Community Contribute to Gene Ontology? - Summary

**Author:** Ruth C. Lovering

## Summary

This chapter examines the various approaches and initiatives used to engage the scientific community in contributing to GO development and annotation. Lovering provides a comprehensive review of both successful and failed community engagement strategies, offering practical insights into the motivations, challenges, and opportunities for researcher participation in GO curation activities.

### Key Community Engagement Models

**Lincoln Stein's Four Organizational Models + "The School":**

1. **The Factory**: High degree of automation (current computational pipelines)
2. **The Museum**: Expert curators (traditional model organism databases)
3. **The Cottage Industry**: Individual scientists working from laboratories
4. **The Party/Jamboree**: Short intensive annotation workshops
5. **The School**: Bioinformatics training programs incorporating annotation activities

### Ontology Development Through Expert Consultation

**Successful Domain-Specific Expansions:**
- **Heart Development**: 1½ day meeting with four experts expanded terms from 12 to >280
  - Created highly specific terms like "secondary heart field specification" (GO:0003139)
  - Generated "canonical Wnt signaling in cardiac neural crest cell differentiation" (GO:0061310)
- **Other Notable Projects**: Immune system, kidney development, muscle processes, cell cycle, transcription
- **Key Success Factor**: Detailed email exchanges before and after meetings with domain experts

### Community Annotation Approaches

**1. Educational/Training Models:**

**CACAO (Community Assessment of Community Annotation with Ontologies):**
- **Competitive peer review system** at Texas A&M University
- **Gamification approach**: Students earn points for annotations, can lose points for errors
- **Professional curation oversight**: Expert curators review all submissions
- **Impressive results**: 3700 annotations submitted to GO database, >2500 proteins annotated, >700 students trained
- **Sustained engagement**: 3-month competition period reinforces learning

**UCL Literature Review Projects:**
- **MSc student projects**: Four completed projects on autism, heart development, folic acid metabolism, hereditary hemochromatosis
- **Output**: >1000 annotations created
- **Limitation**: Lacks domain expertise from active researchers

**UCL 2-Day Bioinformatics Course:**
- **Broad participation**: >200 scientists over 5 years
- **Low conversion rate**: Only ~50 annotations submitted per course, minimal continuation
- **Common problem**: Limited sustained engagement beyond workshop period

**2. Community-Specific Initiatives:**

**PomBase Success Story:**
- **Pilot project**: 80 fission yeast researchers submitted 226 GO annotations
- **Sustained success**: Regular ongoing community contributions
- **Tools**: CANTO curation tool enables direct community submission
- **Key factors**: Small community size, early visionary investment, high-quality curation support

**Norwegian Transcription Factor Project:**
- **Standardized guidelines**: Detailed annotation conventions created with GOC
- **Direct integration**: Literature-curated data imported with minimal quality checking
- **Scale**: Annotations for 400 proteins
- **Success factor**: Clear, comprehensive annotation guidelines

**SYSCILIA Consortium:**
- **Domain focus**: Ciliary components and processes
- **Collaborative approach**: Working directly with GOC on term development
- **Active contribution**: Currently submitting GO annotations

**3. Individual "Cottage Industry" Contributions:**

**Ralf Stephan Example:**
- **Remarkable dedication**: Single-handedly annotated 60% of *Mycobacterium tuberculosis* genome
- **Literature scope**: Reviewed >1000 papers
- **Quality output**: 7700 annotations for 2500 proteins
- **Validation**: UniProt-GOA team required minimal edits before incorporation

### Challenges and Barriers

**Workshop Limitations:**
- **Drosophila genome workshop**: First GO annotation workshop but limited sustained impact
- **Pathema workshops (2007)**: 150 attendees provided guidance rather than annotations
- **General pattern**: High initial interest, poor follow-through

**Engagement Obstacles:**
- **Time investment**: Annotation requires significant literature review and learning
- **Technical barriers**: Unfamiliar tools and submission processes
- **Lack of incentives**: Limited professional recognition for annotation contributions
- **Training overhead**: Providing quality feedback to novice annotators is labor-intensive

### Motivations for Community Participation

**Primary Motivations:**
- **Research area representation**: Ensuring specific domains are well-curated
- **Publication promotion**: Getting own research properly annotated in databases
- **Citation enhancement**: Improved database representation may increase paper citations
- **Competitive elements**: Peer competition as demonstrated by CACAO success

**Strategic Considerations:**
- **Funding allocation**: Argues for including GO annotation components in grants rather than purchasing proprietary tools
- **Developing country support**: Emphasis on improving freely available resources
- **Sustainable approach**: Community investment more sustainable than proprietary solutions

### Resources and Tools for Community Contribution

**Submission Pathways:**
- **Contact methods**: GOC webforms, direct email to relevant databases
- **CANTO tool**: PomBase's community curation tool available for any species
- **Protein2GO**: UniProt annotation tool with author notification system

**Useful Contributions:**
- **Key publication identification**: Suggesting important papers for curation
- **Annotation review**: Identifying missing, wrong, or controversial annotations
- **Ontology feedback**: Comments on term definitions and hierarchy structure
- **Domain expertise**: Guidance on specialized biological processes

**Quality Assurance:**
- **Professional oversight**: All community submissions reviewed by expert curators
- **Consistency maintenance**: Ensures adherence to GO annotation standards
- **Integration support**: Notifications provided when suggestions are incorporated

## Relevance to AI Gene Review Project

This chapter provides **essential insights** for understanding community engagement in functional annotation and its implications for our over-annotation detection work:

### 1. **Understanding Annotation Origins and Quality Variation**
The chapter reveals significant quality differences across annotation sources:
- **Student annotations**: Created for training purposes, may lack domain expertise
- **Competition-based annotations**: Higher engagement but variable expertise levels
- **Expert community contributions**: High quality but limited in scope
- **Workshop annotations**: Often superficial due to limited follow-through

This variability directly impacts our curation decisions, as annotations from different sources require different levels of scrutiny.

### 2. **Recognizing Systematic Biases in Community Annotations**
Several patterns emerge that could lead to over-annotation:
- **Training project bias**: Students may over-interpret limited evidence to complete assignments
- **Domain-specific focus**: Intensive projects in specific areas (heart development, transcription factors) may create annotation density imbalances
- **Competition incentives**: CACAO-style systems may encourage quantity over precision

### 3. **Quality Assessment Framework for Community Contributions**
The chapter highlights quality indicators relevant to our curation work:
- **Professional oversight**: Annotations reviewed by expert curators generally higher quality
- **Standardized guidelines**: Projects with detailed annotation standards (Norwegian transcription factors) produce more consistent results
- **Sustained engagement**: One-time workshops produce lower quality than ongoing community relationships

### 4. **Evidence Code Interpretation Context**
Understanding community contribution methods helps interpret evidence codes:
- **Traceable Author Statement (TAS)**: May reflect variable quality depending on submission pathway
- **Curator inference codes**: May incorporate community input of varying reliability
- **Training set contamination**: Some annotations may derive from educational exercises rather than research expertise

### 5. **Over-Annotation Pattern Recognition**
Several community engagement patterns could contribute to over-annotation:
- **Domain inflation**: Intensive focus on specific biological areas may lead to over-specific term creation
- **Educational over-interpretation**: Training contexts may encourage annotation of marginal evidence
- **Competitive annotation**: Point-based systems may incentivize annotation quantity over appropriateness

### 6. **Literature-Based Curation Priorities**
The chapter's discussion of publication selection provides guidance for our literature-based approach:
- **Expert identification**: Domain experts' publication recommendations likely high-quality
- **Community feedback**: Research community input on missing papers valuable for comprehensive coverage
- **Quality vs. quantity**: Ralf Stephan example shows intensive literature review by experts produces high-quality annotations

### 7. **Validation and Quality Control Insights**
Successful community programs emphasize quality control measures relevant to our approach:
- **Professional curation oversight**: Essential for maintaining annotation quality
- **Standardized criteria**: Clear annotation guidelines critical for consistency
- **Feedback mechanisms**: Author notification systems (Protein2GO) help identify annotation errors

### 8. **Sustainable Curation Models**
The chapter advocates for approaches aligned with our project goals:
- **Investment in free resources**: Supporting open annotation databases rather than proprietary tools
- **Expert involvement**: Engaging domain experts in annotation review and improvement
- **Quality over quantity**: Emphasis on thorough, expert-reviewed annotations rather than broad coverage

### 9. **Community Engagement for Over-Annotation Detection**
The chapter suggests strategies we could adopt:
- **Expert consultation**: Engaging research communities to identify problematic annotations in their domains
- **Feedback systems**: Mechanisms for researchers to report annotation issues
- **Educational impact**: Our curation work could serve as training examples for future community annotators

This understanding of community annotation processes is crucial for evaluating the origins and reliability of existing GO annotations, helping us make informed decisions about which annotations represent genuine expert consensus versus over-interpretation from less reliable sources.