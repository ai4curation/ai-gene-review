# Curation Notes for *Variovorax paradoxus* S110 `iadC` (`C5CSP5`, `Vapar_1492`)

## Overview
- **UniProt Accession:** `C5CSP5` (`C5CSP5_VARPS`)
- **Ordered Locus Name:** `Vapar_1492`
- **Gene Symbol:** `iadC`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Class IA NADH-dependent FMN- and `[2Fe-2S]`-containing reductase component (`IadC`, 330 aa) of the indole-3-acetic acid (IAA) Rieske non-heme iron dioxygenase system (`IadC–IadD/IadE`).

## Literature & Structural Evidence
1. **In Vivo Requirement for Rapid IAA Degradation and RGI Reversion (`PMID:36266335`):**
   - Conway et al. (2022) demonstrated that while `iadDE` expressed in *E. coli* can slowly convert IAA using endogenous surrogate reductases, co-expression of `iadC` (`iadCDE`) substantially accelerates IAA turnover in vivo and in vitro.
   - Crucially, in *Variovorax* (`ΔiadC`), deletion of `iadC` drastically reduces the rate of IAA degradation and abolishes the ability of *Variovorax* to rescue *Arabidopsis* root growth inhibition (RGI) caused by the IAA-producing commensal *Arthrobacter* CL28 (`PMID:36266335`).

2. **Crystal Structure and Electron Transfer Mechanism (`PMID:37459330`):**
   - Ma et al. (2023) solved the 1.82 Å crystal structure of *Variovorax paradoxus* S110 `IadC` (PDB `7YLR`, mapped to `C5CSP5`).
   - `IadC` (330 aa) is a monomeric Class IA Rieske dioxygenase reductase comprising three domains:
     1. **FMN-binding domain (residues 1–115):** Six-stranded antiparallel $\beta$-barrel that non-covalently binds flavin mononucleotide (FMN); the isoalloxazine ring is positioned 5.2 Å from the `[2Fe-2S]` cluster (`PMID:37459330`).
     2. **NADH-binding domain (residues 116–238):** Classic $\alpha/\beta$ Rossmann-like fold (`PMID:37459330`).
     3. **Plant-type `[2Fe-2S]` ferredoxin domain (residues 239–329):** Connected via a loop (residues 239–249) and coordinates a `[2Fe-2S]` cluster via four conserved cysteine residues (`Cys274`, `Cys279`, `Cys282`, and `Cys314`) (`PMID:37459330`).
   - `IadC` oxidizes NADH, reduces FMN, transfers electrons intramolecularly to its `[2Fe-2S]` cluster, and shuttles electrons intermolecularly to the Rieske `[2Fe-2S]` cluster of `IadD` in the `IadD/IadE` oxygenase complex (`PMID:37459330`).

## Review of Existing GOA Annotations
- `GO:0051537` (`2 iron, 2 sulfur cluster binding`, IEA) -> **ACCEPT** (directly supported by PDB `7YLR` where `Cys274`, `Cys279`, `Cys282`, and `Cys314` coordinate the `[2Fe-2S]` cluster, `PMID:37459330`).
- `GO:0051536` (`iron-sulfur cluster binding`, IEA) -> **MODIFY** to `GO:0051537` (`2 iron, 2 sulfur cluster binding`) (since `GO:0051536` is a general parent term and the exact `[2Fe-2S]` stoichiometry is established by X-ray crystallography in `PMID:37459330`).
- `GO:0016491` (`oxidoreductase activity`, IEA) -> **MODIFY** to `GO:0008860` (`ferredoxin-NAD+ reductase activity`).

## Proposed New Annotations
- `GO:0008860` (`ferredoxin-NAD+ reductase activity`) — `enables`, supported by `PMID:36266335` and `PMID:37459330`.
- `GO:0010181` (`FMN binding`) — `enables`, supported by crystal structure PDB `7YLR` and flavin quantification in `PMID:37459330`.
- `GO:0042437` (`indoleacetic acid catabolic process`) — `involved_in`, supported by `PMID:36266335` and `PMID:37459330`.
- `GO:0005829` (`cytosol`) — `located_in`, supported by `PMID:37459330`.
