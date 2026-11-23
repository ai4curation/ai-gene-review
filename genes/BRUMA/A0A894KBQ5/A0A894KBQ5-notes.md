# BRUMA A0A894KBQ5 / GLC-4 notes

## Setup

- 2026-11-22: fetched `BRUMA` `GLC-4` from UniProt accession `A0A894KBQ5` into an accession-named `genes/BRUMA/A0A894KBQ5/` folder to avoid overloading the broad PTHR18945 Cys-loop receptor family.
- UniProt resolves `A0A894KBQ5_BRUMA` to gene `GLC-4`, protein `Glutamate-gated chloride channel subunit 4`, EMBL `MW196268` / `QRW38686.1`, and PANTHER `PTHR18945`.
- Lamassiaude et al. identify the same B. malayi GLC-4 clone as `MW196268`, tying the UniProt accession directly to the Bma-GLC-4 subunit tested in Xenopus oocytes [PMID:34623639 "The sequences used in this study are available on GenBank under the following accession numbers: B. malayi (Bma): AVR‐14B (MW196269), GLC‐2 (MW196266), GLC‐3 (MW196267), GLC‐4 (MW196268)"].
- `just fetch-gene-pmids BRUMA A0A894KBQ5` found no GOA PMID references; the seven seeded rows came from InterPro, UniProt-SubCell, and combined UniProt automated mappings.
- `just paint-losses BRUMA A0A894KBQ5` reported that A0A894KBQ5 is a PTHR18945 member but not a leaf of the cached PAINT tree, so no IRD or IKR loss could be checked on this lineage.
- No provider-generated deep-research file was present for this accession; this manual review used the UniProt record, the seeded GOA rows, cached Lamassiaude et al. full text, and explicit PMID-free GOA and PAINT-loss checks.

## Annotation decisions

- Keep the generic Cys-loop receptor, ion-channel and extracellular ligand-gated channel activities from InterPro, because Bma-GLC-4 has intact GluCl extracellular ligand-binding and transmembrane signatures and belongs to the Lamassiaude panel of conserved nematode GluCl subunits [PMID:34623639 "In the present study, we reasoned that GluCls composed of the highly conserved AVR‐14, GLC‐2, GLC‐3 and GLC‐4 subunits could be involved in the broad‐spectrum activity of macrocyclic lactones on nematodes."].
- Do not add `GO:0008068 extracellularly glutamate-gated chloride channel activity`: Lamassiaude et al. found no robust homomeric Bma-GLC-4 channel, and Bma-GLC-2/Bma-GLC-4 and Bma-GLC-3/Bma-GLC-4 coexpression were also silent under the tested Xenopus-oocyte conditions [PMID:34623639 "Finally, in oocytes injected with Bma‐glc‐2 (n = 11), Pun‐glc‐2 (n = 11), Bma‐glc‐3 (n = 14), Bma‐glc‐4 (n = 13) or Pun‐glc‐4 (n = 12), 1‐mM glutamate application did not produce detectable responses."] [PMID:34623639 "In contrast with C. elegans, the B. malayi and the P. univalens GLC‐2/GLC‐4 combination failed to produce detectable glutamate responses (n = 8 and n = 11, respectively)."] [PMID:34623639 "No currents could be recorded with 1‐mM glutamate application on oocytes injected with Bma‐GLC‐3/GLC‐4 (n = 13)"].
- Record the unresolved native Bma-GLC-4 receptor composition as a biology gap rather than adding a module association.
