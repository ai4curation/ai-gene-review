# CASP9 (Caspase-9) Notes - ISOFORMS Project

## Key Isoform Biology

CASP9 is an **initiator caspase** in the intrinsic apoptosis pathway, but has a dominant-negative short isoform.

### Isoforms (4 named)

| Isoform | UniProt ID | Synonym | Key Feature | Function |
|---------|------------|---------|-------------|----------|
| **Isoform 1** | P55211-1 | 9L, Alpha | Full-length, catalytically active | **INDUCES APOPTOSIS** |
| **Isoform 2** | P55211-2 | 9S, Beta | Lacks catalytic domain | **DOMINANT-NEGATIVE INHIBITOR** |
| Isoform 3 | P55211-3 | Gamma | - | Unknown |
| Isoform 4 | P55211-4 | - | - | Unknown |

### Critical Antagonism: Long vs Short

**Caspase-9L (Isoform 1)**:
- Contains CARD domain for Apaf-1 binding
- Contains catalytic domain
- Forms apoptosome with Apaf-1 and cytochrome c
- Cleaves and activates CASP3/CASP7
- **PRO-APOPTOTIC**

**Caspase-9S (Isoform 2)**:
UniProt explicitly states:
> "Lacks activity is an dominant-negative inhibitor of caspase-9" [PMID:10070954]

Mechanism: Caspase-9S competes with Caspase-9L for Apaf-1 binding but cannot activate downstream caspases.

### Mechanism of Antagonism

```
Apaf-1 + Cyt c + dATP → Apoptosome

If Caspase-9L binds: → Apoptosis
If Caspase-9S binds: → No apoptosis (dominant-negative)
```

The ratio of 9L/9S determines apoptotic sensitivity.

## GOA Annotation Status

- **109 total annotations**
- **NO isoform-specific annotations** (no P55211-X identifiers)
- Annotations conflate pro-apoptotic 9L with anti-apoptotic 9S

## Expected Annotation Issues

1. **"Caspase activity"** - TRUE for isoform 1, FALSE for isoform 2
2. **"Positive regulation of apoptotic process"** - TRUE for isoform 1, FALSE for isoform 2
3. **"Negative regulation of apoptotic process"** - should be annotated for isoform 2!
4. **"Apoptosome" annotations** - both isoforms can be in apoptosome, but with opposite effects

## Biological Significance

Like BCL2L1, this is a case where the balance between isoforms determines cell fate:
- High 9L/9S ratio → apoptosis-sensitive
- Low 9L/9S ratio → apoptosis-resistant

Cancer cells often shift this ratio towards 9S to evade apoptosis.

## Key References

- PMID:10070954 - Caspase-9S dominant-negative function

## 2026-09-30 APOPTOSIS review

- Re-reviewed the pre-existing CASP9 YAML without using the provider deep-research
  files as assertion support. Primary rows now cite cached PubMed, Reactome, GOA,
  and GO-CAM evidence directly.
- Tightened inherited top-level `GO:0006915 apoptotic process` rows to
  `GO:0097193 intrinsic apoptotic signaling pathway`, and tightened broad
  apoptosis-regulation assertions to `GO:1900119 positive regulation of execution
  phase of apoptosis` where the evidence is full-length CASP9 maturing
  executioner procaspases.
- Retained `GO:0051604 protein maturation` for the direct CASP9 step of
  proteolytically activating CASP3/CASP7; CASP9 is upstream of the execution
  phase rather than itself being an executioner-caspase component.
- Replaced APaf-1/procaspase-9 generic `GO:0005515` rows with
  `GO:0050700 CARD domain binding` or the apoptotic cysteine-endopeptidase
  activator term as appropriate, and removed uninformative high-throughput or
  inhibitor/interactor `GO:0005515` edges.
- Made the endogenous Caspase-9S negative-regulator proposal isoform-specific
  to `P55211-2` and more precise as `GO:2001243 negative regulation of intrinsic
  apoptotic signaling pathway`; removed a broad `GO:0030234 enzyme regulator
  activity` placeholder that had only been present to satisfy the core-function
  shape.
- Deferred abstract-only rows where the visible record did not expose the
  CASP9 assay behind the GOA annotation, and marked the DNA-damage/c-Abl Tyr-153
  rows as unresolved because PMID:29066624 challenged the original activating
  phosphorylation model from PMID:15657060.
