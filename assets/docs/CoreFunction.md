
# Class: CoreFunction

A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the reviewed core annotations, brought together into a unified GO-CAM-like representation.

URI: [gene_review:CoreFunction](https://w3id.org/ai4curation/gene_review/CoreFunction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[SupportingTextInReference],[KnowledgeGap],[Term]<in_complex%200..1-++[CoreFunction&#124;description:string%20%3F],[Term]<substrates%200..*-++[CoreFunction],[Term]<anatomical_locations%200..*-++[CoreFunction],[Term]<locations%200..*-++[CoreFunction],[Term]<directly_involved_in%200..*-++[CoreFunction],[Term]<contributes_to_molecular_function%200..1-++[CoreFunction],[Term]<molecular_function%200..1-++[CoreFunction],[SupportingTextInReference]<supported_by%200..*-++[CoreFunction],[KnowledgeGap]<knowledge_gaps%200..*-++[CoreFunction],[GeneReview]++-%20core_functions%200..*>[CoreFunction],[GeneReview])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[SupportingTextInReference],[KnowledgeGap],[Term]<in_complex%200..1-++[CoreFunction&#124;description:string%20%3F],[Term]<substrates%200..*-++[CoreFunction],[Term]<anatomical_locations%200..*-++[CoreFunction],[Term]<locations%200..*-++[CoreFunction],[Term]<directly_involved_in%200..*-++[CoreFunction],[Term]<contributes_to_molecular_function%200..1-++[CoreFunction],[Term]<molecular_function%200..1-++[CoreFunction],[SupportingTextInReference]<supported_by%200..*-++[CoreFunction],[KnowledgeGap]<knowledge_gaps%200..*-++[CoreFunction],[GeneReview]++-%20core_functions%200..*>[CoreFunction],[GeneReview])

## Referenced by Class

 *  **None** *[core_functions](core_functions.md)*  <sub>0..\*</sub>  **[CoreFunction](CoreFunction.md)**

## Attributes


### Own

 * [knowledge_gaps](knowledge_gaps.md)  <sub>0..\*</sub>
     * Description: Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).
     * Range: [KnowledgeGap](KnowledgeGap.md)
 * [➞description](coreFunction__description.md)  <sub>0..1</sub>
     * Description: Description of the core function
     * Range: [String](types/String.md)
 * [➞supported_by](coreFunction__supported_by.md)  <sub>0..\*</sub>
     * Range: [SupportingTextInReference](SupportingTextInReference.md)
 * [➞molecular_function](coreFunction__molecular_function.md)  <sub>0..1</sub>
     * Description: The molecular function this gene product enables (i.e., has the activity independently). For complex subunits that contribute to but don't independently have a complex-level activity, use contributes_to_molecular_function instead and put a subunit-specific MF here (e.g., structural constituent of ribosome, electron transfer activity).
     * Range: [Term](Term.md)
 * [➞contributes_to_molecular_function](coreFunction__contributes_to_molecular_function.md)  <sub>0..1</sub>
     * Description: A molecular function that this gene product contributes to as part of a complex, but does not independently enable. Used for accessory/structural subunits of multi-protein complexes (e.g., an accessory subunit of Complex I contributes_to NADH dehydrogenase activity but does not have that activity on its own). The molecular_function slot should then contain the subunit-specific activity (e.g., structural molecule activity).
     * Range: [Term](Term.md)
 * [➞directly_involved_in](coreFunction__directly_involved_in.md)  <sub>0..\*</sub>
     * Range: [Term](Term.md)
 * [➞locations](coreFunction__locations.md)  <sub>0..\*</sub>
     * Description: Cellular anatomical entities (e.g. membranes, nucleus, cytosol, organelle parts) where the gene product functions. Do NOT use this for protein-containing complexes (GO:0032991 and its descendants) — record complex membership in in_complex instead.
     * Range: [Term](Term.md)
 * [➞anatomical_locations](coreFunction__anatomical_locations.md)  <sub>0..\*</sub>
     * Range: [Term](Term.md)
 * [➞substrates](coreFunction__substrates.md)  <sub>0..\*</sub>
     * Range: [Term](Term.md)
 * [➞in_complex](coreFunction__in_complex.md)  <sub>0..1</sub>
     * Description: The protein-containing complex (GO:0032991 descendant) that this gene product is an active unit of. Use this — not locations — for complex membership (e.g. ribosome, spliceosome, EMC, signal peptidase complex).
     * Range: [Term](Term.md)
 * [CoreFunction➞description](CoreFunction_description.md)  <sub>0..1</sub>
     * Description: Description of the entity
     * Range: [String](types/String.md)
