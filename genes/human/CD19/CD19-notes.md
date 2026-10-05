# CD19 review notes

## Scope and access, 2026-10-05

The normal source import contains human CD19/P15391, 38 annotations, two alternative products and 22 references. All machine fields are preserved. Six existing publication caches and six Reactome caches are reused without replacement; their access flags describe the selected versions. The two family exports remain outside this review. No new GO annotation is proposed.

The normal Falcon deep-research command and its Perplexity fallback both failed to resolve the pinned deep-research-client dependency in the available offline environment. No provider report was authored or substituted. This document records manual research. All twelve selected publication headers and abstracts and six complete Reactome summaries were read. Selected original Methods and Results are identified below; this is not a claim to have inspected all figures, supplements or raw data.

## Functional synthesis

CD19 provides a noncatalytic membrane platform connecting the B-cell receptor environment to intracellular signaling proteins. The core molecular function is signaling receptor complex adaptor activity (GO:0030159), supported by complex assembly and recruitment evidence. Regulation of B-cell receptor signaling (GO:0050855) is the core process. Plasma membrane is the core location. Proliferation, antibody responses and calcium mobilization are downstream outputs; CD19 is not assigned kinase, lipid-kinase or calcium-channel activity.

The antibody-coligation study establishes enhanced antigen sensitivity ([PMID:1373518](https://pubmed.ncbi.nlm.nih.gov/1373518/)). Its cached abstract and PubMed record were read; the complete original methods were not obtained. The patient study connects biallelic CD19 mutations to defective antigenic responses despite preserved mature B-cell numbers ([PMID:16672701](https://pubmed.ncbi.nlm.nih.gov/16672701/)). Publisher-indexed calcium text was available, but direct full-page and PDF requests failed. Its canonical cache remains abstract-only.

Human receptor-complex coprecipitation and surface patching support association with CD21/CR2, CD81/TAPA-1 and Leu-13 ([PMID:1383329](https://pubmed.ncbi.nlm.nih.gov/1383329/), complete abstract). Raji and recombinant K562 experiments distinguish the ligand-recognition role of CR2 from the CD19-containing signaling assembly ([PMID:1702139](https://pubmed.ncbi.nlm.nih.gov/1702139/), complete abstract; "CR2 associates directly with CD19"). These results do not assign complement-fragment binding to CD19 itself.

## Primary experiment boundaries

[PMID:9382888](https://pubmed.ncbi.nlm.nih.gov/9382888/): selected complete cached Methods and Results concern human WT or Y484F/Y515F CD19 expressed in mouse J558Lμm3CD45+ cells, plus a separate mouse splenic-B-cell arm. PI3K, IP3 and calcium were measured; AKT is discussed as a possible downstream mechanism. Historical residue numbering is retained as reported. Figure pixels and results reported as “not shown” were not inspected.

[PMID:29523808](https://pubmed.ncbi.nlm.nih.gov/29523808/): selected Results, Figure 8 caption and expression/antibody Methods describe GRB2-SH2 affinity purification from human DG75 lysates with GST and mutant-domain controls. CD19 was detected by immunoblot despite absence from the mass-spectrometry identification. This supports association, without proving purified binary binding or a native messenger-binding mechanism for CD19. The source coreceptor annotation remains UNDECIDED because GO:0015026 explicitly includes messenger binding; the established adaptor function is accepted separately.

[PMID:23071339](https://pubmed.ncbi.nlm.nih.gov/23071339/): the existing 8 KB full-text-marked cache is abbreviated. Selected Results from the richer authenticated 29 KB extraction describe CD19 crosslinking and a CD19–IKAROS–SYK complex in human FL112 pro-B cells. Supplementary Figure S4 was not inspected. The SYK/Ikaros-focused title is not evidence of a wrong-gene annotation. Preserve the broad complex observation as non-core; do not infer direct binary interaction or CD19 kinase activity.

[PMID:9317126](https://pubmed.ncbi.nlm.nih.gov/9317126/) is explicitly a transgenic-mouse study of a CD19 construct lacking its cytoplasmic region. Its abstract supports signaling dependence on that region. It is not described as a primary-human experiment. Antibody effects in the human study [PMID:2463100](https://pubmed.ncbi.nlm.nih.gov/2463100/) depend on cell type and stimulus; its abstract does not support a universal activating direction.

## Curator deference and remaining limits

The external-surface IDA annotations cite FcRL6 and microRNA papers ([PMID:17213291](https://pubmed.ncbi.nlm.nih.gov/17213291/), [PMID:20660734](https://pubmed.ncbi.nlm.nih.gov/20660734/)). Their selected abstracts do not expose the CD19 assays. The localizations agree with independent CD19 surface evidence, so the annotations are retained with explicit curator deference, without claiming those assays were inspected. The exosome observation ([PMID:20458337](https://pubmed.ncbi.nlm.nih.gov/20458337/)) remains non-core; its target table was not inspected, and detection does not imply exosome-biogenesis activity.

All six Reactome summaries were read. Membrane complexes support location; lipid phosphorylation belongs to PI3K and complement recognition to CR2. The inhibitor-context reaction does not make CD19 an enzyme or a direct inhibitor target.

The three PAINT assertions retain the curator's evolutionary judgment. The IBD placement and alignment were not independently inspected, and no structured ancestral-gain claim is invented. CD19 appearing in its own descendant-evidence list is legitimate, not circular support. The two alternative products remain exactly as seeded; no product-specific functional distinction is inferred from their names.

GO definitions were checked in official GO/MOD displays: [signaling receptor complex adaptor activity](https://amigo.geneontology.org/amigo/term/GO:0030159) and [coreceptor activity](https://amigo.geneontology.org/amigo/term/GO:0015026). The single pathway refinement narrows antigen receptor signaling to B-cell receptor signaling. It creates no new assertion and preserves the original source fields.

## Validation

Normal schema, term and best-practice validation passed without diagnostics. The status check computed COMPLETE; the initial manually selected DRAFT was corrected to that computed value. The one unresolved coreceptor annotation remains explicit. Independent whole-review assessment is pending.
