# P10 (P10_BPPH6, P11127) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P10` / Envelope protein P10 (`UniProtKB:P11127`, 42 AA)
- **Genomic Segment:** Encoded on the middle (M) dsRNA segment.

## Biological Role in the Cystovirus Lifecycle
1. **Viral Envelope Membrane Protein (`GO:0019031`, `GO:0055036`):**
   - P10 is a 42-residue single-pass integral membrane protein (transmembrane helix AA 20–40) incorporated into the lipid-containing viral envelope (`GO:0019031`, `GO:0055036`) alongside P3, P6, P9, and P13 [file:BPPH6/P10/P10-uniprot.txt; PMID:8021194].
   - Upon infection, fusion of the phi6 viral membrane with the *Pseudomonas syringae* outer membrane delivers viral membrane proteins and phospholipids into the host outer membrane (`GO:0039662` host cell outer membrane) [PMID:3608985].
2. **Holin-like Host Cell Lysis Factor (`GO:0044659`):**
   - Nonsense mutations in gene 10 abolish host cell lysis at the end of the infective cycle without preventing intracellular assembly of infectious enveloped virions [file:BPPH6/P10/P10-uniprot.txt].
   - P10 functions as the membrane-depolarizing holin-like factor required for phage-mediated cytolysis (`GO:0044659` viral release from host cell by cytolysis), enabling the muralytic endolysin P5 to degrade the peptidoglycan layer and release progeny virions.

## Curation Decisions
- **Existing GOA Annotations:**
  - `GO:0019031` (`viral envelope`, IEA): `ACCEPT`.
  - `GO:0055036` (`virion membrane`, IEA): `ACCEPT`.
  - `GO:0031640` (`killing of cells of another organism`, IEA): `MODIFY` to `GO:0044659` (`viral release from host cell by cytolysis`), which more specifically captures phage-mediated host cell lysis at the end of the replication cycle.
  - `GO:0044384` (`host outer membrane`, IDA from `PMID:3608985`): `MODIFY` to `GO:0039662` (`host cell outer membrane`), because `GO:0044384` is obsolete in current GO and replaced by `GO:0039662`.
- **New Annotations (`action: NEW`):**
  - `GO:0044659` (`viral release from host cell by cytolysis`, `involved_in`, `IC` from `file:BPPH6/P10/P10-uniprot.txt`): Directly captures P10's essential role in host cell lysis for progeny virion release.
