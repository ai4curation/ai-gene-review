# FBN1 evidence guide

The review separates mature matrix fibrillin-1 from released asprosin. It combines all 154 imported annotation contexts, retaining their original identifiers, evidence, references and order. The [biological notes](FBN1-notes.md) summarize matrix assembly, adhesion, growth-factor availability and hormone activity; the preserved journal records the direct-evidence assessment.

## Evidence and decision records

- [Matrix and interaction source guide](FBN1-direct-source-guide.md): original assays and target-specific proteomics evidence across 43 publications.
- [Direct decisions](FBN1-direct-decisions.yaml): 85 complete source annotations, methods and decisions.
- [Binding records](FBN1-binding-records.yaml): 29 generic protein-binding contexts, with experimental partner and assay limits.
- [Asprosin source guide](FBN1-asprosin-source-guide.md) and [asprosin decisions](FBN1-asprosin-decisions.yaml): seven contexts, including the parent-identifier extracellular annotation, ligand/receptor species, replication differences and reagent limits.
- [Database source guide](FBN1-database-source-guide.yaml) and [database decisions](FBN1-database-source-table.yaml): 62 phylogenetic, electronic, orthology and pathway contexts, including the distinction between a matrix function and downstream consequences of its mutation.
- [Product-source joins](FBN1-product-source-joins.yaml): all seven imported processed-asprosin contexts, including the appetite ISS context, plus the parent-product extracellular control. Each record includes the unchanged source annotation, official raw annotation/product identifiers and zero-based raw/GOA indices.

## Processing boundaries

The [UniProt P35555 record](https://www.uniprot.org/uniprotkb/P35555/entry) identifies mature fibrillin-1 (45–2731; PRO_0000007581) and asprosin (2732–2871; PRO_0000436882). These are recorded as cleavage products. They are not inferred alternative splice isoforms. The imported annotation objects remain unchanged where the seeder did not retain the raw processed-product identifier; the product-source table preserves that identity explicitly.

For [PMID:10636927](https://pubmed.ncbi.nlm.nih.gov/10636927/), the [accessed original publisher text](https://www.sciencedirect.com/science/article/pii/S0021925818311608) supplies Experimental Procedures for human skin-fibroblast purification and Edman sequencing, the native-monomer Results, and recombinant rF24 Results/Figure 5 caption. Native human fibrillin-1 begins at Arg45; recombinant rF24 yields Ala25 and Arg45 termini. Chick aortic pulse-chase experiments are a separate organismal context. The normal cached record is abstract-only; the external operative text was read, but figure pixels were not. The C-terminal processing experiments in [PMID:24982166](https://pubmed.ncbi.nlm.nih.gov/24982166/) distinguish secretion from microfibril incorporation. FBN1 supplies the processed products, not the proteolytic machinery.

## Interpretation limits

The broad extracellular structural function covers elastic and elastin-free scaffolding and growth-factor storage. The elasticity annotation is a matrix-level IC inference; it does not require isolated fibrillin to behave as elastin. Integrin binding is an adhesive matrix activity. Generic positive protein-binding records remain non-core under the project instruction, with source-specific uncertainty preserved where operative assays or exact target records were inaccessible.

Asprosin activity is assigned to the released product. The original glucogenic paper retains its DISPUTED reference assessment alongside the negative replication study and later positive evidence. Human recombinant ligand tested in rodent systems is distinguished from direct human physiology and from mouse-versus-human receptor evidence. The combined reference assessments preserve those limits while appending the additional database evidence scopes.

All contexts have a review decision; UNDECIDED records express unresolved evidence, not target absence or a curator error. No new GO annotation or publication quotation is introduced. Exact selected publication, Reactome and PAINT cache versions are retained; discovery-only publications are not needed for this review.
