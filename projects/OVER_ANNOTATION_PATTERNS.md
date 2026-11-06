---
title: "Over-Annotation Patterns Project"
maturity: MATURE
tags: [PIPELINE, FLAGSHIP, EVALUATION]
species: [human, SCHPO, CANAL, PSEAE, STRCO, SACEN, HORSE]
genes: [PHYKPL, UBA7, Epe1, LPL1, pqsC, pqsB, actI-ORF1, actI-ORF2, eryCII, AARS2, HORSE/DARS2]
manifest:
  slides:
    - href: OVER_ANNOTATION_PATTERNS/slides/OVER_ANNOTATION_PATTERNS-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/MrmXAmcMnpxL43743j1ogb
      title: Project brief
---

# Over-Annotation Patterns Project

**Bottom line:** many GO annotations are technically defensible but tell a reader almost
nothing, or assert an activity the protein does not have, because they come from
high-throughput interactome screens, domain signatures, broad keyword mappings or
over-generalised family propagation. We catalogued the recurring shapes of this
over-annotation that surfaced during gene review, nine categories in all, each tied to
worked examples in real reviews. We did this so that curators and pipeline authors can
recognise a pattern once rather than rediscovering it gene by gene; the catalogue was
first presented at the GO Consortium meeting in October 2025. Eleven exemplar reviews are
complete (human PHYKPL, UBA7 and AARS2, fission yeast Epe1, *Candida* LPL1,
horse <gene species="HORSE" symbol="DARS2">DARS2</gene>,
and five biosynthetic-cluster enzymes: pqsC, pqsB, actI-ORF1, actI-ORF2, eryCII), and their
recorded actions match the patterns: all ten generic `protein binding` IPI rows on
PHYKPL and UBA7 are REMOVE, and Epe1's electronically inferred JmjC-domain
demethylase, oxidoreductase and dioxygenase rows are REMOVE, while its two
experimental IDA/EXP H3K9 demethylase rows and its metal ion binding row are
UNDECIDED. The catalogue is qualitative; it does not yet measure how
often each pattern occurs across the repository.

## Overview

This project documents systematic patterns of over-annotation discovered through AI-assisted gene review. Over-annotation occurs when GO terms are assigned that are technically correct but provide minimal functional insight, or when terms are too broad/generic to be useful for understanding gene function.

These patterns emerge from multiple sources:
- High-throughput screens that generate generic annotations
- Domain-based IEA annotations that don't reflect actual activity
- IBA annotations that over-generalize from distantly related proteins
- Keyword-based mappings that assign parent terms unnecessarily

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Categories of Over-Annotation

### 1. Generic "Protein Binding" (GO:0005515)

**The Problem**: High-throughput interactome studies generate thousands of IPI annotations to "protein binding" that provide no functional information.

**Examples from Reviews**:
- **PHYKPL**: 4 protein binding annotations from HTP screens showing interactions with POT1, USO1, VAC14, LNX2 - none related to its metabolic function
- **UBA7**: 6 protein binding annotations from interactome studies - UBA7 obviously binds proteins (ISG15, UBE2L6) but the generic term adds nothing
- **Epe1**: Protein binding IPI row (partner Cdt2) when ubiquitin protein ligase binding (GO:0031625) is more informative

**Recommended Action**: REMOVE generic protein binding when more specific functional annotations exist or when interactions are from HTP screens without validation.

### 2. Overly Broad Enzymatic Terms

**The Problem**: Generic enzymatic terms (hydrolase activity, oxidoreductase activity, ligase activity) assigned when more specific terms exist.

**Examples**:
- **LPL1**: `GO:0016787` (hydrolase activity) when `GO:0102545` (phospholipase B activity) is more specific
- **Epe1**: `GO:0016491` (oxidoreductase activity) assigned although no catalytic activity has been detected and the Fe(II) triad is non-canonical
- **UBA7**: `GO:0016874` (ligase activity) when `GO:0019782` (ISG15 activating enzyme activity) is specific

**Recommended Action**: REMOVE or MODIFY to more specific child terms.

### 3. Domain-Based Predictions Without Validation

**The Problem**: IEA annotations from domain presence (InterPro, Pfam) that don't reflect actual biochemical activity.

**Examples**:
- **Epe1**: JmjC domain → histone demethylase activity, dioxygenase activity (REMOVE - no activity detected, non-canonical Fe(II) triad, although the divergent Tyr370 is required for function); metal ion binding left UNDECIDED (two of three iron ligands retained, binding unmeasured)
- **PHYKPL**: Aminotransferase domain → transaminase activity (INCORRECT - functions as phospho-lyase)

