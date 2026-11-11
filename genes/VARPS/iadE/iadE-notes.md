# Curation Notes for *Variovorax paradoxus* S110 `iadE` (`C5CSP7`, `Vapar_1494`)

## Overview
- **UniProt Accession:** `C5CSP7` (`C5CSP7_VARPS`)
- **Ordered Locus Name:** `Vapar_1494`
- **Gene Symbol:** `iadE`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Structural beta subunit (`IadE`, 162 aa) of the heterohexameric ($\alpha_3\beta_3$) indole-3-acetic acid (IAA) Rieske non-heme iron aromatic-ring-hydroxylating dioxygenase complex (`IadD/IadE`).

## Literature & Structural Evidence
1. **Discovery & Genetic Requirement in the `iad` Operon (`PMID:32999461`, `PMID:36266335`):**
   - `iadE` (`Vapar_1494`) is co-transcribed immediately downstream of `iadD` (`Vapar_1493`) in the *Variovorax* auxin-degradation (`iad`) operon (`PMID:32999461`, `PMID:36266335`).
   - Conway et al. (2022) demonstrated that `iadD` and `iadE` (`iadDE`) are the minimal gene pair required and sufficient for IAA transformation when expressed heterologously in *E. coli*, and deletion of `iadDE` in *Variovorax* completely abolishes IAA catabolism and the ability to revert root-growth inhibition (RGI) in *Arabidopsis* seedlings (`PMID:36266335`).

2. **Crystal Structure and Role in the $\alpha_3\beta_3$ Heterohexamer (`PMID:37459330`):**
   - Ma et al. (2023) determined the crystal structures of apo and IAA-bound *V. paradoxus* S110 `IadD/IadE` (PDB `7YLS` and `8H2T`).
   - `IadE` (162 aa) adopts an NTF2-like (nuclear transport factor 2-like) $\alpha+\beta$ barrel fold and trimerizes to form the structural "stem" base of the mushroom-shaped $\alpha_3\beta_3$ `IadD/IadE` heterohexamer, stabilizing the trimeric `IadD` catalytic cap (`PMID:37459330`).
   - Unlike `IadD`, `IadE` lacks metal-binding centers or an active-site pocket, functioning as the obligate structural scaffold subunit of the two-component Rieske dioxygenase oxygenase component (`IadD/IadE`). While purified `IadD` alone can bind IAA weakly ($K_d = 24.1\text{ }\mu\text{M}$ vs $17.0\text{ }\mu\text{M}$ for `IadD/IadE`), the intact `IadD/IadE` complex is the physiological holoenzyme that receives electrons from `IadC` to oxygenate IAA (`PMID:37459330`).

## Review of Existing GOA Annotations
- `GO:0019380` (`3-phenylpropionate catabolic process`, IEA via TreeGrafter `GO_REF:0000118`, `PANTHER:PTN002222818`) -> **REMOVE**!
  - **Rationale:** TreeGrafter over-propagated `3-phenylpropionate catabolic process` from a distant paralogous aromatic dioxygenase beta subunit (such as *E. coli* HcaF in `PTHR43780`). Direct biochemical, structural, and genetic characterization of *V. paradoxus* S110 `IadD/IadE` (`PMID:36266335`, `PMID:37459330`) proves that `IadE` is the beta subunit of the indole-3-acetic acid (IAA) dioxygenase complex (`IadD/IadE`), which specifically catabolizes IAA and shows no physiological role in 3-phenylpropionate catabolism.

## Proposed New Annotations
- `GO:0042437` (`indoleacetic acid catabolic process`) — `involved_in`, supported by `PMID:36266335` and `PMID:37459330`.
- `GO:0016708` / `GO:0051213` (`contributes_to` dioxygenase activity as the structural $\beta$ subunit of the $\alpha_3\beta_3$ `IadD/IadE` complex), supported by `PMID:37459330`.
- `GO:0005829` (`cytosol`) — `located_in`, supported by `PMID:37459330`.
