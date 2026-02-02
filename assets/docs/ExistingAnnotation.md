
# Class: ExistingAnnotation

An existing annotation from the GO database, plus a review of the annotation.

URI: [gene_review:ExistingAnnotation](https://w3id.org/ai4curation/gene_review/ExistingAnnotation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Review],[Reference],[Review]<review%200..1-++[ExistingAnnotation&#124;negated:boolean%20%3F;evidence_type:EvidenceType;retired:boolean%20%3F;isoform:string%20%3F;supporting_entities:string%20*],[Reference]<original_reference_id%200..1-%20[ExistingAnnotation],[AnnotationExtension]<extensions%200..*-++[ExistingAnnotation],[Term]<term%200..1-++[ExistingAnnotation],[GeneReview]++-%20existing_annotations%200..*>[ExistingAnnotation],[GeneReview],[AnnotationExtension])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Review],[Reference],[Review]<review%200..1-++[ExistingAnnotation&#124;negated:boolean%20%3F;evidence_type:EvidenceType;retired:boolean%20%3F;isoform:string%20%3F;supporting_entities:string%20*],[Reference]<original_reference_id%200..1-%20[ExistingAnnotation],[AnnotationExtension]<extensions%200..*-++[ExistingAnnotation],[Term]<term%200..1-++[ExistingAnnotation],[GeneReview]++-%20existing_annotations%200..*>[ExistingAnnotation],[GeneReview],[AnnotationExtension])

## Referenced by Class

 *  **None** *[existing_annotations](existing_annotations.md)*  <sub>0..\*</sub>  **[ExistingAnnotation](ExistingAnnotation.md)**

## Attributes


### Own

 * [ExistingAnnotation➞term](ExistingAnnotation_term.md)  <sub>0..1</sub>
     * Description: Term to be annotated
     * Range: [Term](Term.md)
 * [extensions](extensions.md)  <sub>0..\*</sub>
     * Range: [AnnotationExtension](AnnotationExtension.md)
 * [negated](negated.md)  <sub>0..1</sub>
     * Description: Whether the term is negated
     * Range: [Boolean](types/Boolean.md)
 * [evidence_type](evidence_type.md)  <sub>1..1</sub>
     * Description: Evidence code (e.g., IDA, IBA, ISS, TAS)
     * Range: [EvidenceType](EvidenceType.md)
 * [original_reference_id](original_reference_id.md)  <sub>0..1</sub>
     * Description: ID of the original reference
     * Range: [Reference](Reference.md)
 * [retired](retired.md)  <sub>0..1</sub>
     * Description: Whether the annotation is retired or replaced
     * Range: [Boolean](types/Boolean.md)
 * [isoform](isoform.md)  <sub>0..1</sub>
     * Description: UniProt isoform identifier (e.g., "P19544-1" for WT1 isoform 1). Only populated when the annotation is specific to a particular isoform rather than the canonical protein sequence. Note that just because an experiment used a particular isoform doesn't mean the annotation is isoform-specific - it may apply to all isoforms. Use this field only when there is clear evidence the annotation is isoform-specific.
     * Range: [String](types/String.md)
 * [supporting_entities](supporting_entities.md)  <sub>0..\*</sub>
     * Description: IDs of the supporting entities
     * Range: [String](types/String.md)
 * [review](review.md)  <sub>0..1</sub>
     * Description: Review of the gene
     * Range: [Review](Review.md)
