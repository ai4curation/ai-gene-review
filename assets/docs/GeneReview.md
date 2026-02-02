
# Class: GeneReview

Complete review for a gene

URI: [gene_review:GeneReview](https://w3id.org/ai4curation/gene_review/GeneReview)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Reference],[Question],[ProposedOntologyTerm],[Experiment]<suggested_experiments%200..*-++[GeneReview&#124;id:string;gene_symbol:string;product_type:ProductTypeEnum%20%3F;aliases:string%20*;tags:string%20*;status:GeneReviewStatusEnum%20%3F;description:string%20%3F],[Question]<suggested_questions%200..*-++[GeneReview],[ProposedOntologyTerm]<proposed_new_terms%200..*-++[GeneReview],[CoreFunction]<core_functions%200..*-++[GeneReview],[ExistingAnnotation]<existing_annotations%200..*-++[GeneReview],[Reference]<references%200..*-++[GeneReview],[FunctionalIsoform]<functional_isoforms%200..*-++[GeneReview],[AlternativeProduct]<alternative_products%200..*-++[GeneReview],[Term]<taxon%201..1-++[GeneReview],[FunctionalIsoform],[Experiment],[ExistingAnnotation],[CoreFunction],[AlternativeProduct])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Reference],[Question],[ProposedOntologyTerm],[Experiment]<suggested_experiments%200..*-++[GeneReview&#124;id:string;gene_symbol:string;product_type:ProductTypeEnum%20%3F;aliases:string%20*;tags:string%20*;status:GeneReviewStatusEnum%20%3F;description:string%20%3F],[Question]<suggested_questions%200..*-++[GeneReview],[ProposedOntologyTerm]<proposed_new_terms%200..*-++[GeneReview],[CoreFunction]<core_functions%200..*-++[GeneReview],[ExistingAnnotation]<existing_annotations%200..*-++[GeneReview],[Reference]<references%200..*-++[GeneReview],[FunctionalIsoform]<functional_isoforms%200..*-++[GeneReview],[AlternativeProduct]<alternative_products%200..*-++[GeneReview],[Term]<taxon%201..1-++[GeneReview],[FunctionalIsoform],[Experiment],[ExistingAnnotation],[CoreFunction],[AlternativeProduct])

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [gene_symbol](gene_symbol.md)  <sub>1..1</sub>
     * Description: Symbol of the gene
     * Range: [String](types/String.md)
 * [product_type](product_type.md)  <sub>0..1</sub>
     * Description: Type of gene product (protein, ncRNA, etc.)
     * Range: [ProductTypeEnum](ProductTypeEnum.md)
 * [aliases](aliases.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [tags](tags.md)  <sub>0..\*</sub>
     * Description: Tags associated with the gene for categorization and organization
     * Range: [String](types/String.md)
 * [status](status.md)  <sub>0..1</sub>
     * Description: Overall status of the gene review
     * Range: [GeneReviewStatusEnum](GeneReviewStatusEnum.md)
 * [GeneReview➞description](GeneReview_description.md)  <sub>0..1</sub>
     * Description: Description of the entity
     * Range: [String](types/String.md)
 * [taxon](taxon.md)  <sub>1..1</sub>
     * Range: [Term](Term.md)
 * [alternative_products](alternative_products.md)  <sub>0..\*</sub>
     * Description: Alternative splicing products (isoforms) of the gene. Seeded from UniProt ALTERNATIVE PRODUCTS section. Only populated if there are multiple isoforms. Use this to document isoform-specific functions and biology. DEPRECATED: Use functional_isoforms instead for curated functional classes.
     * Range: [AlternativeProduct](AlternativeProduct.md)
 * [functional_isoforms](functional_isoforms.md)  <sub>0..\*</sub>
     * Description: Curated functional isoform classes for the gene. Unlike alternative_products (which is seeded from UniProt), this field is purely curator/agent-defined to capture FUNCTIONALLY RELEVANT distinctions. Examples: - Splice classes that group multiple UniProt isoforms (e.g., WT1 +KTS vs -KTS) - Cleavage products from polyproteins (e.g., POMC peptides) - Modification states with distinct functions Only populate when there ARE functionally distinct forms worth documenting.
     * Range: [FunctionalIsoform](FunctionalIsoform.md)
 * [references](references.md)  <sub>0..\*</sub>
     * Range: [Reference](Reference.md)
 * [existing_annotations](existing_annotations.md)  <sub>0..\*</sub>
     * Range: [ExistingAnnotation](ExistingAnnotation.md)
 * [core_functions](core_functions.md)  <sub>0..\*</sub>
     * Range: [CoreFunction](CoreFunction.md)
 * [proposed_new_terms](proposed_new_terms.md)  <sub>0..\*</sub>
     * Description: Proposed new ontology terms that should exist but don't
     * Range: [ProposedOntologyTerm](ProposedOntologyTerm.md)
 * [suggested_questions](suggested_questions.md)  <sub>0..\*</sub>
     * Description: Suggested questions to ask experts about the gene. Only include if not obvious from the literature.
     * Range: [Question](Question.md)
 * [suggested_experiments](suggested_experiments.md)  <sub>0..\*</sub>
     * Range: [Experiment](Experiment.md)
