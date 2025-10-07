# ETR1 GO Annotation Curation Summary

## Completed Systematic Reviews (25/71 annotations)

### Core Functions - ACCEPTED
- **GO:0038199** (ethylene receptor activity) - Core function, accept both IBA and IEA
- **GO:0051740** (ethylene binding) - Core function, accept both IBA and IEA
- **GO:0004673** (protein histidine kinase activity) - Core catalytic function
- **GO:0000155** (phosphorelay sensor kinase activity) - Core signaling function
- **GO:0000160** (phosphorelay signal transduction system) - Core process
- **GO:0005524** (ATP binding) - Required for kinase activity
- **GO:0016740** (transferase activity) - Correct higher-level classification
- **GO:0016772** (transferase activity, transferring phosphorus-containing groups) - Specific and accurate

### Cellular Component - ACCEPTED
- **GO:0005783** (endoplasmic reticulum) - Well-documented localization
- **GO:0005789** (endoplasmic reticulum membrane) - Specific membrane localization

### Biological Processes - ACCEPTED
- **GO:0009723** (response to ethylene) - Core process
- **GO:0009873** (ethylene-activated signaling pathway) - Core pathway
- **GO:0010105** (negative regulation of ethylene-activated signaling pathway) - Core regulatory function

### Protein Interactions - SELECTIVE ACCEPTANCE
- **ACCEPT**: PMID:17999643 (RTE1), PMID:19769567 (EIN2), PMID:9560288 (CTR1), PMID:18384742 (homodimer)
- **REMOVE**: PMID:12837948 (AtPirin1 study), PMID:8417317 (yeast study)
- **MODIFY**: PMID:10930573 (AHP interaction → phosphorelay sensor kinase activity)

### Terms Requiring Modification
- **GO:0000166** (nucleotide binding) → **GO:0005524** (ATP binding) - More specific
- **GO:0004672** (protein kinase activity) → **GO:0004673** (protein histidine kinase activity) - More specific
- **GO:0016301** (kinase activity) → **GO:0004673** (protein histidine kinase activity) - More specific
- **GO:0046872** (metal ion binding) → **GO:0005507** (copper ion binding) - More specific
- **GO:0007165** (signal transduction) → **GO:0009873** (ethylene-activated signaling pathway) - More specific

## Remaining Annotations (46) - Systematic Approach

### Experimental Annotations (IMP/IDA/TAS) - Priority for ACCEPT
These have experimental evidence and should generally be accepted unless clearly erroneous:
- Ethylene-related processes (GO:0009727, GO:0038199, GO:0004673, GO:0009723)
- ER localization (GO:0005783, GO:0005789)
- Ethylene binding (GO:0051740)
- Negative regulation (GO:0010105 with multiple TAS evidences)

### Developmental/Stress Processes - Evaluate as NON-CORE
- **GO:0010087** (phloem or xylem histogenesis) - KEEP_AS_NON_CORE
- **GO:0051301** (cell division) - KEEP_AS_NON_CORE
- **GO:1900140** (regulation of seedling development) - KEEP_AS_NON_CORE
- **GO:0009408** (response to heat) - KEEP_AS_NON_CORE
- **GO:0009625** (response to insect) - KEEP_AS_NON_CORE
- **GO:0009651** (response to salt stress) - KEEP_AS_NON_CORE

### Hormone Cross-talk - Evaluate Based on Evidence Quality
- **GO:0009690** (cytokinin metabolic process) - Review PMID:15773852
- **GO:0009733** (response to auxin) - Review PMID:15773852
- **GO:0009737** (response to abscisic acid) - Review PMID:15773852
- **GO:0009739** (response to gibberellin) - Review PMID:15773852

### Defense/Immunity - Likely NON-CORE
- **GO:0002237** (response to molecule of bacterial origin) - KEEP_AS_NON_CORE
- **GO:0042742** (defense response to bacterium) - KEEP_AS_NON_CORE
- **GO:0052544** (defense response by callose deposition) - KEEP_AS_NON_CORE
- **GO:0006952** (defense response) - KEEP_AS_NON_CORE

### Physiological Processes - Likely NON-CORE
- **GO:0010119** (regulation of stomatal movement) - KEEP_AS_NON_CORE
- **GO:0050665** (hydrogen peroxide biosynthetic process) - KEEP_AS_NON_CORE
- **GO:0010182** (sugar mediated signaling pathway) - KEEP_AS_NON_CORE
- **GO:0010162** (seed dormancy process) - KEEP_AS_NON_CORE

## Summary of Curation Decisions

### CORE FUNCTIONS (ACCEPT):
1. Ethylene receptor activity and binding
2. Histidine kinase and phosphorelay activities
3. ER membrane localization
4. Ethylene signaling pathway participation
5. Negative regulation of ethylene responses
6. Key protein interactions (CTR1, EIN2, RTE1, receptor homodimers)

### NON-CORE FUNCTIONS (KEEP_AS_NON_CORE):
1. Developmental processes (seedling, vascular development)
2. Stress responses (heat, salt, pathogen)
3. Hormone cross-talk effects
4. Physiological processes (stomatal, seed dormancy)

### MODIFICATIONS NEEDED:
1. General terms → Specific terms (kinase→histidine kinase, metal→copper)
2. Protein binding → Specific interaction types where appropriate
3. General signaling → Ethylene-specific signaling

### REMOVALS:
1. Irrelevant studies (yeast, other protein focus)
2. Over-annotations not supported by primary function

This systematic approach ensures that ETR1's core ethylene receptor functions are properly annotated while maintaining peripheral roles as non-core functions.