# SAS3 Gene Annotation Review - Curation Summary

**Gene:** SAS3 (Histone acetyltransferase SAS3)
**UniProt ID:** P34218
**Organism:** Saccharomyces cerevisiae
**Review Date:** 2025-12-31

---

## Executive Summary

Reviewed 38 GO annotations for yeast SAS3, the catalytic subunit of the NuA3 histone acetyltransferase complex. SAS3 is fundamentally different from its paralog SAS2:
- **SAS3** primarily regulates transcription activation via H3K14 acetylation
- **SAS2** primarily mediates transcriptional silencing via H4K16 acetylation

---

## Key Findings

### Substrate Specificity (Critical)
**Primary substrate: Histone H3K14 (NOT H3K9)**
- Documented in UniProt function field
- Confirmed by PMID:10817755, PMID:17157260, PMID:25104842
- In vitro also acetylates free histones H3 and H4

### Complex Organization
SAS3 functions in TWO distinct NuA3 forms:
1. **NuA3a** - binds H3K4me3 at promoters → transcription initiation
   - Composition: NTO1, SAS3, TAF14, YNG1, EAF6
   - Evidence: PMID:17157260 (PMID:25104842)
2. **NuA3b** - binds H3K36me3 at coding regions → transcription elongation
   - Unique subunit: PDP3 (PWWP domain)
   - Evidence: PMID:25104842

---

## Annotation Actions Summary

### Annotations ACCEPTED (27)
**Well-supported, mechanistically accurate:**
- GO:0000785 (chromatin) - IBA
- GO:0004402 (histone acetyltransferase activity) - IBA, IEA, IDA, IMP
- GO:0005634 (nucleus) - IBA, IEA, NAS
- GO:0006357 (regulation of transcription by RNA polymerase II) - IBA
- GO:0003682 (chromatin binding) - IBA
- GO:1990467 (NuA3a histone acetyltransferase complex) - IBA, IDA
- GO:1990468 (NuA3b histone acetyltransferase complex) - IDA
- GO:0003712 (transcription coregulator activity) - IBA
- GO:0006325 (chromatin organization) - IEA
- GO:0006355 (regulation of DNA-templated transcription) - IEA
- GO:0008270 (zinc ion binding) - IEA, RCA
- GO:0016740 (transferase activity) - IEA
- GO:0016746 (acyltransferase activity) - IEA
- GO:0046872 (metal ion binding) - IEA
- GO:0061733 (protein-lysine-acetyltransferase activity) - IEA
- GO:0070775 (H3 histone acetyltransferase complex) - IEA
- GO:0031509 (subtelomeric heterochromatin formation) - IMP
- GO:0030466 (silent mating-type cassette heterochromatin formation) - IMP
- GO:0033100 (NuA3 histone acetyltransferase complex) - IDA (×2)

### Annotations REMOVED (7)
**Generic "protein binding" (GO:0005515) with IPI evidence**
- PMID:12077334, PMID:12672825, PMID:16554755, PMID:17157260, PMID:21179020, PMID:25473596, PMID:37968396

**Reason:** GO:0005515 is minimally informative and violates GO annotation guidelines. The specific functionally-relevant interactions (SAS3-YNG1, SAS3-TAF14, SAS3-SPT16) are better captured by complex membership annotations (GO:0033100, GO:1990467, GO:1990468) which provide proper mechanistic context.

### Annotations MARKED AS OVER-ANNOTATED (2)
- **GO:0006351** (DNA-templated transcription) - IEA, NAS
  - Mechanistically misleading: SAS3 regulates transcription but doesn't catalyze it directly
  - Better terms: GO:0006357 (regulation), GO:0031509 (heterochromatin formation)

- **GO:0031507** (heterochromatin formation) - IEA
  - Secondary to primary transcription activation role
  - More specific terms available: GO:0031509, GO:0030466

### Annotations MARKED AS NON-CORE (2)
- **GO:0000781** (chromosome, telomeric region) - IEA
  - Technically sound logical inference but too general
  - More specific functional terms more informative

