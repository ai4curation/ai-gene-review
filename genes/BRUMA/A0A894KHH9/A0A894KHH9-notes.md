# BRUMA A0A894KHH9 / GLC-3 notes

## Setup

- 2026-11-22: fetched `BRUMA` `GLC-3` from UniProt accession `A0A894KHH9` into an accession-named `genes/BRUMA/A0A894KHH9/` folder to avoid overloading the broad PTHR18945 Cys-loop receptor family.
- Live UniProt exact-accession resolution tied `A0A894KHH9_BRUMA` to gene `GLC-3`, protein `Glutamate-gated chloride channel subunit 3`, EMBL `MW196267` / `QRW38685.1`, and PANTHER `PTHR18945`.
- Lamassiaude et al. identify the same cDNA as `B. malayi (Bma): ... GLC-3 (MW196267)`, tying the UniProt accession directly to the Bma-GLC-3 subunit tested in Xenopus oocytes.
- `just fetch-gene-pmids BRUMA A0A894KHH9` found no GOA PMID references; the ten seeded rows came from InterPro, UniProt-SubCell, combined UniProt and EnsemblMetazoa automated mappings.
- `just paint-losses BRUMA A0A894KHH9` reported that A0A894KHH9 is a PTHR18945 member but not a leaf of the cached PAINT tree, so no IRD or IKR loss could be checked on this lineage.

## Annotation decisions

- Keep the generic Cys-loop receptor, ion-channel and extracellular ligand-gated channel activities, and add `GO:0008068 extracellularly glutamate-gated chloride channel activity` with `qualifier: contributes_to`, because Bma-GLC-3 supported glutamate-evoked microampere currents when coexpressed with Pun-GLC-2.
- Keep the new exact GluCl function narrow. Lamassiaude et al. found no robust Bma-GLC-3 homomer and no responsive Bma-GLC-2/Bma-GLC-3 or Bma-GLC-3/Bma-GLC-4 channel, so this review does not assert a native B. malayi receptor composition or add a module association.
- Chloride selectivity is inferred from the Cys-loop GluCl family and the `LGIC_ECD_GluCl` and `LGIC_TM_GluCl` CDD signatures on A0A894KHH9 rather than directly assayed by ion substitution in the Pun-GLC-2/Bma-GLC-3 chimera.
- Mark the EnsemblMetazoa `GO_REF:0000107` transfers of C. elegans GLC-3 sensory and locomotory processes `MARK_AS_OVER_ANNOTATED`: they propagate worm native-neuron contexts to a B. malayi subunit for which only recombinant oocyte function is available.
