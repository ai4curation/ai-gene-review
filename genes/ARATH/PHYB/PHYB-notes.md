# Phytochrome B (PHYB) P14713 Review Notes

## Gene Overview
- **Gene**: PHYB (AT2G18790)
- **Protein**: Phytochrome B (1172 AA)
- **Alternative Names**: LONG HYPOCOTYL 3 (HY3), OUT OF PHASE 1 (OOP1)
- **Organism**: Arabidopsis thaliana

## Core Molecular Function

PHYB is a **red/far-red light photoreceptor** that undergoes photoconversion between two forms:
- **Pr form**: Absorbs red light (~660nm), inactive form
- **Pfr form**: Absorbs far-red light (~730nm), active form that translocates to nucleus

The protein functions as a **homodimer** and contains a covalently-linked **phytochromobilin chromophore** (at Cys-357) [PMID:24982198 "Crystal structure shows homodimer with phytochromobilin"].

## Key Biological Roles

### 1. Photomorphogenesis
- Inhibits hypocotyl elongation in red light [PMID:8453299 "hy3 mutants have long hypocotyls"]
- Promotes seedling de-etiolation
- Controls stomatal development and function [PMID:19363093]

### 2. Flowering Time Regulation
- Regulates photoperiodic flowering [PMID:22904146 "interacts with VOZ1/VOZ2 to regulate flowering"]
- Interacts with CONSTANS (CO) through PHL [PMID:24127609]

### 3. Circadian Clock Regulation
- Controls circadian phase [PMID:12177480 "oop1 mutant has altered circadian timing"]
- Regulates circadian calcium oscillations [PMID:17982000]

### 4. Temperature Sensing
- Functions as a thermosensor [PMID:27789797 "Phytochromes function as thermosensors"]
- Pfr form is destabilized at warm temperatures
- Associates with promoters in temperature-dependent manner to repress PIF4 targets [PMID:27789797]
- Senses daytime temperature via HEMERA [PMID:30635559]

### 5. Transcriptional Regulation
- Sequence-specific DNA binding [PMID:27789797]
- Promoter-specific chromatin binding [PMID:27789797]
- Negative regulation of transcription via PIF degradation [PMID:27789797]

## Key Protein Interactions

### PIF Transcription Factors
- PIF1, PIF3, PIF4, PIF5, PIF8/UNE10 [multiple PMIDs]
- Light-activated PHYB binds PIFs and promotes their degradation
- This relieves repression of light-responsive genes

### Other Photoreceptors
- CRY1: Interacts specifically in dark/Pr state, not Pfr [PMID:22577138]
- CRY2: Interacts functionally [PMID:11089975]
- phyA, phyC, phyD, phyE: Forms heterodimers [PMID:15273290, PMID:19286967]

### Regulatory Proteins
- HEMERA/PAP5/HMR: Required for photobody formation and temperature sensing [PMID:22895253, PMID:30635559]
- PCH1/PCHL: Control dark reversion [PMID:29263319]
- VOZ1/VOZ2: Flowering regulation [PMID:22904146]
- SMP2, SWAP1, DRT111/SFPS: Splicing factors in photobodies [PMID:35222493, PMID:36282917, PMID:28760995]

## Cellular Localization

Dynamic localization:
- **Cytoplasm**: In darkness (Pr form)
- **Nuclear translocation**: Upon red light activation (Pfr form) [PMID:15707897, PMID:10225946]
- **Nuclear photobodies**: Light-activated Pfr forms subnuclear structures [PMID:29263319, PMID:23321421]
- **Nuclear speckles**: Observed with PAPP5 [PMID:15707897]

## Protein Domains

Based on UniProt and structure:
- N-terminal photosensory module (aa 90-624):
  - PAS domain
  - GAF domain (aa 252-433) - contains chromophore binding site
  - PHY domain
- C-terminal regulatory module:
  - PAS domains (aa 652-723, 786-857)
  - Histidine kinase-related domain (aa 934-1153)

## Review Strategy

### Annotations to ACCEPT as core function:
- Red/far-red light photoreceptor activity
- Homodimerization
- Nuclear localization (light-dependent)
- Photomorphogenesis
- Red light signaling pathway
- Temperature sensing
- Chromatin binding and transcriptional regulation

### Annotations requiring careful review:
- Generic "protein binding" - many PIFs, should be more specific or KEEP_AS_NON_CORE
- Developmental processes (flowering, seed germination) - these are important but downstream
- Stress responses (cold, heat, defense) - PHYB has roles but may be over-annotations

### Terms to avoid:
- Generic "DNA binding" without context
- Generic "signal transduction"
- Processes where PHYB plays indirect/modulatory role

## Key References for Core Function
- PMID:2606345 - Original cloning
- PMID:8453299 - hy3 mutant characterization
- PMID:12177480 - Circadian function
- PMID:24982198 - Crystal structure
- PMID:27789797 - Thermosensor function
- PMID:30635559 - Daytime temperature sensing
- PMID:22895253 - HEMERA interaction

## 2026-09-27: merged the duplicate P14713 review into PHYB

These notes were written for the duplicate review in `genes/ARATH/P14713/`, which covered the same protein (P14713). That folder has been retired and the review now lives here. The GOA file was refreshed and the conflicting verdicts were reconciled:

- The histidine-kinase rows (GO:0000155 IEA and IBA, GO:0000160 IBA) are now REMOVE. Plant phytochromes carry a histidine kinase-related domain that lacks the residues needed for HK activity [PMID:19286967 "plant phys have unique C termini that contain two PAS domains and a region homologous to two-component histidine kinases but lacking residues critical to HK activity"]. Before the merge, this file had them as ACCEPT and P14713 had them as KEEP_AS_NON_CORE.
- Plasma membrane (ISM and IBA) is now REMOVE, because PHYB is a soluble protein found in the cytoplasm and nucleus.
- Response to temperature stimulus is now ACCEPT, and thermosensing has been added as a second core function (P14713's view). The sensing is done by the thermal reversion of PHYB's own Pfr state.
- Sequence-specific DNA binding stays MODIFY → promoter-specific chromatin binding. P14713's core function built on sequence-specific DNA binding was not carried over.
