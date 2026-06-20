# CD33 curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human CD33 --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, Reactome, PANTHER family, and publication evidence.
- CD33/Siglec-3 is a myeloid-lineage type I membrane Siglec and inhibitory receptor. UniProt summarizes expression in monocytic/myeloid cells and brain microglia, cell-surface CD33M localization, and an intracellular/peroxisomal CD33m splice isoform.
- Sialic acid binding and cell-cell interaction are core. The founding ligand study reports that CD33 recognizes sialylated glycans and concludes that "CD33 can function as a sialic acid-dependent cell adhesion molecule" [PMID:7718872 "CD33 can function as a sialic acid-dependent cell adhesion molecule"].
- CD33 inhibitory signaling is mediated by ITIM phosphorylation and SHP-1/SHP-2 recruitment. The JBC study reports that "Phosphorylated CD33 recruited both the protein-tyrosine phosphatases, SHP-1 and SHP-2" [PMID:10206955 "Phosphorylated CD33 recruited both the protein-tyrosine phosphatases, SHP-1 and SHP-2"].
- Functional inhibitory receptor evidence is direct: CD33 down-regulates CD64/FcgammaRI calcium signaling, and dominant-negative SHP-1 blocks this effect [PMID:10887109 "CD33 is an inhibitory receptor and also that SHP-1 phosphatase has a significant role in mediating CD33 function"].
- CD33 monocyte repressor activity depends on sialic acid recognition and PI3K-linked intracellular signaling. The cached abstract says lower CD33 surface expression caused spontaneous cytokine production, neuraminidase increased IL-1 beta, and ligand addition reversed the effect [PMID:15597323 "depending on the sialic acid microenvironment for its repressor activity"].
- CD33 engagement can inhibit proliferation/survival in normal or leukemic myeloid contexts, supporting the negative regulation of cell population proliferation annotation as part of inhibitory receptor biology [PMID:10611343 "Engagement of CD33 led to inhibition in some experiments"].
- C1q interaction is biologically meaningful but should not be left as generic protein binding if a more specific representation becomes available. The full text reports that C1q/gC1q interacts with CD33 and activates inhibitory motifs [PMID:28325905 "C1q and gC1q interact with CD33 to activate its inhibitory motifs"].
- CD33m peroxisome localization is isoform-specific and Alzheimer-relevant but not the core cell-surface receptor function. The cached abstract says CD33m lacks the sialic acid-binding domain and "does not localize to cell surfaces; instead, it accumulates in peroxisomes" [PMID:28747436 "does not localize to cell surfaces; instead, it accumulates in peroxisomes"].
- The tau/protein secretion annotation from PMID:27044754 was marked UNDECIDED because the cached abstract names FRMD4A as the functional tau-secretion hit and does not expose the CD33-specific screen result [PMID:27044754 "FRMD4A is functionally linked to tau secretion"].
- Generic `protein binding` annotations were marked over-annotated except where a specific term exists (`protein phosphatase binding`); high-throughput interactome hits do not define CD33 function without more specific biological context.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls and reference-review
coverage. No YAML changes were needed in this pass.

The single UNDECIDED annotation remains GO:0050714 positive regulation of
protein secretion from PMID:27044754. The cached abstract identifies FRMD4A as
the functional tau-release hit and does not show the CD33-specific evidence
behind the IMP annotation. Because the annotation is experimental and the local
cache is abstract-only for the relevant claim, it should remain UNDECIDED rather
than be removed.

The core function remains CD33/Siglec-3 sialic-acid binding at the myeloid cell
surface plus ITIM-dependent SHP-1/SHP-2 recruitment and inhibitory signaling.
The Alzheimer-relevant CD33m splice isoform should be handled as isoform- and
localization-specific biology rather than used to redefine the core CD33M
surface inhibitory receptor function.
