# SPKW Anopheles gambiae (ANOGA) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This subproject explores UniProt Keyword (SPKW) unique contributions to *Anopheles gambiae* (African malaria mosquito) GO annotations. ANOGA is of high interest because:

1. **Vector biology relevance**: Mosquito immune system and salivary proteins are critical for understanding malaria transmission
2. **Less curated organism**: Fewer experimental annotations means higher reliance on automated pipelines
3. **Unique biology**: Insect immunity, blood-feeding adaptations, and vector-pathogen interactions

## Summary Statistics (from ANOGA.ddb)

| Metric | Value |
|--------|-------|
| Total ANOGA annotations | 86,061 |
| SPKW (GO_REF:0000043) annotations | 17,787 |
| SPKW-unique annotations | 12,076 |
| Unique genes with SPKW-only annotations | 5,812 |
| Unique GO terms from SPKW-only | 246 |

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 7,883 | 4,125 | 83 |
| P (Biological Process) | 3,616 | 2,693 | 143 |
| C (Cellular Component) | 577 | 508 | 20 |

## Status

- [x] Initial exploration complete (2026-01-30)
- [x] D7 protein family review complete (2026-01-30) - **ALL 8 PROTEINS REVIEWED**
- [x] Immune gene pilot batch complete (2026-01-30) - **6 GENES REVIEWED**
- [x] PGRP/TEP extended batch (2026-01-31) - **ALL 8 GENES REVIEWED**
- [ ] Review remaining immune genes (~133 more)

## High-Interest Categories for ANOGA

These terms are uniquely relevant to mosquito biology:

| Term | Label | SPKW-unique Genes | Interest Level |
|------|-------|-------------------|----------------|
| GO:0002376 | immune system process | 147 | **HIGH** - vector immunity |
| GO:0045087 | innate immune response | 76 | **HIGH** - pathogen response |
| GO:0090729 | toxin activity | 15 | **HIGH** - salivary proteins |
| GO:0042742 | defense response to bacterium | 11 | **HIGH** - antimicrobials |

### Known Problematic Terms (from Human Analysis)

| Term | Label | SPKW-unique Genes | Expected Over-annotation Rate |
|------|-------|-------------------|------------------------------|
| GO:0006915 | apoptotic process | 28 | ~80% (based on human) |
| GO:0048511 | rhythmic process | 20 | ~100% (based on human) |
| GO:0006914 | autophagy | 16 | ~80% (based on human) |

## Query Used

```sql
-- Database: ~/repos/go-db/db/ANOGA.ddb
-- Find SPKW-unique contributions (gene-term pairs with no other evidence)

WITH spkw_annotations AS (
    SELECT a.db_object_id, a.db_object_symbol, a.ontology_class_ref, a.aspect
    FROM gaf_association a
    WHERE a.supporting_references = 'GO_REF:0000043'
),
gene_term_with_other_evidence AS (
    SELECT DISTINCT db_object_id, ontology_class_ref
    FROM gaf_association
    WHERE supporting_references != 'GO_REF:0000043'
),
spkw_unique AS (
    SELECT s.*
    FROM spkw_annotations s
    WHERE NOT EXISTS (
        SELECT 1 FROM gene_term_with_other_evidence o
        WHERE o.db_object_id = s.db_object_id
          AND o.ontology_class_ref = s.ontology_class_ref
    )
)
SELECT
    su.ontology_class_ref,
    tl.label,
    su.aspect,
    COUNT(DISTINCT su.db_object_id) as gene_count
FROM spkw_unique su
JOIN term_label tl ON su.ontology_class_ref = tl.id
GROUP BY su.ontology_class_ref, tl.label, su.aspect
ORDER BY gene_count DESC;
```

---

## D7 Family Review Summary (8 proteins)

