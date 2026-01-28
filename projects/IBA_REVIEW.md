# IBA Annotation Quality Project

## Overview

This project examines the quality of IBA (Inferred from Biological Aspect of Ancestor) annotations discovered through AI-assisted gene review. IBA annotations use phylogenetic trees to transfer function from characterized proteins to uncharacterized orthologs.

While IBA is a powerful curation tool, it can produce problematic annotations when:
1. **Functional divergence** - Orthologs have evolved different functions
2. **Pseudo-enzymes** - Catalytic function lost despite domain retention
3. **Context-specific function** - Function differs between organisms/tissues
4. **Over-generalization** - Broad terms transferred when specific functions differ

## IBA Quality Issues

### 1. Pseudo-Enzyme Propagation

**The Problem**: Enzymatic activity transferred to proteins that have lost catalytic function.

**Example - Epe1 (S. pombe)**:
- IBA annotation: `GO:0032452` (histone demethylase activity)
- Source: Related JmjC domain proteins with characterized demethylase activity
- Reality: Epe1 has degenerate active site (HVD vs HXD), no detectable activity
- **Impact**: Misleading annotation propagated via phylogenetic inference

### 2. Ubiquitin-Like Modifier Confusion

**The Problem**: Function from ubiquitin E1 transferred to ISG15-specific E1.

**Example - UBA7 (human)**:
- IBA annotations from ubiquitin pathway:
  - `GO:0008641` (ubiquitin-like modifier activating enzyme activity) - too general
  - Various ubiquitin-related terms
- Reality: UBA7 specifically activates ISG15, not ubiquitin, in mammals
- **Impact**: Generic terms obscure specific function

### 3. Substrate Specificity Transfer

**The Problem**: Specific substrate preference may differ between orthologs.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0004622` (phosphatidylcholine lysophospholipase activity)
- Source: S. cerevisiae ortholog with characterized PC specificity
- Reality: Enzyme has broad specificity for ALL glycerophospholipids
- **Impact**: Over-specific annotation from ortholog doesn't capture full activity

### 4. Neo-Functionalization: Opposite Function in Subfamily

**The Problem**: When a subfamily undergoes neo-functionalization to catalyze the **opposite reaction**, IBA from the family root propagates the wrong function.

**Example - Cds1 (M. tuberculosis, V. cholerae) - PTHR10314 SF135**:
- IBA annotation: `GO:0019344` (cysteine biosynthetic process)
- Source: Root node (PTN000034104) of PTHR10314 family
- Reality: Cds1 catalyzes cysteine **CATABOLISM** (EC 4.4.1.1), the exact opposite!
- **Impact**: IBA propagates biosynthesis when the enzyme actually degrades cysteine to H2S + pyruvate

**Why this is severe**: The annotation isn't just wrong - it's **directionally opposite**. The enzyme produces H2S from cysteine degradation; the annotation says it synthesizes cysteine.

**Root Cause Analysis**:
| Evidence | SF135 (Cds1) | SF194/SF162 (Synthases) |
|----------|--------------|-------------------------|
| EC Number | **4.4.1.1** (lyase) | 2.5.1.47 (transferase) |
| Reaction | L-Cys → H2S + pyruvate | O-Ac-Ser + H2S → L-Cys |
| Branch length | **0.528** (longest) | 0.402-0.458 |
| Seq identity to synthases | **~24%** | 40-43% between each other |
| Active site motif | **ASSGST** | PTSGNTG |

The subfamily SF135 shares only 24% identity with synthases - less than synthases share with each other (43%). The longest branch length indicates maximum divergence and neo-functionalization.

### 5. Secondary Activity Promotion

**The Problem**: Non-core activities from well-characterized orthologs promoted to uncharacterized proteins.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0047372` (monoacylglycerol lipase activity)
- This is likely substrate promiscuity, not core function
- **Action**: KEEP_AS_NON_CORE rather than ACCEPT

### 6. Organism/Tissue Context Transfer

**The Problem**: Annotations derived from organism-specific experimental systems carry that context to orthologs where it doesn't apply.

