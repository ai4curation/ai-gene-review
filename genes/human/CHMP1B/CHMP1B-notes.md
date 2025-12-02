# CHMP1B Annotation Review Notes

## Gene Overview
CHMP1B (Charged Multivesicular Body Protein 1B) is an ESCRT-III complex component with multiple cellular roles.

## Core Functions (from deep research)
1. **ESCRT-III component** for MVB formation and ILV biogenesis - mediates reverse-topology membrane scission for cargo sorting to lysosomes
2. **Normal-topology membrane scission** (with IST1 partner) - mediates endosomal recycling (transferrin receptor, M6PR)
3. **Cytokinetic abscission** - recruits spastin to midbody for final cell division step
4. **Plasma membrane repair** - ESCRT machinery recruited to membrane wounds
5. **Viral budding** - HIV-1 release (moderate role, less essential than CHMP2/CHMP4)
6. **Autophagy** - required for autophagosome maturation and fusion with lysosomes

## Key Evidence
- Peripherally associated ESCRT-III component [UniProt Q7LBR1]
- Forms IST1-CHMP1B copolymers for normal-topology scission [deep research]
- Interacts with VPS4 ATPases for ESCRT-III disassembly
- Interacts with spastin MIT domain for midbody recruitment [PMID:18997780]
- Required for EGFR degradation, regulated by USP8-mediated ubiquitination
- Localizes to: late endosomes, MVB membranes, midbodies, autophagosomes

## Annotation Review Strategy
1. ACCEPT: Core ESCRT-III functions with strong experimental evidence
2. MODIFY: Terms that are too general or need specificity
3. KEEP_AS_NON_CORE: Pleiotropic/secondary functions with decent evidence
4. REMOVE/MARK_AS_OVER_ANNOTATED: Weak IEA annotations, especially those without strong lit support
5. Avoid "protein binding" - not informative, replace with specific MF terms

## Key Papers to Reference
- PMID:17984323 - Autophagy, MVB function in protein aggregates
- PMID:20616062 - Centrosome and spindle maintenance, cytokinesis
- PMID:24482116 - Plasma membrane repair
- PMID:26040712 - Spastin recruitment, spindle disassembly
- PMID:26040713 - Nuclear envelope reformation
- PMID:24878737 - ESCRT-III structure, HIV budding
- PMID:16554368 - MVB sorting, EGFR degradation

---

## REVIEW COMPLETED - Summary

**Date:** 2025-11-23
**Status:** COMPLETE

### Summary Statistics
- **Total annotations reviewed:** 117
- **ACCEPT:** 66 annotations (core ESCRT-III functions)
- **KEEP_AS_NON_CORE:** 17 annotations (mitotic/kinetochore functions)
- **MODIFY:** 10 annotations (terms needing replacement)
- **REMOVE:** 4 annotations (extracellular exosome contaminants, inappropriate yeast terms)

### Key Decisions

1. **Accepted core functions:**
   - MVB/late endosome localization and membrane remodeling
   - Autophagosome maturation and lysosome transport
   - Midbody abscission and nuclear envelope reformation
   - Plasma membrane repair
   - Cargo sorting via MVB pathway
   - MIT domain binding (highly specific MF)
   - Identical protein binding (ESCRT-III oligomerization)

2. **Non-core but valid functions:**
   - Kinetochore/mitotic functions (chromosome alignment, spindle regulation)
   - Centrosome duplication regulation
   - HIV-1 budding (moderate contributor)

3. **Modified annotations:**
   - Replaced generic "protein transport" with specific MVB sorting terms
   - Replaced yeast-specific "vacuole" terms with mammalian "lysosome" terms
   - Recommended replacing generic "protein binding" IPIs with specific binding terms

4. **Removed annotations:**
   - 3x extracellular exosome (HDA) - likely ESCRT contamination in proteomics
   - Vacuolar transport (yeast IEA) - inappropriate for human

### Core Molecular Functions Identified
- **GO:0090541 (MIT domain binding):** High-affinity binding to VPS4 and spastin for ESCRT-III regulation
- **GO:0042802 (identical protein binding):** Self-assembly into helical filaments for membrane constriction

### Notable Insights
- CHMP1B exhibits **dual topology specificity** - unique among ESCRT-III proteins
- Forms IST1-CHMP1B copolymers specifically for normal-topology scission
- Regulated by USP8-mediated deubiquitination in response to growth factors
- Bifunctional MIM motif enables context-dependent VPS4 vs spastin recruitment