| Gene | UniProt | Binding Specificity | Toxin Activity Annotation | Key Finding |
|------|---------|---------------------|---------------------------|-------------|
| D7r1 | Q9UB30 | Serotonin, histamine | **OVER-ANNOTATED** | Kratagonist for biogenic amines |
| D7r2 | Q9UB31 | Serotonin, histamine, norepinephrine | N/A (not annotated) | Kratagonist for biogenic amines |
| D7r3 | A0A1S4GYH9 | Serotonin, histamine | N/A (not annotated) | Has IDA evidence for localization |
| D7r4 | Q7PNF2 | Serotonin, histamine, norepinephrine, tryptamine | N/A (not annotated) | Crystal structure solved |
| **D7r5** | Q7PN86 | **NONE** | N/A (not annotated) | Possible pseudogene, no binding |
| D7L1 | Q7PJ76 | Leukotriene C4, thromboxane A2 | **OVER-ANNOTATED** | Binds eicosanoids, not amines |
| D7L2 | A0A1S4GYJ6 | Weak leukotriene binding | **OVER-ANNOTATED** | Less characterized |
| **D7L3** | A0A1S4HE90 | **Serotonin only** | **OVER-ANNOTATED** | Only long-form that binds amine |

**Result: 4/4 (100%) "toxin activity" annotations are OVER-ANNOTATED; the other 4 D7 proteins do not carry GO:0090729 in GOA**

### Why "Toxin Activity" is Wrong for D7 Proteins

The GO definition of toxin activity (GO:0090729) requires:
> "initiating pathogenesis (leading to an abnormal, generally detrimental state)"

D7 proteins fail this criterion because:
1. They do NOT initiate pathogenesis - they facilitate normal feeding behavior
2. They do NOT cause tissue damage - effects are reversible
3. The host returns to normal after the mosquito finishes feeding
4. Their mechanism is sequestration (removing mediators), not introducing harmful substances

### The Kratagonism Mechanism

D7 proteins are "kratagonists" (from Greek *kratos* = power/strength + antagonist) - high-affinity scavengers that neutralize host defense molecules:

```
Host response to bite:
  Tissue damage → Serotonin/Histamine release → Vasoconstriction + Inflammation
                                    ↓
                           D7 protein binds mediator
                                    ↓
                           Mediator sequestered (inactive)
                                    ↓
                           Blood vessel stays dilated → Successful feeding
```

This is fundamentally different from toxin activity:
- **Toxin**: Introduces harmful substance → causes pathology
- **Kratagonist**: Removes host substance → prevents host defense

### Short-Form vs Long-Form D7 Proteins

| Property | Short Forms (D7r1-5) | Long Forms (D7L1-3) |
|----------|---------------------|---------------------|
| Size | ~15-17 kDa | ~30 kDa (two OBP domains) |
| Primary ligands | Biogenic amines | Eicosanoids (lipid mediators) |
| Targets | Serotonin, histamine | Leukotrienes, thromboxane A2 |
| Host pathway blocked | Vasoconstriction | Inflammation, platelet aggregation |

**Exception**: D7L3 (7DL3) binds serotonin, making it unique among long-forms.

### Recommended GO Annotations for D7 Proteins

**Instead of "toxin activity":**
- GO:0051378 (serotonin binding) - for D7r1-4, D7L3
- GO:0051381 (histamine binding) - for D7r1-4
- GO:1900047 (negative regulation of hemostasis) - for all
- GO:0005615 (extracellular space) - appropriate, keep

### Full Documentation

See comprehensive write-up: `interpro/panther/PTHR11857/PTHR11857-summary.md`

---

## Immune Gene Pilot Batch Review (6 genes)

Reviewed 6 well-characterized ANOGA immune genes with SPKW-unique annotations to "immune system process" (GO:0002376).

| Gene | UniProt | Description | Immune Status | Key Issue Found |
|------|---------|-------------|---------------|-----------------|
| **TEP1** | C9XI63 | Thioester-containing protein 1 | ✅ LEGITIMATE | Remove "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **SRPN2** | Q7QIJ8 | Serpin 2 | ✅ LEGITIMATE | Core melanization regulator, well-supported |
| **PGRPS1** | Q7QFK2 | Peptidoglycan recognition protein S1 | ✅ LEGITIMATE | Remove "amidase activity" (lacks catalytic residues) |
| **CLIPB4** | Q7PEV7 | CLIP-domain serine protease B4 | ✅ LEGITIMATE | Add GO:0035006 (melanization defense response) |
| **TOLL9** | Q5TWL7 | Toll receptor 9 | ✅ LEGITIMATE | Remove "inflammatory response" (vertebrate-specific term) |
| **psidin** | Q7PYI4 | Phagocyte signaling-impaired protein | ❌ OVER-ANNOTATED | Core function is NatB acetyltransferase subunit |

**Result: 5/6 (83%) immune annotations are LEGITIMATE**