**Example - RIMBP2 (human)**:
- IBA annotation: `GO:0007274` (neuromuscular synaptic transmission)
- Source: Drosophila ortholog (FB:FBgn0262483) where NMJ is the primary synapse model
- Reality: Human RIMBP2 functions mainly at CNS synapses (hippocampal, auditory)
- **Impact**: Term implies NMJ function when actual function is at central synapses
- **Root cause**: IBA quality limited by organism-specific biases in source annotations

## Featured Examples

### Epe1 - Pseudo-Demethylase

**Species**: pombe
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0032452 histone demethylase activity | Pseudo-enzyme - no activity | REMOVE |
| GO:0006338 chromatin remodeling | Too broad | MODIFY |
| GO:0006357 regulation of transcription by RNA pol II | Valid | ACCEPT |
| GO:0003712 transcription coregulator activity | Valid | ACCEPT |

**Lesson**: IBA can propagate enzymatic activity to pseudo-enzymes that retain the domain fold but lack catalytic function.

### UBA7 - ISG15-Specific E1

**Species**: human
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0005737 cytoplasm | Correct | ACCEPT |
| GO:0019782 ISG15 activating enzyme activity | Correct, specific | ACCEPT |
| GO:0032020 ISG15-protein conjugation | Correct | ACCEPT |
| GO:0045087 innate immune response | Correct | ACCEPT |
| GO:0006974 DNA damage response | Correct | ACCEPT |

**Note**: UBA7 IBA annotations are largely correct because the ISGylation pathway is conserved.

### LPL1 - Phospholipase Specificity

**Species**: CANAL
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0006629 lipid metabolic process | Correct | ACCEPT |
| GO:0004622 PC lysophospholipase activity | Too narrow | MODIFY |
| GO:0005811 lipid droplet | Correct | ACCEPT |
| GO:0047372 monoacylglycerol lipase activity | Secondary activity | KEEP_AS_NON_CORE |

### RIMBP2 - Context-Specific Term Transfer

**Species**: human
**Status**: COMPLETE
**PANTHER Family**: [PTHR14234](../interpro/panther/PTHR14234/) (RIM BINDING PROTEIN-RELATED)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0007274 neuromuscular synaptic transmission | Wrong synapse type context | MODIFY |

**Lesson**: IBA transferred a term specific to *Drosophila* NMJ context to a human gene that functions primarily at CNS synapses. The IBA source (FB:FBgn0262483) is the fly ortholog where neuromuscular junctions are a major experimental system. However, human RIMBP2 functions at hippocampal (mossy fiber, CA3-CA1), auditory ribbon, and other central synapses - not primarily at neuromuscular junctions. This illustrates how IBA can propagate organism-specific or tissue-specific contexts that don't apply to the target species.

**Root Cause Analysis**: This is a case where **IBAs are only as good as the manual annotations on orthologs**. The Drosophila RIMBP ortholog is well-characterized at the NMJ because that's the major accessible synapse type in flies. When this annotation gets transferred to human via phylogenetic inference, it carries the fly-specific context with it.

**Family-Level Context**: The [PANTHER family analysis](../interpro/panther/PTHR14234/PTHR14234-deep-research-falcon.md) reveals additional IBA quality concerns:
- The representative structure (PDB 4z8a) is from *Drosophila* RIM-BP bound to Cacophony (fly NMJ Ca2+ channel)
- The family contains **functionally divergent subfamilies**:
  - RIMBP1/2 (SF18, SF20): Neuronal synaptic scaffolds
  - RIMBP3 (SF21): **Non-synaptic** - testis-specific, spermiogenesis/manchette function
- The family research explicitly warns: "Avoid propagating 'regulation of neurotransmitter release' to RIMBP3 paralogs"
- This demonstrates that IBA issues can affect entire subfamilies, not just individual genes

### Cds1 (PTHR10314) - Neo-Functionalization (Opposite Reaction)

**Species**: MYCTU (Mycobacterium tuberculosis), VIBCH (Vibrio cholerae)
**Status**: COMPLETE
**Family**: PTHR10314 (Cysteine Synthase/Cystathionine Beta-Synthase)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0019344 cysteine biosynthetic process | **Opposite function** - enzyme is catabolic | REMOVE |

