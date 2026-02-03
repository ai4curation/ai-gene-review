# SPKW E. coli O157:H7 (ECO57) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

E. coli O157:H7 is a pathogenic bacterium with well-characterized virulence factors including:
- **Shiga toxins (Stx1, Stx2)** - True toxins that kill host cells
- **Type III secretion system (T3SS) effectors** - Signaling modulators that manipulate host cells

This provides an ideal test case for distinguishing between:
1. **True toxins** - Proteins that directly damage/kill host cells (LEGITIMATE toxin annotations)
2. **Effectors** - Proteins that modulate signaling without direct cytotoxicity (potential OVER-ANNOTATIONS)

## Statistics (2026-01-31)

| Metric | Count |
|--------|-------|
| Total SPKW annotations (taxon:83334) | ~74,000 |
| SPKW-unique "toxin activity" annotations | 37 genes |
| SPKW-unique "killing of cells" annotations | 24 genes |

## Status

- [x] Initial exploration complete (2026-01-31)
- [x] Deep research for 2 genes (2026-01-31)
- [x] Annotation review complete (2026-01-31)
- [x] Write-up complete (2026-01-31)
- [ ] Additional T3SS effectors (nleB2, nleE, etc.) - future work

---

## Case Studies (2 genes reviewed)

### Case 1: nleB1 - Type III Effector (OVER-ANNOTATED)

**Gene:** nleB1 (Q8XBX8) - Protein-arginine N-acetylglucosaminyltransferase

**Review file:** `genes/ECO57/nleB1/nleB1-ai-review.yaml`

**SPKW annotation:** GO:0090729 (toxin activity)

**Review decision:** **REMOVE**

**Analysis:** NleB1 is a T3SS effector that modulates host signaling, NOT a toxin:

```
True Toxin (e.g., Stx2A):
┌─────────────────────────────────────────────────────────────────────────────┐
│ Enters cell → Inactivates ribosomes → Halts translation → CELL DEATH       │
│                                                                             │
│ Direct cytotoxicity = TRUE TOXIN                                            │
└─────────────────────────────────────────────────────────────────────────────┘

NleB1 (Type III Effector):
┌─────────────────────────────────────────────────────────────────────────────┐
│ Injected via T3SS → GlcNAcylates death domain proteins → Blocks apoptosis  │
│                                                                             │
│ Modulates signaling = EFFECTOR, NOT TOXIN                                   │
│                                                                             │
│ Key difference: NleB1 PREVENTS cell death, not causes it!                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**NleB1's actual function:**
1. Glycosyltransferase that adds GlcNAc to arginine residues
2. Targets death domain proteins (FADD, TRADD, RIPK1)
3. Blocks death receptor signaling complex assembly
4. SUPPRESSES apoptosis and necroptosis - opposite of toxin!

**Literature evidence (PMID:30619781):**
> "NleB1 inhibitors were not significantly toxic to mammalian cells"
> "Did not cause significant macrophage death"

**Core function:** GO:0106362 (protein-arginine N-acetylglucosaminyltransferase activity)

---

### Case 2: stx2A - Shiga Toxin A Subunit (LEGITIMATE)

**Gene:** stx2A (A0A9Q6Z964) - rRNA N-glycosylase

**Review file:** `genes/ECO57/stx2A/stx2A-ai-review.yaml`

**SPKW annotation:** GO:0090729 (toxin activity)

**Review decision:** **ACCEPT** (Legitimate annotation)

**Analysis:** Stx2A is a TRUE TOXIN with direct cytotoxic activity:

```
Shiga Toxin Mechanism:
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. B pentamer binds Gb3 receptor → Endocytosis                              │
│ 2. A chain cleaved by furin → A1 (catalytic) released to cytosol            │
│ 3. A1 depurinates A4324 in 28S rRNA sarcin-ricin loop                       │
│ 4. Ribosomes inactivated → Translation halted → CELL DEATH                  │
│                                                                             │
│ Direct ribosome inactivation = TRUE TOXIN ACTIVITY                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Stx2A's actual function:**
1. rRNA N-glycosylase (EC 3.2.2.22)
2. Depurinates specific adenine in 28S rRNA sarcin-ricin loop
3. Inactivates ribosomes (ribosome-inactivating protein, RIP)
4. Causes hemolytic uremic syndrome (HUS) in humans

**This is EXACTLY what "toxin activity" (GO:0090729) describes:**
> "initiating pathogenesis (leading to an abnormal, generally detrimental state)"

---

## Key Finding: Distinguishing Toxins from Effectors

| Property | True Toxin (Stx2A) | Effector (NleB1) |
|----------|-------------------|------------------|
| **Mechanism** | Direct cytotoxicity | Signaling modulation |
| **Effect on cell** | Kills cell | Manipulates cell |
| **Target** | Essential machinery (ribosomes) | Signaling proteins (death domains) |
| **Outcome** | Cell death | Cell survival (blocks apoptosis) |
| **GO:0090729 appropriate?** | **YES** | **NO** |

## Over-Annotation Pattern: "Toxin" Applied to Effectors

The UniProt "Toxin" keyword is being applied too broadly to T3SS effectors:

**Genes correctly annotated as toxins:**
- stx1A, stx1B, stx2A, stx2B (Shiga toxins) - TRUE TOXINS
- hlyA, hlyE (hemolysins) - TRUE TOXINS (pore-forming)

**Genes incorrectly annotated as toxins:**
- nleB1, nleB2 (glycosyltransferases) - EFFECTORS
- nleE (cysteine methyltransferase) - EFFECTOR

## Comparison: O157:H7 vs Other Organisms

| Organism | Domain | Toxin Annotation Accuracy | Notes |
|----------|--------|--------------------------|-------|
| E. coli O157:H7 | Bacteria | ~50% (split) | True toxins correct, effectors wrong |
| T4 Phage | Virus | 0% | No true toxins, all over-annotated |
| A. gambiae D7 | Eukarya | 0% | Kratagonists, not toxins |

## Recommendations for Bacterial Pathogen SPKW Curation

1. **Distinguish toxins from effectors**: Toxins directly kill; effectors modulate signaling

2. **Check mechanism of action**: Does the protein directly damage cells or manipulate them?

3. **Consider the biological outcome**: If a protein PREVENTS cell death (like NleB1), it's not a toxin

4. **Validate Shiga toxin family**: These are legitimate toxin annotations

5. **Review T3SS effector annotations**: Many may have incorrect "toxin" annotations

## Review Files Location

```
genes/ECO57/
├── nleB1/nleB1-ai-review.yaml   (REMOVE: toxin - is effector that blocks apoptosis)
└── stx2A/stx2A-ai-review.yaml   (ACCEPT: toxin - true ribosome-inactivating protein)
```
