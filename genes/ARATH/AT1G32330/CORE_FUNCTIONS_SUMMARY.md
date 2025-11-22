# HSFA1D (AT1G32330) Core Functions Synthesis Summary

## Updated Sections

### 1. Description Field
**Updated description emphasizes:**
- **Co-master regulator status** - equal to HSFA1A/B, not subordinate
- **Unique regulatory integration** - light (CRY1), circadian (CCA1/LHY), hormone (BIN2/COP1)
- **Intermediate activity level** - compared to HSFA1A/B for heat stress
- **Broader stress response range** - chilling, salt/osmotic stress

### 2. Core Functions (5 distinct functions)

#### Function 1: Core Heat Stress Response (Shared with HSFA1A/B)
**Key features:**
- Co-master regulator with equal status alongside HSFA1A and HSFA1B
- Binds HSE elements (5'-nGAAn-3' repeats)
- Activates HSPs (HSP17, HSP70, HSP90, HSP101)
- Activates secondary transcription factors (HSFA2, DREB2A)
- Essential for acquired thermotolerance (triple KO evidence)

**GO annotations:**
- MF: GO:0003700 (DNA-binding transcription factor activity)
- BP: GO:0034605 (cellular response to heat)
- BP: GO:0045944 (positive regulation of transcription by RNA polymerase II)
- CC: GO:0005634 (nucleus), GO:0005737 (cytoplasm)

#### Function 2: Light-Dependent Thermomorphogenesis (UNIQUE)
**Key features:**
- Integrates blue light signaling via CRY1 photoreceptor
- CRY1 enhances nuclear localization through IMPα1 interaction
- Light-induced thermotolerance (LIT) - anticipatory stress response
- cry1 mutants show reduced thermotolerance after light pretreatment
- Enables preparation for elevated temperatures during sunny conditions

**GO annotations:**
- MF: GO:0000978 (RNA pol II cis-regulatory region sequence-specific DNA binding)
- BP: GO:0071483 (cellular response to blue light) - **NEW**
- BP: GO:0140919 (thermomorphogenesis) - **NEW**
- BP: GO:0034605 (cellular response to heat)
- CC: GO:0005634 (nucleus)

#### Function 3: Circadian-Gated Stress Response (UNIQUE)
**Key features:**
- Time-of-day-dependent heat stress responses
- Integration with CCA1/LHY clock components
- 70% of heat-responsive genes show circadian gating
- Allows anticipatory stress responses timed to daily temperature cycles
- Coordinates with circadian rhythms for optimal stress timing

**GO annotations:**
- MF: GO:0003700 (DNA-binding transcription factor activity)
- BP: GO:0032922 (circadian regulation of gene expression) - **NEW**
- BP: GO:0034605 (cellular response to heat)
- CC: GO:0005634 (nucleus)

#### Function 4: Brassinosteroid-Integrated Thermomorphogenesis (UNIQUE)
**Key features:**
- BIN2 kinase phosphorylates HSFA1D → reduces nuclear localization and DNA-binding
- COP1 antagonizes BIN2 → restores HSFA1D activity
- BR signaling promotes HSFA1D function
- Integrates growth hormone (BR) with stress responses
- PIF4 interaction and stabilization for thermomorphogenic hypocotyl elongation

**GO annotations:**
- MF: GO:0003700 (DNA-binding transcription factor activity)
- BP: GO:0140922 (positive regulation of thermomorphogenesis) - **NEW**
- BP: GO:0034605 (cellular response to heat)
- CC: GO:0005634 (nucleus)

#### Function 5: Chilling Tolerance (Broader Stress Response)
**Key features:**
- Activates ribosomal protein genes under chilling conditions
- Maintains protein synthesis capacity under low non-freezing temperatures
- ChIP evidence for direct binding to ribosomal protein gene promoters
- Distinct regulatory mechanisms from heat stress (no increased nuclear accumulation)
- NPR1-dependent basal nuclear localization under chilling
- hsfa1d mutants show reduced hypocotyl elongation under chilling

**GO annotations:**
- MF: GO:0003700 (DNA-binding transcription factor activity)
- BP: GO:0009409 (response to cold) - **NEW**
- BP: GO:0045944 (positive regulation of transcription by RNA polymerase II)
- CC: GO:0005634 (nucleus)

## Functional Distinctions from HSFA1A/B

### Shared Features (Functional Redundancy)
- Co-master regulator status (equal importance)
- Constitutive expression
- Essential for thermotolerance (triple/quadruple KO evidence)
- Binds HSE elements, activates HSPs
- Regulated by HSP70/HSP90 chaperones

### HSFA1D-Specific Features (Unique Integration)
1. **Light integration**: CRY1-dependent nuclear import enhancement
2. **Circadian regulation**: Time-of-day gating (70% of heat genes)
3. **BR signaling**: BIN2/COP1 pathway modulation
4. **Broader stress range**:
   - Intermediate activity for heat (between HSFA1A/B strongest and HSFA1E weakest)
   - Stronger contribution to salt/osmotic stress
   - Chilling tolerance through ribosomal protein gene activation
5. **Developmental role**: Hypocotyl elongation under temperature stress

## Evidence Quality

All core functions are supported by:
- **Primary literature** cited in deep-research-perplexity.md (40 citations)
- **Direct experimental evidence** (genetic KOs, ChIP, protein interactions)
- **Mechanistic data** (protein-protein interactions, subcellular localization)
- **Functional assays** (thermotolerance assays, gene expression analysis)

## Validation Status

- YAML file validates successfully
- 5 warnings for NEW GO terms not in existing_annotations (expected and appropriate)
- All GO term IDs verified against Gene Ontology
- Supporting text extracted from authoritative sources

## Next Steps (Optional)

The validator suggests adding these NEW terms to existing_annotations block:
- GO:0071483 (cellular response to blue light)
- GO:0140919 (thermomorphogenesis)
- GO:0032922 (circadian regulation of gene expression)
- GO:0140922 (positive regulation of thermomorphogenesis)
- GO:0009409 (response to cold)

These could be added as proposed new annotations with action: NEW, but this is not required for the core_functions section to be complete and valid.