**Lesson**: This is the most severe type of IBA error - the annotation isn't merely imprecise, it's **directionally wrong**. Cds1 (subfamily SF135) catalyzes cysteine **degradation** (EC 4.4.1.1), producing H2S + pyruvate from L-cysteine. The IBA annotation GO:0019344 says it participates in cysteine **biosynthesis** - the exact opposite reaction!

**Root Cause Analysis**:
1. GO:0019344 is annotated at the PANTHER family root node (PTN000034104)
2. Root annotation propagates to ALL descendants, including subfamily SF135 (Cds1)
3. SF135 underwent **neo-functionalization**: same fold, opposite reaction
4. Evidence of neo-functionalization:
   - Longest branch length (0.528) from root = most divergent
   - Different EC class: 4.4.1.1 (lyase/catabolism) vs 2.5.1.47 (transferase/biosynthesis)
   - Only 24% sequence identity with synthases (synthases share 40-43% with each other)
   - Distinct active site motif: ASSGST (Cds1) vs PTSGNTG (synthases)

**Experimental Evidence**:
- PMID:34439535 (M. tuberculosis): Cds1 produces H2S, pyruvate from cysteine; KM=11.26 mM, kcat=78.71/s
- PMID:34283874 (V. cholerae): VC1061/cds1 is principal enzyme for cysteine-derived H2S production

**Recommendation for PANTHER Curators**:
- Remove GO:0019344 propagation to SF135
- Add SF135-specific annotations: GO:0019450 (L-cysteine catabolic process to pyruvate), GO:0080146 (L-cysteine desulfhydrase activity)

See detailed family analysis: `interpro/panther/PTHR10314/PTHR10314-notes.md`

## Genes with IBA Issues

| Gene | Species | IBA Issue Type | Severity | Status |
|------|---------|----------------|----------|--------|
| Epe1 | pombe | Pseudo-enzyme propagation | HIGH | COMPLETE |
| cds1 | MYCTU, VIBCH | **Neo-functionalization (opposite reaction)** | **CRITICAL** | COMPLETE |
| LPL1 | CANAL | Substrate specificity | MEDIUM | COMPLETE |
| UBA7 | human | Generic vs specific terms | LOW | COMPLETE |
| RIMBP2 | human | Context-specific term transfer | MEDIUM | COMPLETE |

## Recommendations for IBA Curation

1. **Flag pseudo-enzyme candidates**: Proteins with enzyme domains but missing catalytic residues
2. **Flag neo-functionalized subfamilies**: Long branch lengths and different EC numbers indicate potential opposite function
3. **Validate substrate specificity**: Don't assume identical specificity across orthologs
4. **Distinguish core vs. secondary**: Mark promiscuous activities as non-core
5. **Prefer specific terms**: Replace generic IBA with specific terms when evidence exists
6. **Check for functional divergence**: Especially in rapidly evolving families
7. **Consider organism-specific biases**: Source annotations may reflect experimental systems (e.g., NMJ in flies) that don't apply to target species
8. **Validate annotations at family root**: Root-level annotations propagate everywhere - ensure they're truly universal to ALL subfamilies

## Quality Indicators

**Signs of problematic IBA**:
- Enzymatic activity for proteins with degenerate active sites
- **Long branch lengths from family root** (indicates divergence/neo-functionalization)
- **Different EC numbers between subfamilies** (may catalyze opposite reactions!)
- Generic terms when specific function is known
- Process annotations that don't match organism biology
- Multiple conflicting IBA annotations

**Signs of reliable IBA**:
- Core metabolic enzymes with conserved mechanism
- Well-defined pathways with conserved components
- Structural proteins with conserved function
- Process/location terms that are organism-agnostic
- **Subfamilies with high sequence identity and same EC number**

---

# STATUS

## Analyzed Genes
- [x] pombe/Epe1 - Pseudo-enzyme propagation (HIGH severity)
- [x] MYCTU/cds1 - Neo-functionalization opposite reaction (CRITICAL severity)
- [x] VIBCH/cds1 - Neo-functionalization opposite reaction (CRITICAL severity)
- [x] CANAL/LPL1 - Substrate specificity (MEDIUM severity)
- [x] human/UBA7 - Generic vs specific terms (LOW severity)
- [x] human/RIMBP2 - Organism/tissue context transfer (MEDIUM severity)

