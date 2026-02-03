# SPKW Arabidopsis thaliana (ARATH) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

Arabidopsis thaliana is the premier plant model organism. Unlike TAIR (which has no SPKW annotations due to its own curation pipeline), the GOA database contains substantial SPKW-derived annotations. This analysis examines whether the over-annotation patterns seen in animals apply to plants.

## Key Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Total annotations (GOA) | 299,228 |
| SPKW annotations | 46,710 (16%) |
| TRUE SPKW-unique (after closure) | 13,108 |
| Unique genes with TRUE SPKW-unique | 8,433 |
| Unique terms in TRUE SPKW-unique | 266 |
| **Closure filtering reduction** | **72%** |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 7,225 (55%) | 4,980 | 80 |
| P (Biological Process) | 5,170 (39%) | 3,778 | 163 |
| C (Cellular Component) | 713 (6%) | 651 | 23 |

## Top TRUE SPKW-Unique Terms

| Term | Label | Genes | Expected Pattern |
|------|-------|-------|------------------|
| GO:0046872 | metal ion binding | 2,258 | Broad MF - legitimate |
| GO:0008270 | zinc ion binding | 1,035 | Broad MF - legitimate |
| GO:0006952 | defense response | 535 | **Mixed** - need case review |
| GO:0005524 | ATP binding | 517 | Broad MF - legitimate |
| GO:0071555 | cell wall organization | 305 | Likely legitimate |
| GO:0031640 | killing of cells of another organism | 291 | **Needs review** - defensins |
| GO:0050832 | defense response to fungus | 277 | Mixed |
| GO:0009734 | auxin-activated signaling pathway | 169 | **Needs review** |
| GO:0051301 | cell division | 204 | Likely legitimate |
| GO:0048511 | rhythmic process | 21 | **100% over-annotated in human** |
| GO:0051321 | meiotic cell cycle | 24 | **Problematic in S. pombe** |
| GO:0006914 | autophagy | 5 | 80% over-annotated in human |

## Plant-Specific Considerations

Unlike animals, plants have:
1. **Hormone signaling pathways** (auxin, ABA, ethylene, etc.) with specific GO terms
2. **Photosynthesis and light responses** - unique to photosynthetic organisms
3. **Cell wall biology** - fundamentally different from animal ECM
4. **Defense without immune cells** - rely on innate immunity in every cell
5. **Specialized reproductive biology** - pollen, self-incompatibility

---

## Full Gene Reviews Completed (2026-01-31)

| Gene | UniProt | Category | Key SPKW Term | Action | Finding |
|------|---------|----------|---------------|--------|---------|
| LCR1 | P82716 | Defensin | killing of cells | **REMOVE** | PCP-like DEFL, not antimicrobial |
| ELF4 | O04211 | Circadian | rhythmic process | **MARK_OVER_ANNOTATED** | Redundant with specific terms |
| ARF19 | Q8RYC8 | Hormone | auxin signaling | **MODIFY** | ARF responds TO auxin, not signal transduction |
| BUB3.1 | Q9LJN8 | Cell cycle | meiotic cell cycle | **MODIFY** | General SAC gene, not meiosis-specific |

**Over-annotation patterns: 3/4 genes had issues (75%)**

---

### Case 1: LCR1 - Subclade-Specific Function vs Family Annotation ✓

**Gene:** LCR1 (P82716) - Defensin-like protein 147

**Review file:** `genes/ARATH/LCR1/LCR1-ai-review.yaml`

**SPKW annotation:** GO:0031640 (killing of cells of another organism)

**Review decision:** **REMOVE**

**Analysis:** This is a **surprising finding**. Unlike the D. melanogaster lysozymes which were correctly annotated to "killing", LCR1 should NOT have this annotation because:

1. **LCR1 is a PCP-like (pollen coat protein-like) defensin-like protein (DEFL)**
   - Within the ~300-member Arabidopsis DEFL family, LCR1 clusters with reproductive signaling proteins
   - This is distinct from PDF1.1/PDF1.2 defensins with proven antimicrobial activity

2. **Expression pattern contradicts defense function**
   - Expressed exclusively in flower buds
   - NOT in stems, roots, or leaves where defense would be needed

3. **No experimental antimicrobial evidence**
   - Deep research states: "LCR1's direct antimicrobial activity is not reported"
   - UniProt keywords based on family, not gene-specific data

**This demonstrates that family-level keyword assignments can miss subclade-specific functional divergence.**

---

### Case 2: ELF4 - Legitimate but Redundant ✓

**Gene:** ELF4 (O04211) - EARLY FLOWERING 4

**Review file:** `genes/ARATH/ELF4/ELF4-ai-review.yaml`

**SPKW annotation:** GO:0048511 (rhythmic process)

**Review decision:** **MARK_AS_OVER_ANNOTATED**

**Analysis:** Unlike human "rhythmic process" genes (100% over-annotated), ELF4 IS a bona fide clock gene:
- Core component of the Evening Complex (EC) with ELF3 and LUX
- Experimental evidence for circadian rhythm regulation (IMP, IDA)

However, the "rhythmic process" annotation is **redundant** because ELF4 already has:
- GO:0042752 (regulation of circadian rhythm) - IDA
- GO:0042753 (positive regulation of circadian rhythm) - IMP
- GO:0009649 (entrainment of circadian clock) - IMP

