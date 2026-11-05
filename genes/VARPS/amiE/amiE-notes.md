# Curation Notes for *Variovorax paradoxus* S110 `amiE` (`C5CWZ4`, `AMIE_VARPS`, `Vapar_3054`)

## Overview
- **UniProt Accession:** `C5CWZ4` (`AMIE_VARPS`)
- **Ordered Locus Name:** `Vapar_3054`
- **Gene Symbol:** `amiE`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Aliphatic amidase (`AmiE`, 343 aa, EC 3.5.1.4) of the nitrilase/cyanide hydratase (`CN_hydrolase`, `Pfam:PF00795`, `HAMAP:MF_00658`) superfamily that hydrolyzes short-chain aliphatic amides (such as acetamide, propionamide, and acrylamide) to their corresponding organic acids and ammonia.

## Literature & Domain Evidence
1. **Genomic & Metabolic Context in *Variovorax paradoxus* S110 (`PMID:21183664`):**
   - Han et al. (2011) sequenced the complete 6.75 Mb biphasic genome of *Variovorax paradoxus* S110 and highlighted its diverse catabolic repertoire enabling utilization of recalcitrant organic nitrogen and carbon substrates in the rhizosphere (`PMID:21183664`).
2. **Conserved Nitrilase/Amidase Catalytic Triad (`UniProtKB:C5CWZ4`):**
   - `C5CWZ4` (`AMIE_VARPS`) is a Swiss-Prot reviewed entry curated under HAMAP rule `MF_00658` (`InterPro:IPR011692`, aliphatic amidase `AmiE`).
   - Contains the conserved `Glu-Lys-Cys` catalytic triad characteristic of the nitrilase superfamily:
     - `Glu59` (`FT ACT_SITE 59`)
     - `Lys134` (`FT ACT_SITE 134`)
     - `Cys166` (`FT ACT_SITE 166`, nucleophilic cysteine that forms the covalent acyl-enzyme thioester intermediate).
   - Forms a homohexamer (`CC SUBUNIT: Homohexamer`, `CC SUBCELLULAR LOCATION: Cytoplasm`).
   - In the rhizosphere, `AmiE` frequently operates downstream of nitrile hydratases or plant/microbial amide exudation to liberate bioavailable ammonium (`NH4+`) and short-chain carboxylates.

## Review of Existing GOA Annotations
- `GO:0004040` (`amidase activity`, IEA via HAMAP / InterPro / UniProtKB-EC) -> **ACCEPT** (core catalytic activity, EC 3.5.1.4).
- `GO:0016811` (`hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides`, IEA via UniProtKB-KW) -> **MODIFY** to `GO:0004040` (`amidase activity`) (as `GO:0016811` is a broader parent term of `GO:0004040`).
- `GO:0005737` (`cytoplasm`, IEA via HAMAP / UniProtKB-SubCell) -> **ACCEPT** (cytoplasmic localization).
