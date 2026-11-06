# Curation Notes for *Variovorax paradoxus* S110 `amiE` (`C5CWZ4`, `AMIE_VARPS`, `Vapar_0135`)

## Overview
- **UniProt Accession:** `C5CWZ4` (`AMIE_VARPS`)
- **Ordered Locus Name:** `Vapar_0135`
- **Gene Symbol:** `amiE`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Aliphatic amidase (`AmiE`, 344 aa, EC 3.5.1.4) of the carbon-nitrogen hydrolase (`CN_hydrolase`, `Pfam:PF00795`, `HAMAP:MF_01242`, `InterPro:IPR023719`) superfamily that hydrolyzes short-chain aliphatic amides to their corresponding organic acids and ammonia.

## Literature & Domain Evidence
1. **Genomic & Metabolic Context in *Variovorax paradoxus* S110 (`PMID:21183664`):**
   - Han et al. (2011) sequenced the complete 6.75 Mb biphasic genome of *Variovorax paradoxus* S110 and highlighted its diverse catabolic repertoire enabling utilization of organic nitrogen and carbon substrates in the rhizosphere (`PMID:21183664`).
2. **Conserved Nitrilase/Amidase Catalytic Triad (`UniProtKB:C5CWZ4`):**
   - `C5CWZ4` (`AMIE_VARPS`) is a Swiss-Prot reviewed entry curated under HAMAP rule `MF_01242` (`InterPro:IPR023719`, aliphatic amidase `AmiE`).
   - Contains the conserved `Glu-Lys-Cys` catalytic triad characteristic of the carbon-nitrogen hydrolase superfamily:
     - `Glu59` (`FT ACT_SITE 59`, proton acceptor)
     - `Lys134` (`FT ACT_SITE 134`, proton donor)
     - `Cys166` (`FT ACT_SITE 166`, nucleophilic cysteine that forms the covalent acyl-enzyme thioester intermediate).
   - In the rhizosphere, `AmiE` hydrolyzes short-chain linear aliphatic amides to liberate bioavailable ammonium (`NH4+`) and monocarboxylates.

## Review of Existing GOA Annotations
- `GO:0004040` (`amidase activity`, IEA via HAMAP / InterPro / UniProtKB-EC) -> **ACCEPT** (core catalytic activity, EC 3.5.1.4).
- `GO:0016811` (`hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides`, IEA via InterPro) -> **TOO_GENERAL** (subsumed by the accepted child term `GO:0004040` `amidase activity`).
- `GO:0005829` (`cytosol`, IC) -> **NEW** (inferred by curator from soluble cytoplasmic HAMAP `MF_01242` family membership and lack of signal peptides or transmembrane segments).
