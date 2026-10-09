# CD46 review notes

## Scope and source preservation — 2026-10-09

Reviewed human CD46/MCP (UniProt P15529), preserving all 50 imported GO assertions, including their terms, evidence codes, original references, supporting entities and qualifiers. All 16 imported alternative products are unchanged. One separately sourced molecular-function annotation is proposed; no new biological-process annotation is proposed.

The starting files were recovered from the authentic intake archive, not from an earlier scientific review. Existing canonical publication and Reactome bytes were selected where available; missing source files were copied from the verified recovered archive into an isolated workspace. The original GOA, UniProt, source publications and Reactome records were not edited. Source selection, paths and checksums are recorded in the working packet. No provider report was fabricated.

The normal research wrapper ran Falcon with an explicit perplexity-lite fallback. Both attempts timed out after 90 seconds; no provider report was produced. The normal publication-fetch command reused all 10 original publication caches. Additional normal fetches produced authentic caches for PMIDs 3260937, 14566051, 10843656, 12112588 and 36477203. These manual notes record the research actually performed.

## Biological synthesis

CD46 has extracellular complement-control domains, a membrane anchor and alternatively spliced tails. C3b/C4b recognition supplies cofactor activity for factor I-mediated complement inactivation; factor I performs the cleavage. Cloning/topology evidence and the human variant study support this role, while the disease study establishes predisposition rather than universal penetrance. [PMID:3260937](https://pubmed.ncbi.nlm.nih.gov/3260937/), [PMID:14566051](https://pubmed.ncbi.nlm.nih.gov/14566051/), [PMID:1711570](https://pubmed.ncbi.nlm.nih.gov/1711570/).

Human CD46 also transmits a T-cell costimulatory signal. Receptor aggregation induces phosphorylation of cellular signaling proteins, and CD3/CD46 stimulation supports proliferation and IL-10-producing regulatory responses in the reported cytokine context. These observations do not make CD46 a kinase or establish identical functions for all splice products. [PMID:10843656](https://pubmed.ncbi.nlm.nih.gov/10843656/), [PMID:12540904](https://pubmed.ncbi.nlm.nih.gov/12540904/).

The full Jagged1 study establishes ectodomain binding using recombinant and biophysical assays. Its human-cell experiments support a model in which CD46 regulates Jagged1 availability to Notch during activation. Binding, sequestration and intracellular signaling are related but distinguishable activities. Patient responses vary with residual expression and stimulation conditions. The review does not infer human T-cell mechanisms from ordinary mouse CD46 physiology. [PMID:23086448](https://pubmed.ncbi.nlm.nih.gov/23086448/).

The three core units are therefore complement recognition/cofactor activity, T-cell costimulation and Jagged1 sequestration. The C3b-specific molecular term represents the well-established binding component of the complement unit; C4b recognition is described in its biological context without inventing a protease activity. The special sperm location and viral exploitation are retained outside these core activities. [PMID:12112588](https://pubmed.ncbi.nlm.nih.gov/12112588/), [PMID:8402913](https://pubmed.ncbi.nlm.nih.gov/8402913/).

## Annotation decisions and evidence boundaries

The original assertions comprise 18 ACCEPT, 6 KEEP_AS_NON_CORE, 12 MODIFY and 14 UNDECIDED decisions. The additional NEW assertion is transmembrane signaling receptor activity, sourced to PMID:10843656. The normal status command may classify a review as COMPLETE even when explicit UNDECIDED outcomes remain; completion is not a claim that those experiments have been resolved.

- Two C3/C3b generic-binding rows are refined to GO:0001851, complement component C3b binding. The original C3-focused paper has an exact CD46/C3 IntAct ELISA record linked to Figure 2A-1; its abstract-only cache is not mistaken for full-text review. Independent CD46 cofactor evidence corroborates the activity.
- The two Jagged1 rows are refined to protein sequestering activity using the mechanistic source. The exact high-throughput atlas row from PMID:35922511 was not independently recovered; the atlas is not represented as having established sequestration.
- The original signaling-receptor TAS row from PMID:8402913 is refined to virus receptor activity. Its experiment concerns Edmonston-strain measles entry. The independent host costimulatory activity is represented by the separate NEW MF assertion, so the viral source is not repurposed to establish host signaling.
- The new MF is based on direct receptor-aggregation and costimulation observations in the authentic primary abstract, with later mechanistic corroboration. Full methods and exact constructs were not accessible. No endogenous ligand identity is inferred from the antibody-stimulation result, and no new process annotation is added.
- PMID:20534589 explicitly uses anti-human CD46 surface staining as a plasma-membrane marker in the full methods/results. Its toxin-centered title does not invalidate that CD46 evidence.
- The PAINT rows are evaluated against the inherited biology. No donor-count argument or claim of circularity is made from self-inclusion among descendant sources; the ancestral placements themselves were not reconstructed.

### Fragmentomics: positive assays versus unresolved encodings

The paper assays short motifs against isolated PDZ domains by holdup chromatography, with many affinities below quantification thresholds. It cannot be read as demonstrating every tested pair. The exact IntAct publication-linked records were retrieved through the public PSICQUIC interface and joined to the original CD46 partner accessions. [PMID:36115835](https://pubmed.ncbi.nlm.nih.gov/36115835/).

All 17 annotated partner groups have records involving the CD46 C-terminal fragment mapped to canonical residues 383–392 and PDZ domains. Seven groups contain quantified micromolar affinities and are refined to GO:0030165, PDZ domain binding. This is an in vitro fragment activity, not proof of an endogenous full-length complex. The motif lies in the canonical CYT1 tail; UniProt documents tail replacement in other products, so the result is not generalized across all 16 products.

| Partner accession | Target record assessment | Decision |
| --- | --- | --- |
| A4D2P6 | Quantified PDZ-domain affinity | MODIFY |
| P78352 | Quantified PDZ-domain affinity | MODIFY |
| Q14160 | Quantified PDZ-domain affinities | MODIFY |
| Q5T2W1 | Quantified PDZ-domain affinities | MODIFY |
| Q86UL8 | Quantified PDZ-domain affinity | MODIFY |
| Q92796 | Quantified PDZ-domain affinities | MODIFY |
| Q9C0E4 | Quantified PDZ-domain affinity | MODIFY |
| O75970, Q07157, Q14005, Q68DX3, Q86UT5, Q8N448, Q8NI35, Q8TBB1, Q99767, Q9Y3R0 | Only unresolved 10 M encodings among the retrieved records | UNDECIDED |

The ten unresolved groups are not promoted to supported binding merely because IntAct has a record. Conversely, the encoded values do not justify a claim that binding is impossible in every biological context. Original Supplementary Data 1 could not be recovered: the publisher CDN and ProfAff host failed DNS lookup, and the correctly identified Europe PMC supplementary-files request timed out. The target records, detailed joins and access receipts are retained in the working packet. The source generic-binding preference permits KEEP_AS_NON_CORE only when the asserted interaction is supported; it does not turn unadjudicated assay records into positive findings.

The normal cache for the author correction lacks a substantive correction body. Independently retrieved Europe PMC full XML specifies corrections to missing/incomplete labels and panel organization in Figures 2, 4 and 5. It states no change to Supplementary Data 1. This does not close the unresolved affinity encoding. [PMID:36477203](https://pubmed.ncbi.nlm.nih.gov/36477203/).

### Other unresolved claims

The remaining four UNDECIDED rows concern focal-adhesion localization, exosome localization, cadherin binding and increased TGF-beta production. The proteomic CD46 target identifications were not independently recovered. For cadherin binding, the full article discusses alpha-E-catenin association, whereas the GOA supporting entity is CDH1/P12830; the relevant supplementary figure was not accessible. This is not a claim of curator misattribution. The original regulatory T-cell abstract supports IL-10 and the Tr1 phenotype but does not report the TGF-beta measurement. [PMID:21423176](https://pubmed.ncbi.nlm.nih.gov/21423176/), [PMID:20458337](https://pubmed.ncbi.nlm.nih.gov/20458337/), [PMID:23086448](https://pubmed.ncbi.nlm.nih.gov/23086448/), [PMID:12540904](https://pubmed.ncbi.nlm.nih.gov/12540904/).

## Access and ontology record

All 10 original publication abstracts were read. Main-text methods/results were inspected where available, especially for Jagged1, surface localization and the fragment assay. Abstract-only sources remain labeled as such, including the additional cofactor, disease, costimulation and sperm papers. The apparent Full Text section in the PMID:3260937 normal cache repeats its abstract; it was not treated as full-article access. Main-text access does not imply supplementary-table or figure-pixel inspection.

The four existing Reactome caches were read in full and reused without refresh. They consistently place CD46 in complement-fragment binding/cofactor reactions; factor I supplies catalysis. The live ontology definitions were verified through official QuickGO when no callable OLS tool was available. Relevant terms include C3b binding, PDZ domain binding, transmembrane signaling receptor activity, protein sequestering activity and virus receptor activity. A read-only search of the cached GO-CAM index found no CD46/P15529 entries. No new biological-process assertion was based on this absence.

A mistyped preliminary Europe PMC request returned PMID:23259495, not the Jagged1 paper. Its identity was checked and it was excluded from evidence. The corrected request for PMC3505834 returned the intended PMID:23086448. Similarly, the fragment article's PMC article-instance identifier differs from its PMCID; the corrected supplementary request used PMC9482650. These unsuccessful or irrelevant retrievals were not added as gene references or substituted for authentic caches.

## Verification

All original annotation fields outside `review` and all alternative products are compared structurally with the authenticated seed. Normal validation, status and rendering run with the repository's unmodified code/configuration and authentic caches in an isolated workspace. Four short verbatim anchors appear once each in the YAML; these notes add no source quotations. The aggregate quote audit counts repetitions across authored artifacts, verifies each anchor against its authentic cache and enforces at most 25 words per source. The finite publication manifest distinguishes new authored/source files from exact pre-existing source reuse. Root coordination owns canonical import, history creation and publication.

The correction reference omits `full_text_unavailable` because its full correction XML was read externally; its unchanged local publication cache remains abstract-only. The availability flag describes actual source access, and the reference assessment records the distinction.