### Comparison: D7 vs Immune Genes

| Batch | Genes | Over-Annotation Rate | Pattern |
|-------|-------|---------------------|---------|
| D7 proteins | 8 | 100% | "Toxin activity" wrong for kratagonists |
| Immune genes | 6 | 17% | Most are bona fide immune genes |

### Key Pattern: Secondary Over-annotations from Domain Homology

Even when the primary immune annotation is correct, we found **secondary over-annotations** from automated pipelines:

| Gene | Over-annotated Term | Source | Reason |
|------|---------------------|--------|--------|
| TEP1 | GO:0004866 (endopeptidase inhibitor) | InterPro | A2M domain ≠ inhibitor function |
| PGRPS1 | GO:0008745 (amidase activity) | IBA/IEA | Lacks catalytic zinc-binding residues |
| TOLL9 | GO:0006954 (inflammatory response) | IBA | Vertebrate-specific term for insects |
| psidin | GO:0002376 (immune system process) | IEA | Phenotype from Drosophila, not core function |

### Biological Insights

1. **TEP1**: Complement-like opsonin that binds Plasmodium ookinetes via thioester bond
2. **SRPN2**: Key negative regulator of melanization cascade (inhibits CLIPB9/CLIPB10)
3. **PGRPS1**: Non-catalytic PGRP that senses bacterial peptidoglycan (Toll pathway)
4. **CLIPB4**: Upstream protease in prophenoloxidase activation cascade
5. **TOLL9**: Pattern recognition receptor activating Rel1/NF-κB pathway
6. **psidin**: NAA25/MDM20 ortholog - NatB complex subunit, NOT an immune protein

---

## PGRP/TEP Extended Batch Review (8 genes)

Extended review of PGRP (peptidoglycan recognition protein) and TEP (thioester-containing protein) families - key innate immune genes in Anopheles.

| Gene | UniProt | Description | Immune Status | Key Finding |
|------|---------|-------------|---------------|-------------|
| **PGRPLB** | F5HMW5 | PGRP-LB (catalytic, transmembrane) | ✅ LEGITIMATE | Catalytic amidase, negative regulator of IMD pathway |
| **PGRPLC** | A7UTA1 | PGRP-LC (non-catalytic, transmembrane) | ✅ LEGITIMATE | Principal IMD receptor; REMOVE "amidase activity" (non-catalytic) |
| **PGRPLD** | A0A1S4GYQ6 | PGRP-LD | ✅ LEGITIMATE | IMD pathway receptor |
| **PGRPS2** | D2SU82 | PGRP-S2 (secreted, catalytic) | ✅ LEGITIMATE | Catalytic amidase (retains His-His-Tyr-Cys zinc-binding) |
| **PGRPS3** | D2STP8 | PGRP-S3 (secreted, catalytic) | ✅ LEGITIMATE | Retains zinc-binding catalytic residues (unlike S1) |
| **TEP2** | Q5TQC0 | Thioester-containing protein 2 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **TEP6** | Q7Q251 | Thioester-containing protein 6 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |
| **TEP10** | Q7PSK0 | Thioester-containing protein 10 | ✅ LEGITIMATE | REMOVE "endopeptidase inhibitor" (opsonin, not inhibitor) |

**Result: 8/8 (100%) immune annotations are LEGITIMATE**

### Key Pattern: PGRP Catalytic vs Non-Catalytic

| PGRP Type | Examples | Zinc-binding Residues | Function |
|-----------|----------|----------------------|----------|
| **Catalytic** | PGRPLB, PGRPS2, PGRPS3 | Present (His-His-Tyr-Cys) | N-acetylmuramoyl-L-alanine amidase - degrades PGN |
| **Non-catalytic receptor** | PGRPLC, PGRPS1 | Absent/mutated | Pattern recognition receptor - binds PGN to signal |
| **Non-catalytic regulator** | PGRPLD | Absent | Negative regulator of immunity (no PGN binding/cleavage) |

### Key Pattern: TEP "Endopeptidase Inhibitor" Over-annotation

All TEPs (TEP1, TEP2, TEP6, TEP10) are incorrectly annotated with **GO:0004866 (endopeptidase inhibitor activity)** based on InterPro A2M domain mapping. This is a systematic over-annotation:

