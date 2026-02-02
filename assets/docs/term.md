
# Class: Term

A term in a specific ontology

URI: [gene_review:Term](https://w3id.org/ai4curation/gene_review/Term)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExistingAnnotation]++-%20term%200..1>[Term&#124;id:string;label:string;description:string%20%3F;ontology:string%20%3F],[CoreFunction]++-%20anatomical_locations%200..*>[Term],[CoreFunction]++-%20directly_involved_in%200..*>[Term],[CoreFunction]++-%20in_complex%200..1>[Term],[CoreFunction]++-%20locations%200..*>[Term],[CoreFunction]++-%20molecular_function%201..1>[Term],[CoreFunction]++-%20substrates%200..*>[Term],[FunctionalIsoform]++-%20isoform_specific_terms%200..*>[Term],[ProposedOntologyTerm]++-%20proposed_parent%200..1>[Term],[Review]++-%20proposed_replacement_terms%200..*>[Term],[GeneReview]++-%20taxon%201..1>[Term],[ExistingAnnotation]++-%20term(i)%200..1>[Term],[AnnotationExtension]++-%20term%200..1>[Term],[TermMapping]++-%20target_term%201..1>[Term],[TermMapping],[Review],[ProposedOntologyTerm],[GeneReview],[FunctionalIsoform],[ExistingAnnotation],[CoreFunction],[AnnotationExtension])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExistingAnnotation]++-%20term%200..1>[Term&#124;id:string;label:string;description:string%20%3F;ontology:string%20%3F],[CoreFunction]++-%20anatomical_locations%200..*>[Term],[CoreFunction]++-%20directly_involved_in%200..*>[Term],[CoreFunction]++-%20in_complex%200..1>[Term],[CoreFunction]++-%20locations%200..*>[Term],[CoreFunction]++-%20molecular_function%201..1>[Term],[CoreFunction]++-%20substrates%200..*>[Term],[FunctionalIsoform]++-%20isoform_specific_terms%200..*>[Term],[ProposedOntologyTerm]++-%20proposed_parent%200..1>[Term],[Review]++-%20proposed_replacement_terms%200..*>[Term],[GeneReview]++-%20taxon%201..1>[Term],[ExistingAnnotation]++-%20term(i)%200..1>[Term],[AnnotationExtension]++-%20term%200..1>[Term],[TermMapping]++-%20target_term%201..1>[Term],[TermMapping],[Review],[ProposedOntologyTerm],[GeneReview],[FunctionalIsoform],[ExistingAnnotation],[CoreFunction],[AnnotationExtension])

## Referenced by Class

 *  **[ExistingAnnotation](ExistingAnnotation.md)** *[ExistingAnnotation➞term](ExistingAnnotation_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **None** *[➞anatomical_locations](coreFunction__anatomical_locations.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[➞directly_involved_in](coreFunction__directly_involved_in.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[➞in_complex](coreFunction__in_complex.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **None** *[➞locations](coreFunction__locations.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[➞molecular_function](coreFunction__molecular_function.md)*  <sub>1..1</sub>  **[Term](Term.md)**
 *  **None** *[➞substrates](coreFunction__substrates.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[➞isoform_specific_terms](functionalIsoform__isoform_specific_terms.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[➞proposed_parent](proposedOntologyTerm__proposed_parent.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **None** *[proposed_replacement_terms](proposed_replacement_terms.md)*  <sub>0..\*</sub>  **[Term](Term.md)**
 *  **None** *[taxon](taxon.md)*  <sub>1..1</sub>  **[Term](Term.md)**
 *  **None** *[term](term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **None** *[➞target_term](termMapping__target_term.md)*  <sub>1..1</sub>  **[Term](Term.md)**

## Attributes


### Own

 * [Term➞id](Term_id.md)  <sub>1..1</sub>
     * Description: An OBO CURIE for a term in GO, CL, CHEBI, etc.
     * Range: [String](types/String.md)
 * [Term➞label](Term_label.md)  <sub>1..1</sub>
     * Description: the term name
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of the entity
     * Range: [String](types/String.md)
 * [ontology](ontology.md)  <sub>0..1</sub>
     * Description: Ontology of the term. E.g `go`, `cl`, `hp`
     * Range: [String](types/String.md)