## Patterns Identified
- [x] Pseudo-enzyme IBA propagation
- [x] **Neo-functionalization: opposite reaction in subfamily** (NEW - most severe type)
- [x] Substrate specificity over-transfer
- [x] Secondary activity promotion
- [x] Organism/tissue context transfer

Last updated: 2026-01-26

# NOTES

## 2026-01-26

**Added PTHR10314/cds1 - Neo-Functionalization (Opposite Reaction) Pattern**

This is arguably the most informative example for the IBA quality review project. The cds1 case (subfamily SF135 of PTHR10314) demonstrates the **most severe type of IBA error**: annotation of the exact **opposite biological function**.

Key findings from family analysis:
- GO:0019344 (cysteine biosynthetic process) is annotated at family root and propagates to all descendants
- Subfamily SF135 (Cds1/desulfhydrases) underwent neo-functionalization: same fold, opposite reaction
- Cds1 catalyzes cysteine **CATABOLISM** (EC 4.4.1.1): L-Cys → H2S + pyruvate + NH3
- IBA says cysteine **BIOSYNTHESIS** - directionally wrong!

Evidence of neo-functionalization in SF135:
1. Longest branch length (0.528) from root = most sequence divergence
2. Different EC class: 4.4.1.1 vs 2.5.1.47
3. Only 24% identity with synthases (synthases share 43% with each other)
4. Different active site motif: ASSGST vs PTSGNTG

Detailed analysis in: `interpro/panther/PTHR10314/PTHR10314-notes.md`

This pattern represents a new category beyond the previously identified issues:
- Pseudo-enzyme (Epe1): function lost, but domain retained
- Neo-functionalization (cds1): function **inverted**, same fold

Both reviewed genes (MYCTU/cds1, VIBCH/cds1) have comprehensive reviews with experimental evidence from PMID:34439535 and PMID:34283874.

---

**Added RIMBP2 - Organism Context Transfer Pattern**

RIMBP2 illustrates a subtle but important IBA quality issue: **context-specific term transfer**. The IBA annotation `GO:0007274` (neuromuscular synaptic transmission) was transferred from the Drosophila ortholog (FB:FBgn0262483), where NMJ is a primary experimental system for studying synaptic function.

However, human RIMBP2 functions primarily at:
- Hippocampal mossy fiber synapses
- CA3-CA1 synapses
- Auditory ribbon synapses

Not at neuromuscular junctions. The annotation isn't "wrong" in the sense that RIMBP2 is involved in synaptic transmission, but it's misleading because it implies NMJ function.

**Key Insight**: IBAs are only as good as the manual annotations on orthologs. When source organisms have biased annotation (e.g., flies are heavily annotated at NMJ because that's the accessible synapse type), this bias propagates through phylogenetic inference.

**Family-Level Analysis (PTHR14234)**: The PANTHER family analysis provides additional context:
- Representative structure is *Drosophila* RIM-BP (PDB 4z8a) - fly-centric
- Family includes RIMBP3 (SF21) which is **non-synaptic** (testis/spermiogenesis)
- Family research warns: "Avoid propagating 'regulation of neurotransmitter release' to RIMBP3 paralogs"
- This shows IBA issues can affect entire subfamilies when root annotations don't apply universally

See: `interpro/panther/PTHR14234/PTHR14234-deep-research-falcon.md`

**Recommendation**: For synaptic genes, consider whether the specific synapse type in the term (NMJ, CNS, etc.) actually applies to the target species, or whether a more general synaptic transmission term would be more accurate.

## 2026-01-22

**Project Creation**

Documented IBA quality issues discovered through AI review.

**Key Finding**: The most severe IBA quality issue is **pseudo-enzyme propagation** - transferring enzymatic activity to proteins that have lost catalytic function while retaining the domain fold.

**Epe1 Case Study**:
- JmjC domain → IBA from active demethylases
- Epe1 has HVD motif (not HXD), missing Fe(II) coordination
- Mass spec assays: NO demethylation detected
- H297A catalytic mutant: retains anti-silencing function
- **Conclusion**: All enzymatic IBA annotations should be REMOVE

**Recommendation**: Develop automated pipeline to flag IBA annotations for proteins with degenerate active site motifs.