---

## Missing Annotations (NEW)

### Recommended Addition
**GO:0036408 - histone H3K14 acetyltransferase activity**
- Evidence: IDA (Direct Assay)
- References: PMID:10817755, PMID:17157260
- Justification: This substrate-specific function is critical to SAS3 and well-documented but missing from annotations. Parallel to GO:0046972 (H4K16 acetyltransferase) for related HATs.

---

## Core Functions Identified

1. **Histone H3K14 Acetylation** (primary molecular function)
   - Catalytic activity of SAS3 in both NuA3a and NuA3b
   - Essential for transcription regulation

2. **Transcription Initiation (NuA3a)**
   - H3K4me3 recognition → H3K14 acetylation at promoters
   - YNG1 PHD finger coordinates targeting

3. **Transcription Elongation (NuA3b)**
   - H3K36me3 recognition → H3K14 acetylation at coding regions
   - PDP3 PWWP domain coordinates targeting

4. **Heterochromatin Formation** (secondary)
   - HML silencing and subtelomeric heterochromatin (IMP evidence)
   - Less important than transcription activation roles

---

## Comparison with SAS2 Paralog

| Feature | SAS3 | SAS2 |
|---------|------|------|
| Complex | NuA3 (two forms) | SAS (SAS2/SAS4/SAS5) |
| Primary Substrate | H3K14 | H4K16 + H3K14 |
| Primary Function | Transcription activation | Transcriptional silencing |
| Key Histone Mark | H3K4me3, H3K36me3 | Telomeric/subtelomeric regions |
| Secondary Function | HML silencing | Limited |

---

## Literature Evidence Summary

**Foundational Papers:**
- **PMID:10817755** - Discovery of SAS3 as NuA3 catalytic subunit; biochemical characterization
- **PMID:11731479** - Silencing roles of SAS complex; initial characterization
- **PMID:17157260** - Detailed NuA3a mechanism; H3K4me3 recognition by YNG1; H3K14 substrate specificity
- **PMID:25104842** - Discovery of NuA3b form; H3K36me3 recognition; transcription elongation role

**Interaction Studies:**
- PMID:12077334 (YNG1 modulation)
- PMID:16554755 (global protein complexes)
- PMID:21179020 (chromatin-associated interactome)
- PMID:25473596 (comprehensive NuA3 analysis)
- PMID:37968396 (protein interactome)

---

## Recommended Actions

### Immediate
1. REMOVE all 7 GO:0005515 (protein binding) IPI annotations
2. ADD GO:0036408 (histone H3K14 acetyltransferase activity) with IDA evidence
3. Mark GO:0006351 and GO:0031507 as OVER_ANNOTATED

### For Expert Review
- Verify whether SAS3 has authentic in vivo role in histone H4 acetylation
- Determine relative contribution of SAS3 vs GCN5 to total H3K14ac
- Clarify specific targeting differences between NuA3a and NuA3b

---

## Quality Metrics

- **Total Annotations Reviewed:** 38
- **Complex Duplicates:** Multiple evidence types for core functions (valid)
- **Generic Terms Removed:** 7 (GO:0005515)
- **Over-annotated Terms:** 2
- **Newly Proposed:** 1 (GO:0036408)
- **Evidence Type Distribution:**
  - IDA: 6 (highest quality)
  - IMP: 3 (strong)
  - IBA: 8 (phylogenetic)
  - IEA: 16 (automated)
  - IPI: 7 (removed as uninformative)
  - NAS: 2
  - RCA: 1

---

## References Used in This Review

All assertions backed by literature:
- UniProt P34218 function field
- PMID:10817755 - NuA3 discovery and biochemistry
- PMID:11731479 - SAS complex silencing roles
- PMID:17157260 - NuA3a mechanism and substrate specificity
- PMID:25104842 - NuA3b discovery and elongation role
- PMID:14562095 - Nuclear localization
- PMID:30358795 - Zinc proteome database

