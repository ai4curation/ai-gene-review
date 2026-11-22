# ONCVO A0A8R1XRX4 notes

## Setup

- 2026-11-22: fetched `ONCVO` `A0A8R1XRX4` from the exact UniProt accession into an accession-named `genes/ONCVO/A0A8R1XRX4/` folder because UniProt does not assign a gene symbol to this O. volvulus Cys-loop receptor record.
- UniProt exact-accession resolution: live UniProtKB returned `A0A8R1XRX4_ONCVO`, protein `Glutamate-gated chloride channel`, EnsemblMetazoa model `OVOC290.1`, EMBL scaffold `CMVM020000020`, PANTHER `PTHR18945`, and CDD signatures `LGIC_ECD_GluCl` and `LGIC_TM_GluCl`.
- The UniProt feature table predicts four transmembrane helices at 245..269, 275..295, 307..329, and 399..422, so this looks like a complete Cys-loop pore architecture rather than a Q25634-like C-terminal fragment.
- GOA seeded 11 automated rows: generic receptor/channel/transport/membrane InterPro2GO rows; UniProt-SubCell plasma-membrane and membrane rows; EnsemblMetazoa transfers of `GO:0008068` and `GO:1902476` from C. elegans Q17328/GLC-2 and WormBase F25F8.2.1; and GOC logical inferences to `GO:0060079` and `GO:0098794`.
- `just fetch-gene-pmids ONCVO A0A8R1XRX4` found no GOA PMID references.
- `just deep-research-falcon ONCVO A0A8R1XRX4 --fallback perplexity-lite` could not run because `agentapi` was not on `PATH`; the wrapper reported only `claude_code` available and both `falcon` and `perplexity-lite` failed before writing provider files.
- `just paint-losses ONCVO A0A8R1XRX4` reported that A0A8R1XRX4 is a PTHR18945 member but not a leaf of the cached PAINT tree, so no IRD or IKR loss could be checked on this lineage.

## Annotation decisions

- Keep the EnsemblMetazoa-transferred `GO:0008068` and `GO:1902476` rows as core inferred GluCl biology. The transfer is from C. elegans Q17328/GLC-2, and A0A8R1XRX4 has the GluCl-specific extracellular and transmembrane CDD signatures expected for a beta-like nematode GluCl subunit.
- Keep `GO:0004888`, `GO:0005230`, and `GO:0005886` as correct generic parents or inferred location terms for a full-length predicted GluCl-family subunit.
- Mark `GO:0005216`, `GO:0006811`, `GO:0034220`, and `GO:0016020` `TOO_GENERAL` beside the asserted glutamate-gated chloride-channel activity, chloride-transport process, and plasma-membrane location.
- Mark `GO:0060079` `MARK_AS_OVER_ANNOTATED` because it is the known sign-wrong inference from the current ontology placement of `GO:0008068` under an excitatory glutamate-gated parent; a chloride-selective nematode GluCl should not be propagated to excitatory postsynaptic potential.
- Mark `GO:0098794` `MARK_AS_OVER_ANNOTATED`: it is a postsynapse inference through the sign-wrong excitatory row rather than a direct O. volvulus or exact parasite GluCl localization.
- Do not assert a module association yet. A0A8R1XRX4 is GLC-2-like, but the native O. volvulus alpha-like partner, cell type, and ivermectin or moxidectin response have not been tested.
