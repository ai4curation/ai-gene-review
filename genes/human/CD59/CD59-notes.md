# CD59 review notes

## Core complement function

- CD59 is the human GPI-anchored Ly6/uPAR-domain inhibitor of the terminal complement membrane attack complex. UniProt summarizes the mature protein as a cell-membrane, GPI-anchored protein whose soluble urinary form retains complement binding but is much weaker at blocking MAC assembly on membranes.
- PMID:36797260 is the strongest mechanistic paper for the 2025 UniProt rows. It directly resolves CD59 bound to nascent C5b-8 and C5b-9 and shows that CD59 traps MAC intermediates before the C8/C9 beta-hairpins complete membrane insertion and C9 polymerization.
- The older UniProt experimental rows from PMID:11882685 and PMID:1698710 are consistent with that mechanism: they measured CD59/protectin blocking C5b-8/C5b-9 channel formation and C9 insertion. They support the BP/MF rows but no longer need to carry the whole mechanistic explanation alone.

## Locations

- Plasma membrane and external side of plasma membrane are core. Cell surface and generic membrane are true but less precise than the accepted plasma-membrane and external-side assertions.
- Soluble extracellular CD59 is real and experimentally supported by PMID:8670172, but it is secondary because membrane tethering is the main setting for MAC inhibition.
- Multiple HDA exosome rows are kept as non-core. The generic PMID:19190083 vesicle row is refined to extracellular exosome because the paper describes exosome-like vesicles released by human tracheobronchial epithelium.
- Reactome secretory-traffic TAS rows place CD59 in ER, ERGIC, Golgi, COPII and transport-vesicle membranes while modeling export of a newly synthesized GPI-anchored cargo. PMID:20427317 supports ER-to-Golgi cargo export through Sec24 and p24-p23, but these rows are not evidence that CD59 resides or functions in those compartments.
- Reactome neutrophil specific-granule and tertiary-granule rows are retained as non-core storage pools that deliver CD59 to the plasma membrane by degranulation.

## Rows removed or demoted

- The eight GO:0005515 rows are all removed under the project protein-binding policy. They come from Htt interactome screens, p24 cargo-receptor binding, hepatitis B core binding, AIM/CD5L binding, an AGR2 cargo assay, and high-throughput interactome maps; none should remain as the bare molecular-function root.
- PINC rows from PMID:7691713 and PMID:1381503 are old literature-mapping rows. The chromosome-mapping CD59/MIC11 paper does not establish CD59 cell-surface-receptor signaling, and the CD59 gene-structure paper does not support blood coagulation.

## Family, modules and GO-CAMs

- PTHR10036 is a heterogeneous Ly6/uPAR fold family with separate CD59, LYPD1 and SLURP-like/sleepless-like branches. The CD59 PAINT node carries complement binding, plasma membrane and MAC inhibition; the LYPD1 node carries nicotinic acetylcholine receptor inhibition/signaling.
- The production GO-CAM index has no CD59 or LYPD1 activities. Reactome `R-HSA-2530445` covers the small CD59 complement event directly, so no separate GO-CAM or ModuleReview is needed here.
