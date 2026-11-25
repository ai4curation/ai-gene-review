# Curation Notes for *Variovorax paradoxus* `acdS` (`Q6J256`, `ACDS_VARPD`)

## Overview
- **UniProt Accession:** `Q6J256` (`ACDS_VARPD`)
- **Gene Symbol:** `acdS`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`)
- **Protein Function:** Pyridoxal 5'-phosphate (PLP)-dependent 1-aminocyclopropane-1-carboxylate (ACC) deaminase (`AcdS`, 338 aa, EC 3.5.99.7) that catalyzes the ring-opening deamination of the immediate plant ethylene precursor ACC into $\alpha$-ketobutyrate (`2-oxobutanoate`) and ammonia (`NH3`).

## Literature & Structural/Domain Evidence
1. **UniProt Swiss-Prot Reviewed Entry (`UniProtKB:Q6J256`):**
   - `Q6J256` (`ACDS_VARPD`) is a Swiss-Prot reviewed entry supported by HAMAP rule `MF_00656` (`InterPro:IPR005965`).
   - Active-site pyridoxal 5'-phosphate (PLP) cofactor is covalently bound as a Schiff base (`N6-(pyridoxal phosphate)lysine`) at conserved residue `Lys51` (`FT MOD_RES 51`).
   - Catalyzes the reaction: `1-aminocyclopropane-1-carboxylate + H2O = 2-oxobutanoate + NH4+` (EC 3.5.99.7), localized to the cytoplasm (`CC SUBCELLULAR LOCATION: Cytoplasm`).

2. **Role in Rhizosphere Auxin–Ethylene Crosstalk (`PMID:32999461`, `PMID:36266335`):**
   - Finkel et al. (2020) demonstrated that severe root-growth inhibition (RGI) induced by complex microbial communities or synthetic auxins can be triggered through both auxin and ethylene signaling pathways, as high auxin stimulates plant 1-aminocyclopropane-1-carboxylate (ACC) synthase and ethylene biosynthesis (`PMID:32999461`).
   - While all RGI-reverting *Variovorax* strains possess the conserved `iad` auxin-catabolic locus (`PMID:32999461`, `PMID:36266335`), a subset of *Variovorax paradoxus* strains (such as *V. paradoxus* 5C-2, whereas S110 lacks `acdS`) additionally encode `acdS` (`Q6J256`), enabling dual buffering of rhizosphere phytohormones by simultaneously degrading indole-3-acetic acid (`IadCDE`) and cleaving the ethylene precursor ACC (`AcdS`).

## Review of Existing GOA Annotations
- `GO:0008660` (`1-aminocyclopropane-1-carboxylate deaminase activity`, IEA via UniProtKB-EC / InterPro / HAMAP) -> **ACCEPT** (core enzymatic function of `AcdS`).
- `GO:0030170` (`pyridoxal phosphate binding`, IEA via InterPro / UniProtKB-KW) -> **ACCEPT** (PLP cofactor covalently linked at `Lys51`).
- `GO:0005737` (`cytoplasm`, IEA via HAMAP / UniProtKB-SubCell) -> **ACCEPT** (cytosolic/cytoplasmic enzyme).

## Proposed New Annotations
- `GO:0042217` (`1-aminocyclopropane-1-carboxylate catabolic process`) — `involved_in`, supported by `UniProtKB:Q6J256` (`FT_DOMAIN`, `CC_CATALYTIC_ACTIVITY`, `DR_HAMAP`) and `PMID:32999461`.
