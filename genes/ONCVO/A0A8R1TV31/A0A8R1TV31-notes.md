# ONCVO A0A8R1TV31 notes

## Setup

- 2026-11-22: fetched `ONCVO` `A0A8R1TV31` from the exact UniProt accession into an accession-named `genes/ONCVO/A0A8R1TV31/` folder because UniProt does not assign a gene symbol to this O. volvulus Cys-loop receptor record.
- UniProt exact-accession resolution: live UniProtKB returned `A0A8R1TV31_ONCVO`, protein `Uncharacterized protein`, EnsemblMetazoa model `OVOC6009.1`, PANTHER `PTHR18945`, and CDD signatures `LGIC_ECD_GluCl` and `LGIC_TM_GluCl`.
- GOA seeded 10 automated rows: generic receptor/channel/transport/membrane InterPro2GO rows; UniProt-SubCell plasma-membrane and membrane rows; and EnsemblMetazoa transfers of `GO:0007606`, `GO:0031987`, and `GO:0050893` from C. elegans GLC-3 / G5EEZ3.
- `just fetch-gene-pmids ONCVO A0A8R1TV31` found no GOA PMID references.
- `just deep-research-falcon ONCVO A0A8R1TV31 --fallback perplexity-lite` could not run because `agentapi` was not on `PATH`; the wrapper reported only `claude_code` available and both `falcon` and `perplexity-lite` failed before writing provider files.
- `just paint-losses ONCVO A0A8R1TV31` reported that A0A8R1TV31 is a PTHR18945 member but not a leaf of the cached PAINT tree, so no IRD or IKR loss could be checked on this lineage.
- Manual UniProtKB feature comparison flagged the OVOC6009.1 model as probably N-terminally truncated. A0A8R1TV31 is 455 aa versus 486 aa for BRUMA GLC-3 A0A894KHH9 and 484 aa for C. elegans GLC-3; ONCVO residue 9 aligns to BRUMA residue 42, and the same 33-residue offset separates their ligand-binding-domain coordinates (13..228 versus 46..261) and first transmembrane segments (229..253 versus 262..286). The ONCVO sequence starts `MLISRVTK` and has no `FT SIGNAL` feature, while C. elegans GLC-3 has `SIGNAL 1..22`.

## Annotation decisions

- Keep `GO:0004888`, `GO:0005230`, `GO:0005886`, and `GO:0034220` as correct generic receptor, extracellular ligand-gated channel, plasma membrane, and ion-transmembrane-transport calls for a predicted GluCl-family Cys-loop channel subunit.
- Mark `GO:0005216`, `GO:0006811`, and `GO:0016020` `TOO_GENERAL` beside the more informative accepted channel, transport, and location rows.
- Mark the three EnsemblMetazoa transfers from C. elegans GLC-3, `GO:0007606`, `GO:0031987`, and `GO:0050893`, as `MARK_AS_OVER_ANNOTATED`: Shinkai et al. and Cook et al. support the source worm sensory and locomotory contexts, but no O. volvulus publication tests A0A8R1TV31 cell expression or parasite behavior.
- Do not propose `GO:0008068` or `GO:1902476` yet. A0A8R1TV31 has GluCl-specific extracellular and transmembrane CDD signatures and an intact PAR-like anion-selectivity motif in M2, and the EnsemblMetazoa donor is C. elegans glc-3, but the deposited model appears to lack its signal peptide, the accession cannot be placed on the cached PTHR18945 PAINT tree, and no paper has assayed this subunit's glutamate gating or chloride selectivity.