**The SPKW annotation is accurate but adds no information beyond existing specific terms.**

Also identified: GO:0009908 (flower development) → MODIFY to GO:0009909 (regulation of flower development) - ELF4 controls flowering TIME, not flower organogenesis.

---

### Case 3: ARF19 - Signaling Endpoint vs Transduction ✓

**Gene:** ARF19 (Q8RYC8) - Auxin Response Factor 19

**Review file:** `genes/ARATH/ARF19/ARF19-ai-review.yaml`

**SPKW annotation:** GO:0009734 (auxin-activated signaling pathway)

**Review decision:** **MODIFY** → GO:0009733 (response to auxin)

**Analysis:** This reveals a subtle but important distinction:

```
Auxin Signaling Pathway:
┌─────────────────────────────────────────────────────────┐
│ Auxin → TIR1/AFB receptor → AUX/IAA degradation → ARF  │
│   ↑                                                    │
│   Signal molecule                     Downstream effector
└─────────────────────────────────────────────────────────┘
```

ARF19:
- Does NOT bind auxin directly
- Is RELEASED from repression when AUX/IAA proteins are degraded
- Acts as the ENDPOINT transcription factor, not a signal transducer

The GO definition of "auxin-activated signaling pathway" refers to "binding of auxin to a receptor" - ARF19 is downstream of this. The correct term is GO:0009733 (response to auxin).

**This pattern is analogous to Sin1 in D. mel - both are downstream effectors incorrectly annotated to the signaling pathway.**

---

### Case 4: BUB3.1 - General vs Specific Cell Cycle Function ✓

**Gene:** BUB3.1 (Q9LJN8) - BUB3 spindle checkpoint protein

**Review file:** `genes/ARATH/BUB3.1/BUB3.1-ai-review.yaml`

**SPKW annotation:** GO:0051321 (meiotic cell cycle)

**Review decision:** **MODIFY** → GO:0000278 (mitotic cell cycle)

**Analysis:** This parallels the S. pombe ATG gene pattern but with a key difference:

| Organism | Gene | Keyword | Actual Function | Over-annotation Type |
|----------|------|---------|-----------------|---------------------|
| S. pombe | atg5 | Meiosis | Autophagy | Completely wrong process |
| Arabidopsis | BUB3.1 | Meiosis | Cell cycle checkpoint | Wrong specificity within correct process |

BUB3.1 is a **general spindle assembly checkpoint protein**:
- Functions in BOTH mitosis and meiosis
- Experimental evidence is primarily for mitotic function
- Recent studies (2024) show BUB3.1/BUB3.2 specialize in cytokinesis, not meiosis

The "meiotic cell cycle" annotation implies a meiosis-specific function that is not supported. BUB3.3 appears to be the paralog with kinetochore-specific functions.

---

## Arabidopsis Over-Annotation Patterns

| Pattern | Example | Frequency | Severity |
|---------|---------|-----------|----------|
| **Subclade function divergence** | LCR1 (PCP-like, not antimicrobial) | Novel | High |
| **Redundant broad term** | ELF4 (rhythmic process) | Common | Low |
| **Downstream effector as pathway** | ARF19 (auxin signaling) | Common | Medium |
| **General as specific** | BUB3.1 (meiotic vs cell cycle) | Common | Medium |

## Comparison: Arabidopsis vs Other Organisms

| Organism | Over-Annotation Rate | Main Patterns |
|----------|---------------------|---------------|
| Human (apoptosis) | 80-100% | Process conflation |
| S. pombe (ATG-meiosis) | 100% | Support process conflation |
| D. melanogaster | 50% | Mixed |
| P. putida | 25% | RT defense keyword |
| **Arabidopsis** | **75%** | Subclade divergence, specificity |

## Key Lessons from Arabidopsis

1. **Subclade functional divergence matters**: The DEFL family shows that family-level keywords can mask subfunctionalization. LCR1 is in a reproductive signaling subclade, not an antimicrobial subclade.

2. **Redundancy is common in well-curated organisms**: When experimental annotations exist (ELF4), SPKW adds redundant broad terms rather than new information.

3. **Signaling endpoint ≠ signaling pathway**: ARF19 reveals the same pattern as Sin1 - downstream effectors get annotated to the pathway they respond to.

4. **Plants have similar meiosis over-annotation issues**: BUB3.1 shows that keywords like "Meiosis" get applied to general cell cycle genes, though less severely than the ATG-meiosis conflation in yeast.

## Recommendations for Plant SPKW Curation

1. **Review defensin family annotations**: Check if genes are in antimicrobial or PCP-like subclades before accepting "killing" annotations

2. **Validate hormone signaling terms**: Distinguish between signal transduction components and downstream response factors

3. **Check experimental redundancy**: For well-characterized genes, SPKW may add no new information

4. **Apply same meiosis criteria as yeast**: General cell cycle genes should not get meiosis-specific annotations without direct evidence

## Review Files Location

```
genes/ARATH/
├── LCR1/LCR1-ai-review.yaml      (REMOVE: killing - PCP-like subclade)
├── ELF4/ELF4-ai-review.yaml      (REDUNDANT: rhythmic process)
├── ARF19/ARF19-ai-review.yaml    (MODIFY: auxin signaling → response)
└── BUB3.1/BUB3.1-ai-review.yaml  (MODIFY: meiotic → mitotic cell cycle)
```
