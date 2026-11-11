# P13 (P13_BPPH6, P11130) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P13` / Protein P13 (`UniProtKB:P11130`, 72 AA)
- **Genomic Segment:** Encoded on the middle (M) dsRNA segment.

## Biological Role in the Cystovirus Lifecycle
1. **Viral Envelope Membrane Protein (`GO:0019031`, `GO:0055036`, `GO:0039660`):**
   - P13 is a 72-residue (7.6 kDa) membrane-associated protein encoded on the middle (M) dsRNA segment along with the other membrane-associated proteins P3, P6, and P10 [file:BPPH6/P13/P13-uniprot.txt].
   - P13 is a component of the lipid-containing viral envelope membrane (`GO:0019031` viral envelope, `GO:0055036` virion membrane), which is composed of phospholipids and proteins P3, P6, P9, P10, and P13 [PMID:8021194; file:BPPH6/P13/P13-uniprot.txt].
   - Unlike P3 (host attachment spike), P6 (membrane fusion protein), P9 (major envelope protein), and P10 (holin-like lysis factor), the precise non-structural or accessory role of P13 within the virion envelope remains incompletely defined.

## Curation Decisions
- **Existing GOA Annotations:**
  - `GO:0019031` (`viral envelope`, IEA): `ACCEPT`.
  - `GO:0055036` (`virion membrane`, IEA): `ACCEPT`.
- **New Annotations (`action: NEW`):**
  - `GO:0039660` (`structural constituent of virion`, `enables`, `IC` from `PMID:8021194` and `file:BPPH6/P13/P13-uniprot.txt`): P13 is a constituent protein of the mature phi6 virion lipid-protein membrane.
