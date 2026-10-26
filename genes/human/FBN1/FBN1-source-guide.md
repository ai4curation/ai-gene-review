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

The broad extracellular structural function covers elastic and elastin-free scaffolding and growth-factor storage. The elasticity annotation is a matrix-level IC inference; it does not require isolated fibrillin to behave as elastin. Integrin binding is an adhesive matrix activity. The five BMP/GDF prodomain interactions use the specific BMP-binding term. Other positive generic protein-binding records remain non-core when no evidence-backed specific term is available, with source-specific uncertainty preserved where operative assays or exact target records were inaccessible.

Asprosin activity is assigned to the released product. The original glucogenic paper retains its DISPUTED reference assessment alongside the negative replication study and later positive evidence. Human recombinant ligand tested in rodent systems is distinguished from direct human physiology and from mouse-versus-human receptor evidence. The combined reference assessments preserve those limits while appending the additional database evidence scopes.

All contexts have a review decision; UNDECIDED records express unresolved evidence, not target absence or a curator error. No new GO annotation or publication quotation is introduced. Exact selected publication, Reactome and PAINT cache versions are retained; discovery-only publications are not needed for this review.


## Claim-level follow-up

The [feedback decision table](FBN1-feedback-decisions.yaml) gives the complete source keys for changed decisions and retained uncertainty. Skeletal development is non-core based on the Fbn1-null matrix-sequestration mechanism in [PMID:20855508](https://doi.org/10.1083/jcb.201003089), Results on Fbn1-null osteoblasts, matrix/media BMP and pathway-separation experiments. This is independent evidence, not recovery of the original human family assay. Interstitial-matrix localization is non-core based on [PMID:3536967](https://doi.org/10.1083/jcb.103.6.2499), human tissue Results and Figures 4–9; the exact MatrisomeDB record remains unverified.

Microfibril, alpha5beta1, calcium-binding and integrin-adhesion claims have matching independent positive human evidence. Their inaccessible original assays remain inaccessible. AlphaVbeta6, collagen XVI, the human processed-asprosin ligand, and the unresolved endothelial/cell-derived/venous proteomics joins have additional claim dimensions that a shared GO label does not settle. Those contexts remain undecided. The source-specific whole-reference assessments and assay limits are preserved.

The core synthesis now distinguishes matrix scaffolding, self-association, calcium coordination, integrin adhesion and released-asprosin signaling. Elasticity and heparin affinity remain supported non-core properties; broad extracellular structural activity retains nonelastic and growth-factor-scaffold scope. No redundant structural parent/elasticity child core pair is introduced. Hormone-associated cAMP signaling and glucose homeostasis are explicit, with ligand species, preparation and receptor limits intact. The four hormone process terms have no strict pairwise is_a/part_of ancestor relation in the verified ontology response.

The feedback table records the verified is_a edges from integrin binding to protein-containing complex binding and from negative regulation of osteoclast development to negative regulation of osteoclast differentiation. Reactome extracellular-region refinements remain based on the actual matrix/microfibril entity in those reactions. Broader extracellular annotations remain informative for soluble products, processing and proteolytic contexts; these are not claims that the broad location is false.