**Recommended Action**: REMOVE when biochemical evidence contradicts domain prediction.

### 4. Indirect Downstream Process Annotations

**The Problem**: Genes annotated to broad biological processes based on indirect effects rather than direct function.

**Pattern**: Gene affects X → X affects Y → Gene annotated to Y

**Examples**:
- Kinase that phosphorylates one transcription factor annotated to "regulation of cell proliferation"
- Enzyme in metabolic pathway annotated to disease process it indirectly affects

**Recommended Action**: Use more proximal process terms; annotate to direct function, not downstream consequences.

### 5. Duplicate IEA Annotations

**The Problem**: Multiple automated pipelines annotate the same term, creating redundancy.

**Examples**:
- **GND1**: Same term (`GO:0004616`) from both IBA and IEA sources
- **UBA7**: Cytoplasm annotation from IBA, IEA, and IDA sources

**Note**: This is less problematic as multiple evidence codes can provide confidence, but creates clutter.

### 6. Predicted Localization Conflicts

**The Problem**: Automated transmembrane predictions leading to incorrect membrane annotations.

**Examples**:
- **LPL1**: `GO:0016020` (membrane) from transmembrane prediction, but protein localizes to lipid droplets (monolayer, not bilayer membrane)

**Recommended Action**: REMOVE when experimental localization data contradicts prediction.

### 7. Fold-Based Pathway Mis-Propagation (wrong product class)

**The Problem**: A catalytic-domain signature shared between two pathways propagates the
**wrong pathway's** terms. The β-ketoacyl-synthase (FabH/KAS-III) fold is common to fatty-acid
and polyketide synthases, so InterPro/IEA assigns fatty-acid terms to polyketide/secondary-
metabolite enzymes.

**Examples (BGC project)**:
- **pqsC** (PSEAE): `GO:0006633` fatty acid biosynthetic process and `GO:0004315` 3-oxoacyl-ACP
  synthase → the enzyme makes a quinolone QS signal (octanoate is a *substrate*, not the product).
- **actI-ORF1** (STRCO): `GO:0006633` / `GO:0030497` fatty acid elongation → it is a **polyketide**
  ketosynthase (`GO:0016218`); MODIFY to `GO:1901112` actinorhodin biosynthetic process.

### 8. Catalytic Function Assigned to Non-Catalytic Complex Subunits

**The Problem**: Domain signatures assign a catalytic MF to every subunit of an obligate
heterodimer, including the partner that lacks the active site. Per GO guidelines the activity
belongs on the catalytic member (`enables`); the partner takes `contributes_to` at most.

**Examples (BGC project)**: **pqsB** (PqsBC; catalytic Cys/His in PqsC), **actI-ORF2/CLF**
(no active site), **eryCII** (heme-less P450 activator). See `PSEUDOENZYMES.md` and
`PROTEIN_COMPLEX_FUNCTIONS.md`.

### 9. Specificity That Restates Another Aspect (cross-aspect redundancy)

**The Problem**: a term is more specific than its parent, but the only thing its
specificity adds is a fact already asserted in a *different* GO aspect. "Prefer the more
specific term" then pushes a curator or reviewer toward a term that carries no extra
information, and in the worst case toward marking the correct parent as an
over-annotation.

The worked case is tRNA charging. GO had 42 biological-process terms naming the amino
acid being charged: `GO:0006419` alanyl-tRNA aminoacylation and its 19 siblings, their 20
mitochondrial twins, and two compartment-qualified variants. Each paired 1:1 with an
existing molecular function that already carries the amino acid, `GO:0004813`
alanine-tRNA ligase activity and so on, and each obsoletion comment says so in those
terms: the process "restates an existing molecular function ... and adds nothing beyond
it". Annotation is directed to the MF plus the compartment-level process, and every one of
the 42 carries a `replaced_by`: 40 name that compartment-level process, and the two
compartment-qualified cytosolic variants (`GO:0061475`, `GO:1990762`) name `GO:7770128`
tRNA aminoacylation for cytosolic protein translation instead.

A 43rd term went in the same batch for a different reason, and is not an instance of this
pattern: `GO:0070681` glutaminyl-tRNAGln biosynthesis via transamidation was obsoleted as
"a specific pathway variant, which is out of scope for GO", its MF counterpart is
`GO:0050567` rather than a Gln-tRNA ligase, and its comment gives `consider` targets
instead of a `replaced_by` because "no single term is a safe automatic substitution". See
`AMINO_ACID_ACTIVATION_OBSOLETION.md`.

