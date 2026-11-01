# brt (Bordetella phage BPP-1) — Curation Notes

## Overview
- **Gene symbol**: `brt`
- **UniProt ID**: `Q775D8` (`RDPO_BPBPP`, `bRT`, `bbp8`)
- **Organism**: *Bordetella* phage BPP-1 (`NCBITaxon:2885909`)
- **Product**: Reverse transcriptase (`bRT`; 328 aa, ~38 kDa; PDB `8UB7`–`8UBF`)

## Biological Function and Mechanism
- **Catalytic subunit of the prototypical DGR**: `brt` (`bRT`) encodes the 328-amino-acid RNA-directed DNA polymerase that drives the diversity-generating retroelement (DGR) in *Bordetella* phage BPP-1, enabling mutagenic homing and host tropism switching at the variable region (`VR1`) of the distal tail fiber gene `mtd` [PMID:11910109; PMID:14973019; PMID:15386016].
- **RNP assembly with Avd and DGR RNA**: Unlike canonical retroviral or group II intron reverse transcriptases, `bRT` lacks reverse transcription activity on its own and requires assembly into a ternary ribonucleoprotein complex with a homo-pentameric barrel of the accessory variability determinant (`Avd`, encoded by `bbp7`) and cis-acting structured `DGR RNA` spanning the upstream `avd` spacer through the template repeat (`TR`) and downstream 140-nt tail [PMID:39779855].
- **Self-primed cDNA synthesis and adenine-specific mutagenesis**: Cryo-EM structures (`PDB:8UB7`–`8UBF`) show that the `bRT-Avd:RNA` complex positions `SpA56` (spacer adenine 56) and the first template base `TRG117` in the `bRT` active site, where the `2'-OH` of `SpA56` serves as the primer for covalent branched RNA-cDNA synthesis [PMID:39779855]. A flexible "tower" loop (`residues 228–260`) and an adaptable base-normalizing pocket in `bRT` specifically misincorporate dNTPs opposite template adenines (`A`-specific mutagenesis), while rapidly terminating synthesis after `G` incorporation when a template `A` is encountered, only extending after misincorporation opposite `A` [PMID:30982661; PMID:39779855].

## Curation Decisions
- **Existing annotations**:
  - `GO:0003964` (`RNA-directed DNA polymerase activity`, IEA): `ACCEPT`. Experimentally verified reverse transcriptase activity (`bRT`).
  - `GO:0006278` (`RNA-templated DNA biosynthetic process`, IEA): `ACCEPT`. `bRT` synthesizes mutated cDNA copies from the `DGR RNA` template repeat (`TR`).
- **Previous draft cleanup**:
  - Removed three unsupported `NEW` rows (`GO:0019028` viral capsid, `GO:0015074` DNA integration, `GO:0003676` nucleic acid binding) and removed invalid `inference:curator_inference` and `file:BPBPP/brt/brt-falcon-research.md` references. (`bRT` is a non-capsid intracellular enzyme and does not itself catalyze the host RecA-independent integration/homing step.)
