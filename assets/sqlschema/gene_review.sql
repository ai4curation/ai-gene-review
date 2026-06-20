-- # Class: GeneReview Description: Complete review for a gene
--     * Slot: id
--     * Slot: gene_symbol Description: Symbol of the gene
--     * Slot: product_type Description: Type of gene product (protein, ncRNA, etc.)
--     * Slot: status Description: Overall status of the gene review
--     * Slot: description Description: Description of the entity
--     * Slot: taxon_id
-- # Class: AlternativeProduct Description: An alternative splicing product (isoform) of the gene. Corresponds to UniProt isoform entries. Use this to document isoform-specific functions where different isoforms have distinct or even antagonistic biological activities. DEPRECATED: Use FunctionalIsoform instead for curated functional classes.
--     * Slot: id Description: UniProt isoform ID (e.g., Q07817-1, Q07817-2)
--     * Slot: name Description: Common name of the isoform (e.g., Bcl-xL, Bcl-xS)
--     * Slot: sequence_note Description: Brief note about sequence differences (e.g., "lacks exon 2", "shorter C-terminus")
--     * Slot: description Description: Agent-populated description of the isoform's function. Document any isoform-specific functions, expression patterns, or biological activities that differ from other isoforms.
--     * Slot: GeneReview_id Description: Autocreated FK slot
-- # Class: FunctionalIsoform Description: A curated functional isoform class. Unlike AlternativeProduct (which maps 1:1 to UniProt isoforms), this captures FUNCTIONALLY RELEVANT distinctions that may: - Group multiple UniProt isoforms into a functional class (e.g., WT1 +KTS isoforms) - Represent cleavage products from polyproteins (e.g., POMC peptides) - Describe modification states or conformational variants Only create entries when there ARE functionally distinct forms worth documenting.
--     * Slot: id Description: Curator-defined identifier for this functional class. Use a descriptive format like GENE_CLASS (e.g., WT1_PLUS_KTS, POMC_ACTH, BCL2L1_XL).
--     * Slot: name Description: Human-readable name for this functional class (e.g., "+KTS isoforms", "ACTH/Corticotropin", "Bcl-xL").
--     * Slot: type Description: Type of functional distinction (SPLICE_VARIANT, SPLICE_CLASS, CLEAVAGE_PRODUCT, MODIFICATION_STATE, CONFORMATIONAL_STATE).
--     * Slot: description Description: Detailed description of this functional class. Document the specific functions, how they differ from other classes, tissue specificity, and any antagonistic relationships (e.g., "OREXIGENIC - opposite to alpha-MSH").
--     * Slot: GeneReview_id Description: Autocreated FK slot
-- # Class: FunctionalIsoformMapping Description: A mapping from a functional isoform class to underlying UniProt identifiers. Allows grouping multiple UniProt isoforms or chains into a single functional class.
--     * Slot: id
--     * Slot: type Description: Type of identifier (UNIPROT_ISOFORM or UNIPROT_CHAIN)
--     * Slot: residues Description: Residue range for cleavage products (e.g., "138-176" for ACTH). Only applicable for UNIPROT_CHAIN type.
--     * Slot: FunctionalIsoform_id Description: Autocreated FK slot
-- # Class: Term Description: A term in a specific ontology
--     * Slot: id Description: A CURIE for a term or database object in GO, CL, CHEBI, UniProtKB, PANTHER, etc.
--     * Slot: label Description: the term name
--     * Slot: description Description: Description of the entity
--     * Slot: ontology Description: Ontology of the term. E.g `go`, `cl`, `hp`
--     * Slot: FunctionalIsoform_id Description: Autocreated FK slot
--     * Slot: Review_id Description: Autocreated FK slot
--     * Slot: CoreFunction_id Description: Autocreated FK slot
-- # Class: Reference Description: A reference is a published text  that describes a finding or a method. References might be formal publications (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review can be made by using the `file:` prefix.
--     * Slot: id
--     * Slot: title Description: Title of the entity
--     * Slot: is_invalid Description: Whether the reference is invalid (e.g., retracted or replaced)
--     * Slot: publication_type Description: The kind of publication or source this reference is (e.g. primary research article, review, meta-analysis, database record, AI deep-research report). For PMIDs this is normally inferred from the PubMed publication-type ('PT') metadata rather than set by hand; for non-PMID references (GO_REF, Reactome, file:) it is inferred from the identifier. Lets analyses ask, e.g., whether review articles or abstracts alone are sufficient to support a given annotation action.
--     * Slot: full_text_unavailable Description: Whether the full text is unavailable
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: ModuleReview_id Description: Autocreated FK slot
--     * Slot: RuleReview_id Description: Autocreated FK slot
--     * Slot: PredictionReview_id Description: Autocreated FK slot
--     * Slot: reference_review_id Description: Manual reviewer assessment of this reference (relevance, and citation correctness / scientific soundness). Reviewer-supplied, distinct from the machine-fetched id/title.
-- # Class: ReferenceReview Description: Manual reviewer assessment of a reference - how relevant it is to the gene's function, and whether it is correctly cited and scientifically sound. Distinct from the machine-fetched id/title fields; all fields are optional and reviewer-supplied.
--     * Slot: id
--     * Slot: relevance Description: Reviewer judgment of how relevant the reference is to the gene's function and this review.
--     * Slot: correctness Description: Reviewer's overall assessment of a reference's trustworthiness - both citation correctness (the identifier resolves to the intended paper that supports its use) and scientific soundness of that paper's claim.
--     * Slot: review_notes Description: Free-text note explaining the relevance/correctness judgment (e.g. what was verified, or why a citation is wrong, disputed, or low quality).
-- # Class: Finding Description: A finding is a statement about a gene, which is supported by a reference. Similar to "comments" in uniprot
--     * Slot: id
--     * Slot: statement Description: Concise statement describing an aspect of the gene
--     * Slot: supporting_text Description: Supporting text from the publication. This should be exact substrings. Different substrings can be broken up by '...'s. These substrings will be checked against the actual text of the paper. If editorialization is necessary, put this in square brackets (this is not checked). For example, you can say '...[CFAP300 shows] transport within cilia is IFT dependent...'
--     * Slot: full_text_unavailable Description: Whether the full text is unavailable
--     * Slot: reference_section_type Description: Type of section in the reference (e.g., 'ABSTRACT', 'METHODS', 'RESULTS', 'DISCUSSION')
--     * Slot: finding_review_id Description: Manual reviewer assessment of this specific finding - in particular whether the finding remains current, is disputed, or has been overturned/superseded by later evidence. Reviewer-supplied; distinct from the statement/supporting_text that describe the finding itself.
-- # Class: FindingReview Description: Manual reviewer assessment of a specific finding within a reference - in particular whether it remains current, is disputed, or has been overturned/superseded by later evidence. This is finer-grained than reference_review (which assesses the whole reference); a paper may contain some findings that stand and others that are overturned. All fields optional and reviewer-supplied.
--     * Slot: id
--     * Slot: finding_status Description: Reviewer's assessment of the empirical standing of a specific finding in light of other evidence (e.g. whether it has been disputed or overturned).
--     * Slot: review_notes Description: Free-text note explaining the relevance/correctness judgment (e.g. what was verified, or why a citation is wrong, disputed, or low quality).
-- # Class: SupportingTextInReference Description: A supporting text in a reference.
--     * Slot: id
--     * Slot: reference_id
--     * Slot: supporting_text Description: Supporting text from the publication. This should be exact substrings. Different substrings can be broken up by '...'s. These substrings will be checked against the actual text of the paper. If editorialization is necessary, put this in square brackets (this is not checked). For example, you can say '...[CFAP300 shows] transport within cilia is IFT dependent...'
--     * Slot: supporting_text_fulltext Description: Supporting text from the full-text PDF when the full text cannot be committed to the repository. This is an interim solution for cases where we have access to full text but cannot share it publicly. Unlike supporting_text, this field is not validated against cached publication text.
--     * Slot: full_text_unavailable Description: Whether the full text is unavailable
--     * Slot: reference_section_type Description: Type of section in the reference (e.g., 'ABSTRACT', 'METHODS', 'RESULTS', 'DISCUSSION')
--     * Slot: KnowledgeGap_id Description: Autocreated FK slot
-- # Class: EvidenceItem Description: A lightweight citable source for module-level assertions. The source may be a PMID, DOI, database record, local file, pathway record, issue, or any other citable artifact. This is deliberately less strict than the publication quote validation used in gene reviews.
--     * Slot: id
--     * Slot: source_id Description: Identifier for the evidence source, e.g. PMID:123456, DOI:..., Reactome:R-HSA-..., MetaCyc:..., file:...
--     * Slot: title
--     * Slot: statement Description: The assertion this evidence supports in this module.
--     * Slot: supporting_text Description: Optional quote or excerpt from the evidence source.
--     * Slot: url
--     * Slot: notes
--     * Slot: Descriptor_id Description: Autocreated FK slot
--     * Slot: ChemicalEntityDescriptor_id Description: Autocreated FK slot
--     * Slot: GeneDescriptor_id Description: Autocreated FK slot
--     * Slot: GeneProductDescriptor_id Description: Autocreated FK slot
--     * Slot: FamilyDescriptor_id Description: Autocreated FK slot
--     * Slot: DomainDescriptor_id Description: Autocreated FK slot
--     * Slot: CellularComponentDescriptor_id Description: Autocreated FK slot
--     * Slot: ProteinComplexDescriptor_id Description: Autocreated FK slot
--     * Slot: ComplexUnit_uid Description: Autocreated FK slot
--     * Slot: CellTypeDescriptor_id Description: Autocreated FK slot
--     * Slot: AnatomicalEntityDescriptor_id Description: Autocreated FK slot
--     * Slot: DevelopmentalStageDescriptor_id Description: Autocreated FK slot
--     * Slot: TaxonDescriptor_id Description: Autocreated FK slot
--     * Slot: MolecularFunctionDescriptor_id Description: Autocreated FK slot
--     * Slot: BiologicalProcessDescriptor_id Description: Autocreated FK slot
--     * Slot: RelationDescriptor_id Description: Autocreated FK slot
--     * Slot: ModuleReview_id Description: Autocreated FK slot
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: ModulePart_id Description: Autocreated FK slot
--     * Slot: ModuleVariantSet_uid Description: Autocreated FK slot
--     * Slot: ModuleAnnoton_uid Description: Autocreated FK slot
--     * Slot: ParticipantSelector_id Description: Autocreated FK slot
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: ModuleConnection_id Description: Autocreated FK slot
-- # Class: Descriptor Description: A human-friendly descriptor with optional ontology/database grounding. The preferred_term may be more nuanced than the term label, and the term may be absent when no good identifier exists yet.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: MolecularFunctionDescriptor_id Description: Autocreated FK slot
--     * Slot: BiologicalProcessDescriptor_id Description: Autocreated FK slot
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: ChemicalEntityDescriptor Description: A descriptor for a chemical entity, metabolite, cofactor, ion, or small molecule.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: GeneDescriptor Description: A descriptor for a gene or locus.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: GeneProductDescriptor Description: A descriptor for a gene product, protein, isoform, or gene-product form.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: FamilyDescriptor_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: FamilyDescriptor Description: A descriptor for a protein family, orthogroup, or other evolutionary grouping.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: DomainDescriptor Description: A descriptor for a protein domain, motif, site, or architectural feature.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: CellularComponentDescriptor Description: A descriptor for a cellular component, organelle, compartment, or complex location.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleAnnoton_uid Description: Autocreated FK slot
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: ProteinComplexDescriptor Description: A descriptor for a protein-containing complex or subcomplex.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: ComplexUnit Description: A role-bearing unit within a protein complex descriptor.
--     * Slot: uid
--     * Slot: id
--     * Slot: label
--     * Slot: role
--     * Slot: stoichiometry Description: Optional stoichiometry or copy-number statement when known.
--     * Slot: notes
--     * Slot: ProteinComplexDescriptor_id Description: Autocreated FK slot
--     * Slot: participant_id
--     * Slot: function_id
-- # Class: CellTypeDescriptor Description: A descriptor for a cell type or cell state.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: AnatomicalEntityDescriptor Description: A descriptor for an anatomical entity, tissue, organismal region, or structure.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: DevelopmentalStageDescriptor Description: A descriptor for a developmental stage, life-cycle stage, or temporal window.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: TaxonDescriptor Description: A descriptor for a taxon or taxonomic scope.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleContext_id Description: Autocreated FK slot
--     * Slot: term_id
-- # Class: MolecularFunctionDescriptor Description: A descriptor for a molecular function. Extra slots capture common functional nuance without requiring formal post-composition.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: source_location_id
--     * Slot: destination_location_id
--     * Slot: term_id
-- # Class: BiologicalProcessDescriptor Description: A descriptor for a biological process, pathway, reaction, or process-like module grounding.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleAnnoton_uid Description: Autocreated FK slot
--     * Slot: starts_with_id
--     * Slot: ends_with_id
--     * Slot: term_id
-- # Class: RelationDescriptor Description: A descriptor for a relation or connection predicate.
--     * Slot: id
--     * Slot: preferred_term
--     * Slot: description
--     * Slot: notes
--     * Slot: term_id
-- # Class: ModuleReview Description: Review or curation record for a recursively decomposable biological module. This can describe a pathway, organelle lifecycle, protein complex, molecular function, developmental process, or abstract/evolutionary functional plan.
--     * Slot: id
--     * Slot: title Description: Title of the entity
--     * Slot: description Description: Description of the entity
--     * Slot: status
--     * Slot: notes
--     * Slot: module_id
-- # Class: ModuleNode Description: A node in a module. Nodes can be recursively decomposed using parts and variant_sets, and may also carry leaf annotons and connections.
--     * Slot: id
--     * Slot: label
--     * Slot: module_type
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleVariantSet_uid Description: Autocreated FK slot
--     * Slot: context_id
-- # Class: ModulePart Description: A conjunctive part or step of a module node.
--     * Slot: id
--     * Slot: order Description: Optional display or temporal order. Equal or absent values imply partial ordering only.
--     * Slot: role Description: Curator-supplied role of this part within the parent module.
--     * Slot: optional Description: Whether this part is optional in the parent module.
--     * Slot: notes
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: node_id
-- # Class: ModuleVariantSet Description: A set of alternative implementations for a module node or part. Variants may themselves contain parts, annotons, connections, and nested variant sets.
--     * Slot: uid
--     * Slot: id
--     * Slot: label
--     * Slot: axis Description: The dimension along which these variants differ, e.g. taxon, cell type, compartment, route, enzyme family.
--     * Slot: selection Description: How many variants may be selected in a concrete realization.
--     * Slot: notes
--     * Slot: ModuleNode_id Description: Autocreated FK slot
-- # Class: ModuleAnnoton Description: A leaf role assertion in a module. The participant may be a concrete gene or an abstract selector, and the function/process/location fields are descriptor holders rather than direct GO annotation exports.
--     * Slot: uid
--     * Slot: id
--     * Slot: label
--     * Slot: role_description
--     * Slot: notes
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: participant_id
--     * Slot: function_id
-- # Class: ParticipantSelector Description: A selector for a concrete or abstract participant in a module annoton. This can ground to a gene, gene product, complex, family, domain, ortholog, homolog, or any entity satisfying a functional/domain constraint.
--     * Slot: id
--     * Slot: selector_type
--     * Slot: description
--     * Slot: notes
--     * Slot: gene_id
--     * Slot: gene_product_id
--     * Slot: protein_complex_id
--     * Slot: family_id
--     * Slot: domain_id
--     * Slot: homolog_of_id
--     * Slot: ortholog_of_id
--     * Slot: required_function_id
--     * Slot: required_domain_id
--     * Slot: taxon_id
-- # Class: ModuleContext Description: Context that applies to a module node, variant, annoton, or connection.
--     * Slot: id
--     * Slot: notes
-- # Class: ModuleConnection Description: A connection between module nodes, annotons, or other named elements. Source and target are IDs scoped to the module document.
--     * Slot: id
--     * Slot: source
--     * Slot: target
--     * Slot: connection_type
--     * Slot: description
--     * Slot: notes
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: predicate_id
--     * Slot: context_id
-- # Class: ExistingAnnotation Description: An existing annotation from the GO database, plus a review of the annotation.
--     * Slot: id
--     * Slot: qualifier Description: The GO annotation qualifier specifying the relationship between the gene product and the term. For MF annotations, distinguishes 'enables' (gene product has the activity independently) from 'contributes_to' (gene product contributes to a complex's activity but does not have the activity alone). For BP, distinguishes 'involved_in', 'acts_upstream_of', etc. For CC, distinguishes 'located_in', 'part_of', 'is_active_in', 'colocalizes_with'.
--     * Slot: negated Description: Whether the term is negated
--     * Slot: evidence_type Description: Evidence code (e.g., IDA, IBA, ISS, TAS)
--     * Slot: original_reference_id Description: ID of the original reference
--     * Slot: retired Description: Whether the annotation is retired or replaced
--     * Slot: isoform Description: UniProt isoform identifier (e.g., "P19544-1" for WT1 isoform 1). Only populated when the annotation is specific to a particular isoform rather than the canonical protein sequence. Note that just because an experiment used a particular isoform doesn't mean the annotation is isoform-specific - it may apply to all isoforms. Use this field only when there is clear evidence the annotation is isoform-specific.
--     * Slot: term_id Description: Term to be annotated
--     * Slot: review_id Description: Review of the gene
-- # Class: Review Description: A review of an existing annotation.
--     * Slot: id
--     * Slot: summary Description: Summary of the review
--     * Slot: action Description: Action to be taken
--     * Slot: reason Description: Reason for the action
-- # Class: CoreFunction Description: A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the reviewed core annotations, brought together into a unified GO-CAM-like representation.
--     * Slot: id
--     * Slot: description Description: Description of the core function
--     * Slot: molecular_function_id Description: The molecular function this gene product enables (i.e., has the activity independently). For complex subunits that contribute to but don't independently have a complex-level activity, use contributes_to_molecular_function instead and put a subunit-specific MF here (e.g., structural constituent of ribosome, electron transfer activity).
--     * Slot: contributes_to_molecular_function_id Description: A molecular function that this gene product contributes to as part of a complex, but does not independently enable. Used for accessory/structural subunits of multi-protein complexes (e.g., an accessory subunit of Complex I contributes_to NADH dehydrogenase activity but does not have that activity on its own). The molecular_function slot should then contain the subunit-specific activity (e.g., structural molecule activity).
--     * Slot: in_complex_id Description: The protein-containing complex (GO:0032991 descendant) that this gene product is an active unit of. Use this — not locations — for complex membership (e.g. ribosome, spliceosome, EMC, signal peptidase complex).
-- # Class: AnnotationExtension
--     * Slot: id
--     * Slot: predicate Description: Predicate of the extension
--     * Slot: term_id Description: Term to be annotated
-- # Class: TermMapping Description: A mapping between the proposed term and an equivalent term in another ontology
--     * Slot: id
--     * Slot: predicate Description: Mapping predicate (e.g., 'skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch', 'skos:narrowMatch')
--     * Slot: ProposedOntologyTerm_id Description: Autocreated FK slot
--     * Slot: target_term_id Description: The target term in another ontology
-- # Class: ProposedOntologyTerm Description: A proposed new ontology term that should exist but doesn't currently
--     * Slot: id
--     * Slot: proposed_name Description: Proposed name for the new term
--     * Slot: proposed_definition Description: Proposed definition for the new term
--     * Slot: justification Description: Justification for why this term is needed
--     * Slot: KnowledgeGap_id Description: Autocreated FK slot
--     * Slot: proposed_parent_id Description: Proposed parent term in the ontology hierarchy
-- # Class: KnowledgeGap Description: A curated, literature-grounded statement of what is NOT known about a gene product, core function, module, or step — its molecular activity, mechanism, partner(s), localization, or biological role. A knowledge gap is a reviewer judgment reached by reading the primary literature, NOT a pattern in the annotations: a heavily annotated gene can hide a gaping mechanistic hole, and a sparsely annotated one can be perfectly understood and merely under-curated. Each gap is a small, defensible scholarly object with the same evidentiary discipline used for positive claims. See projects/FUNCTION_KNOWLEDGE_GAPS.md for the methodology and worked exemplars.
--     * Slot: id
--     * Slot: gap_statement Description: The specific unknown, stated precisely. Not "role unclear" but e.g. "the direct substrate / the catalytic activity / the essential partner is undetermined".
--     * Slot: boundary Description: What IS firmly established, so the gap is sharply delimited. The edge of current knowledge against which the gap is defined.
--     * Slot: dark_aspect Description: Which GO aspect (or pattern) is dark for this gap. Most "dark" genes are not uniformly dark.
--     * Slot: status Description: Lifecycle status of the gap, tracking progress toward resolution.
--     * Slot: significance Description: Why closing this gap matters.
--     * Slot: resolution Description: What would resolve the gap — the experiment, ontology term, or curation action. For ONTOLOGY gaps, pair with proposed_terms (or the gene's top-level proposed_new_terms).
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: ModuleReview_id Description: Autocreated FK slot
--     * Slot: ModuleNode_id Description: Autocreated FK slot
--     * Slot: Review_id Description: Autocreated FK slot
--     * Slot: CoreFunction_id Description: Autocreated FK slot
-- # Class: Experiment Description: A suggested experiment to answer a question about the gene
--     * Slot: id
--     * Slot: hypothesis Description: Hypothesis to be investigated
--     * Slot: description Description: Detailed description of the experiment to be performed
--     * Slot: experiment_type Description: Type of experiment or assay to answer the question
-- # Class: Question Description: A question to be answered about the gene
--     * Slot: id
--     * Slot: question Description: Question to be answered
-- # Class: RuleReview Description: A review of a UniProt annotation rule (ARBA or UniRule). Each review covers ONE rule and assesses its quality, literature support, and biological appropriateness.
--     * Slot: id Description: The rule ID (e.g., ARBA00026249, UR000000070)
--     * Slot: description Description: Description of the entity
--     * Slot: status Description: Status of the rule review
--     * Slot: rule_type Description: Type of rule (ARBA or UniRule)
--     * Slot: review_summary Description: Overall summary of the review findings
--     * Slot: action Description: Recommended action for this rule
--     * Slot: action_rationale Description: Rationale for the recommended action
--     * Slot: confidence Description: Overall confidence in the rule (0.0 to 1.0)
--     * Slot: rule_id Description: The embedded rule being reviewed
--     * Slot: parsimony_id Description: Assessment of rule parsimony (simplicity vs complexity)
--     * Slot: literature_support_id Description: Assessment of literature support for the rule
--     * Slot: condition_overlap_id Description: Assessment of overlap between rule conditions
--     * Slot: go_specificity_id Description: Assessment of GO term specificity
--     * Slot: taxonomic_scope_id Description: Assessment of taxonomic restriction appropriateness
-- # Class: EmbeddedRule Description: An embedded representation of an ARBA or UniRule for storage in YAML. Captures the essential structure: conditions (antecedent) and GO annotations (consequent).
--     * Slot: id
--     * Slot: rule_id Description: Original rule ID (e.g., ARBA00026249, UR000000070)
--     * Slot: reviewed_protein_count Description: Number of reviewed (Swiss-Prot) proteins annotated by this rule
--     * Slot: unreviewed_protein_count Description: Number of unreviewed (TrEMBL) proteins annotated by this rule
--     * Slot: created_date Description: Date the rule was created
--     * Slot: modified_date Description: Date the rule was last modified
--     * Slot: ipr2go_redundancy_id Description: Analysis of redundancy with InterPro2GO mappings
-- # Class: RuleConditionSet Description: A set of conditions that must ALL be true (conjunction/AND). Multiple condition sets in a rule are OR-ed together (disjunction).
--     * Slot: id
--     * Slot: number Description: 1-based condition set number (CS1, CS2, CS3, etc.)
--     * Slot: notes Description: Reviewer notes on this specific condition set
--     * Slot: EmbeddedRule_id Description: Autocreated FK slot
-- # Class: RuleCondition Description: A single condition in a rule antecedent
--     * Slot: id
--     * Slot: condition_type Description: Type of condition
--     * Slot: value Description: The condition value (e.g., IPR000001, NCBITaxon:4751)
--     * Slot: curie Description: Normalized CURIE form (e.g., InterPro:IPR000001, NCBITaxon:4751)
--     * Slot: label Description: Human-readable label
--     * Slot: interpro_type Description: InterPro entry type (family, domain, active_site, etc.). Only populated for InterPro conditions (condition_type = INTERPRO). Extracted from InterPro metadata or API.
--     * Slot: negated Description: Whether this is a negative condition (NOT)
--     * Slot: protein_count Description: Number of proteins matching this condition in specified database. Only populated for domain/family conditions (InterPro, FunFam, PANTHER). Null for taxon and other condition types.
--     * Slot: protein_database Description: Which protein database was queried (e.g., SWISSPROT, TREMBL). Defaults to SWISSPROT (reviewed proteins only). Important to specify since counts differ dramatically between databases.
--     * Slot: uniqueness_score Description: Measure of domain uniqueness (0.0 to 1.0). Calculated as 1.0 - mean(containment in other domains in same condition set). High score = more unique/specific domain. Low score = broad domain that commonly co-occurs.
--     * Slot: RuleConditionSet_id Description: Autocreated FK slot
-- # Class: RuleGOAnnotation Description: A GO annotation produced by the rule
--     * Slot: id
--     * Slot: go_id Description: GO term ID (e.g., GO:0004791)
--     * Slot: go_label Description: GO term name
--     * Slot: aspect Description: GO aspect (F, P, or C)
--     * Slot: EmbeddedRule_id Description: Autocreated FK slot
-- # Class: PairwiseOverlap Description: Overlap statistics between two domain conditions (InterPro, FunFam, etc.) in the same condition set. Provides set difference metrics to measure uniqueness and redundancy.
--     * Slot: id
--     * Slot: condition_a Description: First condition value (e.g., IPR005982)
--     * Slot: condition_b Description: Second condition value (e.g., IPR008255)
--     * Slot: condition_a_label Description: Human-readable label for condition A
--     * Slot: condition_b_label Description: Human-readable label for condition B
--     * Slot: protein_database Description: Which protein database was queried (SWISSPROT or TREMBL)
--     * Slot: count_a Description: Number of proteins matching condition A in specified database
--     * Slot: count_b Description: Number of proteins matching condition B in specified database
--     * Slot: intersection_count Description: Number of proteins matching BOTH A AND B (|A ∩ B|) in specified database
--     * Slot: a_minus_b_count Description: Number of proteins in A but not in B (|A - B|). Represents the uniqueness of A with respect to B. High value = A adds unique coverage beyond B. Zero value = A is completely contained in B (A ⊆ B).
--     * Slot: b_minus_a_count Description: Number of proteins in B but not in A (|B - A|). Represents the uniqueness of B with respect to A. High value = B adds unique coverage beyond A. Zero value = B is completely contained in A (B ⊆ A).
--     * Slot: jaccard_similarity Description: Jaccard similarity coefficient: |A ∩ B| / |A ∪ B| = intersection / (count_a + count_b - intersection). 0.0 = no overlap, 1.0 = complete overlap.
--     * Slot: containment_a_in_b Description: Proportion of A contained in B: |A ∩ B| / |A|. 1.0 means A is completely contained in B (A ⊆ B).
--     * Slot: containment_b_in_a Description: Proportion of B contained in A: |A ∩ B| / |B|. 1.0 means B is completely contained in A (B ⊆ A).
--     * Slot: interpretation Description: Automated interpretation of overlap pattern
--     * Slot: RuleConditionSet_id Description: Autocreated FK slot
-- # Class: RuleReviewEntry Description: An entity in the rule - either a domain/family condition or a GO term target. Each entry tracks its relationships (predictions, predicted-by, equivalence) to other entries.
--     * Slot: id Description: Identifier (IPR005982, GO:0004791, 3.50.50.60:FF:000064, etc.)
--     * Slot: label Description: Human-readable name
--     * Slot: type Description: Type of entry (INTERPRO, FUNFAM, PANTHER, GO_TERM, etc.)
--     * Slot: protein_count Description: Number of proteins matching this condition (from SwissProt)
--     * Slot: source Description: Source of this entry if external to the rule (e.g., 'ipr2go' for InterPro entries that map to the same GO term via InterPro2GO but are not part of any condition set)
--     * Slot: EmbeddedRule_id Description: Autocreated FK slot
-- # Class: RelatedEntry Description: A relationship from this entry to another entry in the rule. Categorized as PREDICTS (this → other), PREDICTED_BY (other → this), or EQUIV (bidirectional).
--     * Slot: id
--     * Slot: relationship Description: Type of relationship
--     * Slot: target_id Description: ID of the related entry
--     * Slot: containment Description: Containment score (0-1) for the directional relationship. For PREDICTS: this_in_target (how much of this is contained in target). For PREDICTED_BY: target_in_this (how much of target is contained in this). For EQUIV: max of both directions.
--     * Slot: jaccard_similarity Description: Jaccard similarity coefficient (0-1)
--     * Slot: intersection_count Description: Number of proteins in both this and target
--     * Slot: exclusive_count Description: Number of proteins exclusive to the "source" of the relationship. For PREDICTS: proteins in this but not target. For PREDICTED_BY: proteins in target but not this. For EQUIV: proteins in this but not target (A - B).
--     * Slot: RuleReviewEntry_id Description: Autocreated FK slot
-- # Class: InterPro2GORedundancy Description: Analysis of whether rule GO annotations are redundant with existing InterPro2GO mappings from the GO Consortium.
--     * Slot: id
--     * Slot: summary Description: Human-readable summary of redundancy analysis
-- # Class: RedundantAnnotation Description: A GO annotation that is redundant with an existing InterPro2GO mapping
--     * Slot: id
--     * Slot: go_id Description: GO term ID (e.g., GO:0004791)
--     * Slot: go_label Description: GO term label
--     * Slot: interpro_source Description: InterPro ID that already maps to this GO term in ipr2go
--     * Slot: interpro_label Description: InterPro domain label
--     * Slot: InterPro2GORedundancy_id Description: Autocreated FK slot
-- # Class: ParsimonyAssessment Description: Assessment of rule parsimony (simplicity vs complexity)
--     * Slot: id
--     * Slot: assessment Description: Parsimony assessment value
--     * Slot: notes Description: Notes on parsimony - e.g., which conditions are redundant
-- # Class: LiteratureSupportAssessment Description: Assessment of literature support for the rule
--     * Slot: id
--     * Slot: assessment Description: Level of literature support
--     * Slot: notes Description: Notes on literature support - key papers, gaps in evidence
-- # Class: ConditionOverlapAssessment Description: Assessment of overlap between rule conditions
--     * Slot: id
--     * Slot: assessment Description: Overlap assessment value
--     * Slot: notes Description: Notes on condition overlap - e.g., "IPR000001 and IPR000002 both represent the same structural domain" or "FunFam subsumes the InterPro entry"
-- # Class: GOSpecificityAssessment Description: Assessment of GO term specificity
--     * Slot: id
--     * Slot: assessment Description: Specificity assessment value
--     * Slot: notes Description: Notes on specificity - suggested alternative terms if too broad/narrow
-- # Class: TaxonomicScopeAssessment Description: Assessment of taxonomic restriction appropriateness
--     * Slot: id
--     * Slot: assessment Description: Taxonomic scope assessment value
--     * Slot: notes Description: Notes on taxonomic scope - suggested changes to taxon constraints
-- # Class: PredictionReview Description: Review of computational/ML predictions for a gene that are NOT in the curated GOA/UniProt annotations. This captures predictions from methods like DeepECTF, PANTHER/IBA, InterPro2GO, CLEAN, GloEC, MAPred, etc. and evaluates them against literature and bioinformatic evidence. Inspired by the systematic evaluation in de Crécy-Lagard et al. 2025 (PMID:40703034).
--     * Slot: id Description: UniProt accession for the gene product
--     * Slot: gene_symbol Description: Symbol of the gene
--     * Slot: description Description: Summary of the prediction review findings
--     * Slot: status Description: Overall status of the gene review
--     * Slot: locus_tag Description: Locus tag for the gene (e.g., b1267 for E. coli)
--     * Slot: taxon_id
-- # Class: PredictedAnnotation Description: A single computational prediction and its review. Each prediction comes from a specific method and predicts a term (EC number, GO term, etc.) for the gene.
--     * Slot: id
--     * Slot: source_method Description: Name of the prediction method (e.g., DeepECTF, PANTHER_IBA, InterPro2GO, CLEAN, GloEC, MAPred, ProteinInfer)
--     * Slot: source_version Description: Version or date of the prediction method
--     * Slot: source_reference_id Description: Reference for the prediction method or study (e.g., PMID:37820725 for the Kim et al. 2023 DeepECTF study)
--     * Slot: predicted_term_type Description: Type of predicted term (EC, GO_MF, GO_BP, GO_CC)
--     * Slot: PredictionReview_id Description: Autocreated FK slot
--     * Slot: predicted_term_id Description: The predicted term (GO term, EC number, etc.)
--     * Slot: review_id Description: Assessment of this prediction
-- # Class: PredictionAssessment Description: Assessment of a single computational prediction. Uses categories from de Crécy-Lagard et al. 2025 (PMID:40703034) plus extensions for GO predictions.
--     * Slot: id
--     * Slot: assessment Description: Assessment category for this prediction
--     * Slot: confidence_score Description: Confidence score following de Crécy-Lagard et al. 2025: 2 = concordant with evidence, 1 = uncertain, 0 = discordant with evidence
--     * Slot: error_type Description: Type of error that led to the incorrect prediction, following Table 1 of de Crécy-Lagard et al. 2025
--     * Slot: summary Description: Summary of the assessment rationale
-- # Class: GeneReview_aliases
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: aliases
-- # Class: GeneReview_tags
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: tags Description: Tags associated with the gene for categorization and organization
-- # Class: GeneReview_existing_annotations
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: existing_annotations_id
-- # Class: GeneReview_core_functions
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: core_functions_id
-- # Class: GeneReview_proposed_new_terms
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: proposed_new_terms_id Description: Proposed new ontology terms that should exist but don't
-- # Class: GeneReview_suggested_questions
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: suggested_questions_id Description: Suggested questions to ask experts about the gene. Only include if not obvious from the literature.
-- # Class: GeneReview_suggested_experiments
--     * Slot: GeneReview_id Description: Autocreated FK slot
--     * Slot: suggested_experiments_id
-- # Class: FunctionalIsoformMapping_ids
--     * Slot: FunctionalIsoformMapping_id Description: Autocreated FK slot
--     * Slot: ids Description: UniProt identifiers belonging to this functional class. For UNIPROT_ISOFORM: P19544-1, P19544-2, etc. For UNIPROT_CHAIN: PRO_0000024969, PRO_0000024970, etc.
-- # Class: Reference_findings
--     * Slot: Reference_id Description: Autocreated FK slot
--     * Slot: findings_id
-- # Class: FindingReview_superseded_by
--     * Slot: FindingReview_id Description: Autocreated FK slot
--     * Slot: superseded_by_id Description: Reference(s) that dispute, correct, or overturn this finding. Used together with finding_status DISPUTED or OVERTURNED.
-- # Class: ExistingAnnotation_extensions
--     * Slot: ExistingAnnotation_id Description: Autocreated FK slot
--     * Slot: extensions_id
-- # Class: ExistingAnnotation_supporting_entities
--     * Slot: ExistingAnnotation_id Description: Autocreated FK slot
--     * Slot: supporting_entities Description: IDs of the supporting entities
-- # Class: Review_additional_reference_ids
--     * Slot: Review_id Description: Autocreated FK slot
--     * Slot: additional_reference_ids_id Description: IDs of the references
-- # Class: Review_supported_by
--     * Slot: Review_id Description: Autocreated FK slot
--     * Slot: supported_by_id
-- # Class: CoreFunction_supported_by
--     * Slot: CoreFunction_id Description: Autocreated FK slot
--     * Slot: supported_by_id
-- # Class: ProposedOntologyTerm_supported_by
--     * Slot: ProposedOntologyTerm_id Description: Autocreated FK slot
--     * Slot: supported_by_id
-- # Class: KnowledgeGap_gap_kind
--     * Slot: KnowledgeGap_id Description: Autocreated FK slot
--     * Slot: gap_kind Description: The kind(s) of ignorance — biology, curation, and/or ontology — which determines who can resolve it. Multiple values denote a blend (e.g. a biology gap with an ontology shadow).
-- # Class: Question_experts
--     * Slot: Question_id Description: Autocreated FK slot
--     * Slot: experts Description: Experts to answer the question. These should be drawn from the authors of relevant publications already referenced. If no suitable experts are available, it's OK to leave this as an empty list!
-- # Class: RuleReview_suggested_modifications
--     * Slot: RuleReview_id Description: Autocreated FK slot
--     * Slot: suggested_modifications Description: Specific modifications suggested if action is MODIFY
-- # Class: RuleReview_supported_by
--     * Slot: RuleReview_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this review
-- # Class: RuleCondition_sample_proteins
--     * Slot: RuleCondition_id Description: Autocreated FK slot
--     * Slot: sample_proteins Description: Sample UniProt IDs matching this condition. Only included when protein_count < 20 to avoid bloating files. Limited to max 10 examples.
-- # Class: PairwiseOverlap_condition_a_in_sets
--     * Slot: PairwiseOverlap_id Description: Autocreated FK slot
--     * Slot: condition_a_in_sets Description: List of 1-based condition set indices where condition A appears
-- # Class: PairwiseOverlap_condition_b_in_sets
--     * Slot: PairwiseOverlap_id Description: Autocreated FK slot
--     * Slot: condition_b_in_sets Description: List of 1-based condition set indices where condition B appears
-- # Class: RuleReviewEntry_appears_in_condition_sets
--     * Slot: RuleReviewEntry_id Description: Autocreated FK slot
--     * Slot: appears_in_condition_sets Description: Which condition sets (1-based) contain this entry (for domain conditions only)
-- # Class: RuleReviewEntry_asserted_predicted_go_terms
--     * Slot: RuleReviewEntry_id Description: Autocreated FK slot
--     * Slot: asserted_predicted_go_terms Description: GO terms that this entry maps to via external mappings (e.g., ipr2go). Only populated for external entries not in the rule's condition sets.
-- # Class: InterPro2GORedundancy_novel_annotations
--     * Slot: InterPro2GORedundancy_id Description: Autocreated FK slot
--     * Slot: novel_annotations Description: GO IDs not found in InterPro2GO for any rule condition
-- # Class: ParsimonyAssessment_supported_by
--     * Slot: ParsimonyAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this assessment
-- # Class: LiteratureSupportAssessment_supported_by
--     * Slot: LiteratureSupportAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this assessment
-- # Class: ConditionOverlapAssessment_supported_by
--     * Slot: ConditionOverlapAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this assessment
-- # Class: GOSpecificityAssessment_supported_by
--     * Slot: GOSpecificityAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this assessment
-- # Class: TaxonomicScopeAssessment_supported_by
--     * Slot: TaxonomicScopeAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting text from literature for this assessment
-- # Class: PredictionReview_source_documents
--     * Slot: PredictionReview_id Description: Autocreated FK slot
--     * Slot: source_documents Description: Paths to supporting source documents (e.g., reasoning traces, raw model outputs) for provenance
-- # Class: PredictionAssessment_supported_by
--     * Slot: PredictionAssessment_id Description: Autocreated FK slot
--     * Slot: supported_by_id Description: Supporting evidence for the assessment

CREATE TABLE "GeneReview" (
	id TEXT NOT NULL,
	gene_symbol TEXT NOT NULL,
	product_type VARCHAR(13),
	status VARCHAR(11),
	description TEXT,
	taxon_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(taxon_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_GeneReview_id" ON "GeneReview" (id);
CREATE TABLE "FunctionalIsoform" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	type VARCHAR(20) NOT NULL,
	description TEXT NOT NULL,
	"GeneReview_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id)
);CREATE INDEX "ix_FunctionalIsoform_id" ON "FunctionalIsoform" (id);
CREATE TABLE "Term" (
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	description TEXT,
	ontology TEXT,
	"FunctionalIsoform_id" TEXT,
	"Review_id" INTEGER,
	"CoreFunction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FunctionalIsoform_id") REFERENCES "FunctionalIsoform" (id),
	FOREIGN KEY("Review_id") REFERENCES "Review" (id),
	FOREIGN KEY("CoreFunction_id") REFERENCES "CoreFunction" (id)
);CREATE INDEX "ix_Term_id" ON "Term" (id);
CREATE TABLE "ReferenceReview" (
	id INTEGER NOT NULL,
	relevance VARCHAR(6),
	correctness VARCHAR(16),
	review_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ReferenceReview_id" ON "ReferenceReview" (id);
CREATE TABLE "FindingReview" (
	id INTEGER NOT NULL,
	finding_status VARCHAR(12),
	review_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FindingReview_id" ON "FindingReview" (id);
CREATE TABLE "Descriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"MolecularFunctionDescriptor_id" INTEGER,
	"BiologicalProcessDescriptor_id" INTEGER,
	"ModuleNode_id" TEXT,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("MolecularFunctionDescriptor_id") REFERENCES "MolecularFunctionDescriptor" (id),
	FOREIGN KEY("BiologicalProcessDescriptor_id") REFERENCES "BiologicalProcessDescriptor" (id),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_Descriptor_id" ON "Descriptor" (id);
CREATE TABLE "CellularComponentDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleAnnoton_uid" INTEGER,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleAnnoton_uid") REFERENCES "ModuleAnnoton" (uid),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_CellularComponentDescriptor_id" ON "CellularComponentDescriptor" (id);
CREATE TABLE "MolecularFunctionDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	source_location_id INTEGER,
	destination_location_id INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(source_location_id) REFERENCES "CellularComponentDescriptor" (id),
	FOREIGN KEY(destination_location_id) REFERENCES "CellularComponentDescriptor" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_MolecularFunctionDescriptor_id" ON "MolecularFunctionDescriptor" (id);
CREATE TABLE "BiologicalProcessDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleAnnoton_uid" INTEGER,
	starts_with_id INTEGER,
	ends_with_id INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleAnnoton_uid") REFERENCES "ModuleAnnoton" (uid),
	FOREIGN KEY(starts_with_id) REFERENCES "Descriptor" (id),
	FOREIGN KEY(ends_with_id) REFERENCES "Descriptor" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_BiologicalProcessDescriptor_id" ON "BiologicalProcessDescriptor" (id);
CREATE TABLE "ModuleNode" (
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	module_type VARCHAR(21),
	description TEXT,
	notes TEXT,
	"ModuleVariantSet_uid" INTEGER,
	context_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleVariantSet_uid") REFERENCES "ModuleVariantSet" (uid),
	FOREIGN KEY(context_id) REFERENCES "ModuleContext" (id)
);CREATE INDEX "ix_ModuleNode_id" ON "ModuleNode" (id);
CREATE TABLE "ModuleVariantSet" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	label TEXT,
	axis TEXT,
	selection VARCHAR(12),
	notes TEXT,
	"ModuleNode_id" TEXT,
	PRIMARY KEY (uid),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id)
);CREATE INDEX "ix_ModuleVariantSet_uid" ON "ModuleVariantSet" (uid);
CREATE TABLE "ModuleAnnoton" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	label TEXT,
	role_description TEXT,
	notes TEXT,
	"ModuleNode_id" TEXT,
	participant_id INTEGER,
	function_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY(participant_id) REFERENCES "ParticipantSelector" (id),
	FOREIGN KEY(function_id) REFERENCES "MolecularFunctionDescriptor" (id)
);CREATE INDEX "ix_ModuleAnnoton_uid" ON "ModuleAnnoton" (uid);
CREATE TABLE "ParticipantSelector" (
	id INTEGER NOT NULL,
	selector_type VARCHAR(17) NOT NULL,
	description TEXT,
	notes TEXT,
	gene_id INTEGER,
	gene_product_id INTEGER,
	protein_complex_id INTEGER,
	family_id INTEGER,
	domain_id INTEGER,
	homolog_of_id INTEGER,
	ortholog_of_id INTEGER,
	required_function_id INTEGER,
	required_domain_id INTEGER,
	taxon_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(gene_id) REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY(gene_product_id) REFERENCES "GeneProductDescriptor" (id),
	FOREIGN KEY(protein_complex_id) REFERENCES "ProteinComplexDescriptor" (id),
	FOREIGN KEY(family_id) REFERENCES "FamilyDescriptor" (id),
	FOREIGN KEY(domain_id) REFERENCES "DomainDescriptor" (id),
	FOREIGN KEY(homolog_of_id) REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY(ortholog_of_id) REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY(required_function_id) REFERENCES "MolecularFunctionDescriptor" (id),
	FOREIGN KEY(required_domain_id) REFERENCES "DomainDescriptor" (id),
	FOREIGN KEY(taxon_id) REFERENCES "TaxonDescriptor" (id)
);CREATE INDEX "ix_ParticipantSelector_id" ON "ParticipantSelector" (id);
CREATE TABLE "ModuleContext" (
	id INTEGER NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ModuleContext_id" ON "ModuleContext" (id);
CREATE TABLE "Review" (
	id INTEGER NOT NULL,
	summary TEXT,
	action VARCHAR(22) NOT NULL,
	reason TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Review_id" ON "Review" (id);
CREATE TABLE "CoreFunction" (
	id INTEGER NOT NULL,
	description TEXT,
	molecular_function_id TEXT,
	contributes_to_molecular_function_id TEXT,
	in_complex_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(molecular_function_id) REFERENCES "Term" (id),
	FOREIGN KEY(contributes_to_molecular_function_id) REFERENCES "Term" (id),
	FOREIGN KEY(in_complex_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_CoreFunction_id" ON "CoreFunction" (id);
CREATE TABLE "Experiment" (
	id INTEGER NOT NULL,
	hypothesis TEXT,
	description TEXT NOT NULL,
	experiment_type TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Experiment_id" ON "Experiment" (id);
CREATE TABLE "Question" (
	id INTEGER NOT NULL,
	question TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Question_id" ON "Question" (id);
CREATE TABLE "InterPro2GORedundancy" (
	id INTEGER NOT NULL,
	summary TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_InterPro2GORedundancy_id" ON "InterPro2GORedundancy" (id);
CREATE TABLE "ParsimonyAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(14) NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ParsimonyAssessment_id" ON "ParsimonyAssessment" (id);
CREATE TABLE "LiteratureSupportAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(12) NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_LiteratureSupportAssessment_id" ON "LiteratureSupportAssessment" (id);
CREATE TABLE "ConditionOverlapAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(11) NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ConditionOverlapAssessment_id" ON "ConditionOverlapAssessment" (id);
CREATE TABLE "GOSpecificityAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(11) NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_GOSpecificityAssessment_id" ON "GOSpecificityAssessment" (id);
CREATE TABLE "TaxonomicScopeAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(11) NOT NULL,
	notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TaxonomicScopeAssessment_id" ON "TaxonomicScopeAssessment" (id);
CREATE TABLE "PredictionAssessment" (
	id INTEGER NOT NULL,
	assessment VARCHAR(3) NOT NULL,
	confidence_score INTEGER NOT NULL,
	error_type VARCHAR(29),
	summary TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_PredictionAssessment_id" ON "PredictionAssessment" (id);
CREATE TABLE "AlternativeProduct" (
	id TEXT NOT NULL,
	name TEXT,
	sequence_note TEXT,
	description TEXT,
	"GeneReview_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id)
);CREATE INDEX "ix_AlternativeProduct_id" ON "AlternativeProduct" (id);
CREATE TABLE "FunctionalIsoformMapping" (
	id INTEGER NOT NULL,
	type VARCHAR(15) NOT NULL,
	residues TEXT,
	"FunctionalIsoform_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FunctionalIsoform_id") REFERENCES "FunctionalIsoform" (id)
);CREATE INDEX "ix_FunctionalIsoformMapping_id" ON "FunctionalIsoformMapping" (id);
CREATE TABLE "Finding" (
	id INTEGER NOT NULL,
	statement TEXT,
	supporting_text TEXT,
	full_text_unavailable BOOLEAN,
	reference_section_type VARCHAR(22),
	finding_review_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(finding_review_id) REFERENCES "FindingReview" (id)
);CREATE INDEX "ix_Finding_id" ON "Finding" (id);
CREATE TABLE "ChemicalEntityDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_ChemicalEntityDescriptor_id" ON "ChemicalEntityDescriptor" (id);
CREATE TABLE "GeneDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_GeneDescriptor_id" ON "GeneDescriptor" (id);
CREATE TABLE "FamilyDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_FamilyDescriptor_id" ON "FamilyDescriptor" (id);
CREATE TABLE "DomainDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_DomainDescriptor_id" ON "DomainDescriptor" (id);
CREATE TABLE "ProteinComplexDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_ProteinComplexDescriptor_id" ON "ProteinComplexDescriptor" (id);
CREATE TABLE "CellTypeDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_CellTypeDescriptor_id" ON "CellTypeDescriptor" (id);
CREATE TABLE "AnatomicalEntityDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_AnatomicalEntityDescriptor_id" ON "AnatomicalEntityDescriptor" (id);
CREATE TABLE "DevelopmentalStageDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_DevelopmentalStageDescriptor_id" ON "DevelopmentalStageDescriptor" (id);
CREATE TABLE "TaxonDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"ModuleContext_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_TaxonDescriptor_id" ON "TaxonDescriptor" (id);
CREATE TABLE "RelationDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_RelationDescriptor_id" ON "RelationDescriptor" (id);
CREATE TABLE "ModuleReview" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	status TEXT,
	notes TEXT,
	module_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(module_id) REFERENCES "ModuleNode" (id)
);CREATE INDEX "ix_ModuleReview_id" ON "ModuleReview" (id);
CREATE TABLE "ModulePart" (
	id INTEGER NOT NULL,
	"order" INTEGER,
	role TEXT,
	optional BOOLEAN,
	notes TEXT,
	"ModuleNode_id" TEXT,
	node_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY(node_id) REFERENCES "ModuleNode" (id)
);CREATE INDEX "ix_ModulePart_id" ON "ModulePart" (id);
CREATE TABLE "AnnotationExtension" (
	id INTEGER NOT NULL,
	predicate TEXT NOT NULL,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_AnnotationExtension_id" ON "AnnotationExtension" (id);
CREATE TABLE "EmbeddedRule" (
	id INTEGER NOT NULL,
	rule_id TEXT NOT NULL,
	reviewed_protein_count INTEGER,
	unreviewed_protein_count INTEGER,
	created_date TEXT,
	modified_date TEXT,
	ipr2go_redundancy_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(ipr2go_redundancy_id) REFERENCES "InterPro2GORedundancy" (id)
);CREATE INDEX "ix_EmbeddedRule_id" ON "EmbeddedRule" (id);
CREATE TABLE "RedundantAnnotation" (
	id INTEGER NOT NULL,
	go_id TEXT NOT NULL,
	go_label TEXT,
	interpro_source TEXT NOT NULL,
	interpro_label TEXT,
	"InterPro2GORedundancy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InterPro2GORedundancy_id") REFERENCES "InterPro2GORedundancy" (id)
);CREATE INDEX "ix_RedundantAnnotation_id" ON "RedundantAnnotation" (id);
CREATE TABLE "PredictionReview" (
	id TEXT NOT NULL,
	gene_symbol TEXT NOT NULL,
	description TEXT,
	status VARCHAR(11),
	locus_tag TEXT,
	taxon_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(taxon_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_PredictionReview_id" ON "PredictionReview" (id);
CREATE TABLE "GeneReview_aliases" (
	"GeneReview_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("GeneReview_id", aliases),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id)
);CREATE INDEX "ix_GeneReview_aliases_aliases" ON "GeneReview_aliases" (aliases);CREATE INDEX "ix_GeneReview_aliases_GeneReview_id" ON "GeneReview_aliases" ("GeneReview_id");
CREATE TABLE "GeneReview_tags" (
	"GeneReview_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("GeneReview_id", tags),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id)
);CREATE INDEX "ix_GeneReview_tags_tags" ON "GeneReview_tags" (tags);CREATE INDEX "ix_GeneReview_tags_GeneReview_id" ON "GeneReview_tags" ("GeneReview_id");
CREATE TABLE "GeneReview_core_functions" (
	"GeneReview_id" TEXT,
	core_functions_id INTEGER,
	PRIMARY KEY ("GeneReview_id", core_functions_id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY(core_functions_id) REFERENCES "CoreFunction" (id)
);CREATE INDEX "ix_GeneReview_core_functions_GeneReview_id" ON "GeneReview_core_functions" ("GeneReview_id");CREATE INDEX "ix_GeneReview_core_functions_core_functions_id" ON "GeneReview_core_functions" (core_functions_id);
CREATE TABLE "GeneReview_suggested_questions" (
	"GeneReview_id" TEXT,
	suggested_questions_id INTEGER,
	PRIMARY KEY ("GeneReview_id", suggested_questions_id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY(suggested_questions_id) REFERENCES "Question" (id)
);CREATE INDEX "ix_GeneReview_suggested_questions_suggested_questions_id" ON "GeneReview_suggested_questions" (suggested_questions_id);CREATE INDEX "ix_GeneReview_suggested_questions_GeneReview_id" ON "GeneReview_suggested_questions" ("GeneReview_id");
CREATE TABLE "GeneReview_suggested_experiments" (
	"GeneReview_id" TEXT,
	suggested_experiments_id INTEGER,
	PRIMARY KEY ("GeneReview_id", suggested_experiments_id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY(suggested_experiments_id) REFERENCES "Experiment" (id)
);CREATE INDEX "ix_GeneReview_suggested_experiments_suggested_experiments_id" ON "GeneReview_suggested_experiments" (suggested_experiments_id);CREATE INDEX "ix_GeneReview_suggested_experiments_GeneReview_id" ON "GeneReview_suggested_experiments" ("GeneReview_id");
CREATE TABLE "Question_experts" (
	"Question_id" INTEGER,
	experts TEXT,
	PRIMARY KEY ("Question_id", experts),
	FOREIGN KEY("Question_id") REFERENCES "Question" (id)
);CREATE INDEX "ix_Question_experts_experts" ON "Question_experts" (experts);CREATE INDEX "ix_Question_experts_Question_id" ON "Question_experts" ("Question_id");
CREATE TABLE "InterPro2GORedundancy_novel_annotations" (
	"InterPro2GORedundancy_id" INTEGER,
	novel_annotations TEXT,
	PRIMARY KEY ("InterPro2GORedundancy_id", novel_annotations),
	FOREIGN KEY("InterPro2GORedundancy_id") REFERENCES "InterPro2GORedundancy" (id)
);CREATE INDEX "ix_InterPro2GORedundancy_novel_annotations_novel_annotations" ON "InterPro2GORedundancy_novel_annotations" (novel_annotations);CREATE INDEX "ix_InterPro2GORedundancy_novel_annotations_InterPro2GORedundancy_id" ON "InterPro2GORedundancy_novel_annotations" ("InterPro2GORedundancy_id");
CREATE TABLE "GeneProductDescriptor" (
	id INTEGER NOT NULL,
	preferred_term TEXT NOT NULL,
	description TEXT,
	notes TEXT,
	"FamilyDescriptor_id" INTEGER,
	term_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FamilyDescriptor_id") REFERENCES "FamilyDescriptor" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_GeneProductDescriptor_id" ON "GeneProductDescriptor" (id);
CREATE TABLE "ComplexUnit" (
	uid INTEGER NOT NULL,
	id TEXT,
	label TEXT,
	role TEXT,
	stoichiometry TEXT,
	notes TEXT,
	"ProteinComplexDescriptor_id" INTEGER,
	participant_id INTEGER,
	function_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ProteinComplexDescriptor_id") REFERENCES "ProteinComplexDescriptor" (id),
	FOREIGN KEY(participant_id) REFERENCES "ParticipantSelector" (id),
	FOREIGN KEY(function_id) REFERENCES "MolecularFunctionDescriptor" (id)
);CREATE INDEX "ix_ComplexUnit_uid" ON "ComplexUnit" (uid);
CREATE TABLE "ModuleConnection" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	target TEXT NOT NULL,
	connection_type VARCHAR(20),
	description TEXT,
	notes TEXT,
	"ModuleNode_id" TEXT,
	predicate_id INTEGER,
	context_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY(predicate_id) REFERENCES "RelationDescriptor" (id),
	FOREIGN KEY(context_id) REFERENCES "ModuleContext" (id)
);CREATE INDEX "ix_ModuleConnection_id" ON "ModuleConnection" (id);
CREATE TABLE "KnowledgeGap" (
	id INTEGER NOT NULL,
	gap_statement TEXT NOT NULL,
	boundary TEXT,
	dark_aspect VARCHAR(15),
	status VARCHAR(9),
	significance TEXT,
	resolution TEXT,
	"GeneReview_id" TEXT,
	"ModuleReview_id" TEXT,
	"ModuleNode_id" TEXT,
	"Review_id" INTEGER,
	"CoreFunction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY("ModuleReview_id") REFERENCES "ModuleReview" (id),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY("Review_id") REFERENCES "Review" (id),
	FOREIGN KEY("CoreFunction_id") REFERENCES "CoreFunction" (id)
);CREATE INDEX "ix_KnowledgeGap_id" ON "KnowledgeGap" (id);
CREATE TABLE "RuleReview" (
	id TEXT NOT NULL,
	description TEXT,
	status VARCHAR(11),
	rule_type VARCHAR(7) NOT NULL,
	review_summary TEXT,
	action VARCHAR(9) NOT NULL,
	action_rationale TEXT,
	confidence FLOAT,
	rule_id INTEGER NOT NULL,
	parsimony_id INTEGER,
	literature_support_id INTEGER,
	condition_overlap_id INTEGER,
	go_specificity_id INTEGER,
	taxonomic_scope_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(rule_id) REFERENCES "EmbeddedRule" (id),
	FOREIGN KEY(parsimony_id) REFERENCES "ParsimonyAssessment" (id),
	FOREIGN KEY(literature_support_id) REFERENCES "LiteratureSupportAssessment" (id),
	FOREIGN KEY(condition_overlap_id) REFERENCES "ConditionOverlapAssessment" (id),
	FOREIGN KEY(go_specificity_id) REFERENCES "GOSpecificityAssessment" (id),
	FOREIGN KEY(taxonomic_scope_id) REFERENCES "TaxonomicScopeAssessment" (id)
);CREATE INDEX "ix_RuleReview_id" ON "RuleReview" (id);
CREATE TABLE "RuleConditionSet" (
	id INTEGER NOT NULL,
	number INTEGER NOT NULL,
	notes TEXT,
	"EmbeddedRule_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("EmbeddedRule_id") REFERENCES "EmbeddedRule" (id)
);CREATE INDEX "ix_RuleConditionSet_id" ON "RuleConditionSet" (id);
CREATE TABLE "RuleGOAnnotation" (
	id INTEGER NOT NULL,
	go_id TEXT NOT NULL,
	go_label TEXT,
	aspect TEXT,
	"EmbeddedRule_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("EmbeddedRule_id") REFERENCES "EmbeddedRule" (id)
);CREATE INDEX "ix_RuleGOAnnotation_id" ON "RuleGOAnnotation" (id);
CREATE TABLE "RuleReviewEntry" (
	id TEXT NOT NULL,
	label TEXT,
	type VARCHAR(8) NOT NULL,
	protein_count INTEGER,
	source TEXT,
	"EmbeddedRule_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("EmbeddedRule_id") REFERENCES "EmbeddedRule" (id)
);CREATE INDEX "ix_RuleReviewEntry_id" ON "RuleReviewEntry" (id);
CREATE TABLE "PredictedAnnotation" (
	id INTEGER NOT NULL,
	source_method TEXT NOT NULL,
	source_version TEXT,
	source_reference_id TEXT,
	predicted_term_type VARCHAR(5) NOT NULL,
	"PredictionReview_id" TEXT,
	predicted_term_id TEXT NOT NULL,
	review_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("PredictionReview_id") REFERENCES "PredictionReview" (id),
	FOREIGN KEY(predicted_term_id) REFERENCES "Term" (id),
	FOREIGN KEY(review_id) REFERENCES "PredictionAssessment" (id)
);CREATE INDEX "ix_PredictedAnnotation_id" ON "PredictedAnnotation" (id);
CREATE TABLE "FunctionalIsoformMapping_ids" (
	"FunctionalIsoformMapping_id" INTEGER,
	ids TEXT NOT NULL,
	PRIMARY KEY ("FunctionalIsoformMapping_id", ids),
	FOREIGN KEY("FunctionalIsoformMapping_id") REFERENCES "FunctionalIsoformMapping" (id)
);CREATE INDEX "ix_FunctionalIsoformMapping_ids_ids" ON "FunctionalIsoformMapping_ids" (ids);CREATE INDEX "ix_FunctionalIsoformMapping_ids_FunctionalIsoformMapping_id" ON "FunctionalIsoformMapping_ids" ("FunctionalIsoformMapping_id");
CREATE TABLE "PredictionReview_source_documents" (
	"PredictionReview_id" TEXT,
	source_documents TEXT,
	PRIMARY KEY ("PredictionReview_id", source_documents),
	FOREIGN KEY("PredictionReview_id") REFERENCES "PredictionReview" (id)
);CREATE INDEX "ix_PredictionReview_source_documents_source_documents" ON "PredictionReview_source_documents" (source_documents);CREATE INDEX "ix_PredictionReview_source_documents_PredictionReview_id" ON "PredictionReview_source_documents" ("PredictionReview_id");
CREATE TABLE "Reference" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	is_invalid BOOLEAN,
	publication_type VARCHAR(17),
	full_text_unavailable BOOLEAN,
	"GeneReview_id" TEXT,
	"ModuleReview_id" TEXT,
	"RuleReview_id" TEXT,
	"PredictionReview_id" TEXT,
	reference_review_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY("ModuleReview_id") REFERENCES "ModuleReview" (id),
	FOREIGN KEY("RuleReview_id") REFERENCES "RuleReview" (id),
	FOREIGN KEY("PredictionReview_id") REFERENCES "PredictionReview" (id),
	FOREIGN KEY(reference_review_id) REFERENCES "ReferenceReview" (id)
);CREATE INDEX "ix_Reference_id" ON "Reference" (id);
CREATE TABLE "EvidenceItem" (
	id INTEGER NOT NULL,
	source_id TEXT NOT NULL,
	title TEXT,
	statement TEXT,
	supporting_text TEXT,
	url TEXT,
	notes TEXT,
	"Descriptor_id" INTEGER,
	"ChemicalEntityDescriptor_id" INTEGER,
	"GeneDescriptor_id" INTEGER,
	"GeneProductDescriptor_id" INTEGER,
	"FamilyDescriptor_id" INTEGER,
	"DomainDescriptor_id" INTEGER,
	"CellularComponentDescriptor_id" INTEGER,
	"ProteinComplexDescriptor_id" INTEGER,
	"ComplexUnit_uid" INTEGER,
	"CellTypeDescriptor_id" INTEGER,
	"AnatomicalEntityDescriptor_id" INTEGER,
	"DevelopmentalStageDescriptor_id" INTEGER,
	"TaxonDescriptor_id" INTEGER,
	"MolecularFunctionDescriptor_id" INTEGER,
	"BiologicalProcessDescriptor_id" INTEGER,
	"RelationDescriptor_id" INTEGER,
	"ModuleReview_id" TEXT,
	"ModuleNode_id" TEXT,
	"ModulePart_id" INTEGER,
	"ModuleVariantSet_uid" INTEGER,
	"ModuleAnnoton_uid" INTEGER,
	"ParticipantSelector_id" INTEGER,
	"ModuleContext_id" INTEGER,
	"ModuleConnection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Descriptor_id") REFERENCES "Descriptor" (id),
	FOREIGN KEY("ChemicalEntityDescriptor_id") REFERENCES "ChemicalEntityDescriptor" (id),
	FOREIGN KEY("GeneDescriptor_id") REFERENCES "GeneDescriptor" (id),
	FOREIGN KEY("GeneProductDescriptor_id") REFERENCES "GeneProductDescriptor" (id),
	FOREIGN KEY("FamilyDescriptor_id") REFERENCES "FamilyDescriptor" (id),
	FOREIGN KEY("DomainDescriptor_id") REFERENCES "DomainDescriptor" (id),
	FOREIGN KEY("CellularComponentDescriptor_id") REFERENCES "CellularComponentDescriptor" (id),
	FOREIGN KEY("ProteinComplexDescriptor_id") REFERENCES "ProteinComplexDescriptor" (id),
	FOREIGN KEY("ComplexUnit_uid") REFERENCES "ComplexUnit" (uid),
	FOREIGN KEY("CellTypeDescriptor_id") REFERENCES "CellTypeDescriptor" (id),
	FOREIGN KEY("AnatomicalEntityDescriptor_id") REFERENCES "AnatomicalEntityDescriptor" (id),
	FOREIGN KEY("DevelopmentalStageDescriptor_id") REFERENCES "DevelopmentalStageDescriptor" (id),
	FOREIGN KEY("TaxonDescriptor_id") REFERENCES "TaxonDescriptor" (id),
	FOREIGN KEY("MolecularFunctionDescriptor_id") REFERENCES "MolecularFunctionDescriptor" (id),
	FOREIGN KEY("BiologicalProcessDescriptor_id") REFERENCES "BiologicalProcessDescriptor" (id),
	FOREIGN KEY("RelationDescriptor_id") REFERENCES "RelationDescriptor" (id),
	FOREIGN KEY("ModuleReview_id") REFERENCES "ModuleReview" (id),
	FOREIGN KEY("ModuleNode_id") REFERENCES "ModuleNode" (id),
	FOREIGN KEY("ModulePart_id") REFERENCES "ModulePart" (id),
	FOREIGN KEY("ModuleVariantSet_uid") REFERENCES "ModuleVariantSet" (uid),
	FOREIGN KEY("ModuleAnnoton_uid") REFERENCES "ModuleAnnoton" (uid),
	FOREIGN KEY("ParticipantSelector_id") REFERENCES "ParticipantSelector" (id),
	FOREIGN KEY("ModuleContext_id") REFERENCES "ModuleContext" (id),
	FOREIGN KEY("ModuleConnection_id") REFERENCES "ModuleConnection" (id)
);CREATE INDEX "ix_EvidenceItem_id" ON "EvidenceItem" (id);
CREATE TABLE "ProposedOntologyTerm" (
	id INTEGER NOT NULL,
	proposed_name TEXT NOT NULL,
	proposed_definition TEXT NOT NULL,
	justification TEXT,
	"KnowledgeGap_id" INTEGER,
	proposed_parent_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("KnowledgeGap_id") REFERENCES "KnowledgeGap" (id),
	FOREIGN KEY(proposed_parent_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_ProposedOntologyTerm_id" ON "ProposedOntologyTerm" (id);
CREATE TABLE "RuleCondition" (
	id INTEGER NOT NULL,
	condition_type VARCHAR(15) NOT NULL,
	value TEXT NOT NULL,
	curie TEXT,
	label TEXT,
	interpro_type VARCHAR(22),
	negated BOOLEAN,
	protein_count INTEGER,
	protein_database VARCHAR(9),
	uniqueness_score FLOAT,
	"RuleConditionSet_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RuleConditionSet_id") REFERENCES "RuleConditionSet" (id)
);CREATE INDEX "ix_RuleCondition_id" ON "RuleCondition" (id);
CREATE TABLE "PairwiseOverlap" (
	id INTEGER NOT NULL,
	condition_a TEXT NOT NULL,
	condition_b TEXT NOT NULL,
	condition_a_label TEXT,
	condition_b_label TEXT,
	protein_database VARCHAR(9) NOT NULL,
	count_a INTEGER NOT NULL,
	count_b INTEGER NOT NULL,
	intersection_count INTEGER NOT NULL,
	a_minus_b_count INTEGER NOT NULL,
	b_minus_a_count INTEGER NOT NULL,
	jaccard_similarity FLOAT NOT NULL,
	containment_a_in_b FLOAT NOT NULL,
	containment_b_in_a FLOAT NOT NULL,
	interpretation VARCHAR(12),
	"RuleConditionSet_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RuleConditionSet_id") REFERENCES "RuleConditionSet" (id)
);CREATE INDEX "ix_PairwiseOverlap_id" ON "PairwiseOverlap" (id);
CREATE TABLE "RelatedEntry" (
	id INTEGER NOT NULL,
	relationship VARCHAR(12) NOT NULL,
	target_id TEXT NOT NULL,
	containment FLOAT,
	jaccard_similarity FLOAT,
	intersection_count INTEGER,
	exclusive_count INTEGER,
	"RuleReviewEntry_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("RuleReviewEntry_id") REFERENCES "RuleReviewEntry" (id)
);CREATE INDEX "ix_RelatedEntry_id" ON "RelatedEntry" (id);
CREATE TABLE "KnowledgeGap_gap_kind" (
	"KnowledgeGap_id" INTEGER,
	gap_kind VARCHAR(8),
	PRIMARY KEY ("KnowledgeGap_id", gap_kind),
	FOREIGN KEY("KnowledgeGap_id") REFERENCES "KnowledgeGap" (id)
);CREATE INDEX "ix_KnowledgeGap_gap_kind_gap_kind" ON "KnowledgeGap_gap_kind" (gap_kind);CREATE INDEX "ix_KnowledgeGap_gap_kind_KnowledgeGap_id" ON "KnowledgeGap_gap_kind" ("KnowledgeGap_id");
CREATE TABLE "RuleReview_suggested_modifications" (
	"RuleReview_id" TEXT,
	suggested_modifications TEXT,
	PRIMARY KEY ("RuleReview_id", suggested_modifications),
	FOREIGN KEY("RuleReview_id") REFERENCES "RuleReview" (id)
);CREATE INDEX "ix_RuleReview_suggested_modifications_RuleReview_id" ON "RuleReview_suggested_modifications" ("RuleReview_id");CREATE INDEX "ix_RuleReview_suggested_modifications_suggested_modifications" ON "RuleReview_suggested_modifications" (suggested_modifications);
CREATE TABLE "RuleReviewEntry_appears_in_condition_sets" (
	"RuleReviewEntry_id" TEXT,
	appears_in_condition_sets INTEGER,
	PRIMARY KEY ("RuleReviewEntry_id", appears_in_condition_sets),
	FOREIGN KEY("RuleReviewEntry_id") REFERENCES "RuleReviewEntry" (id)
);CREATE INDEX "ix_RuleReviewEntry_appears_in_condition_sets_appears_in_condition_sets" ON "RuleReviewEntry_appears_in_condition_sets" (appears_in_condition_sets);CREATE INDEX "ix_RuleReviewEntry_appears_in_condition_sets_RuleReviewEntry_id" ON "RuleReviewEntry_appears_in_condition_sets" ("RuleReviewEntry_id");
CREATE TABLE "RuleReviewEntry_asserted_predicted_go_terms" (
	"RuleReviewEntry_id" TEXT,
	asserted_predicted_go_terms TEXT,
	PRIMARY KEY ("RuleReviewEntry_id", asserted_predicted_go_terms),
	FOREIGN KEY("RuleReviewEntry_id") REFERENCES "RuleReviewEntry" (id)
);CREATE INDEX "ix_RuleReviewEntry_asserted_predicted_go_terms_RuleReviewEntry_id" ON "RuleReviewEntry_asserted_predicted_go_terms" ("RuleReviewEntry_id");CREATE INDEX "ix_RuleReviewEntry_asserted_predicted_go_terms_asserted_predicted_go_terms" ON "RuleReviewEntry_asserted_predicted_go_terms" (asserted_predicted_go_terms);
CREATE TABLE "SupportingTextInReference" (
	id INTEGER NOT NULL,
	reference_id TEXT NOT NULL,
	supporting_text TEXT,
	supporting_text_fulltext TEXT,
	full_text_unavailable BOOLEAN,
	reference_section_type VARCHAR(22),
	"KnowledgeGap_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(reference_id) REFERENCES "Reference" (id),
	FOREIGN KEY("KnowledgeGap_id") REFERENCES "KnowledgeGap" (id)
);CREATE INDEX "ix_SupportingTextInReference_id" ON "SupportingTextInReference" (id);
CREATE TABLE "ExistingAnnotation" (
	id INTEGER NOT NULL,
	qualifier VARCHAR(42),
	negated BOOLEAN,
	evidence_type VARCHAR(3) NOT NULL,
	original_reference_id TEXT,
	retired BOOLEAN,
	isoform TEXT,
	term_id TEXT,
	review_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(original_reference_id) REFERENCES "Reference" (id),
	FOREIGN KEY(term_id) REFERENCES "Term" (id),
	FOREIGN KEY(review_id) REFERENCES "Review" (id)
);CREATE INDEX "ix_ExistingAnnotation_id" ON "ExistingAnnotation" (id);
CREATE TABLE "TermMapping" (
	id INTEGER NOT NULL,
	predicate TEXT NOT NULL,
	"ProposedOntologyTerm_id" INTEGER,
	target_term_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("ProposedOntologyTerm_id") REFERENCES "ProposedOntologyTerm" (id),
	FOREIGN KEY(target_term_id) REFERENCES "Term" (id)
);CREATE INDEX "ix_TermMapping_id" ON "TermMapping" (id);
CREATE TABLE "GeneReview_proposed_new_terms" (
	"GeneReview_id" TEXT,
	proposed_new_terms_id INTEGER,
	PRIMARY KEY ("GeneReview_id", proposed_new_terms_id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY(proposed_new_terms_id) REFERENCES "ProposedOntologyTerm" (id)
);CREATE INDEX "ix_GeneReview_proposed_new_terms_GeneReview_id" ON "GeneReview_proposed_new_terms" ("GeneReview_id");CREATE INDEX "ix_GeneReview_proposed_new_terms_proposed_new_terms_id" ON "GeneReview_proposed_new_terms" (proposed_new_terms_id);
CREATE TABLE "Reference_findings" (
	"Reference_id" TEXT,
	findings_id INTEGER,
	PRIMARY KEY ("Reference_id", findings_id),
	FOREIGN KEY("Reference_id") REFERENCES "Reference" (id),
	FOREIGN KEY(findings_id) REFERENCES "Finding" (id)
);CREATE INDEX "ix_Reference_findings_Reference_id" ON "Reference_findings" ("Reference_id");CREATE INDEX "ix_Reference_findings_findings_id" ON "Reference_findings" (findings_id);
CREATE TABLE "FindingReview_superseded_by" (
	"FindingReview_id" INTEGER,
	superseded_by_id TEXT,
	PRIMARY KEY ("FindingReview_id", superseded_by_id),
	FOREIGN KEY("FindingReview_id") REFERENCES "FindingReview" (id),
	FOREIGN KEY(superseded_by_id) REFERENCES "Reference" (id)
);CREATE INDEX "ix_FindingReview_superseded_by_FindingReview_id" ON "FindingReview_superseded_by" ("FindingReview_id");CREATE INDEX "ix_FindingReview_superseded_by_superseded_by_id" ON "FindingReview_superseded_by" (superseded_by_id);
CREATE TABLE "Review_additional_reference_ids" (
	"Review_id" INTEGER,
	additional_reference_ids_id TEXT,
	PRIMARY KEY ("Review_id", additional_reference_ids_id),
	FOREIGN KEY("Review_id") REFERENCES "Review" (id),
	FOREIGN KEY(additional_reference_ids_id) REFERENCES "Reference" (id)
);CREATE INDEX "ix_Review_additional_reference_ids_Review_id" ON "Review_additional_reference_ids" ("Review_id");CREATE INDEX "ix_Review_additional_reference_ids_additional_reference_ids_id" ON "Review_additional_reference_ids" (additional_reference_ids_id);
CREATE TABLE "RuleCondition_sample_proteins" (
	"RuleCondition_id" INTEGER,
	sample_proteins TEXT,
	PRIMARY KEY ("RuleCondition_id", sample_proteins),
	FOREIGN KEY("RuleCondition_id") REFERENCES "RuleCondition" (id)
);CREATE INDEX "ix_RuleCondition_sample_proteins_RuleCondition_id" ON "RuleCondition_sample_proteins" ("RuleCondition_id");CREATE INDEX "ix_RuleCondition_sample_proteins_sample_proteins" ON "RuleCondition_sample_proteins" (sample_proteins);
CREATE TABLE "PairwiseOverlap_condition_a_in_sets" (
	"PairwiseOverlap_id" INTEGER,
	condition_a_in_sets INTEGER,
	PRIMARY KEY ("PairwiseOverlap_id", condition_a_in_sets),
	FOREIGN KEY("PairwiseOverlap_id") REFERENCES "PairwiseOverlap" (id)
);CREATE INDEX "ix_PairwiseOverlap_condition_a_in_sets_condition_a_in_sets" ON "PairwiseOverlap_condition_a_in_sets" (condition_a_in_sets);CREATE INDEX "ix_PairwiseOverlap_condition_a_in_sets_PairwiseOverlap_id" ON "PairwiseOverlap_condition_a_in_sets" ("PairwiseOverlap_id");
CREATE TABLE "PairwiseOverlap_condition_b_in_sets" (
	"PairwiseOverlap_id" INTEGER,
	condition_b_in_sets INTEGER,
	PRIMARY KEY ("PairwiseOverlap_id", condition_b_in_sets),
	FOREIGN KEY("PairwiseOverlap_id") REFERENCES "PairwiseOverlap" (id)
);CREATE INDEX "ix_PairwiseOverlap_condition_b_in_sets_PairwiseOverlap_id" ON "PairwiseOverlap_condition_b_in_sets" ("PairwiseOverlap_id");CREATE INDEX "ix_PairwiseOverlap_condition_b_in_sets_condition_b_in_sets" ON "PairwiseOverlap_condition_b_in_sets" (condition_b_in_sets);
CREATE TABLE "GeneReview_existing_annotations" (
	"GeneReview_id" TEXT,
	existing_annotations_id INTEGER,
	PRIMARY KEY ("GeneReview_id", existing_annotations_id),
	FOREIGN KEY("GeneReview_id") REFERENCES "GeneReview" (id),
	FOREIGN KEY(existing_annotations_id) REFERENCES "ExistingAnnotation" (id)
);CREATE INDEX "ix_GeneReview_existing_annotations_GeneReview_id" ON "GeneReview_existing_annotations" ("GeneReview_id");CREATE INDEX "ix_GeneReview_existing_annotations_existing_annotations_id" ON "GeneReview_existing_annotations" (existing_annotations_id);
CREATE TABLE "ExistingAnnotation_extensions" (
	"ExistingAnnotation_id" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("ExistingAnnotation_id", extensions_id),
	FOREIGN KEY("ExistingAnnotation_id") REFERENCES "ExistingAnnotation" (id),
	FOREIGN KEY(extensions_id) REFERENCES "AnnotationExtension" (id)
);CREATE INDEX "ix_ExistingAnnotation_extensions_ExistingAnnotation_id" ON "ExistingAnnotation_extensions" ("ExistingAnnotation_id");CREATE INDEX "ix_ExistingAnnotation_extensions_extensions_id" ON "ExistingAnnotation_extensions" (extensions_id);
CREATE TABLE "ExistingAnnotation_supporting_entities" (
	"ExistingAnnotation_id" INTEGER,
	supporting_entities TEXT,
	PRIMARY KEY ("ExistingAnnotation_id", supporting_entities),
	FOREIGN KEY("ExistingAnnotation_id") REFERENCES "ExistingAnnotation" (id)
);CREATE INDEX "ix_ExistingAnnotation_supporting_entities_ExistingAnnotation_id" ON "ExistingAnnotation_supporting_entities" ("ExistingAnnotation_id");CREATE INDEX "ix_ExistingAnnotation_supporting_entities_supporting_entities" ON "ExistingAnnotation_supporting_entities" (supporting_entities);
CREATE TABLE "Review_supported_by" (
	"Review_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("Review_id", supported_by_id),
	FOREIGN KEY("Review_id") REFERENCES "Review" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_Review_supported_by_supported_by_id" ON "Review_supported_by" (supported_by_id);CREATE INDEX "ix_Review_supported_by_Review_id" ON "Review_supported_by" ("Review_id");
CREATE TABLE "CoreFunction_supported_by" (
	"CoreFunction_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("CoreFunction_id", supported_by_id),
	FOREIGN KEY("CoreFunction_id") REFERENCES "CoreFunction" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_CoreFunction_supported_by_supported_by_id" ON "CoreFunction_supported_by" (supported_by_id);CREATE INDEX "ix_CoreFunction_supported_by_CoreFunction_id" ON "CoreFunction_supported_by" ("CoreFunction_id");
CREATE TABLE "ProposedOntologyTerm_supported_by" (
	"ProposedOntologyTerm_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("ProposedOntologyTerm_id", supported_by_id),
	FOREIGN KEY("ProposedOntologyTerm_id") REFERENCES "ProposedOntologyTerm" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_ProposedOntologyTerm_supported_by_ProposedOntologyTerm_id" ON "ProposedOntologyTerm_supported_by" ("ProposedOntologyTerm_id");CREATE INDEX "ix_ProposedOntologyTerm_supported_by_supported_by_id" ON "ProposedOntologyTerm_supported_by" (supported_by_id);
CREATE TABLE "RuleReview_supported_by" (
	"RuleReview_id" TEXT,
	supported_by_id INTEGER,
	PRIMARY KEY ("RuleReview_id", supported_by_id),
	FOREIGN KEY("RuleReview_id") REFERENCES "RuleReview" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_RuleReview_supported_by_supported_by_id" ON "RuleReview_supported_by" (supported_by_id);CREATE INDEX "ix_RuleReview_supported_by_RuleReview_id" ON "RuleReview_supported_by" ("RuleReview_id");
CREATE TABLE "ParsimonyAssessment_supported_by" (
	"ParsimonyAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("ParsimonyAssessment_id", supported_by_id),
	FOREIGN KEY("ParsimonyAssessment_id") REFERENCES "ParsimonyAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_ParsimonyAssessment_supported_by_supported_by_id" ON "ParsimonyAssessment_supported_by" (supported_by_id);CREATE INDEX "ix_ParsimonyAssessment_supported_by_ParsimonyAssessment_id" ON "ParsimonyAssessment_supported_by" ("ParsimonyAssessment_id");
CREATE TABLE "LiteratureSupportAssessment_supported_by" (
	"LiteratureSupportAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("LiteratureSupportAssessment_id", supported_by_id),
	FOREIGN KEY("LiteratureSupportAssessment_id") REFERENCES "LiteratureSupportAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_LiteratureSupportAssessment_supported_by_supported_by_id" ON "LiteratureSupportAssessment_supported_by" (supported_by_id);CREATE INDEX "ix_LiteratureSupportAssessment_supported_by_LiteratureSupportAssessment_id" ON "LiteratureSupportAssessment_supported_by" ("LiteratureSupportAssessment_id");
CREATE TABLE "ConditionOverlapAssessment_supported_by" (
	"ConditionOverlapAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("ConditionOverlapAssessment_id", supported_by_id),
	FOREIGN KEY("ConditionOverlapAssessment_id") REFERENCES "ConditionOverlapAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_ConditionOverlapAssessment_supported_by_ConditionOverlapAssessment_id" ON "ConditionOverlapAssessment_supported_by" ("ConditionOverlapAssessment_id");CREATE INDEX "ix_ConditionOverlapAssessment_supported_by_supported_by_id" ON "ConditionOverlapAssessment_supported_by" (supported_by_id);
CREATE TABLE "GOSpecificityAssessment_supported_by" (
	"GOSpecificityAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("GOSpecificityAssessment_id", supported_by_id),
	FOREIGN KEY("GOSpecificityAssessment_id") REFERENCES "GOSpecificityAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_GOSpecificityAssessment_supported_by_GOSpecificityAssessment_id" ON "GOSpecificityAssessment_supported_by" ("GOSpecificityAssessment_id");CREATE INDEX "ix_GOSpecificityAssessment_supported_by_supported_by_id" ON "GOSpecificityAssessment_supported_by" (supported_by_id);
CREATE TABLE "TaxonomicScopeAssessment_supported_by" (
	"TaxonomicScopeAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("TaxonomicScopeAssessment_id", supported_by_id),
	FOREIGN KEY("TaxonomicScopeAssessment_id") REFERENCES "TaxonomicScopeAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_TaxonomicScopeAssessment_supported_by_TaxonomicScopeAssessment_id" ON "TaxonomicScopeAssessment_supported_by" ("TaxonomicScopeAssessment_id");CREATE INDEX "ix_TaxonomicScopeAssessment_supported_by_supported_by_id" ON "TaxonomicScopeAssessment_supported_by" (supported_by_id);
CREATE TABLE "PredictionAssessment_supported_by" (
	"PredictionAssessment_id" INTEGER,
	supported_by_id INTEGER,
	PRIMARY KEY ("PredictionAssessment_id", supported_by_id),
	FOREIGN KEY("PredictionAssessment_id") REFERENCES "PredictionAssessment" (id),
	FOREIGN KEY(supported_by_id) REFERENCES "SupportingTextInReference" (id)
);CREATE INDEX "ix_PredictionAssessment_supported_by_PredictionAssessment_id" ON "PredictionAssessment_supported_by" ("PredictionAssessment_id");CREATE INDEX "ix_PredictionAssessment_supported_by_supported_by_id" ON "PredictionAssessment_supported_by" (supported_by_id);
