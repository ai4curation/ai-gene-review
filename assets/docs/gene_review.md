
# gene_review


**metamodel version:** 1.7.0

**version:** None


Schema for gene curation Top level entity is a GeneReview, which is about a single gene (and its equivalent swiss-prot entry). It contains a high level summary of the gene, plus a review of all existing annotations. It also contains a list of core functions, which are GO-CAM-like annotons describing the core evolved functions of the gene.


### Classes

 * [AnnotationExtension](AnnotationExtension.md)
 * [ConditionOverlapAssessment](ConditionOverlapAssessment.md) - Assessment of overlap between rule conditions
 * [CoreFunction](CoreFunction.md) - A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the reviewed core annotations, brought together into a unified GO-CAM-like representation.
 * [EmbeddedRule](EmbeddedRule.md) - An embedded representation of an ARBA or UniRule for storage in YAML. Captures the essential structure: conditions (antecedent) and GO annotations (consequent).
 * [ExistingAnnotation](ExistingAnnotation.md) - An existing annotation from the GO database, plus a review of the annotation.
 * [Experiment](Experiment.md) - A suggested experiment to answer a question about the gene
 * [Finding](Finding.md) - A finding is a statement about a gene, which is supported by a reference. Similar to "comments" in uniprot
 * [GOSpecificityAssessment](GOSpecificityAssessment.md) - Assessment of GO term specificity
 * [GeneReview](GeneReview.md) - Complete review for a gene
 * [InterPro2GORedundancy](InterPro2GORedundancy.md) - Analysis of whether rule GO annotations are redundant with existing InterPro2GO mappings from the GO Consortium.
 * [LiteratureSupportAssessment](LiteratureSupportAssessment.md) - Assessment of literature support for the rule
 * [PairwiseOverlap](PairwiseOverlap.md) - Overlap statistics between two domain conditions (InterPro, FunFam, etc.) in the same condition set. Provides set difference metrics to measure uniqueness and redundancy.
 * [ParsimonyAssessment](ParsimonyAssessment.md) - Assessment of rule parsimony (simplicity vs complexity)
 * [ProposedOntologyTerm](ProposedOntologyTerm.md) - A proposed new ontology term that should exist but doesn't currently
 * [Question](Question.md) - A question to be answered about the gene
 * [RedundantAnnotation](RedundantAnnotation.md) - A GO annotation that is redundant with an existing InterPro2GO mapping
 * [Reference](Reference.md) - A reference is a published text  that describes a finding or a method. References might be formal publications (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review can be made by using the `file:` prefix.
 * [RelatedEntry](RelatedEntry.md) - A relationship from this entry to another entry in the rule. Categorized as PREDICTS (this → other), PREDICTED_BY (other → this), or EQUIV (bidirectional).
 * [Review](Review.md) - A review of an existing annotation.
 * [RuleCondition](RuleCondition.md) - A single condition in a rule antecedent
 * [RuleConditionSet](RuleConditionSet.md) - A set of conditions that must ALL be true (conjunction/AND). Multiple condition sets in a rule are OR-ed together (disjunction).
 * [RuleGOAnnotation](RuleGOAnnotation.md) - A GO annotation produced by the rule
 * [RuleReview](RuleReview.md) - A review of a UniProt annotation rule (ARBA or UniRule). Each review covers ONE rule and assesses its quality, literature support, and biological appropriateness.
 * [RuleReviewEntry](RuleReviewEntry.md) - An entity in the rule - either a domain/family condition or a GO term target. Each entry tracks its relationships (predictions, predicted-by, equivalence) to other entries.
 * [SupportingTextInReference](SupportingTextInReference.md) - A supporting text in a reference.
 * [TaxonomicScopeAssessment](TaxonomicScopeAssessment.md) - Assessment of taxonomic restriction appropriateness
 * [Term](Term.md) - A term in a specific ontology
 * [TermMapping](TermMapping.md) - A mapping between the proposed term and an equivalent term in another ontology

### Mixins


### Slots

 * [action](action.md) - Action to be taken
 * [additional_reference_ids](additional_reference_ids.md) - IDs of the references
 * [aliases](aliases.md)
 * [➞assessment](conditionOverlapAssessment__assessment.md) - Overlap assessment value
 * [➞notes](conditionOverlapAssessment__notes.md) - Notes on condition overlap - e.g., "IPR000001 and IPR000002 both represent the same structural domain" or "FunFam subsumes the InterPro entry"
 * [➞supported_by](conditionOverlapAssessment__supported_by.md) - Supporting text from literature for this assessment
 * [➞anatomical_locations](coreFunction__anatomical_locations.md)
 * [➞description](coreFunction__description.md) - Description of the core function
 * [➞directly_involved_in](coreFunction__directly_involved_in.md)
 * [➞in_complex](coreFunction__in_complex.md)
 * [➞locations](coreFunction__locations.md)
 * [➞molecular_function](coreFunction__molecular_function.md)
 * [➞substrates](coreFunction__substrates.md)
 * [➞supported_by](coreFunction__supported_by.md)
 * [core_functions](core_functions.md)
 * [description](description.md) - Description of the entity
 * [➞condition_sets](embeddedRule__condition_sets.md) - List of condition sets (OR-ed together). Each condition set is a conjunction (AND) of conditions. The rule fires if ANY condition set matches.
 * [➞created_date](embeddedRule__created_date.md) - Date the rule was created
 * [➞entries](embeddedRule__entries.md) - Entry-centric view of all entities in the rule (domain conditions and GO terms). Each entry tracks its relationships (PREDICTS, PREDICTED_BY, EQUIV) to other entries.
 * [➞go_annotations](embeddedRule__go_annotations.md) - GO terms assigned by this rule
 * [➞ipr2go_redundancy](embeddedRule__ipr2go_redundancy.md) - Analysis of redundancy with InterPro2GO mappings
 * [➞modified_date](embeddedRule__modified_date.md) - Date the rule was last modified
 * [➞reviewed_protein_count](embeddedRule__reviewed_protein_count.md) - Number of reviewed (Swiss-Prot) proteins annotated by this rule
 * [➞rule_id](embeddedRule__rule_id.md) - Original rule ID (e.g., ARBA00026249, UR000000070)
 * [➞unreviewed_protein_count](embeddedRule__unreviewed_protein_count.md) - Number of unreviewed (TrEMBL) proteins annotated by this rule
 * [evidence_type](evidence_type.md) - Evidence code (e.g., IDA, IBA, ISS, TAS)
 * [existing_annotations](existing_annotations.md)
 * [➞description](experiment__description.md) - Detailed description of the experiment to be performed
 * [➞experiment_type](experiment__experiment_type.md) - Type of experiment or assay to answer the question
 * [➞hypothesis](experiment__hypothesis.md) - Hypothesis to be investigated
 * [extensions](extensions.md)
 * [findings](findings.md)
 * [full_text_unavailable](full_text_unavailable.md) - Whether the full text is unavailable
 * [➞assessment](gOSpecificityAssessment__assessment.md) - Specificity assessment value
 * [➞notes](gOSpecificityAssessment__notes.md) - Notes on specificity - suggested alternative terms if too broad/narrow
 * [➞supported_by](gOSpecificityAssessment__supported_by.md) - Supporting text from literature for this assessment
 * [gene_symbol](gene_symbol.md) - Symbol of the gene
 * [id](id.md)
     * [RuleReview➞id](RuleReview_id.md) - The rule ID (e.g., ARBA00026249, UR000000070)
     * [Term➞id](Term_id.md) - An OBO CURIE for a term in GO, CL, CHEBI, etc.
 * [➞novel_annotations](interPro2GORedundancy__novel_annotations.md) - GO IDs not found in InterPro2GO for any rule condition
 * [➞redundant_annotations](interPro2GORedundancy__redundant_annotations.md) - GO annotations that already exist in InterPro2GO
 * [➞summary](interPro2GORedundancy__summary.md) - Human-readable summary of redundancy analysis
 * [is_invalid](is_invalid.md) - Whether the reference is invalid (e.g., retracted or replaced)
 * [label](label.md) - Human readable name of the entity
     * [Term➞label](Term_label.md) - the term name
 * [➞assessment](literatureSupportAssessment__assessment.md) - Level of literature support
 * [➞notes](literatureSupportAssessment__notes.md) - Notes on literature support - key papers, gaps in evidence
 * [➞supported_by](literatureSupportAssessment__supported_by.md) - Supporting text from literature for this assessment
 * [negated](negated.md) - Whether the term is negated
 * [ontology](ontology.md) - Ontology of the term. E.g `go`, `cl`, `hp`
 * [original_reference_id](original_reference_id.md) - ID of the original reference
 * [➞a_minus_b_count](pairwiseOverlap__a_minus_b_count.md) - Number of proteins in A but not in B (|A - B|). Represents the uniqueness of A with respect to B. High value = A adds unique coverage beyond B. Zero value = A is completely contained in B (A ⊆ B).
 * [➞b_minus_a_count](pairwiseOverlap__b_minus_a_count.md) - Number of proteins in B but not in A (|B - A|). Represents the uniqueness of B with respect to A. High value = B adds unique coverage beyond A. Zero value = B is completely contained in A (B ⊆ A).
 * [➞condition_a](pairwiseOverlap__condition_a.md) - First condition value (e.g., IPR005982)
 * [➞condition_a_in_sets](pairwiseOverlap__condition_a_in_sets.md) - List of 1-based condition set indices where condition A appears
 * [➞condition_a_label](pairwiseOverlap__condition_a_label.md) - Human-readable label for condition A
 * [➞condition_b](pairwiseOverlap__condition_b.md) - Second condition value (e.g., IPR008255)
 * [➞condition_b_in_sets](pairwiseOverlap__condition_b_in_sets.md) - List of 1-based condition set indices where condition B appears
 * [➞condition_b_label](pairwiseOverlap__condition_b_label.md) - Human-readable label for condition B
 * [➞containment_a_in_b](pairwiseOverlap__containment_a_in_b.md) - Proportion of A contained in B: |A ∩ B| / |A|. 1.0 means A is completely contained in B (A ⊆ B).
 * [➞containment_b_in_a](pairwiseOverlap__containment_b_in_a.md) - Proportion of B contained in A: |A ∩ B| / |B|. 1.0 means B is completely contained in A (B ⊆ A).
 * [➞count_a](pairwiseOverlap__count_a.md) - Number of proteins matching condition A in specified database
 * [➞count_b](pairwiseOverlap__count_b.md) - Number of proteins matching condition B in specified database
 * [➞interpretation](pairwiseOverlap__interpretation.md) - Automated interpretation of overlap pattern
 * [➞intersection_count](pairwiseOverlap__intersection_count.md) - Number of proteins matching BOTH A AND B (|A ∩ B|) in specified database
 * [➞jaccard_similarity](pairwiseOverlap__jaccard_similarity.md) - Jaccard similarity coefficient: |A ∩ B| / |A ∪ B| = intersection / (count_a + count_b - intersection). 0.0 = no overlap, 1.0 = complete overlap.
 * [➞protein_database](pairwiseOverlap__protein_database.md) - Which protein database was queried (SWISSPROT or TREMBL)
 * [➞assessment](parsimonyAssessment__assessment.md) - Parsimony assessment value
 * [➞notes](parsimonyAssessment__notes.md) - Notes on parsimony - e.g., which conditions are redundant
 * [➞supported_by](parsimonyAssessment__supported_by.md) - Supporting text from literature for this assessment
 * [predicate](predicate.md) - Predicate of the extension
     * [AnnotationExtension➞predicate](AnnotationExtension_predicate.md)
 * [product_type](product_type.md) - Type of gene product (protein, ncRNA, etc.)
 * [➞justification](proposedOntologyTerm__justification.md) - Justification for why this term is needed
 * [➞proposed_definition](proposedOntologyTerm__proposed_definition.md) - Proposed definition for the new term
 * [➞proposed_mappings](proposedOntologyTerm__proposed_mappings.md) - Proposed mappings to equivalent terms in other ontologies
 * [➞proposed_name](proposedOntologyTerm__proposed_name.md) - Proposed name for the new term
 * [➞proposed_parent](proposedOntologyTerm__proposed_parent.md) - Proposed parent term in the ontology hierarchy
 * [➞supported_by](proposedOntologyTerm__supported_by.md)
 * [proposed_new_terms](proposed_new_terms.md) - Proposed new ontology terms that should exist but don't
 * [proposed_replacement_terms](proposed_replacement_terms.md) - If the action is MODIFY, then this is a list of proposed replacement terms
 * [➞experts](question__experts.md) - Experts to answer the question. These should be drawn from the authors of relevant publications already referenced. If no suitable experts are available, it's OK to leave this as an empty list!
 * [➞question](question__question.md) - Question to be answered
 * [reason](reason.md) - Reason for the action
 * [➞go_id](redundantAnnotation__go_id.md) - GO term ID (e.g., GO:0004791)
 * [➞go_label](redundantAnnotation__go_label.md) - GO term label
 * [➞interpro_label](redundantAnnotation__interpro_label.md) - InterPro domain label
 * [➞interpro_source](redundantAnnotation__interpro_source.md) - InterPro ID that already maps to this GO term in ipr2go
 * [reference_id](reference_id.md)
 * [reference_section_type](reference_section_type.md) - Type of section in the reference (e.g., 'ABSTRACT', 'METHODS', 'RESULTS', 'DISCUSSION')
 * [references](references.md)
 * [➞containment](relatedEntry__containment.md) - Containment score (0-1) for the directional relationship. For PREDICTS: this_in_target (how much of this is contained in target). For PREDICTED_BY: target_in_this (how much of target is contained in this). For EQUIV: max of both directions.
 * [➞exclusive_count](relatedEntry__exclusive_count.md) - Number of proteins exclusive to the "source" of the relationship. For PREDICTS: proteins in this but not target. For PREDICTED_BY: proteins in target but not this. For EQUIV: proteins in this but not target (A - B).
 * [➞intersection_count](relatedEntry__intersection_count.md) - Number of proteins in both this and target
 * [➞jaccard_similarity](relatedEntry__jaccard_similarity.md) - Jaccard similarity coefficient (0-1)
 * [➞relationship](relatedEntry__relationship.md) - Type of relationship
 * [➞target_id](relatedEntry__target_id.md) - ID of the related entry
 * [retired](retired.md) - Whether the annotation is retired or replaced
 * [review](review.md) - Review of the gene
 * [➞conditions](ruleConditionSet__conditions.md) - Conditions in this set (all must match)
 * [➞notes](ruleConditionSet__notes.md) - Reviewer notes on this specific condition set
 * [➞number](ruleConditionSet__number.md) - 1-based condition set number (CS1, CS2, CS3, etc.)
 * [➞pairwise_overlap](ruleConditionSet__pairwise_overlap.md) - Pairwise overlap statistics for domain conditions in this set. Only computed for InterPro, FunFam, PANTHER conditions. Provides set difference metrics (uniqueness) and Jaccard similarity.
 * [➞condition_type](ruleCondition__condition_type.md) - Type of condition
 * [➞curie](ruleCondition__curie.md) - Normalized CURIE form (e.g., InterPro:IPR000001, NCBITaxon:4751)
 * [➞interpro_type](ruleCondition__interpro_type.md) - InterPro entry type (family, domain, active_site, etc.). Only populated for InterPro conditions (condition_type = INTERPRO). Extracted from InterPro metadata or API.
 * [➞label](ruleCondition__label.md) - Human-readable label
 * [➞negated](ruleCondition__negated.md) - Whether this is a negative condition (NOT)
 * [➞protein_count](ruleCondition__protein_count.md) - Number of proteins matching this condition in specified database. Only populated for domain/family conditions (InterPro, FunFam, PANTHER). Null for taxon and other condition types.
 * [➞protein_database](ruleCondition__protein_database.md) - Which protein database was queried (e.g., SWISSPROT, TREMBL). Defaults to SWISSPROT (reviewed proteins only). Important to specify since counts differ dramatically between databases.
 * [➞sample_proteins](ruleCondition__sample_proteins.md) - Sample UniProt IDs matching this condition. Only included when protein_count < 20 to avoid bloating files. Limited to max 10 examples.
 * [➞uniqueness_score](ruleCondition__uniqueness_score.md) - Measure of domain uniqueness (0.0 to 1.0). Calculated as 1.0 - mean(containment in other domains in same condition set). High score = more unique/specific domain. Low score = broad domain that commonly co-occurs.
 * [➞value](ruleCondition__value.md) - The condition value (e.g., IPR000001, NCBITaxon:4751)
 * [➞aspect](ruleGOAnnotation__aspect.md) - GO aspect (F, P, or C)
 * [➞go_id](ruleGOAnnotation__go_id.md) - GO term ID (e.g., GO:0004791)
 * [➞go_label](ruleGOAnnotation__go_label.md) - GO term name
 * [➞appears_in_condition_sets](ruleReviewEntry__appears_in_condition_sets.md) - Which condition sets (1-based) contain this entry (for domain conditions only)
 * [➞asserted_predicted_go_terms](ruleReviewEntry__asserted_predicted_go_terms.md) - GO terms that this entry maps to via external mappings (e.g., ipr2go). Only populated for external entries not in the rule's condition sets.
 * [➞id](ruleReviewEntry__id.md) - Identifier (IPR005982, GO:0004791, 3.50.50.60:FF:000064, etc.)
 * [➞label](ruleReviewEntry__label.md) - Human-readable name
 * [➞protein_count](ruleReviewEntry__protein_count.md) - Number of proteins matching this condition (from SwissProt)
 * [➞related_entries](ruleReviewEntry__related_entries.md) - Relationships to other entries in the rule
 * [➞source](ruleReviewEntry__source.md) - Source of this entry if external to the rule (e.g., 'ipr2go' for InterPro entries that map to the same GO term via InterPro2GO but are not part of any condition set)
 * [➞type](ruleReviewEntry__type.md) - Type of entry (INTERPRO, FUNFAM, PANTHER, GO_TERM, etc.)
 * [➞action](ruleReview__action.md) - Recommended action for this rule
 * [➞action_rationale](ruleReview__action_rationale.md) - Rationale for the recommended action
 * [➞condition_overlap](ruleReview__condition_overlap.md) - Assessment of overlap between rule conditions
 * [➞confidence](ruleReview__confidence.md) - Overall confidence in the rule (0.0 to 1.0)
 * [➞go_specificity](ruleReview__go_specificity.md) - Assessment of GO term specificity
 * [➞literature_support](ruleReview__literature_support.md) - Assessment of literature support for the rule
 * [➞parsimony](ruleReview__parsimony.md) - Assessment of rule parsimony (simplicity vs complexity)
 * [➞review_summary](ruleReview__review_summary.md) - Overall summary of the review findings
 * [➞rule](ruleReview__rule.md) - The embedded rule being reviewed
 * [➞rule_type](ruleReview__rule_type.md) - Type of rule (ARBA or UniRule)
 * [➞status](ruleReview__status.md) - Status of the rule review
 * [➞suggested_modifications](ruleReview__suggested_modifications.md) - Specific modifications suggested if action is MODIFY
 * [➞supported_by](ruleReview__supported_by.md) - Supporting text from literature for this review
 * [➞taxonomic_scope](ruleReview__taxonomic_scope.md) - Assessment of taxonomic restriction appropriateness
 * [statement](statement.md) - Concise statement describing an aspect of the gene
 * [status](status.md) - Overall status of the gene review
 * [suggested_experiments](suggested_experiments.md)
 * [suggested_questions](suggested_questions.md) - Suggested questions to ask experts about the gene. Only include if not obvious from the literature.
 * [summary](summary.md) - Summary of the review
 * [supported_by](supported_by.md)
 * [supporting_entities](supporting_entities.md) - IDs of the supporting entities
 * [supporting_text](supporting_text.md) - Supporting text from the publication. This should be exact substrings. Different substrings can be broken up by '...'s. These substrings will be checked against the actual text of the paper. If editorialization is necessary, put this in square brackets (this is not checked). For example, you can say '...[CFAP300 shows] transport within cilia is IFT dependent...'
 * [tags](tags.md) - Tags associated with the gene for categorization and organization
 * [taxon](taxon.md)
 * [➞assessment](taxonomicScopeAssessment__assessment.md) - Taxonomic scope assessment value
 * [➞notes](taxonomicScopeAssessment__notes.md) - Notes on taxonomic scope - suggested changes to taxon constraints
 * [➞supported_by](taxonomicScopeAssessment__supported_by.md) - Supporting text from literature for this assessment
 * [term](term.md) - Term to be annotated
     * [ExistingAnnotation➞term](ExistingAnnotation_term.md)
 * [➞predicate](termMapping__predicate.md) - Mapping predicate (e.g., 'skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch', 'skos:narrowMatch')
 * [➞target_term](termMapping__target_term.md) - The target term in another ontology
 * [title](title.md) - Title of the entity

### Enums

 * [ActionEnum](ActionEnum.md)
 * [ConditionTypeEnum](ConditionTypeEnum.md) - Types of conditions in rule antecedents
 * [EntryRelationshipEnum](EntryRelationshipEnum.md) - Type of relationship between entries in a rule
 * [EntryTypeEnum](EntryTypeEnum.md) - Type of entry in a rule review (domain/family condition or GO term target)
 * [EvidenceType](EvidenceType.md) - Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
 * [GOBiologicalProcessEnum](GOBiologicalProcessEnum.md) - A biological process term in the GO ontology
 * [GOCellularLocationEnum](GOCellularLocationEnum.md) - A cellular location term in the GO ontology (excludes protein-containing complexes)
 * [GOMolecularActivityEnum](GOMolecularActivityEnum.md) - A molecular activity term in the GO ontology
 * [GOProteinContainingComplexEnum](GOProteinContainingComplexEnum.md) - A protein-containing complex term in the GO ontology
 * [GOTermEnum](GOTermEnum.md) - A term in the GO ontology
 * [GeneReviewStatusEnum](GeneReviewStatusEnum.md) - Status of the gene review process
 * [InterProTypeEnum](InterProTypeEnum.md) - InterPro entry types categorizing protein signatures
 * [LiteratureSupportEnum](LiteratureSupportEnum.md) - Level of literature support for the rule
 * [ManuscriptSection](ManuscriptSection.md) - Sections of a scientific manuscript or publication
 * [OverlapEnum](OverlapEnum.md) - Assessment of condition overlap/redundancy
 * [OverlapInterpretationEnum](OverlapInterpretationEnum.md) - Automated interpretation of domain overlap patterns
 * [ParsimonyEnum](ParsimonyEnum.md) - Assessment of rule parsimony (simplicity vs complexity)
 * [ProductTypeEnum](ProductTypeEnum.md) - Type of gene product
 * [ProteinDatabaseEnum](ProteinDatabaseEnum.md) - Protein database types for rule analysis
 * [ROTermEnum](ROTermEnum.md) - A term in the relation ontology
 * [RuleActionEnum](RuleActionEnum.md) - Recommended action for the rule
 * [RuleReviewStatusEnum](RuleReviewStatusEnum.md) - Status of the rule review
 * [RuleTypeEnum](RuleTypeEnum.md) - Type of UniProt annotation rule
 * [SpecificityEnum](SpecificityEnum.md) - Assessment of GO term specificity
 * [TaxonomicScopeEnum](TaxonomicScopeEnum.md) - Assessment of taxonomic restriction appropriateness

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
