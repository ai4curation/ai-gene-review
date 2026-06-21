
# Class: Reference

A reference is a published text  that describes a finding or a method. References might be formal publications (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review can be made by using the `file:` prefix.

URI: [gene_review:Reference](https://w3id.org/ai4curation/gene_review/Reference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferenceReview],[ReferenceReview]<reference_review%200..1-++[Reference&#124;id:string;title:string;is_invalid:boolean%20%3F;publication_type:PublicationTypeEnum%20%3F;full_text_unavailable:boolean%20%3F],[Finding]<findings%200..*-++[Reference],[Review]-%20additional_reference_ids%200..*>[Reference],[ExistingAnnotation]-%20original_reference_id%200..1>[Reference],[SupportingTextInReference]-%20reference_id%201..1>[Reference],[GeneReview]++-%20references%200..*>[Reference],[ModuleReview]++-%20references%200..*>[Reference],[RuleReview]++-%20references%200..*>[Reference],[PredictionReview]++-%20references%200..*>[Reference],[FindingReview]-%20superseded_by%200..*>[Reference],[SupportingTextInReference],[RuleReview],[Review],[PredictionReview],[ModuleReview],[GeneReview],[FindingReview],[Finding],[ExistingAnnotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReferenceReview],[ReferenceReview]<reference_review%200..1-++[Reference&#124;id:string;title:string;is_invalid:boolean%20%3F;publication_type:PublicationTypeEnum%20%3F;full_text_unavailable:boolean%20%3F],[Finding]<findings%200..*-++[Reference],[Review]-%20additional_reference_ids%200..*>[Reference],[ExistingAnnotation]-%20original_reference_id%200..1>[Reference],[SupportingTextInReference]-%20reference_id%201..1>[Reference],[GeneReview]++-%20references%200..*>[Reference],[ModuleReview]++-%20references%200..*>[Reference],[RuleReview]++-%20references%200..*>[Reference],[PredictionReview]++-%20references%200..*>[Reference],[FindingReview]-%20superseded_by%200..*>[Reference],[SupportingTextInReference],[RuleReview],[Review],[PredictionReview],[ModuleReview],[GeneReview],[FindingReview],[Finding],[ExistingAnnotation])

## Referenced by Class

 *  **None** *[additional_reference_ids](additional_reference_ids.md)*  <sub>0..\*</sub>  **[Reference](Reference.md)**
 *  **None** *[original_reference_id](original_reference_id.md)*  <sub>0..1</sub>  **[Reference](Reference.md)**
 *  **None** *[reference_id](reference_id.md)*  <sub>1..1</sub>  **[Reference](Reference.md)**
 *  **None** *[references](references.md)*  <sub>0..\*</sub>  **[Reference](Reference.md)**
 *  **None** *[superseded_by](superseded_by.md)*  <sub>0..\*</sub>  **[Reference](Reference.md)**

## Attributes


### Own

 * [Reference➞id](Reference_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [title](title.md)  <sub>1..1</sub>
     * Description: Title of the entity
     * Range: [String](types/String.md)
 * [findings](findings.md)  <sub>0..\*</sub>
     * Range: [Finding](Finding.md)
 * [is_invalid](is_invalid.md)  <sub>0..1</sub>
     * Description: Whether the reference is invalid (e.g., retracted or replaced)
     * Range: [Boolean](types/Boolean.md)
 * [publication_type](publication_type.md)  <sub>0..1</sub>
     * Description: The kind of publication or source this reference is (e.g. primary research article, review, meta-analysis, database record, AI deep-research report). For PMIDs this is normally inferred from the PubMed publication-type ('PT') metadata rather than set by hand; for non-PMID references (GO_REF, Reactome, file:) it is inferred from the identifier. Lets analyses ask, e.g., whether review articles or abstracts alone are sufficient to support a given annotation action.
     * Range: [PublicationTypeEnum](PublicationTypeEnum.md)
 * [full_text_unavailable](full_text_unavailable.md)  <sub>0..1</sub>
     * Description: Whether the full text is unavailable
     * Range: [Boolean](types/Boolean.md)
 * [reference_review](reference_review.md)  <sub>0..1</sub>
     * Description: Manual reviewer assessment of this reference (relevance, and citation correctness / scientific soundness). Reviewer-supplied, distinct from the machine-fetched id/title.
     * Range: [ReferenceReview](ReferenceReview.md)
