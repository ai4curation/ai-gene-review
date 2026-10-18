# Bacteriophage P2 Gene lysA (Antiholin LysA; UniProt P51769)

## Overview
Gene **lysA** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a 141-amino-acid four-transmembrane inner-membrane protein (15.5 kDa; `UniProt:P51769`, `InterPro:IPR009218` / `PF05929`) that acts as a specific antiholin regulating the P2 class I holin gpY (`PMID:8051010`, `PMID:23335412`). An amber mutation in `lysA` causes accelerated lysis (`PMID:8051010`), and co-expression of `lysA` in trans with a chimeric $\lambda\text{-}Y$ phage specifically delays gpY-mediated host lysis by ~10 minutes and increases progeny phage burst size (PFU/ml) by ~50% without altering gpY protein accumulation (`PMID:23335412`).

## Key Literature & Experimental Evidence
- **PMID:8051010** (*Functions involved in bacteriophage P2-induced host cell lysis and identification of a new tail gene.*):
  - `"The gene products of lysA and lysB, although nonessential, appear to play a role in the correct timing of lysis, since a lysA amber mutant caused slightly accelerated lysis and a lysB amber mutant slightly delayed lysis of nonpermissive strains."`
- **PMID:23335412** (*Functional analysis of a class I holin, P2 Y.*):
  - `"Finally, instead of encoding a second translational product of Y as an antiholin, as shown for lambda S107, the P2 lysis cassette encodes another predicted membrane protein, LysA, which is shown here to have a Y-specific antiholin character."`
  - `"Induction of λ- Y lysogens transformed with the lysA construct resulted in lysis ~10 min later than the same lysogen transformed with the isogenic vector ( Fig. 4B ), with an ~50% increase in the yield of PFU (1.4 × 10 9 PFU/ml versus 9.3 × 10 8 PFU/ml) in the final lysate, without affecting the accumulation of Y (data not shown)."`

## Curation Decisions
- **Molecular Function**:
  - No specific molecular function term is directly assayed in the cached literature; `core_functions` therefore captures its antiholin role via the biological process (`GO:0044659`) and host inner membrane location (`GO:0020002`).
- **Biological Process**:
  - `GO:0031640` (`killing of cells of another organism`, IEA): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`).
  - `GO:0044659` (`viral release from host cell by cytolysis`): **NEW** supported by `PMID:8051010` and `PMID:23335412` (regulates the timing of holin-mediated cytolytic viral release to maximize burst size).
- **Cellular Component**:
  - `GO:0020002` (`host cell plasma membrane`, IEA): **ACCEPT**
