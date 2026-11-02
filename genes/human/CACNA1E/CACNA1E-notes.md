# CACNA1E notes

## 2026-10-04

CACNA1E encodes the pore-forming alpha1E subunit of CaV2.3, the R-type high-voltage-activated calcium channel. Four homologous membrane domains combine voltage sensors with one ion-conduction pore. This is the channel's own molecular activity: opening permits extracellular calcium to enter the cytosol. Auxiliary alpha2delta and beta subunits alter its behavior without supplying the alpha1 pore. [PMID:7536609; PMID:8071363; PMID:36720859]

The reviewed human UniProt record Q15878 has 2,313 amino acids, sequence version 3 and CRC64 CCC7F309C27C42F1. Its three named products, Alpha-1E (Q15878-1), Alpha-1E-1 (Q15878-2) and Alpha-1E-3 (Q15878-3), and their sequence notes are retained from the source. Historical clone lengths and historical splice-product counts are not substituted for that current inventory. The 2,312-residue clone in PMID:7536609 and the historical forms in PMID:8071363 therefore remain properties of those studies.

### Channel mechanism and experimental systems

PMID:7536609 describes a human-brain cDNA expressed in Xenopus oocytes. The recorded barium currents establish voltage-dependent channel function. Although some pharmacological features resemble low-voltage channels, the reported channel is high-voltage activated. Its two putative calcium-binding sites are sequence predictions. The abstract does not contain a calcium-affinity experiment at either site.

PMID:8071363 distinguishes mouse and human clones and explicitly reports human alpha1E expression in HEK293 cells and Xenopus oocytes. Auxiliary alpha2/delta and beta subunits substantially increase expressed currents. These results support high-voltage channel activity and complex formation. Only the complete cached abstracts of these two cloning studies were available; their original figures and detailed Methods were not inspected.

The 2023 structural study, PMID:36720859, supplies direct human complex evidence. Full-length human alpha1E was coexpressed with alpha2delta1 and beta1 in HEK293-F cells for purification and cryo-EM. The structure places the voltage-sensor domains around the pore and identifies an intracellular W-helix that blocks the closed gate. Mutational electrophysiology links particular interfaces to channel activation or inactivation. The patch-clamp experiments in HEK293-T cells used barium as charge carrier; they are not measurements of calcium binding to the C-terminal EF-hand-like region. The abstract and relevant structural Results and construct/electrophysiology Methods were read from the full-text cache; supplementary images were not inspected. No EF-hand affinity assay was identified in those inspected sections.

Calcium permeation, selectivity-filter ion coordination, calmodulin-mediated sensing and calcium binding by an intrinsic EF-hand are different claims. The existing GO:0005509 IEA comes from InterPro:IPR002048. The UniProt calcium-site statements are inferred, and neither a predicted motif nor the channel's ability to conduct calcium verifies that particular binding assertion. That row remains UNDECIDED. The structural paper is positive support for the pore and channel complex, not a reason to declare an EF-hand binding experiment.

### Cellular role and participation

The human Reactome event R-HSA-210420 includes R-type channels in presynaptic calcium influx. Alpha1E performs the calcium-entry step that supports synaptic transmission; downstream vesicle fusion is performed by other molecular machinery. The core combines high-voltage channel activity, calcium import, plasma membrane, channel complex and the established synaptic context. No extra fusion or secretion annotation is manufactured.

Reactome:R-HSA-265645 separately includes CaV2.3 in human beta-cell calcium entry and sustained insulin secretion. The same summary discusses syntaxin association for CaV1.2/CaV1.3; that interaction is not transferred to CaV2.3. These complete cached summaries are curated pathway accounts. Their full participant/compartment graphs and all linked primary experiments were not independently reconstructed.

The inherited neuronal-cell-body location is retained with curator deference and an explicit access limit. The exact native-human localization experiment and complete PAINT tree/MSA were not read. IBA judgments preserve the original ancestral-node and donor identifiers; a short donor list or human target self-inclusion is not treated as evidence of failure. A search of the current local GO-CAM index found no CACNA1E/Q15878 entry.

### Mendelian association and correction

PMID:30343943 reports de novo CACNA1E variants in developmental and epileptic encephalopathy with associated contractures, macrocephaly and dyskinesias. Functional studies of selected S6 and S4-S5-linker variants showed altered activation/inactivation consistent with enhanced channel activity. This supports a mechanism for tested alleles, not a universal gain-of-function rule for every variant. The complete cached abstract was read; the original detailed Methods, variant tables and figures were unavailable.

PMID:30849329 is the 2019 erratum to that study. The fetched cache contains publication metadata and an author list, without the correction body. The correction text was separately read in the author-institution publication record: it corrects an author's spelling and omitted authors, rather than the channel-function results. The two publication identifiers remain separate and retain their fetched titles. The erratum is documented as correction provenance and does not independently support a new biological assertion. [Correction record](https://mayoclinic.elsevierpure.com/en/publications/erratum-de-novo-pathogenic-variants-in-cacna1e-cause-developmenta)

### Review scope and access

All 23 GOA-derived assertions are reviewed, with their original terms, evidence codes, references, qualifiers and partner/donor fields preserved. Seventeen are ACCEPT, five MODIFY and one UNDECIDED. Broad electronic activity/transport/location rows are refined to supported existing terms; no NEW annotation is proposed. One core function describes the integrated channel mechanism. The sole verbatim anchor in the YAML is five words from PMID:8071363; this note adds no source quotations.

One isolated standard deep-research attempt tried Falcon and its configured perplexity-lite fallback. Both failed with connection errors and produced no provider artifact. The failure trace is preserved under tmp/CACNA1E-deep-research-attempt; these are manual notes and are not labeled provider research. Gene/source files and the two later reference caches came through the unchanged source-fetch workflow. Fetched UniProt, GOA, publication and Reactome bytes are preserved.
