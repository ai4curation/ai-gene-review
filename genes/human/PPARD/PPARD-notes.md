# PPARD curation notes

Deep research status: no configured non-Claude deep-research provider was available, so this is a manual synthesis from UniProt, the GOA seed, Reactome caches and PTHR24082 PAINT records.

## Core biology

PPARD is PPAR-delta/beta. UniProt summarizes it as a "Ligand-activated transcription factor key mediator of energy metabolism in adipose tissues"; after ligand activation, "the receptor binds to promoter elements of target genes" and "Regulates the peroxisomal beta-oxidation pathway of fatty acids" (`file:human/PPARD/PPARD-uniprot.txt`, CC:FUNCTION).

The accepted core rows are the shared PPAR rows: nuclear receptor activity, RNA polymerase II transcription-factor activity, cis-regulatory DNA binding, nucleus/chromatin localization and positive or negative Pol II transcriptional regulation. PPARD has fewer direct GOA rows than PPARG or PPARA for a named PPAR signaling process, so its `core_functions` section points to the accepted positive regulation of Pol II transcription row rather than adding a new PPAR-signaling assertion.

## Boundary decisions

PPARD GOA carries many broad processes transferred from mouse or rat: axon ensheathment, fat-cell and epidermis development, myoblast proliferation, smooth-muscle migration, decidualization, implantation and insulin secretion. These are plausible PPARD-dependent outputs but not the direct conserved molecular function, so they were mostly retained as non-core.

`GO:0003707 nuclear steroid receptor activity` and `GO:0030518 nuclear receptor-mediated steroid hormone signaling pathway` were marked as over-annotations for the same reason as in PPARA: PPARD is a fatty-acid-activated PPAR, not a steroid-hormone receptor.

The five bare `GO:0005515` IPI annotations are uninformative physical-interaction rows and were removed under the project protein-binding policy.

## PANTHER and modules

`just paint-losses human PPARD` reported no IRD or IKR on the lineage. The one existing module hit is `efferocytosis_induced_anti_inflammatory_programme`, where PPARD represents the PPAR-delta lipid-sensing route in macrophages. That module already records the efferocytosis context, so the gene review keeps the broader PPARD metabolic terms and does not add another module.

## PR review follow-up

The fatty-acid oxidation, beta-oxidation, fatty-acid transport and generic lipid-metabolism rows are regulatory outputs of PPARD-dependent transcription, not enzyme or transporter activities. The ISS/IEA orthology rows were therefore recast to regulatory GO terms where their source clearly points at the oxidative PPAR-delta program. The old `PMID:1333051` TAS row for `GO:0006629 lipid metabolic process` is weaker: that paper cloned PPARD and showed fatty acids can activate its ligand-binding domain in a reporter assay, but the review keeps its action consistent with the ISS row for the same broad term and recasts both as `GO:0019216 regulation of lipid metabolic process`.
