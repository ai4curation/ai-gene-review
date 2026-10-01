# BCS1L evidence reassessment

The reviewed source set contains 19 GOA annotations and one inherited proposed molecular-function annotation. All 19 source objects are preserved after the standard GOA parser backfills their qualifiers and supporting entities. There are no alternative-product records in the normal UniProt source or existing review. Raw UniProt, GOA, provider research and cached publications are unchanged.

The proposed review retains 12 annotations as ACCEPT, refines two generic molecular functions, retains two as non-core, and leaves three UNDECIDED. The existing NEW proposal is narrowed to protein-transporting ATPase activity (GO:0015450); it is not accompanied by an additional ancestor annotation or a new process annotation. Nucleotide binding is refined to ATP binding and hydrolase activity to ATP hydrolysis. The specific existing ATP-hydrolysis annotation is retained alongside the coupled activity.

## Evidence and access limits

- PMID:9878253: the complete cached abstract was read. Its original full text was unavailable. Human mitochondrial targeting and orthology support the localization and conserved-function interpretation. The mature-complex TAS assertion remains unresolved rather than being rejected on the strength of an abstract.
- PMID:11528392: the complete cached abstract was read; its full text was unavailable. Human variant evidence and yeast complementation are distinguished from a direct human biochemical assay.
- PMID:18628306: the complete cached abstract and selected publisher BCS1L Results, Discussion and Methods were read, including the text describing Figures 7–8. The study supports retaining the interaction and morphology annotations without treating them as an additional established core molecular function. Complex I/IV participation remains an open mechanistic question. Original images, supplements and all unrelated LETM1 experiments were not independently audited. [Publisher article](https://journals.biologists.com/jcs/article/121/15/2588/30154/Characterization-of-the-mitochondrial-protein).
- PMID:37821516: substantive Introduction, Results and Discussion and selected expression/purification, reconstitution, HS-AFM and binding Methods were read from the full XML cache. The construct BC019781 maps to mouse Bcs1l in the NCBI GEO platform record; Pichia is the expression host. The reviewed experiment measures conformational cycling, without a substrate-loaded transport assay. Later data-analysis Methods, images and supplementary movies were not audited. [Primary article](https://doi.org/10.1038/s41467-023-41806-5).
- PMID:34800366: the complete abstract was read. The exact BCS1L supplemental proteomics entry was not reconstructed; the source HTP attribution is retained with independent human localization support.
- The complete cached Reactome R-HSA-9865881 summary and normal UniProt identity, function, catalytic, localization, topology and disease sections were read. Reactome supplies pathway context; it is not a direct BCS1L transport experiment. The inherited provider document is retained as provenance, without using its prose as primary experimental evidence.

The conserved-function ISS proposal therefore does not assert direct human transport kinetics, a fixed ATP-per-cargo ratio, or a uniquely demonstrated human heptameric mechanism. The human identity and disease evidence and the ortholog mechanistic evidence have complementary roles.

## Ontology and provenance

The consulted official AmiGO snapshot was loaded on 2026-08-06. GO:0015450 is a child of transmembrane protein transporter activity (GO:0008320) and ATPase-coupled transmembrane transporter activity. It captures the coupled protein movement. The more narrowly named mitochondrial child GO:0008566 describes import through the inner-membrane translocase, which does not match this client-export mechanism; GO:0008564 describes secretory-pathway export. Neither is chosen merely from its name. The GO:0016887 comment supports representing hydrolysis together with an ATP-dependent overall activity. [GO:0015450](https://amigo.geneontology.org/amigo/term/GO:0015450), [GO:0016887](https://amigo.geneontology.org/amigo/term/GO:0016887).

The original IBA node placement was not independently reconstructed. Retention rests on agreement with established conserved function and no identified target-specific loss; the human target in the complex III IBA WITH/FROM is not treated as circular. No historical mapping failure mechanism is invented for the unresolved mature-complex annotation.

Later structural papers PMID:38821922 and PMID:40410623 remain research leads, not read evidence or formal reference additions. Short exact anchors are used only from the normal cached sources. The assistant's conservative per-source quotation budget is separate from the repository's mechanical reference checks.

Read-only ownership clearance found no current competing changes in the observed main/head/base scope. That snapshot does not replace fresh scope verification before publication. Canonical application, focused validation, rendering and an append-only history record remain separate steps after independent review.

## Applied review and validation

The preceding proposal-stage pending statements are superseded by the applied review. Independent science review passed, and focused `just validate human BCS1L` passed with two advisories. The supported generic protein-binding assertion is retained as non-core under the supplied action policy; the unchanged Falcon report is preserved without being cited as primary experimental evidence. Rendering and the scaffolded Codex/gpt-6 EDIT history validation passed. The rendered page embeds the reviewed YAML. These are focused checks, not a claim that repository-wide validation was run. All nine protected raw, research and source files remain unchanged. Publication remains a separate step subject to fresh ownership and exact-scope checks.
