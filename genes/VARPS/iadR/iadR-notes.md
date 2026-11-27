# Curation Notes for *Variovorax paradoxus* S110 `iadR` (`C5CSP2`, `Vapar_1489`)

## Overview
- **UniProt Accession:** `C5CSP2` (`C5CSP2_VARPS`)
- **Ordered Locus Name:** `Vapar_1489`
- **Gene Symbol:** `iadR` (also designated `MarR_73` in Conway et al. 2022)
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Indole-3-acetic acid (IAA)-sensing MarR-family DNA-binding transcriptional repressor (`IadR`, 158 aa) that negatively regulates transcription of the *Variovorax* `iad` auxin-catabolic operon in the absence of IAA and derepresses it upon direct IAA binding.

## Literature & Structural Evidence
1. **Discovery of the Auxin-Responsive `iad` Operon (`PMID:32999461`):**
   - Finkel et al. (2020) showed that the *Variovorax* auxin-degradation hotspot 33 is strongly upregulated at the transcriptional level when *Variovorax* is exposed to exogenous IAA or co-cultured with IAA-producing bacteria (`PMID:32999461`).

2. **Genetic, Biochemical, and Structural Characterization of `IadR` (`MarR_73`, `PMID:36266335`):**
   - Conway et al. (2022) identified `iadR` (`Vapar_1489` in *V. paradoxus* S110; `MarR_73`) at the 5' boundary of the `iad` operon and proved that it functions as an IAA-responsive transcriptional repressor (`PMID:36266335`).
   - **Genetic evidence:** Deletion of `iadR` (`ΔiadR`) results in constitutive expression of the `iad` operon and constitutive IAA degradation even without prior IAA induction (`PMID:36266335`).
   - **Direct ligand binding (ITC):** Isothermal titration calorimetry (ITC) demonstrated that `IadR` binds IAA directly with high affinity ($K_d = 0.41 \pm 0.03\text{ }\mu\text{M}$), whereas synthetic auxins such as 2,4-dichlorophenoxyacetic acid (2,4-D) bind ~30-fold more weakly ($K_d = 12 \pm 1\text{ }\mu\text{M}$) and fail to efficiently derepress the `iad` operon in vivo (`PMID:36266335`).
   - **X-ray crystal structures (PDB `7KFO`, `7KFQ`, `7KFP`, `7KFR`, `7KFS`, `7KFT`, `7KFU`, `7KRG`, `7KRH`):**
     - Conway et al. (2022) solved 9 high-resolution crystal structures of *V. paradoxus* S110 `IadR` (`C5CSP2`) in apo form (`7KFO`) and bound to IAA (`7KFQ`), IBA, IPA, NAA, 2,4-D, 4-Cl-IAA, and indole (`PMID:36266335`).
     - `IadR` forms a canonical MarR-family homodimer with an N/C-terminal helical dimerization domain ($\alpha 1, \alpha 5, \alpha 6$) and a central winged-helix-turn-helix (wHTH) DNA-binding domain ($\alpha 2, \alpha 3, \alpha 4, \beta 1, \beta 2$) (`PMID:36266335`).
     - Each monomer contains an IAA-binding pocket where the indole ring of IAA is stabilized by hydrophobic interactions with `Tyr15` (from the opposing monomer), `Ala18`, `Trp45`, `Arg46`, and `Val65`, while the carboxylate group forms a salt bridge and hydrogen-bonding network with `Arg46`, `His32`, and `Ser28` (`PMID:36266335`).
     - **Mechanism of derepression:** Electrophoretic mobility shift assays (EMSAs) showed that apo `IadR` binds specifically to a 24 bp palindromic operator sequence in the intergenic promoter region between `iadR` and `iadA`, where the recognition helices ($\alpha 4$) are separated by ~38 Å to fit consecutive major grooves of B-DNA. Binding of IAA induces a conformational shift in the dimer that releases `IadR` from the operator DNA in a concentration-dependent manner, derepressing transcription of the `iad` operon (`PMID:36266335`).

## Review of Existing GOA Annotations
- `GO:0003677` (`DNA binding`, IEA) -> **MODIFY** to `GO:0000976` (`transcription cis-regulatory region binding`) or `GO:1990837` (`sequence-specific double-stranded DNA binding`) (since EMSA in `PMID:36266335` demonstrates sequence-specific binding to the 24 bp operator in the `iadR–iadA` intergenic regulatory region).
- `GO:0003700` (`DNA-binding transcription factor activity`, IEA) -> **MODIFY** to `GO:0001217` (`DNA-binding transcription repressor activity`) (since `ΔiadR` genetics and operator binding in `PMID:36266335` establish that `IadR` is a transcriptional repressor).
- `GO:0006351` (`DNA-templated transcription`, IEA) -> **REMOVE** (obsolete/inappropriate for transcription factors per GO curation guidelines; `IadR` regulates transcription rather than catalyzing RNA polymerization).
- `GO:0006355` (`regulation of DNA-templated transcription`, IEA) -> **MODIFY** to `GO:0045892` (`negative regulation of DNA-templated transcription`) (as `IadR` specifically represses transcription of the `iad` operon).
- `GO:0006950` (`response to stress`, IEA via TreeGrafter `PANTHER:PTN000496747`) -> **REMOVE** (TreeGrafter over-propagation from antibiotic/oxidative-stress MarR homologs; `IadR` senses indole-3-acetic acid to regulate auxin catabolism, not a general stress response).

## Proposed New Annotations
- `GO:0001217` (`DNA-binding transcription repressor activity`) — `enables`, supported by `PMID:36266335`.
- `GO:0045892` (`negative regulation of DNA-templated transcription`) — `involved_in`, supported by `PMID:36266335`.
- `GO:0042437` (`indoleacetic acid catabolic process`) — `involved_in`, supported by `PMID:36266335`.
- `GO:0042803` (`protein homodimerization activity`) — `enables`, supported by crystal structures `7KFO`/`7KFQ` in `PMID:36266335`.
