# HSFA1A (AT4G17750) Curation Notes

## Gene Summary
**Primary master regulator** of heat stress response in Arabidopsis [PMID:21931939, deep-research:perplexity]

## Core Function (Molecular Activity)
- **DNA-binding transcription factor** - binds heat shock elements (HSE): 5'-AGAAnnTTCT-3' [UniProt, deep-research]
- Forms **homotrimers** for high-affinity DNA binding and transactivation [UniProt, deep-research]
- Contains **AHA transcriptional activation domain** [UniProt, deep-research]

## Key Biological Processes

### Heat Stress Response (PRIMARY/CORE)
- Master regulator initiating the heat shock transcriptional cascade [deep-research]
- Directly activates HSP genes: HSP17, HSP70, HSP90, HSP101 [deep-research]
- Essential for **acquired thermotolerance** - triple/quadruple KO of HSFA1A/B/D/E abolishes thermotolerance [deep-research]
- Activates HSFA2 (amplifier) and other secondary HSFs [deep-research]

### Drought Stress (SECONDARY)
- Induces autophagy genes (ATG10, ATG18f) for protein quality control [deep-research PMID:26408532]
- Overexpression enhances drought tolerance [deep-research]

### Pathogen Defense (SECONDARY)
- Regulates ROS production via Wfi1 (RBOH) [deep-research PMID:28017714]
- Required for Mi-1.2-mediated resistance to root-knot nematodes [deep-research]

### Other Stress Responses
- Salt, osmotic, oxidative stress (less potent than HSFA1E for salt/osmotic) [deep-research]

### Developmental Role
- **Thermomorphogenesis** - regulates growth responses to ambient temperature changes (17°C→27°C) [deep-research]
- Distinct from acute heat stress response [deep-research]

## Regulation of HSFA1A Activity

### By Molecular Chaperones
- **HSP70/HSP90 bind to TDR domain** → inactive, monomeric form under non-stress conditions [UniProt PMID:11807141, deep-research]
- Heat stress → HSP70 dissociates → trimerization → nuclear translocation → activation [deep-research]
- **HOPs (HSP70-HSP90 organizing proteins)** stabilize HSFA1A, prevent proteasomal degradation [deep-research]

### Post-Translational Modifications
- **SUMOylation** (thermosensitive, abolished at 50°C) [deep-research]
- **Phosphorylation** by CRK1 (calmodulin-binding protein kinase 3) [UniProt PMID:18466301]
- Temperature-dependent phosphorylation [UniProt]

### Other Regulators
- **HSBP** (heat shock binding protein) - negative regulator via nuclear translocation [UniProt PMID:20388662]

## Chromatin Remodeling & 3D Organization
- Facilitates **promoter-enhancer loop formation** during heat stress [deep-research]
- Mediates **H2A.Z nucleosome displacement** at target genes [deep-research]
- Reorganizes 3D genome structure for amplified transcriptional response [deep-research]

## Protein Interactions
- **HSP70-1, HSP70-4** - regulatory interactions [UniProt PMID:11807141]
- **CRK1** - phosphorylates HSFA1A [UniProt PMID:18466301]
- **HSBP** - negative regulator [UniProt PMID:20388662, PMID:20657173]
- **TBP1, TBP2** (TATA-binding proteins) [UniProt IntAct]
- **HOPs** (AtHOP1/2/3) - stabilization [deep-research]
- Forms heterodimers with **HSFA2** for cooperative activation [deep-research]

## Subcellular Localization
- **Cytoplasm** (under normal conditions, HSP70-bound) [UniProt, deep-research]
- **Nucleus** (upon heat stress, active form) [UniProt, deep-research]
- Dynamic stress-dependent translocation [deep-research]

## Target Genes (Direct)
- **HSP genes**: HSP17, HSP70, HSP90, HSP101 [deep-research]
- **Autophagy genes**: ATG10, ATG18f [deep-research]
- **Antioxidant enzymes**: Cu/Zn-SOD, GSTs, MDAR [deep-research]
- **Secondary HSFs**: HSFA2, HSFB2B, HSFA7A [deep-research]
- **Other TFs**: DREB2A, RAP2.4, EPR1, bZIP28 [deep-research]
- **ROS production**: Wfi1 (RBOH) [deep-research]
- ~5000 putative binding sites genome-wide [deep-research]

## Genetic Evidence
- **Quadruple KO** (hsfa1a/b/d/e) → no acquired thermotolerance [deep-research]
- **Triple KO** (hsfa1a/b/d) → dramatic thermotolerance defects [deep-research]
- **Knockdown** → reduced heat stress-induced gene expression, compromised pathogen resistance [deep-research]
- **Overexpression** → enhanced drought tolerance, enhanced HSP expression [deep-research]

## Expression Pattern
- **Constitutively expressed** [UniProt PMID:7948881]
- **Strongly induced by heat stress** [UniProt PMID:7948881]

## Structural Features
- **DNA-binding domain (DBD)** with helix-turn-helix motif [deep-research]
- **Oligomerization domain (OD)** with leucine zipper motifs [deep-research, UniProt]
- **AHA activation domain** (C-terminal) [deep-research, UniProt]
- **TDR domain** (temperature-dependent repression) - mediates HSP70/90 interaction [deep-research]
- **Nuclear localization signal (NLS)** [deep-research]
- Conserved R107 residue critical for DNA-binding affinity [deep-research]

## Functional Specialization
- **HSFA1A** - most potent thermotolerance inducer (but less effective for salt/osmotic stress)
- **HSFA1B** - cooperates with HSFA1A for early heat response
- **HSFA1D** - intermediate activity, contributes to salt/osmotic stress
- **HSFA1E** - no thermotolerance alone, but strong salt/osmotic tolerance
- Subfunctionalization allows stress-specific responses [deep-research]

## Curation Strategy
1. **ACCEPT** core heat stress response annotations (cellular response to heat, HSF activity)
2. **ACCEPT** DNA-binding transcription factor activity
3. **ACCEPT** nucleus and cytoplasm localization
4. **KEEP_AS_NON_CORE** general transcription regulation (too broad)
5. **MODIFY** if terms are too general → find more specific GO terms
6. **ADD** missing key functions:
   - Transcriptional activator activity (sequence-specific)
   - Heat shock protein binding (for HSP70/HSP90 interactions)
   - Autophagy regulation (drought-specific)
   - ROS-mediated pathogen defense
   - Thermomorphogenesis
   - Chromatin remodeling
7. **REMOVE** any over-annotations or unsupported terms

## References
- UniProt: P41151
- Deep research: AT4G17750-deep-research-perplexity.md (37 citations)
- Key PMIDs: 21931939, 11807141, 18466301, 20388662, 20657173, 7948881
