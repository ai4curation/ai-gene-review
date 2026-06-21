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

## Falcon deep research integration (2026-06-21)

A grounded Falcon (Edison) deep-research report (CD33-deep-research-falcon.md, ~19 citations) was integrated; it strongly corroborates the existing review's core model (myeloid sialic-acid-binding Ig-type lectin / ITIM-bearing inhibitory receptor recruiting SHP-1/SHP-2) and adds structural, ligand, and disease-genetics detail without contradicting any existing action call. All Falcon-sourced citations below are not yet independently verified against full text.

NEW or REFINED findings beyond existing notes/review:

- Sialic-acid-binding site is centered on a conserved Arg119 forming a salt bridge to the sialic acid carboxylate, with an aromatic cluster (Phe21, His45, Tyr127) and the STKYSYK motif (residues 124-130); preference for alpha-2,6-linked sialoglycans, and a defined high-affinity ligand Neu5Ac-alpha2-3[6SO3]Gal-beta1-4GlcNAc [Yeh et al. 2026 J Biomed Sci, DOI:10.1186/s12929-026-01248-9; Vu et al. 2025 Biochemistry 64:1450-1462, DOI:10.1021/acs.biochem.4c00864] (not yet independently verified against full text).
- Structural architecture: smallest-Siglec two-domain ectodomain (IgV + single IgC), an IgC1 homodimerization interface (~808 sq A, shared only with Siglec-6), a 21-residue mostly monomeric TM helix, and a dynamically unstructured cytoplasmic tail with one ITIM + one ITIM-like motif [Vu et al. 2025 Biochemistry, DOI:10.1021/acs.biochem.4c00864] (not yet independently verified against full text).
- Physiological/pathogen ligands: keratan sulfate proteoglycans as endogenous CNS ligands, and alpha-2,6-biantennary sialoglycans on hepatitis B surface antigen (HBsAg) as a pathogen-derived ligand that engages CD33 to drive ITIM/SHP-1/2-mediated immune suppression (a viral immune-evasion axis not in the current review) [Yeh et al. 2026 J Biomed Sci, DOI:10.1186/s12929-026-01248-9; Vu et al. 2025 Biochemistry] (not yet independently verified against full text).
- Microglial signaling context: CD33 antagonizes ITAM/DAP12-SYK/ERK activating pathways (e.g. TREM2-associated); CD33 loss/disruption raises SYK and ERK1/2 phosphorylation and increases phagocytosis of Abeta1-42 and bacterial particles, with constitutive inflammatory gene transcription (IL-1beta, IL-8, IL-10, INPP5D) on knockout [Wissfeld et al. 2021 Glia 69:1393-1412, DOI:10.1002/glia.23968] (not yet independently verified against full text).
- Alzheimer-risk allele biology made explicit: rs3865444C risk allele associates with increased full-length CD33 surface density and reduced Abeta phagocytosis, whereas the protective rs12459419T promotes exon-2 skipping to the CD33m / CD33dE2 isoform lacking the IgV sialic-acid-binding domain [Beckers et al. 2024 Genes 15:1204, DOI:10.3390/genes15091204; Wissfeld et al. 2021 Glia, DOI:10.1002/glia.23968] (not yet independently verified against full text).
- REFINED isoform view: CD33m is reported not only as cell-surface-diverted but as a gain-of-function isoform (enhanced phagocytosis/proliferation, reduced adhesion, Abeta uptake without the oxidative burst seen with full knockout); this nuances the existing notes' loss-of-function/peroxisomal framing [Wissfeld et al. 2021 Glia] (not yet independently verified against full text).
- Therapeutic context: AAV-delivered artificial-miRNA knockdown of CD33 in APP/PS1 mice reduced CD33 mRNA, soluble Abeta40/42, plaque burden, and neuroinflammation [Griciuc et al. 2020 Hum Mol Genet 29:2920-2935, DOI:10.1093/hmg/ddaa179]; CD33 as a validated AML antibody-drug-conjugate target (gemtuzumab ozogamicin) [Laubli et al. 2022 Cancer Immunol Res 10:1423-1432, DOI:10.1158/2326-6066.cir-22-0366] (not yet independently verified against full text).

Discrepancies / annotations to revisit:

- No direct contradiction with existing annotations or action calls. The report reinforces ACCEPT for GO:0033691 (sialic acid binding), GO:0019903 (protein phosphatase binding), GO:0008160 (protein tyrosine phosphatase activator activity), GO:0002765 (immune response-inhibiting signal transduction), and the negative-regulation/cytokine terms.
- The HBsAg/HBV immune-suppression axis and the microglial TREM2/SYK-ERK antagonism are not captured by any current GO term in the review; these are candidate new-term / process directions to consider (e.g. negative regulation of microglial phagocytosis or innate immune response) but are based on single Falcon-sourced reports and should be verified before any term is added.
- The report does not bear on the one UNDECIDED annotation (GO:0050714 positive regulation of protein secretion, PMID:27044754); that remains UNDECIDED pending CD33-specific full-text evidence.
