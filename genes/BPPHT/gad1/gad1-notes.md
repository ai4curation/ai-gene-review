# gad1 (Bacillus phage phi3T) — Curation Notes

## Overview
- **Gene symbol**: `gad1`
- **UniProt ID**: `A0A1P8CWZ3` (`GAD1_BPPHT`, ORF `phi3T_128`)
- **Organism**: *Bacillus* phage phi3T (`NCBITaxon:10736`)
- **Product**: Protein Gad1 (Gabija anti-defense 1; 295 aa, ~35 kDa; PDB `8U7I`)

## Biological Function and Mechanism
- **Anti-Gabija immune evasion**: `Gad1` is a phage-encoded anti-defense protein that counteracts the bacterial Gabija (`GajAB`) antiphage defense system [PMID:37992756; PMID:37992757].
- **Structural mechanism (octameric web)**: Cryo-EM analysis (`PDB:8U7I`) revealed that eight copies of `Gad1` assemble into a homo-octameric web that wraps 360° around the host 4:4 `GajAB` supramolecular complex to form an ~775 kDa `4:4:8` `GajAB–Gad1` co-complex [PMID:37992757].
- **Steric blockade of DNA binding and cleavage**: Using an N-terminal "fist" domain, an central "arm" with "shoulder" and "elbow" contacts, and a C-terminal "thumb" domain, `Gad1` encases the `GajA` Toprim endonuclease dimer-of-dimers core and sterically obstructs the `GajA` DNA-binding groove [PMID:37992757]. Consequently, `Gad1` completely abolishes `GajAB` binding to target DNA and blocks DNA nicking and double-strand cleavage in vitro and in vivo, without requiring disassembly of the `GajAB` complex [PMID:37992756; PMID:37992757].

## Curation Decisions
- **Existing annotations**:
  - `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA): `ACCEPT`. Directly captures the biological role of `Gad1` in suppressing the bacterial Gabija innate antiphage immune complex.
  - `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA): `TOO_GENERAL`. True of `Gad1`, but already entailed by the more specific ancestor/descendant term `GO:0052170` (`symbiont-mediated suppression of host innate immune response`) present in this review.
