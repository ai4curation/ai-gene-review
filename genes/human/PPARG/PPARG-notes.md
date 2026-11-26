# PPARG curation notes

Deep research status: `just deep-research-openai human PPARG` failed because only the `claude_code` provider is configured in this lane. These notes were therefore written by hand from the fetched UniProt flat file, the seeded GOA rows, Reactome records, the PTHR24082 PAINT table, and cached publications.

## Core biology

PPARG is PPAR-gamma, a lipid-activated NR1 nuclear receptor. The curated UniProt FUNCTION text captures the conserved mechanism used for core rows: PPARG is a "Ligand-activated transcription factor that forms obligate heterodimers with the retinoic acid receptor", and "Specifically binds to DNA specific PPAR response elements (PPRE) and modulates the transcription of its target genes" (`file:human/PPARG/PPARG-uniprot.txt`, CC:FUNCTION).

The review treats these as the central direct functions:

- ligand-dependent nuclear receptor activity in RXR heterodimers;
- sequence-specific binding to PPRE cis-regulatory DNA;
- positive and negative RNA polymerase II transcriptional regulation;
- nuclear/chromatin and RNA polymerase II transcription-regulator-complex localizations;
- the adipocyte and lipid/glucose homeostasis outputs that are the established PPAR-gamma program.

The PPARgamma2 isoform has the adipocyte-specialized arm. UniProt summarizes the mouse-backed isoform biology as "the key factor controlling the development of adipocytes" and specifically names white, beige and brown adipocyte differentiation, so the GOA adipocyte-development rows were kept as core rather than demoted to generic developmental phenotypes.

## Boundary decisions

Many PPARG rows are direct experiments on a particular target or cell type: smooth-muscle proliferation, BMP/TGF-beta/SMAD signaling, angiogenesis, vascular proliferation, macrophage foam-cell formation and miRNA expression. Those are retained as non-core outputs unless they were already the broad ancestors of accepted transcription terms. The review does not manufacture new process annotations from perturbation data: a PPARG knockdown or ligand treatment experiment only earns the recorded process when PPARG is being tested as the transcription factor for that response.

The two `GO:0046965` RXR-binding rows are MODIFY decisions. The GO term is obsolete, but the underlying RXRA:PPARG interaction is sound and is recorded as `GO:0016922 nuclear receptor binding`, which preserves the identity of the RXR partner better than a generic protein-heterodimerization term.

Every bare `GO:0005515` row is removed under the protein-binding policy. Several are real high-throughput or curated interactions, but the rows do not state the informative molecular function.

## PANTHER and modules

PANTHER PTHR24082 places the pan-NR1 nuclear receptor, DNA-binding, nucleus and Pol II transcription terms above the PPAR subfamilies. `just paint-losses human PPARG` reported no IRD or IKR on the PPARG lineage.

The cached GO-CAM index already contains PPARG activities for PTEN transcription, PAQR3/STUB1-mediated PPARG turnover, YTHDC1 stabilization of PPARG in brown adipocyte development, and PRDM16/TLE3 chromatin-adapter adipocyte modules. Those are compatible with the gene review but are too context-specific for a new family-level module here.

## PR review follow-up

The `GO:0004955 prostaglandin receptor activity` TAS row and the `GO:0007186 G protein-coupled receptor signaling pathway` IEA row both trace to lipid activation of PPARG rather than to seven-transmembrane prostaglandin receptor signaling. The former remains marked over-annotated, and the latter now follows it instead of being kept as a non-core GPCR process.

The `GO:0001890 placenta development` ISS row is supported by the mouse `Pparg` knockout placental phenotype in Barak et al. 1999, but that phenotype is a tissue output of PPARG transcriptional regulation rather than the conserved core receptor mechanism. The row is therefore kept as non-core, while PPARG adipocyte differentiation, lipid storage and insulin-sensitizing metabolic outputs remain part of the synthesized core function.

Broad DNA-templated transcription rows were aligned with the existing `TOO_GENERAL`
RNA polymerase II regulation policy, and the `GO:0043235` PPARG:RXRA row now
points to the Chandra intact-complex structure instead of the location/output
template.