**The diagnostic**: ask what the specific term asserts that its parent plus the gene's
other annotations do not. If the answer is "the amino acid", "the substrate" or "the
product", and an MF row already names it, the specificity is redundant and the parent is
the right term.

**What this is not**: an argument against specificity in general. Compartment
specificity survived the same obsoletion untouched — `GO:0070127` tRNA aminoacylation for
mitochondrial protein translation is still live and still an `is_a` child of `GO:0006418`,
because no MF term says where the reaction happens. A mitochondrial synthetase should
still be refined from `GO:0006418` to `GO:0070127`. The test is whether the added content
is already carried elsewhere, not how deep the term sits.

**Examples**: four reviews made the inverted judgement explicitly, and all four have
since been migrated. `PSEPK/glnS` and `PSEPK/gltX` marked `GO:0006418` over-annotated
because the amino-acid-specific child "already captures" the process; `PSEPK/serS`
modified it to `GO:0006434`; `human/AARS1` modified it to `GO:0006419`. Each now accepts
`GO:0006418`, with it in `core_functions`. This was a minority judgement rather than a
house style — most synthetase reviews, `PSEPK/valS` among them, accepted `GO:0006418` all
along — which is what makes the pattern worth naming: it is available to anyone applying
"prefer the more specific term", not a habit of one curation batch.

`human/AARS2` and `HORSE/DARS2` are the same pattern one level down: both proposed an
amino-acid-specific *mitochondrial* child (`GO:0070143`, `GO:0070146`), now obsolete, and
both resolve to `GO:0070127` with specificity on `GO:0004813` / `GO:0004815`.

## Genes Exemplifying Patterns

| Gene | Species | Over-Annotation Pattern | Status |
|------|---------|------------------------|--------|
| PHYKPL | human | Protein binding, transaminase (wrong mechanism) | COMPLETE |
| UBA7 | human | Protein binding, generic ligase | COMPLETE |
| Epe1 | pombe | Domain-based demethylase (pseudo-enzyme) | COMPLETE |
| LPL1 | CANAL | Generic hydrolase, membrane localization | COMPLETE |
| pqsC | PSEAE | Fatty-acid synthase terms (KAS-III fold) on a quinolone synthase | COMPLETE |
| actI-ORF1 | STRCO | Fatty-acid biosynthesis/elongation terms on a polyketide synthase | COMPLETE |
| pqsB | PSEAE | Catalytic acyltransferase MF on the non-catalytic subunit | COMPLETE |
| actI-ORF2 | STRCO | Catalytic acyltransferase MF on the chain-length factor (no active site) | COMPLETE |
| eryCII | SACEN | Full P450 MF/cofactor set on a heme-less pseudoenzyme | COMPLETE |
| AARS2 | human | Amino-acid-specific BP restating the paired MF (obsoleted upstream) | COMPLETE |
| HORSE/DARS2 | HORSE | Amino-acid-specific BP restating the paired MF (obsoleted upstream) | COMPLETE |

## Recommended Curation Principles

1. **Specificity over breadth, with one exception**: prefer the most specific accurate
   term, unless its only added content is already asserted in another aspect (pattern 9)
2. **Remove uninformative annotations**: Generic protein binding from HTP screens
3. **Validate domain predictions**: Especially for enzymatic activity
4. **Distinguish direct vs. indirect**: Annotate to proximal function
5. **Consider pseudo-enzymes**: Domains don't guarantee activity

## Impact on Annotation Quality

These over-annotation patterns:
- Dilute the signal from informative annotations
- Create false impressions of functional understanding
- Complicate enrichment analyses
- Propagate through IBA to other species

---

# STATUS

## Documented Patterns
- [x] Generic protein binding
- [x] Overly broad enzymatic terms
- [x] Domain-based predictions without validation
- [x] Indirect downstream processes
- [x] Predicted localization conflicts

## Genes Analyzed
- [x] human/PHYKPL - transaminase vs phospho-lyase
- [x] human/UBA7 - protein binding from HTP, generic ligase
- [x] pombe/Epe1 - pseudo-demethylase
- [x] CANAL/LPL1 - hydrolase, membrane prediction

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Documented systematic over-annotation patterns discovered through AI review.

**Key Insight**: The most common over-annotation is generic "protein binding" (GO:0005515) from high-throughput interactome studies. These annotations:
- Provide no functional information
- Often represent false positives or indirect interactions
- Should be removed when specific functional annotations exist

**Curation Recommendation**: Consider flagging or filtering HTP-derived protein binding annotations during curation review.