- **Source**: InterPro2GO from IPR001599 (Alpha-2-macroglobulin)
- **Problem**: Vertebrate A2M proteins ARE protease inhibitors, but insect TEPs have **functionally diverged**
- **Reality**: Insect TEPs are **complement-like opsonins** that covalently tag pathogens via thioester bond
- **Action**: REMOVE the endopeptidase inhibitor annotation from all ANOGA TEPs

```
A2M Family Functional Divergence:
┌─────────────────────┐
│   Common Ancestor   │ (A2M domain + thioester)
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌──────────────┐
│Vertebrate│ │Insect TEPs   │
│A2M       │ │              │
└────┬────┘ └──────┬───────┘
     │             │
  Protease      Complement-like
  Trapping      Opsonization
     │             │
  Inhibitor     Pathogen
  Activity      Tagging
```

---

## PANTHER Family Analysis: PTHR11857 (OBP/PBP-related)

**Family context for D7 proteins**: The D7L1 and D7L2 proteins belong to PANTHER family PTHR11857 (Odorant-binding/pheromone-binding protein-related), specifically subfamily SF43 (GEO07291P1-RELATED).

**Deep research completed**: `interpro/panther/PTHR11857/PTHR11857-deep-research-falcon.md`

### Key findings about the family:

| Subfamily | Structure | Function | Members in PTHR11857 |
|-----------|-----------|----------|---------------------|
| Classic OBPs | 6 Cys, 6 α-helices | Odorant transport | Drosophila Obp genes |
| Plus-C OBPs | ≥8 Cys, extra disulfides | Specialized/non-olfactory | Extended variants |
| Minus-C OBPs | 4-5 Cys, flexible | Broader ligand spectra | Reduced variants |
| PBPs | Classic scaffold | Sex pheromone binding | Lepidopteran PBPs |
| GOBPs | Similar to PBPs | Host volatile recognition | GOBP1/2 clades |
| **SF43** | Mixed D7s + OBPs | **Neo-functionalized** | D7L1, D7L2, Obp56d |

### Critical insight - Neo-functionalization

The D7 salivary proteins in subfamily SF43 represent a clear case of **neo-functionalization**:

- **Ancestral function (OBPs)**: Transport odorants/pheromones to olfactory receptors in sensory lymph
- **Derived function (D7s)**: Sequester host signaling molecules (serotonin, histamine, leukotrienes) in saliva to facilitate blood feeding

Both share:
- Similar structural fold (OBP-like helical architecture)
- Bind similar ligands (biogenic amines)
- Extracellular secretion

But differ in:
- **Biological context**: Olfactory tissue vs. salivary gland
- **Biological role**: Sensory perception vs. anti-hemostatic adaptation
- **Evolutionary purpose**: Chemical communication vs. blood-feeding facilitation

### GO annotation implications:

1. **"odorant binding" (GO:0005549)** - Based on family membership via InterPro, but D7 proteins don't function in olfaction → **MODIFY** to specific binding terms (serotonin/histamine/leukotriene binding)

2. **"toxin activity" (GO:0090729)** - Applied via SPKW "Toxin" keyword, but D7 proteins are kratagonists not toxins → **OVER-ANNOTATED**

3. **"extracellular space" (GO:0005615)** - Appropriate for both OBPs and D7s (both are secreted)

**This case study demonstrates how PANTHER family membership can propagate inappropriate GO annotations when neo-functionalization has occurred.**

---

## Recommendations

1. **Prioritize immune terms for review**: GO:0002376 and GO:0045087 have the most SPKW-unique genes and are highly relevant to vector biology research

2. **Validate toxin activity annotations**: The D7 proteins suggest some toxin annotations may be legitimate, but "toxin" may not be the best term

3. **Check apoptosis/autophagy/rhythm**: Based on human experience, expect 80-100% over-annotation rate

4. **Consider ANOGA-specific biology**: Blood-feeding, olfaction (host-seeking), and innate immunity are core mosquito biology that may have legitimate unique annotations

### Review Files Location

```
genes/ANOGA/
├── D7r1/, D7r2/, D7r3/, D7r4/, D7r5/, D7L1/, D7L2/, D7L3/
├── TEP1/, TEP2/, TEP6/, TEP10/
├── PGRPS1/, PGRPLB/, PGRPLC/, PGRPLD/, PGRPS2/, PGRPS3/
├── SRPN2/, CLIPB4/, TOLL9/, psidin/
```
