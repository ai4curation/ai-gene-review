# BPMS2 L (Lysis protein / P03609) Notes

## Overview
- **Gene symbol**: `L`
- **UniProt ID**: `P03609` (`LYS_BPMS2`)
- **Organism**: Escherichia phage MS2 (`NCBITaxon:12022`)
- **Protein**: Lysis protein (L protein), 75 amino acids, encoded in an overlapping reading frame spanning the 3' end of `cp` and the 5' end of `rep`.

## Biological Function & Localization
- **Single-gene lysis (Sgl) protein**: Unlike dsDNA phages that use holin-endolysin systems or alloleviviruses like Qbeta whose maturation protein (`A2`) inhibits cytoplasmic MurA, MS2 encodes a dedicated 75-aa membrane-associated lysis protein `L` ([PMID:2656650]; [PMID:3053640]; [file:BPMS2/L/L-uniprot.txt]).
- **Envelope localization and membrane adhesion sites**: Inserts predominantly into the *Escherichia coli* cytoplasmic (inner) membrane (`GO:0020002`) and intermediate-density membrane adhesion zones connecting the inner and outer membranes (Bayer's patches), triggering activation of the host autolytic murein hydrolase system and cytolytic viral release (`GO:0044659`) ([PMID:2656650]; [PMID:3053640]). Note that subsequent genetic studies (e.g., Chamakura et al.) have also implicated host chaperone DnaJ in MS2 L-mediated lysis.

## Curation Decisions
- **ACCEPT**:
  - `GO:0020002` (`host cell plasma membrane`, EXP from PMID:2656650, EXP from PMID:3053640, and IEA from GO_REF:0000044): Immunoelectron microscopy and sucrose density gradient membrane fractionation directly show that L localizes predominantly to the host cytoplasmic membrane and inner-outer membrane adhesion sites.
- **MODIFY**:
  - `GO:0031640` (`killing of cells of another organism`, IEA from GO_REF:0000043) -> `GO:0044659` (`viral release from host cell by cytolysis`), which is a descendant term that specifically captures phage-mediated host cell lysis for virion release.
