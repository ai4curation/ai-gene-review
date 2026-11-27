# fabZ (Escherichia coli K-12, UniProtKB:P0A6Q6) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml` as the E. coli
representative of the FabZ dehydratase variant. FabZ dehydrates
(3R)-hydroxyacyl-ACP to trans-2-enoyl-ACP across a broad chain-length range,
including the long unsaturated species on which its paralogue FabA is nearly
inactive
[PMID:8910376 "The FabZ dehydratase efficiently catalyzed the dehydration of short chain beta-hydroxyacyl-ACPs and long chain saturated and unsaturated beta-hydroxyacyl-ACPs."],
which is the division of labour that keeps both dehydratases in the module.

The lipid A row is kept as non-core: the gene was found because lesions in it
suppress a temperature-sensitive lipid A acyltransferase, through a raised
(3R)-hydroxymyristoyl-ACP pool
[PMID:7806516 "We suggest that bypass of the lpxA2 phenotype by mutations in orf17 may be due to an increased (3R)-hydroxymyristoyl-ACP pool."],
so FabZ sets the level of the lipid A acyl donor rather than performing a lipid A
step — the same call as the P. putida fabZ review. The generic hydro-lyase row is
TOO_GENERAL (the P. putida review recorded the identical judgment as
MARK_AS_OVER_ANNOTATED, before TOO_GENERAL existed).

## Annotation decisions (12 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0005737 cytoplasm | IEA | ACCEPT | Cytoplasmic location of a soluble FAS-II enzyme. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic assignment of fatty-acid biosynthesis across the bacterial FAS-II dehydratase clade, which is the pathway FabZ serves. |
| GO:0006633 fatty acid biosynthetic process | IDA | ACCEPT | Direct demonstration that FabZ functions in fatty-acid synthesis, by reconstitution of elongation cycles with purified proteins. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Electronic pathway assignment, consistent with the experimental rows. |
| GO:0009245 lipid A biosynthetic process | IEA | KEEP_AS_NON_CORE | Lipid A biosynthesis depends on the (3R)-hydroxymyristoyl-ACP pool that FabZ dehydrates; a real but secondary role of the same catalytic step. |
| GO:0016836 hydro-lyase activity | IEA | TOO_GENERAL | Correct but uninformative parent activity; the exact dehydratase term is asserted on five other rows of this review. |
| GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity | EXP | ACCEPT | The core molecular function, from the study that reconstituted the complete FAS-II elongation cycle with purified enzymes. |
| GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity | EXP | ACCEPT | The core dehydratase activity, from the paper that identified fabZ as the structural gene for (3R)-hydroxymyristoyl-ACP dehydrase. |
| GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity | IBA | ACCEPT | Phylogenetic assignment of the dehydratase activity across the FabA/FabZ clade. |
| GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity | IDA | ACCEPT | Direct assay of the dehydratase on beta-hydroxyacyl-ACP substrates of several chain lengths. |
| GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity | IEA | ACCEPT | Electronic assignment of the core dehydratase activity from Rhea and EC mappings. |
| GO:0042802 identical protein binding | IDA | KEEP_AS_NON_CORE | Self-association of FabZ, which is an oligomer of the hotdog-fold dehydratase family. |

**Core function:** enables GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; in GO:0006633; located in GO:0005737

